from queue import Queue
import argparse
import socket
import threading
import platform
import subprocess

#######################################################
# n0nuser ~ https://github.com/n0nuser/Python-scripts #
#######################################################

# https://www.neuralnine.com/threaded-port-scanner-in-python/
def portscan(target,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# https://www.neuralnine.com/threaded-port-scanner-in-python/
def worker(queue, open_ports, target, verbose):
    while not queue.empty():
        port = queue.get()
        if portscan(target, port):
            if verbose == 1 or verbose == 2:
                print("Port {} is open!".format(port))
            open_ports.append(port)
        else:
            if verbose == 2:
                print("Port {} is closed!".format(port))

# https://www.neuralnine.com/threaded-port-scanner-in-python/
def get_ports(mode, queue):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 65535):
            queue.put(port)
    elif mode == 3:
        ports = [21, 22, 23, 25, 80, 81, 110, 135, 139, 389, 443, 445, 873, 1433, 1434, 1521, 2433, 3306, 3307, 3389, 5800, 5900, 8080, 22222, 22022, 27017, 28017]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (separate by blank):")
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)

# https://www.neuralnine.com/threaded-port-scanner-in-python/
def run_scanner(threads, mode, target, verbose):
    queue = Queue()
    get_ports(mode, queue)
    open_ports = []
    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker, args=(queue, open_ports, target, verbose))
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open ports are:", open_ports)

# https://stackoverflow.com/a/32684938
def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def args():
    desc = "Multithreaded Port Scanner ~ n0nuser (https://github.com/n0nuser/Python-scripts)"
    hostDesc = "IP or host to scan."
    threadDesc = "Number of threads used. Default is 20."
    modeDesc = "Mode 1: Ports 1-1024\nMode 2: Ports 1-65535\nMode 3: Most Common Ports (Faster than mode 1 and 2)\nMode 4: Manual Mode"
    verbDesc = "Detailed Info. Mode 0 is None, Mode 1 Open Ports and Mode 2 Open/Closed Ports"

    parser = argparse.ArgumentParser(description=desc,formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-u", "--target", help=hostDesc, type=str, dest="target", required=True)
    parser.add_argument("-t", "--threads", help=threadDesc, type=int, dest="threads")
    parser.add_argument("-m", "--mode", help=modeDesc, type=int, dest="mode", choices=[1, 2, 3, 4])
    parser.add_argument("-v", "--verbose", help=verbDesc, type=int, dest="verbose", choices=[0, 1, 2])

    target = parser.parse_args().target
    threads = parser.parse_args().threads
    mode = parser.parse_args().mode
    verbose = parser.parse_args().verbose
    return target, threads, mode, verbose

def main():
    target, threads, mode, verbose = args()

    if threads is None:
        threads = 20
    if mode is None:
        mode = 1
    if verbose is None:
        verbose = 0

    if ping(target) is False:
        print("Can't reach that host.")
        exit()
    target = socket.gethostbyname(target)
    print("Target: " + target)
    run_scanner(threads, mode, target, verbose)


main()