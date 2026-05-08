+++
slug = "literal-and-final"
title = "Literal and Final"
section = "Types"
summary = "Literal restricts values, while Final marks names that should not be rebound."
doc_path = "/library/typing.html#typing.Literal"
+++

Literal restricts values, while Final marks names that should not be rebound. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

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
