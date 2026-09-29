# Diagram upgrade plan

Written 2026-09-27 from a review of every attached figure on the live
site, the gestalt review pages, the grammar, both rubrics and the
registry. The rubrics remain the scoring instruments. This document
records what the review found, the principles that follow from it,
what the first pull request changed, and the queue after that.

## What the review found

The library's strengths are enforced rather than hoped for: the palette,
stroke weights and typography are locked by contracts, captions assert
what is true instead of narrating the picture, and the gestalt review
page paints from the production paint functions. The figures that teach
best show a mechanism changing state, such as aliasing before and after
an append, the iterator caret advancing one row at a time, and the MRO
diamond flattening into a chain.

The weaknesses are measurable.

| finding | measure |
|---|---:|
| paint functions using only cell, arrow, dashed line and text | 66 of 124 |
| `cell` calls / `closed_arrow` calls / `lanes` calls | 236 / 129 / 1 |
| attachments anchored after cell 0 | 106 of 115 |
| example figures scoring exactly 9.0 (the rest 9.5, none lower) | 106 of 109 |
| journey figures scoring exactly 9.0 | 21 of 21 |
| arrows shorter than 20 units | 9 |

Behind the numbers: figures hard-coded the light palette, so in dark
mode each one sat on a cream chip; a paired banner had no shared
baseline; the SVG asked for JetBrains Mono and Source Sans while the
page loaded no web fonts, so the visitor's operating system chose the
faces; several selector figures put the accent on whichever row the
loop reached last; and because no contract read figure text, the
bytes-and-bytearray figure rendered doubled backslashes for months and
the regular-expressions figure drew a pattern the example never uses.

## Principles

1. **Show state over time.** One frame is a label. The same frame after
   each step is a mechanism. Repeating one drawing is cheap in this
   grammar; `iterator-unroll` and `generator-resume` do it.
2. **Draw the heap.** Python's picture is frames on the left and objects
   on the right with arrows crossing between them. The grammar now has
   an `env` phrase for the frame, and closures uses it.
3. **Redraw a weak figure; never replace it with a note.** A drawing
   that would be no worse as a two-column table needs a mechanism
   drawn in its place. Removing it and recording a rationale leaves the
   page with less than it had, which the first draft of this plan got
   wrong for four pages.
4. **The figure carries the lesson's own names.** Reuse the mechanism
   by parametrising the paint function, so `variables` shows `message`
   and `constants` shows `MAX_RETRIES`.
5. **Accent only what the caption names.** When the caption names no
   single element, the figure has no accent.
6. **Check figure content against the example.** Geometry contracts
   cannot see a wrong label. A content contract can.
7. **Paint with tokens.** The grammar emits `var(--fig-*)`; the page's
   stylesheet decides the ink in each colour scheme.
8. **Typography follows the page.** Mono and sans use the page's own
   stacks, and mono runs carry `textLength` so divider maths holds on
   every platform. The italic serif stays for identifiers.
9. **Rank before scoring.** With 106 of 109 figures at 9.0, the score
   is a ship gate. Choosing what to redesign next needs a ranking.

## What the first pull request changed

Grammar (`src/marginalia_grammar.py`):

- `INK`, `INK_SOFT`, `EMPHASIS` and `SOFT_FILL` are `var(--fig-*)`
  references. `FIGURE_TOKENS_LIGHT` and `FIGURE_TOKENS_DARK` hold the
  values; `figure_token_css()` emits them for the gestalt pages and the
  social-card shell.
- `FONT_MONO` and `FONT_SANS` match `public/site.css`; every mono run is
  pinned to `MONO_ADVANCE` with `textLength`.
- `ARROW_MIN = 20`; `Canvas` records every arrow's length.
- `name_box` and `bind` take a width so long names fit.
- The `env` phrase draws a frame with bindings, optionally ghosted, and
  returns anchors for heap arrows.

Figures (`src/marginalia.py`):

- `closure-cell` is an environment diagram: the returned frame ghosted,
  `double` naming a heap function object, one accented `__closure__`
  reference back into the frame.
- `generator-resume` replaces `generator-ribbon`: three ribbons for
  three `next()` calls on the cell's own `countdown(3)`, the surviving
  local beside each.
- `format-spec` is a railroad tracing the cell's own `05.1f`: visited
  stations shaded, skipped stations ghosted under a bypass rail.
- `bytes-vs-bytearray` draws the example's bytes as integer slots and
  the in-place write `packet[0] = ord("P")`, anchored to the cell that
  performs it.
- `regex-groups` replaces `regex-anchors`: the cell's two capture
  groups dropped onto the record `Ada: 10`.
- `value-type-lookup` replaces `value-types`: `text` bound to a `str`
  object, then the `type()` hop to the class where `upper()` lives.
- `logging-threshold` replaces `logging-levels`: the cell's three
  records crossing the handler's INFO gate, `debug` dropped.
- `variables-bind` and `constants-bind` come from one parametrised
  factory.
- Nine arrows lengthened to the minimum; five figures lost an accent
  that marked an arbitrary row.
- `literal-forms` and `collections-containers` stay as they were, scored
  8.5, until a mechanism replaces them.

Page (`public/site.css`, `src/templates/about.html`):

- `--fig-ink`, `--fig-ink-soft`, `--fig-accent` and `--fig-soft` defined
  for light and dark; the dark-mode paper chip removed.
- `.cell-banner figure` is a two-row subgrid, so paired figures
  bottom-align their drawings and start both captions on one line.

Contracts (`tests/test_marginalia_geometry.py`):

- 13, content: no doubled backslash anywhere; an escape sequence in an
  attached figure must appear in that example's source.
- 14, arrow length: every arrow at least `ARROW_MIN`.
- 15, theme tokens: `site.css` defines all four tokens in both schemes
  with the grammar's values, and every grammar colour is a token.

Rubrics: the redraw rule, the zero-accent rule, the placement note and
the three contracts are in `docs/example-figure-rubric.md` and
`docs/journey-visualisation-rubric.md`; the token and typography
invariants are in `docs/visual-explainer-spec.md`.

## Queue

Ordered by payoff. Each item is one pull request.

1. **State over time** for `context-managers` (enter, body, exit, with
   the exception path as a second strip), `decorators` (two calls, two
   wrappers) and `object-lifecycle`.
2. **Heap drawings** with `env` for `scope-global-nonlocal`, `recursion`
   (frames with `n` bindings instead of labelled cells) and `unpacking`.
3. **Mechanisms for the two table figures.** `literals`: the same value
   spelled three ways converging on one `int` object. `collections-module`:
   one container's operation, or split the page.
4. **Parametrise the remaining reused figures**: `iterator-unroll`,
   `iter-protocol`, `class-triangle`, `operator-dispatch`,
   `comprehension-equivalence`.
5. **Move anchors to the cell where the move happens.** For each cell-0
   attachment, ask whether a later cell holds the mutation, dispatch or
   resume the figure depicts. Rewrite criterion 10 once the distribution
   is honest.
6. **Rank the gestalt.** A pairwise ranking table in the registry, and
   redesign from the bottom ten. The 8.5 score stays as the gate.
7. **Widen the content contract** from escape sequences to every mono
   literal that looks like Python source: it must appear in the
   example's code or output.
8. **Buffers and hashes.** `dict-buckets` and `set-buckets` with hash
   values from the example; `list-append` and `slice-ruler` as header
   plus buffer.

## What to study

- **Composing Programs** (composingprograms.com) and **Python Tutor**
  (pythontutor.com) for the environment diagram: frames left, objects
  right, and how a closure and a recursive call are drawn.
- **Ned Batchelder, "Facts and myths about Python names and values"**
  for name-to-value drawings done the same way every time.
- **Crafting Interpreters** (craftinginterpreters.com) for warm ink on
  cream, one idea per figure, held consistent across a whole book.
- **Sam Rose, samwho.dev** ("Hashing", "Memory Allocation") for
  programmer-facing figures with a locked grammar; the model for the
  bucket figures.
- **Lydia Hallie, "JavaScript Visualized"** for the frame designs of
  scope chain and closures.
- **Bartosz Ciechanowski** (ciechanow.ski) for figures where exactly
  one variable changes between frames.
- **SQLite syntax diagrams** for what a railroad is; `format-spec`
  follows them.
- **The Rust Book, chapter 4** and **"Go Slices: usage and internals"**
  for header-plus-buffer drawings of list, bytearray and slice.
- **Tufte, Visual Explanations, "the smallest effective difference"**
  for how little contrast emphasis needs.
- **Maggie Appleton** and **Julia Evans** for mechanism drawings that stay playful without adding marks.
- **Distill.pub** for captions that carry the claim.
