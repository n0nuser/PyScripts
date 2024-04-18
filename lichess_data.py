"""
This module is designed to retrieve and display statistics for a Lichess user across different game types.
It uses the `python-lichess` package to interact with the Lichess API.

Usage:
    python script_name.py USERNAME

Where `USERNAME` is the Lichess username of the player whose statistics you wish to retrieve.
"""

# Author: n0nuser - Pablo Jesús González Rubio
# Description: Retrieve and display statistics for a Lichess user.
# Requirements: https://pypi.org/project/python-lichess/

import argparse
from typing import Any, Dict
import lichess.api  # https://pypi.org/project/python-lichess/


def retrieve_stat(user_object: Dict[str, Any], game_type: str, stat: str) -> str:
    """
    Retrieve a specific statistic from the user object.

    Args:
        user_object: The JSON object containing the user's Lichess profile information.
        game_type: The type of game (e.g., "bullet", "blitz") from which to retrieve the statistic.
        stat: The specific statistic to retrieve (e.g., "rating", "games").

    Returns:
        The value of the requested statistic as a string.
    """
    return str(user_object["perfs"][game_type][stat])


def print_game_stats(user_object: Dict[str, Any], game_type: str) -> None:
    """
    Prints statistics for a specific game type.

    Args:
        user_object: The JSON object containing the user's Lichess profile information.
        game_type: The type of game for which to print statistics.
    """
    print(f"\n{game_type.upper()}\n" + "-" * len(game_type))
    stats = ["games", "rating", "rd", "prog"]
    for stat in stats:
        print(f"- {stat.capitalize()}: {retrieve_stat(user_object, game_type, stat)}")


def get_user_stats(username: str) -> None:
    """
    Retrieve and print statistics for all game types for a given user.

    Args:
        username: The Lichess username of the player.
    """
    game_types = ["bullet", "blitz", "rapid", "classical", "puzzle"]

    try:
        user_object = lichess.api.user(username)
        print(f"Retrieving stats for {username}...\n")

        for game_type in game_types:
            print_game_stats(user_object, game_type)

    except lichess.api.ApiHttpError:
        print("Failed to retrieve data. Check your internet connection or the Lichess API status.")
    except lichess.api.ApiNotFoundError:
        print("That user does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main() -> None:
    """
    Main function to parse command-line arguments and retrieve user statistics.
    """
    parser = argparse.ArgumentParser(description="Retrieve and display Lichess user statistics.")
    parser.add_argument("username", help="Lichess username for which to retrieve stats")

    args = parser.parse_args()

    get_user_stats(args.username)


if __name__ == "__main__":
    main()
