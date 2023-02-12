# pretty-history

[![PyTest](https://github.com/apatel762/pretty-history/actions/workflows/pytest.yml/badge.svg)](https://github.com/apatel762/pretty-history/actions/workflows/pytest.yml) [![PyPi version](https://img.shields.io/pypi/v/browserexport.svg)](https://pypi.python.org/pypi/browserexport) [![Python 3.7|3.8|3.9](https://img.shields.io/pypi/pyversions/browserexport.svg)](https://pypi.python.org/pypi/browserexport) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

The `pretty-history` app is a simple Python script that can be run via the command-line, and will generate Markdown files summarising your browser history.

## Installation

Install from the PyPi repository using `pip`:

```
pip install pretty-history
```

## Usage

After installing the app, run:

```
prettyhist --help
```

To see some instructions for how to use it.

### Example

Pretty-format browsing history from Firefox:

```bash
prettyhist -b firefox
```

Pretty-format browsing history from Firefox, merging with data from Brave Browser:

```bash
browserexport save --browser brave --to .
browserexport merge --json ./*.sqlite > ./history.json

prettyhist -b firefox -f ./history.json
```

## References

1. [seanbreckenridge/browserexport](https://github.com/seanbreckenridge/browserexport)
