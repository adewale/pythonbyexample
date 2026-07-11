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

Use Node 22, install the committed dependency locks, and start the local Worker with the repository-pinned Wrangler:

```bash
node --version  # v22.x
uv sync --locked --all-groups
npm ci --ignore-scripts
make dev
```

Then run:

```bash
make verify
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

These scripts enforce the catalog-level rules from `docs/example-quality-rubric.md`. Run them together with `make quality-checks`.

| Script | What it gates |
| --- | --- |
| `scripts/check_registry_integrity.py` | Every owner slug in `docs/quality-registries.toml` exists in `manifest.toml`; tokens are present; each `paired_pages` pair is discoverable through `see_also` and has registry-named cell tokens demonstrated inside a teaching cell. |
| `scripts/check_confusable_pairs.py` | Each confusable pair's owning page contains every token inside teaching cells; a token shadowed inside a longer sibling token (plain `def` inside `async def`) does not count. |
| `scripts/check_broad_surface_tours.py` | Each broad-title page either covers every required form or sets `scope_first_pass = true` with registry-named `focused_neighbors` linked through `see_also`. |
| `scripts/check_footgun_coverage.py` | Each canonical Python footgun has a page that contains both broken-form and fixed-form tokens. |
| `scripts/check_notes_supported.py` | Every `:::note` bullet (across all note blocks) shares at least one keyword with the page body outside the notes, so notes cannot assert behavior the page never demonstrates. |
| `scripts/check_program_covers_cells.py` | Every executable cell shares substantive code with the `:::program` block, so the editor reproduces what the cells teach; `standalone_cells = true` opts out visibly. |
| `scripts/check_prose_duplication.py` | No verbatim repeated paragraphs, no cell prose copied from the intro, no duplicate note bullets. |
| `scripts/check_inline_links.py` | Inline `[text](target)` links in prose resolve to real `/examples` or `/journeys` pages. |
| `scripts/score_example_criteria.py` | Heuristic criterion scores per example; fails when a curated score exceeds the heuristic by more than the delta bound, so the score registry cannot inflate without the page changing. |
| `scripts/check_quality_scores.py` | Curated scores meet the 9.0 target / 8.5 hard minimum, waivers carry future expiry dates and are dropped when stale, and the journey-section average stays above its floor. |
| `scripts/check_no_figure_rationales.py` | No-figure opt-outs carry a reason and an unexpired `review_after` date. |
| `scripts/check_journey_outcomes.py` | Every journey section declares learner outcomes. |
| `scripts/audit_example_graph.py --check` | The `see_also` graph has no broken targets, self-links, over-linked pages, or orphaned examples. |

The single source of truth for the registries is `docs/quality-registries.toml`. Add confusable pairs, broad tours, footguns, journey metadata, figure attachments, captions, and curated scores there, then update the owning page so the tokens appear in cells or prose.

## Adding a new example end to end

1. Write `src/example_sources/<slug>.md` (frontmatter, intro prose, one `:::program`, cells, notes) and add the slug to `manifest.toml`'s `order`.
2. Add `see_also` links in both directions — `scripts/audit_example_graph.py --check` fails orphaned pages.
3. Score the page against `docs/example-quality-rubric.md` and add the `[[example_quality_scores]]` entry to `docs/quality-registries.toml`.
4. Attach a figure by adding `[[figure_attachments]]` and `[[example_figure_scores]]` entries to `docs/quality-registries.toml` (or add a `no_figure_rationales` entry with a review date); keep only new paint functions in `src/marginalia.py`. Review the result on `public/prototyping/marginalia-gestalt.html`, which shows the production caption under every figure.
5. Run `make build`, `make verify-examples`, `make quality-checks`, and `scripts/format_examples.py --check`.
6. Run the full `make verify` with a local Worker running, then commit — including the regenerated `src/example_sources_data.py`, `src/editorial_registry_data.py`, `src/asset_manifest.py`, and fingerprinted assets.

## Secrets and deploy configuration

Production deployment is manual through an authenticated Wrangler session with `make deploy`; public `workers.dev` and version preview URLs are disabled. Runtime Worker secrets (`TURNSTILE_SECRET_KEY`, `TURNSTILE_CLEARANCE_SECRET`, `PBE_SMOKE_BYPASS_SECRET`) are managed with `wrangler secret put`; see `docs/turnstile-runner-protection-spec.md`.

Generated output is prevented from drifting before merge: install the local hooks with `scripts/install-git-hooks.sh`, and keep `main` protected so pull requests require the `verify` status check to pass against the current base. CI enforces the same `make check-generated` contract for contributors without local hooks.

## Style expectations

- Keep examples compact and language-tour focused.
- Prefer practical names and output that proves the concept.
- Keep source/output cells executable and deterministic.
- Do not add task-cookbook examples to the language tour.
- Link to official Python 3.13 documentation through `doc_path`.
