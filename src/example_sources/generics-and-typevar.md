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
min_python = "3.13"
version_notes = "Type parameter syntax needs Python 3.12; type parameter defaults and __default__ need Python 3.13."
+++

Generics connect types across an API. A plain function that returns `object` loses information; a generic function can say that the returned value has the same type as the input element.

A type parameter stands for a type chosen by the caller. In `def first[T](items: list[T]) -> T`, the brackets after the function name declare `T`, and the same `T` says that a list of strings produces a string and a list of integers produces an integer.

Use generics when a function or class is reusable but still preserves a relationship between input and output types. Older code declares the same variable with `typing.TypeVar`; both spellings mean the same thing to a type checker.

:::program
```python
from typing import TypeVar


def first[T](items: list[T]) -> T:
    return items[0]


def pair[T](left: T, right: T) -> tuple[T, T]:
    return (left, right)


class Box[T]:
    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item


class Setting[T = str]:
    def __init__(self, value: T) -> None:
        self.value = value


Item = TypeVar("Item")


def last(items: list[Item]) -> Item:
    return items[-1]

print(first([1, 2, 3]))
print(first(["Ada", "Grace"]))
print(pair("x", "y"))
print(Box(3).get())
print(Box.__type_params__)
print(Setting.__type_params__[0].__default__)
print(last([1, 2, 3]))
print(first.__annotations__)
print(last.__annotations__)
```
:::

:::cell
Square brackets after the function name declare a type parameter. `T` stands for a type chosen by the caller, so the return type follows the list element type.

```python
def first[T](items: list[T]) -> T:
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
Reusing the same type parameter expresses a relationship between parameters and results. Each function declares its own `T`; the name is scoped to that definition.

```python
def pair[T](left: T, right: T) -> tuple[T, T]:
    return (left, right)

print(pair("x", "y"))
```

```output
('x', 'y')
```
:::

:::cell
A class takes type parameters the same way. `Box[T]` says that whatever type goes in through `__init__` is the type that `get()` hands back. The parameters are recorded on the class, but nothing checks them at runtime.

```python
class Box[T]:
    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item

print(Box(3).get())
print(Box.__type_params__)
```

```output
3
(T,)
```
:::

:::cell
Python 3.13 lets a type parameter name a default. A type checker reads a bare `Setting` as `Setting[str]`, while `Setting[int]` still overrides it. The default is stored on the parameter object.

```python
class Setting[T = str]:
    def __init__(self, value: T) -> None:
        self.value = value

print(Setting.__type_params__[0].__default__)
```

```output
<class 'str'>
```
:::

:::cell
Before Python 3.12 the variable had to be created separately with `TypeVar` and then used by name. This legacy spelling still works and is common in existing code; the annotations show it as `~Item` rather than a scoped `T`.

```python
from typing import TypeVar

Item = TypeVar("Item")


def last(items: list[Item]) -> Item:
    return items[-1]

print(last([1, 2, 3]))
print(first.__annotations__)
print(last.__annotations__)
```

```output
3
{'items': list[T], 'return': T}
{'items': list[~Item], 'return': ~Item}
```
:::

:::note
- `def first[T](...)` and `class Box[T]` declare type parameters inline; this syntax needs Python 3.12 or later.
- `[T = str]` gives a type parameter a default; that needs Python 3.13.
- `T = TypeVar("T")` is the legacy spelling of the same idea and is still what older codebases use.
- Generic functions avoid losing information to `object` or `Any`.
- Use generics when input and output types are connected.
:::
