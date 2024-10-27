import argparse
import pathlib
from argparse import ArgumentParser
from argparse import Namespace
from typing import Optional

from browserexport.browsers.all import DEFAULT_BROWSERS

from pretty_history import prettyhist

OPT_BROWSER: str = "-b"
OPT_BROWSER_PROFILE: str = "-p"
OPT_JSON_FILE: str = "-f"
OPT_DESTINATION_FOLDER: str = "-o"

LONG_OPT_BROWSER_PROFILE: str = "--profile"


def main():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate a pretty view of your browser history from a JSON export."
    )
    parser.add_argument(
        OPT_BROWSER,
        dest="browser",
        action="store",
        type=str,
        required=False,
        choices=[b.__name__.lower() for b in DEFAULT_BROWSERS],
        help=f"The browser that you want to extract your browsing history data from. If you also provide the "
        f"'{OPT_JSON_FILE}' option, the data from the JSON file will be merged with whatever is found in your browser.",
    )
    parser.add_argument(
        OPT_BROWSER_PROFILE,
        LONG_OPT_BROWSER_PROFILE,
        dest="profile",
        action="store",
        type=str,
        required=False,
        help=f"The browser profile that you want to extract history for. You must supply the '{OPT_BROWSER}' option if you provide this.",
    )
    parser.add_argument(
        OPT_JSON_FILE,
        dest="json_file",
        action="store",
        type=pathlib.Path,
        required=False,
        metavar="./my_history.json",
        help="The absolute or relative path to the JSON file containing your browser history. The schema of the JSON "
        "file should match the output from 'purarue/browserexport'.",
    )
    parser.add_argument(
        OPT_DESTINATION_FOLDER,
        dest="destination_folder",
        action="store",
        type=pathlib.Path,
        required=False,
        metavar="./folder",
        help="The absolute or relative path to a folder that you want to send the generated output to.",
    )
    args: Namespace = parser.parse_args()

    browser: Optional[str] = args.browser
    profile: Optional[str] = args.profile
    json_file: Optional[pathlib.Path] = args.json_file
    destination_folder: Optional[pathlib.Path] = args.destination_folder

    if profile is not None and browser is None:
        parser.error(
            f"you must provide '{OPT_BROWSER}' if you have provided '{OPT_BROWSER_PROFILE}'/'{LONG_OPT_BROWSER_PROFILE}'"
        )

    if browser is None and json_file is None:
        parser.error(
            f"you must provide at least one of '{OPT_BROWSER}' or '{OPT_JSON_FILE}'"
        )

    if json_file is not None and not json_file.is_file():
        parser.error(f"the provided JSON file '{json_file}' does not exist")

    if destination_folder is not None and not destination_folder.is_dir():
        parser.error(
            f"the provided destination folder '{destination_folder}' does not exist"
        )

    prettyhist.prettify(
        browser=browser,
        browser_profile=profile if profile is not None else "*",
        history_json=args.json_file,
        dumping_folder=args.destination_folder,
    )


if __name__ == "__main__":
    main()
