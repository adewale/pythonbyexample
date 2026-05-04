# Python By Example

A small, versioned "Python By Example" site inspired by [Go by Example](https://gobyexample.com/), with examples linked to the official [Python docs](https://docs.python.org/3/).

The app is built for Cloudflare Python Workers and runs each curated example in a Cloudflare Dynamic Worker sandbox.

## Development

This project is developed with red-green-refactor TDD:

1. Write or update a failing test.
2. Implement the smallest change that makes it pass.
3. Refactor while keeping tests green.

Run tests:

```bash
python3 -m unittest discover -s tests -v
```

Run locally on Workers:

```bash
uv run pywrangler dev --port 9696
```

Deploy:

```bash
uv run pywrangler deploy
```

## Updating for a new Python version

Edit `src/examples.py`:

- update `PYTHON_VERSION` for the Python docs target
- add, remove, or revise entries in `EXAMPLES`
- keep every example self-contained so it can run inside a Dynamic Python Worker
- link `doc_url` to the matching page in `https://docs.python.org/<version>/`

Then update tests or add new tests first, run them red, implement, and refactor.

## Cloudflare notes

- `wrangler.jsonc` enables `python_workers` and `python_dedicated_snapshot`.
- The parent Worker uses a `LOADER` Worker Loader binding.
- Dynamic examples are cached by `pythonbyexample:<python-version>:<slug>`.
- Dynamic Workers are loaded with `globalOutbound: null` and tight CPU/subrequest limits.
