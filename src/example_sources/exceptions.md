+++
slug = "exceptions"
title = "Exceptions"
section = "Errors"
summary = "Use try and except to handle exceptional cases."
doc_path = "/tutorial/errors.html"
+++

Exceptions represent errors or unusual conditions that interrupt normal control flow. `try` and `except` let you recover at the point where recovery makes sense.

Catch specific exceptions whenever possible. A broad catch can hide programming mistakes, while a targeted `ValueError` handler documents exactly what failure is expected.

Keep the successful path readable and put recovery logic near the operation that may fail.

:::program
```python
def parse_int(text):
    return int(text)

print(parse_int("42"))

try:
    number = parse_int("python")
except ValueError:
    number = None

print(number)
```
:::

:::cell
When no exception is raised, execution continues normally and the function returns its value.

```python
def parse_int(text):
    return int(text)

print(parse_int("42"))
```

```output
42
```
:::

:::cell
When `int()` cannot parse the string, it raises `ValueError`. Catching that specific exception makes the recovery path explicit.

```python
try:
    number = parse_int("python")
except ValueError:
    number = None

print(number)
```

```output
None
```
:::

:::note
- Catch the most specific exception you can.
- Unhandled exceptions stop the current flow.
- Put recovery where the program has enough context to choose a fallback.
:::
