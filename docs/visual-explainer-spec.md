# Visual explainer spec

This spec describes how figures attach to existing Python By Example pages
without changing what contributors author. The earlier draft of this spec
relied on absolute-positioned figures escaping into the page's implicit
outer margin; that approach was rolled back in favour of inline placement
between prose and code, which works at every viewport.

## Goals

- **One column model per page type, fixed.** Example pages keep cells in
  the prose|code 2-col grid; journey pages keep section heading + figure
  in a 2-col grid. Figures never reflow the surrounding columns.
- **Universal, not viewport-conditional.** A reader at any width sees the
  same figure in the same place. No `@media` breakpoints for figure
  positioning; no overlay layer.
- **Multiple figures supported.** Banners hold one, two, or three
  figures via an auto-fit grid; small multiples are first-class.
- **No contributor burden.** Example markdown stays as it is. Figures are
  curated separately by the project owner.
- **Quiet by default.** A page with no figures attached renders
  bit-for-bit identical to today.
- **Grammar reuse.** Figures are composed from the locked vocabulary in
  `src/marginalia_grammar.py`. No bespoke SVG.

## Layout strategy

Two patterns, one for each page type. Both keep their underlying column
model fixed; figures slot into defined positions without disrupting it.

### Example pages — banners between cells

Each `.lp-cell` stays `grid-template-columns: minmax(17rem, .85fr)
minmax(0, 1fr)` — prose left, code right — **always**. Figures live in
banner rows that sit between cells, not inside them. The banner spans
the full content width and uses an auto-fit grid so it can hold one,
two, or three figures as small multiples.

```
[ cell 0 · prose | code ]
─────── banner row ───────
[ figure ]    optional caption
─────────────────────────
[ cell 1 · prose | code ]
```

This matches the union of three influences:
- *Knuth* — cells preserve the literate-program rhythm of prose and code
  side by side, uninterrupted.
- *Tufte* — the banner slot accepts a small-multiple of related figures
  so contrasts and progressions read as one composition.
- *Algebrica* — each banner figure carries a quiet italic caption beneath,
  in the muted text colour, with generous whitespace above and below.

Banner positions:

| key                | renders                              |
|--------------------|--------------------------------------|
| `before`           | once, before the first cell           |
| `after-cell-N`     | once, after cell N (zero-indexed)     |
| `after-walkthrough`| once, after the last cell             |

Each position holds **one or more** figures via `cell-banner` markup.
Captions are per-figure.

```html
<section class="literate-program">
  <section class="lp-cell">prose | code</section>
  <div class="cell-banner cell-banner--2">
    <figure>
      <svg>…</svg>
      <figcaption>Mutable: change visible through any alias.</figcaption>
    </figure>
    <figure>
      <svg>…</svg>
      <figcaption>Immutable: aliases share a frozen value.</figcaption>
    </figure>
  </div>
  <section class="lp-cell">prose | code</section>
</section>
```

```css
.cell-banner {
  margin: var(--space-5) 0;
  padding: var(--space-4) 0;
  border-block: 1px dashed var(--hairline-soft);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--space-4);
  justify-items: center;
}
.cell-banner figure   { margin: 0; padding: 0; max-width: 360px; }
.cell-banner svg      { width: 100%; height: auto; display: block; }
.cell-banner figcaption {
  margin-top: var(--space-2);
  color: var(--muted);
  font-size: .92rem;
  font-style: italic;
  max-width: 44ch;
}
.cell-banner--1 figure { max-width: clamp(280px, 65vw, 640px); }
```

The cell never reflows: cells without banners around them and cells
between banners look identical to today's layout.

### Journey pages — figure between section heading and list

Journey pages are not literate code; they are linear lists of items
grouped under section headings. The figure renders as a centered block
**between** the section heading and the example list — the same
single-column flow on every viewport:

```css
.journey-section-figure {
  margin: var(--space-4) auto;
  width: 100%;
  max-width: clamp(280px, 70vw, 640px);
}
```

One figure per section, faithful to the section's conceptual shift,
scored against `docs/journey-visualisation-rubric.md`. Figures are
mapped by section title via `SECTION_FIGURES` in `src/marginalia.py`;
`render_for_section` returns empty for unmapped titles, but the
SectionFigureContract requires every production journey section to
have one.

### Why these two, not five

The earlier prototypes that mixed inline-above, inline-between,
after-output, and prose-aside all switched the cell's column model
when a figure was present. That created the perils of randomly
oscillating between 1, 2, and 3 columns within the same page. The
banner-between grammar fixes the column model and lets figure count
vary instead. Adding a second or third figure changes the banner's
internal grid (auto-fit handles 1/2/3+), but the cells around it
remain unchanged — no reflow, no cognitive context-switch.

## Anchors and attachments

`src/marginalia.py` declares which figures attach where. `ATTACHMENTS`
remains the single registry; its anchor vocabulary is the position
grammar. Multiple tuples on the same position share one banner as a
small multiple:

```python
# implemented shape — the mutability pair renders as one two-figure banner
ATTACHMENTS = {
    "mutability": [
        ("cell-0", "aliasing-mutation",
         "Two names share one mutable list — appending through one "
         "name changes the object visible through both."),
        ("cell-0", "tuple-no-mutation",
         "By contrast, a tuple is frozen — its contents cannot change "
         "in place, so aliasing carries no mutation hazard."),
    ],
}
```

Banner positions (anchor spellings in parentheses):

| position                            | renders                           |
|-------------------------------------|-----------------------------------|
| `before`                            | once, before the first cell       |
| `after-cell-N` (or legacy `cell-N`) | once, after cell N (zero-indexed) |
| `after-walkthrough`                 | once, after the last cell         |

`render_banner(slug, position)` resolves both anchor spellings and
returns one `.cell-banner` row holding every figure attached to that
position. Adding a banner figure is a one-line edit in
`src/marginalia.py`.

## Authoring model

### What contributors do

Nothing new. Example markdown stays:

```
:::cell
prose…
```python
…
```
```output
…
```
:::
```

There is no `:::figure` block, no frontmatter key, no caption alongside
the prose. Contributors merge cell content; the figure layer is composed
independently.

### What the project owner does

Edit `docs/quality-registries.toml`. Add `[[figure_attachments]]` and
`[[example_figure_scores]]` entries. If the figure is new, add a paint
function (composed from grammar primitives) and register it in `FIGURES` in
`src/marginalia.py`. Done.

## Pipeline invariants (root-cause rules)

These rules exist because we hit, and fixed, both failure modes
explicitly. Re-introducing either is a defect.

1. **The SVG element renders at intrinsic CSS-pixel size.**
   `Canvas.to_svg()` emits `width="W"` and `height="H"` matching the
   `viewBox`. CSS that displays a figure must use `max-width: 100%`,
   never `width: 100%`. With `width: 100%` a small viewBox is stretched
   to fill the container, which doubles or triples the apparent text
   size inside; with `max-width: 100%` the figure renders at its
   designed size and only shrinks when the container is narrower.

2. **A figure's diagrammatic content does not duplicate its figcaption.**
   Where a figure is rendered with a `<figcaption>` (production cell
   pages, prototype journey pages, the journey-figures gestalt) the
   SVG must not contain an inline `<text>` that repeats the caption's
   sentence. Captions are the canonical prose; the SVG is diagrammatic.
   Functional labels inside the SVG (`stdout`, `iter()`, `next()`,
   `await`, panel tags like `before` / `after`, type-signature
   annotations like `x: int | str | None`) are diagrammatic — they
   name a part of the figure, not the figure as a whole. A full
   sentence describing the figure is prose and belongs in the
   figcaption.

   The `marginalia-gestalt` review page is an exception: cards there
   have no figcaption, so inline prose can stand in as the only
   explanation. Figures destined for promotion to the production
   registry must drop their inline prose first.

## Files

- `src/marginalia_grammar.py` — palette, tokens, words, phrases, metrics.
  Aligned with `public/site.css` design tokens; figures use the four
  palette constants and never pick colours directly.
- `src/marginalia.py` — figure registry (`FIGURES`) and attachment map.
  Exports `render_banner(slug, position)` for the position grammar
  (`render_for_anchor` remains as an anchor-spelling wrapper).
- `src/app.py` — `_render_walkthrough` is the walkthrough-level
  renderer: it interleaves cells with `before`, `after-cell-N`, and
  `after-walkthrough` banners.
- `public/site.css` — `.cell-banner` rules. Production uses the
  banner-between grammar; cells always render with the prose|code
  2-column grid and never receive a `has-figure` class.
- `scripts/build_prototypes.py` — already implements the banner grammar
  and journey-section grammar so prototypes can validate it before
  production migration.

## Edge cases

- **Many figures in one banner.** Auto-fit grid handles 1 (centered,
  larger), 2 (small-multiple pair), 3+ (wraps as content allows). More
  than 3 in one banner is usually a signal that two adjacent banners
  are clearer.
- **No figures attached.** The page renders bit-for-bit identical to
  today.
- **Print.** Banners and cells both flow naturally in single-column
  print contexts.
- **Very narrow viewports (≤340px).** Banner figures stack via the
  auto-fit grid; SVGs scale via `max-width: 100%`. Cells keep their
  existing 980px breakpoint for collapsing the 2-col grid.

## Non-goals

- **No JavaScript-driven layout.** No scroll listener, no resize observer,
  no popup affordance. Pure CSS + server-side rendering.
- **No viewport-conditional layout.** The earlier margin-overlay approach
  required a 1440px+ viewport to work; that complexity is gone.
- **No contributor surface.** Contributors do not author figures or
  preview placement.
- **No chromatic decoration.** Figures use only the locked palette
  (`--text`, `--muted`, `--accent`, `--accent-soft`-equivalent neutral).
  Emphasis is scarce: at most one accent mark per figure, used only for
  the single element the prose names.
