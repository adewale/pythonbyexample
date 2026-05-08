+++
slug = "partial-functions"
title = "Partial Functions"
section = "Functions"
summary = "functools.partial pre-fills arguments to make a more specific callable."
doc_path = "/library/functools.html#functools.partial"
+++

functools.partial pre-fills arguments to make a more specific callable. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
from functools import partial


def apply_tax(rate, amount):
    return round(amount * (1 + rate), 2)

vat = partial(apply_tax, 0.2)
service_tax = partial(apply_tax, rate=0.1)

print(vat(50))
print(service_tax(amount=80))
print(vat.func.__name__)
```
:::

:::cell
A partial object remembers some arguments.

```python
from functools import partial


def apply_tax(rate, amount):
    return round(amount * (1 + rate), 2)

vat = partial(apply_tax, 0.2)
service_tax = partial(apply_tax, rate=0.1)

print(vat(50))
print(service_tax(amount=80))
print(vat.func.__name__)
```

```output
60.0
88.0
apply_tax
```
:::

:::note
- A partial object remembers some arguments.
- The resulting callable can be passed where an ordinary function is expected.
- Prefer a named function when the pre-filled behavior needs richer logic.
:::
