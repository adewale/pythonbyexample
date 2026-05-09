+++
slug = "iterator-vs-iterable"
title = "Iterator vs Iterable"
section = "Iteration"
summary = "Iterables produce fresh iterators; iterators are one-pass."
doc_path = "/glossary.html#term-iterable"
see_also = [
  "iterators",
  "iterating-over-iterables",
  "generators",
]
+++

An iterable can produce values when asked. An iterator is the object that remembers where the production currently is. The distinction matters because iterables can be traversed many times, while many iterators can be traversed only once.

`iter(iterable)` returns a fresh iterator each call. `iter(iterator)` returns the iterator itself. That self-iteration property is how `for` loops can accept either kind, and it is also why a function that loops over its argument twice silently breaks when called with a generator instead of a list.

The takeaway for API design: receive iterables when the caller may want a second pass, and materialize once at the boundary if you must.

:::program
```python
names = ["Ada", "Grace"]

print(list(names))
print(list(names))

stream = iter(names)
print(list(stream))
print(list(stream))

first = iter(names)
second = iter(names)
print(first is second)
print(iter(first) is first)

def total_and_count(numbers):
    total = sum(numbers)
    count = sum(1 for _ in numbers)
    return total, count

def values():
    yield from [10, 9, 8]

print(total_and_count([10, 9, 8]))
print(total_and_count(values()))

def total_and_count_safe(numbers):
    items = list(numbers)
    return sum(items), len(items)

print(total_and_count_safe(values()))
```
:::

:::cell
A list is iterable. Each `for` loop or `list()` call asks the list for a fresh iterator under the hood, so the same data can be traversed many times.

```python
names = ["Ada", "Grace"]
print(list(names))
print(list(names))
```

```output
['Ada', 'Grace']
['Ada', 'Grace']
```
:::

:::cell
An iterator is one-pass. Calling `iter()` returns a position-tracking object; once it has been exhausted, it stays exhausted.

```python
stream = iter(names)
print(list(stream))
print(list(stream))
```

```output
['Ada', 'Grace']
[]
```
:::

:::cell
Calling `iter()` on an iterable returns a brand-new iterator each time. Calling `iter()` on an iterator returns the same object — that is the rule that lets a `for` loop accept either kind.

```python
first = iter(names)
second = iter(names)
print(first is second)
print(iter(first) is first)
```

```output
False
True
```
:::

:::cell
The distinction shows up at API boundaries. A function that loops over its argument twice works for an iterable but silently produces wrong answers for an iterator, because the second pass finds the iterator already exhausted. Materialize once at the boundary when both passes matter.

```python
def total_and_count(numbers):
    total = sum(numbers)
    count = sum(1 for _ in numbers)
    return total, count

def values():
    yield from [10, 9, 8]

print(total_and_count([10, 9, 8]))
print(total_and_count(values()))

def total_and_count_safe(numbers):
    items = list(numbers)
    return sum(items), len(items)

print(total_and_count_safe(values()))
```

```output
(27, 3)
(27, 0)
(27, 3)
```
:::

:::note
- An iterable produces an iterator each time `iter()` is called on it; an iterator produces values until it is exhausted.
- `iter(iterable)` returns a fresh iterator; `iter(iterator)` returns the same iterator.
- Functions that traverse their input more than once must accept an iterable or materialize the input at the boundary.
:::
