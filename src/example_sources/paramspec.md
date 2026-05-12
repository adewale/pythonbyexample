+++
slug = "paramspec"
title = "ParamSpec"
section = "Types"
summary = "ParamSpec preserves callable parameter types through wrappers."
doc_path = "/library/typing.html#typing.ParamSpec"
see_also = [
  "callable-types",
  "decorators",
  "generics-and-typevar",
]
+++

`ParamSpec` lets a wrapper preserve the parameter types of the function it wraps. The pressure that justifies it is decorators: a generic decorator that returns `Callable[..., R]` erases the wrapped function's argument types, so callers lose type-checker help on every call.

Use `ParamSpec` when a decorator should be transparent to type checkers — the wrapped function and the decorated name should accept the same arguments. Reach for plain `Callable` when the wrapper deliberately changes the signature.

`P.args` and `P.kwargs` annotate the `*args` and `**kwargs` of the inner wrapper, which is how the parameter spec gets bound. Pair `ParamSpec` with a `TypeVar` for the return type when the wrapper should also stay generic over what the wrapped function returns.

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
