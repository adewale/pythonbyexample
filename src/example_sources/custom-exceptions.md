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

:::cell
Create a custom exception when a failure has a name in your problem domain. The class can be empty at first.

Raise the custom exception where the invalid state is detected. The message explains this particular occurrence.

Callers can catch the precise error type without accidentally catching unrelated failures.

```python
class EmptyCartError(Exception):
    pass

def checkout(items):
    if not items:
        raise EmptyCartError("cart is empty")
    return "paid"

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
:::
