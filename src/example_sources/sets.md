+++
slug = "sets"
title = "Sets"
section = "Collections"
summary = "Sets store unique values and support set algebra."
doc_path = "/tutorial/datastructures.html#sets"
+++

Sets store unique hashable values. Use them when membership and de-duplication matter more than order.

The `in` operator is the everyday membership test. Set algebra then expresses how groups relate to each other.

Because sets are unordered, examples often wrap output in `sorted()` so the display is deterministic.

:::program
```python
languages = {"python", "go", "python"}
compiled = {"go", "rust"}

print(sorted(languages))
print("python" in languages)
print(sorted(languages | compiled))
print(sorted(languages & compiled))
print(sorted(languages - compiled))
```
:::

:::cell
Creating a set automatically removes duplicates. The repeated `python` value appears only once.

```python
languages = {"python", "go", "python"}
compiled = {"go", "rust"}

print(sorted(languages))
```

```output
['go', 'python']
```
:::

:::cell
Membership checks are the most common set operation.

```python
print("python" in languages)
```

```output
True
```
:::

:::cell
Union, intersection, and difference describe relationships between groups without manual loops.

```python
print(sorted(languages | compiled))
print(sorted(languages & compiled))
print(sorted(languages - compiled))
```

```output
['go', 'python', 'rust']
['go']
['python']
```
:::

:::note
- Sets remove duplicates and support fast membership tests.
- Set algebra operators make union, intersection, and difference explicit.
- Sets are unordered, so sort them when examples need deterministic display.
:::
