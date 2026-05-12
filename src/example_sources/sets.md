+++
slug = "sets"
title = "Sets"
section = "Collections"
summary = "Sets store unique values and make membership checks explicit."
doc_path = "/tutorial/datastructures.html#sets"
see_also = [
  "lists",
  "dicts",
  "comprehensions",
]
+++

Sets store unique hashable values. Use them when membership and de-duplication matter more than order.

A list can answer membership with `in`, but a set communicates that membership is the main operation. Set algebra then expresses how groups relate to each other.

Because sets are unordered, examples often wrap output in `sorted()` so the display is deterministic.

:::program
```python
languages = ["python", "go", "python"]
unique_languages = set(languages)
print(sorted(unique_languages))

allowed = {"python", "rust"}
print("python" in allowed)
print("ruby" in allowed)

compiled = {"go", "rust"}
print(sorted(allowed | compiled))
print(sorted(allowed & compiled))
print(sorted(allowed - compiled))
```
:::

:::cell
Creating a set removes duplicates. Keep a list when order and repeated values matter; convert to a set when uniqueness is the point.

```python
languages = ["python", "go", "python"]
unique_languages = set(languages)
print(sorted(unique_languages))
```

```output
['go', 'python']
```
:::

:::cell
Membership checks are the everyday set operation. A list can also use `in`, but a set says that membership is central to the data shape.

```python
allowed = {"python", "rust"}
print("python" in allowed)
print("ruby" in allowed)
```

```output
True
False
```
:::

:::cell
Union, intersection, and difference describe relationships between groups without manual loops.

```python
compiled = {"go", "rust"}
print(sorted(allowed | compiled))
print(sorted(allowed & compiled))
print(sorted(allowed - compiled))
```

```output
['go', 'python', 'rust']
['rust']
['python']
```
:::

:::note
- Use lists when order and repeated values matter.
- Use sets when uniqueness and membership are the main operations.
- Prefer lists when order or repeated values are part of the meaning.
- Sets are unordered, so sort them when examples need deterministic display.
:::
