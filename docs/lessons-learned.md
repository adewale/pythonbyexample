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
- Beware broad-surface titles that quietly teach only one narrow slice. Pages named `Testing`, `Packages`, `Regular Expressions`, `Type Hints`, `Async Await`, or `Special Methods` must either cover the forms a reader reasonably expects or explicitly frame themselves as a first pass and link to focused neighbors.
- Do not let an important syntax form live only in a separate page if another page title strongly implies it. An umbrella `Operators` page should at least point to and lightly show `:=`, even though `Assignment Expressions` remains the focused lesson.
- Journey order should follow prerequisite thinking, not catalog order. Put booleans before truthiness and conditionals, scope before closures, bytes before networking, and environment boundaries before subprocess/thread boundaries.
- Runtime-boundary caveats should not become the hero. For Dynamic Worker limitations, teach normal Python first and state the constraint once in the marked boundary cell.
- Algebrica's useful editorial principle is “reduce without distorting.” Python examples should be compact, but not so compressed that the concept loses its necessary contrast, edge case, or progression.
- Broad examples need a visible learning arc. If a page reads like a tray of samples, either add a map-like progression or split it into narrower examples.
- Keep teaching artifacts inspectable. Markdown sources, editable programs, teaching cells, expected output, and diagrams/screenshots should be clean enough to serve as public educational material, not just implementation input.

### Broad-surface audit notes

- `Operators and Literals`: fixed by splitting it into `Operators` and `Literals`, then adding `:=` surface coverage and a `See also` link to `Assignment Expressions` from `Operators`.
- `Special Methods`: fixed by keeping the entry page small and adding focused data-model pages for truth/size, containers, callables, operators, and attribute access.
- `Testing`: fixed by replacing boilerplate with arrange/assert/run structure and explicit scoping to the smallest `unittest` loop.
- `Packages`: fixed by splitting package-as-module, dotted imports, and dynamic import into separate cells.
- `Regular Expressions`: fixed by separating repeated extraction, first-match groups, and the string-method alternative.
- `Async Await` and `Type Hints`: acceptable for now because both state their boundaries and are supported by focused neighboring examples/journeys.

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
- A full rubric audit is broader than `make verify`. Pair the ordinary pre-push set with `make quality-checks`, `python3 -m unittest tests.test_marginalia_geometry -v`, and `scripts/audit_example_graph.py --check` so example quality, figure grammar, journey outcomes, and graph connectivity are checked as separate ledgers.

## Documentation and GitHub readiness

- Keep generated runtime directories out of Git: `.wrangler/`, `.venv/`, `.venv-workers/`, and `python_modules/`.
- Keep `README.md` focused on how to understand, verify, and deploy the project.
- Keep this lessons document updated when a bug reveals a general rule.
- Record user-visible changes in `CHANGELOG.md` before significant commits or releases.

## Visualisations and marginalia

- **A diagram set needs a grammar, not a collection of one-off layouts.** Hand-drawn SVGs drift in stroke weight, cell size, type-tag placement, arrow style. A locked `Canvas` grammar (palette, tokens, words, phrases, metrics) makes drift structurally impossible. Cards declare figures by composing primitives; the library guarantees consistency.
- **Emit explicit `width`/`height` on every SVG; use `max-width: 100%` in CSS, never `width: 100%`.** Without `width`/`height` the browser stretches a small viewBox to fill its container, doubling text inside. This was the root cause of every "figure too big" report. The fix lives in `Canvas.to_svg()` and the CSS rules in `public/site.css`, `scripts/build_prototypes.py`, and `scripts/build_marginalia.py`.
- **A figure's diagrammatic content must not duplicate its figcaption.** SVGs may carry functional labels (`stdout`, `iter()`, panel tags like `before` / `after`, type signatures like `x: int | str | None`). Full sentences describing the figure as a whole are prose and belong in the figcaption. Captions are the canonical voice. The exception is review-only pages (`marginalia-gestalt`) where cards have no figcaption; figures destined for promotion to production must drop their inline prose first.
- **Emphasis is scarce.** With site `--accent` saturated for UI use, a coral arrow on every line reads as no emphasis at all. `closed_arrow` defaults to `emphasis=False`; figures opt in only for the single element the prose names. Same rule for accent dots, gates, and ring highlights.
- **Soft fills should be neutral, not accent-tinted.** A 5% warm-brown tint reads as a quiet container. An accent-tinted soft fill makes every object box look highlighted, which breaks the scarcity rule a second way.
- **Two rubrics, one craft section.** Journey-section figures depict a *conceptual shift* across multiple lessons; example-cell figures depict the *single move* the surrounding cell discusses. `docs/journey-visualisation-rubric.md` and `docs/example-figure-rubric.md` score each on 10 points: content fidelity, craft, context. Topic gates per kind of section / cell shape.
- **Constraint-shaped sections can improve when the constraint is drawn as a boundary, not a caveat.** Workers' runtime sections originally scored below target when the figure merely said an API was unavailable. They became rubric-complete once the diagrams showed the standard Python contract, the Worker boundary, and the portable evidence that preserves the lesson. If a constraint-shaped section cannot be reframed this way, then use the no-figure rationale registry instead of shipping a weak mechanism picture.
- **Authoring stays on the contributor; figures stay on the curator.** Example markdown does not include figure references. `src/marginalia.py` holds `FIGURES` (paint functions) and `ATTACHMENTS` (slug → cell → figure → caption). Curating figures is a single-file edit that contributors never see.
- **Inline between prose and code is the production layout; banners between cells is the prototyped richer grammar.** Cells with figures drop to single-column stacking (prose, figure, code) via `.lp-cell.has-figure { grid-template-columns: 1fr }`. Cells without figures keep today's `prose | code` 2-column grid bit-for-bit. The banner-between approach (`/prototyping/layout-banner-*`) supports multi-figure small-multiples between cells when one inline figure isn't enough.
- **Centralised gestalt pages catch drift that page-by-page review misses.** `/prototyping/marginalia-gestalt`, `/prototyping/journey-figures-gestalt`, and `/prototyping/production-figures-gestalt` show every figure in three different framings. Seeing all section figures of a journey in one 3-up row exposes inconsistencies invisible across six tabs.
- **Mapping reuses existing figures; promoting moves design to production.** Half of example coverage came from attaching existing FIGURES to new examples (no paint code). The other half from new paint code copied or designed from gestalt cards. Both paths must pass the rubric.
- **Tests against the cell layout must allow the `has-figure` class.** When the renderer adds `has-figure` to cells with attached figures, assertions on the literal string `class="lesson-step lp-cell"` fail. Change those tests to check the substring `lesson-step lp-cell` so both variants match.
- **Score what's shipping, not what was designed.** A scoring dict on the gestalt is design-time review. Production figures live in `src/marginalia.py` `FIGURES` and may have been redesigned during promotion. Scoring should track the production version with the gestalt as separate history.
- **Semantic diagram review has four objects: page, cell, paint function, caption.** Geometry contracts can prove that a figure renders, but not that it still teaches the adjacent cell. On every diagram pass, read the current example cell, the attached paint function, the caption, and the score rationale together. The same audit caught `container-protocols` still showing `iter()/next()` after the page had shifted to `__setitem__`/`__contains__`/`__getitem__`, `structured-data-shapes` over-focusing on `TypedDict` while anchored to a dataclass cell, and `object-lifecycle` mentioning `__del__` after the lesson had been reframed around references.
- **Some examples should never have figures.** Constraint-shaped, infrastructure-shaped, and aggregator-shaped slugs lack a single mechanism to depict. Force-fitting figures on them scores below the gate. Leave them figure-less and document why rather than ship weak figures.
- **Audits without contracts rot; bug classes need automated gates.** When you find a bug class — clipping, collision, off-palette colour, drifting twin coordinates, duplicate caption — write a unit test that asserts the invariant across every figure. The geometry contracts in `tests/test_marginalia_geometry.py` started as ad-hoc scripts and were promoted to CI gates after the same bug class recurred. 54 tests today cover 9 contract families; new figures pass them automatically because each test iterates `FIGURES`.
- **Clipping ≠ collision; padding the viewBox fixes one but not the other.** The `value-types` bug had two components: the first `INT` tag was clipped above the viewBox (geometry escapes its frame), and the `STR`/`LIST`/`DICT` tags overlapped the boxes above them (geometry collides internally). Padding the viewBox solved (1) and disguised (2). Element-element collision needs its own audit that walks every text-rect, text-text, and (for label-on-edge cases) text-line bounding-box pair.
- **Heuristic audits over-flag; trust the design, not the regex.** Probes for "prose duplication" (SVG text matching caption substring), "text crossing a line" (label bbox bisected by a hairline), and "text overlapping a circle" each surfaced ~3-10 hits — all false positives. Diagrammatic labels naturally appear in captions (`__getattr__`, `yield from inner`); dashed strikes through `.append` are deliberate; text inside node circles is the design. Don't promote heuristic findings to contracts without confirming each is a real bug.
- **Structural twins must share coordinates exactly.** When two figures depict parallel concepts — `kw-only-separator` and `positional-only-separator`, `class-triangle` and `metaclass-triangle` — they read as a pair. A single-pixel drift in one breaks the visual rhyme. Treat a coordinate change in one as a forced change in both, in the same commit. The audit caught `kw-only-separator` at the old `x=82` after `positional-only-separator` had moved to the corrected `x=75`.
- **Reused figure → bespoke caption per slug, and revalidate reuse after page rewrites.** The 8 library figures (`iter-protocol` across iteration slugs, `aliasing-mutation` across mutability + copying-collections, etc.) shouldn't all carry the same caption. Each slug is a separate lesson; the figure stays, the framing changes. But reuse also has an expiry date: if the page's teaching cell changes topic, the old reusable figure may become semantically wrong even while tests pass. `FigureCaptionContract` enforces uniqueness; semantic review enforces fit.
- **One paint registry, not two.** The marginalia-gestalt review page once rendered its own `e_*` paint functions parallel to `src/marginalia.py FIGURES`. Reviewers saw a different picture than readers, and the gestalt's bugs (overlapping labels, misaligned dashed lines) didn't ship. The gestalt is now a thin view over production: same paint, same drift surface, same audit coverage. 862 lines of duplicated paint code went away.
- **Tag-above vs tag-inside is a layout decision driven by stacking.** `object_box(tag_position="above")` is natural for an isolated box; `tag_position="inside"` is required when boxes stack vertically with less than ~13px of gap (the tag's footprint). Defaults to `"above"` for the common isolated case; stacked callers opt in. The grammar carries the choice, not the caller's hand-positioned `tag()` call.
- **Mono character alignment uses the font's advance, not eyeballed pixels.** JetBrains Mono advances ~6px per char at fs=10. A dashed line marking the `/` at index 12 of `def f(a, b, /, c, d): …` lives at `x=12*6+3=75`, not `x=82`. Hand-tuned positions drift; computed positions match the rendered glyph.
- **Lines must terminate AT elements, not in their gaps or interiors.** A 1.5px gap between a tree edge and a leaf dot reads as "the tree is disconnected" (the `exception-group-peel` bug). A line endpoint 2px inside a circle reads as "the arrow pierces the node" (the `context-bowtie` bug). When connecting to a dot, end the line at the dot's centre and let the dot draw on top — the visual termination is the circumference, with zero gap or overshoot.
- **Journey pages render section figures inline.** `SECTION_FIGURES` lives in `src/marginalia.py` (single source of truth, keyed by section title) and `render_for_section(title)` is invoked from `render_journey_page` between each section's meta and its example list. The same paint code that produces the `/prototyping/journey-figures-gestalt` review page renders on production journey pages; drift between the two is structurally impossible. Contract 10 asserts every section in `JOURNEYS` has a figure and every figure name resolves.
- **An explicit comparison loop should iterate over the topic's whole spectrum.** When a cell teaches by doing `for label, value in [(...), (...)]: print(...)`, the bracketed list IS the lesson. Two items is a binary contrast; three items reads as a progression. The strings example presented English (pure ASCII, 1 byte/char) against Thai (3 bytes/char) but skipped the Latin-extended middle (French `café`: 4 code points, 5 bytes — `é` is 2 UTF-8 bytes). Adding the middle row turned the cell from "ASCII vs non-Latin" into "1-byte / 2-byte / 3-byte progression." The rule is narrow — most examples spread categories across cells, which is also a valid pattern — but when a comparison loop exists, fill it with the topic's actual spectrum, not just the endpoints.
- **Quality debt must be tracked, not normalized away.** `docs/example-quality-rubric.md` sets a 9.0 target and `scripts/check_quality_scores.py` enforces the score registry: pages below the hard minimum need a concrete improvement backlog entry, stale backlog entries fail once a page clears the gate, and Hello World is the only standing waiver because first examples are traditionally tiny. A score below target is allowed only when the remaining work is named.
- **No-figure decisions need a registry.** Some examples should not have figures, but that cannot be an invisible omission. `scripts/check_no_figure_rationales.py` validates `no_figure_rationales` so future constraint-shaped pages can opt out explicitly instead of shipping weak diagrams.
- **Journey sections need outcome contracts.** `scripts/check_journey_outcomes.py` ties each journey section to learner outcomes and support examples so journey pages stay mental maps rather than catalog slices.
- **Opaque scores hide the next move.** `scripts/score_example_criteria.py` breaks each page into rubric criteria so quality work can target decomposition, boundaries, source/result pairing, graph support, or practical payoff directly. The bottom-28 pass showed that most misses were boundary/neighbor problems, not syntax problems. `docs/quality-search.md` records the hill-climbing and simulated-annealing loop for escaping locally tidy but globally weak page shapes.
- **Audit across dimensions, not just artifacts.** A serious pass reads examples for payoff, rationale, alternatives, determinism, idiom, literate fit, source/result pairing, decomposition, progression, coverage, usefulness, and editorial shape; reads figures for cell fidelity, earned value, one move, mechanism, caption voice, grammar, emphasis, restraint, and fit; and reads journeys for section fidelity, scope, conceptual move, independence from lesson figures, outcome support, and prerequisite order. File-by-file review misses cross-cutting failures that dimension-by-dimension review catches.
- **When every score is green, resist score inflation and look for unsupported claims.** The current steady state is intentionally boring: one documented `hello-world` waiver, no below-target example diagrams, no below-target journey figures, no orphaned examples, and no stale weak-section backlog. Future audits should preserve that baseline by finding semantic drift, note claims without cells, weak `See also` edges, or journey sections that no longer match their support examples — not by raising 9.0 scores to 9.5 without new evidence.
- **Journey audit is graph audit plus outcome audit.** A journey section is healthy only when its examples form a prerequisite-respecting mental map and its declared outcomes are backed by cells on those examples. A section can have a beautiful figure and still fail if the support list is a catalog slice, if the `See also` graph isolates one example, or if the section caption describes a conceptual shift the examples do not actually make.
- **A green total can still hide a weak criterion.** The journey-figure audit found every section figure above the project gate while 15 sections still reused a lesson paint function, which weakened the independence-from-lesson-figures dimension. Bespoke runtime, control-flow, iteration, types, and reliability section figures cleared that watchlist; keep tracking criterion-level weakness even when the aggregate score remains shippable.
- **Deployment smoke belongs beside CI.** `scripts/smoke_deployment.py` checks rendered Worker pages, runtime-boundary pages, journey pages, prototype review pages, and representative Dynamic Worker POST runs for HTTP failures, exception markers, and stale edited-code output. Build success is not enough; the deployed Worker must render and execute edited examples.
