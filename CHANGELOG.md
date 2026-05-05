# Changelog

All notable changes to Python By Example are documented here.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses date-based release notes while the app is pre-1.0.

## Unreleased

### Added

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

### Changed

- Example walkthroughs now pair prose, source fragments, and output evidence.
- Read-only code highlighting is handled by Shiki; editable code highlighting is handled by CodeMirror.
- Prototype routes under `/layout-options/*` bypass the Worker Cache API and return `Cache-Control: no-store`.
- Static assets use immutable cache headers only on fingerprinted filenames.
- Deployment flow now regenerates asset fingerprints first.
- Output panels reserve space for execution timing to prevent layout shift after runs.

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
