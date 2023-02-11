import os.path
import platform
from pathlib import Path
from unittest.mock import MagicMock

import pretty_history.prettyhist
from pretty_history import __version__

GENERAL_IN: str = os.path.join("tests", "resources", "general_in.json")
GENERAL_OUT: str = os.path.join("tests", "resources", "general_out.md")


def test_version():
    assert __version__ == "1.0.7"


def test_dump_correctly(tmp_path: Path):
    """
    Given an example input, ensure that the output is exactly as expected.
    """
    platform.node = MagicMock(return_value="hostname_of_computer")
    os.path.abspath = MagicMock(return_value="/path/to/the/script.py")

    pretty_history.prettyhist.prettify(
        history_json=Path(GENERAL_IN), dumping_folder=tmp_path
    )

    expected: str = __read_file_contents(file_path=GENERAL_OUT)
    actual: str = __read_file_contents(
        file_path=os.path.join(
            tmp_path, "September 10, 2022, online browsing history.md"
        )
    )

    assert actual == expected


def __read_file_contents(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()
