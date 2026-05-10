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

Score each example figure on a 10-point scale.

## Content (5.5)

1. **Cell fidelity (0-1.5)** — the figure depicts the move the cell's
   prose discusses, not the example's title. If the example is
   "Mutability" but cell 1 is about immutable strings, a figure on
   cell 1 must depict immutability, not aliasing. Wrong cell, wrong
   figure.
2. **Match the running variables (0-1.0)** — names, values, and shapes
   in the figure match the cell's source. If the cell uses `first` and
   `second` on a list, the figure says `first` and `second`. Generic
   placeholders (`a`, `b`, `xs`) are fine *only* when the cell itself
   is generic; specific names earn their place when the cell uses them.
3. **One conceptual move (0-1.0)** — exactly one shift, before-state
   to after-state, or one mechanism. Squint test: a reader should
   identify the figure's single point in two seconds.
4. **Mechanism over metaphor (0-1.0)** — the figure shows the actual
   machinery (the cell, the binding, the dispatch, the iterator),
   not a cartoon of it. Knuth's rule.
5. **Caption asserts; figure depicts (0-1.0)** — `figcaption` is a
   declarative sentence about what the figure shows. The SVG itself
   contains no prose duplicating the caption — only diagrammatic
   labels (`stdout`, `iter()`, panel tags, type signatures). See
   pipeline invariant 2 in the spec.

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

9. **Cell-column fit (0-1.0)** — the figure's intrinsic width sits
   comfortably inside `.cell-figure`'s `max-width: 360px`. Wider
   intrinsic widths are clamped (good — figures shrink, never grow);
   much narrower widths leave whitespace on either side. Aim for an
   intrinsic viewBox between 200 and 360 px wide.
10. **Pairs with the code, not the title (0-0.5)** — when the figure
    sits next to its source block (cell-figure layout), the eye reads
    prose → figure → source as one move. The figure should make the
    *source* easier to read, not stand alone as a generic
    illustration of the example title.

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

- **One figure per cell, at most.** Two figures on one cell signal
  the cell is doing two things; split the cell instead.
- **figcaption present and declarative.** Captions in the form
  "Two names share one mutable list — appending through one name
  changes the object visible through both." Not "this shows X" or
  "see how Y".
- **figcaption agrees with the cell's prose.** The cell's prose
  paragraph in the markdown and the figure's figcaption assert the
  same thing in different words. If they disagree, one is wrong.
- **Palette discipline.** Only `INK`, `INK_SOFT`, `EMPHASIS`,
  `SOFT_FILL`. No literal hex codes, no `rgba(0,0,0,…)` neutrals.
- **Pipeline invariants** (see spec) hold: SVG renders at intrinsic
  size; SVG contains no prose duplicating the caption.

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
