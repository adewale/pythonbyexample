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

from src.marginalia import FIGURES
from src.marginalia_grammar import Canvas

ATTR = re.compile(r'([\w-]+)="([^"]+)"')

# Padding emitted by Canvas.to_svg(). Must agree with the constants in
# src/marginalia_grammar.py.
PAD_TOP, PAD_X, PAD_BOTTOM = 14, 8, 14

# Approximate character widths as a multiple of font-size. These are
# conservative upper bounds for the fonts the grammar emits; the audit
# would rather flag a borderline-clean figure than miss a real overflow.
CHAR_WIDTH = {
    "mono": 0.62,    # JetBrains Mono / IBM Plex Mono
    "sans": 0.58,    # Source Sans Pro / system sans
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
        for name, (paint, w, h) in FIGURES.items():
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
        for name, (paint, w, h) in FIGURES.items():
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


if __name__ == "__main__":
    unittest.main()
