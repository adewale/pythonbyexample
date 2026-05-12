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

overload describes APIs whose return type depends on argument types. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
from typing import overload

@overload
def double(value: int) -> int: ...

@overload
def double(value: str) -> str: ...

def double(value):
    return value * 2

print(double(4))
print(double("ha"))
print(double.__name__)
```
:::

:::cell
`@overload` signatures are for static type checkers.

```python
from typing import overload

@overload
def double(value: int) -> int: ...

@overload
def double(value: str) -> str: ...

def double(value):
    return value * 2

print(double(4))
print(double("ha"))
print(double.__name__)
```

```output
8
haha
double
```
:::

:::note
- `@overload` signatures are for static type checkers.
- The real implementation comes after the overload declarations.
- Use overloads when a single runtime function has multiple precise static shapes.
:::
