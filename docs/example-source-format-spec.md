# Example source format spec

This spec describes a future source format for Python By Example examples. The goal is to make each example independently editable, reviewable, and verifiable while keeping the project strictly a Python language tour.

Every page should teach a Python language concept, standard syntax pattern, object model behavior, or core standard-library concept that belongs in the learning sequence.

## Goals

- Store each example in one human-editable Markdown file.
- Load only the requested example's full code, prose, and output when rendering an example page.
- Keep enough lightweight metadata available to build navigation without parsing every full page body.
- Use the same parsed code model for local tests, generated expected output, embedded Worker data, and the website editor.
- Make pull requests easy to review: one example change should usually touch one Markdown file.
- Make source/result pairing strict: visible output must be produced by adjacent visible source.
- Make generated deploy artifacts reproducible through one build step.

## Go By Example tooling lessons

Go By Example's `tools/` directory is intentionally small and strict. Useful lessons for this project:

- `tools/build` runs validation, formatting, line-length measurement, and generation as one pipeline.
- Generated output is written to a temporary directory first, then optionally diffed against checked-in output in testing mode.
- `tools/test` validates examples with the language toolchain (`go vet ./examples/...`).
- `tools/format` formats example source files (`gofmt`).
- `tools/measure` enforces short rendered lines for readability.
- `tools/generate.go` parses one canonical source format and uses that parsed model to render pages.
- The source format keeps prose close to code; comments/prose and code are parsed into ordered segments.

Python By Example should copy the philosophy, not the exact format: one canonical parser, one strict build pipeline, language-aware validation, line-length/layout constraints, generated-output diffing, and no separate hand-maintained website copy of example code.

## File layout

Preferred source layout:

```text
src/example_sources/
  manifest.toml
  hello-world.md
  values.md
  variables.md
```

The sources live under `src/example_sources/` so they are visibly part of the app source. Cloudflare Python Workers did not package arbitrary Markdown files in the attempted migration, so the build must also generate an importable Python module:

```text
src/example_sources_data.py
```

The canonical loader should prefer live Markdown files during local development and fall back to `src/example_sources_data.py` inside the Worker bundle. Verification must fail if the embedded module is stale.

`manifest.toml` defines learning order, section grouping, and the active Python documentation/runtime target:

```toml
python_version = "3.13"
docs_base_url = "https://docs.python.org/3.13"

order = [
  "hello-world",
  "values",
  "variables",
]
```

The Python version belongs in the manifest, not in every example file. A future migration from Python 3.13 to Python 3.14 should be driven by changing `python_version` and `docs_base_url`, then running strict verification.

## Markdown file format

Each example file contains:

1. TOML frontmatter delimited by `+++`.
2. Introductory prose.
3. One or more explicit `:::cell` blocks.
4. Optional `:::note` blocks.

TOML is preferred over YAML so the loader can use Python's standard-library `tomllib` locally and in the Worker bundle.

Example:

````markdown
+++
slug = "values"
title = "Values"
section = "Basics"
summary = "Python has strings, integers, floats, booleans, and None."
doc_path = "/library/stdtypes.html"
+++

Python programs are built from values. Strings, integers, floats, booleans,
and `None` are basic values used throughout the language.

:::cell
Strings have methods, and numbers work with arithmetic operators.

```python
text = "python"
count = 3
ratio = 2.5

print(text.upper())
print(count + 4)
print(ratio * 2)
```

```output
PYTHON
7
5.0
```
:::
````

## Frontmatter

Required fields:

```toml
slug = "values"
title = "Values"
section = "Basics"
summary = "Python has strings, integers, floats, booleans, and None."
doc_path = "/library/stdtypes.html"
```

Optional fields:

```toml
version_sensitive = false
min_python = "3.13"
version_notes = "Output includes exception text that should be reviewed during Python version migrations."
```

Rules:

- `slug` must match the filename without `.md`.
- `slug` must appear exactly once in `src/example_sources/manifest.toml`.
- `doc_path` must be a path, not a full URL. The loader combines it with `docs_base_url` from the manifest to produce `doc_url`.
- Example files must not hardcode `docs.python.org/3.x` URLs in frontmatter or body prose unless an explicit verifier allowlist is added.
- `min_python`, when present, must be less than or equal to the manifest `python_version`.
- `version_sensitive = true` requires `version_notes`.
- The format intentionally has no `kind` field. All examples are language-tour examples.

## Cells

Each `:::cell` block is one teaching unit:

```text
prose
python source fence
output fence
```

Rules:

- A cell must contain exactly one `python` code fence.
- A cell must contain exactly one `output` fence.
- Cell prose is required.
- The output fence must match the output produced by that cell according to the verifier.
- Cell labels or numeric IDs may exist for tooling later, but must not render as noisy UI labels.

Some language-tour examples contain source fragments that are not independently executable, such as method bodies without their class header. The failed migration showed that forcing every visual fragment to be an independently executable cell can collapse useful explanations into one large cell. The format therefore needs one of these explicit strategies before implementation:

- require cells to contain independently executable source, accepting fewer/larger cells where necessary;
- add an explicit continuation/setup mechanism that contributes to execution without noisy UI labels;
- or keep separate display fragments and executable cells, with tooling proving that they map to the same full program.

Do not infer non-executable fragments silently.

## Full runnable code

The website editor must use code derived from the same parsed model that tests use.

Default rule:

```python
full_code = "\n\n".join(cell.source for cell in cells)
```

The full expected output is derived similarly:

```python
expected_output = "\n".join(cell.output for cell in cells)
```

The attempted migration showed this can introduce harmless extra blank lines compared with the current hand-authored source. That is acceptable only if the verifier treats it as intentional and full output remains unchanged. If byte-for-byte source parity matters, the format needs an explicit full-source block or source-span metadata instead of naive cell joining.

## Output verification model

The verifier should execute cells in order in one Python process namespace:

1. Run cell 1 source.
2. Capture stdout emitted by cell 1.
3. Compare captured stdout to cell 1 `output` fence.
4. Keep globals alive.
5. Run cell 2 source.
6. Compare only the new stdout to cell 2 `output` fence.
7. Continue through the file.

The full runnable code should also be executed separately, and its stdout should equal the concatenated cell outputs.

Verifier execution must use:

```python
compile(code, "<example>", "exec", dont_inherit=True)
```

This prevents future flags from the verifier module, such as `from __future__ import annotations`, from changing example behavior.

## Loader requirement

There must be one canonical parser/loader, for example:

```text
src/example_loader.py
```

Both the website and tooling must use it:

```text
FastAPI route -> load_example(slug) -> render page/editor
verify script -> load_example(slug) -> run cells/full code
build script -> load examples -> generate embedded Worker data
```

Do not maintain one parser for tests and a different parser for the website.

The parsed model should be equivalent to:

```python
@dataclass(frozen=True)
class ExampleCatalog:
    python_version: str
    docs_base_url: str
    examples: list[ExampleSummary]

@dataclass(frozen=True)
class Example:
    slug: str
    title: str
    section: str
    summary: str
    doc_path: str
    doc_url: str
    intro: str
    cells: list[Cell]
    notes: list[str]
    code: str
    expected_output: str
    min_python: str | None = None
    version_sensitive: bool = False
    version_notes: str | None = None

@dataclass(frozen=True)
class Cell:
    prose: list[str]
    source: str
    output: str
```

The website, verifier, build step, and Dynamic Worker cache-key logic should read the active Python version from this catalog model rather than duplicating it in separate constants.

## Build step

A required build step should turn canonical Markdown sources into generated deploy artifacts.

Suggested targets:

```make
build: embed-examples fingerprint

embed-examples:
	uv run scripts/embed_example_sources.py

fingerprint: embed-examples
	uv run scripts/fingerprint_assets.py

check-generated: build
	git diff --exit-code src/example_sources_data.py src/asset_manifest.py public/_headers

verify-examples: build
	uv run scripts/verify_examples.py

verify: build test seo-cache-lint verify-examples browser-layout-test lint check-generated

deploy: build
	uv run pywrangler deploy
```

Build requirements:

- Regenerate `src/example_sources_data.py` from Markdown sources.
- Regenerate `src/asset_manifest.py` and cache headers.
- Include Markdown source content or embedded source data in `HTML_CACHE_VERSION` so example-only edits bust cached HTML.
- Fail CI or local verification if generated files are stale.
- Keep deploy dependent on build.

## Strict tooling

Required checks:

- Parse every Markdown file through the canonical loader.
- Verify `src/example_sources_data.py` matches the Markdown source files.
- Verify manifest order, duplicate slugs, missing slugs, and filename/slug mismatch.
- Verify required frontmatter fields.
- Verify every page is language-tour content; reject unsupported metadata or off-tour sections.
- Verify every cell has prose, one Python fence, and one output fence.
- Execute every cell in order and compare stdout with the adjacent output fence.
- Execute full generated code and compare stdout with generated expected output.
- Parse full generated code with `ast.parse`.
- Run formatting checks on generated code, or provide a formatter command that rewrites code fences consistently.
- Enforce readable line lengths for code and prose, with exceptions for URLs.
- Verify `python_version` and `docs_base_url` agree, for example `3.13` maps to `https://docs.python.org/3.13`.
- Verify example files use `doc_path`, not hardcoded versioned `docs.python.org` URLs.
- Verify generated `doc_url` values use the manifest docs version.
- Verify `min_python` is compatible with the manifest `python_version`.
- List every `version_sensitive` example in verifier output during a version migration.
- Verify summaries are non-empty and titles are unique.
- Report errors with source filenames and line numbers where possible.

## Python version migrations

Migration checklist:

1. Confirm Cloudflare Python Workers supports the new Python runtime.
2. Update `python_version` and `docs_base_url` in `src/example_sources/manifest.toml`.
3. Ensure website runtime constants and Dynamic Worker cache keys are derived from the catalog model.
4. Run `make verify-python-version VERSION=3.14` under the target runtime when available.
5. Review every example reported as `version_sensitive`.
6. Update outputs only by rerunning examples through the verifier/update tool, not by hand-editing guesses.
7. Run full project verification before deployment.

The command should fail if:

- any example file contains a hardcoded `docs.python.org/3.x` URL;
- generated docs links use the wrong version;
- `min_python` exceeds the configured version;
- cell output changes under the new runtime;
- full generated output changes under the new runtime;
- site copy, SEO metadata, or Dynamic Worker cache-key version still points at the old version.

## Migration safety for implementing this spec

Moving from `src/examples.py` to Markdown source files should be done as a compatibility-preserving migration.

Required safety checks before removing the old source:

- Convert examples to Markdown mechanically first; do not rewrite teaching content in the same change.
- Keep the old `src/examples.py` model temporarily as a golden source.
- Add the Markdown loader, verifier, and build step while the website still serves the old model.
- Load every old example and every new Markdown example through their respective loaders.
- Compare slug, title, section, summary, generated `doc_url`, full `code`, `expected_output`, walkthrough prose/source/output, notes, and previous/next order.
- Explicitly report any whitespace-only code differences.
- Render representative pages with both models and compare stable HTML structure after ignoring expected fingerprint/cache-version differences.
- Run local Worker startup, not only unit tests, because packaging failures may only appear in `pywrangler dev`.
- Verify POST execution still uses the full generated code and still returns edited-code output.
- Run all current tests, SEO/cache lint, browser layout tests, Ruff, and `git diff --check`.
- Deploy only after both custom domain and workers.dev smoke tests pass.

The first implementation milestone should add loader, build, verifier, and parity tests while the website still serves `src/examples.py`. The second milestone should switch the website to the new loader only after golden-model parity and Worker startup pass.

## Contributor workflow

A contributor adding or changing an example should be able to run:

```bash
make build
make verify-examples
```

For one page:

```bash
uv run scripts/verify_examples.py values
```

The command should report errors against the Markdown source file and line numbers where possible.

## Non-goals

- Do not introduce task-cookbook examples.
- Do not make the homepage heavier as part of this format.
- Do not require contributors to edit Python dictionaries after migration.
- Do not keep separate hand-written expected output in `src/examples.py` after migration.
- Do not allow website-rendered code to diverge from locally verified code.
