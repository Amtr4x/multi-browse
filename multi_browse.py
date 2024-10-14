"""
Open multiple browser tabs displaying results of a Google Search query

@author: Amtr4x
"""

import argparse
import time
import webbrowser
import requests
import sys

import bs4
from bs4 import ResultSet
from bs4 import Tag


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
    query = args.query
    tabs_limit = args.tl
    open_browser_tabs(query, tabs_limit)


def open_browser_tabs(query: str, tabs_limit: int = 3):
    """Open a new tab for every obtained result for the query.

    Args:
        query (str): Google search query to do.
        tabs_limit (int, optional): The maximum amount of tabs will be opened. Defaults to 3.
    """
    link: str = f"https://www.google.com/search?q={query}"
    results_links: list[str] = obtain_links(link)
    tabs_opened: int = 0

    for result in results_links:
        webbrowser.open_new_tab(result)
        tabs_opened += 1
        if tabs_opened >= tabs_limit:
            break
        # this is to avoid performance issues
        time.sleep(1)


def obtain_links(link: str) -> list[str]:
    """This function will parse the html and obtain every link
    that appear in the page you provide.

    Args:
        link (str): url of the resource you want to visit

    Returns:
        list[str]: a list of the links found in the page
    """
    links: list[str] = []

    try:
        page_request = requests.get(link)
        page_request.raise_for_status()
        page_content = bs4.BeautifulSoup(page_request.text, features="html.parser")
    except Exception as err:
        print(f"Failed to get related links:\n{err}")
        sys.exit(1)

    anchor_elements: ResultSet[Tag] = page_content.select("a[data-ved]")

    # get every href attribute value of the anchor links
    for elem in anchor_elements:
        href: str = str(elem.get("href"))[7:]
        if href.startswith("https://"):
            links.append(href)

    return links


if __name__ == "__main__":
    main()
