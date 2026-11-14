+++
slug = "constants"
title = "Constants"
section = "Basics"
summary = "Python uses naming conventions and optional types for values that should not change."
doc_path = "/library/typing.html#typing.Final"
see_also = [
  "variables",
  "literal-and-final",
  "type-hints",
]
+++

Python has no `const` keyword for ordinary names. Modules use all-caps names such as `MAX_RETRIES` to say “treat this as fixed configuration, not changing state.”

The interpreter will still let code rebind the name. That is why constants are primarily an API and readability convention. If a project also uses static typing, `Final` can make the convention machine-checkable.

Named constants remove magic values from code and give repeated literals one place to change.

:::program
```python
from typing import Final

MAX_RETRIES: Final = 3
API_VERSION = "2026-05"

attempts = 2
print(attempts < MAX_RETRIES)
attempts = 3
print(attempts < MAX_RETRIES)

print(API_VERSION)

MAX_RETRIES = 5
print(MAX_RETRIES)
```
:::

:::cell
All-caps names communicate design intent: this value is configuration that callers should treat as fixed. Comparing against `MAX_RETRIES` instead of a bare `3` keeps the meaning beside the check, and gives the limit one place to change.

```python
MAX_RETRIES = 3

attempts = 2
print(attempts < MAX_RETRIES)
attempts = 3
print(attempts < MAX_RETRIES)
```

```output
True
False
```
:::

:::cell
Constants are useful when a repeated literal deserves a name at the domain boundary.

```python
API_VERSION = "2026-05"
print(API_VERSION)
```

```output
2026-05
```
:::

:::cell
`Final` lets type checkers reject reassignment, but Python still runs ordinary rebinding at runtime.

```python
from typing import Final

MAX_RETRIES: Final = 3
MAX_RETRIES = 5
print(MAX_RETRIES)
```

```output
5
```
:::

:::note
- Python constants are a convention, not a runtime lock.
- Use all-caps names for fixed module-level configuration.
- Add `Final` when static tooling should flag accidental rebinding.
:::
