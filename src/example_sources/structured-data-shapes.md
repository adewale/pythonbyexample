+++
slug = "structured-data-shapes"
title = "Structured Data Shapes"
section = "Classes"
summary = "dataclass, NamedTuple, and TypedDict each model records with different trade-offs."
doc_path = "/library/dataclasses.html"
see_also = [
  "dataclasses",
  "typed-dicts",
  "tuples",
  "classes",
]
+++

`@dataclass`, `typing.NamedTuple`, and `typing.TypedDict` are three ways to give a record a name and a schema. They model the same data but differ in mutability, access syntax, and what the type information costs at runtime.

A dataclass is a regular class with `__init__` and `__repr__` generated for you, so instances are mutable and attribute-accessed. A `NamedTuple` is a tuple subclass with named positions, so instances are immutable and support both `obj.field` and `obj[index]`. A `TypedDict` is a plain dict at runtime; the schema lives only in the type checker.

Pick the shape that matches the problem: a dataclass when methods or mutability help; a `NamedTuple` for small immutable records that benefit from unpacking; a `TypedDict` for JSON-shaped data that should stay as a dict at the boundary.

:::program
```python
from dataclasses import dataclass
from typing import NamedTuple, TypedDict

@dataclass
class UserClass:
    name: str
    score: int

class UserTuple(NamedTuple):
    name: str
    score: int

class UserDict(TypedDict):
    name: str
    score: int

a = UserClass("Ada", 98)
print(a)
a.score = 100
print(a.score)

b = UserTuple("Ada", 98)
print(b)
print(b.name, b[1])
print(b._replace(score=100))

c: UserDict = {"name": "Ada", "score": 98}
print(c)
print(c["name"])
print(type(c).__name__)

print(isinstance(a, UserClass))
print(isinstance(b, tuple))
print(isinstance(c, dict))
```
:::

:::cell
A dataclass is a normal class with `__init__` and `__repr__` generated from the annotated fields. Instances are mutable, support attribute access, and can carry methods like any other class.

```python
from dataclasses import dataclass

@dataclass
class UserClass:
    name: str
    score: int

a = UserClass("Ada", 98)
print(a)
a.score = 100
print(a.score)
```

```output
UserClass(name='Ada', score=98)
100
```
:::

:::cell
A `NamedTuple` is a tuple subclass with named positions. Instances are immutable, support both `obj.field` and `obj[index]`, and the helper `_replace` produces a modified copy without mutating the original (since assigning to a field would fail).

```python
from typing import NamedTuple

class UserTuple(NamedTuple):
    name: str
    score: int

b = UserTuple("Ada", 98)
print(b)
print(b.name, b[1])
print(b._replace(score=100))
```

```output
UserTuple(name='Ada', score=98)
Ada 98
UserTuple(name='Ada', score=100)
```
:::

:::cell
A `TypedDict` is a plain dictionary at runtime. The annotations exist only for the type checker, so the value behaves like any `dict` — useful for JSON-shaped data that crosses an API boundary as a mapping.

```python
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    score: int

c: UserDict = {"name": "Ada", "score": 98}
print(c)
print(c["name"])
print(type(c).__name__)
```

```output
{'name': 'Ada', 'score': 98}
Ada
dict
```
:::

:::cell
Same record, three runtime identities. The dataclass is its own class. The `NamedTuple` is literally a tuple. The `TypedDict` is literally a dict. That difference drives the choice: pick the form whose runtime behavior matches what the rest of the program already expects.

```python
print(isinstance(a, UserClass))
print(isinstance(b, tuple))
print(isinstance(c, dict))
```

```output
True
True
True
```
:::

:::note
- `@dataclass` — mutable, attribute access, methods; good default when behavior travels with data.
- `typing.NamedTuple` — immutable, attribute + index access, tuple semantics; good for small records that flow through unpacking.
- `typing.TypedDict` — runtime is `dict`, schema is type-checker-only; good for JSON-shaped data.
- `collections.namedtuple` is the older, untyped form of `NamedTuple`; prefer the `typing` version in new code.
:::
