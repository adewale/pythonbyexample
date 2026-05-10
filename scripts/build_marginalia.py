#!/usr/bin/env python3
"""Generate public/marginalia-gestalt.html from declarative card descriptions.

Every figure composes WORDS and PHRASES from marginalia_grammar.Canvas. No card
draws raw SVG. Drift is impossible because metrics live in the grammar module.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from marginalia_grammar import (  # noqa: E402  (sys.path set above)
    BASELINE,
    CELL,
    EMPHASIS,
    GAP_L,
    GAP_S,
    INK,
    INK_SOFT,
    NAME_H,
    NAME_W,
    OBJECT_H,
    OBJECT_W,
    SOFT_FILL,
    TICK_LEN,
    Canvas,
    Card,
)

OUT = ROOT / "public" / "prototyping" / "marginalia-gestalt.html"


# ─── Journeys ──────────────────────────────────────────────────────────


def j_runtime(c: Canvas) -> None:
    c.bind(20, 36, "x", "int", "42")


def j_streams(c: Canvas) -> None:
    c.cells(20, 30, ["a", "b", "c", "d"])
    c.caret(20 + CELL / 2, 30)
    c.closed_arrow(120, 42, 198, 42)
    c.label(160, 36, "next() · next() · next()", anchor="middle")
    c.object_box(204, 30, "", "consumer", w=92, h=24)


def j_shapes(c: Canvas) -> None:
    pairs = [("list", "[a,b,c]"), ("tuple", "(a,b,c)"), ("dict", "{k:v}"), ("set", "{a,b}")]
    for i, (tag, val) in enumerate(pairs):
        c.object_box(16 + i * 76, 32, tag, val, w=64, h=30)


def j_interfaces(c: Canvas) -> None:
    c.frame(20, 24, 78, 56, label="function")
    c.mono(59, 56, "def f()")
    c.frame(116, 24, 88, 56, label="class")
    c.mono(160, 50, "state +")
    c.mono(160, 64, "methods")
    c.frame(222, 24, 78, 56, label="protocol")
    c.mono(261, 56, "shape")


def j_types(c: Canvas) -> None:
    c.mono(20, 50, "def f(x: int, y: str) -> bool", anchor="start")
    c.dashed(60, 38, 76, 38)
    c.dashed(96, 38, 116, 38)
    c.dashed(140, 38, 184, 38)
    c.label(160, 28, "annotations describe; runtime accepts any object", anchor="middle")


def j_reliability(c: Canvas) -> None:
    ys = [(22, "try"), (42, "except"), (62, "else"), (82, "finally")]
    path = [(40, 22), (110, 22), (130, 62), (210, 62), (230, 82), (290, 82)]
    c.lanes(ys, x0=40, x1=300, path=path)


JOURNEYS = [
    Card("runtime", "Runtime", "Journey", "01", j_runtime, is_journey=True,
         note="names bind to objects"),
    Card("streams", "Streams", "Journey", "02", j_streams, is_journey=True,
         note="iteration is a value stream"),
    Card("shapes", "Shapes", "Journey", "03", j_shapes, is_journey=True,
         note="container choice answers a question"),
    Card("interfaces", "Interfaces", "Journey", "04", j_interfaces, is_journey=True,
         note="behavior packaged at increasing abstraction"),
    Card("types", "Types", "Journey", "05", j_types, is_journey=True,
         note="static description of runtime objects"),
    Card("reliability", "Reliability", "Journey", "06", j_reliability, is_journey=True,
         note="program boundaries — failure, cleanup, scope"),
]


# ─── Examples (manifest order) ─────────────────────────────────────────


def e_hello_world(c: Canvas) -> None:
    c.object_box(20, 36, "", 'print("…")', w=90, soft=False)
    c.closed_arrow(112, 52, 188, 52)
    c.label(150, 46, "stdout", anchor="middle")
    c.object_box(190, 36, "", "hello world", w=110)


def e_values(c: Canvas) -> None:
    c.object_box(20, 32, "int", "42", w=60)
    c.object_box(96, 32, "str", '"hi"', w=80)
    c.object_box(192, 32, "list", "[1,2,3]", w=100)


def e_numbers(c: Canvas) -> None:
    c.tag(20, 22, "int · unbounded")
    c.register(20, 38, 280, divisions=8)
    c.tag(20, 64, "float · representable spacing widens")
    c.register(20, 78, 280)
    for x in (28, 50, 80, 122, 152, 162, 170, 182, 210, 250, 292):
        c.tick(x, 78)
    c.dot(162, 78, emphasis=True)


def e_booleans(c: Canvas) -> None:
    c.tag(160, 22, "and", anchor="middle")
    c.label(140, 36, "T", anchor="middle")
    c.label(180, 36, "F", anchor="middle")
    c.label(118, 56, "T", anchor="end")
    c.label(118, 76, "F", anchor="end")
    c.cell(120, 40, "T", w=40, h=18, soft=True)
    c.cell(160, 40, "F", w=40, h=18)
    c.cell(120, 58, "F", w=40, h=18)
    c.cell(160, 58, "F", w=40, h=18)


def e_operators(c: Canvas) -> None:
    c.node(160, 26, "*", r=12)
    c.node(120, 62, "+", r=12)
    c.node(220, 62, "4", r=10)
    c.node(96, 92, "2", r=10)
    c.node(144, 92, "3", r=10)
    c.connect(160, 26, 12, 120, 62, 12)
    c.connect(160, 26, 12, 220, 62, 10)
    c.connect(120, 62, 12, 96, 92, 10)
    c.connect(120, 62, 12, 144, 92, 10)


def e_none(c: Canvas) -> None:
    for i, n in enumerate("abc"):
        c.name_box(20, 18 + i * 30, n)
    for y in (30, 60, 90):
        c.closed_arrow(80, y, 200, 60, emphasis=False)
    c.object_box(202, 44, "NoneType", "None", w=80)


def e_variables(c: Canvas) -> None:
    c.bind(20, 36, "x", "int", "42")
    c.label(220, 88, "id 0x…a0", anchor="middle")


def e_constants(c: Canvas) -> None:
    c.bind(20, 36, "MAX_SIZE", "int", "100", object_w=60, gap=24)


def e_truthiness(c: Canvas) -> None:
    c.tag(20, 28, "falsy")
    items = ["0", "0.0", '""', "[]", "{}", "None", "False"]
    widths = [30, 36, 32, 32, 32, 46, 50]
    x = 20
    for v, w in zip(items, widths):
        c.cell(x, 36, v, w=w, h=26)
        x += w


def e_equality(c: Canvas) -> None:
    c.tag(80, 14, "a is b · a == b", anchor="middle")
    c.name_box(20, 24, "a")
    c.name_box(20, 52, "b")
    c.closed_arrow(80, 36, 138, 50, emphasis=False)
    c.closed_arrow(80, 64, 138, 50, emphasis=False)
    c.object_box(140, 38, "list", "[1,2]", w=44, h=26)
    c.tag(240, 14, "a == b only", anchor="middle")
    c.name_box(180, 24, "a")
    c.name_box(180, 52, "b")
    c.closed_arrow(240, 36, 280, 36, emphasis=False)
    c.closed_arrow(240, 64, 280, 64, emphasis=False)
    c.object_box(280, 24, "", "[1,2]", w=40, h=24)
    c.object_box(280, 52, "", "[1,2]", w=40, h=24)


def e_mutability(c: Canvas) -> None:
    states = [
        ("assign", "[3,1,4]", "id 0x…a0"),
        ("mutate · same id", "[3,1,4,1]", "id 0x…a0"),
        ("rebind · new id", "[3,1,4,1]", "id 0x…b7"),
    ]
    for i, (tag, val, idnote) in enumerate(states):
        y = 14 + i * 60
        c.tag(20, y, tag)
        c.bind(20, y + 8, "xs", "list", val, object_w=80, gap=20)
        c.label(70, y + 52, idnote)


def e_strings(c: Canvas) -> None:
    c.tag(20, 22, "codepoints")
    for i, ch in enumerate("café"):
        c.cell(20 + i * 40, 28, ch, w=40, h=28)
    c.tag(20, 74, "utf-8 bytes")
    widths = [40, 40, 40, 20, 20]
    bytes_ = ["63", "61", "66", "c3", "a9"]
    x = 20
    for w, b in zip(widths, bytes_):
        c.cell(x, 78, b, w=w, h=14)
        x += w


def e_string_formatting(c: Canvas) -> None:
    c.tag(20, 22, "format spec")
    stations = [("align", 36), ("sign", 30), ("#", 22), ("width", 40), (",", 22), (".prec", 44), ("type", 32)]
    x = 20
    for label, w in stations:
        c.cell(x, 38, label, w=w, h=18)
        x += w + 2
    c.label(20, 76, "{:>6,.2f}")


def e_conditionals(c: Canvas) -> None:
    c.node(160, 38, "?", r=18)
    c.closed_arrow(146, 50, 70, 84, emphasis=False)
    c.closed_arrow(174, 50, 250, 84, emphasis=False)
    c.label(70, 96, "if", anchor="middle")
    c.label(250, 96, "else", anchor="middle")


def e_assignment_expressions(c: Canvas) -> None:
    c.mono(20, 40, "if (n := len(xs)) > 10:", anchor="start")
    c.dashed(50, 44, 102, 44)
    c.label(76, 58, "walrus", anchor="middle")
    c.name_box(40, 66, "n")
    c.closed_arrow(100, 78, 158, 78)
    c.object_box(160, 66, "int", "value", w=60, h=24)


def e_for_loops(c: Canvas) -> None:
    items = list("abcd")
    for i in range(4):
        y = 8 + i * 32
        c.cells(20, y, items)
        c.caret(20 + i * CELL + CELL / 2, y)
        suffix = " — last" if i == 3 else ""
        c.label(124, y + 16, f"next(){suffix}")


def e_break_continue(c: Canvas) -> None:
    c.frame(60, 22, 200, 64, label="loop body")
    c.dashed(160, 22, 160, 86)
    c.closed_arrow(110, 60, 110, 18, emphasis=True)
    c.label(110, 14, "continue", anchor="middle")
    c.closed_arrow(220, 54, 290, 54, emphasis=True)
    c.label(254, 50, "break", anchor="middle")


def e_loop_else(c: Canvas) -> None:
    c.frame(20, 32, 100, 44, label="loop")
    c.closed_arrow(120, 40, 200, 22, emphasis=True)
    c.label(140, 18, "fell through")
    c.object_box(212, 12, "", "else: …", w=80, h=20)
    c.closed_arrow(120, 64, 200, 84, emphasis=False)
    c.label(140, 100, "broke — else skipped")


def e_iterating_over_iterables(c: Canvas) -> None:
    c.object_box(20, 36, "iterable", "[a,b,c]", w=70, h=30, soft=True)
    c.dashed(90, 51, 124, 51)
    c.label(108, 46, "iter()", anchor="middle")
    c.object_box(126, 36, "iterator", "", w=70, h=30, soft=False)
    c.closed_arrow(196, 51, 230, 51)
    c.label(214, 46, "next()", anchor="middle")
    c.object_box(232, 36, "", "value …", w=70, h=30, soft=True)


def e_iterators(c: Canvas) -> None:
    c.node(60, 50, "idle", r=20)
    c.node(160, 50, "next()", r=24)
    c.node(252, 50, "done", r=22, ghost=True)
    c.connect(60, 50, 20, 160, 50, 24, kind="emphasis", offset=2)
    c.connect(160, 50, 24, 252, 50, 22, kind="emphasis", offset=2)
    c.label(110, 44, "iter()", anchor="middle")
    c.label(206, 44, "stop", anchor="middle")


def e_match_statements(c: Canvas) -> None:
    c.mono(20, 22, "match value:", anchor="start")
    cases = ["case 0:", "case [x, *_]:", "case _:"]
    for i, txt in enumerate(cases):
        y = 32 + i * 22
        c.cell(40, y, "", w=180, h=18)
        c.mono(50, y + 12, txt, anchor="start", size=9)
    c.dashed(238, 36, 238, 100)
    c.dot(238, 64, emphasis=True)
    c.closed_arrow(238, 92, 238, 102, emphasis=True)
    c.label(254, 70, "first match")


def e_advanced_match(c: Canvas) -> None:
    rows = [("capture", "[x, y]"), ("alternative", "P() | Q()"), ("guard", "[x] if x > 0"), ("class", "Point(x=0, y=_)")]
    for i, (tag, body) in enumerate(rows):
        y = 14 + i * 26
        c.tag(20, y, tag)
        soft = (tag == "class")
        c.cell(80, y - 2, body, w=180, h=18, soft=soft)


def e_while_loops(c: Canvas) -> None:
    c.node(160, 38, "?", r=16)
    c.closed_arrow(176, 38, 240, 38)
    c.cell(242, 26, "body", w=60, h=24)
    c.dashed(272, 50, 272, 78)
    c.dashed(272, 78, 144, 78)
    c.dashed(144, 78, 144, 54)
    c.closed_arrow(144, 38, 96, 38, emphasis=False)
    c.label(96, 30, "exit", anchor="end")


def e_lists(c: Canvas) -> None:
    c.tag(20, 22, "mutable sequence")
    items = ["3", "1", "4", ""]
    c.cells(20, 30, items)
    c.cell(116, 30, "+1", ghost=True)
    c.closed_arrow(150, 42, 200, 42)
    c.label(206, 46, ".append", anchor="start")


def e_tuples(c: Canvas) -> None:
    c.tag(20, 22, "immutable sequence")
    c.cell(20, 30, "", w=160, h=28)
    c.hairline(60, 30, 60, 58)
    c.hairline(100, 30, 100, 58)
    c.hairline(140, 30, 140, 58)
    for i, v in enumerate("3141"):
        c.mono(40 + i * 40, 48, v)


def e_unpacking(c: Canvas) -> None:
    items = ["1", "2", "3", "4", "5"]
    for i, v in enumerate(items):
        c.cell(20 + i * 30, 20, v, w=30, h=22)
    c.cell(20, 78, "a", w=30, h=22)
    c.cell(50, 78, "*rest", w=90, h=22, ghost=True)
    c.cell(140, 78, "b", w=30, h=22)
    c.dashed(35, 42, 35, 78)
    c.dashed(65, 42, 95, 78)
    c.dashed(95, 42, 95, 78)
    c.dashed(125, 42, 95, 78)
    c.dashed(155, 42, 155, 78)


def e_dicts(c: Canvas) -> None:
    c.tag(20, 22, "hash & mask → bucket")
    rows = [("0", '"a" → 1'), ("1", '"b" → 2'), ("2", '"c" → 3')]
    for i, (idx, body) in enumerate(rows):
        y = 30 + i * 24
        c.label(14, y + 16, idx, anchor="end")
        c.cell(20, y, body, w=80, h=24)
    c.closed_arrow(102, 66, 142, 66)
    c.cell(144, 54, '"d" → 4', w=80, h=24, soft=True)
    c.label(232, 70, "collision")


def e_sets(c: Canvas) -> None:
    c.tag(20, 22, "hash buckets · keys only")
    for i, k in enumerate("abc"):
        c.cell(20, 30 + i * 24, k, w=60, h=24)
    c.closed_arrow(82, 66, 158, 66)
    c.label(122, 60, "x in s", anchor="middle")
    c.cell(160, 54, "O(1)", w=60, h=24)
    c.label(230, 56, "no order")
    c.label(230, 70, "no duplicates")


def e_slices(c: Canvas) -> None:
    items = list("abcde")
    for i, v in enumerate(items):
        c.cell(20 + i * 36, 36, v, w=36, h=24)
    for i in range(5):
        c.label(38 + i * 36, 74, str(i), anchor="middle")
    c.register(20, 86, 180, divisions=5)
    for i in range(6):
        c.label(20 + i * 36, 100, str(i), anchor="middle")
    c.dashed(56, 30, 56, 36)
    c.dashed(164, 30, 164, 36)
    c.label(110, 22, "[1:4]", anchor="middle")


def e_comprehensions(c: Canvas) -> None:
    c.cell(20, 22, "[x*2 for x in xs if x > 0]", w=280, h=22, soft=True)
    c.cell(20, 56, "out = []", w=280, h=14, ghost=True)
    c.cell(20, 70, "for x in xs:", w=280, h=14, ghost=True)
    c.cell(20, 84, "    if x > 0: out.append(x*2)", w=280, h=14, ghost=True)


def e_comprehension_patterns(c: Canvas) -> None:
    boxes = [("source", "xs · ys"), ("filter", "if y>0"), ("map", "x*y")]
    x = 20
    for i, (tag, body) in enumerate(boxes):
        c.cell(x, 36, body, w=70, h=30)
        c.tag(x, 30, tag)
        if i < 2:
            c.closed_arrow(x + 72, 51, x + 90, 51)
        x += 90


def e_sorting(c: Canvas) -> None:
    c.tag(60, 16, "input", anchor="middle")
    c.tag(240, 16, "stable sort", anchor="middle")
    inputs = ["2 · Ada", "1 · Bo", "2 · Eve", "1 · Cy"]
    outputs = ["1 · Bo", "1 · Cy", "2 · Ada", "2 · Eve"]
    for i, (a, b) in enumerate(zip(inputs, outputs)):
        c.cell(20, 22 + i * 22, a, w=80, h=20)
        c.cell(200, 22 + i * 22, b, w=80, h=20)
    c.dashed(100, 54, 200, 32)
    c.dashed(100, 98, 200, 54)
    c.dashed(100, 32, 200, 76)
    c.dashed(100, 76, 200, 98)


def e_functions(c: Canvas) -> None:
    c.closed_arrow(20, 50, 80, 50, emphasis=False)
    c.label(50, 42, "args", anchor="middle")
    c.frame(82, 30, 120, 40, label="def f(...)")
    c.closed_arrow(202, 50, 262, 50, emphasis=False)
    c.label(232, 42, "return", anchor="middle")


def e_keyword_only(c: Canvas) -> None:
    c.mono(20, 40, "def f(a, b, *, c, d): …", anchor="start")
    c.dashed(105, 44, 105, 70)
    c.label(60, 80, "positional or kw", anchor="middle")
    c.label(160, 80, "keyword only", anchor="middle")


def e_positional_only(c: Canvas) -> None:
    c.mono(20, 40, "def f(a, b, /, c, d): …", anchor="start")
    c.dashed(112, 44, 112, 70)
    c.label(60, 80, "positional only", anchor="middle")
    c.label(180, 80, "positional or kw", anchor="middle")


def e_args_kwargs(c: Canvas) -> None:
    c.mono(20, 40, "def f(*args, **kwargs): …", anchor="start")
    c.label(80, 70, "extra positionals", anchor="middle")
    c.label(80, 86, "tuple", anchor="middle")
    c.label(180, 70, "extra keywords", anchor="middle")
    c.label(180, 86, "dict", anchor="middle")


def e_multiple_return(c: Canvas) -> None:
    c.frame(20, 32, 100, 32, label="def f()")
    c.closed_arrow(120, 48, 158, 48)
    c.object_box(160, 36, "tuple", "(a, b)", w=80, h=24)
    c.dashed(200, 60, 200, 80)
    c.cell(180, 84, "x", w=22, h=18)
    c.cell(206, 84, "y", w=22, h=18)


def e_closures(c: Canvas) -> None:
    c.frame(20, 22, 280, 80, label="outer()")
    c.object_box(40, 50, "cell", "n=0", w=50, h=22)
    c.frame(102, 44, 180, 56, label="inner()")
    c.label(190, 80, "uses cell", anchor="middle")
    c.closed_arrow(116, 78, 92, 64)


def e_scope_legb(c: Canvas) -> None:
    c.frame(14, 14, 296, 92, label="B · built-in")
    c.frame(34, 30, 262, 72, label="G · global")
    c.frame(58, 46, 226, 52, label="E · enclosing")
    c.frame(86, 62, 170, 32, label="L · local")
    c.dashed(170, 90, 170, 110)


def e_recursion(c: Canvas) -> None:
    for i in range(4):
        c.cell(60, 14 + i * 20, f"factorial({3 - i}){' ← base' if i == 3 else ''}", w=200, h=20)
    c.dashed(272, 90, 272, 18)
    c.closed_arrow(272, 30, 272, 18, emphasis=True)


def e_lambdas(c: Canvas) -> None:
    c.cell(60, 36, "lambda x: x + 1", w=200, h=32, soft=True)
    c.dashed(100, 68, 100, 78)
    c.dashed(220, 68, 220, 78)
    c.label(100, 92, "params", anchor="middle")
    c.label(220, 92, "expression", anchor="middle")


def e_generators(c: Canvas) -> None:
    c.tag(20, 22, "paused between yields · resumed by next()")
    c.ribbon(20, 30, 280, h=30, gates=[84, 156, 228], soft_segments=[(20, 84), (156, 228)])
    c.mono(52, 50, "…work…")
    c.mono(120, 50, "yield")
    c.mono(192, 50, "…work…")
    c.mono(264, 50, "yield")


def e_yield_from(c: Canvas) -> None:
    c.tag(20, 22, "outer")
    c.ribbon(20, 30, 280, h=24, gates=[120, 200])
    c.mono(160, 46, "yield from inner()")
    c.tag(120, 70, "inner")
    c.ribbon(120, 78, 80, h=28, gates=[148, 172])
    c.dashed(160, 78, 160, 54)
    c.label(240, 96, "delegated")


def e_generator_expressions(c: Canvas) -> None:
    c.mono(20, 46, "(", anchor="start")
    c.cell(30, 36, "source", w=60, h=20)
    c.closed_arrow(90, 46, 108, 46)
    c.cell(108, 36, "filter", w=60, h=20)
    c.closed_arrow(168, 46, 186, 46)
    c.cell(186, 36, "map", w=60, h=20)
    c.mono(252, 46, ")", anchor="start")
    c.label(160, 84, "lazy stream — no list materialised", anchor="middle")


def e_itertools(c: Canvas) -> None:
    c.tag(20, 22, "chain")
    c.cell(20, 28, "a · b", w=80, h=14)
    c.cell(100, 28, "c · d", w=80, h=14)
    c.tag(20, 60, "cycle")
    c.cell(20, 66, "a · b · c", w=100, h=14)
    c.dashed(120, 73, 140, 73)
    c.tag(20, 98, "islice")
    c.cell(20, 104, "", w=180, h=14, ghost=True)
    c.cell(60, 104, "window", w=60, h=14)


def e_decorators(c: Canvas) -> None:
    c.tag(20, 18, "before")
    c.bind(20, 26, "f", "fn", "f₀ body", object_w=80, gap=20)
    c.tag(20, 78, "after @dec")
    c.name_box(20, 90, "f")
    c.closed_arrow(80, 102, 110, 102)
    c.cell(112, 88, "wrapper", w=80, h=28)
    c.object_box(196, 90, "cell", "f₀", w=40, h=24)
    c.dashed(192, 102, 196, 102)


def e_classes(c: Canvas) -> None:
    c.dot(50, 50, emphasis=False)
    c.label(50, 78, "instance", anchor="middle")
    c.closed_arrow(56, 50, 118, 50, emphasis=False)
    c.frame(120, 32, 60, 36, label="class")
    c.mono(150, 54, "Class")
    c.closed_arrow(180, 50, 232, 50, emphasis=False)
    c.frame(234, 32, 60, 36, label="type")
    c.mono(264, 54, "type")


def e_inheritance(c: Canvas) -> None:
    c.frame(140, 6, 40, 22, ghost=True)
    c.mono(160, 22, "A")
    c.ghost(160, 28, 100, 50)
    c.ghost(160, 28, 220, 50)
    c.frame(80, 50, 40, 22, ghost=True)
    c.mono(100, 66, "B")
    c.frame(200, 50, 40, 22, ghost=True)
    c.mono(220, 66, "C")
    c.tag(20, 96, "MRO")
    chain = ["D", "B", "C", "A", "object"]
    widths = [40, 40, 40, 40, 60]
    x = 20
    for v, w in zip(chain, widths):
        c.cell(x, 102, v, w=w, h=22)
        x += w


def e_dataclasses(c: Canvas) -> None:
    c.tag(20, 22, "declaration")
    fields = [("name", "str"), ("age", "int"), ("tags", "list")]
    for i, (n, t) in enumerate(fields):
        c.cell(20, 30 + i * 20, f"{n} : {t}", w=120, h=20)
    c.closed_arrow(140, 60, 178, 60)
    c.object_box(180, 44, "", "__init__(name, age, tags)", w=124, h=32)


def e_properties(c: Canvas) -> None:
    c.cell(20, 40, "obj.x", w=80, h=32)
    c.closed_arrow(102, 50, 158, 30)
    c.object_box(160, 14, "", "fget / fset", w=120, h=26)
    c.dashed(102, 60, 158, 86)
    c.cell(160, 74, "__dict__", w=120, h=26, ghost=True)


def e_special_methods(c: Canvas) -> None:
    c.mono(60, 44, "a + b")
    c.closed_arrow(100, 40, 168, 40)
    c.label(135, 32, "dispatches", anchor="middle")
    c.object_box(170, 28, "", "a.__add__(b)", w=130, h=26)


def e_metaclasses(c: Canvas) -> None:
    c.dot(40, 50, emphasis=False)
    c.closed_arrow(46, 50, 108, 50, emphasis=False)
    c.frame(110, 34, 60, 32, label="class")
    c.mono(140, 54, "Class")
    c.closed_arrow(170, 50, 226, 50, emphasis=False)
    c.frame(228, 30, 80, 40, label="metaclass")
    c.mono(268, 50, "Metaclass")


def e_context_managers(c: Canvas) -> None:
    c.node(40, 60, "in", r=14)
    c.closed_arrow(54, 60, 100, 60, emphasis=False)
    c.cell(100, 44, "body", w=120, h=32)
    c.closed_arrow(220, 60, 266, 60)
    c.node(282, 60, "out", r=14)
    c.dashed(160, 76, 268, 60)


def e_delete_statements(c: Canvas) -> None:
    c.tag(20, 18, "before")
    c.bind(20, 26, "x", "list", "[1,2,3]", object_w=80, gap=20)
    c.tag(20, 78, "after del x")
    c.name_box(20, 86, "x")
    c.closed_arrow(80, 98, 118, 98, emphasis=False)
    c.object_box(120, 82, "list", "[1,2,3]", w=80, h=32)


def e_exceptions(c: Canvas) -> None:
    ys = [(22, "try"), (46, "except"), (70, "else"), (94, "finally")]
    path = [(50, 22), (120, 22), (140, 70), (200, 70), (220, 94), (290, 94)]
    c.lanes(ys, x0=40, x1=300, path=path)


def e_assertions(c: Canvas) -> None:
    c.mono(20, 40, "assert cond, msg", anchor="start")
    c.dashed(120, 46, 120, 64)
    c.cell(60, 68, "true · pass", w=70, h=22)
    c.cell(140, 68, "false · AssertionError", w=140, h=22, soft=True)


def e_exception_chaining(c: Canvas) -> None:
    c.cell(20, 36, "ValueError", w=100, h=32)
    c.closed_arrow(120, 44, 200, 44)
    c.label(160, 36, "__cause__", anchor="middle")
    c.dashed(120, 60, 200, 60)
    c.label(160, 78, "__context__", anchor="middle")
    c.cell(202, 36, "RuntimeError", w=100, h=32)


def e_exception_groups(c: Canvas) -> None:
    c.tag(60, 16, "before except*", anchor="middle")
    c.dot(60, 32)
    for x in (30, 50, 70, 90):
        c.ghost(60, 38, x, 60)
    c.dot(30, 64); c.dot(50, 64, emphasis=True); c.dot(70, 64); c.dot(90, 64, emphasis=True)
    c.closed_arrow(120, 50, 180, 50)
    c.label(150, 44, "except*", anchor="middle")
    c.tag(240, 16, "after", anchor="middle")
    c.dot(240, 32)
    c.ghost(240, 38, 220, 60)
    c.ghost(240, 38, 260, 60)
    c.dot(220, 64); c.dot(260, 64)


def e_modules(c: Canvas) -> None:
    c.tag(20, 22, "sys.path")
    paths = ["cwd", "site-packages", "stdlib", "…"]
    for i, p in enumerate(paths):
        c.cell(20, 28 + i * 20, p, w=120, h=20)
    c.closed_arrow(140, 58, 200, 58)
    c.label(170, 52, "first hit", anchor="middle")
    c.cell(202, 46, "mymod.py", w=100, h=24, soft=True)


def e_import_aliases(c: Canvas) -> None:
    c.mono(20, 28, "import numpy as np", anchor="start")
    c.bind(20, 50, "np", "module", "numpy", object_w=120, gap=20)


def e_type_hints(c: Canvas) -> None:
    c.mono(20, 56, "def f(x: int, y: str) -> bool: …", anchor="start")
    c.dashed(72, 60, 92, 60)
    c.dashed(112, 60, 132, 60)
    c.dashed(160, 60, 196, 60)


def e_protocols(c: Canvas) -> None:
    c.tag(60, 14, "object", anchor="middle")
    c.frame(20, 20, 100, 80)
    for i, m in enumerate(["read()", "write()", "close()", "other()"]):
        c.mono(70, 38 + i * 18, m)
    c.closed_arrow(120, 60, 180, 60, emphasis=False)
    c.label(150, 54, "structural ✓", anchor="middle")
    c.tag(240, 14, "protocol", anchor="middle")
    c.frame(200, 20, 100, 80, ghost=True)
    c.mono(250, 44, "read()")
    c.mono(250, 62, "close()")


def e_enums(c: Canvas) -> None:
    c.frame(20, 24, 280, 60, ghost=True, label="Color · closed set")
    for i, m in enumerate(["RED", "GREEN", "BLUE", "no more"]):
        c.cell(40 + i * 60, 38, m, w=50, h=32)


def e_regex(c: Canvas) -> None:
    c.tag(20, 22, "pattern")
    c.mono(20, 44, "^\\d{2}-\\d{2}$", anchor="start")
    c.tag(20, 70, "input")
    c.cell(20, 76, "", w=180, h=20)
    c.cell(40, 76, "12-34", w=120, h=20, soft=True)


def e_number_parsing(c: Canvas) -> None:
    c.node(40, 50, '"42"', r=16)
    c.closed_arrow(56, 50, 100, 50)
    c.label(78, 44, "int()", anchor="middle")
    c.node(120, 50, "42", r=16)
    c.closed_arrow(136, 50, 180, 24, emphasis=False)
    c.cell(180, 14, "ValueError", w=100, h=22, ghost=True)
    c.closed_arrow(136, 50, 180, 80)
    c.cell(180, 70, "int", w=100, h=22, soft=True)


def e_custom_exceptions(c: Canvas) -> None:
    chain = ["BaseException", "Exception", "ValueError", "MyDomainError"]
    for i, name in enumerate(chain):
        emph = (i == len(chain) - 1)
        c.cell(60, 14 + i * 26, name, w=200, h=22, soft=emph)


def e_json(c: Canvas) -> None:
    c.hairline(160, 14, 160, 122)
    c.tag(80, 14, "json", anchor="middle")
    c.tag(240, 14, "python", anchor="middle")
    rows = [("object", "dict"), ("array", "list"), ("string", "str"), ("number", "int / float"), ("true / false", "True / False"), ("null", "None")]
    for i, (a, b) in enumerate(rows):
        y = 36 + i * 16
        c.mono(20, y, a, anchor="start", size=10)
        c.mono(180, y, b, anchor="start", size=10)


def e_datetime(c: Canvas) -> None:
    c.register(20, 60, 280, divisions=7)
    c.dashed(160, 50, 160, 70)
    c.label(160, 44, "one instant", anchor="middle")
    c.node(80, 92, "−5h", r=14)
    c.dashed(80, 78, 160, 70)
    c.node(240, 92, "+0h", r=14)
    c.dashed(240, 78, 160, 70)


def e_async_await(c: Canvas) -> None:
    c.lane(34, x0=20, x1=300, label="loop")
    c.lane(74, x0=20, x1=300, label="coro")
    c.cell(40, 68, "", w=40, h=12)
    c.dashed(80, 74, 120, 34)
    c.cell(120, 28, "", w=60, h=12)
    c.dashed(180, 34, 220, 74)
    c.cell(220, 68, "", w=40, h=12)
    c.label(100, 22, "await", anchor="middle")
    c.label(200, 22, "resume", anchor="middle")


def e_async_iteration(c: Canvas) -> None:
    c.tag(20, 22, "async for · async with")
    c.ribbon(20, 30, 280, h=30, gates=[84, 156, 228])
    c.mono(50, 50, "…")
    c.mono(120, 50, "await yield")
    c.mono(192, 50, "…")
    c.mono(264, 50, "await yield")


EXAMPLES = [
    Card("hello-world", "Hello World", "Basics", 1, e_hello_world),
    Card("values", "Values", "Basics", 2, e_values, note="every value is an object with a type"),
    Card("numbers", "Numbers", "Basics", 3, e_numbers),
    Card("booleans", "Booleans", "Basics", 4, e_booleans, height=90),
    Card("operators-and-literals", "Operators and Literals", "Basics", 5, e_operators, height=130),
    Card("none", "None", "Basics", 6, e_none, height=130, note="one shared singleton"),
    Card("variables", "Variables", "Basics", 7, e_variables, note="names bind to objects"),
    Card("constants", "Constants", "Basics", 8, e_constants, note="UPPER_CASE — convention, not enforcement"),
    Card("truthiness", "Truthiness", "Basics", 9, e_truthiness),
    Card("equality-and-identity", "Equality and Identity", "Basics", 10, e_equality, height=110, note="same object · or two equal objects"),
    Card("mutability", "Mutability", "Basics", 11, e_mutability, height=200),
    Card("strings", "Strings", "Basics", 12, e_strings),
    Card("string-formatting", "String Formatting", "Basics", 13, e_string_formatting, height=100),
    Card("conditionals", "Conditionals", "Control Flow", 14, e_conditionals, height=110),
    Card("assignment-expressions", "Assignment Expressions", "Control Flow", 15, e_assignment_expressions, height=110),
    Card("for-loops", "For Loops", "Control Flow", 16, e_for_loops, height=160),
    Card("break-and-continue", "Break and Continue", "Control Flow", 17, e_break_continue, height=110),
    Card("loop-else", "Loop Else", "Control Flow", 18, e_loop_else, height=120),
    Card("iterating-over-iterables", "Iterating over Iterables", "Control Flow", 19, e_iterating_over_iterables),
    Card("iterators", "Iterators", "Control Flow", 20, e_iterators, height=110),
    Card("match-statements", "Match Statements", "Control Flow", 21, e_match_statements, height=130),
    Card("advanced-match-patterns", "Advanced Match Patterns", "Control Flow", 22, e_advanced_match, height=130),
    Card("while-loops", "While Loops", "Control Flow", 23, e_while_loops, height=110),
    Card("lists", "Lists", "Collections", 24, e_lists),
    Card("tuples", "Tuples", "Collections", 25, e_tuples),
    Card("unpacking", "Unpacking", "Collections", 26, e_unpacking, height=110),
    Card("dicts", "Dictionaries", "Collections", 27, e_dicts, height=110),
    Card("sets", "Sets", "Collections", 28, e_sets, height=110),
    Card("slices", "Slices", "Collections", 29, e_slices, height=110),
    Card("comprehensions", "Comprehensions", "Collections", 30, e_comprehensions, height=110),
    Card("comprehension-patterns", "Comprehension Patterns", "Collections", 31, e_comprehension_patterns, note="nested clauses compose left to right"),
    Card("sorting", "Sorting", "Collections", 32, e_sorting, height=130, note="equal keys keep original order"),
    Card("functions", "Functions", "Functions", 33, e_functions, note="named behavior with a stable interface"),
    Card("keyword-only-arguments", "Keyword-only Arguments", "Functions", 34, e_keyword_only, height=100),
    Card("positional-only-parameters", "Positional-only Parameters", "Functions", 35, e_positional_only, height=100),
    Card("args-and-kwargs", "Args and Kwargs", "Functions", 36, e_args_kwargs, height=100),
    Card("multiple-return-values", "Multiple Return Values", "Functions", 37, e_multiple_return),
    Card("closures", "Closures", "Functions", 38, e_closures, height=120),
    Card("scope-global-nonlocal", "Global and Nonlocal", "Functions", 39, e_scope_legb, height=130),
    Card("recursion", "Recursion", "Functions", 40, e_recursion, height=120),
    Card("lambdas", "Lambdas", "Functions", 41, e_lambdas, height=110),
    Card("generators", "Generators", "Iteration", 42, e_generators, note="function body as a timeline"),
    Card("yield-from", "Yield From", "Iteration", 43, e_yield_from, height=120),
    Card("generator-expressions", "Generator Expressions", "Iteration", 44, e_generator_expressions),
    Card("itertools", "Itertools", "Iteration", 45, e_itertools, height=130),
    Card("decorators", "Decorators", "Functions", 46, e_decorators, height=130),
    Card("classes", "Classes", "Classes", 47, e_classes, height=110),
    Card("inheritance-and-super", "Inheritance and Super", "Classes", 48, e_inheritance, height=130),
    Card("dataclasses", "Dataclasses", "Classes", 49, e_dataclasses, height=120),
    Card("properties", "Properties", "Classes", 50, e_properties, height=120),
    Card("special-methods", "Special Methods", "Data Model", 51, e_special_methods),
    Card("metaclasses", "Metaclasses", "Classes", 52, e_metaclasses, height=110),
    Card("context-managers", "Context Managers", "Data Model", 53, e_context_managers, height=110),
    Card("delete-statements", "Delete Statements", "Data Model", 54, e_delete_statements, height=130),
    Card("exceptions", "Exceptions", "Errors", 55, e_exceptions, height=130, note="no raise → try → else → finally"),
    Card("assertions", "Assertions", "Errors", 56, e_assertions, height=110),
    Card("exception-chaining", "Exception Chaining", "Errors", 57, e_exception_chaining, height=110),
    Card("exception-groups", "Exception Groups", "Errors", 58, e_exception_groups, height=110, note="matched leaves removed; survivors regrouped"),
    Card("modules", "Modules", "Modules", 59, e_modules, height=130),
    Card("import-aliases", "Import Aliases", "Modules", 60, e_import_aliases, height=110),
    Card("type-hints", "Type Hints", "Types", 61, e_type_hints, height=100),
    Card("protocols", "Protocols", "Types", 62, e_protocols, height=120, note="duck — required methods present"),
    Card("enums", "Enums", "Types", 63, e_enums, height=110),
    Card("regular-expressions", "Regular Expressions", "Text", 64, e_regex, height=110),
    Card("number-parsing", "Number Parsing", "Standard Library", 65, e_number_parsing, height=110),
    Card("custom-exceptions", "Custom Exceptions", "Errors", 66, e_custom_exceptions, height=130),
    Card("json", "JSON", "Standard Library", 67, e_json, height=130),
    Card("datetime", "Dates and Times", "Standard Library", 68, e_datetime, height=120),
    Card("async-await", "Async Await", "Async", 69, e_async_await, height=110),
    Card("async-iteration-and-context", "Async Iteration and Context", "Async", 70, e_async_iteration),
]


# ─── Page scaffold ─────────────────────────────────────────────────────


HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Marginalia gestalt — Python By Example</title>
<style>
  :root {
    /* Aligned with public/site.css tokens. */
    --paper: #F5F1EB;
    --ink: #521000;
    --ink-soft: rgba(82, 16, 0, 0.7);
    --rule: #EBD5C1;
  }
  *, *::before, *::after { box-sizing: border-box; }
  html, body { background: var(--paper); color: var(--ink); margin: 0; }
  body {
    font-family: 'Iowan Old Style', 'Charter', Georgia, serif;
    font-size: 14px; line-height: 1.5;
    padding: 48px 56px 96px;
    max-width: 1240px; margin: 0 auto;
  }
  header { margin-bottom: 48px; }
  h1 { font-weight: 500; font-size: 28px; margin: 0 0 8px; letter-spacing: -0.01em; }
  header p { color: var(--ink-soft); max-width: 680px; margin: 0 0 4px; }
  header p.note { font-size: 12px; }
  h2.section {
    font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase;
    color: var(--ink-soft); font-weight: 500;
    border-bottom: 1px solid var(--rule);
    padding-bottom: 8px; margin: 56px 0 24px;
  }
  .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 36px 28px; }
  .card { display: flex; flex-direction: column; gap: 4px; }
  .card .eyebrow {
    font-family: -apple-system, BlinkMacSystemFont, 'Source Sans Pro', sans-serif;
    font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--ink-soft); margin: 0;
  }
  .card h3 { font-size: 15px; font-weight: 500; margin: 0; letter-spacing: -0.005em; }
  .card.journey h3 { font-style: italic; font-size: 17px; }
  .card svg { margin-top: 8px; width: 100%; height: auto; overflow: visible; }
  .card .note {
    margin: 6px 0 0; font-style: italic; font-size: 12px; color: var(--ink-soft);
    max-width: 38ch;
  }
</style>
</head>
<body>
<header>
  <h1>Marginalia gestalt</h1>
  <p>Every journey and example, generated from a single grammar of primitives.</p>
  <p class="note">Locked metrics, locked palette, locked typography. Cards compose words; words compose tokens; nothing is bespoke.</p>
</header>
"""


def render() -> str:
    out = [HEAD]
    out.append('<h2 class="section">Journeys</h2>\n<div class="grid">')
    for j in JOURNEYS:
        out.append(j.render_html())
    out.append("</div>")
    out.append('<h2 class="section">Examples</h2>\n<div class="grid">')
    for e in EXAMPLES:
        out.append(e.render_html())
    out.append("</div>\n</body>\n</html>\n")
    return "\n".join(out)


def main() -> None:
    OUT.write_text(render())
    print(f"wrote {OUT.relative_to(ROOT)} — {len(JOURNEYS)} journeys + {len(EXAMPLES)} examples")


if __name__ == "__main__":
    main()
