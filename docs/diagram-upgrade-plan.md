# Diagram upgrade plan

Written 2026-09-27 from a review of every attached figure on the live
site, the gestalt review pages, the grammar, both rubrics and the
registry. This is the synthesis: what the figures are for, the
principles that follow, what shipped with this plan, and the ordered
queue of what comes next. The rubrics stay the scoring instruments;
this document says where the library is going.

## Where the library stood

The strengths were structural and rare: a locked grammar enforced by
contracts, captions that assert rather than narrate, a review page that
paints from production code, and a banner layout that never reflows
the cells. The best figures showed a mechanism changing state: aliasing
before and after, the iterator caret advancing, the MRO diamond
flattening to a chain.

The weaknesses were also structural.

| finding | measure |
|---|---:|
| paint functions using only cell, arrow, dashed line and text | 66 of 124 |
| `cell` calls / `closed_arrow` calls / `lanes` calls | 236 / 129 / 1 |
| attachments anchored after cell 0 | 106 of 115 |
| example figures scoring exactly 9.0 (rest 9.5, none lower) | 106 of 109 |
| journey figures scoring exactly 9.0 | 21 of 21 |
| arrows shorter than 20 units (mostly arrowhead) | 9 |

Beyond the numbers: figures shipped a hard-coded light palette and sat
on cream chips inside the dark page, a pair of small multiples had no
shared baseline, the SVG asked for fonts the page never loads, the
accent sometimes marked an arbitrary row of a selector, and the
bytes-and-bytearray figure rendered doubled backslashes for months
because no contract read figure text.

## Principles

1. **Show state over time.** A figure that shows one frame is a label;
   a figure that shows the same frame after each step is a mechanism.
   Small multiples of one drawing are cheap in this grammar
   (`iterator-unroll`, now `generator-resume`).
2. **Draw the heap.** Python's true picture is frames on the left,
   objects on the right, arrows crossing. The grammar now has an `env`
   phrase for the frame; closures use it first.
3. **A table is not a figure.** If the drawing would be no worse as a
   two-column table in the prose, it is prose. Demote it and record the
   mechanism that would earn the slot back.
4. **The figure carries the lesson's own names.** Reuse the mechanism,
   parametrise the paint function, never choose between placeholders
   and a bespoke copy.
5. **Accent only what the caption names.** If the caption names no
   single element, the figure has no accent. One orange row because it
   is the third row is decoration.
6. **Figure content is checked against the example.** Geometry
   contracts cannot see a wrong label. Content contracts can.
7. **Figures live in both colour schemes.** The grammar paints with
   tokens; the page decides the ink. No chip, no second palette.
8. **Typography follows the page.** Mono and sans use the page's own
   stacks; the mono advance is pinned with `textLength` so divider math
   holds on every platform. The italic serif stays for identifiers.
9. **Rank, then score.** A saturated score is a ship gate, not a
   priority list. Choose what to redesign next by ranking the gestalt.

## What shipped with this plan

Grammar (`src/marginalia_grammar.py`):

- `INK`, `INK_SOFT`, `EMPHASIS`, `SOFT_FILL` are `var(--fig-*)`
  references; `FIGURE_TOKENS_LIGHT` and `FIGURE_TOKENS_DARK` hold the
  values and `figure_token_css()` emits them for shells that embed
  figures outside the site stylesheet (gestalt pages, social cards).
- `FONT_MONO` and `FONT_SANS` match `public/site.css`; every mono run
  is pinned to `MONO_ADVANCE` with `textLength`.
- `ARROW_MIN = 20`; `Canvas` records every arrow's length.
- `name_box` and `bind` take a width so long running names fit.
- New `env` phrase: a frame with bindings, optionally ghosted, returning
  anchors for heap arrows.

Figures (`src/marginalia.py`):

- `closure-cell` is an environment diagram: the returned frame ghosted,
  `double` naming a heap function object, one accented `__closure__`
  reference back into the frame.
- `generator-resume` replaces `generator-ribbon`: three ribbons for
  three `next()` calls on the cell's own `countdown(3)`, with the
  surviving local beside each.
- `format-spec` is a real railroad with bypass rails; the cell's own
  `05.1f` stations are shaded.
- `bytes-vs-bytearray` draws the example's real bytes as integer slots
  and the in-place write `packet[0] = ord("P")`.
- `variables-bind` and `constants-bind` come from one parametrised
  factory and carry `message → "hi"` and `MAX_RETRIES → 3`.
- Six arrows lengthened to the minimum; five figures lost an arbitrary
  accent (`naming-decisions`, `iteration-loop-selector`,
  `type-shape-catalog`, `reliability-signal-map`, `container-methods`).
- Four table-shaped figures demoted with rationales: `values`,
  `literals`, `logging`, `collections-module`.

Page (`public/site.css`, `src/templates/about.html`):

- `--fig-ink`, `--fig-ink-soft`, `--fig-accent`, `--fig-soft` defined
  for light and dark; the dark-mode paper chip removed.
- `.cell-banner figure` is a two-row subgrid so paired small multiples
  bottom-align their drawings and start both captions on one line.

Contracts (`tests/test_marginalia_geometry.py`):

- 13 content: no doubled backslash anywhere; escape sequences in an
  attached figure must appear in that example's source.
- 14 arrow length: every arrow at least `ARROW_MIN`.
- 15 theme tokens: `site.css` defines all four tokens in both schemes
  with the grammar's values, and every grammar colour is a token.

Rubrics: table gate, zero-accent rule, placement honesty and the new
contracts recorded in `docs/example-figure-rubric.md` and
`docs/journey-visualisation-rubric.md`; palette and typography
invariants updated in `docs/visual-explainer-spec.md`.

## Queue

Ordered by payoff. Each item is one pull request.

1. **State-over-time pass.** Apply the `generator-resume` pattern to
   `context-managers` (enter, body, exit, with the exception path as a
   second strip), `decorators` (call twice, two wrappers) and
   `object-lifecycle`.
2. **Heap pass.** Use `env` for `scope-global-nonlocal`, `recursion`
   (frames with `n` bindings, not labelled cells), `unpacking` and
   default-argument sharing if a cell for it exists.
3. **Redesign the demoted four.** `values` as value → type →
   method lookup; `logging` as a record flowing through a threshold;
   `literals` as three spellings converging on one `int`;
   `collections-module` only if the page is split.
4. **Parametrise the remaining reused figures.** `iterator-unroll`,
   `iter-protocol`, `class-triangle`, `operator-dispatch`,
   `comprehension-equivalence` should take the cell's names.
5. **Move anchors to the cell where the move happens.** For each
   cell-0 attachment, ask whether a later cell holds the mutation,
   dispatch or resume the figure depicts. Rewrite the rubric's
   criterion 10 once the distribution is honest.
6. **Rank the gestalt.** Add a pairwise ranking pass (a simple
   `figure_rank` table in the registry) and redesign from the bottom
   ten. Keep the 8.5 score as the gate only.
7. **Strengthen the content contract.** Extend Contract 13 from escape
   sequences to every mono literal that looks like Python source:
   it must appear in the example's code or output.
8. **Hashing and buffers.** Redraw `dict-buckets` and `set-buckets`
   with real hash values from the example, and `list-append` /
   `slice-ruler` as header-plus-buffer.

## What to study, and what to take

- **Composing Programs** (composingprograms.com) and **Python Tutor**
  (pythontutor.com): the canonical environment diagram. Take the
  frame/heap split and the way a closure and a recursive call are drawn.
- **Ned Batchelder, "Facts and myths about Python names and values"**:
  the simplest name → value drawings, drawn the same way every time.
- **Crafting Interpreters** (craftinginterpreters.com): warm ink on
  cream, one idea per figure, consistent across a whole book. The
  closest match to this palette and a lesson in how much charm
  restraint allows.
- **Sam Rose, samwho.dev** ("Hashing", "Memory Allocation"): programmer
  facing explanatory figures with a locked grammar. The model for the
  bucket figures.
- **Lydia Hallie, "JavaScript Visualized"**: the frame designs for scope
  chain and closures, not the animation.
- **Bartosz Ciechanowski** (ciechanow.ski): every figure changes
  exactly one variable. Read the captions.
- **SQLite syntax diagrams**: what a railroad is; `format-spec` now
  follows it.
- **The Rust Book, chapter 4** and the Go blog **"Go Slices: usage and
  internals"**: header-plus-buffer drawings for list, bytearray, slice.
- **Tufte, Visual Explanations, "the smallest effective difference"**:
  how little contrast emphasis needs; the argument behind the
  zero-accent rule.
- **Maggie Appleton** and **Julia Evans**: one panel, one idea. Tone,
  not palette.
- **Distill.pub**: the figure as the argument, captions carrying the
  claim.
