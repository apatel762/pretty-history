# pretty-history

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
