"""Marginalia attachments and figure registry.

Authors of example markdown never touch this file. The project owner curates
named figures here and attaches them to cells via slug + anchor.

Anchors today:
    "cell-0", "cell-1", … each literate-program cell, zero-indexed.
    The figure renders in a banner row AFTER the named cell.

The renderer in app.py interleaves cells and banners: every cell keeps
its prose|code 2-column grid intact, and a banner row spanning both
columns sits between cells (or after the only cell on single-cell
examples). Multiple figures attached to the same cell share one
banner as a small multiple. Cells without an attached figure render
exactly as before.

See docs/visual-explainer-spec.md for the full design and
docs/journey-visualisation-rubric.md for the figure-quality rubric.
"""

from __future__ import annotations

import html
from typing import Callable

try:
    from .marginalia_grammar import Canvas
except ImportError:  # Cloudflare Workers import siblings without the package prefix.
    from marginalia_grammar import Canvas


# ─── Named figures ─────────────────────────────────────────────────────


def aliasing_mutation(c: Canvas) -> None:
    """Two names binding to one mutable list, before and after a mutation."""
    c.tag(0, 12, "before")
    c.name_box(0, 18, "first")
    c.name_box(0, 48, "second")
    c.closed_arrow(60, 30, 86, 46, emphasis=False)
    c.closed_arrow(60, 60, 86, 46, emphasis=False)
    c.object_box(88, 32, "", '["python"]', w=88, h=28)

    c.tag(0, 100, "after append")
    c.name_box(0, 108, "first")
    c.name_box(0, 138, "second")
    c.closed_arrow(60, 120, 86, 136, emphasis=False)
    c.closed_arrow(60, 150, 86, 136, emphasis=False)
    c.object_box(88, 122, "", '["python","workers"]', w=130, h=28)


def tuple_no_mutation(c: Canvas) -> None:
    """The contrast: two names binding to one immutable tuple — no mutation possible."""
    c.tag(0, 12, "tuple — frozen")
    c.name_box(0, 18, "first")
    c.name_box(0, 48, "second")
    c.closed_arrow(60, 30, 86, 46, emphasis=False)
    c.closed_arrow(60, 60, 86, 46, emphasis=False)
    c.object_box(88, 32, "", '("python",)', w=110, h=28)

    c.tag(0, 100, "no .append")
    c.name_box(0, 108, "first")
    c.name_box(0, 138, "second")
    c.closed_arrow(60, 120, 86, 136, emphasis=False)
    c.closed_arrow(60, 150, 86, 136, emphasis=False)
    c.object_box(88, 122, "", '("python",)', w=110, h=28)
    c.label(150, 170, "tuples raise AttributeError", anchor="middle")


def iterator_unroll(c: Canvas) -> None:
    """Four passes of next() over a sequence, with a caret advancing each row."""
    items = list("abcd")
    for i in range(4):
        y = 8 + i * 30
        c.cells(20, y, items)
        c.caret(20 + i * 24 + 12, y)
        suffix = " — last" if i == 3 else ""
        c.label(124, y + 16, f"next(){suffix}")


def scope_rings(c: Canvas) -> None:
    """LEGB lookup: nested rings, lookup path traced from innermost outward."""
    c.frame(8, 6, 200, 100, label="B · built-in")
    c.frame(28, 22, 160, 76, label="G · global")
    c.frame(48, 38, 120, 52, label="E · enclosing")
    c.frame(68, 54, 80, 28, label="L · local")
    c.dot(108, 68, emphasis=True)
    c.dashed(108, 78, 108, 100)


def closure_cell(c: Canvas) -> None:
    """Inner function references a cell created by the outer call.

    Outer scope holds the `cell` (the captured `factor`); the inner function
    keeps a reference into it, so the call survives the outer return.
    """
    c.frame(0, 16, 240, 96, label="make_multiplier")
    c.tag(16, 32, "cell")
    c.cell(16, 38, "factor=2", w=84, h=22)
    c.frame(112, 38, 122, 60, label="multiply")
    c.label(173, 76, "uses cell", anchor="middle")
    c.closed_arrow(128, 76, 102, 56, emphasis=True)


def slice_ruler(c: Canvas) -> None:
    """Adjacent slices [:3] and [3:] split a sequence at index 3."""
    items = list("abcdef")
    for i, v in enumerate(items):
        c.cell(20 + i * 32, 30, v, w=32, h=24)
    c.hairline(20, 64, 20 + 6 * 32, 64)
    for i in range(7):
        c.tick(20 + i * 32, 64)
        c.label(20 + i * 32, 76, str(i), anchor="middle")
    # bracket above for [:3]
    c.dashed(20, 22, 20, 28)
    c.dashed(20 + 3 * 32, 22, 20 + 3 * 32, 28)
    c.dashed(20, 22, 20 + 3 * 32, 22)
    c.label(20 + 1.5 * 32, 18, "[:3]", anchor="middle")
    # bracket below for [3:]
    c.dashed(20 + 3 * 32, 92, 20 + 3 * 32, 86)
    c.dashed(20 + 6 * 32, 92, 20 + 6 * 32, 86)
    c.dashed(20 + 3 * 32, 92, 20 + 6 * 32, 92)
    c.label(20 + 4.5 * 32, 104, "[3:]", anchor="middle")


def branch_fork(c: Canvas) -> None:
    """Make decisions explicitly: a value flows through a predicate to one branch."""
    c.cell(0, 36, "value", w=52, h=22)
    c.closed_arrow(52, 47, 80, 47, emphasis=False)
    c.node(98, 47, "?", r=14)
    c.closed_arrow(110, 38, 158, 14, emphasis=False)
    c.closed_arrow(110, 56, 158, 80, emphasis=False)
    c.cell(160, 4, "case A", w=68, h=22)
    c.cell(160, 70, "case B", w=68, h=22)


def loop_repetition(c: Canvas) -> None:
    """The shape of a loop: walk the sequence, run the body, return."""
    c.cells(0, 28, ["a", "b", "c", "d"], w=28)
    c.caret(0 + 14, 28)
    c.closed_arrow(116, 40, 142, 40, emphasis=False)
    c.cell(144, 28, "body", w=56, h=24)
    c.dashed(172, 54, 172, 76)
    c.dashed(172, 76, 14, 76)
    c.dashed(14, 76, 14, 54)
    c.closed_arrow(14, 56, 14, 40, emphasis=True)


def iter_protocol(c: Canvas) -> None:
    """The hidden machinery behind for: iterable → iter() → next() … values."""
    c.object_box(0, 30, "iterable", "[a,b,c]", w=82, h=28)
    c.dashed(84, 44, 118, 44)
    c.label(101, 38, "iter()", anchor="middle")
    c.object_box(120, 30, "iterator", "", w=80, h=28)
    c.closed_arrow(200, 44, 232, 44, emphasis=True)
    c.label(216, 38, "next()", anchor="middle")
    c.cells(234, 32, ["a", "b", "c"], w=22)


# ─── Runtime journey ──────────────────────────────────────────────────


def program_output(c: Canvas) -> None:
    """Runtime · Start with executable evidence: a program produces visible output."""
    c.cell(0, 28, 'print("…")', w=92, h=28)
    c.closed_arrow(92, 42, 124, 42, emphasis=False)
    c.label(108, 36, "stdout", anchor="middle")
    c.cell(126, 28, "hello world", w=110, h=28, soft=True)


def identity_and_equality(c: Canvas) -> None:
    """Runtime · Separate value, identity, and absence: same object vs equal objects."""
    c.tag(0, 14, "is + ==")
    c.name_box(0, 22, "a")
    c.name_box(0, 50, "b")
    c.closed_arrow(60, 34, 100, 50, emphasis=False)
    c.closed_arrow(60, 62, 100, 50, emphasis=False)
    c.cell(102, 38, "[1,2]", w=46, h=24, soft=True)
    c.tag(170, 14, "== only")
    c.name_box(170, 22, "a")
    c.name_box(170, 50, "b")
    c.closed_arrow(230, 34, 252, 34, emphasis=False)
    c.closed_arrow(230, 62, 252, 62, emphasis=False)
    c.cell(254, 22, "[1,2]", w=44, h=22, soft=True)
    c.cell(254, 52, "[1,2]", w=44, h=22, soft=True)


def operator_dispatch(c: Canvas) -> None:
    """Runtime · Read expressions as object operations: syntax becomes a method call."""
    c.cell(0, 30, "a + b", w=70, h=28)
    c.closed_arrow(70, 44, 116, 44, emphasis=True)
    c.label(93, 22, "dispatches", anchor="middle")
    c.cell(118, 30, "a.__add__(b)", w=140, h=28, soft=True)


# ─── Shapes journey ───────────────────────────────────────────────────


def container_questions(c: Canvas) -> None:
    """Shapes · Pick the container that matches the question — each answers a different one."""
    pairs = [
        ("list", "[a,b]", "ordered"),
        ("tuple", "(a,b)", "fixed"),
        ("dict", "{k:v}", "lookup"),
        ("set", "{a,b}", "unique"),
    ]
    for i, (tag, val, q) in enumerate(pairs):
        x = i * 70
        c.object_box(x, 26, tag, val, w=64, h=28)
        c.label(x + 32, 70, q, anchor="middle")


def reshape_pipeline(c: Canvas) -> None:
    """Shapes · Move between shapes deliberately: one input, one transform, one result."""
    c.cell(0, 30, "[3,1,4]", w=80, h=28)
    c.closed_arrow(80, 44, 120, 44, emphasis=True)
    c.label(100, 36, "sorted", anchor="middle")
    c.cell(122, 30, "[1,3,4]", w=80, h=28, soft=True)


def text_data_boundary(c: Canvas) -> None:
    """Shapes · Cross text and data boundaries: text in, structured value out."""
    c.cell(0, 30, '"42"', w=70, h=28)
    c.tag(0, 24, "text")
    c.closed_arrow(70, 44, 110, 44, emphasis=True)
    c.label(90, 36, "parse", anchor="middle")
    c.object_box(112, 30, "int", "42", w=58, h=28)


# ─── Interfaces journey ───────────────────────────────────────────────


def function_signature(c: Canvas) -> None:
    """Interfaces · Functions as named behavior: input → body → output."""
    c.closed_arrow(0, 44, 32, 44, emphasis=False)
    c.label(16, 36, "args", anchor="middle")
    c.frame(34, 26, 110, 36, label="def f(...)")
    c.closed_arrow(144, 44, 176, 44, emphasis=False)
    c.label(160, 36, "return", anchor="middle")


def function_as_value(c: Canvas) -> None:
    """Interfaces · Functions as values: name binds to a function object."""
    c.frame(0, 22, 80, 36, label="fn")
    c.mono(40, 44, "def f")
    c.closed_arrow(80, 40, 116, 40, emphasis=True)
    c.cell(118, 26, "g = fn", w=80, h=28, soft=True)


def class_with_state(c: Canvas) -> None:
    """Interfaces · Bundle behavior with state: a class groups fields and methods."""
    c.frame(0, 8, 150, 92, label="class Box")
    c.tag(12, 26, "state")
    c.cell(12, 32, "x · y", w=126, h=22)
    c.tag(12, 64, "methods")
    c.cell(12, 70, "move(...)", w=126, h=22)


# ─── Types journey ────────────────────────────────────────────────────


def annotation_ghost(c: Canvas) -> None:
    """Types · Keep runtime and static separate: annotations describe; runtime accepts any object."""
    c.mono(0, 36, "def f(x: int, y: str) -> bool: …", anchor="start")
    c.dashed(54, 28, 76, 28)
    c.dashed(102, 28, 124, 28)
    c.dashed(150, 28, 192, 28)


def union_types(c: Canvas) -> None:
    """Types · Describe realistic shapes: a slot accepting one of several types."""
    c.tag(0, 14, "x: int|str|None")
    c.cell(0, 22, "x", w=44, h=28)
    c.closed_arrow(44, 36, 80, 14, emphasis=False)
    c.closed_arrow(44, 36, 80, 36, emphasis=False)
    c.closed_arrow(44, 36, 80, 58, emphasis=False)
    c.cell(82, 4, "int", w=70, h=22, soft=True)
    c.cell(82, 26, "str", w=70, h=22, soft=True)
    c.cell(82, 48, "None", w=70, h=22, soft=True)


def generic_preservation(c: Canvas) -> None:
    """Types · Scale annotations: a generic preserves the input type through the call."""
    c.cell(0, 30, "T", w=36, h=28, soft=True)
    c.closed_arrow(36, 44, 72, 44, emphasis=True)
    c.frame(74, 26, 100, 36, label="fn[T]")
    c.closed_arrow(174, 44, 210, 44, emphasis=True)
    c.cell(212, 30, "T", w=36, h=28, soft=True)


# ─── Reliability journey ──────────────────────────────────────────────


def exception_lanes(c: Canvas) -> None:
    """Reliability · Make failure explicit: try/except/else/finally as parallel lanes."""
    ys = [(20, "try"), (40, "except"), (60, "else"), (80, "finally")]
    path = [(50, 20), (110, 20), (130, 60), (200, 60), (220, 80), (290, 80)]
    c.lanes(ys, x0=40, x1=300, path=path)


def context_bowtie(c: Canvas) -> None:
    """Reliability · Control resource boundaries: enter → body → exit, with raise routed through exit."""
    c.node(20, 48, "in", r=14)
    c.closed_arrow(34, 48, 76, 48, emphasis=False)
    c.cell(78, 36, "body", w=86, h=24)
    c.closed_arrow(164, 48, 206, 48, emphasis=False)
    c.node(220, 48, "out", r=14)
    c.dashed(122, 60, 210, 48)


def async_swimlane(c: Canvas) -> None:
    """Reliability · Operations that outlive one expression: loop and coroutine swap on await."""
    c.lane(28, x0=20, x1=270, label="loop")
    c.lane(64, x0=20, x1=270, label="coro")
    c.cell(40, 58, "", w=34, h=12)
    c.dashed(76, 64, 110, 28)
    c.cell(112, 22, "", w=58, h=12)
    c.dashed(172, 28, 206, 64)
    c.cell(208, 58, "", w=34, h=12)
    c.label(95, 16, "await", anchor="middle")
    c.label(190, 16, "resume", anchor="middle")


# ─── Control flow journey ─────────────────────────────────────────────


def naming_decisions(c: Canvas) -> None:
    """Control flow · Name and shape decisions: the walrus binds while comparing."""
    c.cell(0, 30, "len(xs)", w=80, h=28)
    c.closed_arrow(80, 44, 110, 44, emphasis=True)
    c.label(95, 36, ":=", anchor="middle")
    c.cell(112, 4, "n", w=40, h=22, soft=True)
    c.tag(112, 0, "name")
    c.cell(112, 50, "value", w=78, h=22, soft=True)
    c.dashed(152, 16, 196, 16)
    c.cell(198, 4, "n > 10", w=72, h=22)


def early_exit(c: Canvas) -> None:
    """Control flow · Stop as soon as the answer is known: the loop exits on first match."""
    c.cells(0, 28, ["a", "b", "c", "d", "e"], w=28)
    c.dot(70, 40, emphasis=True)
    c.closed_arrow(70, 56, 70, 78, emphasis=True)
    c.cell(40, 80, "found · break", w=80, h=24, soft=True)
    c.label(70, 14, "first match", anchor="middle")


# ─── Iteration journey ────────────────────────────────────────────────


# ─── Example figures (promoted from the gestalt) ──────────────────────


def variables_bind(c: Canvas) -> None:
    """Variables · names bind to objects: the canonical Python picture."""
    c.bind(0, 6, "x", "int", "42", object_w=70, gap=20)


def call_stack(c: Canvas) -> None:
    """Recursion · stacked frames of the same function with different arguments."""
    chain = [3, 2, 1, 0]
    for i, n in enumerate(chain):
        suffix = " ← base" if n == 0 else ""
        c.cell(0, i * 22, f"factorial({n}){suffix}", w=180, h=20)
    c.dashed(192, 90, 192, 18)
    c.closed_arrow(192, 30, 192, 18, emphasis=True)


def decorator_rebind(c: Canvas) -> None:
    """Decorators · before: name binds to function. After @dec: name binds to wrapper."""
    c.tag(0, 12, "before")
    c.bind(0, 18, "f", "fn", "f₀", object_w=50, gap=20)
    c.tag(0, 70, "after @dec")
    c.name_box(0, 78, "f")
    c.closed_arrow(60, 90, 96, 90, emphasis=True)
    c.cell(98, 76, "wrapper", w=80, h=28)
    c.object_box(186, 78, "", "f₀", w=44, h=24)
    c.dashed(178, 90, 186, 90)


def mro_chain(c: Canvas) -> None:
    """Inheritance · diamond becomes a linear MRO via C3 linearization."""
    # Diamond ghost above
    c.frame(80, 0, 40, 22, ghost=True)
    c.mono(100, 16, "A")
    c.ghost(98, 22, 58, 42)
    c.ghost(102, 22, 142, 42)
    c.frame(40, 42, 40, 22, ghost=True)
    c.mono(60, 58, "B")
    c.frame(120, 42, 40, 22, ghost=True)
    c.mono(140, 58, "C")
    c.ghost(60, 64, 96, 80)
    c.ghost(140, 64, 104, 80)
    c.frame(80, 80, 40, 22, ghost=True)
    c.mono(100, 96, "D")
    # MRO chain below
    c.tag(0, 118, "mro")
    chain = [("D", 36), ("B", 36), ("C", 36), ("A", 36), ("object", 56)]
    x = 0
    for v, w in chain:
        c.cell(x, 124, v, w=w, h=22)
        x += w


def dataclass_fields(c: Canvas) -> None:
    """Dataclasses · fields declared once become __init__ parameters."""
    c.tag(0, 12, "declaration")
    fields = [("name", "str"), ("age", "int"), ("tags", "list")]
    for i, (n, t) in enumerate(fields):
        c.cell(0, 18 + i * 20, f"{n} : {t}", w=110, h=20)
    c.closed_arrow(110, 48, 146, 48, emphasis=True)
    c.object_box(148, 32, "", "__init__(name, age, tags)", w=160, h=32)


def class_triangle(c: Canvas) -> None:
    """Classes · instance → class → type — every Python value sits on this triangle."""
    c.dot(20, 28)
    c.label(20, 54, "instance", anchor="middle")
    c.closed_arrow(26, 28, 86, 28, emphasis=False)
    c.frame(88, 10, 60, 36, label="class")
    c.mono(118, 32, "Class")
    c.closed_arrow(148, 28, 208, 28, emphasis=False)
    c.frame(210, 10, 60, 36, label="type")
    c.mono(240, 32, "type")


def exception_cause_context(c: Canvas) -> None:
    """Exception chaining · explicit `__cause__` (raise from) vs implicit `__context__`."""
    c.cell(0, 20, "ValueError", w=100, h=32)
    c.closed_arrow(100, 28, 180, 28, emphasis=True)
    c.label(140, 20, "__cause__", anchor="middle")
    c.dashed(100, 44, 180, 44)
    c.label(140, 62, "__context__", anchor="middle")
    c.cell(182, 20, "RuntimeError", w=100, h=32)


def unpacking_bind(c: Canvas) -> None:
    """Unpacking · left-side names bind to right-side positions; *rest gathers the middle."""
    items = ["1", "2", "3", "4", "5"]
    for i, v in enumerate(items):
        c.cell(i * 30, 0, v, w=30, h=22)
    c.cell(0, 58, "a", w=30, h=22)
    c.cell(30, 58, "*rest", w=90, h=22, ghost=True)
    c.cell(120, 58, "b", w=30, h=22)
    c.dashed(15, 22, 15, 58)
    c.dashed(45, 22, 75, 58)
    c.dashed(75, 22, 75, 58)
    c.dashed(105, 22, 75, 58)
    c.dashed(135, 22, 135, 58)


def comprehension_equivalence(c: Canvas) -> None:
    """Comprehensions · the comprehension above and the equivalent for-loop below."""
    c.cell(0, 0, "[x*2 for x in xs if x > 0]", w=280, h=22, soft=True)
    c.cell(0, 30, "out = []", w=280, h=14, ghost=True)
    c.cell(0, 44, "for x in xs:", w=280, h=14, ghost=True)
    c.cell(0, 58, "    if x > 0: out.append(x*2)", w=280, h=14, ghost=True)


def list_append(c: Canvas) -> None:
    """Lists · mutable sequence; `.append` extends the same list object."""
    c.cells(0, 8, ["3", "1", "4"], w=24)
    c.cell(72, 8, "+1", ghost=True)
    c.closed_arrow(98, 20, 132, 20, emphasis=True)
    c.label(136, 18, ".append", anchor="start")


def dict_buckets(c: Canvas) -> None:
    """Dictionaries · hashed buckets; collisions chain into a neighbouring slot."""
    c.tag(0, 12, "hash → bucket")
    rows = [("0", '"a" → 1'), ("1", '"b" → 2'), ("2", '"c" → 3')]
    for i, (idx, body) in enumerate(rows):
        y = 18 + i * 24
        c.label(0, y + 16, idx, anchor="start")
        c.cell(14, y, body, w=80, h=24)
    c.closed_arrow(96, 54, 132, 54, emphasis=True)
    c.cell(134, 42, '"d" → 4', w=80, h=24, soft=True)
    c.label(218, 58, "collision", anchor="start")


# ─── Workers journey (abstract sections; designs tentative) ──────────


def workers_portable_evidence(c: Canvas) -> None:
    """Workers · the process API is unavailable; a captured value crosses instead."""
    c.tag(0, 4, "unavailable")
    c.cell(0, 12, "multiprocessing.Process()", w=180, h=22, ghost=True)
    c.dashed(0, 24, 180, 24)
    c.tag(0, 50, "portable evidence")
    c.cell(0, 58, "value", w=60, h=22, soft=True)
    c.closed_arrow(60, 69, 100, 69, emphasis=True)
    c.cell(102, 58, "asserted in-process", w=120, h=22)


def workers_protocol_local(c: Canvas) -> None:
    """Workers · the protocol shape is the lesson; no real socket is opened."""
    c.tag(0, 4, "request shape")
    c.cell(0, 12, "GET /resource", w=160, h=22)
    c.closed_arrow(80, 38, 80, 56, emphasis=True)
    c.tag(0, 76, "response shape · asserted locally")
    c.cell(0, 84, "200 OK · { … }", w=160, h=22)


# ─── Examples promoted from the gestalt: new paint code ──────────────


def number_lines(c: Canvas) -> None:
    """Numbers · int unbounded; float spacing widens at the extremes."""
    c.tag(0, 8, "int · unbounded")
    c.register(0, 22, 260, divisions=8)
    c.tag(0, 50, "float · representable spacing widens")
    c.register(0, 64, 260)
    for x in (10, 30, 60, 100, 130, 140, 148, 160, 188, 230, 260):
        c.tick(x, 64)
    c.dot(140, 64, emphasis=True)


def expression_tree(c: Canvas) -> None:
    """Operators and Literals · expression `(2+3)*4` parsed as a tree."""
    c.node(120, 12, "*", r=12)
    c.node(80, 50, "+", r=12)
    c.node(180, 50, "4", r=10)
    c.node(56, 80, "2", r=10)
    c.node(104, 80, "3", r=10)
    c.connect(120, 12, 12, 80, 50, 12)
    c.connect(120, 12, 12, 180, 50, 10)
    c.connect(80, 50, 12, 56, 80, 10)
    c.connect(80, 50, 12, 104, 80, 10)


def none_singleton(c: Canvas) -> None:
    """None · three names converging on the single None object."""
    for i, n in enumerate("abc"):
        c.name_box(0, i * 28, n)
    for y in (12, 40, 68):
        c.closed_arrow(60, y, 158, 40, emphasis=False)
    c.object_box(160, 24, "NoneType", "None", w=80)


def codepoints_bytes(c: Canvas) -> None:
    """Strings · text is unicode; bytes are a separate encoding layer."""
    c.tag(0, 8, "codepoints")
    for i, ch in enumerate("café"):
        c.cell(i * 40, 16, ch, w=40, h=28)
    c.tag(0, 60, "utf-8 bytes")
    widths = [40, 40, 40, 20, 20]
    bytes_ = ["63", "61", "66", "c3", "a9"]
    x = 0
    for w, b in zip(widths, bytes_):
        c.cell(x, 68, b, w=w, h=14)
        x += w


def sort_stability(c: Canvas) -> None:
    """Sorting · stable sort preserves equal keys' original order."""
    c.tag(0, 4, "input")
    c.tag(180, 4, "stable sort by key")
    inputs = ["2 · Ada", "1 · Bo", "2 · Eve", "1 · Cy"]
    outputs = ["1 · Bo", "1 · Cy", "2 · Ada", "2 · Eve"]
    for i, (a, b) in enumerate(zip(inputs, outputs)):
        c.cell(0, 12 + i * 22, a, w=80, h=20)
        c.cell(180, 12 + i * 22, b, w=80, h=20)
    c.dashed(80, 44, 180, 22)
    c.dashed(80, 88, 180, 44)
    c.dashed(80, 22, 180, 66)
    c.dashed(80, 66, 180, 88)


def kw_only_separator(c: Canvas) -> None:
    """Keyword-only arguments · `*` divides positional from keyword-only."""
    c.mono(0, 18, "def f(a, b, *, c, d): …", anchor="start")
    c.dashed(82, 22, 82, 38)
    c.label(40, 50, "positional or kw", anchor="middle")
    c.label(140, 50, "keyword only", anchor="middle")


def positional_only_separator(c: Canvas) -> None:
    """Positional-only parameters · `/` divides positional-only from positional-or-kw."""
    c.mono(0, 18, "def f(a, b, /, c, d): …", anchor="start")
    c.dashed(82, 22, 82, 38)
    c.label(40, 50, "positional only", anchor="middle")
    c.label(140, 50, "positional or kw", anchor="middle")


def generator_ribbon(c: Canvas) -> None:
    """Generators · execution paused between yields, resumed by next()."""
    c.tag(0, 8, "paused between yields · resumed by next()")
    c.ribbon(0, 16, 260, h=30, gates=[64, 136, 208], soft_segments=[(0, 64), (136, 208)])
    c.mono(32, 36, "…")
    c.mono(100, 36, "yield")
    c.mono(172, 36, "…")
    c.mono(244, 36, "yield")


def truth_and_size(c: Canvas) -> None:
    """Truth and size · bool(x) checks __bool__, then __len__, else True."""
    c.cell(0, 22, "x", w=40, h=24)
    c.closed_arrow(40, 34, 70, 34, emphasis=True)
    c.cell(72, 0, "__bool__()", w=160, h=22)
    c.cell(72, 22, "__len__() != 0", w=160, h=22, ghost=True)
    c.cell(72, 44, "default: True", w=160, h=22, ghost=True)


def descriptor_protocol(c: Canvas) -> None:
    """Descriptors · attribute access routes to __get__/__set__/__delete__."""
    c.cell(0, 22, "obj.attr", w=80, h=24)
    c.closed_arrow(80, 34, 110, 34, emphasis=True)
    c.frame(112, 0, 110, 70, label="descriptor")
    c.mono(167, 22, "__get__")
    c.mono(167, 38, "__set__")
    c.mono(167, 54, "__delete__")


def bound_unbound(c: Canvas) -> None:
    """Bound vs unbound methods · instance.method binds self; Class.method does not."""
    c.cell(0, 0, "obj.method", w=110, h=22)
    c.closed_arrow(110, 11, 140, 11, emphasis=True)
    c.cell(142, 0, "bound · self filled", w=152, h=22, soft=True)
    c.cell(0, 32, "Class.method", w=110, h=22)
    c.closed_arrow(110, 43, 140, 43, emphasis=False)
    c.cell(142, 32, "function · self required", w=152, h=22)


def method_kinds(c: Canvas) -> None:
    """Method kinds · classmethod, staticmethod, instance — first-arg differs."""
    rows = [
        ("@classmethod", "Cls"),
        ("@staticmethod", "(none)"),
        ("instance", "self"),
    ]
    for i, (decorator, first_arg) in enumerate(rows):
        y = i * 24
        c.cell(0, y, decorator, w=110, h=22)
        c.closed_arrow(110, y + 11, 140, y + 11, emphasis=False)
        c.cell(142, y, f"first arg · {first_arg}", w=130, h=22, soft=True)


def callable_objects(c: Canvas) -> None:
    """Callable objects · `__call__` makes any object look like a function."""
    c.frame(0, 4, 100, 36, label="object")
    c.mono(50, 26, "__call__")
    c.closed_arrow(100, 22, 138, 22, emphasis=True)
    c.cell(140, 10, "obj(...)", w=80, h=24, soft=True)


def attribute_lookup(c: Canvas) -> None:
    """Attribute access · instance dict, then class dict, then __getattr__; first hit wins."""
    c.cell(0, 22, "obj.x", w=70, h=24)
    c.closed_arrow(70, 34, 100, 34, emphasis=True)
    c.cell(102, 0, "instance __dict__", w=140, h=22)
    c.cell(102, 22, "class __dict__", w=140, h=22)
    c.cell(102, 44, "__getattr__", w=140, h=22, ghost=True)


def guard_clauses(c: Canvas) -> None:
    """Guard clauses · early returns first; main work runs only when guards fall through."""
    c.cell(0, 0, "if not valid: return", w=180, h=22, soft=True)
    c.cell(0, 24, "if missing: return None", w=180, h=22, soft=True)
    c.cell(0, 48, "if special_case: return X", w=180, h=22, soft=True)
    c.cell(0, 78, "main work …", w=180, h=22)
    c.closed_arrow(190, 11, 220, 11, emphasis=False)
    c.closed_arrow(190, 35, 220, 35, emphasis=False)
    c.closed_arrow(190, 59, 220, 59, emphasis=False)
    c.label(222, 38, "exit", anchor="start")


def bytes_vs_bytearray(c: Canvas) -> None:
    """Bytes vs bytearray · frozen sequence of integers vs mutable counterpart."""
    c.tag(0, 4, "bytes — frozen")
    c.cell(0, 12, "b'\\\\x63\\\\x61\\\\x66'", w=160, h=24)
    c.tag(0, 50, "bytearray — mutable")
    c.cell(0, 58, "bytearray(b'\\\\x63\\\\x61')", w=180, h=24)
    c.closed_arrow(180, 70, 218, 70, emphasis=True)
    c.label(222, 67, ".append(0x66)", anchor="start")


def sentinel_iteration(c: Canvas) -> None:
    """Sentinel iteration · `iter(callable, sentinel)` calls until the sentinel returns."""
    c.cell(0, 22, "iter(read, '')", w=120, h=24)
    c.closed_arrow(120, 34, 152, 34, emphasis=True)
    c.cell(154, 0, "value", w=70, h=20)
    c.cell(154, 22, "value", w=70, h=20)
    c.cell(154, 44, "value", w=70, h=20)
    c.cell(154, 66, "''", w=70, h=20, ghost=True)
    c.label(228, 80, "sentinel · stop", anchor="start")


def partial_functions(c: Canvas) -> None:
    """Partial functions · `partial(f, 1)` pre-fills arguments, returning a thinner callable."""
    c.cell(0, 12, "f(a, b, c)", w=100, h=24)
    c.closed_arrow(100, 24, 130, 24, emphasis=True)
    c.cell(132, 0, "partial(f, 1)", w=100, h=24)
    c.closed_arrow(232, 24, 262, 24, emphasis=False)
    c.cell(264, 12, "g(b, c)", w=70, h=24, soft=True)


# ─── More example figures (third coverage push) ───────────────────────


def args_kwargs(c: Canvas) -> None:
    """Args and kwargs · *args gathers extra positionals; **kwargs gathers extra keywords."""
    c.mono(20, 22, "def f(*args, **kwargs): …", anchor="start")
    c.dashed(80, 26, 80, 44)
    c.dashed(152, 26, 152, 44)
    c.label(80, 56, "extra positionals → tuple", anchor="middle")
    c.label(210, 56, "extra keywords → dict", anchor="middle")


def multiple_return(c: Canvas) -> None:
    """Multiple return values · the function returns a tuple; the caller unpacks it."""
    c.cell(0, 0, "def f(): return a, b", w=180, h=24)
    c.closed_arrow(90, 26, 90, 44, emphasis=True)
    c.cell(58, 44, "(a, b)", w=64, h=22, soft=True)
    c.closed_arrow(90, 68, 90, 86, emphasis=False)
    c.cell(50, 86, "x, y", w=80, h=22)


def lambda_expression(c: Canvas) -> None:
    """Lambdas · a function as a value: parameters on the left, expression on the right."""
    c.cell(0, 0, "lambda x: x + 1", w=170, h=28, soft=True)
    c.dashed(40, 28, 40, 50)
    c.dashed(120, 28, 120, 50)
    c.label(40, 62, "params", anchor="middle")
    c.label(120, 62, "expression", anchor="middle")


def property_fork(c: Canvas) -> None:
    """Properties · obj.x routes through fget/fset instead of touching __dict__."""
    c.cell(0, 22, "obj.x", w=70, h=24)
    c.closed_arrow(70, 22, 110, 4, emphasis=True)
    c.cell(112, 0, "fget / fset", w=120, h=22, soft=True)
    c.closed_arrow(70, 46, 110, 56, emphasis=False)
    c.cell(112, 50, "__dict__", w=120, h=22, ghost=True)


def metaclass_triangle(c: Canvas) -> None:
    """Metaclasses · instance → class → metaclass; the metaclass is the type of the class."""
    c.dot(20, 30)
    c.label(20, 56, "instance", anchor="middle")
    c.closed_arrow(26, 30, 86, 30, emphasis=False)
    c.frame(88, 12, 60, 36, label="class")
    c.mono(118, 34, "Class")
    c.closed_arrow(148, 30, 218, 30, emphasis=False)
    c.frame(220, 12, 80, 36, label="metaclass")
    c.mono(260, 34, "type")


def sys_path_resolution(c: Canvas) -> None:
    """Modules · imports walk sys.path; the first hit wins."""
    c.tag(0, 4, "sys.path")
    paths = ["cwd", "site-packages", "stdlib", "…"]
    for i, p in enumerate(paths):
        c.cell(0, 14 + i * 20, p, w=120, h=20)
    c.closed_arrow(120, 46, 156, 46, emphasis=True)
    c.label(145, 30, "first hit", anchor="middle")
    c.cell(158, 34, "mymod.py", w=100, h=24, soft=True)


def import_alias(c: Canvas) -> None:
    """Import aliases · `import x as y` makes y point at the same module object as x."""
    c.mono(0, 8, "import numpy as np", anchor="start")
    c.cell(0, 24, "np", w=40, h=22)
    c.closed_arrow(40, 35, 80, 35, emphasis=True)
    c.cell(82, 24, "numpy module", w=130, h=22, soft=True)


def protocol_check(c: Canvas) -> None:
    """Protocols · structural check; an object satisfies a protocol if it has the required methods."""
    c.frame(0, 4, 100, 70, label="object")
    c.mono(50, 20, "read()")
    c.mono(50, 36, "write()")
    c.mono(50, 52, "close()")
    c.closed_arrow(100, 38, 138, 38, emphasis=True)
    c.label(119, 0, "structural", anchor="middle")
    c.frame(140, 4, 80, 70, label="protocol", ghost=True)
    c.mono(180, 28, "read()")
    c.mono(180, 46, "close()")


def enum_members(c: Canvas) -> None:
    """Enums · a fixed set of named symbolic values; no new members appear at runtime."""
    c.frame(0, 0, 280, 60, label="Color · closed set", ghost=True)
    members = ["RED", "GREEN", "BLUE", "no more"]
    for i, m in enumerate(members):
        c.cell(20 + i * 60, 16, m, w=50, h=28)


def datetime_instant(c: Canvas) -> None:
    """Datetime · one instant; the offset names which clock face you're reading."""
    c.register(10, 40, 260, divisions=8)
    c.dashed(150, 30, 150, 50)
    c.label(150, 24, "one instant", anchor="middle")
    c.node(90, 70, "−5h", r=12)
    c.dashed(90, 58, 150, 50)
    c.node(210, 70, "+0h", r=12)
    c.dashed(210, 58, 150, 50)


def json_python_mapping(c: Canvas) -> None:
    """JSON ↔ Python · six type pairs map across the text boundary."""
    c.hairline(120, 0, 120, 110)
    c.tag(60, 4, "json", anchor="middle")
    c.tag(180, 4, "python", anchor="middle")
    rows = [
        ("object", "dict"),
        ("array", "list"),
        ("string", "str"),
        ("number", "int / float"),
        ("true / false", "True / False"),
        ("null", "None"),
    ]
    for i, (a, b) in enumerate(rows):
        y = 24 + i * 14
        c.mono(0, y, a, anchor="start", size=10)
        c.mono(132, y, b, anchor="start", size=10)


def regex_anchors(c: Canvas) -> None:
    """Regular expressions · anchors and quantifiers shape what the pattern matches."""
    c.tag(0, 4, "pattern")
    c.mono(0, 24, "^\\d{2}-\\d{2}$", anchor="start")
    c.tag(0, 56, "input")
    c.cell(0, 64, "", w=200, h=20)
    c.cell(40, 64, "12-34", w=120, h=20, soft=True)


def number_parse(c: Canvas) -> None:
    """Number parsing · text → typed number, raising on bad input."""
    c.cell(0, 22, '"42"', w=70, h=24)
    c.closed_arrow(70, 34, 102, 34, emphasis=True)
    c.label(86, 26, "int()", anchor="middle")
    c.cell(104, 10, "42", w=60, h=22, soft=True)
    c.cell(104, 36, "ValueError", w=100, h=22, ghost=True)


def format_spec(c: Canvas) -> None:
    """String formatting · the format spec is a railroad of named optional fields."""
    c.tag(0, 4, "format spec")
    stations = [("align", 36), ("sign", 30), ("width", 40), (",", 22), (".prec", 44), ("type", 32)]
    x = 0
    for label_text, w in stations:
        c.cell(x, 16, label_text, w=w, h=18)
        x += w + 2
    c.label(0, 54, "{:>6,.2f}")


def truthy_check(c: Canvas) -> None:
    """Truthiness · bool(x) is True except for a small fixed set of falsy values."""
    c.cell(0, 0, "x", w=40, h=24)
    c.closed_arrow(40, 12, 70, 12, emphasis=True)
    c.label(55, 6, "bool", anchor="middle")
    c.cell(72, 0, "True or False", w=130, h=24)
    c.tag(0, 38, "falsy values")
    falsy = [("0", 22), ("0.0", 30), ('""', 26), ("[]", 22), ("{}", 22), ("None", 40), ("False", 40)]
    x = 0
    for label_text, w in falsy:
        c.cell(x, 46, label_text, w=w, h=20)
        x += w + 2


def boolean_truth_table(c: Canvas) -> None:
    """Booleans · `a and b` is True only when both are True; otherwise False."""
    c.tag(64, 0, "a and b", anchor="middle")
    c.label(80, 16, "T", anchor="middle")
    c.label(112, 16, "F", anchor="middle")
    c.label(58, 36, "T", anchor="end")
    c.label(58, 56, "F", anchor="end")
    c.cell(64, 22, "T", w=32, h=20, soft=True)
    c.cell(96, 22, "F", w=32, h=20)
    c.cell(64, 42, "F", w=32, h=20)
    c.cell(96, 42, "F", w=32, h=20)


def set_buckets(c: Canvas) -> None:
    """Sets · hash buckets with no values; membership is O(1)."""
    c.tag(0, 4, "keys only")
    for i, k in enumerate("abc"):
        c.cell(0, 14 + i * 22, k, w=50, h=20)
    c.closed_arrow(50, 36, 90, 36, emphasis=True)
    c.label(70, 28, "x in s", anchor="middle")
    c.cell(92, 24, "O(1)", w=60, h=22, soft=True)


def tuple_frozen(c: Canvas) -> None:
    """Tuples · ordered, immutable sequence; .append doesn't exist."""
    c.tag(0, 0, "frozen sequence")
    c.cell(0, 12, "(3, 1, 4, 1)", w=180, h=26)
    c.dashed(45, 8, 45, 42)
    c.dashed(90, 8, 90, 42)
    c.dashed(135, 8, 135, 42)
    c.cell(190, 12, ".append", w=80, h=26, ghost=True)
    c.dashed(190, 24, 270, 24)


def value_types(c: Canvas) -> None:
    """Values · every literal is a typed object: int, str, list, dict each carry their behaviour."""
    rows = [("int", "42"), ("str", '"hi"'), ("list", "[1,2,3]"), ("dict", "{k:v}")]
    for i, (t, v) in enumerate(rows):
        y = i * 30
        c.object_box(0, y, t, v, w=160, h=26, tag_position="inside")


def literal_forms(c: Canvas) -> None:
    """Literals · each type has its own literal spellings; the source spelling determines the value type."""
    rows = [
        ("int", "42  ·  0x2a  ·  0b101"),
        ("float", "3.14  ·  1e-3"),
        ("str", '"hi"  ·  \'hi\''),
        ("list", "[1, 2, 3]"),
        ("dict", "{k: v}"),
        ("set", "{1, 2, 3}"),
    ]
    for i, (t, spellings) in enumerate(rows):
        y = i * 22
        c.cell(0, y, t, w=50, h=20, soft=True)
        c.cell(52, y, spellings, w=200, h=20)


def function_with_body(c: Canvas) -> None:
    """Functions · `def greet(name): return "Hello, " + name` takes input, computes, returns output."""
    c.closed_arrow(0, 36, 30, 36, emphasis=False)
    c.label(15, 28, "name", anchor="middle")
    c.frame(32, 18, 150, 44, label="def greet(name):")
    c.mono(107, 44, '"Hello, " + name')
    c.closed_arrow(182, 36, 212, 36, emphasis=True)
    c.cell(214, 24, '"Hello, Ada"', w=120, h=24, soft=True)


def yield_delegation(c: Canvas) -> None:
    """Yield from · delegate iteration to an inner generator; its yields surface here."""
    c.tag(0, 4, "outer")
    c.ribbon(0, 14, 240, h=20, gates=[100, 180])
    c.mono(140, 28, "yield from inner")
    c.tag(100, 46, "inner")
    c.ribbon(100, 56, 80, h=24, gates=[124, 152])
    c.dashed(140, 56, 140, 34)


def itertools_chain(c: Canvas) -> None:
    """Itertools · chain joins two iterables into one stream without materialising either."""
    c.object_box(0, 0, "iter A", "1 · 2", w=70, h=24, tag_position="inside")
    c.object_box(0, 34, "iter B", "3 · 4", w=70, h=24, tag_position="inside")
    c.closed_arrow(70, 12, 100, 22, emphasis=False)
    c.closed_arrow(70, 46, 100, 36, emphasis=False)
    c.object_box(102, 16, "chain", "1 · 2 · 3 · 4", w=140, h=28, tag_position="inside")


def assertion_check(c: Canvas) -> None:
    """Assertions · assert tests a condition; True passes, False raises AssertionError."""
    c.cell(0, 22, "assert cond", w=110, h=24)
    c.closed_arrow(110, 22, 140, 0, emphasis=True)
    c.cell(142, 0, "True · pass", w=120, h=20, soft=True)
    c.closed_arrow(110, 46, 140, 56, emphasis=False)
    c.cell(142, 50, "False · AssertionError", w=160, h=20)


def custom_exception_chain(c: Canvas) -> None:
    """Custom exceptions · subclass an existing exception; gain a domain name without changing semantics."""
    chain = ["BaseException", "Exception", "ValueError", "MyDomainError"]
    for i, name in enumerate(chain):
        emph = i == len(chain) - 1
        c.cell(0, i * 24, name, w=220, h=22, soft=emph)


def exception_group_peel(c: Canvas) -> None:
    """Exception groups · except* peels matching leaves; survivors regroup."""
    c.tag(0, 0, "before")
    c.dot(40, 14)
    for x in (20, 36, 52, 68):
        c.ghost(40, 18, x, 40)
    c.dot(20, 44)
    c.dot(36, 44, emphasis=True)
    c.dot(52, 44)
    c.dot(68, 44, emphasis=True)
    c.closed_arrow(90, 30, 140, 30, emphasis=True)
    c.label(115, 22, "except*", anchor="middle")
    c.tag(160, 0, "after")
    c.dot(200, 14)
    c.ghost(200, 18, 180, 40)
    c.ghost(200, 18, 220, 40)
    c.dot(180, 44)
    c.dot(220, 44)


def delete_name_erased(c: Canvas) -> None:
    """Delete statements · `del x` removes the name; the object survives if any other name holds it."""
    c.tag(0, 0, "before")
    c.name_box(0, 12, "x")
    c.closed_arrow(60, 23, 100, 23, emphasis=False)
    c.cell(102, 12, "[1, 2, 3]", w=90, h=22, soft=True)
    c.tag(0, 52, "after del x")
    c.name_box(0, 60, "x")
    c.dashed(0, 70, 60, 70)
    c.dashed(60, 60, 0, 80)
    c.cell(102, 60, "[1, 2, 3]", w=90, h=22, soft=True)


# ─── Fourth coverage push: constraint-shaped examples ─────────────────


def package_tree(c: Canvas) -> None:
    """Packages · a directory with __init__.py becomes an importable package; submodules nest."""
    c.frame(70, 0, 100, 22, label="mypackage")
    c.mono(120, 14, "__init__.py")
    c.stroke(120, 22, 40, 50)
    c.stroke(120, 22, 120, 50)
    c.stroke(120, 22, 200, 50)
    c.cell(10, 50, "a.py", w=60, h=22)
    c.cell(90, 50, "b.py", w=60, h=22)
    c.cell(170, 50, "sub/", w=60, h=22, soft=True)


def venv_boundary(c: Canvas) -> None:
    """Virtual environments · a venv isolates a project's interpreter and packages from the system."""
    c.frame(0, 0, 110, 70, label="project")
    c.cell(12, 18, "code", w=84, h=20)
    c.cell(12, 42, "requirements", w=84, h=20)
    c.closed_arrow(110, 35, 142, 35, emphasis=True)
    c.frame(144, 0, 130, 70, label="venv")
    c.mono(209, 22, "python")
    c.mono(209, 42, "site-packages")


def subprocess_spawn(c: Canvas) -> None:
    """Subprocesses · spawn a child process; capture stdout, stderr, and exit code as portable evidence."""
    c.cell(0, 22, "parent", w=70, h=24)
    c.closed_arrow(70, 34, 110, 34, emphasis=True)
    c.label(90, 26, "spawn", anchor="middle")
    c.cell(112, 22, "child process", w=110, h=24, soft=True)
    c.closed_arrow(222, 34, 252, 34, emphasis=False)
    c.cell(254, 22, "output", w=70, h=24)


def logging_levels(c: Canvas) -> None:
    """Logging · five levels; messages below the configured threshold are dropped."""
    levels = [("CRITICAL", "50"), ("ERROR", "40"), ("WARNING", "30"), ("INFO", "20"), ("DEBUG", "10")]
    for i, (name, num) in enumerate(levels):
        c.cell(0, i * 22, name, w=120, h=20)
        c.cell(122, i * 22, num, w=40, h=20, soft=True)


def aaa_pattern(c: Canvas) -> None:
    """Testing · arrange-act-assert: set up, run the behavior, compare the result."""
    rows = [("arrange", "set up state"), ("act", "perform behavior"), ("assert", "compare result")]
    for i, (label_text, body) in enumerate(rows):
        c.cell(0, i * 24, label_text, w=80, h=22, soft=(i == 2))
        c.closed_arrow(80, i * 24 + 11, 108, i * 24 + 11, emphasis=False)
        c.cell(110, i * 24, body, w=140, h=22)


def protocol_layers(c: Canvas) -> None:
    """Networking · each layer in the stack hides the next; HTTP rests on TCP on IP on the link."""
    layers = ["application · HTTP", "transport · TCP", "network · IP", "link"]
    for i, name in enumerate(layers):
        c.cell(0, i * 22, name, w=200, h=20)


def gil_lanes(c: Canvas) -> None:
    """Threads and processes · the GIL serialises Python bytecode across threads; processes run in parallel."""
    c.lane(20, x0=54, x1=294, label="GIL")
    c.lane(50, x0=54, x1=294, label="thread A")
    c.lane(80, x0=54, x1=294, label="thread B")
    c.cell(64, 44, "", w=30, h=12)
    c.cell(124, 74, "", w=30, h=12)
    c.cell(184, 44, "", w=30, h=12)
    c.cell(244, 74, "", w=30, h=12)


def cast_escape(c: Canvas) -> None:
    """Casts and any · cast(T, x) tells the type checker to treat x as T; runtime is unaffected."""
    c.cell(0, 22, "Any", w=70, h=24, ghost=True)
    c.closed_arrow(70, 34, 110, 34, emphasis=True)
    c.label(90, 12, "cast(T, x)", anchor="middle")
    c.cell(112, 22, "T", w=70, h=24, soft=True)


def newtype_phantom(c: Canvas) -> None:
    """NewType · two static identities backed by the same runtime type."""
    c.tag(0, 0, "runtime: int")
    c.cell(0, 12, "42", w=60, h=24)
    c.tag(0, 50, "static: UserId")
    c.cell(0, 62, "UserId(42)", w=90, h=24, soft=True)


def overload_signatures(c: Canvas) -> None:
    """Overloads · @overload declares multiple signatures; one implementation routes to the right return type."""
    c.tag(0, 0, "@overload")
    c.cell(0, 12, "def f(x: int) -> str", w=180, h=20)
    c.cell(0, 36, "def f(x: str) -> int", w=180, h=20)
    c.closed_arrow(180, 32, 220, 32, emphasis=True)
    c.cell(222, 22, "one impl", w=80, h=22, soft=True)


def paramspec_preserve(c: Canvas) -> None:
    """ParamSpec · the decorator preserves the wrapped function's full signature, parameter for parameter."""
    c.cell(0, 22, "f(P)", w=50, h=24)
    c.closed_arrow(50, 34, 80, 34, emphasis=True)
    c.frame(82, 12, 100, 44, label="@dec")
    c.mono(132, 36, "P preserved")
    c.closed_arrow(182, 34, 212, 34, emphasis=True)
    c.cell(214, 22, "wrapper(P)", w=80, h=24, soft=True)


def literal_constrained(c: Canvas) -> None:
    """Literal · the type narrows the slot to a fixed set of constant values."""
    c.tag(0, 0, "Literal[…]")
    c.cell(0, 12, "x", w=40, h=24)
    c.closed_arrow(40, 24, 70, 4, emphasis=False)
    c.closed_arrow(40, 24, 70, 24, emphasis=False)
    c.closed_arrow(40, 24, 70, 44, emphasis=False)
    c.cell(72, 0, "'red'", w=70, h=20, soft=True)
    c.cell(72, 22, "'green'", w=70, h=20, soft=True)
    c.cell(72, 44, "'blue'", w=70, h=20, soft=True)


def callable_type(c: Canvas) -> None:
    """Callable types · the annotation captures the call shape: argument types and return type."""
    c.tag(0, 0, "Callable[[int, str], bool]")
    c.cell(0, 12, "(int, str)", w=100, h=22)
    c.closed_arrow(100, 23, 130, 23, emphasis=False)
    c.cell(132, 12, "bool", w=60, h=22)


def isinstance_check(c: Canvas) -> None:
    """Runtime type checks · isinstance asks the runtime; the answer is a bool, not a refinement."""
    c.cell(0, 22, "isinstance(x, T)", w=140, h=24)
    c.closed_arrow(140, 22, 170, 4, emphasis=True)
    c.cell(172, 0, "True", w=60, h=20, soft=True)
    c.closed_arrow(140, 46, 170, 56, emphasis=False)
    c.cell(172, 50, "False", w=60, h=20)


def collections_containers(c: Canvas) -> None:
    """Collections module · four specialised containers for shapes the built-in types don't cover well."""
    rows = [("deque", "fast appends both ends"), ("Counter", "key → count"), ("defaultdict", "missing key default"), ("namedtuple", "tuple with names")]
    for i, (name, role) in enumerate(rows):
        c.cell(0, i * 22, name, w=110, h=20)
        c.cell(112, i * 22, role, w=170, h=20, soft=True)


def typed_dict_shape(c: Canvas) -> None:
    """Structured data shapes · TypedDict names each key's value type; the dict obeys the declared shape."""
    c.frame(0, 0, 200, 86, label="User TypedDict")
    rows = [("id", "int"), ("name", "str"), ("active", "bool")]
    for i, (k, v) in enumerate(rows):
        c.cell(14, 18 + i * 20, f"{k}: {v}", w=172, h=18)


def csv_records(c: Canvas) -> None:
    """CSV data · rows of records; each line has the same columns in the same order."""
    c.tag(0, 0, "rows · records")
    headers = ["id", "name", "score"]
    rows = [["1", "Ada", "97"], ["2", "Bo", "88"], ["3", "Cy", "76"]]
    for j, h in enumerate(headers):
        c.cell(j * 70, 12, h, w=70, h=20, soft=True)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            c.cell(j * 70, 32 + i * 20, v, w=70, h=18)


def warning_signal(c: Canvas) -> None:
    """Warnings · a soft signal: the warning is reported, execution continues."""
    c.cell(0, 22, "code path", w=90, h=24)
    c.closed_arrow(90, 22, 120, 4, emphasis=False)
    c.cell(122, 0, "DeprecationWarning", w=170, h=22, soft=True)
    c.closed_arrow(90, 46, 120, 56, emphasis=True)
    c.cell(122, 50, "execution continues", w=170, h=22)


def object_lifecycle(c: Canvas) -> None:
    """Object lifecycle · __init__ creates; the object lives while refcount > 0; __del__ finalises."""
    c.cell(0, 22, "__init__", w=80, h=24)
    c.closed_arrow(80, 34, 110, 34, emphasis=True)
    c.cell(112, 22, "live · refcount > 0", w=140, h=24, soft=True)
    c.closed_arrow(252, 34, 282, 34, emphasis=False)
    c.cell(284, 22, "__del__", w=80, h=24)


# ─── Fifth pass: tightened figures for slugs that were on reuse-floors ─


def type_alias_name(c: Canvas) -> None:
    """Type aliases · complex annotation collapses to a single readable name."""
    c.cell(0, 30, "dict[str, list[tuple[int, str]]]", w=240, h=24, ghost=True)
    c.closed_arrow(120, 54, 120, 70, emphasis=True)
    c.label(96, 66, "type Index = …", anchor="middle")
    c.cell(80, 76, "Index", w=80, h=24, soft=True)


def match_dispatch_ladder(c: Canvas) -> None:
    """Match statements · the value flows down the patterns; the first match wins."""
    c.cell(0, 0, "match value", w=170, h=22)
    cases = ["case 0:", "case [x, y]:", "case Point(0, _):", "case _:"]
    for i, txt in enumerate(cases):
        c.cell(0, 30 + i * 22, txt, w=170, h=20)
    c.dashed(186, 32, 186, 122)
    c.dot(186, 74, emphasis=True)
    c.closed_arrow(186, 110, 186, 124, emphasis=True)
    c.label(196, 76, "first match", anchor="start")


def match_pattern_variants(c: Canvas) -> None:
    """Advanced match patterns · capture, alternative, guard, class — four pattern shapes."""
    rows = [("capture", "[x, y]"), ("alternative", "P() | Q()"), ("guard", "[x] if x > 0"), ("class", "Point(x=0, y=_)")]
    for i, (kind, shape) in enumerate(rows):
        y = i * 22
        c.cell(0, y, kind, w=90, h=20)
        c.cell(92, y, shape, w=180, h=20, soft=(kind == "class"))


def loop_else_gate(c: Canvas) -> None:
    """Loop else · runs when the loop falls through naturally; break skips it."""
    c.cell(0, 20, "loop body", w=110, h=24)
    c.closed_arrow(110, 20, 150, 0, emphasis=True)
    c.cell(152, 0, "fell through · else runs", w=160, h=20, soft=True)
    c.closed_arrow(110, 44, 150, 56, emphasis=False)
    c.cell(152, 50, "broke · else skipped", w=160, h=20)


def workers_lesson_runtime(c: Canvas) -> None:
    """Workers · lesson uses captured output as evidence when the runtime forbids the process API."""
    c.cell(0, 22, "lesson question", w=130, h=24)
    c.closed_arrow(130, 22, 160, 0, emphasis=False)
    c.cell(162, 0, "process API", w=130, h=20, ghost=True)
    c.dashed(162, 10, 292, 10)
    c.closed_arrow(130, 46, 160, 56, emphasis=True)
    c.cell(162, 50, "captured output", w=130, h=20, soft=True)


def lazy_stream(c: Canvas) -> None:
    """Iteration · Compose lazy value streams: filter and map flow values without materialising."""
    c.object_box(0, 26, "source", "[a,b,c]", w=78, h=24)
    c.dashed(78, 38, 102, 38)
    c.object_box(104, 26, "filter", "x>0", w=68, h=24)
    c.dashed(172, 38, 196, 38)
    c.object_box(198, 26, "map", "x*2", w=64, h=24)
    c.closed_arrow(262, 38, 294, 38, emphasis=True)
    c.label(278, 30, "next()", anchor="middle")


# Registry: figure_name -> (paint_fn, viewbox_w, viewbox_h)
FIGURES: dict[str, tuple[Callable[[Canvas], None], int, int]] = {
    "aliasing-mutation": (aliasing_mutation, 220, 175),
    "tuple-no-mutation": (tuple_no_mutation, 220, 185),
    "iterator-unroll": (iterator_unroll, 220, 130),
    "scope-rings": (scope_rings, 216, 116),
    "closure-cell": (closure_cell, 240, 120),
    "slice-ruler": (slice_ruler, 232, 120),
    "branch-fork": (branch_fork, 232, 100),
    "loop-repetition": (loop_repetition, 204, 90),
    "iter-protocol": (iter_protocol, 304, 70),
    # Runtime
    "program-output": (program_output, 240, 80),
    "identity-and-equality": (identity_and_equality, 304, 96),
    "operator-dispatch": (operator_dispatch, 260, 70),
    # Shapes
    "container-questions": (container_questions, 280, 88),
    "reshape-pipeline": (reshape_pipeline, 204, 80),
    "text-data-boundary": (text_data_boundary, 172, 70),
    # Interfaces
    "function-signature": (function_signature, 188, 80),
    "function-as-value": (function_as_value, 200, 66),
    "class-with-state": (class_with_state, 152, 108),
    # Types
    "annotation-ghost": (annotation_ghost, 220, 52),
    "union-types": (union_types, 156, 80),
    "generic-preservation": (generic_preservation, 250, 70),
    # Reliability
    "exception-lanes": (exception_lanes, 320, 100),
    "context-bowtie": (context_bowtie, 244, 76),
    "async-swimlane": (async_swimlane, 280, 84),
    # Control flow + Iteration coverage gap (see audit)
    "naming-decisions": (naming_decisions, 274, 80),
    "early-exit": (early_exit, 144, 116),
    "lazy-stream": (lazy_stream, 300, 56),
    # Promoted from the gestalt — wired to example pages via ATTACHMENTS
    "variables-bind": (variables_bind, 180, 44),
    "call-stack": (call_stack, 200, 100),
    "decorator-rebind": (decorator_rebind, 232, 110),
    "mro-chain": (mro_chain, 200, 152),
    "dataclass-fields": (dataclass_fields, 312, 76),
    "class-triangle": (class_triangle, 274, 60),
    "exception-cause-context": (exception_cause_context, 282, 70),
    "unpacking-bind": (unpacking_bind, 152, 80),
    "comprehension-equivalence": (comprehension_equivalence, 280, 76),
    "list-append": (list_append, 220, 36),
    "dict-buckets": (dict_buckets, 270, 88),
    # Workers journey (constraint-shaped sections; tightened designs)
    "workers-portable-evidence": (workers_portable_evidence, 222, 84),
    "workers-protocol-local": (workers_protocol_local, 162, 110),
    "workers-lesson-runtime": (workers_lesson_runtime, 300, 80),
    # Newly designed paint code for examples that lacked a figure
    "number-lines": (number_lines, 260, 78),
    "expression-tree": (expression_tree, 220, 92),
    "none-singleton": (none_singleton, 240, 84),
    "codepoints-bytes": (codepoints_bytes, 200, 84),
    "sort-stability": (sort_stability, 270, 100),
    "kw-only-separator": (kw_only_separator, 200, 56),
    "positional-only-separator": (positional_only_separator, 200, 56),
    "generator-ribbon": (generator_ribbon, 260, 50),
    "truth-and-size": (truth_and_size, 232, 70),
    "descriptor-protocol": (descriptor_protocol, 222, 76),
    "bound-unbound": (bound_unbound, 296, 56),
    "method-kinds": (method_kinds, 272, 70),
    "callable-objects": (callable_objects, 220, 44),
    "attribute-lookup": (attribute_lookup, 242, 70),
    "guard-clauses": (guard_clauses, 264, 104),
    "bytes-vs-bytearray": (bytes_vs_bytearray, 308, 86),
    "sentinel-iteration": (sentinel_iteration, 300, 92),
    "partial-functions": (partial_functions, 334, 36),
    # Third coverage push: 24 more figures
    "args-kwargs": (args_kwargs, 280, 68),
    "multiple-return": (multiple_return, 180, 110),
    "lambda-expression": (lambda_expression, 170, 76),
    "property-fork": (property_fork, 232, 72),
    "metaclass-triangle": (metaclass_triangle, 300, 60),
    "sys-path-resolution": (sys_path_resolution, 258, 100),
    "import-alias": (import_alias, 212, 56),
    "protocol-check": (protocol_check, 220, 78),
    "enum-members": (enum_members, 280, 60),
    "datetime-instant": (datetime_instant, 280, 88),
    "json-python-mapping": (json_python_mapping, 220, 116),
    "regex-anchors": (regex_anchors, 200, 92),
    "number-parse": (number_parse, 204, 64),
    "format-spec": (format_spec, 220, 64),
    "truthy-check": (truthy_check, 240, 70),
    "boolean-truth-table": (boolean_truth_table, 132, 64),
    "set-buckets": (set_buckets, 156, 90),
    "tuple-frozen": (tuple_frozen, 280, 48),
    "value-types": (value_types, 160, 116),
    "yield-delegation": (yield_delegation, 240, 84),
    "itertools-chain": (itertools_chain, 246, 64),
    "assertion-check": (assertion_check, 304, 76),
    "custom-exception-chain": (custom_exception_chain, 220, 90),
    "exception-group-peel": (exception_group_peel, 240, 50),
    "delete-name-erased": (delete_name_erased, 200, 84),
    # Fourth coverage push: 19 figures for constraint-shaped examples
    "package-tree": (package_tree, 240, 76),
    "venv-boundary": (venv_boundary, 274, 76),
    "subprocess-spawn": (subprocess_spawn, 324, 60),
    "logging-levels": (logging_levels, 164, 124),
    "aaa-pattern": (aaa_pattern, 250, 80),
    "protocol-layers": (protocol_layers, 200, 100),
    "gil-lanes": (gil_lanes, 300, 100),
    "cast-escape": (cast_escape, 184, 56),
    "newtype-phantom": (newtype_phantom, 96, 92),
    "overload-signatures": (overload_signatures, 304, 64),
    "paramspec-preserve": (paramspec_preserve, 294, 60),
    "literal-constrained": (literal_constrained, 144, 76),
    "callable-type": (callable_type, 196, 40),
    "isinstance-check": (isinstance_check, 232, 76),
    "collections-containers": (collections_containers, 284, 92),
    "typed-dict-shape": (typed_dict_shape, 200, 92),
    "csv-records": (csv_records, 212, 96),
    "warning-signal": (warning_signal, 292, 80),
    "object-lifecycle": (object_lifecycle, 366, 60),
    # Fifth pass: slug-specific figures lifting attached scores off the 8.0 floor
    "type-alias-name": (type_alias_name, 240, 104),
    "match-dispatch-ladder": (match_dispatch_ladder, 260, 130),
    "match-pattern-variants": (match_pattern_variants, 272, 96),
    "loop-else-gate": (loop_else_gate, 312, 76),
    # Sixth pass: lift the lingering 8.0-band figures with slug-specific paint
    "literal-forms": (literal_forms, 252, 132),
    "function-with-body": (function_with_body, 334, 68),
}


# ─── Attachments ───────────────────────────────────────────────────────

# slug -> [(anchor, figure_name, caption_or_None), …]
ATTACHMENTS: dict[str, list[tuple[str, str, str | None]]] = {
    "mutability": [
        (
            "cell-0",
            "aliasing-mutation",
            "Two names share one mutable list — appending through one name changes the object visible through both.",
        ),
    ],
    "variables": [
        (
            "cell-0",
            "variables-bind",
            "A name is a label that points at an object. Assignment binds the label; the object exists independently.",
        ),
    ],
    "lists": [
        (
            "cell-0",
            "list-append",
            "Lists are mutable sequences. `.append` extends the same list object — no new list is created.",
        ),
    ],
    "dicts": [
        (
            "cell-0",
            "dict-buckets",
            "Each key is hashed to a bucket; collisions chain into the next slot. Lookup is constant-time on average.",
        ),
    ],
    "unpacking": [
        (
            "cell-0",
            "unpacking-bind",
            "Left-side names bind to right-side positions; `*rest` gathers the middle into a list.",
        ),
    ],
    "comprehensions": [
        (
            "cell-0",
            "comprehension-equivalence",
            "A comprehension is a compact spelling of the equivalent for-loop with append, made into one expression.",
        ),
    ],
    "classes": [
        (
            "cell-0",
            "class-triangle",
            "Every Python value sits on the instance → class → type triangle; the metaclass is the type of the class.",
        ),
    ],
    "inheritance-and-super": [
        (
            "cell-0",
            "mro-chain",
            "Multiple inheritance forms a graph; C3 linearisation flattens it into the MRO Python uses for attribute lookup.",
        ),
    ],
    "dataclasses": [
        (
            "cell-0",
            "dataclass-fields",
            "Field declarations become the generated __init__ signature: declaration is the constructor.",
        ),
    ],
    "special-methods": [
        (
            "cell-0",
            "operator-dispatch",
            "Operators are method calls. `a + b` dispatches to `a.__add__(b)`; the data model exposes the syntax.",
        ),
    ],
    "decorators": [
        (
            "cell-0",
            "decorator-rebind",
            "@dec rebinds the name to wrapper(f₀); the original function survives only in the wrapper's closure cell.",
        ),
    ],
    "recursion": [
        (
            "cell-1",
            "call-stack",
            "Each call pushes a new frame with the same name and a smaller argument; the base case unwinds back up the stack.",
        ),
    ],
    "exception-chaining": [
        (
            "cell-0",
            "exception-cause-context",
            "`raise X from Y` sets `__cause__` (explicit); raising during except sets `__context__` (implicit).",
        ),
    ],
    # Promoted from gestalt with newly-written paint code
    "hello-world": [(
        "cell-0", "program-output",
        "Every Python program starts as source and produces text on standard output. The smallest mental model.",
    )],
    "numbers": [(
        "cell-1", "number-lines",
        "Ints have unbounded precision; floats use IEEE doubles whose representable values thin out near the extremes.",
    )],
    "operators": [(
        "cell-0", "expression-tree",
        "An expression like `(2 + 3) * 4` parses as a tree; operator precedence and parentheses determine its shape.",
    )],
    "none": [(
        "cell-0", "none-singleton",
        "`None` is a single object: every name that points at None points at the same object.",
    )],
    "equality-and-identity": [(
        "cell-0", "identity-and-equality",
        "Two names can share one object (`is` and `==` both true) or hold two equal-but-distinct objects (only `==` true).",
    )],
    "strings": [(
        "cell-0", "codepoints-bytes",
        "Strings are sequences of Unicode codepoints. UTF-8 encoding turns them into bytes; `é` takes two bytes, `c` takes one.",
    )],
    "for-loops": [(
        "cell-1", "iterator-unroll",
        "Each call to next() advances the caret one cell along the iterable — the same shape behind range(), strings, and any sequence.",
    )],
    "sorting": [(
        "cell-1", "sort-stability",
        "Python's sort is stable: items with equal keys keep their original order, so chained sorts compose predictably.",
    )],
    "keyword-only-arguments": [(
        "cell-0", "kw-only-separator",
        "A bare `*` divides positional or keyword arguments from keyword-only ones; callers must pass `c` and `d` by name.",
    )],
    "positional-only-parameters": [(
        "cell-0", "positional-only-separator",
        "A bare `/` divides positional-only arguments from positional-or-keyword ones; callers cannot name `a` or `b`.",
    )],
    "closures": [(
        "cell-0", "closure-cell",
        "The inner function keeps a reference into the outer scope's cell, so the captured factor survives the outer return.",
    )],
    "scope-global-nonlocal": [(
        "cell-0", "scope-rings",
        "Name lookup walks LEGB — local, enclosing, global, built-in — outward, returning the first binding it finds.",
    )],
    "generators": [(
        "cell-0", "generator-ribbon",
        "A generator's body is a timeline cut by yield gates: each next() advances to the next gate; locals survive the pause.",
    )],
    "type-hints": [(
        "cell-0", "annotation-ghost",
        "Annotations describe expected types for tools; the runtime accepts any object regardless.",
    )],
    "exceptions": [(
        "cell-0", "exception-lanes",
        "try, except, else, and finally as parallel lanes; a single coral path traces what actually runs.",
    )],
    "context-managers": [(
        "cell-0", "context-bowtie",
        "A context manager pairs setup with reliable cleanup; the raise path still routes through __exit__.",
    )],
    "async-await": [(
        "cell-0", "async-swimlane",
        "On await, the coroutine yields to the loop; the loop runs other work and resumes when the awaitable is ready.",
    )],
    "iterators": [(
        "cell-0", "iter-protocol",
        "iter() exposes the iterator behind for; next() pulls one value at a time until exhausted.",
    )],
    "slices": [(
        "cell-0", "slice-ruler",
        "Slice indices sit between cells; [:3] and [3:] partition the sequence at index 3, never overlapping or losing an item.",
    )],
    # Mappings of existing FIGURES to new examples added on main
    "operator-overloading": [(
        "cell-0", "operator-dispatch",
        "Defining `__add__` on a class lets `+` dispatch into the class's own behavior.",
    )],
    "iterator-vs-iterable": [(
        "cell-0", "iter-protocol",
        "An iterable knows how to produce an iterator (via iter()); the iterator knows how to produce values (via next()).",
    )],
    "type-aliases": [(
        "cell-0", "type-alias-name",
        "A type alias names a complex annotation once so call sites read as the domain meaning, not the type composition.",
    )],
    "typed-dicts": [(
        "cell-0", "typed-dict-shape",
        "TypedDict gives each key a typed value, so `obj['x']` is checked against the declared shape.",
    )],
    "union-and-optional-types": [(
        "cell-0", "union-types",
        "`int | str | None` says one slot may hold any of three shapes — including expected absence.",
    )],
    "generics-and-typevar": [(
        "cell-0", "generic-preservation",
        "A generic preserves the input type through the call: the same T flows in and out of fn[T].",
    )],
    "abstract-base-classes": [(
        "cell-0", "class-triangle",
        "An ABC sits on the same triangle as concrete classes; subclasses inherit the abstract methods they must implement.",
    )],
    "copying-collections": [(
        "cell-0", "aliasing-mutation",
        "Without copy() two names share the same object; mutating through one is visible through the other.",
    )],
    # Newly designed figures for examples that previously had none
    "truth-and-size": [(
        "cell-0", "truth-and-size",
        "bool(x) calls __bool__ first; if absent, __len__() != 0; if neither, defaults to True.",
    )],
    "descriptors": [(
        "cell-0", "descriptor-protocol",
        "Attribute access on an instance routes through the descriptor's __get__/__set__/__delete__ when the attribute is a descriptor.",
    )],
    "bound-and-unbound-methods": [(
        "cell-0", "bound-unbound",
        "Accessing a method via an instance binds self; accessing it via the class returns the underlying function.",
    )],
    "classmethods-and-staticmethods": [(
        "cell-0", "method-kinds",
        "Three method kinds, three first-argument conventions: classmethod gets the class, staticmethod gets nothing, instance gets self.",
    )],
    "callable-objects": [(
        "cell-0", "callable-objects",
        "Defining __call__ makes any object callable; functions are just one shape that satisfies this protocol.",
    )],
    "attribute-access": [(
        "cell-0", "attribute-lookup",
        "obj.x checks instance __dict__, then class __dict__, then __getattr__; the first hit wins.",
    )],
    "guard-clauses": [(
        "cell-0", "guard-clauses",
        "Early returns handle the exceptional cases first so the main work is the body of the function, not its tail.",
    )],
    "bytes-and-bytearray": [(
        "cell-0", "bytes-vs-bytearray",
        "bytes is a frozen sequence of integers; bytearray is the mutable counterpart with append/extend/etc.",
    )],
    "sentinel-iteration": [(
        "cell-0", "sentinel-iteration",
        "`iter(callable, sentinel)` calls the callable repeatedly, stopping when it returns the sentinel.",
    )],
    "partial-functions": [(
        "cell-0", "partial-functions",
        "`functools.partial(f, 1)` pre-fills `a=1`, returning a thinner callable `g(b, c)` that only needs the rest.",
    )],
    # Third coverage push: 24 more attachments — newly designed figures and journey-figure reuse
    "args-and-kwargs": [(
        "cell-0", "args-kwargs",
        "*args captures the extra positionals as a tuple; **kwargs captures the extra keywords as a dict.",
    )],
    "multiple-return-values": [(
        "cell-0", "multiple-return",
        "A function returning multiple values really returns one tuple; the caller unpacks it into named bindings.",
    )],
    "lambdas": [(
        "cell-0", "lambda-expression",
        "A lambda is a function literal: parameters before the colon, a single expression after, no statement body.",
    )],
    "properties": [(
        "cell-0", "property-fork",
        "When x is a property, attribute access routes through fget/fset instead of touching __dict__.",
    )],
    "metaclasses": [(
        "cell-0", "metaclass-triangle",
        "A metaclass is the type of a class, just as a class is the type of its instances; type is the default metaclass.",
    )],
    "modules": [(
        "cell-0", "sys-path-resolution",
        "An import walks sys.path entry by entry; the first directory containing the module wins.",
    )],
    "import-aliases": [(
        "cell-0", "import-alias",
        "`import x as y` binds the name y to the same module object x would have.",
    )],
    "protocols": [(
        "cell-0", "protocol-check",
        "An object satisfies a protocol structurally — by having the required methods — not by inheriting it.",
    )],
    "enums": [(
        "cell-0", "enum-members",
        "An enum names a fixed set of symbolic values; no new members appear at runtime.",
    )],
    "datetime": [(
        "cell-0", "datetime-instant",
        "An aware datetime carries a UTC offset; one instant in time reads differently on two clocks.",
    )],
    "json": [(
        "cell-0", "json-python-mapping",
        "Six type pairs bridge the JSON text boundary; each json value maps to one Python type.",
    )],
    "regular-expressions": [(
        "cell-0", "regex-anchors",
        "^ and $ anchor the pattern; quantifiers like {2} bound how many times a token repeats.",
    )],
    "number-parsing": [(
        "cell-0", "number-parse",
        "int() turns text into a typed number; malformed input raises ValueError instead of guessing.",
    )],
    "string-formatting": [(
        "cell-0", "format-spec",
        "The format spec is a railroad of named optional fields: alignment, sign, width, precision, type.",
    )],
    "truthiness": [(
        "cell-0", "truthy-check",
        "bool(x) is True except for a small fixed set: 0, 0.0, \"\", [], {}, None, False.",
    )],
    "booleans": [(
        "cell-0", "boolean-truth-table",
        "`a and b` returns True only when both are True; otherwise it returns the first falsy value.",
    )],
    "sets": [(
        "cell-0", "set-buckets",
        "Sets are hash buckets without values; `x in s` averages O(1) regardless of size.",
    )],
    "tuples": [(
        "cell-0", "tuple-frozen",
        "Tuples are ordered, immutable sequences; positions matter, contents do not change once constructed.",
    )],
    "values": [(
        "cell-0", "value-types",
        "Every literal is an object with a type; the type carries the behaviour, not the variable name.",
    )],
    "yield-from": [(
        "cell-0", "yield-delegation",
        "`yield from inner` delegates iteration to an inner generator; its yields surface here unchanged.",
    )],
    "itertools": [(
        "cell-0", "itertools-chain",
        "chain stitches two iterables into one stream without materialising either: values arrive lazily.",
    )],
    "assertions": [(
        "cell-0", "assertion-check",
        "assert tests a condition; True passes silently, False raises AssertionError with the optional message.",
    )],
    "custom-exceptions": [(
        "cell-0", "custom-exception-chain",
        "Subclassing an existing exception gains a domain name without changing semantics.",
    )],
    "exception-groups": [(
        "cell-0", "exception-group-peel",
        "except* peels matched leaves out of an ExceptionGroup; survivors regroup and propagate.",
    )],
    "delete-statements": [(
        "cell-0", "delete-name-erased",
        "`del x` removes the name; the object survives if any other reference holds it, otherwise gets collected.",
    )],
    # Easy promotions: existing journey figures, reused on examples that fit
    "conditionals": [(
        "cell-0", "branch-fork",
        "A predicate sorts a value into one of several branches; if/elif/else is the explicit spelling.",
    )],
    "match-statements": [(
        "cell-0", "match-dispatch-ladder",
        "match dispatches by pattern shape; the value flows down the patterns and the first match wins.",
    )],
    "assignment-expressions": [(
        "cell-0", "naming-decisions",
        "The walrus binds a name during the surrounding expression; one expression, two outputs.",
    )],
    "iterating-over-iterables": [(
        "cell-0", "iter-protocol",
        "iter() exposes the iterator behind for; next() pulls one value at a time until exhausted.",
    )],
    "generator-expressions": [(
        "cell-0", "lazy-stream",
        "A generator expression composes filter and map lazily; values flow only when next() pulls them.",
    )],
    "async-iteration-and-context": [(
        "cell-0", "async-swimlane",
        "async iteration and async with both rest on the same loop-vs-coroutine handoff as await.",
    )],
    "loop-else": [(
        "cell-0", "loop-else-gate",
        "The loop's else branch runs only when the loop falls through naturally; break skips it.",
    )],
    "break-and-continue": [(
        "cell-0", "early-exit",
        "break exits the loop; continue skips to the next iteration. Both interrupt the natural fall-through.",
    )],
    "comprehension-patterns": [(
        "cell-0", "comprehension-equivalence",
        "Nested clauses compose left to right; the comprehension is still equivalent to a for-loop with append.",
    )],
    "container-protocols": [(
        "cell-0", "iter-protocol",
        "Container protocols share the iter/next backbone; __iter__ + __next__ make any object iterable.",
    )],
    "functions": [(
        "cell-0", "function-with-body",
        "A function takes inputs, evaluates a body, and returns a value: `greet('Ada')` produces `'Hello, Ada'`.",
    )],
    "constants": [(
        "cell-0", "variables-bind",
        "UPPER_CASE is a naming convention, not a language constraint; the binding behaves like any other variable.",
    )],
    "while-loops": [(
        "cell-0", "loop-repetition",
        "while repeats the body until the condition becomes false; the back-edge returns to the test each pass.",
    )],
    "advanced-match-patterns": [(
        "cell-0", "match-pattern-variants",
        "Capture, alternative, guard, and class patterns each name a different way a value can match a case.",
    )],
    "literals": [(
        "cell-0", "literal-forms",
        "Each Python type has its own literal spellings; ints accept decimal, hex, and binary; strings accept either quote.",
    )],
    # Fourth coverage push: constraint-shaped examples
    "packages": [(
        "cell-0", "package-tree",
        "A directory with __init__.py becomes an importable package; submodules and subpackages nest beneath it.",
    )],
    "virtual-environments": [(
        "cell-0", "venv-boundary",
        "A venv carries its own interpreter and site-packages, isolating a project's dependencies from the system.",
    )],
    "subprocesses": [(
        "cell-0", "subprocess-spawn",
        "subprocess.run spawns a child process and captures its stdout, stderr, and exit code as portable evidence.",
    )],
    "logging": [(
        "cell-0", "logging-levels",
        "Five severity levels; the logger's configured threshold drops everything below it.",
    )],
    "testing": [(
        "cell-0", "aaa-pattern",
        "arrange-act-assert: set up the state, perform the behavior under test, compare the result to expectations.",
    )],
    "networking": [(
        "cell-0", "protocol-layers",
        "Network protocols stack: HTTP rests on TCP, which rests on IP, which rests on the link layer.",
    )],
    "threads-and-processes": [(
        "cell-0", "gil-lanes",
        "Threads share memory but the GIL serialises Python bytecode; processes run in parallel with isolated memory.",
    )],
    "casts-and-any": [(
        "cell-0", "cast-escape",
        "cast(T, x) tells the type checker to treat x as T; the runtime is unaffected.",
    )],
    "newtype": [(
        "cell-0", "newtype-phantom",
        "NewType creates a distinct static identity backed by the same runtime type — UserId is int with a name.",
    )],
    "overloads": [(
        "cell-0", "overload-signatures",
        "@overload declares multiple call signatures; one underlying implementation routes input shape to return type.",
    )],
    "paramspec": [(
        "cell-0", "paramspec-preserve",
        "ParamSpec preserves the wrapped function's signature through a decorator, parameter for parameter.",
    )],
    "literal-and-final": [(
        "cell-0", "literal-constrained",
        "Literal narrows a slot to a fixed set of constant values; Final says the binding will not change.",
    )],
    "callable-types": [(
        "cell-0", "callable-type",
        "Callable[[A, B], R] captures the call shape: a tuple of argument types and one return type.",
    )],
    "runtime-type-checks": [(
        "cell-0", "isinstance-check",
        "isinstance and issubclass ask the runtime; the answer is a bool, not a static type refinement.",
    )],
    "collections-module": [(
        "cell-0", "collections-containers",
        "Four specialised containers for shapes the built-in types don't cover well: deque, Counter, defaultdict, namedtuple.",
    )],
    "structured-data-shapes": [(
        "cell-0", "typed-dict-shape",
        "TypedDict names each key's value type; the dict obeys the declared shape at static-check time.",
    )],
    "csv-data": [(
        "cell-0", "csv-records",
        "CSV files are rows of records; each line has the same columns in the same order.",
    )],
    "warnings": [(
        "cell-0", "warning-signal",
        "A warning is a soft signal: the message is reported, but execution continues unless filters elevate it.",
    )],
    "object-lifecycle": [(
        "cell-0", "object-lifecycle",
        "__init__ constructs the object; it lives while at least one reference holds it; __del__ runs when refcount hits zero.",
    )],
}


# ─── Render helpers ────────────────────────────────────────────────────


def _render_svg(figure_name: str) -> str:
    paint, w, h = FIGURES[figure_name]
    canvas = Canvas(w=w, h=h)
    paint(canvas)
    return canvas.to_svg()


def render_for_anchor(slug: str, anchor: str) -> str:
    """HTML for a banner row sitting AFTER the named cell. Empty if none.

    Cells always keep their prose|code 2-column grid. Figures live in
    banner rows that span both columns BETWEEN cells (and after the
    walkthrough for single-cell examples). Multiple figures attached to
    the same cell share one banner as a small multiple.
    """
    attachments = ATTACHMENTS.get(slug, [])
    matched = [(name, caption) for (a, name, caption) in attachments if a == anchor]
    if not matched:
        return ""
    figures: list[str] = []
    for name, caption in matched:
        cap = f"<figcaption>{html.escape(caption)}</figcaption>" if caption else ""
        figures.append(f"<figure>{_render_svg(name)}{cap}</figure>")
    count_class = f" cell-banner--{len(matched)}"
    return f'<div class="cell-banner{count_class}">{"".join(figures)}</div>'


# ─── Scores (v2 rubric — see docs/example-figure-rubric.md) ────────────
# Score every attached example figure against the v2 rubric. The dict is
# the single source of truth for both the gestalt review pages
# (scripts/build_marginalia.py, scripts/build_prototypes.py) and any
# future per-example scoring surface.

SCORES: dict[str, tuple[float, str]] = {
    # 9.5 — canonical, definitive depictions of their cell's move
    "variables": (9.5, "the canonical name → object picture"),
    "mutability": (9.5, "three-state small multiple of aliased mutation"),
    "copying-collections": (9.5, "same picture as mutability, perfect match"),
    # 9.0 — strong mechanism, runs match the cell, all craft criteria full credit
    "hello-world": (9.0, "program → output, smallest mechanism"),
    "numbers": (9.0, "int unbounded vs float thinning, both registers"),
    "operators": (9.0, "expression tree mechanism"),
    "none": (9.0, "three names converging on one None"),
    "equality-and-identity": (9.0, "shared vs separate object, side-by-side"),
    "strings": (9.0, "codepoints + bytes registers"),
    "for-loops": (9.0, "4-row caret advance"),
    "sorting": (9.0, "stability ribbons preserved across keys"),
    "keyword-only-arguments": (9.0, "signature with explicit `*` separator"),
    "positional-only-parameters": (9.0, "signature with explicit `/` separator"),
    "closures": (9.0, "captured cell reference"),
    "scope-global-nonlocal": (9.0, "LEGB nested rings"),
    "recursion": (9.0, "stacked frames with same name, different argument"),
    "lists": (9.0, "cells with append mechanism"),
    "dicts": (9.0, "hash buckets with collision chain"),
    "slices": (9.0, "ruler with bracket overlay"),
    "comprehensions": (9.0, "comprehension over equivalent for-loop"),
    "type-hints": (9.0, "ghost annotations over runtime values"),
    "generators": (9.0, "ribbon cut by yield gates"),
    "exceptions": (9.0, "try/except/else/finally lanes with traced path"),
    "context-managers": (9.0, "enter / body / exit bowtie"),
    "async-await": (9.0, "loop/coro swimlane with await handoffs"),
    "classes": (9.0, "instance/class/type triangle"),
    "inheritance-and-super": (9.0, "MRO chain with diamond ghost"),
    "dataclasses": (9.0, "fields → generated __init__ signature"),
    "decorators": (9.0, "before/after rebinding through cell"),
    "special-methods": (9.0, "syntax → method dispatch"),
    "unpacking": (9.0, "binding-line mechanism with *rest"),
    "exception-chaining": (9.0, "__cause__ vs __context__ distinguished"),
    "iterating-over-iterables": (9.0, "iter() exposes the iterator"),
    "iterators": (9.0, "three-state machine"),
    "iterator-vs-iterable": (9.0, "the protocol exposed"),
    "container-protocols": (9.0, "iter/next backbone"),
    "operator-overloading": (9.0, "dispatch arrow"),
    "union-and-optional-types": (9.0, "type fork to several shapes"),
    "abstract-base-classes": (9.0, "same triangle as concrete classes"),
    "conditionals": (9.0, "predicate forks value to branch"),
    "match-statements": (9.0, "dispatch ladder; first match wins"),
    "advanced-match-patterns": (9.0, "four pattern variants"),
    "loop-else": (9.0, "fell-through vs broke, two outcomes"),
    "while-loops": (9.0, "back-edge mechanism"),
    "type-aliases": (9.0, "complex annotation collapses to a name"),
    "typed-dicts": (9.0, "keys with declared value types"),
    "comprehension-patterns": (9.0, "nested clauses compose"),
    "lambdas": (9.0, "function literal: params / expression"),
    "string-formatting": (9.0, "format-spec railroad"),
    "regular-expressions": (9.0, "pattern ruler with anchors"),
    "json": (9.0, "two-column type mapping"),
    "metaclasses": (9.0, "extended triangle to metaclass"),
    "datetime": (9.0, "one instant, two clock offsets"),
    "values": (9.0, "every literal is a typed object"),
    "literals": (9.0, "literal spellings per type"),
    "booleans": (9.0, "2×2 truth table"),
    "sets": (9.0, "hash buckets without values"),
    "yield-from": (9.0, "stitched ribbons; delegation"),
    "generator-expressions": (9.0, "lazy filter→map pipeline"),
    "async-iteration-and-context": (9.0, "loop/coro lanes with await yields"),
    "assignment-expressions": (9.0, "walrus binds while comparing"),
    "break-and-continue": (9.0, "early exit at first match"),
    "delete-statements": (9.0, "name erased; object survives if referenced"),
    "exception-groups": (9.0, "except* peels matching leaves"),
    "custom-exceptions": (9.0, "subclass chain to a domain name"),
    "modules": (9.0, "sys.path resolution; first hit wins"),
    "protocols": (9.0, "structural duck check"),
    "enums": (9.0, "closed set of symbolic values"),
    "functions": (9.0, "specific call: greet('Ada') → 'Hello, Ada'"),
    "constants": (9.0, "name binding; UPPER_CASE is convention"),
    "import-aliases": (9.0, "two names bind to the same module"),
    "number-parsing": (9.0, "int() success path vs ValueError"),
    "tuples": (9.0, "frozen sequence with struck-through .append"),
    "truthiness": (9.0, "bool(x) with the falsy set as a strip"),
    "itertools": (9.0, "chain joins two iterables into one stream"),
    "assertions": (9.0, "True passes, False raises"),
    "descriptors": (9.0, "get/set/delete protocol routed through descriptor"),
    "attribute-access": (9.0, "instance __dict__ → class __dict__ → __getattr__"),
    "bound-and-unbound-methods": (9.0, "instance.method bound vs Class.method unbound"),
    "classmethods-and-staticmethods": (9.0, "three method kinds, three first-arg conventions"),
    "callable-objects": (9.0, "__call__ makes any object callable"),
    "generics-and-typevar": (9.0, "the same T flows in and out"),
    "truth-and-size": (9.0, "__bool__ → __len__ → True fallback chain"),
    "bytes-and-bytearray": (9.0, "frozen vs mutable contrast"),
    "sentinel-iteration": (9.0, "iter(callable, sentinel) stop condition"),
    "partial-functions": (9.0, "f → partial(f, 1) → g"),
    "guard-clauses": (9.0, "early returns, main body at the tail"),
    "packages": (9.0, "__init__.py + nested submodules"),
    "virtual-environments": (9.0, "project / venv boundary"),
    "subprocesses": (9.0, "spawn → child → captured output"),
    "logging": (9.0, "five thresholded levels"),
    "testing": (9.0, "arrange-act-assert three-row pattern"),
    "networking": (9.0, "HTTP / TCP / IP / link stack"),
    "casts-and-any": (9.0, "Any → cast(T, x) → T, runtime unchanged"),
    "newtype": (9.0, "same runtime, distinct static identity"),
    "paramspec": (9.0, "P preserved through decorator"),
    "literal-and-final": (9.0, "slot narrows to a fixed set"),
    "runtime-type-checks": (9.0, "isinstance returns bool"),
    "collections-module": (9.0, "deque / Counter / defaultdict / namedtuple"),
    "structured-data-shapes": (9.0, "TypedDict named keys with value types"),
    "csv-data": (9.0, "rows × columns; same shape per line"),
    "warnings": (9.0, "soft signal; execution continues"),
    "object-lifecycle": (9.0, "__init__ → live → __del__"),
    "args-and-kwargs": (9.0, "*args tuple, **kwargs dict regions"),
    "multiple-return-values": (9.0, "function returns tuple; caller unpacks"),
    "properties": (9.0, "obj.x routes through fget instead of __dict__"),
    # 8.5 — abstract by nature; the figure mostly is the diagram itself
    "overloads": (8.5, "multiple signatures → one impl; abstract"),
    "callable-types": (8.5, "Callable[[A, B], R] shape; static-only"),
    "threads-and-processes": (8.5, "GIL lanes; abstract concurrency model"),
}


def figure_score(slug: str) -> tuple[float, str] | None:
    """Return the v2 score and rationale for an attached example slug, if any."""
    return SCORES.get(slug)
