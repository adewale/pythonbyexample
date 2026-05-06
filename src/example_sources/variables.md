+++
slug = "variables"
title = "Variables"
section = "Basics"
summary = "Names are bound to values with assignment."
doc_path = "/reference/simple_stmts.html#assignment-statements"
+++

Python variables are names bound to objects. Assignment creates or rebinds a name; it does not require a declaration and it does not permanently attach a type to the name.

Augmented assignment such as += is the idiomatic way to update counters and accumulators. It reads the current binding, computes a new value or mutates in place when appropriate, and stores the result.

Python variables are names bound to objects, not boxes with fixed types. Augmented assignment like += rebinding is common for counters.

:::program
```python
message = "hi"
count = 3
count += 1

print(message)
print(count)
```
:::

:::cell
Python variables are names bound to objects. Assignment creates or rebinds a name; it does not require a declaration and it does not permanently attach a type to the name.

Augmented assignment such as += is the idiomatic way to update counters and accumulators. It reads the current binding, computes a new value or mutates in place when appropriate, and stores the result.

```python
message = "hi"
count = 3
count += 1

print(message)
print(count)
```

```output
hi
4
```
:::

:::note
- Python variables are names bound to objects, not boxes with fixed types.
- Augmented assignment like += rebinding is common for counters.
:::
