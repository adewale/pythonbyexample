+++
slug = "partial-functions"
title = "Partial Functions"
section = "Functions"
summary = "functools.partial pre-fills arguments to make a more specific callable."
doc_path = "/library/functools.html#functools.partial"
see_also = [
  "functions",
  "args-and-kwargs",
  "callable-objects",
]
+++

`functools.partial` turns a general callable into a more specific callable by remembering some positional or keyword arguments. It is useful when another API wants a one-argument callback but your underlying function needs more context.

A partial object is still callable. It keeps the original function in `.func`, pre-filled positional arguments in `.args`, and pre-filled keyword arguments in `.keywords`.

Prefer a named wrapper function when the adapted behavior needs branching, validation, or a docstring. Use `partial` when the adaptation is simply "call this function with these arguments already supplied."

:::program
```python
from functools import partial


def apply_tax(rate, amount):
    return round(amount * (1 + rate), 2)

vat = partial(apply_tax, 0.2)
service_tax = partial(apply_tax, rate=0.1)

print(apply_tax(0.2, 50))
print(vat(50))
print(service_tax(amount=80))
print(vat.func.__name__)
print(vat.args)
```
:::

:::cell
Without `partial`, callers repeat the same fixed argument every time they want the specialized behavior.

```python
def apply_tax(rate, amount):
    return round(amount * (1 + rate), 2)

print(apply_tax(0.2, 50))
```

```output
60.0
```
:::

:::cell
`partial` stores that fixed argument and returns a callable shaped for the remaining arguments.

```python
from functools import partial

vat = partial(apply_tax, 0.2)
service_tax = partial(apply_tax, rate=0.1)

print(vat(50))
print(service_tax(amount=80))
```

```output
60.0
88.0
```
:::

:::cell
Partial objects expose the function and stored arguments, which is helpful when debugging callback wiring.

```python
print(vat.func.__name__)
print(vat.args)
```

```output
apply_tax
(0.2,)
```
:::

:::note
- `partial` adapts a callable by pre-filling arguments.
- The resulting object can be passed anywhere a callable with the remaining parameters is expected.
- Use a regular function when the adapter needs more logic than argument binding.
:::
