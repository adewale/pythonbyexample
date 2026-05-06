+++
slug = "multiple-return-values"
title = "Multiple Return Values"
section = "Functions"
summary = "Python returns multiple values by returning a tuple and unpacking it."
doc_path = "/tutorial/datastructures.html#tuples-and-sequences"
+++

Python multiple return values are tuple return values with friendly syntax. `return a, b` creates one tuple containing two positions.

Most callers unpack that tuple immediately. Good target names make the meaning of each returned position explicit.

Use this for small, fixed groups of results. For larger records, a dataclass or named tuple usually communicates better.

:::program
```python
def divide_with_remainder(total, size):
    quotient = total // size
    remainder = total % size
    return quotient, remainder

boxes, leftover = divide_with_remainder(17, 5)
print(boxes)
print(leftover)
```
:::

:::cell
Python functions can appear to return multiple values. The mechanism is simple: `return quotient, remainder` returns a tuple.

Callers usually unpack the tuple immediately. The names at the call site document what each position means.

```python
def divide_with_remainder(total, size):
    quotient = total // size
    remainder = total % size
    return quotient, remainder

boxes, leftover = divide_with_remainder(17, 5)
print(boxes)
print(leftover)
```

```output
3
2
```
:::

:::note
- A comma creates a tuple; `return a, b` returns one tuple containing two values.
- Unpacking at the call site gives each returned position a meaningful name.
:::
