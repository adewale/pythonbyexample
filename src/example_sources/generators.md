+++
slug = "generators"
title = "Generators"
section = "Iteration"
summary = "yield produces a lazy sequence of values."
doc_path = "/tutorial/classes.html#generators"
+++

A generator function uses `yield` to produce values lazily. Calling the function returns an iterator; the body runs only as values are requested.

Generators are useful for pipelines, large inputs, and infinite sequences because they avoid building an entire collection in memory.

Use `next()` to request one value manually, or loop over the generator to consume values until it is exhausted.

:::program
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

numbers = countdown(3)
print(next(numbers))
print(next(numbers))

for value in countdown(3):
    print(value)
```
:::

:::cell
Calling a generator function returns an iterator. `next()` asks for one value and resumes the function until the next `yield`.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

numbers = countdown(3)
print(next(numbers))
print(next(numbers))
```

```output
3
2
```
:::

:::cell
A `for` loop repeatedly calls `next()` for you. The loop stops when the generator is exhausted.

```python
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
- A generator is consumed as you iterate over it.
:::
