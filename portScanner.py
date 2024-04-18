import argparse
import socket
import threading
from queue import Queue
import platform
import subprocess
from typing import List, Tuple


# Author: n0nuser - Pablo Jesús González Rubio
# Description: A simple multithreaded port scanner.
# Requirements: None


def portscan(target: str, port: int) -> bool:
    """Attempts to connect to a specified port on the target host.

    Args:
        target: The target host IP address or hostname.
        port: The target port to scan.

    Returns:
        A boolean value indicating if the port is open.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((target, port))
            return True
    except:
        return False


def worker(queue: Queue, open_ports: List[int], target: str, verbose: int) -> None:
    """A worker function that scans ports taken from the queue.

    Args:
        queue: A queue containing ports to be scanned.
        open_ports: A list to append open ports to.
        target: The target host IP address or hostname.
        verbose: Verbose level (0, 1, or 2) to control output detail.
    """
    while not queue.empty():
        port = queue.get()
        if portscan(target, port):
            if verbose >= 1:
                print(f"Port {port} is open!")
            open_ports.append(port)
        elif verbose == 2:
            print(f"Port {port} is closed!")


def get_ports(mode: int, queue: Queue) -> None:
    """Populates the queue with ports based on the selected mode.

    Args:
        mode: The scanning mode.
        queue: The queue to populate with ports.
    """
    if mode == 1:
        ports = range(1, 1024)
    elif mode == 2:
        ports = range(1, 65535)
    elif mode == 3:
        ports = [
            21,
            22,
            23,
            25,
            80,
            81,
            110,
            135,
            139,
            389,
            443,
            445,
            873,
            1433,
            1434,
            1521,
            2433,
            3306,
            3307,
            3389,
            5800,
            5900,
            8080,
            22222,
            22022,
            27017,
            28017,
        ]
    elif mode == 4:
        ports_input = input("Enter your ports (separate by blank): ")
        ports = map(int, ports_input.split())

    for port in ports:
        queue.put(port)


def run_scanner(threads: int, mode: int, target: str, verbose: int) -> None:
    """Runs the port scanner using multiple threads.

    Args:
        threads: The number of threads to use for scanning.
        mode: The scanning mode.
        target: The target host IP address or hostname.
        verbose: Verbose level to control output.
    """
    queue = Queue()
    get_ports(mode, queue)
    open_ports: List[int] = []
    thread_list: List[threading.Thread] = []

    for _ in range(threads):
        thread = threading.Thread(target=worker, args=(queue, open_ports, target, verbose))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)


def ping(host: str) -> bool:
    """Pings a host to check its availability.

    Args:
        host: The target host to ping.

    Returns:
        A boolean value indicating if the host is reachable.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0


def parse_arguments() -> Tuple[str, int, int, int]:
    """Parses command-line arguments.

    Returns:
        A tuple containing the target, number of threads, mode, and verbose level.
    """
    parser = argparse.ArgumentParser(
        description="Multithreaded Port Scanner", formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-u", "--target", required=True, type=str, help="IP or host to scan.")
    parser.add_argument(
        "-t", "--threads", default=20, type=int, help="Number of threads used. Default is 20."
    )
    parser.add_argument(
        "-m",
        "--mode",
        choices=[1, 2, 3, 4],
        type=int,
        help="Mode 1: Ports 1-1024\n"
        "Mode 2: Ports 1-65535\n"
        "Mode 3: Most Common Ports\n"
        "Mode 4: Manual Mode",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        choices=[0, 1, 2],
        default=0,
        type=int,
        help="Verbose output: 0=None, 1=Open Ports, 2=Open/Closed Ports",
    )

    args = parser.parse_args()
    return args.target, args.threads, args.mode, args.verbose


def main() -> None:
    """Main function to run the port scanner."""
    target, threads, mode, verbose = parse_arguments()

    if not ping(target):
        print("Can't reach that host.")
        exit()

    target_ip = socket.gethostbyname(target)
    print("Target: " + target_ip)
    run_scanner(threads, mode, target_ip, verbose)


if __name__ == "__main__":
    main()
