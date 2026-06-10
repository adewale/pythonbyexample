"""Marginalia grammar — primitives for the Python By Example diagram set.

The grammar enforces a single visual language. Cards compose figures from
WORDS and PHRASES; metrics, palette, stroke weights, and typography are
locked at module level. There is no escape hatch for raw SVG.

Hierarchy:
    TOKENS  — atomic marks. Never called directly by cards.
    WORDS   — composable shapes (name_box, object_box, cell, register, …).
    PHRASES — recurring multi-word constructions (bind, dispatch, lanes, …).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable

# ─── Palette ───────────────────────────────────────────────────────────
# Aligned with public/site.css design tokens. These are the only
# colours figures may use; cards never pick a colour directly.
#   INK       site --text         (warm dark brown)
#   INK_SOFT  site --muted        (--text at 70%)
#   EMPHASIS  site --accent       (the brand orange)
#   SOFT_FILL site --accent-soft  (--accent at ~8%)
INK = "#521000"
INK_SOFT = "rgba(82, 16, 0, 0.7)"
EMPHASIS = "#FF4801"
# A neutral warm tint built from --text at 5%. Object boxes need to read as
# quiet containers; tinting them with --accent-soft made every box look
# highlighted, which broke the "emphasis is scarce" rule.
SOFT_FILL = "rgba(82, 16, 0, 0.05)"

# ─── Stroke weights ────────────────────────────────────────────────────
W_HAIRLINE = 0.6
W_STROKE = 1.0
W_EMPHASIS = 1.4
W_GHOST = 0.5
GHOST_OPACITY = 0.4
DASH = "2 2"

# ─── Locked geometry — never override per-card ─────────────────────────
GAP_S = 8
GAP_L = 16
DOT_R = 2.5
TICK_LEN = 6
NODE_R = 14
ARROW_OPEN = 5
ARROW_CLOSED = 7

NAME_W = 60
NAME_H = 24
OBJECT_W = 80
OBJECT_H = 32
CELL = 24
WORD_W = 44

# ─── Typography ────────────────────────────────────────────────────────
FONT_SERIF = "'Iowan Old Style', Charter, Georgia, serif"
FONT_MONO = "'JetBrains Mono', 'IBM Plex Mono', Menlo, monospace"
FONT_SANS = "-apple-system, 'Source Sans Pro', sans-serif"
SIZE_BODY = 11
SIZE_MONO = 10
SIZE_SMALL = 9
SIZE_TAG = 8
BASELINE = 4  # add to box-center y to render text vertically centered

# ─── Text metrics ──────────────────────────────────────────────────────
# Single source of truth for character advance. Paint code uses
# MONO_ADVANCE (the font's exact advance) to compute positions; the
# geometry contracts use BBOX_ADVANCE (deliberately conservative
# over-estimates) to detect clipping and collision. Keeping both here —
# instead of one in a paint comment and one in the test file — means a
# recalibration happens in one place and both consumers move together.
MONO_ADVANCE = 0.6  # JetBrains Mono advances 600/1000 units per em.
BBOX_ADVANCE = {
    "mono": 0.62,        # JetBrains Mono / IBM Plex Mono
    "sans_upper": 0.65,  # Source Sans Pro uppercase (tag font)
    "sans": 0.55,        # Source Sans Pro mixed-case (label font)
    "serif": 0.52,       # Iowan Old Style / Charter italic
}


def font_class(family: str) -> str:
    if "Mono" in family or "monospace" in family:
        return "mono"
    # "sans-serif" contains "serif" as a substring; check sans first
    # so the system-sans fallback string doesn't misclassify.
    if "sans" in family.lower():
        return "sans"
    if "serif" in family or "Iowan" in family or "Charter" in family:
        return "serif"
    return "sans"


def text_width(content: str, family: str, size: float, tracking: float = 0.0) -> float:
    """Conservative rendered width of a text run, for bbox math.

    Upper-cased sans glyphs (the tag font: LOOP, INT, …) advance ~18%
    wider than mixed-case sans; differentiating the two keeps the
    contracts tight enough to catch real clips without over-flagging
    every mixed-case label that kisses a sibling rect.
    """
    klass = font_class(family)
    if klass == "sans" and content == content.upper() and any(ch.isalpha() for ch in content):
        per_char = BBOX_ADVANCE["sans_upper"] * size
    else:
        per_char = BBOX_ADVANCE[klass] * size
    return (per_char + tracking) * len(content)


@dataclass
class Canvas:
    w: int = 320
    h: int = 110
    parts: list[str] = field(default_factory=list)
    # Semantic accent census. Every primitive that paints EMPHASIS
    # increments _accents (or sets _gates_painted); the scarcity
    # contract asserts accent_count() <= 1 from here instead of trying
    # to reverse-engineer marks from SVG output, where an arrow's
    # shaft+head pair and a standalone gate line are indistinguishable.
    _accents: int = 0
    _gates_painted: bool = False

    def accent_count(self) -> int:
        """Number of accent marks on the canvas, per the scarcity rule.

        Gates are repeated structural punctuation — every pause point on
        a ribbon, in every ribbon of the figure — and read as one system,
        so all gates collectively count as a single accent. A gate set
        plus any focal accent (emphasis arrow, caret, dot, traced path)
        is still two marks competing for attention, and still fails.
        """
        return self._accents + (1 if self._gates_painted else 0)

    # ── tokens (private; cards should not reach for these) ────────────
    def _add(self, s: str) -> None:
        self.parts.append(s)

    def _line(self, x1, y1, x2, y2, *, color=INK, weight=W_STROKE, dash=None, opacity=1.0):
        attrs = [f'x1="{x1}"', f'y1="{y1}"', f'x2="{x2}"', f'y2="{y2}"',
                 f'stroke="{color}"', f'stroke-width="{weight}"']
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        if opacity < 1.0:
            attrs.append(f'opacity="{opacity}"')
        self._add(f"<line {' '.join(attrs)}/>")

    def hairline(self, x1, y1, x2, y2):
        self._line(x1, y1, x2, y2, weight=W_HAIRLINE)

    def stroke(self, x1, y1, x2, y2):
        self._line(x1, y1, x2, y2)

    def ghost(self, x1, y1, x2, y2):
        self._line(x1, y1, x2, y2, weight=W_GHOST, opacity=GHOST_OPACITY)

    def dashed(self, x1, y1, x2, y2):
        self._line(x1, y1, x2, y2, weight=W_HAIRLINE, dash=DASH)

    def dot(self, x, y, *, emphasis=False):
        if emphasis:
            self._accents += 1
        self._add(f'<circle cx="{x}" cy="{y}" r="{DOT_R}" fill="{EMPHASIS if emphasis else INK}"/>')

    def tick(self, x, y, *, length=TICK_LEN):
        self.hairline(x, y - length / 2, x, y + length / 2)

    def open_arrow(self, x1, y1, x2, y2):
        """Axis-style arrow: hairline ending in tiny open V."""
        self.hairline(x1, y1, x2, y2)
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        bx, by = x2 - ARROW_OPEN * ux, y2 - ARROW_OPEN * uy
        px, py = -uy * (ARROW_OPEN / 2), ux * (ARROW_OPEN / 2)
        self._add(
            f'<path d="M{x2},{y2} L{bx + px},{by + py} M{x2},{y2} L{bx - px},{by - py}" '
            f'stroke="{INK}" stroke-width="{W_HAIRLINE}" fill="none"/>'
        )

    def closed_arrow(self, x1, y1, x2, y2, *, emphasis=False):
        """Becomes-this / dispatches-to: line + filled wedge.

        Defaults to ink. Pass emphasis=True only for THE single live arrow
        per figure — the one mark the surrounding prose explicitly names.
        Saturated --accent strokes everywhere break visual scarcity.
        """
        if emphasis:
            self._accents += 1
        color = EMPHASIS if emphasis else INK
        weight = W_EMPHASIS if emphasis else W_STROKE
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        end_x, end_y = x2 - ARROW_CLOSED * ux, y2 - ARROW_CLOSED * uy
        self._line(x1, y1, end_x, end_y, color=color, weight=weight)
        bx, by = x2 - ARROW_CLOSED * ux, y2 - ARROW_CLOSED * uy
        px, py = -uy * (ARROW_CLOSED / 2.5), ux * (ARROW_CLOSED / 2.5)
        self._add(f'<polygon points="{x2},{y2} {bx + px},{by + py} {bx - px},{by - py}" fill="{color}"/>')

    # ── text ──────────────────────────────────────────────────────────
    def _text(self, x, y, s, *, family, size, anchor, color, italic=False, tracking=None):
        attrs = [f'x="{x}"', f'y="{y}"', f'font-family="{family}"', f'font-size="{size}"',
                 f'fill="{color}"', f'text-anchor="{anchor}"']
        if italic:
            attrs.append('font-style="italic"')
        if tracking:
            attrs.append(f'letter-spacing="{tracking}"')
        self._add(f"<text {' '.join(attrs)}>{s}</text>")

    def mono(self, x, y, s, *, anchor="middle", size=SIZE_MONO, color=INK):
        self._text(x, y, s, family=FONT_MONO, size=size, anchor=anchor, color=color)

    def ident(self, x, y, s, *, anchor="middle", color=INK):
        self._text(x, y, s, family=FONT_SERIF, size=SIZE_BODY, anchor=anchor, color=color, italic=True)

    def label(self, x, y, s, *, anchor="start"):
        self._text(x, y, s, family=FONT_SANS, size=SIZE_SMALL, anchor=anchor, color=INK_SOFT)

    def tag(self, x, y, s, *, anchor="start"):
        self._text(x, y, s.upper(), family=FONT_SANS, size=SIZE_TAG,
                   anchor=anchor, color=INK_SOFT, tracking="0.5")

    # ── words ─────────────────────────────────────────────────────────
    def name_box(self, x, y, name):
        """Open rect with italic identifier. Returns right-edge midpoint."""
        self._add(
            f'<rect x="{x}" y="{y}" width="{NAME_W}" height="{NAME_H}" fill="none" '
            f'stroke="{INK}" stroke-width="{W_STROKE}"/>'
        )
        self.ident(x + NAME_W / 2, y + NAME_H / 2 + BASELINE, name)
        return (x + NAME_W, y + NAME_H / 2)

    def object_box(self, x, y, type_tag, value, *, w=OBJECT_W, h=OBJECT_H, soft=True, tag_position="above"):
        """Filled rect with type tag and value centered. Returns left-edge midpoint.

        tag_position="above" (default) places the type tag at y - 3, just
        above the box — natural for an isolated box. Pass
        tag_position="inside" when callers stack object_boxes vertically:
        the tag then sits in the box's top-left corner instead of
        colliding with the box above it.
        """
        fill = SOFT_FILL if soft else "none"
        self._add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
            f'stroke="{INK}" stroke-width="{W_STROKE}"/>'
        )
        if type_tag:
            tag_y = y + SIZE_TAG + 2 if tag_position == "inside" else y - 5
            self.tag(x + 4, tag_y, type_tag)
        if value:
            self.mono(x + w / 2, y + h / 2 + BASELINE, value)
        return (x, y + h / 2)

    def cell(self, x, y, content="", *, w=CELL, h=CELL, ghost=False, soft=False):
        weight = W_GHOST if ghost else W_STROKE
        opacity = f' opacity="{GHOST_OPACITY}"' if ghost else ""
        fill = SOFT_FILL if soft else "none"
        self._add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
            f'stroke="{INK}" stroke-width="{weight}"{opacity}/>'
        )
        if content:
            self.mono(x + w / 2, y + h / 2 + BASELINE, content)

    def cells(self, x, y, items, *, w=CELL, h=CELL):
        """Row of cells. items is a list of strings (use '' for empty)."""
        for i, c in enumerate(items):
            self.cell(x + i * w, y, c, w=w, h=h)
        return (x, y, x + len(items) * w, y + h)

    def caret(self, x, y_top, *, emphasis=True):
        """Triangular caret pointing down into the cell whose top is at y_top.

        Defaults to the orange emphasis colour because a caret typically
        marks the live position. Set emphasis=False when multiple carets
        appear in the same figure (small multiples) and the surrounding
        prose only names one of them — the others paint in ink so the
        scarce-emphasis rule still holds.
        """
        if emphasis:
            self._accents += 1
        fill = EMPHASIS if emphasis else INK
        self._add(f'<polygon points="{x},{y_top - 1} {x - 4},{y_top - 7} {x + 4},{y_top - 7}" fill="{fill}"/>')

    def mono_divider(self, x_start, index, y_top, y_bot, *, size=SIZE_MONO):
        """Dashed vertical centred on character `index` of a start-anchored
        mono string drawn at x_start.

        The x is computed from the font's advance (MONO_ADVANCE), not
        eyeballed: hand-tuned positions drift, computed positions match
        the rendered glyph. Returns the computed x.
        """
        advance = MONO_ADVANCE * size
        x = x_start + index * advance + advance / 2
        self.dashed(x, y_top, x, y_bot)
        return x

    def register(self, x, y, w, *, divisions=None, between=False):
        """Hairline with regular ticks."""
        self.hairline(x, y, x + w, y)
        if divisions is None:
            return
        step = w / divisions
        for i in range(divisions + 1):
            self.tick(x + i * step, y)
        if between:
            for i in range(divisions):
                self.hairline(x + i * step + step / 2, y - TICK_LEN / 3,
                              x + i * step + step / 2, y + TICK_LEN / 3)

    def node(self, x, y, label, *, r=NODE_R, ghost=False):
        weight = W_GHOST if ghost else W_STROKE
        opacity = f' opacity="{GHOST_OPACITY}"' if ghost else ""
        self._add(
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" '
            f'stroke="{INK}" stroke-width="{weight}"{opacity}/>'
        )
        self.mono(x, y + BASELINE, label, size=SIZE_SMALL)

    def frame(self, x, y, w, h, *, label=None, ghost=False):
        weight = W_GHOST if ghost else W_STROKE
        opacity = f' opacity="{GHOST_OPACITY}"' if ghost else ""
        self._add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" '
            f'stroke="{INK}" stroke-width="{weight}"{opacity}/>'
        )
        if label:
            self.tag(x + 6, y - 3, label)

    def gate(self, x, y_top, y_bot):
        """Vertical EMPHASIS line crossing a ribbon."""
        self._gates_painted = True
        self._line(x, y_top, x, y_bot, color=EMPHASIS, weight=W_EMPHASIS)

    def ribbon(self, x, y, w, *, h=30, gates=(), soft_segments=()):
        """Horizontal track with optional gates and soft fills."""
        for x0, x1 in soft_segments:
            self._add(
                f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" '
                f'fill="{SOFT_FILL}" stroke="none"/>'
            )
        self._add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" '
            f'stroke="{INK}" stroke-width="{W_STROKE}"/>'
        )
        for gx in gates:
            self.gate(gx, y, y + h)

    def lane(self, y, *, x0=20, x1=300, label=None):
        """Horizontal hairline used for parallel dispatch lanes."""
        self.hairline(x0, y, x1, y)
        if label:
            self.tag(x0 - 6, y + 3, label, anchor="end")

    # ── phrases ───────────────────────────────────────────────────────
    def bind(self, x, y, name, type_tag, value, *, object_w=OBJECT_W, gap=40):
        """name → object. The foundational picture."""
        nx, ny = self.name_box(x, y + (OBJECT_H - NAME_H) / 2, name)
        ox, oy = self.object_box(nx + gap, y, type_tag, value, w=object_w)
        self.closed_arrow(nx + 2, ny, ox - 2, oy)
        return (x, y, nx + gap + object_w, y + OBJECT_H)

    def two_names_one_object(self, x, y, tag_text, name_a, name_b, value, *, object_w=OBJECT_W):
        """Two names bound to one shared object — the aliasing picture.

        Twin panels and twin figures (aliasing-mutation,
        tuple-no-mutation) must keep this layout coordinate-identical;
        composing it as a phrase makes drift structurally impossible.
        y is the top of the first name box; the tag paints 6 above it.
        """
        if tag_text:
            self.tag(x, y - 6, tag_text)
        self.name_box(x, y, name_a)
        self.name_box(x, y + 30, name_b)
        self.closed_arrow(x + NAME_W, y + 12, x + NAME_W + 26, y + 28, emphasis=False)
        self.closed_arrow(x + NAME_W, y + 42, x + NAME_W + 26, y + 28, emphasis=False)
        self.object_box(x + NAME_W + 28, y + 14, "", value, w=object_w, h=28)

    def type_triangle(self, third_label, third_value, *, third_w=60):
        """instance → class → <third> — the triangle shared by the
        class-triangle / metaclass-triangle twin figures. The shared
        coordinates live here so the twins cannot drift apart; only the
        third frame's label, value, and width vary.
        """
        self.dot(20, 28)
        self.label(20, 54, "instance", anchor="middle")
        self.closed_arrow(26, 28, 86, 28, emphasis=False)
        self.frame(88, 10, 60, 36, label="class")
        self.mono(118, 32, "Class")
        self.closed_arrow(148, 28, 208, 28, emphasis=False)
        self.frame(210, 10, third_w, 36, label=third_label)
        self.mono(210 + third_w / 2, 32, third_value)

    def dispatch(self, x, y, src, dst, *, src_w=70, dst_w=120):
        """Source form → method form."""
        self.object_box(x, y, "", src, w=src_w, soft=False)
        self.closed_arrow(x + src_w + 4, y + OBJECT_H / 2, x + src_w + 36, y + OBJECT_H / 2)
        self.object_box(x + src_w + 40, y, "", dst, w=dst_w, soft=True)

    def connect(self, ax, ay, ar, bx, by, br, *, kind="stroke", offset=0):
        """Edge between two circles, terminating tangentially at each boundary.

        Endpoints are computed from the line of centers so the edge meets each
        circle exactly — never short of it, never inside it.

        kind:    "stroke" | "ghost" | "dashed" | "arrow" | "emphasis"
        offset:  extra gap past each circle, in viewBox units
                 (0 for tree edges, 2 for state-machine arrows)
        """
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        sx = ax + (ar + offset) * ux
        sy = ay + (ar + offset) * uy
        ex = bx - (br + offset) * ux
        ey = by - (br + offset) * uy
        if kind == "stroke":
            self.stroke(sx, sy, ex, ey)
        elif kind == "ghost":
            self.ghost(sx, sy, ex, ey)
        elif kind == "dashed":
            self.dashed(sx, sy, ex, ey)
        elif kind == "arrow":
            self.closed_arrow(sx, sy, ex, ey, emphasis=False)
        elif kind == "emphasis":
            self.closed_arrow(sx, sy, ex, ey, emphasis=True)
        else:
            raise ValueError(f"unknown connect kind: {kind!r}")

    def lanes(self, ys_labels, *, x0=40, x1=300, path=None):
        """Stack of parallel lanes; optional traced emphasis path through them."""
        for y, lab in ys_labels:
            self.lane(y, x0=x0, x1=x1, label=lab)
        if path:
            # The traced path and its terminal dot are one mark: count
            # once here and paint the dot directly so dot() doesn't
            # count it a second time.
            self._accents += 1
            d = " ".join(("M" if i == 0 else "L") + f"{px},{py}" for i, (px, py) in enumerate(path))
            self._add(f'<path d="{d}" stroke="{EMPHASIS}" stroke-width="{W_EMPHASIS}" fill="none"/>')
            self._add(f'<circle cx="{path[-1][0]}" cy="{path[-1][1]}" r="{DOT_R}" fill="{EMPHASIS}"/>')

    # ── render ────────────────────────────────────────────────────────
    # Figures render at INTRINSIC_SCALE × their viewBox dimensions. The
    # viewBox preserves the geometry (so paint coords, contracts, and
    # collision math don't change); the explicit width/height grow so
    # browsers render the figure larger by default. CSS max-width on the
    # banner container clamps the upper bound; CSS max-width: 100% on
    # the SVG scales it down for narrow viewports. The net effect:
    # figures fill ~1.6× more horizontal space on desktop and still
    # shrink cleanly to mobile widths.
    #
    # The PAD_* offsets give every figure a small margin around its
    # registered canvas. Most figures place a type-tag at y - 5 above
    # the topmost box, which without padding renders outside the
    # viewBox and gets clipped. PAD_TOP=14 covers the SIZE_TAG=8 font
    # plus its baseline offset. PAD_X handles the rare paint function
    # that draws slightly negative x. PAD_BOTTOM absorbs small
    # accidental overflows.
    INTRINSIC_SCALE = 1.6

    def to_svg(self) -> str:
        pad_top, pad_x, pad_bottom = 14, 14, 14
        vb_w = self.w + 2 * pad_x
        vb_h = self.h + pad_top + pad_bottom
        out_w = round(vb_w * self.INTRINSIC_SCALE)
        out_h = round(vb_h * self.INTRINSIC_SCALE)
        # aria-hidden: the figcaption is the canonical voice for every
        # figure; without it screen readers walk the SVG's internal
        # <text> fragments ("STR", "next()", …) out of context before
        # reaching the caption.
        return (
            f'<svg viewBox="-{pad_x} -{pad_top} {vb_w} {vb_h}" '
            f'width="{out_w}" height="{out_h}" '
            f'aria-hidden="true" focusable="false" '
            f'xmlns="http://www.w3.org/2000/svg">'
            + "".join(self.parts)
            + "</svg>"
        )


@dataclass
class Card:
    slug: str
    title: str
    section: str
    order: int | str
    figure: Callable[[Canvas], None]
    note: str = ""
    width: int = 320
    height: int = 110
    is_journey: bool = False
    score: float | None = None
    score_note: str = ""

    def render_html(self) -> str:
        c = Canvas(w=self.width, h=self.height)
        self.figure(c)
        kind = " journey" if self.is_journey else ""
        if isinstance(self.order, int):
            eyebrow = f"{self.section} · {self.order:02d}"
        else:
            eyebrow = f"Journey · {self.order}"
        note_html = f'  <p class="note">{self.note}</p>\n' if self.note else ""
        score_html = ""
        if self.score is not None:
            band = (
                "score-high" if self.score >= 9.0
                else "score-mid" if self.score >= 8.0
                else "score-low"
            )
            note = f" · {self.score_note}" if self.score_note else ""
            score_html = f'  <p class="score {band}">{self.score:.1f}{note}</p>\n'
        return (
            f'<div class="card{kind}">\n'
            f'  <p class="eyebrow">{eyebrow}</p>\n'
            f'  <h3>{self.title}</h3>\n'
            f"  {c.to_svg()}\n"
            f"{score_html}"
            f"{note_html}"
            f"</div>"
        )
