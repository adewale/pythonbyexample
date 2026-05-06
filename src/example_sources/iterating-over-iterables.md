+++
slug = "iterating-over-iterables"
title = "Iterating over Iterables"
section = "Iteration"
summary = "for loops work with any iterable, not just numeric ranges."
doc_path = "/tutorial/controlflow.html#for-statements"
+++

The for statement works with any iterable object: lists, strings, dictionaries, generators, files, and many standard-library helpers. This makes iteration a central Python protocol rather than a special case for arrays.

Use enumerate() when you need positions and values together, and dict.items() when you need keys and values. These helpers express intent better than manual indexing.

Python's for statement consumes iterables through the iterator protocol. Prefer enumerate() over range(len(...)) when you need an index.

:::cell
Start with an ordinary list. A list is iterable, so a for loop can ask it for one value at a time.

When you only need the values, iterate over the collection directly. There is no index variable because the loop body does not need one.

```python
names = ["Ada", "Grace", "Guido"]

# Iterate over values directly.
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
When you need both a position and a value, use enumerate(). It keeps the counter tied to iteration without manual indexing.

```python
# enumerate adds a counter without manual indexing.
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
Dictionaries are iterable too, but dict.items() is the clearest way to say that the loop needs keys and values together.

```python
scores = {"Ada": 10, "Grace": 9}

# items yields key/value pairs from a dictionary.
for name, score in scores.items():
    print(name, score)
```

```output
Ada 10
Grace 9
```
:::

:::note
- Python's for statement consumes iterables through the iterator protocol.
- Prefer enumerate() over range(len(...)) when you need an index.
:::
