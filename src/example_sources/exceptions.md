+++
slug = "exceptions"
title = "Exceptions"
section = "Errors"
summary = "Use try, except, else, and finally to separate success, recovery, and cleanup."
doc_path = "/tutorial/errors.html"
+++

Exceptions represent errors or unusual conditions that interrupt normal control flow. `try` marks the operation that may fail, and `except` handles a specific failure where recovery makes sense.

Keep the successful path separate from the recovery path. `else` runs only when no exception was raised, while `finally` runs either way for cleanup or bookkeeping.

Use exceptions when an operation cannot produce a valid result. Prefer ordinary conditionals for expected branches that are not errors.

Catch specific exceptions whenever possible. A broad catch can hide programming mistakes, while a targeted `ValueError` handler documents exactly what failure is expected.

:::program
```python
def parse_int(text):
    return int(text)

for text in ["42", "python"]:
    try:
        number = parse_int(text)
    except ValueError:
        print(f"{text}: invalid")
    else:
        print(f"{text}: {number}")
    finally:
        print(f"checked {text}")
```
:::

:::cell
When no exception is raised, the `else` block runs. Keeping success in `else` makes the `try` block contain only the operation that might fail.

```python
def parse_int(text):
    return int(text)

text = "42"
try:
    number = parse_int(text)
except ValueError:
    print(f"{text}: invalid")
else:
    print(f"{text}: {number}")
finally:
    print(f"checked {text}")
```

```output
42: 42
checked 42
```
:::

:::cell
When parsing fails, `int()` raises `ValueError`. Catching that specific exception makes the expected recovery path explicit.

```python
text = "python"
try:
    number = parse_int(text)
except ValueError:
    print(f"{text}: invalid")
else:
    print(f"{text}: {number}")
finally:
    print(f"checked {text}")
```

```output
python: invalid
checked python
```
:::

:::note
- Catch the most specific exception you can.
- `else` is for success code that should run only if the `try` block did not fail.
- `finally` runs whether the operation succeeded or failed.
:::
