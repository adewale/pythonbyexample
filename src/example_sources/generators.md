+++
slug = "generators"
title = "Generators"
section = "Iteration"
summary = "yield produces a lazy sequence of values."
doc_path = "/tutorial/classes.html#generators"
+++

A generator function uses yield to produce values lazily. Calling the function returns an iterator; the body runs only as values are requested.

Generators are useful for pipelines, large inputs, and infinite sequences because they avoid building an entire collection in memory.

Generator functions return iterators. Values are produced on demand.

:::cell
A generator function uses yield to produce values lazily. Calling the function returns an iterator; the body runs only as values are requested.

Generators are useful for pipelines, large inputs, and infinite sequences because they avoid building an entire collection in memory.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(3):
    print(value)
```

```output
3
2
1
```
:::

:::note
- Generator functions return iterators.
- Values are produced on demand.
:::
