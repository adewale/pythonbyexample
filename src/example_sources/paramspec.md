+++
slug = "paramspec"
title = "ParamSpec"
section = "Types"
summary = "ParamSpec preserves callable parameter types through wrappers."
doc_path = "/library/typing.html#typing.ParamSpec"
+++

ParamSpec preserves callable parameter types through wrappers. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def logged(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(left: int, right: int) -> int:
    return left + right

print(add(2, 3))
```
:::

:::cell
`ParamSpec` captures the parameters of a callable.

```python
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def logged(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(left: int, right: int) -> int:
    return left + right

print(add(2, 3))
```

```output
calling add
5
```
:::

:::note
- `ParamSpec` captures the parameters of a callable.
- Wrappers can forward `*args` and `**kwargs` without erasing the original signature for type checkers.
- This matters most for decorators.
:::
