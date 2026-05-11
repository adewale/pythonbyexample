# Example figure rubric

Parallel to `docs/journey-visualisation-rubric.md`, but for the figures
that attach to **example pages** (literate-program lessons), not journey
sections. The journey rubric scores the figure beside a section heading;
this one scores the figure that sits between prose and code inside a
single cell of an example walkthrough.

The two rubrics share craft criteria (palette, primitives, emphasis
scarcity) and diverge on content criteria, because the audience and
task differ. A journey-section figure depicts the *conceptual shift*
unifying multiple lessons; an example figure depicts the *single move*
the surrounding cell discusses.

Score each example figure on a 10-point scale. Version 2 of this
rubric, applied 2026-05; see `docs/rubric-saturation.md` for the
reasoning that produced these upgrades. The previous criterion 2
("match the running variables") and criterion 5 ("caption asserts")
have been replaced; a new page-level coherence rubric joins the
per-figure scoring.

## Content (5.5)

1. **Cell fidelity (0-1.5)** — the figure depicts the move the cell's
   prose discusses, not the example's title. If the example is
   "Mutability" but cell 1 is about immutable strings, a figure on
   cell 1 must depict immutability, not aliasing. Wrong cell, wrong
   figure.
2. **The figure earns its place (0-1.0)** — the figure surfaces
   something the prose cannot show in the same word count: a
   relationship, a before/after, a hidden mechanism, an invariant.
   A figure that merely restates the prose in diagram form earns
   0.5; a figure that adds nothing the prose hasn't already said
   earns 0. Generic placeholders (`a`, `b`, `xs`) are fine; what
   matters is whether the figure carries pedagogical weight beyond
   the prose. (Replaces v1's "match the running variables", which
   punished honest reuse of library figures across multiple cells.)
3. **One conceptual move (0-1.0)** — exactly one shift, before-state
   to after-state, or one mechanism. Squint test: a reader should
   identify the figure's single point in two seconds.
4. **Mechanism over metaphor (0-1.0)** — the figure shows the actual
   machinery (the cell, the binding, the dispatch, the iterator),
   not a cartoon of it. Knuth's rule.
5. **Caption quality (0-1.0)** — `figcaption` declares what is true,
   in the section summary's voice; it does not narrate what the
   figure does. "Two names share one mutable list — appending
   through one name changes the object visible through both."
   earns 1.0. "The figure shows two names pointing at one list."
   earns 0 (narration, not assertion). Mixed-voice captions earn
   0.5. The SVG itself contains no prose duplicating the caption;
   only diagrammatic labels (`stdout`, `iter()`, panel tags, type
   signatures). See pipeline invariant 2 in the spec.

## Craft (3.0)

6. **Grammar conformance (0-1.0)** — composed exclusively from
   `Canvas` primitives in `src/marginalia_grammar.py`. No bespoke
   SVG, no new colours, no stroke weights outside the locked set.
7. **Emphasis scarcity (0-1.0)** — at most one accent mark per
   figure. The accent goes on the single element the cell prose
   names (the live mutation, the captured cell, the dispatch arrow).
   Three accent marks competing for attention is no emphasis at all.
8. **Restraint (0-1.0)** — no decoration that does not carry
   information. No drop shadows, gradients, ornamental rules,
   non-orthogonal tilts, or marks placed for "balance".

## Context (1.5)

9. **Banner-row fit (0-1.0)** — the figure's intrinsic width sits
   comfortably inside `.cell-banner`'s auto-fit grid. Intrinsic widths
   beyond ~360 px clamp to the column without growing past it; much
   narrower viewBoxes leave whitespace either side of the centred
   figure. Aim for an intrinsic viewBox between 200 and 360 px wide.
10. **Pairs with the surrounding cell (0-0.5)** — the banner sits
    AFTER the named cell, so the eye reads cell-prose → cell-code →
    banner. The figure should summarise the move the surrounding
    cell just made, not stand alone as a generic illustration of the
    example title.

## Topic gates (cell-shape specific)

- **Binding cells** (assignments, `=`) — show the name-arrow with the
  type tag and the resulting value. The canonical Python picture.
- **Mutation cells** — show before-state and after-state with the
  same object identity, OR rebinding with a new identity. The
  difference is the lesson.
- **Iteration cells** — show the iterator advance: a caret moving,
  or `iter()`+`next()` producing values one at a time.
- **Function-definition cells** — show the signature with parameter
  separators (`/`, `*`) explicit when relevant, or the
  caller→body→return shape.
- **Class cells** — show state and methods bundled, or the
  instance→class→type triangle, or MRO chain. Pick one, not all.
- **Exception cells** — show the lanes (try/except/else/finally)
  with a single traced path, or the exception-cause arrow (`__cause__`
  vs `__context__`).
- **Async cells** — show two parallel lanes (loop · coroutine) with
  await handoffs.

## Release gates outside the score

These are not scored; a figure that violates any of them does not
ship. The geometry, palette, font, stroke, emphasis, registration,
and caption gates are now enforced by automated contracts in
`tests/test_marginalia_geometry.py` (Contracts 1-9). CI fails before
the figure can merge.

- **One figure per cell, at most.** Two figures on one cell signal
  the cell is doing two things; split the cell instead.
- **figcaption present and declarative.** Captions in the form
  "Two names share one mutable list — appending through one name
  changes the object visible through both." Not "this shows X" or
  "see how Y".
- **figcaption agrees with the cell's prose.** The cell's prose
  paragraph in the markdown and the figure's figcaption assert the
  same thing in different words. If they disagree, one is wrong.
- **figcaption is unique across slugs.** A reused figure can serve
  multiple lessons (`iter-protocol` attaches to four), but each
  lesson must frame the figure in its own voice. Verbatim caption
  reuse copies the lesson voice the same way verbatim code reuse
  copies the example. *Contract 5b — FigureCaptionContract.*
- **No clipping.** Every `<rect>`, `<text>`, `<line>`, `<circle>`,
  `<path>` lives inside the padded viewBox. Text width counts: a
  long mono string in a too-narrow box clips even if the geometry
  looks right at first glance. *Contract 1.*
- **No element collision.** Text that overlaps a rect must be
  fully contained by that rect. A type tag sitting on top of the
  box above it (the `/examples/values` STR-LIST-DICT bug) is the
  canonical violation. *Contract 2.*
- **No text-text overlap.** Two text elements may not occupy
  overlapping bounding boxes (the `itertools-chain` "ITER A" /
  "1 · 2" collision in a too-narrow box). *Contract 3.*
- **Palette discipline.** Only `INK`, `INK_SOFT`, `EMPHASIS`,
  `SOFT_FILL`, or `"none"` may appear as fill or stroke. *Contract
  5a — FigureGrammarContract.*
- **Font discipline.** Only `FONT_SERIF`, `FONT_MONO`, `FONT_SANS`
  may appear as `font-family`. *Contract 5b.*
- **Stroke-weight discipline.** Only `W_HAIRLINE`, `W_STROKE`,
  `W_EMPHASIS`, `W_GHOST`. *Contract 5c.*
- **Emphasis scarcity, enforced.** At most ONE accent mark
  (`EMPHASIS`-coloured arrowhead, caret, dot, or rect stroke) per
  figure. Was a soft v1 criterion; now hard. *Contract 9.*
- **Banner-fit, enforced.** Every figure's intrinsic width
  (Canvas.w + 2 · PAD_X) must fit `.cell-banner--1`'s 440px max
  ceiling. *Contract 8.*
- **Twin consistency.** When two figures depict parallel concepts
  (`kw-only-separator` ↔ `positional-only-separator`,
  `class-triangle` ↔ `metaclass-triangle`), their metrics must
  match coordinate-for-coordinate where the concepts coincide. A
  fix to one is a fix to both, in the same commit.
- **Geometric termination.** Lines that connect to dots, circles,
  or rects must terminate AT the element's edge — not 1-2px short
  (looks disconnected) and not inside the glyph (looks broken).
  When in doubt, end the line at the centre and let the dot draw
  on top.
- **Mono character alignment.** When a vertical divider marks a
  position in mono text, its x must match the character's actual
  centre. JetBrains Mono advances ~6px per char at fs=10. A
  visually-similar `82` and `75` are not interchangeable.
- **Pipeline invariants** (see spec) hold: SVG renders at intrinsic
  size; SVG contains no prose duplicating the caption.
- **Gestalt = production.** Review pages under `/prototyping/*`
  must render the same paint code as the production attachments.
  Parallel `e_*` paint functions for "gestalt versions" drift from
  production and hide bugs; we eliminated 76 of them in May 2026.

## Page-level coherence (per slug, multi-figure)

A separate 0-1.0 score applied to slugs whose `ATTACHMENTS[slug]`
list contains more than one figure. Multi-figure pages must form a
coherent set, not three angles on the same point.

- **1.0** — figures show distinct aspects of the lesson in a
  natural reading order (intro picture, mid-walkthrough mechanism,
  summary). Each banner earns its placement.
- **0.5** — figures are individually fine but redundant; one would
  do the work of two. The page reads as cluttered.
- **0** — figures contradict each other, or one figure is on the
  wrong cell, or the page has three figures where one would teach
  better.

For single-figure slugs (today, all 109 of them), page coherence is
trivially 1.0 and does not enter the per-figure score. As multi-
figure attachments grow this criterion will become the discriminator
that prevents the "more figures is better" failure mode.

## Quality bands

- **9.0-10.0** — depicts the cell's move in two seconds; the figcaption
  could only describe this figure; reads pleasantly on return visits.
- **8.0-8.9** — depicts the right move but uses generic placeholders
  where specific names would land harder, or the caption hedges, or
  one secondary mark steals attention from the primary one.
- **7.0-7.9** — depicts the cell but loses something in scope: shows
  the example title rather than the specific cell's move; or topic
  gate not satisfied.
- **below 7.0** — wrong cell, wrong shape, multiple primary ideas
  competing, or accent marks scattered rather than scarce. Redesign
  before promoting.

## Project gate

A cell figure may ship to production once it scores **≥ 8.5**. The
example's figure average should exceed **8.7** so a multi-figure
example reads as a coherent set rather than independently authored
diagrams.

The score is a guide, not a substitute for reading the cell beside
its surrounding prose.
