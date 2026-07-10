# Changelog

All notable changes to Python By Example are documented here.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses date-based release notes while the app is pre-1.0.

## Unreleased

### Added

- `/about` page describing how the site is made — the verified-output pipeline, the runner sandbox, the figure grammar, and the quality gates — with a design-language section that renders the live CSS tokens (color swatches, spacing scale, type specimens, and a real walkthrough cell as a specimen). Linked from the nav on every page and listed in the sitemap.
- Copy buttons on read-only source cells: injected client-side onto `.cell-source` wrappers (so no-JS pages render no dead buttons), clipboard API with a hidden-textarea fallback, and a quiet token-styled treatment that sharpens on hover or focus.
- Keyboard navigation on example pages: `←`/`→` follow the existing `rel="prev"`/`rel="next"` links, ignoring keystrokes with modifiers or focus inside the editor, inputs, or any editable surface.

- Banner position grammar from `docs/visual-explainer-spec.md` is now production: `render_banner(slug, position)` supports `before`, `after-cell-N` (legacy anchor `cell-N`), and `after-walkthrough`, with multiple figures per position rendering as one small-multiple banner. The mutability page ships the canonical two-figure pair (aliased mutation vs. frozen tuple).
- Curated pair banners on contrast cells: `positional-only-parameters` shows the `/` and `*` separator twins side by side, `metaclasses` pairs the metaclass triangle with the familiar class triangle, and `tuples` pairs the frozen tuple with the growing list on the intent-contrast cell. `iterator-vs-iterable` gains the one-pass caret figure on the exhaustion cell.

- `/sitemap.xml` route listing home, journeys, and all example pages; `public/robots.txt` with a Sitemap directive.
- JSON-LD structured data: `WebSite` on the home page, `TechArticle`/`LearningResource` on every example page, enforced by the SEO linter.
- Client-side example search on the home page: a build-step JSON index (`make build-search-index`), fingerprinted `search.js`/`search-index.json` assets, `/` keyboard shortcut, and a Node ranking check (`make search-ranking-test`).
- Dark mode via `prefers-color-scheme`: inverted warm palette, dual-theme Shiki highlighting, a dark CodeMirror highlight style, and marginalia figures rendered on a light paper chip so the locked grammar stays untouched.
- Skip-to-content link on every page.
- Per-example social-card images composed from each example's marginalia figure (`make social-cards`), referenced by `og:image`/`twitter:card` on home and example pages and checked by the SEO linter.
- Learner-behavior report (`scripts/learner_report.py` + `docs/learner-analytics.md`) aggregating exported Worker wide events into most-read pages, most-run examples with edited/error shares and execution percentiles, journey traffic, and missing-example 404s.
- Content gates for program/cell parity, prose duplication, and internal inline links, wired into `make quality-checks`.
- Shared inline-prose rendering, figure XML/caption contracts, regenerated figure-review prototypes, and behavioral tests for the Turnstile and ASGI paths.

### Changed

- Journeys now reference every example: `iterator-vs-iterable`, `classmethods-and-staticmethods`, `bound-and-unbound-methods`, `abstract-base-classes`, and `structured-data-shapes` joined their natural sections, with journey-outcome support lists updated.
- Journey meta descriptions no longer claim gap placeholders; all previously declared gaps are filled.
- Python tooling is pinned to 3.13 through `uv`; CI and preview workflows are hardened, generated-file recovery retries from a clean worktree, and quality gates enforce live registry/score invariants.
- Worker runtime hardening adds body limits, cache-key normalization, constant-time smoke-bypass comparison, fail-closed Turnstile modes, latin-1 ASGI headers, and once-per-isolate lifespan startup.
- Content corrections across 29 example pages improve Python accuracy, executable demonstrations, sandbox-boundary framing, and link/prose quality.

## 2026-05-16

### Added

- Production custom domain `www.pythonbyexample.dev` (with `workers.dev` as fallback).
- Learning journeys: curated multi-example arcs with per-section learner outcomes and a journeys index.
- Marginalia figure system: a locked SVG diagram grammar (`src/marginalia_grammar.py`), curator-owned example-cell figures and journey section figures (`src/marginalia.py`), and gestalt review pages under `/prototyping/*`.
- Figure geometry contract tests covering clipping, collision, palette, caption uniqueness, and anchor resolution for every registered figure.
- Quality registries (`docs/quality-registries.toml`) with criterion-level scoring, confusable-pair checks, footgun coverage, no-figure rationales, journey outcome contracts, and enforced quality-score gates.
- Optional Turnstile protection for edited-code runs: secret-gated, session-scoped clearance cookie, Invisible-mode widget loaded only when the server requires a challenge, and a smoke-test bypass header.
- Structured wide-event observability for the Worker, with smoke checks asserting the custom event payload.
- Deployment smoke script (`scripts/smoke_deployment.py`) checking rendered pages and representative Dynamic Worker POST runs.
- Footer link to the GitHub repository.
- MIT license.
- SEO metadata for the home page and all example pages.
- SEO/cache linter for future page additions.
- Browser layout regression check for Shiki-rendered code blocks.
- CodeMirror-powered editable example editor with textarea fallback.
- Execution-time display below run results with reserved space to avoid layout shift.
- Literate source/output cells for example walkthroughs.
- Fingerprinted CSS/JS assets and generated asset manifest.
- Versioned Worker Cache API keys for rendered HTML.
- `README.md` architecture, verification, deployment, and cache-busting documentation.
- `docs/lessons-learned.md`.
- Markdown-backed example sources with `:::program` and `:::cell` blocks.
- Example source verifier, formatter, embedded-source build step, and golden parity check.
- GitHub Actions verification workflow.
- `iterators` and `generator-expressions` examples to make the Iteration arc explicit.
- Syntax coverage examples for loop control, loop `else`, assertions, deletion, scope rebinding, positional-only parameters, assignment expressions, `yield from`, exception chaining/groups, advanced match patterns, inheritance, metaclasses, async iteration/context managers, import aliases, and specialized operators/literals.
- Optional `see_also` example graph links with validation tests.
- `Protocol` example covering structural typing and its boundary with inheritance.

### Changed

- Example walkthroughs now pair prose, source fragments, and output evidence.
- Iteration examples now frame Python iteration as a value-stream protocol: producers, consumers, eager containers, lazy streams, and one-pass iterators.
- The quality rubric now requires explicit syntax-surface coverage and graph-style conceptual links for neighboring examples.
- Read-only code highlighting is handled by Shiki; editable code highlighting is handled by CodeMirror.
- Prototype routes under `/layout-options/*` bypass the Worker Cache API and return `Cache-Control: no-store`.
- Static assets use immutable cache headers only on fingerprinted filenames.
- Deployment flow now regenerates embedded example data and asset fingerprints first.
- `src/examples.py` is now a compatibility shim over Markdown example sources.
- Output panels reserve space for execution timing to prevent layout shift after runs.
- Removed the Workers journey and folded its runtime-boundary guidance into the affected examples' local notes.

### Fixed

- Shiki line rendering no longer creates visual blank rows beside the orange code rail.
- Prototype pages no longer serve stale HTML from the Worker Cache API.
- Normal cached HTML is busted when app/templates/examples/assets change.
- Source and output fragments now use consistent orange-rail spacing.

## 2026-05-04

### Added

- Initial Cloudflare Python Workers + FastAPI app.
- Dynamic Worker execution for editable Python examples.
- 50 Python 3.13 examples linked to official Python documentation.
- Expected output for every example.
- Previous/next example navigation.
- Workers Assets configuration for favicon and static assets.
- Cache API support for GET-rendered HTML pages.
- Research and quality documents:
  - `docs/example-quality-rubric.md`
  - `docs/literate-programming-inspiration.md`
  - `docs/research-similar-sites.md`
- Example quality scoring script.

### Changed

- Targeted Python 3.13 instead of unsupported Python 3.14.
- Refined UI toward a low-chrome literate-programming style inspired by Go By Example and Rust By Example.
- Extracted templates and CSS from inline Python strings.

### Fixed

- Edited example submissions now use URL-encoded POST bodies so edited code is actually executed.
- Dynamic Worker reuse is keyed by Python version, example slug, and code hash.
- POST example runs are not cached.
