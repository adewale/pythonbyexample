# Contributing

Thanks for helping improve Python By Example.

## Editing examples

Examples live in:

```text
src/example_sources/*.md
```

Each example has:

- TOML frontmatter with `slug`, `title`, `section`, `summary`, and `doc_path`
- exactly one `:::program` block with the full editable program
- one or more `:::cell` blocks with prose, Python source, and expected output
- optional `:::note` blocks

Use `doc_path`, not full versioned Python docs URLs. The active docs version comes from:

```text
src/example_sources/manifest.toml
```

Do not edit generated files by hand:

```text
src/example_sources_data.py
src/asset_manifest.py
public/*.css/js fingerprinted copies
```

Regenerate them with:

```bash
make build
```

## Before opening a pull request

Start the local Worker for browser-backed checks:

```bash
uv run --group workers pywrangler dev --port 9696
```

Then run:

```bash
make verify
scripts/check_example_migration_parity.py
scripts/format_examples.py --check
make verify-python-version VERSION=3.13
git diff --check
```

For example-only changes, also run:

```bash
make verify-examples
make check-generated
```

## Quality checks

Five scripts enforce the catalog-level rules from `docs/example-quality-rubric.md`. Run them together with `make quality-checks`.

| Script | What it gates |
| --- | --- |
| `scripts/check_registry_integrity.py` | Every owner slug in `docs/quality-registries.toml` exists in `manifest.toml`; tokens are present. |
| `scripts/check_confusable_pairs.py` | Each confusable pair's owning page contains every token that signals the contrast. |
| `scripts/check_broad_surface_tours.py` | Each broad-title page either covers every required form or sets `scope_first_pass = true` with `see_also` links to focused neighbors. |
| `scripts/check_footgun_coverage.py` | Each canonical Python footgun has a page that contains both broken-form and fixed-form tokens. |
| `scripts/check_notes_supported.py` | Every `:::note` bullet shares at least one keyword with the page body, so notes cannot assert behavior the page never demonstrates. |

The single source of truth for the registries is `docs/quality-registries.toml`. Add a new pair, broad tour, or footgun there, then update the owning page so the tokens appear in cells or prose.

## Style expectations

- Keep examples compact and language-tour focused.
- Prefer practical names and output that proves the concept.
- Keep source/output cells executable and deterministic.
- Do not add task-cookbook examples to the language tour.
- Link to official Python 3.13 documentation through `doc_path`.
