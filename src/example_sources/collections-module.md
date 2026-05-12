+++
slug = "collections-module"
title = "Collections Module"
section = "Collections"
summary = "collections provides specialized containers for common data shapes."
doc_path = "/library/collections.html"
see_also = [
  "dicts",
  "lists",
  "tuples",
  "sets",
]
+++

`collections` provides specialized containers for common shapes that would otherwise require repetitive plumbing. Use it when the shape has a name: counting, grouping, queueing, or lightweight records.

These types are not replacements for `list`, `dict`, `tuple`, and `set`. They are small standard-library tools for cases where an ordinary container would hide the intent behind manual bookkeeping.

The examples below map each type to the question it answers.

:::program
```python
from collections import Counter, defaultdict, deque, namedtuple

counts = Counter("banana")
print(counts.most_common(2))

groups = defaultdict(list)
for name, team in [("Ada", "red"), ("Grace", "blue"), ("Lin", "red")]:
    groups[team].append(name)
print(dict(groups))

queue = deque(["first"])
queue.append("second")
print(queue.popleft())

Point = namedtuple("Point", "x y")
print(Point(2, 3).x)
```
:::

:::cell
Use `Counter` when the question is "how many times did each value appear?"

```python
from collections import Counter

counts = Counter("banana")
print(counts.most_common(2))
```

```output
[('a', 3), ('n', 2)]
```
:::

:::cell
Use `defaultdict(list)` when each key gathers multiple values and the missing-key case should create an empty list automatically.

```python
from collections import defaultdict

groups = defaultdict(list)
for name, team in [("Ada", "red"), ("Grace", "blue"), ("Lin", "red")]:
    groups[team].append(name)
print(dict(groups))
```

```output
{'red': ['Ada', 'Lin'], 'blue': ['Grace']}
```
:::

:::cell
Use `deque` for queue operations at both ends, and `namedtuple` when a tiny immutable record needs names as well as positions.

```python
from collections import deque, namedtuple

queue = deque(["first"])
queue.append("second")
print(queue.popleft())

Point = namedtuple("Point", "x y")
print(Point(2, 3).x)
```

```output
first
2
```
:::

:::note
- `Counter` counts, `defaultdict` groups, `deque` queues, and `namedtuple` names record fields.
- Prefer the built-in containers until a specialized shape makes the code clearer.
- For new structured records with defaults and methods, consider `dataclasses` instead of `namedtuple`.
:::
