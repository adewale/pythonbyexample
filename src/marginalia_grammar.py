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
from collections.abc import Callable
from dataclasses import dataclass, field
from xml.sax.saxutils import escape as xml_escape

# Padding emitted around every figure's registered canvas by
# Canvas.to_svg(); the geometry contracts import these so paint code and
# tests share one source of truth.
PAD_TOP = 14
PAD_X = 14
PAD_BOTTOM = 14

# ─── Palette ───────────────────────────────────────────────────────────
# Figures paint with CSS custom properties, not literal colours. Inline
# SVG inherits custom properties from the page, so one paint function
# renders correctly in light mode, in dark mode, and on the social
# cards: whichever stylesheet wraps the figure decides the ink. The
# four names below are the only colours figures may use; cards never
# pick a colour directly.
#   INK       --fig-ink       the page's --text
#   INK_SOFT  --fig-ink-soft  the page's --muted
#   EMPHASIS  --fig-accent    the page's --accent
#   SOFT_FILL --fig-soft      a quiet 5% tint of the ink (object boxes
#                             must read as containers, not highlights)
INK = "var(--fig-ink)"
INK_SOFT = "var(--fig-ink-soft)"
EMPHASIS = "var(--fig-accent)"
SOFT_FILL = "var(--fig-soft)"

# The concrete values behind those names, one set per colour scheme.
# public/site.css must define both (a contract checks it); the gestalt
# review pages and the social-card shell embed the light set through
# figure_token_css() so a figure never renders with undefined ink.
FIGURE_TOKENS_LIGHT = {
    "--fig-ink": "#521000",
    "--fig-ink-soft": "rgba(82, 16, 0, 0.7)",
    "--fig-accent": "#FF4801",
    "--fig-soft": "rgba(82, 16, 0, 0.05)",
}
FIGURE_TOKENS_DARK = {
    "--fig-ink": "#F3E7DC",
    "--fig-ink-soft": "rgba(243, 231, 220, 0.72)",
    "--fig-accent": "#FF6B2E",
    "--fig-soft": "rgba(243, 231, 220, 0.07)",
}


def figure_token_css(tokens: dict[str, str]) -> str:
    """CSS declarations for one token set, ready to drop inside a rule."""
    return " ".join(f"{name}: {value};" for name, value in tokens.items())


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
ARROW_CLOSED = 7
# Shortest arrow (shaft plus head) that still reads as an arrow. Below
# this an arrow is mostly head — the naming-decisions "case" chain drew
# 12-unit arrows that looked like stray wedges between boxes. Widen the
# gap between the boxes instead of shrinking the arrow.
ARROW_MIN = 20

NAME_W = 60
NAME_H = 24
OBJECT_W = 80
OBJECT_H = 32
CELL = 24
WORD_W = 44

# ─── Typography ────────────────────────────────────────────────────────
# Mono and sans follow the page's own stacks (public/site.css sets body
# text to system-ui and code to ui-monospace) so a figure's labels are
# set in the same faces as the code cell beside it. The site loads no
# web fonts, so asking for JetBrains Mono or Source Sans here only
# meant "whatever the OS falls back to". The italic serif stays: it is
# the one deliberate contrast, reserved for identifiers.
FONT_SERIF = "'Iowan Old Style', Charter, Georgia, serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
FONT_SANS = "system-ui, -apple-system, 'Segoe UI', sans-serif"
SIZE_BODY = 11
SIZE_MONO = 10
SIZE_SMALL = 9
SIZE_TAG = 8
BASELINE = 4  # add to box-center y to render text vertically centered

# ─── Text metrics ──────────────────────────────────────────────────────
# Single source of truth for character advance. Paint code uses
# MONO_ADVANCE to compute positions; the geometry contracts use
# BBOX_ADVANCE (deliberately conservative over-estimates) to detect
# clipping and collision. Keeping both here — instead of one in a paint
# comment and one in the test file — means a recalibration happens in
# one place and both consumers move together.
#
# MONO_ADVANCE is not a guess about the visitor's font: every mono run
# is emitted with textLength = len * MONO_ADVANCE * size and
# lengthAdjust="spacing", so the browser spaces the glyphs to exactly
# that advance whatever face the stack resolves to. Menlo and SF Mono
# advance 0.6em natively; Consolas advances 0.55em and gets 0.05em of
# letter-spacing. Dividers computed from MONO_ADVANCE therefore land on
# the right character on every platform.
MONO_ADVANCE = 0.6
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
    # Length of every closed arrow painted, for the minimum-length
    # contract (ARROW_MIN). Recorded here because the shaft is shortened
    # by the head in the emitted SVG, so the drawn geometry understates
    # the arrow the author asked for.
    _arrow_lengths: list[float] = field(default_factory=list)

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
        self._arrow_lengths.append(L)
        ux, uy = dx / L, dy / L
        end_x, end_y = x2 - ARROW_CLOSED * ux, y2 - ARROW_CLOSED * uy
        self._line(x1, y1, end_x, end_y, color=color, weight=weight)
        bx, by = x2 - ARROW_CLOSED * ux, y2 - ARROW_CLOSED * uy
        px, py = -uy * (ARROW_CLOSED / 2.5), ux * (ARROW_CLOSED / 2.5)
        self._add(f'<polygon points="{x2},{y2} {bx + px},{by + py} {bx - px},{by - py}" fill="{color}"/>')

    # ── text ──────────────────────────────────────────────────────────
    def _text(self, x, y, s, *, family, size, anchor, color, italic=False, tracking=None, length=None):
        attrs = [f'x="{x}"', f'y="{y}"', f'font-family="{family}"', f'font-size="{size}"',
                 f'fill="{color}"', f'text-anchor="{anchor}"']
        if italic:
            attrs.append('font-style="italic"')
        if tracking:
            attrs.append(f'letter-spacing="{tracking}"')
        if length:
            attrs.append(f'textLength="{length:g}" lengthAdjust="spacing"')
        self._add(f"<text {' '.join(attrs)}>{xml_escape(s)}</text>")

    def mono(self, x, y, s, *, anchor="middle", size=SIZE_MONO, color=INK):
        # Pin the run to MONO_ADVANCE per character so positions computed
        # from it (mono_divider, register ticks under a literal) hold on
        # every platform's monospace face.
        length = len(s) * MONO_ADVANCE * size if s else None
        self._text(x, y, s, family=FONT_MONO, size=size, anchor=anchor, color=color, length=length)

    def ident(self, x, y, s, *, anchor="middle", color=INK):
        self._text(x, y, s, family=FONT_SERIF, size=SIZE_BODY, anchor=anchor, color=color, italic=True)

    def label(self, x, y, s, *, anchor="start"):
        self._text(x, y, s, family=FONT_SANS, size=SIZE_SMALL, anchor=anchor, color=INK_SOFT)

    def tag(self, x, y, s, *, anchor="start"):
        self._text(x, y, s.upper(), family=FONT_SANS, size=SIZE_TAG,
                   anchor=anchor, color=INK_SOFT, tracking="0.5")

    # ── words ─────────────────────────────────────────────────────────
    def name_box(self, x, y, name, *, w=NAME_W):
        """Open rect with italic identifier. Returns right-edge midpoint.

        Pass a wider `w` when the running example's name is longer than
        the default box (MAX_RETRIES needs ~84); the figure should carry
        the lesson's own names, not placeholders chosen to fit the box.
        """
        self._add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{NAME_H}" fill="none" '
            f'stroke="{INK}" stroke-width="{W_STROKE}"/>'
        )
        self.ident(x + w / 2, y + NAME_H / 2 + BASELINE, name)
        return (x + w, y + NAME_H / 2)

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

    def register(self, x, y, w, *, divisions=None):
        """Hairline with regular ticks."""
        self.hairline(x, y, x + w, y)
        if divisions is None:
            return
        step = w / divisions
        for i in range(divisions + 1):
            self.tick(x + i * step, y)

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
    def bind(self, x, y, name, type_tag, value, *, object_w=OBJECT_W, gap=40, name_w=NAME_W):
        """name → object. The foundational picture.

        `gap` is the space between the two boxes; the arrow inside it is
        gap - 4 long, so keep gap >= ARROW_MIN + 4.
        """
        nx, ny = self.name_box(x, y + (OBJECT_H - NAME_H) / 2, name, w=name_w)
        ox, oy = self.object_box(nx + gap, y, type_tag, value, w=object_w)
        self.closed_arrow(nx + 2, ny, ox - 2, oy)
        return (x, y, nx + gap + object_w, y + OBJECT_H)

    def env(self, x, y, label, bindings, *, name_w=52, value_w=44, row_h=20, gap=6, pad=8, ghost=False):
        """An environment frame with its bindings — the Python Tutor picture.

        Each binding is (name, value): the name is an italic identifier,
        the value sits in a mono cell beside it. Pass value "" to leave
        the cell empty so the caller can arrow from it to a heap object.
        Draw the frame ghost when the call has returned; the cells stay
        solid because bindings can outlive their frame (that is what a
        closure is). Returns (right_x, bottom_y, anchors) where
        anchors[i] is the right-edge midpoint of binding i's value cell.
        """
        w = pad + name_w + value_w + pad
        h = pad + len(bindings) * (row_h + gap) - gap + pad
        self.frame(x, y, w, h, label=label, ghost=ghost)
        anchors = []
        for i, (name, value) in enumerate(bindings):
            ry = y + pad + i * (row_h + gap)
            self.ident(x + pad + name_w / 2, ry + row_h / 2 + BASELINE, name)
            vx = x + pad + name_w
            self.cell(vx, ry, value, w=value_w, h=row_h)
            anchors.append((vx + value_w, ry + row_h / 2))
        return (x + w, y + h, anchors)

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
        pad_top, pad_x, pad_bottom = PAD_TOP, PAD_X, PAD_BOTTOM
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
    caption: str = ""
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
        # The production caption is part of what reviewers must judge:
        # a caption that asserts something the figure does not draw is a
        # shipped defect, so the gestalt shows the exact figcaption text.
        caption_html = (
            f'  <p class="caption">{xml_escape(self.caption)}</p>\n' if self.caption else ""
        )
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
            f"{caption_html}"
            f"{score_html}"
            f"{note_html}"
            f"</div>"
        )
