+++
slug = "generators"
title = "Generators"
section = "Iteration"
summary = "yield creates an iterator that produces values on demand."
doc_path = "/tutorial/classes.html#generators"
+++

A generator function is a convenient way to write your own iterator. `yield` produces one value, pauses the function, and resumes when the next value is requested.

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
- Generator functions are a concise way to create custom iterators.
- Values are produced on demand.
- A generator is consumed as you iterate over it.
- Prefer a list when you need to reuse stored results; prefer a generator when values can be streamed once.
:::
