# Codebase audit — 2026-06-11

Full audit of code, docs, and internal consistency, plus improvement
suggestions. Method: every source file, script, workflow, doc, and all 109
example sources were read in full; the verify pipeline, tests (90/90 pass),
quality gates, and example verification were executed under Python 3.13;
high-severity claims were re-verified directly before inclusion.

Severity legend: **high** = user-visible defect, broken workflow, or gate that
cannot do its job; **med** = real defect or drift with limited blast radius;
**low** = latent bug, hygiene, or polish.

## 1. Verified-healthy baseline

These were checked and are in good shape — worth knowing what *not* to spend
time on:

- All 90 unit tests pass; all 109 examples execute with byte-exact outputs
  under 3.13; golden parity reports 100%; `ruff` clean; generated files and
  `uv.lock` fresh.
- Manifest ↔ files ↔ journeys ↔ `see_also` graph: zero broken references,
  no duplicate titles/slugs, every example has `see_also`, every journey item
  resolves.
- XSS surface is sound: every dynamic template substitution is
  `html.escape`d; user code reaches only escaped sinks and the dynamic Worker
  via `repr()`; `editor.js`/`syntax-highlight.js` use `innerHTML` only on
  trusted markup. All 28 template tokens are supplied.
- The Dynamic Worker sandbox is locked down correctly (`globalOutbound:
  null`, `disable_python_external_sdk`, `subRequests: 0`, `cpuMs: 1000`) and
  consistent between `src/main.py` and `wrangler.jsonc`.
- `docs/observability-spec.md` and `docs/turnstile-runner-protection-spec.md`
  match the implementation nearly line-for-line; CHANGELOG spot-checks
  against git history hold; CI (`verify.yml`) runs exactly the documented
  pre-push command set.
- All 123 marginalia figures render well-formed XML, use no `id` attributes,
  and all 24 geometry contracts pass; all current figure anchors resolve.

## 2. Bugs in code

- **med** `tests/test_marginalia_geometry.py:470` — the figure-anchor
  contract validates anchors against `ex["walkthrough"]`, but
  `src/app.py:739-760` renders `ex["cells"]`. The two lists diverge on 10 of
  109 examples in both directions (loader emits one walkthrough entry per
  prose paragraph and drops `unsupported` cells). A `cell-4` anchor on
  `datetime` would pass the contract yet never render; a valid `cell-1`
  anchor on `virtual-environments` would be falsely rejected. Latent today —
  all current anchors happen to resolve against the real cell list.
- **med** `src/marginalia_grammar.py:203-210` — `Canvas._text` interpolates
  figure-internal text into SVG without XML escaping (captions are escaped;
  internal labels are not). A future label containing `<` or `&` ships
  malformed markup silently; no test parses the SVG with an XML parser. All
  123 current figures verified well-formed, so latent.
- **med** `src/worker_asgi_bridge.py:264` — `server.onopen = onclose`
  (should be `server.onclose = onclose`) in the websocket path. Unused by
  the app today; latent vendored-code bug.
- **med** `scripts/check_notes_supported.py:48` — `NOTE_RE.search` examines
  only the first `:::note` block, while the loader supports any number and
  README/CONTRIBUTING say "blocks" plural. Bullets in a second block are
  never checked and additionally count as page "body" that can ground
  bullets in the first. Latent — no current page has two note blocks.
- **low** `src/app.py:430-433` + `770-791` — `_replace` applies
  `str.replace` sequentially and `html.escape` preserves `__TOKEN__` text,
  so user-submitted code containing a literal template token (e.g.
  `__SHOWN_OUTPUT__`) gets later substitution values injected into the
  echoed editor content. Verified by simulation. Not XSS (textarea is
  RCDATA; injected values contain no `</textarea>`), but round-tripped code
  is silently corrupted.
- **low** `src/app.py:790` + `src/templates/example.html` —
  `ORIGINAL_CODE_JSON` uses `json.dumps` with no `<`/`/` escaping inside an
  inline `<script>`. A curated example whose program contained `</script>`
  would break the page. Not user-controllable (the slot always carries
  curated code); fix by escaping `<` as `<`.
- **low** `scripts/lint_seo_cache.py:19,43` — the hashed-asset regex and the
  unfingerprinted-reference check cover `site.css` and `syntax-highlight.js`
  but omit `editor.js`, one of the three fingerprinted assets the lint
  exists to protect.
- **low** `src/worker_asgi_bridge.py:55,171` — header bytes are
  encoded/decoded as UTF-8; the ASGI spec uses latin-1. ASCII-safe today.
- **low** `scripts/capture_browser_screenshot.mjs:8` — `CHROME_PATH`
  defaults to the macOS app path unconditionally; the sibling
  `check_browser_layout.mjs` correctly switches on platform.
- **low** `scripts/verify_examples.py:55` — a frontmatter `slug` that
  doesn't match its filename crashes with a `FileNotFoundError` traceback
  instead of a clean per-file error (the spec calls slug↔filename matching a
  required check).

## 3. Security

- **med** `.github/workflows/preview.yml:50-55` — `${{ inputs.name }}` is
  interpolated directly into `run:` scripts in steps whose env contains
  `CLOUDFLARE_API_TOKEN`. A dispatch input like `x$(curl …)` executes in the
  shell and can exfiltrate the token. Limited to users with workflow-dispatch
  rights; standard fix is passing inputs via `env:`.
- **med** `public/_headers` + `src/main.py` — no security headers anywhere on
  Worker HTML: no CSP, `X-Content-Type-Options`, `X-Frame-Options`/
  `frame-ancestors`, `Referrer-Policy`, or HSTS. Defense-in-depth gap on a
  site that reflects user-submitted code; the Run button is clickjackable.
- **low** `src/main.py:134` — the smoke-bypass header is compared with `==`
  rather than `hmac.compare_digest` (the clearance-cookie path uses
  `compare_digest` correctly).
- **low** `src/main.py:159-165` — `_requires_turnstile` fails open: any
  unrecognized `TURNSTILE_CHALLENGE_MODE` value (e.g. a typo of `session`)
  silently disables the challenge.
- **low** `src/main.py:137-156` — the clearance cookie signs only the expiry
  integer: an unbound, replayable bearer token for its lifetime (8 h default,
  7 d max). Consistent with "once per session" intent; noting the design.
- **low** `src/main.py:191-264` + bridge — no application-level size limit on
  POSTed code, and the ASGI bridge buffers the entire request body in memory
  before the app runs; bounded only by platform caps.
- **low** `src/main.py:77-88` — every distinct query string on a cacheable
  GET creates a separate edge-cache entry for an identical body (the app
  ignores the query). Amplification, not poisoning — the appended
  `__html_v` is always the real version.
- **low** `src/templates/example.html` — `#code=<base64>` prefills the
  editor from the URL hash. Not XSS (string assignment), and execution still
  passes Turnstile + sandbox; limited to social-engineering a sandboxed run.
- **low** `src/main.py:428-434` — non-200 responses on the cacheable GET
  path get no `Cache-Control`, allowing browser heuristic caching of error
  pages.

## 4. Toolchain, build, and CI

- **high** `Makefile` + `README.md:66` — only `test` and
  `verify-python-version` run through `uv run --python 3.13`; every other
  target (`build`, `verify-examples`, `seo-cache-lint`, all quality checks)
  invokes scripts via `#!/usr/bin/env python3` shebangs. On any machine whose
  system python isn't 3.13, `make verify` dies on the first example using the
  3.12+ `type` statement — while README explicitly claims "a system `python3`
  on another version still works." Reproduced under python 3.11.
- **med** `Makefile:70` — `make dev` runs `uv run pywrangler dev` without
  `--group workers`; `pywrangler` lives in the `workers` dependency group, so
  the documented target fails on a fresh checkout. README/CONTRIBUTING give
  the correct `uv run --group workers …` command.
- **med** `.githooks/post-merge`, `.gitattributes:7` — the conflict-avoidance
  machinery covers `src/asset_manifest.py` only; `src/example_sources_data.py`
  is equally generated and conflicts on every concurrent example edit, with no
  `merge=ours` driver and no hook regeneration. Hooks should run `make build`
  and `.gitattributes` should cover both files.
- **med** `.github/workflows/regenerate-generated-files.yml:32-43` — builds
  from the triggering SHA, then `git pull --rebase` before pushing: a
  mid-run push can land stale regenerated files on main (GITHUB_TOKEN pushes
  skip CI), and the next self-heal run hits a rebase conflict because the
  `merge=ours` driver is never configured in CI. Rebuilding after the pull
  closes the race.
- **med** `Makefile:12` vs that workflow — `check-generated` diffs only
  `example_sources_data.py`, `asset_manifest.py`, and `public/_headers`; new
  or stale fingerprinted copies under `public/` are invisible to it (the
  regenerate workflow stages all of `public/`), so a PR can pass with
  `public/` out of sync and only self-heal after merge.
- **low** `verify.yml:3-5` — `push` + `pull_request` triggers double-run
  every same-repo PR push (each run boots a Worker and Chrome and executes
  all 109 examples several times); no `concurrency` group, no `permissions:`
  block (the other two workflows set one).
- **low** `verify.yml:24` vs `preview.yml:41` — verify pins
  `wrangler@4.90.0`; preview uses unpinned `npx --yes wrangler`, so the two
  workflows can exercise different Wrangler majors.
- **low** `preview.yml` + `scripts/smoke_deployment.py:109` —
  `PBE_SMOKE_BYPASS_SECRET` is set nowhere in CI, so POST smoke checks will
  false-fail the moment Turnstile secrets are enabled on the target worker;
  the script also doesn't require https for the origin it sends the secret
  to.

## 5. Quality-gate integrity

The editorial gate layer is partly decorative — several documented gates
cannot fail or are enforced nowhere:

- **high** `scripts/score_example_criteria.py:105-119` — `main()` returns 0
  unconditionally (`--below`/`--limit` only filter printing), yet it is wired
  into `make quality-checks` → `make verify` as if it were a gate. Verified:
  `--below 99` still exits 0.
- **med** `scripts/check_quality_scores.py:64` +
  `docs/quality-registries.toml:191` — waiver `expires` is only checked to be
  a non-empty string; the one shipped waiver says `expires = "never"`. Same
  for `review_after` in `check_no_figure_rationales.py`, whose docstring
  claims it prevents stale entries. A waiver whose score recovers is never
  flagged (backlog entries are).
- **med** `docs/quality-registries.toml:185` — `journey_average_min = 8.8`
  is declared under `[quality_gates]` but read by no script, source file, or
  test.
- **med** `docs/quality-registries.toml:172-180` — `paired_pages` documents
  "at least one member of each pair must demonstrate the relationship in a
  cell"; the only consumer validates slug existence. The actual rule is
  unenforced.
- **med** `scripts/check_confusable_pairs.py` + registry — several token
  sets are degenerate and unfailable: `"def "` is a substring of every
  `"async def "`, so the sync-vs-async pair can't detect loss of sync
  content; `"return"`, `"list"`, `"tuple"`, and `" is "` match ordinary
  prose.
- **med** `src/marginalia.py:2331-2449` — the only fail-able content gate
  keys off hand-edited numbers (`EXAMPLE_QUALITY_SCORES`), with no range
  validation and no bound on curated-vs-heuristic delta; scores have
  collapsed to near-constants (108×9.0 + one 7.1), so the registry no longer
  discriminates.
- **low** `scripts/audit_rubric_snapshot.py:150-338` — hardcodes all 32
  dimension verdicts as PASS, the scoreboard line, the entire "audit
  conclusion" paragraph, and `--date` defaults to 2026-05-12. It is a report
  generator labeled as an audit; re-running it after real drift would
  regenerate a document asserting facts it never checked.
- **low** `scripts/audit_example_graph.py` — the only check-style script
  wired into no Makefile target and no workflow; its unique value (out-degree
  cap, orphan detection) is never enforced. Its `--check` help text is also
  wrong about what fails without the flag.
- **low** `scripts/check_broad_surface_tours.py:44-49` —
  `scope_first_pass = true` bypasses required tokens if `see_also` is merely
  non-empty; the registry declares no expected neighbors, so the documented
  contract isn't what's checked. Latent (no page sets the flag).
- **low** spec-required checks that exist nowhere: line-length enforcement
  for code/prose (`docs/example-source-format-spec.md` "strict tooling"),
  and slug↔filename verification (crashes instead; see §2).
- **low** `public/prototyping/*.html` — 6 of 7 committed gestalt review
  pages are stale relative to their generators (missing
  `aria-hidden`/`focusable` attrs, old y-offsets); `check-generated` doesn't
  cover them and no workflow rebuilds them, despite
  `docs/example-figure-rubric.md:169-172` declaring "gestalt = production" a
  release gate.

## 6. Example content (109 files read)

User-visible defects:

- **high** `src/example_sources/special-methods.md:241,277` and
  `async-await.md:117` — four inline markdown links (`[container-protocols]
  (/data-model/container-protocols)`, `[callable-objects](…)`,
  `[context-managers](…)`, `[async iteration and context]
  (/iteration/async-iteration-and-context)`) are doubly broken:
  `render_inline()` only converts backticks, so they render as literal
  bracket text on the live pages, and the paths use section-style prefixes
  that don't exist as routes (examples live at `/examples/<slug>`).
- **med** `dicts.md:89,108` — "Mutating a dictionary while iterating it
  raises RuntimeError" (stated twice) is overbroad: only size-changing
  mutation raises; reassigning an existing key's value during iteration is
  legal (verified on 3.13). The code only demonstrates deletion.
- **med** `type-hints.md:136-158` — teaches `typing.TypeAlias`
  ("Reach for `TypeAlias` when…") without noting it is deprecated since
  3.12; the sibling `type-aliases.md` correctly presents the PEP 695 `type`
  statement as the modern form. The two pages contradict each other on the
  current idiom.
- **med** `subprocesses.md`, `threads-and-processes.md`, `networking.md` —
  each contains an `:::unsupported` fragment declaring the code "runs in
  standard Python only — the … runner does not provide …" immediately
  followed by an executable `:::cell` running the identical code with
  verified output, and a note claiming the evidence was produced "without
  spawning a process" (it was produced by spawning one at verify time). The
  sandbox-vs-verifier distinction is real but the wording contradicts
  itself.
- **med** `operators.md:143-161` — the short-circuit cell is entirely absent
  from the `:::program` block (the page convention everywhere else is
  program ⊇ cells), so the editable program can't reproduce that cell.
  Same drift, smaller: `numbers.md` (program defines unused `ratio`, cell
  prints it), `decorators.md` (program omits the `__doc__` print).
- **med** `unpacking.md:66-68` — the same paragraph appears verbatim twice
  in a row in cell 3; all three cell prose blocks are copies of the intro.
  Similar copy-paste residue: `hello-world.md` (intro ≡ cell prose ≡ note),
  `truthiness.md` (cells 2/3 share prose that doesn't describe cell 3),
  `sets.md` note (same guidance twice in one list).
- **med** `operator-overloading.md:27-65` — the note says "Return
  `NotImplemented` when an operand type is unsupported," but the
  demonstrated `__eq__`/`__add__` do the opposite: `Vector(1, 1) == 5`
  raises `AttributeError` (verified). The page teaches the anti-pattern its
  own note warns against.
- **med** `positional-only-parameters.md:54-63` — the `clamp=True` demo
  outputs the same value as the unclamped call (4·2 never reaches the
  clamp), and the page never demonstrates the titular restriction (no cell
  shows `scale(value=4)` raising `TypeError`).
- **med** `special-methods.md:212-237` — restores `__hash__` on a mutable
  `Bag` whose hash derives from mutable state, without the standard warning;
  after `bag[1] = "z"` the object can't be found in a set containing it
  (verified). Also claims `sorted()` needs "the rest of the order family"
  (only `__lt__` is required), and the example's `__lt__` (by length) is
  incoherent with its `__eq__` (by contents).
- **med** `exceptions.md:101-124` — the broad-`except` hazard cell calls
  both broken and fixed versions on input `"42"`, where they behave
  identically; the claimed hazard is asserted but never demonstrated.
- **med** `constants.md:6` — `doc_path` points at the class
  scopes/namespaces tutorial section, which says nothing about the all-caps
  convention or `Final`.
- **low** `attribute-access.md:47` — prose says "Calling `object.__setattr__`
  avoids recursing through your own hook" on a cell with no `__setattr__`
  hook; the technique appears two cells later.
- **low** `bound-and-unbound-methods.md` — the title and `unbound` variable
  use Python 2 vocabulary the page's own body correctly refutes, without
  noting the term is historical.
- **low** `regular-expressions.md:107` — overstates `re.compile`'s benefit
  ("skip the parser on each call… when the same pattern runs in a loop");
  module-level `re` functions cache up to 512 compiled patterns.
- **low** `string-formatting.md:55` — "padded to one decimal place"
  conflates `05` (zero-pad to width 5) with `.1f` (precision) in the page's
  only explanation of the format-spec mini-language.
- **low** `comprehensions.md:64-74` — prints a bare set despite the site's
  own sorted-display convention (established in `sets.md`); the set
  comprehension shown is a no-op transformation.
- **low** `match-statements.md` — built on mapping patterns but never warns
  they match on a key subset (extra keys are ignored), the standard footgun.
- **low** `keyword-only-arguments.md:15` — "Callers must name those
  arguments explicitly" is never evidenced; all cells are happy-path.
- **low** `bytes-and-bytearray.md:4` — `section = "Basics"` while its
  manifest neighbors `strings`/`string-formatting` are `"Text"`, splitting
  the encoding story across sections.
- **low** `generics-and-typevar.md`, `paramspec.md` — teach only the
  pre-3.12 `TypeVar("T")`/`ParamSpec("P")` spellings with no mention of
  PEP 695 native syntax, while `type-aliases.md` showcases PEP 695 — an
  inconsistent modernity story within the Types section.

## 7. Figures / marginalia

- **med** `src/marginalia.py:1932-1935,2257` — the while-loops figcaption
  asserts "the back-edge returns to the test each pass" and its score
  commentary says "back-edge mechanism", but the attached figure draws three
  forward arrows and no back-edge (verified by rendering). Caption and score
  describe a figure that doesn't exist — violating the rubric's own
  caption-agreement gate.
- **med** `src/marginalia.py` (23 figcaptions, e.g. line 1556) — captions
  contain markdown backticks that `render_for_anchor` only HTML-escapes, so
  literal backtick characters ship on example pages while adjacent prose
  renders backticks as `<code>`.
- **low** `tests/test_marginalia_geometry.py:338-347` — the section-figure
  contract checks journeys ⊆ SECTION_FIGURES but not the reverse; deleting a
  journey section leaves a dead figure (and its paint function counted as
  used) undetected. Currently 21↔21.
- **low** orphan-figure detection counts a figure as used if its quoted name
  appears anywhere in `build_prototypes.py` source (a comment would count);
  size contract checks width only; collision contracts ignore line-vs-text
  overlap.
- **low** `src/marginalia_grammar.py` — dead vocabulary (`open_arrow`,
  `dispatch`, `register(between=)` unused by all 123 figures); the viewBox
  padding triple is a literal duplicated in the test file with a comment
  pointing at module constants that don't exist; `args_kwargs`
  (marginalia.py:834-842) hand-computes a divider 3 px off char-center
  instead of using the purpose-built `mono_divider`.
- **low** `tests/test_marginalia_geometry.py:15` — header says "all 109
  figures"; there are 123 (109 is the attached-slug count).

## 8. Documentation drift and internal contradictions

- **high** `docs/example-source-format-spec.md` — still opens "describes a
  *future* source format" with every Phase 0–4 checkbox unchecked, though
  the migration shipped (CHANGELOG 2026-05-16; `src/examples.py` is the
  13-line shim). It never documents `:::unsupported` cells, frontmatter
  `expected_output` (used by 4 examples), `see_also` (present in all 109
  files), or `scope_first_pass`; mandates "exactly one output fence" per
  cell (unsupported cells have none); its parsed model and `verify` target
  don't match `example_loader.py`/the Makefile.
- **med** `docs/lessons-learned.md:103-106` — states the production figure
  layout backwards: "inline between prose and code is the production layout;
  banners between cells is the prototyped richer grammar" and cites a
  `.lp-cell.has-figure` rule. Production renders banners between cells
  (`src/app.py:755-760`), and `has-figure` appears nowhere in CSS, src, or
  tests; two other docs state the current reality. Also "54 tests today
  cover 9 contract families" (actual: 24 tests, 11 classes).
- **med** `docs/example-quality-rubric.md:45` vs
  `quality-registries.toml:183` — rubric says "every shipped example should
  score at least 8.5"; the enforced bar is 9.0-or-waiver
  (`check_quality_scores.py:94`). `lessons-learned.md:121` attributes the
  9.0 target to the rubric doc, which never states it.
- **med** `docs/example-figure-rubric.md:150-152` and
  `docs/visual-explainer-spec.md:102` — both cite a 440 px banner ceiling;
  Contract 8 and `site.css:161` enforce 640 px. The rubric's formula also
  omits the 1.6 intrinsic scale. Per the doc ~15 shipped figures would fail;
  per code they pass.
- **med** `docs/visual-explainer-spec.md` — multiple internal
  contradictions and stale names: its CSS sample uses `width: 100%` while
  its own invariant 1 says "never `width: 100%`"; journey figures described
  as a ~280-320 px column beside the heading (echoed by
  `journey-visualisation-rubric.md:58-61,93-94`) while production renders
  them inline, centered, up to 640 px; references
  `JOURNEY_SECTION_FIGURES in scripts/build_prototypes.py` (actual:
  `SECTION_FIGURES` in `src/marginalia.py`) and `_render_walkthrough_cell`
  (actual: `_render_cell`).
- **med** `README.md` — Features/Architecture predate the 2026-05-16
  release: no mention of journeys, the marginalia figure system, `see_also`
  links, Turnstile protection, or wide-event observability. A contributor
  cannot discover that journeys are Python data in `src/app.py` synced with
  `journey_outcomes` in the registry.
- **med** `CONTRIBUTING.md` — says "five scripts enforce the catalog-level
  rules" (`make quality-checks` runs nine), and omits the steps a new
  example actually requires: a curated score in `EXAMPLE_QUALITY_SCORES`
  (`check_quality_scores` fails without it), a figure or a no-figure
  rationale, and `see_also` authoring rules. Deployment/secret setup
  (Turnstile vars, `PBE_SMOKE_BYPASS_SECRET`) is documented only inside the
  turnstile spec.
- **low** `docs/rubric-audit-2026-05-12.md` — the "green baseline" itself
  has drifted: claims 24 journey sections including three from the removed
  Workers journey (current: 21).
- **low** `docs/example-graph-see-also.md:45-48` — "future improvements"
  lists work already shipped (graph audit script, rendered edge labels, 404
  recommendations).
- **low** `docs/turnstile-runner-protection-spec.md:92-107` — documents
  modes `off`/`session` only; `main.py:163` also accepts `once` and
  `once-per-session`.
- **low** `docs/observability-spec.md:502-512` — cleanup snippet predates
  the destroy-only-unused-callbacks refinement in `main.py:379-387`.
- **low** `docs/rubric-saturation.md:3-5` — "109 figures in FIGURES" (now
  123), "12 figures are reused" (now 7); the figure rubric cites these as
  live rationale. `example-figure-rubric.md` labels two different contracts
  "Contract 5b".
- **low** `README.md:153-159` — the Deploy section omits
  `make verify-python-version` and `git diff --check`, which the
  Verification section and PR template require.
- **low** `src/app.py:65-70` — `build_dynamic_worker_code`'s docstring
  claims "The parent Worker supplies only curated example code"; user-edited
  POST code runs there too (that's what Turnstile gates).
- **low** `tests/test_quality_checks.py:1` — docstring says "the four
  quality-check scripts" (nine exist).

## 9. Test gaps

- **med** the Turnstile clearance HMAC/cookie logic (`_sign_clearance`,
  `_clearance_valid`, cookie flags, max-age clamp) and the entire POST
  `/examples/{slug}` run flow (verification-required path, missing-site-key
  path, verify-then-set-clearance path) have no behavioral tests. The one
  related test asserts that `main.py` source *contains substrings*.
- **low** several tests are source-text change-detectors
  (`test_worker_entrypoint_uses_fastapi_asgi_bridge`,
  `test_dynamic_worker_execution_uses_hash_keyed_get_cache`,
  `test_turnstile_verification_is_session_gated_in_worker`), and
  `test_every_example_executes_without_error` ends in
  `assertIsInstance(stdout.getvalue(), str)` — always true.
- **low** `html_cache_key_url`'s key scheme is never invoked by a test; no
  test asserts a figure/banner actually appears in rendered example or
  journey HTML (if the anchor scheme drifted, every figure would vanish with
  the suite green); bridge `process_request` body/streaming/error paths are
  unexercised; negative tests exist only for `check_registry_integrity`
  among the quality gates; `run()`'s `env_overrides` parameter in
  `test_quality_checks.py` is accepted but unused; temp files are never
  removed.

## 10. Improvement suggestions (beyond fixes)

Tooling and architecture:

1. **Pin the whole toolchain to 3.13 in one place.** Route every Makefile
   target through `uv run --python 3.13` (or a `PY := uv run --python 3.13
   python` variable) so `make verify` works on any machine, matching the
   README's promise. Add `--group workers` to `make dev`.
2. **Move editorial data out of Python literals into the existing TOML
   registry pattern.** `JOURNEYS` (285 lines), `SEE_ALSO_EDGE_LABELS`,
   `EXAMPLE_QUALITY_SCORES`, `SCORES`, `SECTION_FIGURE_SCORES`, and
   `ATTACHMENTS` are content, not code; `quality-registries.toml` +
   `tomllib` is already the established home. This alone halves
   `marginalia.py` (~55% data literals) and makes journeys reviewable like
   examples.
3. **Make the quality layer falsifiable.** Give `score_example_criteria` a
   failure condition (e.g. max curated-vs-heuristic delta) or remove it from
   `verify`; compare waiver `expires`/`review_after` against today's date;
   enforce or delete `journey_average_min` and the `paired_pages` rule;
   validate score ranges; replace degenerate confusable tokens with
   word-boundary regexes. Add one negative test per gate proving it can
   fail.
4. **Consolidate script plumbing.** A small `scripts/_common.py` for the
   repeated `ROOT`/`sys.path`/loader/registry boilerplate (~12 scripts) and
   one frontmatter parser instead of three (`example_loader`,
   `format_examples`, `check_broad_surface_tours`) that can drift.
5. **Close the generated-file loop.** Hooks run `make build` (not just
   fingerprints); `.gitattributes` covers `example_sources_data.py`;
   `check-generated` covers `public/` fingerprinted copies and the
   prototyping pages (or prototypes move out of `public/`); the regenerate
   workflow rebuilds after `git pull --rebase`.
6. **Cache the started ASGI app** in the bridge instead of running the
   lifespan per request, and consider memoizing rendered pages — the site
   is fully static per deploy, so even pre-rendering all pages at build time
   (and reserving the Worker for POST runs) is a plausible simplification.
   Measure cold-start impact of the 105 import-time program executions under
   Pyodide; if the dedicated snapshot doesn't absorb it, ship precomputed
   `expected_output` in the embedded data.
7. **Collapse the double routing layer.** FastAPI handlers parse
   `{slug}` then delegate to the hand-rolled `route()` which re-parses the
   URL; route everything through one of the two.
8. **Schedule the planned golden-fixture cleanup.** The spec conditions
   (one stable release cycle, CI coverage) are met; the 11k-line fixture now
   requires regeneration on every content edit, making the parity gate
   near-tautological.
9. **CI hygiene:** `concurrency` + `permissions` on verify.yml; restrict
   `push` trigger to main; pin wrangler consistently; pass workflow inputs
   via `env:`; set `PBE_SMOKE_BYPASS_SECRET` in the smoke steps before
   enabling Turnstile in production.
10. **Add security headers** (CSP without `unsafe-inline` will require
    nonce-ing the two inline scripts or externalizing them;
    `X-Content-Type-Options`, `frame-ancestors`, `Referrer-Policy`) and a
    POST body-size cap.

Content (systemic, from the 109-file review):

11. **Add a program⊇cells build check** — the program block should contain
    every executable cell's code (catches the operators/numbers/decorators
    drift mechanically); pages whose cells are deliberate standalone
    fragments need an explicit marker.
12. **Lint prose duplication** — adjacent duplicate paragraphs and cell
    prose identical to the intro (hello-world, truthiness, unpacking, sets).
13. **"Show the failure" rule** — any page whose headline feature is a
    restriction (`/`, bare `*`) or whose note warns about a hazard (broad
    except, `__eq__` without `NotImplemented`, mutable `__hash__`) should
    demonstrate the rejected call or visible breakage, via `:::unsupported`
    or try/except; sweep flag demos for no-op inputs (`clamp=True`).
14. **Unify the PEP 695 story** across the Types section: one consistent
    "modern vs legacy spelling" framing for type-hints, type-aliases,
    generics-and-typevar, and paramspec; retire or caveat deprecated
    `TypeAlias`.
15. **Support or forbid inline cross-references**: either extend
    `render_inline()` to render markdown links and lint hrefs against real
    routes, or enforce that cross-references go through `see_also` only.
16. **Rewrite the runner-constraint framing** on
    subprocesses/threads/networking: one honest sentence ("verified under
    standard CPython at build time; the in-browser runner cannot spawn
    processes/threads/sockets") instead of the current self-contradiction,
    and drop the duplicated unsupported/executable cell pairs.
17. **Caption pipeline**: run figcaptions through the same inline renderer
    as prose (fixing the 23 backtick captions), and fix or redraw the
    while-loops figure/caption mismatch.

Docs:

18. **Refresh the three drifted clusters in one pass**: mark the format spec
    as implemented and document the four missing constructs; correct
    lessons-learned's backwards layout claim and stale numbers; align the
    rubric/figure-spec numbers (8.5 vs 9.0, 440 vs 640) with the enforced
    values. Cheap insurance: a `make rubric-audit` variant that greps docs
    for the enforced constants.
19. **Write the missing contributor path**: a short "adding an example
    end-to-end" doc covering markdown file → score entry → figure or
    rationale → registries → `make verify`, plus a deployment/secrets
    page; update README Features/Architecture for journeys, figures,
    Turnstile, and observability.
