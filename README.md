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

```bash
browserexport save --browser firefox --to .
browserexport merge --json ./*.sqlite > ./history.json
prettyhist ./history.json
```

Extracting history directly from the browser is still a work-in-progress, see https://github.com/apatel762/pretty-history/issues/1.

## References

1. [seanbreckenridge/browserexport](https://github.com/seanbreckenridge/browserexport)
