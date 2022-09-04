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
        "-j",
        "--json",
        action="store",
        type=pathlib.Path,
        required=True,
        metavar="~/Documents/history.json",
        dest="json_file",
        help="The absolute or relative path to the JSON file containing your browser history. The schema of the JSON "
        "file should match the output from seanbreckenridge/browserexport",
    )
    args: Namespace = parser.parse_args()

    prettyhist.prettify(history_json=args.json_file)


if __name__ == "__main__":
    main()
