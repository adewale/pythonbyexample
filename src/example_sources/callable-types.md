+++
slug = "callable-types"
title = "Callable Types"
section = "Types"
summary = "Callable annotations describe functions passed as values."
doc_path = "/library/typing.html#annotating-callable-objects"
see_also = [
  "functions",
  "callable-objects",
  "protocols",
]
+++

Callable annotations describe values that can be called like functions. They are useful when a function accepts a callback, strategy, predicate, or transformation.

`Callable[[int], int]` says how the callback will be called: one integer argument, integer result. The annotation helps tools and readers, while runtime still only needs an object that is actually callable.

Use `Callable` for simple call shapes. Use a protocol when the callback needs named attributes, overloaded signatures, or a more descriptive interface.

:::program
```python
from collections.abc import Callable


def apply_twice(value: int, func: Callable[[int], int]) -> int:
    return func(func(value))


def add_one(number: int) -> int:
    return number + 1

class Doubler:
    def __call__(self, number: int) -> int:
        return number * 2

print(apply_twice(3, add_one))
print(apply_twice(3, Doubler()))
print(callable(add_one), callable(Doubler()))
```
:::

:::cell
Use `Callable[[Arg], Return]` for function-shaped values. The callback is passed in and called by the receiving function.

```python
from collections.abc import Callable


def apply_twice(value: int, func: Callable[[int], int]) -> int:
    return func(func(value))


def add_one(number: int) -> int:
    return number + 1

print(apply_twice(3, add_one))
```

```output
5
```
:::

:::cell
Callable annotations are structural: an object with `__call__` can also satisfy the shape.

```python
class Doubler:
    def __call__(self, number: int) -> int:
        return number * 2

print(apply_twice(3, Doubler()))
```

```output
12
```
:::

:::cell
Runtime callability is a separate question from static annotation. `callable()` checks whether Python can call the object.

```python
print(callable(add_one), callable(Doubler()))
```

```output
True True
```
:::

:::note
- Use `Callable[[Arg], Return]` for simple function-shaped values.
- The annotation documents how the callback will be called.
- For complex call signatures, protocols can be clearer.
:::
