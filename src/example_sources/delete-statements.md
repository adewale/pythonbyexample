+++
slug = "delete-statements"
title = "Delete Statements"
section = "Data Model"
summary = "del removes bindings, items, and attributes rather than producing a value."
doc_path = "/reference/simple_stmts.html#the-del-statement"
see_also = [
  "variables",
  "dicts",
  "mutability",
]
+++

`del` removes a binding or an item. It is a statement, not a function, and it does not return the removed value.

Use `del name` when a name should no longer be bound. Use `del mapping[key]` or `del sequence[index]` when mutating a container by removing one part.

This is different from assigning `None`: `None` is still a value, while `del` removes the binding or slot.

:::program
```python
profile = {"name": "Ada", "temporary": True}
del profile["temporary"]
print(profile)

items = ["a", "b", "c"]
del items[1]
print(items)

value = "cached"
del value
print("value" in locals())
```
:::

:::cell
Deleting a dictionary key mutates the dictionary. The key is gone; it has not been set to `None`.

```python
profile = {"name": "Ada", "temporary": True}
del profile["temporary"]
print(profile)
```

```output
{'name': 'Ada'}
```
:::

:::cell
Deleting a list item removes that position and shifts later items left.

```python
items = ["a", "b", "c"]
del items[1]
print(items)
```

```output
['a', 'c']
```
:::

:::cell
Deleting a name removes the binding from the current namespace. It is different from rebinding the name to `None`.

```python
value = "cached"
del value
print("value" in locals())
```

```output
False
```
:::

:::note
- `del` removes bindings or container entries.
- Assign `None` when absence should remain an explicit value.
- Use container methods such as `pop()` when you need the removed value back.
:::
