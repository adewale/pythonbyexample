+++
slug = "exception-groups"
title = "Exception Groups"
section = "Errors"
summary = "except* handles matching exceptions inside an ExceptionGroup."
doc_path = "/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions"
see_also = [
  "exceptions",
  "exception-chaining",
  "async-await",
]
+++

`ExceptionGroup` represents several unrelated exceptions raised together. `except*` handles the matching members of the group and lets other members continue separately.

This syntax is most useful with concurrent code, where several tasks can fail before the caller regains control.

Use ordinary `except` for one exception. Use `except*` only when the value being handled is an exception group.

:::program
```python
try:
    raise ExceptionGroup(
        "batch failed",
        [ValueError("bad port"), TypeError("bad mode")],
    )
except* ValueError as group:
    print(type(group).__name__)
    print(group.exceptions[0])
except* TypeError as group:
    print(group.exceptions[0])
```
:::

:::cell
`ExceptionGroup` bundles several exception objects. `except* ValueError` receives a group containing only the matching `ValueError` members.

```python
try:
    raise ExceptionGroup(
        "batch failed",
        [ValueError("bad port"), TypeError("bad mode")],
    )
except* ValueError as group:
    print(type(group).__name__)
    print(group.exceptions[0])
except* TypeError as group:
    print(group.exceptions[0])
```

```output
ExceptionGroup
bad port
bad mode
```
:::

:::note
- `except*` is for `ExceptionGroup`, not ordinary single exceptions.
- Each `except*` clause handles matching members of the group.
- Exception groups often appear around concurrent work.
:::
