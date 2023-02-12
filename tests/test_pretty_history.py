import os.path
import platform
from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import Mock

from browserexport.browsers.firefox import Firefox

import pretty_history.prettyhist
from pretty_history import __version__

GENERAL_IN_FILE: str = os.path.join("tests", "resources", "general_in_file.json")
GENERAL_OUT: str = os.path.join("tests", "resources", "general_out.md")

BROWSER = "firefox"
GENERAL_IN_DB: str = os.path.join("tests", "resources", "general_in_db.sqlite")


def test_version():
    assert __version__ == "2.0.1"


def test_dump_correctly(tmp_path: Path):
    """
    Given an example input, ensure that the output is exactly as expected.
    """
    platform.node = MagicMock(return_value="hostname_of_computer")
    os.path.abspath = MagicMock(return_value="/path/to/the/script.py")

    Firefox.locate_database = Mock(return_value=GENERAL_IN_DB)

    pretty_history.prettyhist.prettify(
        history_json=Path(GENERAL_IN_FILE),
        dumping_folder=tmp_path,
        browser=BROWSER,
        browser_profile="*",
    )

    expected: str = __read_file_contents(file_path=GENERAL_OUT)
    actual: str = __read_file_contents(
        file_path=os.path.join(
            tmp_path, "February 11, 2023, online browsing history.md"
        )
    )

    assert actual == expected


def __read_file_contents(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()
