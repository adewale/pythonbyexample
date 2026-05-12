+++
slug = "variables"
title = "Variables"
section = "Basics"
summary = "Names are bound to values with assignment."
doc_path = "/reference/simple_stmts.html#assignment-statements"
see_also = [
  "values",
  "mutability",
  "object-lifecycle",
  "constants",
]
+++

Python variables are names bound to objects. Assignment creates or rebinds a name; it does not require a declaration and it does not permanently attach a type to the name.

Rebinding changes which object a name refers to. Augmented assignment such as `+=` is the idiomatic way to update counters and accumulators.

Use clear names for values that matter later. Python's flexibility makes naming more important, not less.

Use assignment when a value needs a name for reuse or explanation. Prefer a direct expression when naming the intermediate value would add noise.

:::program
```python
message = "hi"
print(message)

message = "hello"
print(message)

count = 3
count += 1
print(count)
```
:::

:::cell
Assignment binds a name to a value. Once bound, the name can be used anywhere that value is needed.

```python
message = "hi"
print(message)
```

```output
hi
```
:::

:::cell
Assignment can rebind the same name to a different value. The name is not permanently attached to the first object.

```python
message = "hello"
print(message)
```

```output
hello
```
:::

:::cell
Augmented assignment reads the current binding, computes an updated value, and stores the result back under the same name.

```python
count = 3
count += 1
print(count)
```

```output
4
```
:::

:::note
- Python variables are names bound to objects, not boxes with fixed types.
- Rebinding a name is normal.
- Use augmented assignment for counters and accumulators.
:::
