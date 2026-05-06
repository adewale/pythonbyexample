+++
slug = "comprehensions"
title = "Comprehensions"
section = "Collections"
summary = "Comprehensions build collections by mapping and filtering iterables."
doc_path = "/tutorial/datastructures.html#list-comprehensions"
+++

Comprehensions are expression forms for building collections from iterables. Read them from left to right: produce this value, for each item, optionally only when a condition is true.

They are best for direct transformations where the expression is still easy to scan. When the work needs several statements or names, an explicit loop is usually clearer.

Comprehensions can build lists, dictionaries, and sets. Prefer them when the output shape is obvious from the expression.

:::program
```python
names = ["ada", "guido", "grace"]
titled = [name.title() for name in names]
print(titled)

scores = {"Ada": 10, "Guido": 8, "Grace": 10}
high_scores = {name: score for name, score in scores.items() if score >= 10}
print(high_scores)

unique_scores = {score for score in scores.values()}
print(unique_scores)
```
:::

:::cell
A list comprehension maps each input item to one output item. This one calls `title()` for every name and collects the results in a new list.

```python
names = ["ada", "guido", "grace"]
titled = [name.title() for name in names]
print(titled)
```

```output
['Ada', 'Guido', 'Grace']
```
:::

:::cell
Add an `if` clause when only some items should appear. A dictionary comprehension can transform key/value pairs while preserving the dictionary shape.

```python
scores = {"Ada": 10, "Guido": 8, "Grace": 10}
high_scores = {name: score for name, score in scores.items() if score >= 10}
print(high_scores)
```

```output
{'Ada': 10, 'Grace': 10}
```
:::

:::cell
A set comprehension keeps only unique results. Here two people have the same score, so the resulting set has two values.

```python
unique_scores = {score for score in scores.values()}
print(unique_scores)
```

```output
{8, 10}
```
:::

:::note
- The left side says what to produce; the `for` clause says where values come from.
- Use an `if` clause for simple filters.
- Switch to a loop when the transformation needs multiple steps or explanations.
:::
