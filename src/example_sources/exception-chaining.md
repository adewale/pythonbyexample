+++
slug = "exception-chaining"
title = "Exception Chaining"
section = "Errors"
summary = "raise from preserves the original cause when translating exceptions."
doc_path = "/tutorial/errors.html#exception-chaining"
see_also = [
  "exceptions",
  "custom-exceptions",
  "assertions",
]
+++

Exception chaining connects a higher-level error to the lower-level exception that caused it. The syntax is `raise NewError(...) from error`.

Use chaining when translating implementation details into a domain-specific error while preserving the original cause for debugging.

This is different from hiding the original exception. The caller can catch the domain error, and tooling can still inspect `__cause__`.

:::program
```python
class ConfigError(Exception):
    pass


def read_port(text):
    try:
        return int(text)
    except ValueError as error:
        raise ConfigError("port must be a number") from error

print(ConfigError.__name__)

try:
    read_port("abc")
except ConfigError as error:
    print(error)
    print(type(error.__cause__).__name__)
```
:::

:::cell
Catch the low-level exception where it happens, then raise a domain-specific exception from it.

```python
class ConfigError(Exception):
    pass


def read_port(text):
    try:
        return int(text)
    except ValueError as error:
        raise ConfigError("port must be a number") from error

print(ConfigError.__name__)
```

```output
ConfigError
```
:::

:::cell
The caller handles the domain error. The original `ValueError` remains available as `__cause__`.

```python
try:
    read_port("abc")
except ConfigError as error:
    print(error)
    print(type(error.__cause__).__name__)
```

```output
port must be a number
ValueError
```
:::

:::note
- Use `raise ... from error` when translating exceptions across a boundary.
- The new exception's `__cause__` points to the original exception.
- Chaining keeps user-facing errors clear without losing debugging context.
:::
