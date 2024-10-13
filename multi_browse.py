"""
Open multiple browser tabs displaying results of a Google Search query

@author: Amtr4x
"""

import argparse


def main():
    """Main program execution"""

    parser = argparse.ArgumentParser(
        description="Open multiple browser tabs from your Google query."
    )
    parser.add_argument(
        "query",
        type=str,
        help="The Google search query you want to perform.",
    )
    parser.add_argument(
        "-tl",
        type=int,
        help="Limit the maximum amount of tabs to be opened. Default = 3",
        default=3,
        metavar="int",
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()
