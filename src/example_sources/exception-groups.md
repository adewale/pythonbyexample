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

`ExceptionGroup` represents several unrelated exceptions raised together. `except*` exists for code that may receive multiple failures at once, especially concurrent work.

Use ordinary `except` for one exception. Use `except*` only when the value being handled is an exception group and each matching subgroup needs its own handling.

Each `except*` clause receives a smaller exception group containing the matching exceptions.

:::program
```python
errors = ExceptionGroup(
    "batch failed",
    [ValueError("bad port"), TypeError("bad mode")],
)
print(len(errors.exceptions))

try:
    raise errors
except* ValueError as group:
    print(type(group).__name__)
    print(group.exceptions[0])
except* TypeError as group:
    print(group.exceptions[0])
```
:::

:::cell
An exception group bundles several exception objects. This is different from an ordinary exception because more than one failure is present.

```python
errors = ExceptionGroup(
    "batch failed",
    [ValueError("bad port"), TypeError("bad mode")],
)
print(len(errors.exceptions))
```

```output
2
```
:::

:::cell
`except*` handles matching members of the group. The `ValueError` handler sees the value error, and the `TypeError` handler sees the type error.

```python
try:
    raise errors
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
