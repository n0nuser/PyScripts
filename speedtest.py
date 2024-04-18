#!/usr/bin/python3
"""
This module performs a speed test of the current internet connection and
provides the option to save the results to a specified file.
"""

# Author: n0nuser - Pablo Jesús González Rubio
# Description: A simple internet speed test script.
# Requirements: https://pypi.org/project/speedtest-cli/

import argparse
import os
from typing import Optional
import speedtest


def parse_arguments() -> Optional[str]:
    """
    Parses command line arguments to get the output file name, if provided.

    Returns:
        Optional[str]: The name of the output file, or None if not provided.
    """
    desc = "Performs a speed test and optionally saves the results to a file."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("-m", help="Name of Output File", type=str, dest="name")
    return parser.parse_args().name


def print_interface() -> None:
    """
    Prints the interface banner to the console.
    """
    interface = """\033[1;95m
    _____                     ________          __ 
   / ___/____  ___  ___  ____/ /_  __/__  _____/ /_
   \__ \/ __ \/ _ \/ _ \/ __  / / / / _ \/ ___/ __/
  ___/ / /_/ /  __/  __/ /_/ / / / /  __(__  ) /_  
 /____/ .___/\___/\___/\__,_/ /_/  \___/____/\__/  
     /_/                                           
\033[0m
"""
    print(interface)


def perform_speedtest() -> tuple[float, float]:
    """
    Performs the internet connection speed test and returns the download and upload speeds.

    Returns:
        tuple[float, float]: The download and upload speeds in Mbps.
    """
    print(" Please wait \033[5m...\033[0m")
    st = speedtest.Speedtest()
    st.get_best_server()
    download = round(st.download() / 1000000, 4)
    upload = round(st.upload() / 1000000, 4)
    return download, upload


def display_results(download: float, upload: float) -> None:
    """
    Displays the download and upload speeds to the console.

    Args:
        download (float): The download speed in Mbps.
        upload (float): The upload speed in Mbps.
    """
    os.system("clear")
    print_interface()
    print(f"\033[1;96m Download\033[0m: {download} (mb/s)")
    print(f"\033[1;96m Upload\033[0m: {upload} (mb/s)")


def save_results(name: str, download: float, upload: float) -> None:
    """
    Saves the download and upload speeds to a specified file.

    Args:
        name (str): The name of the file to save the results to.
        download (float): The download speed in Mbps.
        upload (float): The upload speed in Mbps.
    """
    with open(name, "w", encoding="utf-8") as f:
        f.write(f"Download: {download} (mb/s)\nUpload: {upload} (mb/s)")


def main() -> None:
    """
    Main function to execute the speed test script.
    """
    name = parse_arguments()
    print_interface()
    download, upload = perform_speedtest()
    display_results(download, upload)
    if name:
        save_results(name, download, upload)


if __name__ == "__main__":
    main()
