+++
slug = "literal-and-final"
title = "Literal and Final"
section = "Types"
summary = "Literal restricts exact values, while Final marks names that should not be rebound."
doc_path = "/library/typing.html#typing.Literal"
see_also = [
  "type-hints",
  "constants",
  "union-and-optional-types",
  "overloads",
]
+++

`Literal` and `Final` make two different static promises. `Literal` narrows a value to exact allowed options. `Final` tells a type checker that a name should not be rebound after its first assignment.

Both annotations help at API boundaries: a function can accept only known modes, and a module can publish a constant that other code should treat as fixed. Python still runs the same assignment rules at runtime, so these are promises for tools and readers rather than runtime locks.

Use `Literal` when a small closed set is clearer than a broad `str` or `int`. Use `Final` when rebinding would be a bug in the design, especially for module constants and class attributes.

:::program
```python
from typing import Final, Literal

Mode = Literal["read", "write"]
DEFAULT_MODE: Final[Mode] = "read"


def open_label(mode: Mode) -> str:
    return f"opening for {mode}"

print(open_label(DEFAULT_MODE))
print(open_label("write"))

DEFAULT_MODE = "debug"
print(DEFAULT_MODE)
```
:::

:::cell
`Literal` describes exact allowed values. A type checker can reject `"debug"` as a `Mode` even though it is an ordinary string at runtime.

```python
from typing import Final, Literal

Mode = Literal["read", "write"]


def open_label(mode: Mode) -> str:
    return f"opening for {mode}"

print(open_label("write"))
```

```output
opening for write
```
:::

:::cell
`Final` marks a name that should not be rebound. It is stronger documentation than the all-caps constant convention because static tools can flag reassignment.

```python
DEFAULT_MODE: Final[Mode] = "read"
print(open_label(DEFAULT_MODE))
```

```output
opening for read
```
:::

:::cell
The annotation is not a runtime lock. Python still rebinds the name; the mistake is that a type checker and human reader should reject the design.

```python
DEFAULT_MODE = "debug"
print(DEFAULT_MODE)
```

```output
debug
```
:::

:::note
- `Literal` narrows values to a small exact set.
- `Final` prevents rebinding in static analysis, not at runtime.
- Use enums when the option set needs names, behavior, or iteration over members.
:::
