"""
Script to zip directories as CBZ files and delete the original directories.

Made by @n0nuser - 06/05/2024
"""

import os
import pathlib
import shutil
import zipfile
import unicodedata
from typing import List


def get_directories() -> List[str]:
    """
    Get a list of directories in the current working directory.

    Returns:
        List[str]: A list of directory names.
    """
    filepath = pathlib.Path(__file__).resolve().parent
    return [d for d in os.listdir(filepath) if os.path.isdir(d)]


def strip_non_latin(text: str) -> str:
    """
    Remove non-Latin characters from a given text.

    Args:
        text (str): The input text.

    Returns:
        str: The input text with non-Latin characters removed.
    """
    return "".join(c for c in text if unicodedata.category(c)[0] == "L")


def zip_directory(directory: str) -> str:
    """
    Zip a directory.

    Args:
        directory (str): The directory to zip.

    Returns:
        str: The name of the zip file created.
    """
    sanitized_directory = strip_non_latin(directory)
    zip_filename = sanitized_directory + ".cbz"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))
    return zip_filename


def delete_directory(directory: str) -> None:
    """
    Delete a directory.

    Args:
        directory (str): The directory to delete.
    """
    shutil.rmtree(directory)
    print(f"Directory '{directory}' deleted.")


def zip_and_delete_directories() -> None:
    """
    Zip and delete all directories in the current working directory.
    """
    directories = get_directories()
    for directory in directories:
        zip_filename = zip_directory(directory)
        print(f"Directory '{directory}' zipped to '{zip_filename}'.")
        delete_directory(directory)

    print("All directories zipped and deleted.")


if __name__ == "__main__":
    zip_and_delete_directories()
