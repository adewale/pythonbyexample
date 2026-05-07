+++
slug = "assertions"
title = "Assertions"
section = "Errors"
summary = "assert documents internal assumptions and fails loudly when they are false."
doc_path = "/reference/simple_stmts.html#the-assert-statement"
see_also = [
  "exceptions",
  "custom-exceptions",
  "type-hints",
]
+++

`assert` checks an internal assumption. If the condition is false, Python raises `AssertionError` with an optional message.

Use assertions for programmer assumptions, not for validating user input or external data. Input validation should raise ordinary exceptions that production code expects to handle.

Assertions make invariants executable while keeping the successful path compact.

:::program
```python
def average(scores):
    assert scores, "scores must not be empty"
    return sum(scores) / len(scores)

print(average([8, 10]))

try:
    average([])
except AssertionError as error:
    print(error)
```
:::

:::cell
When the assertion is true, execution continues normally. The assertion documents the function's internal expectation.

```python
def average(scores):
    assert scores, "scores must not be empty"
    return sum(scores) / len(scores)

print(average([8, 10]))
```

```output
9.0
```
:::

:::cell
When the assertion is false, Python raises `AssertionError`. This signals a broken assumption, not a normal recovery path.

```python
try:
    average([])
except AssertionError as error:
    print(error)
```

```output
scores must not be empty
```
:::

:::note
- Use `assert` for internal invariants and debugging assumptions.
- Use explicit exceptions for user input, files, network responses, and other expected failures.
- Assertions can be disabled with Python optimization flags, so do not rely on them for security checks.
:::
