# Lessons Learned

This document records project lessons that should guide future changes to Python By Example.

## Cloudflare Python Workers

- Use the Cloudflare Python Workers FastAPI pattern: keep the FastAPI app ordinary, then bridge it from the Worker entrypoint with `asgi.fetch(...)`.
- Python Workers currently target Python 3.13 in this project. Do not update examples or docs links to a Python version unsupported by the Worker runtime.
- Dynamic Workers should be reused by a stable key, but output should not be cached. The key should include Python version, example slug, and a hash of the submitted code.
- Disable outbound access for Dynamic Workers running user-edited examples. The example runner should not need network access.
- POST runs must never go through the rendered-page cache path.

## Cache busting and Worker Cache API

- Fingerprinted filenames are the correct fit for immutable static assets.
- Do not attach `immutable` cache headers to stable asset URLs unless the HTML references versioned/fingerprinted paths.
- Rendered HTML needs its own cache-busting mechanism. Fingerprinted CSS/JS alone does not help if stale HTML still points at old assets or old markup.
- The Worker Cache API key should include a generated HTML version derived from templates, app code, examples, and asset fingerprints.
- Prototype routes should not be cached. Iteration speed matters more than edge caching for `/layout-options/*`.
- Local Wrangler/Miniflare cache can survive server restarts. If local pages look stale, clear `.wrangler/state/v3/cache` or use no-store routes for prototypes.

## Syntax highlighting

- Shiki is excellent for read-only code blocks.
- Do not use two server/client syntax highlighters for the same read-only block. Server-render plain escaped code, then let Shiki progressively enhance it.
- Shiki outputs `.line` spans separated by newline text nodes. If `.line` is styled as `display: block`, those newline text nodes can create visual blank rows. Keep Shiki line spans inline for the orange-rail code blocks.
- A `<textarea>` cannot be syntax-highlighted directly. Use a real editor such as CodeMirror for editable code, with the textarea preserved as a no-JS fallback and form submission source.
- CodeMirror package versions should be kept compatible; duplicate `@codemirror/state` instances can break extension checks.

## Literate examples

- The strongest page structure is prose + source + output evidence. Output should sit near the code that produced it.
- Notebook tools such as marimo are useful inspiration, but the goal is not to become a notebook. Python By Example should stay article-like and low chrome.
- Avoid decorative labels that do not teach. Labels such as `Cell 1 · <<fragment-1>>` add noise unless the fragment name is meaningful to the learner.
- If a source fragment only prepares state and has no output, merge it with the next fragment that produces output. Every displayed cell should have evidence.
- Keep the complete editable program visible because it is the thing that actually runs.
- When storing examples as Markdown, keep the full editable program in `:::program` and teaching fragments in separate `:::cell` blocks. Do not concatenate cells to recreate the editor source.
- Fine-grained cells can restate definitions to stay executable. This is better than collapsing class, property, recursion, match, or type-hint examples into one large cell.
- Preserve a frozen golden catalog while migrating source formats. Full stdout parity is not enough; rendered teaching-cell structure must also match.

## Layout and mobile

- Mobile should make execution obvious early. A good order is title, explanation cells, notes, then the complete runner, or for prototypes: runner/output before deeper explanation.
- Avoid layout shifts after execution. Reserve space for metadata such as execution time before a run occurs.
- When two columns use the orange rail, source and output need identical rail spacing. Differences in border/padding make the page feel broken even if the content is correct.
- Use browser screenshot tests for visual bugs. Static HTML/CSS assertions are useful but can miss actual rendered layout behavior.

## Testing and verification

- Unit tests are good for catalog integrity, rendering contracts, Dynamic Worker code generation, and cache-policy source checks.
- Browser tests are necessary for Shiki/CodeMirror layout behavior and visual regressions.
- SEO and cache-busting deserve a dedicated linter because errors are easy to reintroduce when adding pages or assets.
- Always run the full pre-push set before publishing. Start `pywrangler dev --port 9696`, then run:

```bash
make verify
scripts/check_example_migration_parity.py
scripts/format_examples.py --check
make verify-python-version VERSION=3.13
git diff --check
```

- `make check-generated` should fail if embedded example data, asset manifests, or cache headers are stale.

## Documentation and GitHub readiness

- Keep generated runtime directories out of Git: `.wrangler/`, `.venv/`, `.venv-workers/`, and `python_modules/`.
- Keep `README.md` focused on how to understand, verify, and deploy the project.
- Keep this lessons document updated when a bug reveals a general rule.
- Record user-visible changes in `CHANGELOG.md` before significant commits or releases.
