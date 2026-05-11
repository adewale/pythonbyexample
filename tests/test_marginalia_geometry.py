"""Geometry contracts for every figure in src/marginalia.py.

These tests fix two classes of bug the visual audit caught:

  1. Clipping: an element extends outside the padded viewBox and gets
     cropped at render time. Symptom: the first row's type tag was
     invisible on /examples/values because it sat at y=-3 with no
     padding.

  2. Element-element collision: a text label's bounding box partially
     overlaps a rect it isn't meant to be inside. Symptom: on
     /examples/values, the "STR"/"LIST"/"DICT" tags sat on top of the
     box above them, making the type names unreadable.

Both contracts are asserted across all 109 figures. New figures are
covered automatically because the tests iterate FIGURES.
"""
from __future__ import annotations

import re
import unittest

from src.marginalia import ATTACHMENTS, FIGURES, SCORES
from src.marginalia_grammar import Canvas


# The gestalt review pages under /prototyping/* render the same paint
# functions that ship on /examples/<slug>, so auditing FIGURES is
# sufficient — there is no separate gestalt registry to walk.
ALL_FIGURES: dict[str, tuple] = FIGURES

ATTR = re.compile(r'([\w-]+)="([^"]+)"')

# Padding emitted by Canvas.to_svg(). Must agree with the constants in
# src/marginalia_grammar.py.
PAD_TOP, PAD_X, PAD_BOTTOM = 14, 14, 14

# Approximate character widths as a multiple of font-size. These are
# conservative upper bounds for the fonts the grammar emits; the audit
# would rather flag a borderline-clean figure than miss a real overflow.
# Sans uppercase (tag font) is wider than mixed case — the tag()
# primitive upper-cases its argument, so the conservative bound for
# sans must cover uppercase letters like L, O, P with tracking 0.5.
CHAR_WIDTH = {
    "mono": 0.62,    # JetBrains Mono / IBM Plex Mono
    "sans": 0.65,    # Source Sans Pro / system sans, uppercase + tracking
    "serif": 0.52,   # Iowan Old Style / Charter italic
}


def font_class(family: str) -> str:
    if "Mono" in family or "monospace" in family:
        return "mono"
    if "serif" in family or "Iowan" in family or "Charter" in family:
        return "serif"
    return "sans"


def text_bbox(d: dict, content: str) -> tuple[float, float, float, float]:
    """Return (x, y, width, height) bounding box for a <text> element."""
    x = float(d.get("x", 0))
    y = float(d.get("y", 0))
    fs = float(d.get("font-size", 10))
    anchor = d.get("text-anchor", "start")
    family = d.get("font-family", "sans-serif")
    tracking = float(d.get("letter-spacing", 0))
    width = (CHAR_WIDTH[font_class(family)] * fs + tracking) * len(content)
    if anchor == "middle":
        x -= width / 2
    elif anchor == "end":
        x -= width
    top = y - fs
    # SVG text baseline + small descender allowance.
    height = fs * 1.3
    return x, top, width, height


def rect_bbox(d: dict) -> tuple[float, float, float, float]:
    return (
        float(d.get("x", 0)),
        float(d.get("y", 0)),
        float(d.get("width", 0)),
        float(d.get("height", 0)),
    )


def line_bbox(d: dict) -> tuple[float, float, float, float]:
    x1, y1 = float(d.get("x1", 0)), float(d.get("y1", 0))
    x2, y2 = float(d.get("x2", 0)), float(d.get("y2", 0))
    x, y = min(x1, x2), min(y1, y2)
    return x, y, abs(x2 - x1), abs(y2 - y1)


def circle_bbox(d: dict) -> tuple[float, float, float, float]:
    cx, cy = float(d.get("cx", 0)), float(d.get("cy", 0))
    r = float(d.get("r", 0))
    return cx - r, cy - r, 2 * r, 2 * r


_NUM = re.compile(r"-?\d+(?:\.\d+)?")


def path_bbox(d: dict) -> tuple[float, float, float, float]:
    """Coarse bounding box of a path: min/max of every numeric token in `d`.

    The grammar's paths are short (arrowheads and curves) and use absolute
    coordinates with no transforms, so harvesting every numeric token
    yields a safe over-estimate without writing a path parser.
    """
    coords = [float(n) for n in _NUM.findall(d.get("d", ""))]
    if not coords:
        return 0, 0, 0, 0
    xs, ys = coords[0::2], coords[1::2]
    if not xs or not ys:
        return 0, 0, 0, 0
    return min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)


def parse_parts(parts: list[str]) -> list[tuple[str, dict, str]]:
    """Yield (kind, attrs, content) for every drawable element."""
    out = []
    for part in parts:
        d = dict(ATTR.findall(part))
        if part.startswith("<rect"):
            out.append(("rect", d, ""))
        elif part.startswith("<text"):
            content = part[part.find(">") + 1 : part.find("</text>")]
            out.append(("text", d, content))
        elif part.startswith("<line"):
            out.append(("line", d, ""))
        elif part.startswith("<circle"):
            out.append(("circle", d, ""))
        elif part.startswith("<path"):
            out.append(("path", d, ""))
    return out


def element_bbox(kind: str, attrs: dict, content: str) -> tuple[float, float, float, float]:
    if kind == "rect":
        return rect_bbox(attrs)
    if kind == "text":
        return text_bbox(attrs, content)
    if kind == "line":
        return line_bbox(attrs)
    if kind == "circle":
        return circle_bbox(attrs)
    if kind == "path":
        return path_bbox(attrs)
    return 0, 0, 0, 0


def contains(outer: tuple[float, float, float, float], inner: tuple[float, float, float, float], slack: float = 0.5) -> bool:
    ox, oy, ow, oh = outer
    ix, iy, iw, ih = inner
    return (
        ix >= ox - slack
        and iy >= oy - slack
        and ix + iw <= ox + ow + slack
        and iy + ih <= oy + oh + slack
    )


def overlaps(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


class FigureClippingContract(unittest.TestCase):
    """Contract 1: every element stays inside the padded viewBox."""

    def test_every_figure_renders_inside_its_padded_viewbox(self):
        failures: list[str] = []
        for name, (paint, w, h) in ALL_FIGURES.items():
            canvas = Canvas(w=w, h=h)
            paint(canvas)
            viewbox = (-PAD_X, -PAD_TOP, w + 2 * PAD_X, h + PAD_TOP + PAD_BOTTOM)
            for kind, attrs, content in parse_parts(canvas.parts):
                bbox = element_bbox(kind, attrs, content)
                if not contains(viewbox, bbox):
                    bx, by, bw, bh = bbox
                    failures.append(
                        f"{name}: {kind} ({bx:.1f},{by:.1f},{bw:.1f}×{bh:.1f}) "
                        f"escapes viewBox {viewbox}"
                        + (f" [{content!r}]" if content else "")
                    )
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


class FigureCollisionContract(unittest.TestCase):
    """Contract 2: no text partially overlaps a rect.

    A text element is allowed to overlap a rect only if the rect fully
    contains the text (e.g. the value centered inside an object_box, or
    a type tag placed inside the box's interior). Partial overlap means
    the text is sitting on top of a different rect's edge, which is what
    made `STR`/`LIST`/`DICT` collide with the box above them on the
    /examples/values figure.
    """

    def test_no_text_partially_overlaps_a_rect(self):
        failures: list[str] = []
        for name, (paint, w, h) in ALL_FIGURES.items():
            canvas = Canvas(w=w, h=h)
            paint(canvas)
            elements = parse_parts(canvas.parts)
            rects = [(element_bbox(k, a, c), k, a) for k, a, c in elements if k == "rect"]
            for kind, attrs, content in elements:
                if kind != "text":
                    continue
                tbox = element_bbox(kind, attrs, content)
                for rbox, _, _ in rects:
                    if overlaps(tbox, rbox) and not contains(rbox, tbox):
                        failures.append(
                            f"{name}: text {content!r} {tbox} partially overlaps rect {rbox}"
                        )
                        break
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


class FigureTextCollisionContract(unittest.TestCase):
    """Contract 3: no two text elements in the same figure overlap.

    Two text bounding boxes that overlap render on top of each other
    and become unreadable. This catches narrow object_boxes whose tag
    and value compete for horizontal space (the itertools-chain bug
    where "ITER A" and "1 · 2" couldn't both fit in a 70px box).
    """

    def test_no_two_texts_overlap_in_a_figure(self):
        failures: list[str] = []
        for name, (paint, w, h) in ALL_FIGURES.items():
            canvas = Canvas(w=w, h=h)
            paint(canvas)
            texts = []
            for kind, attrs, content in parse_parts(canvas.parts):
                if kind == "text":
                    texts.append((element_bbox(kind, attrs, content), content))
            for i, (abox, ac) in enumerate(texts):
                for j in range(i + 1, len(texts)):
                    bbox, bc = texts[j]
                    if overlaps(abox, bbox):
                        failures.append(f"{name}: texts {ac!r} and {bc!r} overlap at {abox} ∩ {bbox}")
                        break
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


class FigureRegistrationContract(unittest.TestCase):
    """Contract 4: FIGURES, ATTACHMENTS, SCORES stay in sync.

    Every slug in ATTACHMENTS must be in SCORES, and vice versa.
    Every figure name an attachment points to must exist in FIGURES.
    Every paint function in FIGURES must be attached to at least one
    slug — orphan paint functions accumulate as dead code and silently
    fail to ship the design they encode.
    """

    def test_every_attached_slug_is_scored(self):
        unscored = set(ATTACHMENTS) - set(SCORES)
        self.assertEqual(unscored, set(), f"attached but unscored: {sorted(unscored)}")

    def test_every_scored_slug_is_attached(self):
        unattached = set(SCORES) - set(ATTACHMENTS)
        self.assertEqual(unattached, set(), f"scored but unattached: {sorted(unattached)}")

    def test_every_attachment_points_to_a_real_figure(self):
        names = {name for items in ATTACHMENTS.values() for _, name, _ in items}
        orphan_refs = names - set(FIGURES)
        self.assertEqual(orphan_refs, set(), f"attachments reference unknown figures: {sorted(orphan_refs)}")

    def test_no_unused_figure_paint_functions(self):
        # A figure name counts as "used" if it ships on an example page
        # (ATTACHMENTS), a journey section (SECTION_FIGURES), or appears
        # anywhere in scripts/build_prototypes.py (banner layouts and
        # gestalt galleries that aren't covered by the structured
        # registries).
        from pathlib import Path

        from src.marginalia import SECTION_FIGURES

        prototype_src = (
            Path(__file__).resolve().parents[1] / "scripts" / "build_prototypes.py"
        ).read_text()
        used = {name for items in ATTACHMENTS.values() for _, name, _ in items}
        used |= {name for name, _ in SECTION_FIGURES.values()}
        used |= {name for name in FIGURES if f'"{name}"' in prototype_src or f"'{name}'" in prototype_src}
        unused = set(FIGURES) - used
        self.assertEqual(
            unused, set(),
            f"figures defined but never rendered (orphan paint functions): {sorted(unused)}",
        )


class FigureGrammarContract(unittest.TestCase):
    """Contract 5: every emitted SVG element uses only the locked
    palette, font set, and stroke weights from marginalia_grammar.py.

    Drift here is how the design system erodes — one cardinal red
    here, one Inter font there, and suddenly the library reads as
    independently authored.
    """

    def test_every_emitted_color_is_from_the_locked_palette(self):
        from src.marginalia_grammar import INK, INK_SOFT, EMPHASIS, SOFT_FILL

        allowed = {INK, INK_SOFT, EMPHASIS, SOFT_FILL, "none"}
        failures: list[str] = []
        for name, (paint, w, h) in ALL_FIGURES.items():
            canvas = Canvas(w=w, h=h)
            paint(canvas)
            for kind, attrs, _ in parse_parts(canvas.parts):
                for key in ("fill", "stroke"):
                    color = attrs.get(key, "")
                    if color and color not in allowed:
                        failures.append(f"{name}: {kind} {key}={color!r}")
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))

    def test_every_emitted_font_is_from_the_locked_set(self):
        from src.marginalia_grammar import FONT_SERIF, FONT_MONO, FONT_SANS

        allowed = {FONT_SERIF, FONT_MONO, FONT_SANS}
        failures: list[str] = []
        for name, (paint, w, h) in ALL_FIGURES.items():
            canvas = Canvas(w=w, h=h)
            paint(canvas)
            for kind, attrs, _ in parse_parts(canvas.parts):
                family = attrs.get("font-family", "")
                if family and family not in allowed:
                    failures.append(f"{name}: {kind} font-family={family!r}")
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))

    def test_every_stroke_width_is_from_the_locked_set(self):
        allowed = {"0.6", "1.0", "1.4", "0.5"}  # W_HAIRLINE, W_STROKE, W_EMPHASIS, W_GHOST
        failures: list[str] = []
        for name, (paint, w, h) in ALL_FIGURES.items():
            canvas = Canvas(w=w, h=h)
            paint(canvas)
            for kind, attrs, _ in parse_parts(canvas.parts):
                weight = attrs.get("stroke-width", "")
                if weight and weight not in allowed:
                    failures.append(f"{name}: {kind} stroke-width={weight!r}")
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


class SectionFigureContract(unittest.TestCase):
    """Contract 10: every journey section in app.py JOURNEYS has a
    figure in SECTION_FIGURES, and every SECTION_FIGURES entry maps
    to a real FIGURES paint function.
    """

    def test_every_journey_section_has_a_figure(self):
        from src.app import JOURNEYS
        from src.marginalia import SECTION_FIGURES

        section_titles = {s["title"] for j in JOURNEYS for s in j["sections"]}
        missing = section_titles - set(SECTION_FIGURES)
        self.assertEqual(
            missing, set(),
            f"journey sections without a figure: {sorted(missing)}",
        )

    def test_every_section_figure_points_to_a_real_paint_function(self):
        from src.marginalia import SECTION_FIGURES

        orphan_refs = {name for name, _ in SECTION_FIGURES.values()} - set(FIGURES)
        self.assertEqual(
            orphan_refs, set(),
            f"SECTION_FIGURES references unknown figures: {sorted(orphan_refs)}",
        )

    def test_every_section_figure_caption_is_unique(self):
        from collections import defaultdict
        from src.marginalia import SECTION_FIGURES

        caption_to_titles: dict[str, list[str]] = defaultdict(list)
        for title, (_, caption) in SECTION_FIGURES.items():
            if caption:
                caption_to_titles[caption].append(title)
        duplicates = {c: t for c, t in caption_to_titles.items() if len(t) > 1}
        self.assertEqual(duplicates, {}, f"duplicate section captions: {duplicates}")


class FigureCaptionContract(unittest.TestCase):
    """Contract 5b: every attachment caption is unique.

    A figure can legitimately be reused across slugs (iter-protocol
    serves four iteration examples). But each lesson should frame the
    figure in its own voice — copying the caption verbatim means two
    lessons share the same prose, which is the same anti-pattern as
    two examples sharing the same code.
    """

    def test_no_caption_is_used_on_more_than_one_slug(self):
        from collections import defaultdict

        caption_to_slugs: dict[str, list[str]] = defaultdict(list)
        for slug, items in ATTACHMENTS.items():
            for _, _, caption in items:
                if caption:
                    caption_to_slugs[caption].append(slug)
        duplicates = {cap: slugs for cap, slugs in caption_to_slugs.items() if len(slugs) > 1}
        message_lines = [
            f"{slugs!r} share caption {cap!r}" for cap, slugs in duplicates.items()
        ]
        self.assertEqual(duplicates, {}, "\n  " + "\n  ".join(message_lines))


class FigureAnchorContract(unittest.TestCase):
    """Contract 6: every cell-N attachment anchor points to a real cell.

    Adding an attachment that points past the end of an example's
    walkthrough leaves the figure orphan — `render_for_anchor` returns
    empty and the figure never ships. Catches a typo or a stale
    attachment after a markdown example loses a cell.
    """

    def test_every_attachment_anchor_resolves_to_a_real_cell(self):
        # Imported lazily to avoid pulling the example loader for every
        # test in this file.
        import re as _re
        from src.example_loader import load_examples

        _, examples = load_examples()
        by_slug = {ex["slug"]: ex for ex in examples}

        failures: list[str] = []
        for slug, items in ATTACHMENTS.items():
            ex = by_slug.get(slug)
            if ex is None:
                failures.append(f"{slug}: ATTACHMENT exists but no markdown example matches")
                continue
            cells = ex.get("walkthrough", [])
            for anchor, name, _ in items:
                match = _re.match(r"cell-(\d+)$", anchor)
                if not match:
                    failures.append(f"{slug}: anchor {anchor!r} is not cell-N")
                    continue
                if int(match.group(1)) >= len(cells):
                    failures.append(
                        f"{slug}: anchor {anchor!r} → figure {name!r}, "
                        f"but example has only {len(cells)} cell(s)"
                    )
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


class FigureScoreContract(unittest.TestCase):
    """Contract 7: every SCORES entry is a real assessment.

    A score must be a number in [0, 10] (the rubric's range) with a
    non-empty short commentary. Catches typos where a comma slips and
    a tuple turns into something else.
    """

    def test_every_score_is_in_range_with_commentary(self):
        failures: list[str] = []
        for slug, entry in SCORES.items():
            if not isinstance(entry, tuple) or len(entry) != 2:
                failures.append(f"{slug}: not a (score, commentary) tuple")
                continue
            score, commentary = entry
            if not isinstance(score, (int, float)) or not 0 <= score <= 10:
                failures.append(f"{slug}: score {score!r} outside [0, 10]")
            if not isinstance(commentary, str) or not commentary.strip():
                failures.append(f"{slug}: empty commentary")
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


class FigureSizeContract(unittest.TestCase):
    """Contract 8: every figure's RENDERED width fits the banner ceiling.

    Canvas.to_svg emits explicit width/height attributes scaled by
    Canvas.INTRINSIC_SCALE so figures fill more of the available
    column on desktop. The largest banner cap in public/site.css is
    640px (.cell-banner--1 and .journey-section-figure use
    clamp(280px, 65vw/70vw, 640px)). A figure whose rendered width
    exceeds 640px scales down on every viewport above the clamp's
    middle term, shrinking text in ways the paint code didn't plan
    for.

    Rendered width = INTRINSIC_SCALE * (Canvas.w + 2 * PAD_X).
    """

    BANNER_MAX_WIDTH = 640  # cell-banner--1 / journey-section-figure max-width

    def test_every_figure_fits_the_banner(self):
        from src.marginalia_grammar import Canvas as _C

        failures: list[str] = []
        for name, (_, w, _) in ALL_FIGURES.items():
            rendered = round((w + 2 * PAD_X) * _C.INTRINSIC_SCALE)
            if rendered > self.BANNER_MAX_WIDTH:
                failures.append(
                    f"{name}: rendered width {rendered}px exceeds "
                    f"{self.BANNER_MAX_WIDTH}px banner ceiling"
                )
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


class FigureEmphasisScarcityContract(unittest.TestCase):
    """Contract 9: at most one accent mark (EMPHASIS-colored) per figure.

    From docs/example-figure-rubric.md criterion 7: "at most one accent
    mark per figure. The accent goes on the single element the cell
    prose names (the live mutation, the captured cell, the dispatch
    arrow). Three accent marks competing for attention is no emphasis
    at all."

    An accent mark is counted as one whole arrow (the line + polygon
    pair that `closed_arrow(emphasis=True)` emits), one orange caret,
    or one element whose fill or stroke is the EMPHASIS colour and
    isn't part of those compound shapes.
    """

    def test_at_most_one_accent_per_figure(self):
        from src.marginalia_grammar import EMPHASIS

        failures: list[str] = []
        for name, (paint, w, h) in ALL_FIGURES.items():
            canvas = Canvas(w=w, h=h)
            paint(canvas)
            accents = 0
            for part in canvas.parts:
                attrs = dict(ATTR.findall(part))
                # The closed_arrow primitive emits BOTH a coloured <line>
                # and a coloured <polygon> for one arrow head; count the
                # polygon and ignore the line to avoid double-counting.
                if part.startswith("<polygon") and attrs.get("fill") == EMPHASIS:
                    accents += 1
                elif part.startswith("<circle") and attrs.get("fill") == EMPHASIS:
                    accents += 1
                elif part.startswith("<rect") and attrs.get("stroke") == EMPHASIS:
                    accents += 1
            if accents > 1:
                failures.append(f"{name}: {accents} accent marks (rubric allows at most 1)")
        self.assertEqual(failures, [], "\n  " + "\n  ".join(failures))


if __name__ == "__main__":
    unittest.main()
