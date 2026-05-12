+++
slug = "for-loops"
title = "For Loops"
section = "Control Flow"
summary = "for iterates over values produced by an iterable."
doc_path = "/tutorial/controlflow.html#for-statements"
see_also = [
  "while-loops",
  "iterating-over-iterables",
  "iterators",
]
+++

A `for` loop asks an iterable for values and runs the indented block once per value. Python's loop is not primarily a numeric counter; it is a consumer of lists, ranges, files, generators, and any object that implements the iterator protocol.

Prefer direct iteration when you need each value. Use `range()` when the numbers themselves are the data, and use `enumerate()` when the position and the value both matter.

The loop body is the indented block. When the iterable is exhausted, execution continues after the block. The neighboring `while` loop shape is for conditions that must be rechecked manually.

:::program
```python
for name in ["Ada", "Grace", "Guido"]:
    print(name)

for number in range(3):
    print(number)

for index, name in enumerate(["Ada", "Grace"], start=1):
    print(index, name)
```
:::

:::cell
Direct iteration keeps the code focused on the values in the collection.

```python
for name in ["Ada", "Grace", "Guido"]:
    print(name)
```

```output
Ada
Grace
Guido
```
:::

:::cell
`range(3)` yields `0`, `1`, and `2` lazily. Use it when those integers are the thing being iterated over.

```python
for number in range(3):
    print(number)
```

```output
0
1
2
```
:::

:::cell
`enumerate()` is the usual Python way to keep a counter beside each value without indexing back into the list.

```python
for index, name in enumerate(["Ada", "Grace"], start=1):
    print(index, name)
```

```output
1 Ada
2 Grace
```
:::

:::note
- A `for` loop consumes an iterable until it is exhausted.
- Reach for `while` when the stopping condition must be rechecked manually.
- `iter()` and `next()` expose the protocol that `for` uses internally.
:::
