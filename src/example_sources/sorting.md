+++
slug = "sorting"
title = "Sorting"
section = "Collections"
summary = "sorted returns a new ordered list from any iterable."
doc_path = "/howto/sorting.html"
+++

sorted() accepts any iterable and returns a new list in sorted order. The original collection is left untouched, which makes it safe to use in expressions.

The key function tells Python what value to compare for each item. This is the idiomatic way to sort dictionaries, objects, and tuples by a specific field.

key functions compute values to sort by. list.sort() sorts a list in place.

:::program
```python
users = [{"name": "Ada", "score": 10}, {"name": "Guido", "score": 8}]
ranked = sorted(users, key=lambda user: user["score"], reverse=True)
print(ranked[0]["name"])
```
:::

:::cell
sorted() accepts any iterable and returns a new list in sorted order. The original collection is left untouched, which makes it safe to use in expressions.

```python
users = [{"name": "Ada", "score": 10}, {"name": "Guido", "score": 8}]
ranked = sorted(users, key=lambda user: user["score"], reverse=True)
print(ranked[0]["name"])
```

```output
Ada
```
:::

:::note
- key functions compute values to sort by.
- list.sort() sorts a list in place.
:::
