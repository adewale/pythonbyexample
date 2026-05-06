+++
slug = "itertools"
title = "Itertools"
section = "Iteration"
summary = "itertools provides efficient iterator building blocks."
doc_path = "/library/itertools.html"
+++

The itertools module contains iterator building blocks for combining, slicing, grouping, and repeating streams of values. These tools pair naturally with for loops and generators.

Many itertools functions are lazy, including count() and chain(). Use helpers such as islice() to take a finite window from an infinite iterator.

Iterator pipelines avoid building intermediate lists. Use islice to take a finite piece from an infinite iterator.

:::cell
The itertools module contains iterator building blocks for combining, slicing, grouping, and repeating streams of values. These tools pair naturally with for loops and generators.

Many itertools functions are lazy, including count() and chain(). Use helpers such as islice() to take a finite window from an infinite iterator.

```python
import itertools

print(list(itertools.islice(itertools.count(10), 3)))
print(list(itertools.chain([1, 2], [3])))
```

```output
[10, 11, 12]
[1, 2, 3]
```
:::

:::note
- Iterator pipelines avoid building intermediate lists.
- Use islice to take a finite piece from an infinite iterator.
:::
