import os
import platform
import string
import unicodedata
from collections import OrderedDict
from dataclasses import dataclass
from datetime import date
from datetime import datetime
from pathlib import Path
from typing import List
from typing import Optional
from urllib.parse import ParseResult
from urllib.parse import quote_plus
from urllib.parse import urlparse

from browserexport.merge import read_and_merge
from browserexport.model import Visit


def clean(s: str) -> str:
    # keep only valid ascii chars
    cleaned: str = unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode()

    # keep only whitelisted chars
    whitelist: str = "%s%s%s%s" % (
        string.ascii_letters,
        string.digits,
        string.punctuation,
        " ",
    )
    cleaned: str = "".join(c for c in cleaned if c in whitelist)
    return cleaned[:255]


def clean_url(url: str) -> str:
    parsed: ParseResult = urlparse(url=url)
    parsed._replace(
        query=quote_plus(parsed.query), fragment=quote_plus(parsed.fragment)
    )
    return parsed.geturl()


def get_dumping_dir() -> Path:
    cache_home: str = os.getenv("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))

    cache_path: Path = Path(
        f"{cache_home}/pretty_history/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    cache_path.mkdir(parents=True, exist_ok=True)
    return cache_path


def to_markdown_link(event: Visit) -> str:
    if event.metadata is None:
        return f"<{event.url}>"
    if "file://" in event.url:
        return f"*{clean(event.url.lstrip('file://'))}*"
    if len(event.metadata.title) > 0:
        return f"[{clean(event.metadata.title)}]({clean_url(url=event.url)})"


def prettify(history_json: Path, dumping_folder: Optional[Path]) -> None:
    grouped: OrderedDict[date, List[Visit]] = OrderedDict()
    for visit in read_and_merge([history_json]):  # type: Visit
        grouped.setdefault(visit.dt.date(), []).append(visit)

    out: Path = dumping_folder if dumping_folder is not None else get_dumping_dir()

    for key, val in grouped.items():
        page: Page = Page(dt=key, visits=val)
        page.dump(out_folder=out)

    print(f"Browser history files have been dumped to:\n{out}")


@dataclass(frozen=True)
class Page:
    dt: date
    visits: List[Visit]

    def dump(self, out_folder: Path) -> None:
        assert (
            len(self.visits) > 0
        ), f"Cannot dump browsing history page with no recorded visits ('{self.page_name}')"

        with open(os.path.join(out_folder, self.page_name + ".md"), "w") as f:
            f.write(f"# {self.page_name}")
            f.write("\n\n")
            f.write(datetime.strftime(self.visits[0].dt, "%Y%m%d%H%M%S"))
            f.write("\n\n")
            f.write(
                f"This file was autogenerated by `{platform.node()}` using `{os.path.abspath(__file__)}`."
            )
            f.write("\n\n")
            for visit in sorted(self.visits, key=lambda v: v.dt):  # type: Visit
                f.write(
                    f"- {datetime.strftime(visit.dt, '%H:%M')} {to_markdown_link(visit)}"
                )
                f.write("\n")

    @property
    def page_name(self) -> str:
        return f"{self.formatted_dt}, online browsing history"

    @property
    def formatted_dt(self) -> str:
        return (
            date.strftime(self.dt, "%B %#d, %Y")
            if platform.system() == "Windows"
            else date.strftime(self.dt, "%B %-d, %Y")
        )
