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

## Lessons from the full migration attempt

The first full implementation was functional enough to pass tests, start locally, deploy, and serve production, but it was rolled back because it did not preserve teaching quality with 100% parity.

What worked:

- Markdown sources were pleasant to review and edit.
- Embedded `src/example_sources_data.py` solved the Worker bundling failure.
- `make build`, `make verify-examples`, `make check-generated`, and `verify-python-version` were useful workflow pieces.
- `compile(..., dont_inherit=True)` was necessary and correct for output verification.
- The deployed Worker could serve both the custom domain and `workers.dev` with Markdown-backed examples.

What did not work well enough:

- The golden source was removed too soon, which weakened parity checking after the app switch.
- Some examples lost fine-grained literate cells because the conversion required executable cells and collapsed non-executable fragments.
- Deriving editor code by joining cells coupled teaching structure to runnable program structure and created avoidable whitespace/parity problems.
- The formatter was too shallow; it normalized whitespace but did not fully reserialize TOML/frontmatter.
- The parity script became less useful once the old catalog disappeared from the tree.
- Passing production smoke tests was not enough; teaching-structure parity must be a release blocker.

Examples that lost fine-grained literate cells in the attempted conversion:

- `match-statements`
- `recursion`
- `classes`
- `properties`
- `special-methods`
- `type-hints`

Those examples must be rewritten into executable cells before any future app switch. Collapsing them into one large cell is allowed only as a temporary tooling fixture, not as a production-equivalent migration.

## Dependency-ordered task list

Investigation and verification tasks come first because they decide the implementation shape.

### Phase 0: spikes and investigations

- [ ] Freeze a golden copy of the current catalog before conversion; do not rely on git history as the only golden source.
- [ ] Spike Cloudflare Worker bundling for raw Markdown files under `src/example_sources/` using `pywrangler dev`.
- [ ] Spike production bundling, or document why local Worker bundling failure is enough to require embedded source data.
- [ ] Decide whether to keep the default embedded-data approach or replace it with proven native file bundling.
- [ ] Audit current walkthrough fragments and classify each example as fully executable cells, needs larger cells, or needs rewrite.
- [ ] Rewrite or redesign `match-statements`, `recursion`, `classes`, `properties`, `special-methods`, and `type-hints` so they retain fine-grained literate cells without non-executable fragments.
- [ ] Decide the final cell policy for non-executable explanatory fragments before writing conversion tooling.
- [ ] Confirm the `:::program` plus executable restatement-cell model works for the six problematic examples before converting all examples.
- [ ] Spike parser line-number tracking for frontmatter, cells, Python fences, output fences, and notes.
- [ ] Spike formatter behavior on several hand-edited Markdown examples and confirm it preserves prose/code semantics.
- [ ] Spike `uv run --python $(VERSION)` behavior for `verify-python-version` on locally available Python versions.
- [ ] Identify which examples should be marked `version_sensitive` before future Python runtime migrations.

### Phase 1: tooling while the live app stays on `src/examples.py`

- [ ] Add fixture Markdown examples for a small subset: `hello-world`, `values`, one multi-cell example, and one difficult class/method example.
- [ ] Add a checked-in golden catalog fixture for parity; keep it until after the cleanup milestone.
- [ ] Add `src/example_loader.py` with TOML frontmatter parsing, explicit cell parsing, line-number metadata, and generated `doc_url`.
- [ ] Add verifier execution using `compile(..., dont_inherit=True)`.
- [ ] Add support for exactly one `:::program` block per example and make the website editor source come from that block.
- [ ] Add verifier checks for wrong output, missing fences, duplicate slugs, stale embedded data, hardcoded docs versions, incompatible `min_python`, and inherited future flags.
- [ ] Add `scripts/format_examples.py` with `--check` mode.
- [ ] Add `scripts/embed_example_sources.py` if the bundling spike keeps the embedded-data approach.
- [ ] Add `scripts/check_example_migration_parity.py` against the checked-in golden catalog fixture and the current `src/examples.py` golden source.
- [ ] Add Make targets: `build`, `embed-examples`, `check-generated`, `verify-examples`, `format-examples`, and `verify-python-version`.
- [ ] Update fingerprinting so Markdown source or embedded source data changes `HTML_CACHE_VERSION`.
- [ ] Keep the website importing the current `src/examples.py` during this phase.

### Phase 2: mechanical conversion and parity

- [ ] Mechanically convert all current examples to Markdown without rewriting teaching content.
- [ ] Run the formatter and commit canonical Markdown shape.
- [ ] Run verifier across every Markdown example.
- [ ] Run golden parity and require the program block to match old `code` byte-for-byte.
- [ ] Run golden parity and classify walkthrough differences as identical or teaching-structure.
- [ ] Fix every semantic difference; do not allowlist semantic differences for the app switch.
- [ ] Fix every teaching-structure difference, including collapsed/lost cells.
- [ ] Fix examples whose cells are not executable according to the final cell policy.
- [ ] Verify Markdown-only edits change generated embedded data and `HTML_CACHE_VERSION`.
- [ ] Verify stale generated files fail `make check-generated`.

### Phase 3: app switch

- [ ] Block this phase unless golden parity reports 100% parity for metadata, code behavior, output, notes, walkthrough prose/source, rendered cell count, and cell source/output structure.
- [ ] Switch `src/examples.py` to a thin compatibility layer over the Markdown loader.
- [ ] Verify existing app tests still pass without weakening assertions.
- [ ] Run `make build`, `make verify-examples`, `make test`, `make seo-cache-lint`, `make browser-layout-test`, `make lint`, and `git diff --check`.
- [ ] Start local Worker with `pywrangler dev` and verify it does not fail on missing Markdown files.
- [ ] Verify representative GET pages render from the Markdown loader.
- [ ] Verify POST execution still runs edited code through Dynamic Workers.
- [ ] Verify browser layout for Shiki, CodeMirror, literate cells, and output panels.

### Phase 4: deploy and cleanup

- [ ] Do not deploy Markdown-backed examples unless Phase 3 has 100% parity and no collapsed/lost literate cells.
- [ ] Deploy only after local Worker startup and all verification pass.
- [ ] Smoke-test `https://www.pythonbyexample.dev`.
- [ ] Smoke-test `https://pythonbyexample.adewale-883.workers.dev`.
- [ ] Verify production asset caching and HTML cache-busting after an example-only edit.
- [ ] Remove old hand-authored example catalog only after one successful production deployment.
- [ ] Remove temporary golden parity scaffolding after cleanup is complete.
- [ ] Update README contributor instructions to point contributors at Markdown examples, `make build`, and `make verify-examples`.

## Implementation milestones

This migration must not be implemented as one large switch-over.

1. **Tooling-only milestone** — add Markdown sources, canonical loader, build scripts, verifier, formatter, and golden parity checks while the live app still imports `src/examples.py`.
2. **Dual-read milestone** — allow tests to load both `src/examples.py` and Markdown examples; keep `src/examples.py` as the public catalog until parity is clean.
3. **App switch milestone** — switch `src/examples.py` to a thin compatibility layer over the Markdown loader only after local Worker startup, browser layout checks, and 100% golden parity pass.
4. **Cleanup milestone** — remove the old hand-authored catalog and golden fixture only after one successful deploy and smoke test on both `www.pythonbyexample.dev` and the `workers.dev` hostname.

Each milestone should be independently reviewable and revertible.

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

`src/example_sources_data.py` is generated, committed, and treated like `src/asset_manifest.py`: it is not hand-edited, but it is included in commits so deploys are reproducible and Cloudflare has all required source data.

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
3. Exactly one `:::program` block containing the full editable program.
4. One or more explicit `:::cell` blocks for the literate walkthrough.
5. Optional `:::note` blocks.

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

:::program
```python
text = "python"
count = 3
ratio = 2.5
ready = True
missing = None

print(text.upper())
print(count + 4)
print(ratio * 2)
print(ready and count > 0)
print(missing is None)
```
:::

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
- Cell source must be executable when run after previous cells in the same namespace.
- The output fence must match the new stdout produced by that cell according to the verifier.
- Cell labels or numeric IDs may exist for tooling later, but must not render as noisy UI labels.

The failed migration showed that some current walkthrough fragments are not independently executable, such as method bodies without their class header. The spec resolves this by making executable cells the only renderable source/output unit. Non-executable excerpts may appear only as inline prose or future non-output annotations; they must not be rendered as source/output cells.

Cells are allowed to restate earlier definitions when that makes the fragment independently executable and preserves teaching flow. For example, a class-method cell may repeat the class header and initializer, then add the method being taught. These restatement cells are verified as cells, but they are not concatenated to form the editor program.

For production migration, fewer/larger cells are not acceptable if they reduce the current teaching structure. The parity gate must compare rendered cell counts and cell prose/source/output structure. Any collapsed cell is a teaching-structure difference that blocks the app switch until the example is rewritten into executable fine-grained cells.

## Full runnable code

The website editor must use the exact source from the `:::program` block, not source reconstructed by concatenating cells.

Program block shape:

````markdown
:::program
```python
print("hello world")
```
:::
````

Rules:

- Each example must contain exactly one `:::program` block.
- The program block must contain exactly one `python` fence.
- The program block is the editable source shown in the runner.
- `expected_output` is generated by executing the program block.
- The parity script must require the program block to match the current `src/examples.py` code byte-for-byte during migration.

The attempted migration showed that deriving editor code from `"\n\n".join(cell.source for cell in cells)` introduces whitespace drift and can force teaching cells to become the full program structure. The solution is to separate the full editable program from the literate cells while verifying both with the same loader.

## Output verification model

The verifier should execute cells in order in one Python process namespace:

1. Run cell 1 source.
2. Capture stdout emitted by cell 1.
3. Compare captured stdout to cell 1 `output` fence.
4. Keep globals alive.
5. Run cell 2 source.
6. Compare only the new stdout to cell 2 `output` fence.
7. Continue through the file.

The full runnable program should also be executed separately, and its stdout should equal the program's expected output. Cell outputs do not need to concatenate to the full program output because cells are teaching units and may restate earlier definitions.

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
    code: str  # from the :::program block
    expected_output: str  # stdout from executing code
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

A required build step turns canonical Markdown sources into generated deploy artifacts. It should be deterministic and safe to run repeatedly.

Required targets:

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

format-examples:
	uv run scripts/format_examples.py

verify-python-version: build
	uv run --python $(VERSION) scripts/verify_examples.py --python-version $(VERSION)

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
- Keep generated files committed until Cloudflare Python Workers reliably bundles Markdown data files directly.

`check-generated` must be part of CI. It catches contributors who edit Markdown but forget to run the build.

## Formatter

`format_examples.py` should make Markdown examples stable without rewriting author voice.

Required behavior:

- Preserve prose text, except for trimming trailing whitespace and normalizing blank lines.
- Sort frontmatter keys in this order: `slug`, `title`, `section`, `summary`, `doc_path`, then optional version fields.
- Normalize frontmatter to TOML with quoted strings.
- Normalize code fences to exactly `````python` and `````output`.
- Ensure each file ends with one newline.
- Leave Python code semantics unchanged; do not run Black over snippets unless the command can prove output is unchanged.
- Provide `--check` mode for CI.

Formatting and verification are separate: formatting rewrites shape, verification executes code and checks output.

## Strict tooling

Required checks:

- Parse every Markdown file through the canonical loader.
- Verify `src/example_sources_data.py` matches the Markdown source files.
- Verify manifest order, duplicate slugs, missing slugs, and filename/slug mismatch.
- Verify required frontmatter fields.
- Verify every page is language-tour content; reject unsupported metadata or off-tour sections.
- Verify every example has exactly one program block with one Python fence.
- Verify every cell has prose, one Python fence, and one output fence.
- Execute every cell in order and compare stdout with the adjacent output fence.
- Execute the program block and compare stdout with generated expected output.
- Parse the program block with `ast.parse`.
- Run formatting checks on generated code, or provide a formatter command that rewrites code fences consistently.
- Enforce readable line lengths for code and prose, with exceptions for URLs.
- Verify `python_version` and `docs_base_url` agree, for example `3.13` maps to `https://docs.python.org/3.13`.
- Verify example files use `doc_path`, not hardcoded versioned `docs.python.org` URLs.
- Verify generated `doc_url` values use the manifest docs version.
- Verify `min_python` is compatible with the manifest `python_version`.
- List every `version_sensitive` example in verifier output during a version migration.
- Verify summaries are non-empty and titles are unique.
- Report errors with source filenames and line numbers.

Line-number requirement:

- The parser should keep source offsets for frontmatter, each cell, each Python fence, each output fence, and each note block.
- Verification errors should point to the Markdown file and the start line of the failing cell or field, for example `src/example_sources/values.md:17: output mismatch`.
- Parser errors should include the nearest construct name: frontmatter, cell, python fence, output fence, or note.
- If exact line numbers are unavailable during the first tooling-only milestone, the verifier may ship temporarily with file-level errors, but app switch is blocked until line numbers are implemented.

## Python version migrations

Migration checklist:

1. Confirm Cloudflare Python Workers supports the new Python runtime.
2. Update `python_version` and `docs_base_url` in `src/example_sources/manifest.toml`.
3. Update `pyproject.toml` only after the Worker runtime supports the new version.
4. Ensure website runtime constants and Dynamic Worker cache keys are derived from the catalog model.
5. Run local verifier under the target CPython when available:

   ```bash
   make verify-python-version VERSION=3.14
   ```

6. Run Worker runtime verification with `pywrangler dev`, because CPython and Cloudflare's Pyodide runtime may differ.
7. Review every example reported as `version_sensitive`.
8. Update outputs only by rerunning examples through the verifier/update tool, not by hand-editing guesses.
9. Run full project verification before deployment.

The command should fail if:

- any example file contains a hardcoded `docs.python.org/3.x` URL;
- generated docs links use the wrong version;
- `min_python` exceeds the configured version;
- cell output changes under the new runtime;
- full generated output changes under the new runtime;
- site copy, SEO metadata, or Dynamic Worker cache-key version still points at the old version.

`verify-python-version` is only meaningful when `uv` can run the requested Python version. Until Cloudflare exposes the same runtime locally, the migration also requires a Worker smoke test for representative examples and at least one POST execution through Dynamic Workers.

## Worker bundling policy

Default policy:

- Keep Markdown sources in `src/example_sources/`.
- Generate `src/example_sources_data.py` during `make build`.
- Load live Markdown files when present; fall back to embedded data in the Worker bundle.
- Verify embedded data is fresh before tests, deploys, and CI.

Do not replace this with a native Wrangler data-file approach unless a spike proves all of the following:

- `pywrangler dev` can read the files locally;
- `pywrangler deploy` includes the files in production;
- imports work under Cloudflare's Python Worker module layout;
- cache fingerprinting sees example-only edits;
- tests fail if files are missing from the bundle.

The attempted migration failed at Worker startup because Markdown files were not present under `/session/metadata/`. That failure mode must remain covered by a local Worker startup check.

## Golden parity script

Add a dedicated migration script before switching the app:

```text
scripts/check_example_migration_parity.py
```

Required behavior:

- Import the old `src/examples.py` catalog and a checked-in frozen golden fixture as the golden sources.
- Load the Markdown catalog through `src/example_loader.py`.
- Compare example count and order.
- Compare `slug`, `title`, `section`, `summary`, generated `doc_url`, `expected_output`, notes, and walkthrough prose/source.
- Render old and new walkthrough cells and compare cell count, prose grouping, source, output, and order.
- Execute old and new full code and compare stdout.
- Classify full-code differences as `identical`, `whitespace-only`, or `semantic`.
- Classify walkthrough differences as `identical` or `teaching-structure`.
- Fail on every semantic or teaching-structure difference. No allowlist is permitted for the app switch.
- Print a short table of differences for review.

This script is temporary migration scaffolding. It can be removed only after the old catalog is deleted, one production deployment succeeds, and the rollback window has passed.

## Fourteen prerequisite verification gates

Before the app switch milestone, verify these fourteen gates with red-green-refactor TDD. For each gate, first add or run a failing check (**Red**), then implement the smallest code/tooling change that makes it pass (**Green**), then simplify without weakening the check (**Refactor**).

1. **Cloudflare bundling behavior** — prove whether raw Markdown files are available in `pywrangler dev` and production; if not, prove embedded source data is present and fresh.
2. **Golden parity script** — prove old `src/examples.py` and the Markdown loader agree on order, metadata, docs URLs, outputs, notes, and walkthrough content.
3. **Cell model** — prove every rendered source/output cell is executable after previous cells and rejects non-executable fragments.
4. **Generated full code** — prove the `:::program` block is the editor source and matches the old source byte-for-byte during migration.
5. **Verifier correctness** — prove the verifier catches wrong output, missing fences, duplicate slugs, stale embedded data, hardcoded docs versions, incompatible `min_python`, and inherited future flags.
6. **Line-number reporting** — prove parser and verifier failures point to useful Markdown file lines before the app switch.
7. **Formatter behavior** — prove formatting is deterministic, preserves prose/code semantics, normalizes frontmatter/fences, and has a `--check` mode.
8. **Build step** — prove `make build` regenerates all generated artifacts and `make check-generated` fails on stale generated files.
9. **Cache busting** — prove editing only an example Markdown file changes `HTML_CACHE_VERSION` and therefore invalidates cached HTML.
10. **Worker runtime startup** — prove `pywrangler dev` starts successfully with the Markdown loader and generated embedded data.
11. **POST execution** — prove edited code still runs through the Dynamic Worker POST path and returns the edited output.
12. **Browser layout** — prove Shiki, CodeMirror, literate cells, and output panels still render with browser tests.
13. **Production smoke test** — prove both `https://www.pythonbyexample.dev` and the `workers.dev` hostname serve the migrated app after deploy.
14. **Python version migration command** — prove `make verify-python-version VERSION=x.y` runs under the requested local runtime when available and is paired with Worker runtime verification.

These gates are not optional acceptance notes. They are the checklist that blocks the app switch milestone.

## Red-green-refactor order

Use this order for each implementation milestone:

1. **Red** — add a focused failing test, linter assertion, parity check, or smoke check for one gate. Do not change production code yet.
2. **Green** — make the smallest source/tooling/spec change that satisfies that failing check.
3. **Refactor** — simplify parser/build/test code while keeping the new check passing and preserving the old app behavior until the app switch milestone.

Prefer many small red-green-refactor cycles over another large migration commit.

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

The first implementation milestone should add loader, build, verifier, and parity tests while the website still serves `src/examples.py`. The second milestone should switch the website to the new loader only after 100% golden parity and Worker startup pass. If parity is below 100%, stop before deploy.

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

The command must report errors against the Markdown source file and line numbers before the app switch milestone.

## Non-goals

- Do not introduce task-cookbook examples.
- Do not make the homepage heavier as part of this format.
- Do not require contributors to edit Python dictionaries after migration.
- Do not keep separate hand-written expected output in `src/examples.py` after migration.
- Do not allow website-rendered code to diverge from locally verified code.
