import argparse
import pathlib
from argparse import ArgumentParser
from argparse import Namespace

from pretty_history import prettyhist


def main():
    parser: ArgumentParser = argparse.ArgumentParser(
        description="Generate a pretty view of your browser history from a JSON export."
    )
    parser.add_argument(
        dest="json_file",
        action="store",
        type=pathlib.Path,
        help="The absolute or relative path to the JSON file containing your browser history. The schema of the JSON "
        "file should match the output from 'seanbreckenridge/browserexport'.",
    )
    parser.add_argument(
        "-o",
        dest="destination_folder",
        action="store",
        type=pathlib.Path,
        required=False,
        metavar="./folder",
        help="The absolute or relative path to a folder that you want to send the generated output to.",
    )
    args: Namespace = parser.parse_args()

    prettyhist.prettify(
        history_json=args.json_file, dumping_folder=args.destination_folder
    )


if __name__ == "__main__":
    main()
