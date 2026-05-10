# Journey visualisation rubric

This rubric scores the figure beside each journey section heading.
The example rubric (docs/example-quality-rubric.md) covers individual
lesson pages; this one covers the conceptual figures that introduce
each journey section.

A journey section sits *above* individual lessons. It groups three to
five examples under a shared conceptual shift, e.g. "Recognise iteration
as a protocol" or "Bundle behavior with state". The figure beside that
heading should depict the shift the section asks the reader to make.
It is not a recycled lesson figure.

Score each section figure on a 10-point scale.

## Content (5.5)

1. **Section fidelity (0-1.5)** — the figure depicts the conceptual
   shift the section title and summary describe. It does not depict
   one of the section's examples. A figure for "Make decisions
   explicitly" must show *deciding*, not the body of any particular
   `match` statement; a figure for "Bundle behavior with state" must
   show *bundling*, not one specific class.
2. **Pedagogical scope (0-1.0)** — the figure captures the general
   pattern that unifies the section's items. If the figure could be
   replaced with the diagram from any single lesson it is too specific.
3. **One conceptual move (0-1.0)** — exactly one shift, before-state
   to after-state, or the depiction of a single mechanism. Two ideas
   compete for the reader's eye and both lose. Squint test: the
   primary structure is identifiable within two seconds.
4. **Mechanism over metaphor (0-1.0)** — the figure shows the actual
   machinery the section names — the iterator object, the cell, the
   dispatch arrow — not a cartoon of it. Knuth's rule.
5. **Caption alignment (0-1.0)** — the `figcaption` names the
   conceptual shift in plain language and matches the section
   summary's voice. The caption is part of the figure, not optional.

## Craft (3.0)

6. **Grammar conformance (0-1.0)** — composed exclusively from
   `Canvas` primitives in `src/marginalia_grammar.py`. No bespoke
   SVG, no new colours, no stroke weights outside the locked set.
7. **Emphasis scarcity (0-1.0)** — at most one accent mark per
   figure. The accent goes on the single element the section names
   (the live yield, the dispatch arrow, the captured cell). If three
   things are orange the figure has no emphasis at all.
8. **Restraint (0-1.0)** — no decoration that does not carry
   information. No drop shadows, gradients, ornamental rules,
   non-orthogonal tilts, or marks placed for "balance".

## Context (1.5)

9. **Independence from lesson figures (0-1.0)** — distinct framing
   from any single lesson's diagram. If the section figure is
   identical to a `cell-figure` in one of the section's lessons,
   one of them is wrong. Usually the section figure should be the
   *more abstract* one.
10. **Layout fit (0-0.5)** — renders comfortably at the journey
    page's ~280-320px section-figure column. Text inside the SVG
    stays readable at that scale; the figure does not overflow.

## Topic gates

- **Decision sections** — depict the fork explicitly: a value flowing
  through a predicate to one of several branches. A single linear
  arrow does not satisfy this gate.
- **Loop sections** — show the back-edge that makes a loop a loop.
  A linear sequence of cells without a return path is not a loop
  picture, it is just a sequence.
- **Iteration sections** — show the `iter()` / `next()` protocol
  explicitly: an iterable, an iterator, and one or more values
  pulled out by `next()`. The figure must distinguish iterable
  from iterator.
- **Type sections** — show annotations as ghost overlays on runtime
  values, or show type relationships (union, generic, structural
  matching) as containment / flow. Do not let a type figure devolve
  into "a function with parameter names".
- **Resource and boundary sections** — show enter and exit as paired
  events bracketing a body, with the failure path also routed
  through exit. A one-way arrow is not a context manager.
- **Concurrency sections** — show two parallel lanes with handoffs
  between them. A single timeline is not a concurrency picture.

## Release gates outside the score

- **Exactly one figure per section.** Section figures are not stacked.
  If the section needs two figures the section is doing two things.
- **Caption present.** A figure without a `figcaption` is not allowed.
- **Section summary aligns with caption.** The summary in
  `src/app.py`'s `JOURNEYS` list agrees with what the figure caption
  asserts. Disagreement means one or the other is wrong.
- **Renders within `.journey-section`'s 2-column grid.** The figure
  obeys the column the layout gives it (~280-320px); design at a
  viewBox sized for that column, not at lesson-figure dimensions.
- **Uses only the four palette constants.** `INK`, `INK_SOFT`,
  `EMPHASIS`, `SOFT_FILL`. Anything else is grounds for redesign.

## Quality bands

- **9.0-10.0** — captures the conceptual shift in two seconds; the
  caption could only describe this figure; pleasant to look at on
  return visits.
- **8.0-8.9** — depicts the right idea but shares too much framing
  with a lesson figure, or the caption hedges instead of asserting,
  or one secondary mark steals attention from the primary one.
- **7.0-7.9** — depicts the section but loses something in scope:
  uses a specific predicate / iterable / type instead of the
  general pattern; or topic gate not satisfied.
- **below 7.0** — recycled lesson figure, missing topic gate,
  multiple primary ideas competing, or accent marks scattered
  rather than scarce. Redesign before publishing.

## Project gate

Every section figure on a published journey page should score at
least **8.5**. The journey average across its three sections should
exceed **8.8** so the journey reads as a unified set rather than
three independently designed cards.

The score is a guide, not a substitute for reading the page beside
its surrounding lessons.
