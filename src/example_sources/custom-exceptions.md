+++
slug = "custom-exceptions"
title = "Custom Exceptions"
section = "Errors"
summary = "Custom exception classes name failures that belong to your domain."
doc_path = "/tutorial/errors.html#user-defined-exceptions"
+++

Custom exceptions give names to failures in your problem domain. A named exception is easier to catch and explain than a generic error with only a string message.

Raise the custom exception at the point where the invalid state is discovered. Include a message for the specific occurrence.

Catch custom exceptions at the boundary where recovery makes sense, such as returning an error response or asking for corrected input.

:::program
```python
class EmptyCartError(Exception):
    pass

print(EmptyCartError.__name__)


def checkout(items):
    if not items:
        raise EmptyCartError("cart is empty")
    return "paid"

print(checkout(["book"]))

try:
    checkout([])
except EmptyCartError as error:
    print(error)
```
:::

:::cell
Create a custom exception when a failure has a name in your problem domain. The class can be empty at first.

```python
class EmptyCartError(Exception):
    pass

print(EmptyCartError.__name__)
```

```output
EmptyCartError
```
:::

:::cell
Raise the custom exception where the invalid state is detected. Normal inputs still follow the ordinary success path.

```python
def checkout(items):
    if not items:
        raise EmptyCartError("cart is empty")
    return "paid"

print(checkout(["book"]))
```

```output
paid
```
:::

:::cell
Callers can catch the precise error type without accidentally catching unrelated failures.

```python
try:
    checkout([])
except EmptyCartError as error:
    print(error)
```

```output
cart is empty
```
:::

:::note
- Subclass `Exception` for errors callers are expected to catch.
- A custom exception name can be clearer than reusing a generic `ValueError` everywhere.
- Catch custom exceptions at a boundary that can recover or report clearly.
:::
