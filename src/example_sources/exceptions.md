+++
slug = "exceptions"
title = "Exceptions"
section = "Errors"
summary = "Use try, except, else, and finally to separate success, recovery, and cleanup."
doc_path = "/tutorial/errors.html"
see_also = [
  "conditionals",
  "guard-clauses",
  "custom-exceptions",
  "warnings",
]
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


def safe_parse_broken(text):
    try:
        return int(text)
    except Exception:
        return None

def safe_parse_fixed(text):
    try:
        return int(text)
    except ValueError:
        return None

print(safe_parse_broken("42"))
print(safe_parse_fixed("42"))
print(safe_parse_broken(["4", "2"]))

try:
    safe_parse_fixed(["4", "2"])
except TypeError as error:
    print(type(error).__name__)
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

:::cell
Bare `except:` and broad `except Exception:` swallow far more than the failure you meant to handle, including `KeyboardInterrupt` (bare) and most programming bugs (broad). The two functions look interchangeable on good input — the divergence appears on a buggy call: passing a list is a programming error, yet the broad version converts it into a quiet `None` while the specific version lets the `TypeError` surface.

```python
def safe_parse_broken(text):
    try:
        return int(text)
    except Exception:
        return None

def safe_parse_fixed(text):
    try:
        return int(text)
    except ValueError:
        return None

print(safe_parse_broken("42"))
print(safe_parse_fixed("42"))
print(safe_parse_broken(["4", "2"]))

try:
    safe_parse_fixed(["4", "2"])
except TypeError as error:
    print(type(error).__name__)
```

```output
42
42
None
TypeError
```
:::

:::note
- Catch the most specific exception you can.
- `else` is for success code that should run only if the `try` block did not fail.
- `finally` runs whether the operation succeeded or failed.
- Avoid bare `except:` and broad `except Exception:` — they hide bugs and absorb signals like `KeyboardInterrupt`.
:::
