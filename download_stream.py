#!/usr/bin/env python3

import argparse
import os
import sys
from shutil import which

# Author: n0nuser - Pablo Jesús González Rubio
# Description: Downloads Stream Video with ".m3u8" file and transcodes it to mp4
# Requirements: VLC installed


def check_vlc_installed() -> None:
    """
    Ensure VLC is installed on the system.

    Exits the script with an error message if VLC is not found.
    """
    if which("vlc") is None:
        sys.exit("VLC is not installed. Please install it with: sudo apt install vlc -y")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        An argparse.Namespace object containing the input and output arguments.
    """
    parser = argparse.ArgumentParser(
        description="Download and transcode stream video from .m3u8 to .mp4",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example: python3 downloadStream.py -i https://mywebsite.ext/myfile.m3u8 -o myfile",
    )
    parser.add_argument("-i", "--input", type=str, required=True, help="Link to the .m3u8 stream")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="Output filename for the .mp4 (without extension)",
    )
    return parser.parse_args()


def validate_input_url(input_url: str) -> None:
    """
    Validate the input URL to ensure it is a .m3u8 file.

    Args:
        input_url: The URL to validate.

    Exits the script with an error message if the input URL does not end with '.m3u8'.
    """
    if not input_url.endswith(".m3u8"):
        sys.exit("Input URL must be a .m3u8 file.")


def download_and_transcode(stream_url: str, output_file: str) -> None:
    """
    Download the stream and transcode it to an MP4 file.

    Args:
        stream_url: The URL of the .m3u8 stream to download.
        output_file: The desired output filename (without the .mp4 extension).
    """
    command = f"vlc -I dummy --sout '#transcode{{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}}:standard{{mux=mp4,dst=\"{output_file}.mp4\",access=file}}' {stream_url}"
    os.system(command)


def main() -> None:
    """
    Main function to orchestrate the script execution.

    This function performs the following steps:
    - Check if VLC is installed.
    - Parse command line arguments.
    - Validate the input URL.
    - Download the .m3u8 stream and transcode it to MP4.
    """
    check_vlc_installed()
    args = parse_arguments()
    validate_input_url(args.input)
    download_and_transcode(args.input, args.output)


if __name__ == "__main__":
    main()
