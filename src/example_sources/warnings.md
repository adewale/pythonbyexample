+++
slug = "warnings"
title = "Warnings"
section = "Errors"
summary = "warnings report soft problems without immediately stopping the program."
doc_path = "/library/warnings.html"
see_also = [
  "exceptions",
  "logging",
  "testing",
]
+++

A warning reports a problem that callers should know about, but it does not have to stop the current operation. Deprecations are the classic case: the old API can still return a value while telling users to migrate.

Warnings sit between logging and exceptions. Logging records operational evidence; exceptions stop the current path; warnings make compatibility or correctness concerns visible according to a filter.

Tests often capture warnings so deprecations are asserted instead of merely printed. Filters can also turn warnings into errors when a project wants to enforce cleanup.

:::program
```python
import warnings


def old_name():
    warnings.warn("old_name is deprecated", DeprecationWarning, stacklevel=2)
    return "result"

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always", DeprecationWarning)
    print(old_name())
    print(caught[0].category.__name__)
    print(str(caught[0].message))

with warnings.catch_warnings():
    warnings.simplefilter("error", DeprecationWarning)
    try:
        old_name()
    except DeprecationWarning:
        print("warning became error")
```
:::

:::cell
Capture warnings in tests when the returned value still matters but the migration notice must be asserted.

```python
import warnings


def old_name():
    warnings.warn("old_name is deprecated", DeprecationWarning, stacklevel=2)
    return "result"

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always", DeprecationWarning)
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

:::cell
A filter can promote selected warnings to exceptions, which is useful in CI when deprecated calls should fail the build.

```python
with warnings.catch_warnings():
    warnings.simplefilter("error", DeprecationWarning)
    try:
        old_name()
    except DeprecationWarning:
        print("warning became error")
```

```output
warning became error
```
:::

:::note
- Use warnings for soft problems callers can act on later.
- Use exceptions when the current operation cannot continue.
- `stacklevel` should point the warning at the caller rather than inside the helper.
:::
