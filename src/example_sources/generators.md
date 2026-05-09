+++
slug = "generators"
title = "Generators"
section = "Iteration"
summary = "yield creates an iterator that produces values on demand."
doc_path = "/tutorial/classes.html#generators"
see_also = [
  "iterators",
  "iterator-vs-iterable",
  "generator-expressions",
]
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

def countdown_eager(n):
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

values = countdown_eager(3)
print(values)
print(values)

stream = countdown(3)
print(list(stream))
print(list(stream))

class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        value = self.n
        self.n -= 1
        return value

print(list(Countdown(3)))
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

:::cell
`return` builds the entire result before handing it back; `yield` produces values on demand. The list keeps its values for repeated use, while the generator is exhausted after one pass.

```python
def countdown_eager(n):
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

values = countdown_eager(3)
print(values)
print(values)

stream = countdown(3)
print(list(stream))
print(list(stream))
```

```output
[3, 2, 1]
[3, 2, 1]
[3, 2, 1]
[]
```
:::

:::cell
Every generator is an iterator. The same countdown written by hand needs `__iter__` and `__next__` and an explicit `StopIteration`. The generator function expresses the same protocol with one `yield`.

```python
class Countdown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        value = self.n
        self.n -= 1
        return value

print(list(Countdown(3)))
```

```output
[3, 2, 1]
```
:::

:::note
- Generator functions are a concise way to create custom iterators; every generator is an iterator.
- `yield` defers work and streams values; `return` produces the whole result up front.
- A generator is consumed as you iterate over it.
- Prefer a list when you need to reuse stored results; prefer a generator when values can be streamed once.
:::
