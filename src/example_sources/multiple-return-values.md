+++
slug = "multiple-return-values"
title = "Multiple Return Values"
section = "Functions"
summary = "Python returns multiple values by returning a tuple and unpacking it."
doc_path = "/tutorial/datastructures.html#tuples-and-sequences"
see_also = [
  "tuples",
  "unpacking",
  "functions",
]
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

result = divide_with_remainder(17, 5)
print(result)

boxes, leftover = result
print(boxes)
print(leftover)
```
:::

:::cell
Returning values separated by commas returns one tuple. The tuple is visible if the caller stores the result directly.

```python
def divide_with_remainder(total, size):
    quotient = total // size
    remainder = total % size
    return quotient, remainder

result = divide_with_remainder(17, 5)
print(result)
```

```output
(3, 2)
```
:::

:::cell
Callers usually unpack the tuple immediately or soon after. The names at the call site document what each position means.

```python
boxes, leftover = result
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
- Use a class-like record when the result has many fields.
:::
