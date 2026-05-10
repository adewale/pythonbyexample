+++
slug = "type-hints"
title = "Type Hints"
section = "Types"
summary = "Annotations document expected types and power static analysis."
doc_path = "/library/typing.html"
see_also = [
  "union-and-optional-types",
  "type-aliases",
  "generics-and-typevar",
  "runtime-type-checks",
]
+++

Type hints are annotations that document expected shapes for values, parameters, and return results. They exist so tools and readers can understand API boundaries before the program runs.

Python stores many annotations but does not enforce most of them at runtime. Use type hints for communication and static analysis; use validation or exceptions when runtime checks are required.

The alternative to an annotation is prose, tests, or runtime validation. Good Python code often uses all three at important boundaries.

:::program
```python
from typing import TypeAlias

def total(numbers: list[int]) -> int:
    return sum(numbers)

print(total([1, 2, 3]))
print(total.__annotations__)


def label(score: int) -> str:
    return f"score={score}"

print(label("high"))


def find(name: str, options: list[str]) -> str | None:
    return name if name in options else None

print(find("Ada", ["Ada", "Grace"]))
print(find("Guido", ["Ada", "Grace"]))


from typing import Optional

def lookup(name: str) -> Optional[int]:
    table = {"Ada": 1815, "Grace": 1906}
    return table.get(name)

print(lookup("Ada"))
print(lookup("Guido"))


Score: TypeAlias = int

def grade(score: Score) -> str:
    return "pass" if score >= 50 else "fail"

print(grade(72))
```
:::

:::cell
Type hints document expected parameter and return shapes. Python still runs the function normally at runtime.

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

print(total([1, 2, 3]))
```

```output
6
```
:::

:::cell
Python stores annotations on the function object for tools and introspection. Type checkers use this information without changing the function call syntax.

```python
print(total.__annotations__)
```

```output
{'numbers': list[int], 'return': <class 'int'>}
```
:::

:::cell
Most hints are not runtime validation. This call passes a string where the hint says `int`; Python still calls the function because the body can format any value.

```python
def label(score: int) -> str:
    return f"score={score}"

print(label("high"))
```

```output
score=high
```
:::

:::cell
Use `X | Y` (PEP 604) to express "either type". `str | None` says the result is a string or absent. `typing.Optional[X]` is the older, still-supported spelling for the same idea — `Optional[X]` is equivalent to `X | None`.

```python
def find(name: str, options: list[str]) -> str | None:
    return name if name in options else None

print(find("Ada", ["Ada", "Grace"]))
print(find("Guido", ["Ada", "Grace"]))


from typing import Optional

def lookup(name: str) -> Optional[int]:
    table = {"Ada": 1815, "Grace": 1906}
    return table.get(name)

print(lookup("Ada"))
print(lookup("Guido"))
```

```output
Ada
None
1815
None
```
:::

:::cell
`TypeAlias` names a type so it can be reused with intent. `Score: TypeAlias = int` keeps the underlying type at runtime but lets the API talk about a domain concept rather than a primitive.

```python
from typing import TypeAlias

Score: TypeAlias = int

def grade(score: Score) -> str:
    return "pass" if score >= 50 else "fail"

print(grade(72))
```

```output
pass
```
:::

:::note
- Python does not enforce most type hints at runtime.
- Tools like type checkers and editors use annotations to catch mistakes earlier.
- Use `X | Y` for unions and `Optional[X]` for "X or None"; both spellings mean the same thing.
- Reach for `TypeAlias` when a domain name reads better than a raw primitive type.
- Use runtime validation when untrusted input must be rejected while the program runs.
:::
