+++
slug = "casts-and-any"
title = "Casts and Any"
section = "Types"
summary = "Any and cast are escape hatches for places static analysis cannot prove."
doc_path = "/library/typing.html#typing.cast"
see_also = [
  "type-hints",
  "runtime-type-checks",
  "typed-dicts",
]
+++

`Any` and `cast()` are escape hatches. They are useful at messy boundaries where a type checker cannot prove what a value is, but they also remove protection when overused.

`Any` tells static tools to stop checking most operations on a value. `cast(T, value)` tells the type checker to treat a value as `T`, but it returns the same runtime object unchanged.

Prefer narrowing with runtime checks when possible. Use `cast()` when another invariant already proves the type and the checker cannot see that proof.

:::program
```python
from typing import Any, cast

raw: Any = {"score": "98"}
score_text = cast(dict[str, str], raw)["score"]
score = int(score_text)

print(score + 2)
print(cast(list[int], raw) is raw)
print(type(raw).__name__)

value: object = {"score": "98"}
if isinstance(value, dict):
    print(value["score"])
```
:::

:::cell
`Any` disables most static checking for a value. The runtime object is still whatever value was actually assigned.

```python
from typing import Any, cast

raw: Any = {"score": "98"}
score_text = cast(dict[str, str], raw)["score"]
score = int(score_text)
print(score + 2)
```

```output
100
```
:::

:::cell
`cast()` does not convert or validate the value. It returns the same object at runtime.

```python
print(cast(list[int], raw) is raw)
print(type(raw).__name__)
```

```output
True
dict
```
:::

:::cell
A real runtime check narrows by inspecting the value. This is safer when the input is untrusted.

```python
value: object = {"score": "98"}
if isinstance(value, dict):
    print(value["score"])
```

```output
98
```
:::

:::note
- `Any` disables most static checking for a value.
- `cast()` tells the type checker to trust you without changing the runtime object.
- Prefer narrowing with checks when possible.
:::
