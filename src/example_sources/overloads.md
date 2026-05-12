+++
slug = "overloads"
title = "Overloads"
section = "Types"
summary = "overload describes APIs whose return type depends on argument types."
doc_path = "/library/typing.html#typing.overload"
see_also = [
  "type-hints",
  "union-and-optional-types",
  "generics-and-typevar",
]
+++

`@overload` lets type checkers describe a function whose return type depends on the argument types. The overload declarations are static-only promises; the runtime function is still the single implementation that appears after them.

Use overloads when a union return type would be too vague for callers. For example, `double(4)` returns an `int`, while `double("ha")` returns a `str`; `int | str` loses that relationship.

At runtime the overload stubs are not dispatch cases. The implementation must inspect or operate on the value just like any other Python function.

:::program
```python
from typing import overload

@overload
def double(value: int) -> int: ...

@overload
def double(value: str) -> str: ...

def double(value: int | str) -> int | str:
    return value * 2

print(double(4))
print(double("ha"))
print(double.__annotations__)
```
:::

:::cell
The overload stubs give static tools precise call shapes: integer in, integer out; string in, string out.

```python
from typing import overload

@overload
def double(value: int) -> int: ...

@overload
def double(value: str) -> str: ...

print("static signatures only")
```

```output
static signatures only
```
:::

:::cell
There is still one runtime implementation. It must accept every shape promised by the overloads.

```python
def double(value: int | str) -> int | str:
    return value * 2

print(double(4))
print(double("ha"))
```

```output
8
haha
```
:::

:::cell
Only the implementation's annotations are visible on the runtime function. The overload declarations were for the type checker.

```python
print(double.__annotations__)
```

```output
{'value': int | str, 'return': int | str}
```
:::

:::note
- Put `@overload` declarations immediately before the implementation.
- Overloads improve static precision; they do not create runtime dispatch.
- If all callers can work with one broad return type, a simple union annotation is usually enough.
:::
