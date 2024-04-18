#!/usr/bin/env python3
"""
This script converts WEBM video files to MP3 audio files using ffmpeg.
"""

# Author: n0nuser - Pablo Jesús González Rubio
# Description: Convert WEBM video files to MP3 audio files.
# Requirements: ffmpeg (sudo apt install ffmpeg -y)

import argparse
import subprocess
from typing import Tuple

# Constants
FFMPEG_CHECK_CMD = ["which", "ffmpeg"]
CONVERSION_CMD = ["ffmpeg", "-i", None, "-vn", "-ab", "128k", "-ar", "44100", "-y", None]
USAGE_MSG = "usage: webm2mp3.py [-h] [-i INPUT] [-o OUTPUT]"
FFMPEG_NOT_FOUND_MSG = (
    "ffmpeg is required but not found!\n" + "To install it: sudo apt install ffmpeg -y"
)

OUTPUT_FILE_ERROR_MSG = "Output file must have a .mp3 extension!"


def parse_arguments() -> Tuple[str, str]:
    """Parse and validate command-line arguments.

    Returns:
        Tuple[str, str]: A tuple containing the input and output file paths.

    Raises:
        ValueError: If input or output file arguments are missing or invalid.
    """
    parser = argparse.ArgumentParser(description="Convert WEBM to MP3.")
    parser.add_argument("-i", help="Name of Input File", type=str, required=True)
    parser.add_argument("-o", help="Name of Output File", type=str, required=True)
    args = parser.parse_args()

    if not args.o.endswith(".mp3"):
        raise ValueError(OUTPUT_FILE_ERROR_MSG)

    return args.i, args.o


def check_ffmpeg_installed() -> None:
    """Check if ffmpeg is installed.

    Raises:
        RuntimeError: If ffmpeg is not installed.
    """
    result = subprocess.run(FFMPEG_CHECK_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError(FFMPEG_NOT_FOUND_MSG)


def convert_webm_to_mp3(input_file: str, output_file: str) -> None:
    """Convert a WEBM file to an MP3 file using ffmpeg.

    Args:
        input_file (str): Path to the input WEBM file.
        output_file (str): Path to the output MP3 file.
    """
    cmd = list(CONVERSION_CMD)
    cmd[2] = input_file
    cmd[-1] = output_file
    subprocess.run(cmd, check=True)
    print(f"Successfully converted {input_file} to {output_file}.")


def main() -> None:
    """Main function to orchestrate the conversion process."""
    try:
        input_file, output_file = parse_arguments()
        check_ffmpeg_installed()
        convert_webm_to_mp3(input_file, output_file)
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
        exit(1)
    except subprocess.CalledProcessError:
        print("Error during conversion. Please check your input file and try again.")
        exit(1)


if __name__ == "__main__":
    main()
