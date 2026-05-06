+++
slug = "exceptions"
title = "Exceptions"
section = "Errors"
summary = "Use try and except to handle exceptional cases."
doc_path = "/tutorial/errors.html"
+++

Exceptions represent errors or unusual conditions that interrupt normal control flow. try and except let you recover at the point where recovery makes sense.

Catch specific exceptions whenever possible. A broad catch can hide programming mistakes, while a targeted ValueError handler documents exactly what failure is expected.

Catch the most specific exception you can. Unhandled exceptions stop the current flow.

:::program
```python
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None

print(parse_int("42"))
print(parse_int("python"))
```
:::

:::cell
Exceptions represent errors or unusual conditions that interrupt normal control flow. try and except let you recover at the point where recovery makes sense.

Catch specific exceptions whenever possible. A broad catch can hide programming mistakes, while a targeted ValueError handler documents exactly what failure is expected.

```python
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None

print(parse_int("42"))
print(parse_int("python"))
```

```output
42
None
```
:::

:::note
- Catch the most specific exception you can.
- Unhandled exceptions stop the current flow.
:::
