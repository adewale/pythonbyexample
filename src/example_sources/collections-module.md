+++
slug = "collections-module"
title = "Collections Module"
section = "Collections"
summary = "collections provides specialized containers for common data shapes."
doc_path = "/library/collections.html"
+++

collections provides specialized containers for common data shapes. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

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
Use `Counter` when counting is the data shape.

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

```output
[('a', 3), ('n', 2)]
{'red': ['Ada', 'Lin'], 'blue': ['Grace']}
first
2
```
:::

:::note
- Use `Counter` when counting is the data shape.
- Use `defaultdict` when grouping values by key.
- Use `deque` for efficient queue operations and `namedtuple` for lightweight named records.
:::
