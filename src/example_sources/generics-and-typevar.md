+++
slug = "generics-and-typevar"
title = "Generics and TypeVar"
section = "Types"
summary = "Generics preserve type information across reusable functions and classes."
doc_path = "/library/typing.html#generics"
see_also = [
  "type-hints",
  "collections-module",
  "casts-and-any",
]
+++

Generics connect types across an API. A plain function that returns `object` loses information; a generic function can say that the returned value has the same type as the input element.

A `TypeVar` stands for a type chosen by the caller. In `list[T] -> T`, the same `T` says that a list of strings produces a string and a list of integers produces an integer.

Use generics when a function or class is reusable but still preserves a relationship between input and output types.

:::program
```python
from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]


def pair(left: T, right: T) -> tuple[T, T]:
    return (left, right)

print(first([1, 2, 3]))
print(first(["Ada", "Grace"]))
print(pair("x", "y"))
print(T.__name__)
```
:::

:::cell
A `TypeVar` stands for a type chosen by the caller. The return type follows the list element type.

```python
from typing import TypeVar

T = TypeVar("T")


def first(items: list[T]) -> T:
    return items[0]

print(first([1, 2, 3]))
print(first(["Ada", "Grace"]))
```

```output
1
Ada
```
:::

:::cell
Reusing the same `TypeVar` expresses a relationship between parameters and results.

```python
def pair(left: T, right: T) -> tuple[T, T]:
    return (left, right)

print(pair("x", "y"))
```

```output
('x', 'y')
```
:::

:::cell
`TypeVar` is visible at runtime, but the relationship is mainly for type checkers.

```python
print(T.__name__)
print(first.__annotations__)
```

```output
T
{'items': list[~T], 'return': ~T}
```
:::

:::note
- A `TypeVar` stands for a type chosen by the caller.
- Python 3.12+ also accepts the inline PEP 695 spelling `def first[T](items: list[T]) -> T`, which declares the variable without a separate `TypeVar` line; the explicit form shown here works everywhere and reads the same way.
- Generic functions avoid losing information to `object` or `Any`.
- Use generics when input and output types are connected.
:::
