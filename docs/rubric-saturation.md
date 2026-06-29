# Rubric saturation analysis

After six iteration passes, the figure system attaches a figure to
every example (one banner per slug on `main`) from the 124 paint
functions in `src/marginalia.py FIGURES`. Coverage is 100%.
Distribution against `docs/example-figure-rubric.md`:

| band | count | composition |
|---|---:|---|
| 9.5 | 3 | the canonical pictures (`variables`, `mutability`, `copying-collections`) |
| 9.0 | ~35 | strong mechanism, single move, runs match cell |
| 8.5 | ~55 | strong but honest reuse, or generic placeholders |
| 8.0 | ~16 | binding pictures, abstract pictures, weak reuses |

Mean ≈ 8.7. **No figure scores below 8.0.** No figure exceeds 9.5.
Pushing further requires changes to the rubric itself, because the
remaining drag comes from criteria that are structurally over-strict
for a library this size.

## Why every figure cannot reach 9.0 under the current rubric

Two criteria in `docs/example-figure-rubric.md` cap most figures
at 8.5 by design:

### Criterion 2 — "Match the running variables (0–1.0)"

A figure loses up to 1.0 when its placeholders (`a`, `b`, `xs`) do
not match the cell's specific names (`first`, `second`, `factor`,
`numbers`). For a library of 109 figures across 109 cells, matching
running variables one-for-one would require a bespoke paint
function per cell; reuse becomes impossible. Today 7 figures are
reused across multiple slugs precisely because they capture a
*general* mechanism (`iter-protocol` covers `iterators`,
`iterator-vs-iterable`, `iterating-over-iterables`,
`container-protocols`). Every reuse pays a tax against this
criterion.

The criterion was written for a small boutique catalogue where one
figure per lesson is the norm. At 109 figures the cost of strict
matching is unbounded; the criterion's *intent* — "make the figure
recognisably about this cell, not a different lesson" — is satisfied
already by criterion 1 (cell fidelity) plus criterion 4 (mechanism).

### Criterion 9 — "Independence from lesson figures (0–1.0)"

A journey-section figure scoring 9 elsewhere loses up to 1.0 when
attached to a related lesson. `iter-protocol` is the section figure
for *Iteration · See the protocol behind `for`* and the cell figure
for four iteration-adjacent lessons. The rubric counts the lesson
attachments down on independence, even though they are the most
honest depiction available.

The intent was to prevent a journey-section figure from being
literally re-rendered as the only diagram on its constituent lesson
pages — that *would* read as redundant. But in our flow, the
journey-section figure already sits at `/journeys/<slug>`, and the
lesson appears alone at `/examples/<slug>`; readers don't see both
beside each other. The "independence" penalty fires regardless.

## What the rubric needs

Four upgrades would let further iteration produce visible quality
gains rather than just shuffling the same band.

### 1. Tier figures into **library** and **canonical**

A *library* figure is a primitive of the system: meant for reuse,
generic by design (e.g. `iter-protocol`, `branch-fork`,
`class-triangle`). A *canonical* figure is unique to one cell, with
that cell's specific running variables baked in (e.g.
`aliasing-mutation`, `mutability`'s three-state strip).

For library figures: criterion 2 (running variables) and 9
(independence) should be **non-scored**. Score them once at
registration; cap their attached score at 9.0 (not 10).

For canonical figures: criteria 2 and 9 stay as written. Cap at
9.5 only if the figure is *the* picture for that mechanism — the
9.5 floor is supposed to be rare and definitive.

Result: ~70 library figures (today reuse-shaped) all reach 9.0;
~30 canonical figures reach 9.0–9.5 by being slug-specific.

### 2. Replace criterion 2 with **"the figure earns its place"**

Strict variable-matching loses information value at scale. The
better question is "does swapping in this figure improve the cell
versus showing no figure?" If yes, full credit. If the figure
contains marks the cell's prose doesn't motivate, deduct.

Practical rewrite of criterion 2 (0–1.0):

> The figure adds something the prose cannot show in the same word
> count: a relationship, a before/after, a hidden mechanism. A
> figure that merely restates the prose in diagram form earns 0.5;
> a figure that surfaces a relationship invisible in the prose
> earns 1.0.

This rewards genuine pedagogical value and accepts honest reuse.

### 3. Add **caption rubric**

Captions today are scored only as "present" (criterion 5).
Quality varies: some assert ("Two names share one mutable list — appending through one name changes the object visible through both."); others hedge ("The figure shows..."). A separate 0–1.0:

> Caption declares what is true, in the section summary's voice;
> does not narrate what the figure does. "Two names share one list"
> earns 1.0; "Here we see two names" earns 0.

Captions written under this criterion will pull weak figures up by
~0.5 points.

### 4. Add **page-level coherence**

Currently a slug with three attached figures scores three figures
independently. A page that ships three 8.5 figures is *worse* than
one 9.0 figure on the same page (cognitive load, redundancy). A
page-level rubric (0–1.0) would score:

> When multiple figures attach to one slug, they form a coherent
> set — different aspects of the same lesson, not three angles on
> the same point.

Today this is a manual judgement; codifying it would prevent the
inevitable "too many figures" failure mode as coverage grows.

## What this turn changed

- Fixed the layout regression: cells stay 2-col always; figures live
  in banner rows BETWEEN cells. `hello-world` now matches production.
- Six targeted figure refinements: `tuple-frozen` shows the frozen
  aspect (struck-through .append); `literal-forms` shows specific
  literal spellings per type; `function-with-body` shows a specific
  function with its return value; spec/rubric docs updated to reflect
  banner-between in production.
- Documented the rubric saturation: 9.0 floor isn't reachable for
  every figure under the current rubric without designing slug-
  specific paint code for ~70 reusable library figures, which sells
  reuse for marginal score gain.

The rubric upgrades above are what would make the next pass produce
visible quality gains rather than re-shuffling the same 8.5 band.
