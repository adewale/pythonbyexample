+++
slug = "literal-and-final"
title = "Literal and Final"
section = "Types"
summary = "Literal restricts values, while Final marks names that should not be rebound."
doc_path = "/library/typing.html#typing.Literal"
+++

`Literal` restricts a value to one of a small set of exact options, and `Final` tells the type checker that a name should not be rebound. Both are static promises that type checkers enforce; Python's runtime assignment rules still permit any value through if a program ignores the annotation.

Use them when an annotation makes a constant or a small option set explicit at the API boundary. Prefer simpler neighboring tools when the extra machinery would hide the intent.

`Literal` pairs naturally with type aliases and overloads when a function should accept only a known set of strings or numbers. `Final` is most useful for module-level constants and class attributes that the rest of the codebase should treat as immutable.

:::program
```python
from typing import Final, Literal

Mode = Literal["read", "write"]
DEFAULT_MODE: Final[Mode] = "read"


def open_label(mode: Mode) -> str:
    return f"opening for {mode}"

print(open_label(DEFAULT_MODE))
print(open_label("write"))
print(DEFAULT_MODE)
```
:::

:::cell
`Literal` describes a small set of exact allowed values.

```python
from typing import Final, Literal

Mode = Literal["read", "write"]
DEFAULT_MODE: Final[Mode] = "read"


def open_label(mode: Mode) -> str:
    return f"opening for {mode}"

print(open_label(DEFAULT_MODE))
print(open_label("write"))
print(DEFAULT_MODE)
```

```output
opening for read
opening for write
read
```
:::

:::note
- `Literal` describes a small set of exact allowed values.
- `Final` tells type checkers that a name should not be rebound.
- Both are static promises; ordinary runtime assignment rules still apply.
:::
