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

`ParamSpec` is for decorators and wrapper functions that should keep the wrapped callable's parameter shape. Without it, a generic decorator often falls back to `Callable[..., R]`, which says “this returns the right type, but I no longer know what arguments are valid.”

Use `ParamSpec` when the wrapper forwards `*args` and `**kwargs` to the original function without changing the signature. Use a plain `Callable` when the wrapper deliberately accepts a different set of parameters.

`P.args` and `P.kwargs` annotate the wrapper's forwarded arguments. A separate `TypeVar` keeps the return type tied to the wrapped function's return type.

:::program
```python
from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def erased(func: Callable[..., R]) -> Callable[..., R]:
    return func


def logged(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(left: int, right: int) -> int:
    return left + right

print(erased(add)(2, 3))
print(add(2, 3))
```
:::

:::cell
`Callable[..., R]` is sometimes too broad. It preserves the return type, but the ellipsis means the callable accepts any argument list as far as the type checker can tell.

```python
from collections.abc import Callable
from typing import ParamSpec, TypeVar

R = TypeVar("R")


def erased(func: Callable[..., R]) -> Callable[..., R]:
    return func

print(erased.__name__)
```

```output
erased
```
:::

:::cell
`ParamSpec` captures the original parameters and lets the wrapper forward exactly that shape.

```python
P = ParamSpec("P")


def logged(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

print(logged.__name__)
```

```output
logged
```
:::

:::cell
The decorated function still runs normally. The benefit is static: tools can keep checking that `add` receives two integers.

```python
@logged
def add(left: int, right: int) -> int:
    return left + right

print(erased(add)(2, 3))
print(add(2, 3))
```

```output
calling add
5
calling add
5
```
:::

:::note
- `ParamSpec` preserves a callable's parameter list through transparent wrappers.
- Pair `ParamSpec` with a `TypeVar` when the return type should also be preserved.
- Python 3.12+ also accepts the inline PEP 695 spelling `def wrap[**P, R](func: Callable[P, R])`, which declares both variables in the signature itself.
- If the wrapper changes the public signature, write that new signature directly instead.
:::
