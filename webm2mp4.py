#!/usr/bin/env python3
"""
This script converts WEBM video files to MP4 video files using ffmpeg.
"""

# Author: n0nuser - Pablo Jesús González Rubio
# Description: Convert WEBM video files to MP4 video files.
# Requirements: ffmpeg (sudo apt install ffmpeg -y)

import argparse
import subprocess
import sys
from typing import Tuple


def parse_arguments() -> Tuple[str, str]:
    """
    Parses command line arguments for the script.

    Returns:
        Tuple containing input and output file names.

    Raises:
        SystemExit: If the required arguments are not provided or if the output file extension is not .mp4.
    """
    parser = argparse.ArgumentParser(description="Convert WEBM to MP4.")
    parser.add_argument("-i", "--input", help="Name of Input File", required=True, type=str)
    parser.add_argument("-o", "--output", help="Name of Output File", required=True, type=str)

    args = parser.parse_args()

    if not args.output.endswith(".mp4"):
        parser.error("Output file must have a .mp4 extension")

    return args.input, args.output


def check_ffmpeg_installed() -> None:
    """
    Checks if ffmpeg is installed on the system.

    Raises:
        RuntimeError: If ffmpeg is not found.
    """
    try:
        subprocess.run(["which", "ffmpeg"], check=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        raise RuntimeError(
            "ffmpeg is required but not installed. To install it: sudo apt install ffmpeg -y"
        )


def convert_webm_to_mp4(input_file: str, output_file: str) -> None:
    """
    Converts a WEBM video file to MP4 format using ffmpeg.

    Args:
        input_file: The path to the input WEBM file.
        output_file: The path to the output MP4 file.
    """
    try:
        print(f"Converting {input_file} to {output_file}")
        subprocess.run(["ffmpeg", "-i", input_file, output_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {input_file} to {output_file}: {e}")
        sys.exit(1)


def main() -> None:
    """
    Main function to parse arguments, check dependencies, and convert video file format.
    """
    input_file, output_file = parse_arguments()
    try:
        check_ffmpeg_installed()
        convert_webm_to_mp4(input_file, output_file)
    except RuntimeError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
