+++
slug = "warnings"
title = "Warnings"
section = "Errors"
summary = "warnings report soft problems without immediately stopping the program."
doc_path = "/library/warnings.html"
+++

warnings report soft problems without immediately stopping the program. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
import warnings


def old_name():
    warnings.warn("old_name is deprecated", DeprecationWarning, stacklevel=2)
    return "result"

warnings.simplefilter("always", DeprecationWarning)
with warnings.catch_warnings(record=True) as caught:
    print(old_name())
    print(caught[0].category.__name__)
    print(str(caught[0].message))
```
:::

:::cell
Warnings are useful for deprecations and soft failures.

```python
import warnings


def old_name():
    warnings.warn("old_name is deprecated", DeprecationWarning, stacklevel=2)
    return "result"

warnings.simplefilter("always", DeprecationWarning)
with warnings.catch_warnings(record=True) as caught:
    print(old_name())
    print(caught[0].category.__name__)
    print(str(caught[0].message))
```

```output
result
DeprecationWarning
old_name is deprecated
```
:::

:::note
- Warnings are useful for deprecations and soft failures.
- Filters decide whether warnings are ignored, shown, or turned into errors.
- Tests often capture warnings to assert migration behavior.
:::
