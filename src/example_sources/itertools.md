+++
slug = "itertools"
title = "Itertools"
section = "Iteration"
summary = "itertools provides lazy iterator building blocks."
doc_path = "/library/itertools.html"
+++

The `itertools` module contains iterator building blocks for combining, slicing, grouping, and repeating streams of values. These tools pair naturally with `for` loops and generators.

Many `itertools` functions are lazy. They describe work to do later instead of building a list immediately, so helpers such as `islice()` are useful when taking a finite window.

Iterator pipelines let each step stay small. Convert to `list()` only at the edge when you need to display, store, or reuse the results.

:::program
```python
import itertools

counter = itertools.count(10)
print(list(itertools.islice(counter, 3)))

pages = itertools.chain(["intro", "setup"], ["deploy"])
print(list(pages))

scores = [7, 10, 8, 10]
high_scores = itertools.compress(scores, [score >= 9 for score in scores])
print(list(high_scores))
```
:::

:::cell
`count()` can produce values forever, so `islice()` takes a finite window. Nothing is materialized until `list()` consumes the iterator.

```python
import itertools

counter = itertools.count(10)
print(list(itertools.islice(counter, 3)))
```

```output
[10, 11, 12]
```
:::

:::cell
`chain()` presents several iterables as one stream. This avoids building an intermediate list just to loop over combined inputs.

```python
pages = itertools.chain(["intro", "setup"], ["deploy"])
print(list(pages))
```

```output
['intro', 'setup', 'deploy']
```
:::

:::cell
Iterator helpers compose with ordinary Python expressions. `compress()` keeps items whose corresponding selector is true.

```python
scores = [7, 10, 8, 10]
high_scores = itertools.compress(scores, [score >= 9 for score in scores])
print(list(high_scores))
```

```output
[10, 10]
```
:::

:::note
- Iterator pipelines avoid building intermediate lists.
- Use `islice()` to take a finite piece from an infinite iterator.
- Convert to a list only when you need concrete results.
:::
