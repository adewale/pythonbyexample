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
min_python = "3.13"
version_notes = "The warnings.deprecated decorator was added in Python 3.13."
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


@warnings.deprecated("use new_name() instead")
def older_name():
    return "result"

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always", DeprecationWarning)
    print(older_name())
    print(str(caught[0].message))
print(older_name.__deprecated__)
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

:::cell
Python 3.13 adds the `@warnings.deprecated` decorator, which states the deprecation once at the definition. Calling the function emits a `DeprecationWarning` aimed at the caller, the message is kept on `__deprecated__`, and type checkers flag uses of the function before the program runs.

```python
@warnings.deprecated("use new_name() instead")
def older_name():
    return "result"

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always", DeprecationWarning)
    print(older_name())
    print(str(caught[0].message))
print(older_name.__deprecated__)
```

```output
result
use new_name() instead
use new_name() instead
```
:::

:::note
- Use warnings for soft problems callers can act on later.
- Use exceptions when the current operation cannot continue.
- `stacklevel` should point the warning at the caller rather than inside the helper.
- On Python 3.13 and later, prefer `@warnings.deprecated(...)` for whole functions and classes; call `warnings.warn()` directly for narrower cases such as one deprecated argument.
:::
