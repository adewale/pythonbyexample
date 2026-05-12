+++
slug = "sorting"
title = "Sorting"
section = "Collections"
summary = "sorted returns a new ordered list and key functions choose the sort value."
doc_path = "/howto/sorting.html"
see_also = [
  "lists",
  "lambdas",
  "functions",
]
+++

`sorted()` accepts any iterable and returns a new list. The original collection is left untouched, which makes `sorted()` useful in expressions and pipelines.

Use `key=` to say what value should be compared for each item. This is the idiomatic way to sort records, tuples, dictionaries, and objects by a field.

Use `reverse=True` for descending order. Use `list.sort()` instead when you intentionally want to mutate an existing list in place.

:::program
```python
names = ["Guido", "Ada", "Grace"]
print(sorted(names))
print(names)

users = [
    {"name": "Ada", "score": 10},
    {"name": "Guido", "score": 8},
    {"name": "Grace", "score": 10},
]
ranked = sorted(users, key=lambda user: user["score"], reverse=True)
print([user["name"] for user in ranked])

users.sort(key=lambda user: user["name"])
print([user["name"] for user in users])
```
:::

:::cell
`sorted()` returns a new list. Printing the original list afterward shows that the input order did not change.

```python
names = ["Guido", "Ada", "Grace"]
print(sorted(names))
print(names)
```

```output
['Ada', 'Grace', 'Guido']
['Guido', 'Ada', 'Grace']
```
:::

:::cell
A key function computes the value to compare. Here the records are sorted by score, highest first, and the output shows the resulting order.

```python
users = [
    {"name": "Ada", "score": 10},
    {"name": "Guido", "score": 8},
    {"name": "Grace", "score": 10},
]
ranked = sorted(users, key=lambda user: user["score"], reverse=True)
print([user["name"] for user in ranked])
```

```output
['Ada', 'Grace', 'Guido']
```
:::

:::cell
`list.sort()` sorts the list in place. Use it when mutation is the point and no separate sorted copy is needed.

```python
users.sort(key=lambda user: user["name"])
print([user["name"] for user in users])
```

```output
['Ada', 'Grace', 'Guido']
```
:::

:::note
- `sorted()` makes a new list; `list.sort()` mutates an existing list.
- `key=` should return the value Python compares for each item.
- Python's sort is stable, so equal keys keep their original relative order.
:::
