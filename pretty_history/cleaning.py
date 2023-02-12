import string
import unicodedata
from urllib.parse import ParseResult
from urllib.parse import quote_plus
from urllib.parse import urlparse


def clean(s: str) -> str:
    """
    Given a string, remove all invalid chars and truncate the string if it's too long.
    """
    # keep only valid ascii chars
    cleaned: str = unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode()

    # keep only whitelisted chars
    whitelist: str = "%s%s%s%s" % (
        string.ascii_letters,
        string.digits,
        string.punctuation,
        " ",
    )
    cleaned_and_whitelisted: str = "".join(c for c in cleaned if c in whitelist)
    return cleaned_and_whitelisted[:255]


def clean_url(url: str) -> str:
    """
    Escape any invalid characters in the URL query and fragment.
    """
    parsed: ParseResult = urlparse(url=url)
    parsed._replace(
        query=quote_plus(parsed.query), fragment=quote_plus(parsed.fragment)
    )
    return parsed.geturl()
