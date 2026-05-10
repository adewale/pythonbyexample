+++
slug = "iterating-over-iterables"
title = "Iterating over Iterables"
section = "Iteration"
summary = "for loops consume values from any iterable object."
doc_path = "/tutorial/controlflow.html#for-statements"
see_also = [
  "iterators",
  "iterator-vs-iterable",
  "for-loops",
]
+++

Python's `for` statement consumes values from any iterable object: lists, strings, dictionaries, ranges, generators, files, and many standard-library helpers.

This makes iteration a value-stream protocol rather than a special case for arrays. The producer decides how values are made, and the loop consumes them one at a time.

Use `enumerate()` when you need positions and values together, and `dict.items()` when you need keys and values. These helpers express intent better than manual indexing.

:::program
```python
names = ["Ada", "Grace", "Guido"]

for name in names:
    print(name)

for index, name in enumerate(names):
    print(index, name)

scores = {"Ada": 10, "Grace": 9}
for name, score in scores.items():
    print(name, score)
```
:::

:::cell
Start with an ordinary list. A list stores values, and a `for` loop asks it for one value at a time.

When you only need the values, iterate over the collection directly. There is no index variable because the loop body does not need one.

```python
names = ["Ada", "Grace", "Guido"]

for name in names:
    print(name)
```

```output
Ada
Grace
Guido
```
:::

:::cell
When you need both a position and a value, use `enumerate()`. It produces index/value pairs without manual indexing.

```python
for index, name in enumerate(names):
    print(index, name)
```

```output
0 Ada
1 Grace
2 Guido
```
:::

:::cell
Dictionaries are iterable too, but `dict.items()` is the clearest way to say that the loop needs keys and values together.

```python
scores = {"Ada": 10, "Grace": 9}
for name, score in scores.items():
    print(name, score)
```

```output
Ada 10
Grace 9
```
:::

:::note
- A `for` loop consumes values from an iterable.
- Different producers can feed the same loop protocol.
- Prefer `enumerate()` over `range(len(...))` when you need an index.
:::
