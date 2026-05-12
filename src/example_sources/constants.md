+++
slug = "constants"
title = "Constants"
section = "Basics"
summary = "Python uses naming conventions for values that should not change."
doc_path = "/tutorial/classes.html#python-scopes-and-namespaces"
see_also = [
  "variables",
  "literal-and-final",
  "type-hints",
]
+++

Python has no `const` keyword for ordinary variables. Instead, modules use all-caps names to mark values that should be treated as constants by convention.

The interpreter will not stop rebinding, but the convention is important API communication. Readers understand that `MAX_RETRIES` is configuration, not loop state.

Named constants remove magic values from code and give repeated literals one place to change.

:::program
```python
MAX_RETRIES = 3
API_VERSION = "2026-05"

for attempt in range(1, MAX_RETRIES + 1):
    print(f"attempt {attempt} of {MAX_RETRIES}")

print(API_VERSION)
```
:::

:::cell
Python does not have a `const` declaration like Go or Rust. Instead, modules use all-caps names for values callers should treat as fixed.

The interpreter will still let you rebind the name, but the convention is strong enough that readers understand the design intent.

```python
MAX_RETRIES = 3
API_VERSION = "2026-05"

for attempt in range(1, MAX_RETRIES + 1):
    print(f"attempt {attempt} of {MAX_RETRIES}")
```

```output
attempt 1 of 3
attempt 2 of 3
attempt 3 of 3
```
:::

:::cell
Constants are useful for configuration values that should be named once and reused instead of repeated as magic literals.

```python
print(API_VERSION)
```

```output
2026-05
```
:::

:::note
- Python has no `const` keyword for ordinary names.
- All-caps names such as `MAX_RETRIES` communicate that a value is intended to stay fixed.
:::
