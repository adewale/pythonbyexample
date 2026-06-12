+++
slug = "positional-only-parameters"
title = "Positional-only Parameters"
section = "Functions"
summary = "Use / to mark parameters that callers must pass by position."
doc_path = "/tutorial/controlflow.html#special-parameters"
see_also = [
  "keyword-only-arguments",
  "functions",
  "args-and-kwargs",
]
+++

A `/` in a function signature marks the parameters before it as positional-only. Callers must pass those arguments by position, not by keyword.

This is useful when parameter names are implementation details or when an API should match built-in functions that accept positional values.

Together, `/` and `*` let a signature draw clear boundaries: positional-only inputs, ordinary inputs, and keyword-only options.

:::program
```python
def scale(value, /, factor=2, *, clamp=False):
    result = value * factor
    if clamp:
        result = min(result, 10)
    return result

print(scale(4))
print(scale(4, factor=3))
print(scale(4, factor=3, clamp=True))

try:
    scale(value=4)
except TypeError as error:
    print(type(error).__name__)
```
:::

:::cell
Parameters before `/` are positional-only. `value` is the main input, while `factor` remains an ordinary parameter that can be named.

```python
def scale(value, /, factor=2, *, clamp=False):
    result = value * factor
    if clamp:
        result = min(result, 10)
    return result

print(scale(4))
print(scale(4, factor=3))
```

```output
8
12
```
:::

:::cell
Parameters after `*` are keyword-only. That makes options such as `clamp` explicit at the call site — here `4 * 3` would be `12`, and the clamp visibly caps the result at `10`.

```python
print(scale(4, factor=3, clamp=True))
```

```output
10
```
:::

:::cell
The restriction is enforced, not advisory: passing the positional-only `value` by keyword raises `TypeError` at the call site.

```python
try:
    scale(value=4)
except TypeError as error:
    print(type(error).__name__)
```

```output
TypeError
```
:::

:::note
- `/` marks parameters before it as positional-only.
- `*` marks parameters after it as keyword-only.
- Use these markers when the call shape is part of the API design.
:::
