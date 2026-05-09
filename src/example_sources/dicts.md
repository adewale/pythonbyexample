+++
slug = "dicts"
title = "Dictionaries"
section = "Collections"
summary = "Dictionaries map keys to values for records, lookup, and structured data."
doc_path = "/tutorial/datastructures.html#dictionaries"
+++

Dictionaries are Python's built-in mapping type. They exist for data where names or keys are more meaningful than numeric positions: records, lookup tables, counters, and JSON-like payloads.

Use direct indexing when a key is required. Use `get()` when absence is expected and the code has a reasonable fallback.

Unlike lists, dictionaries answer “what value belongs to this key?” rather than “what value is at this position?” Iterating with `items()` keeps each key next to its value.

:::program
```python
profile = {"name": "Ada", "language": "Python"}
profile["year"] = 1843
print(profile["name"])
print(profile.get("timezone", "UTC"))

scores = {"Ada": 10, "Grace": 9}
print(scores["Grace"])
print(scores.get("Guido", 0))

for name, score in scores.items():
    print(f"{name}: {score}")

inventory = {"apple": 0, "pear": 3, "plum": 0}
for name in list(inventory.keys()):
    if inventory[name] == 0:
        del inventory[name]
print(inventory)
```
:::

:::cell
Use a dictionary as a small record when fields have names. Direct indexing communicates that the key is required, while `get()` communicates that a missing key has a fallback.

```python
profile = {"name": "Ada", "language": "Python"}
profile["year"] = 1843
print(profile["name"])
print(profile.get("timezone", "UTC"))
```

```output
Ada
UTC
```
:::

:::cell
Use a dictionary as a lookup table when keys identify values. This is different from a list, where numeric position is the lookup key.

```python
scores = {"Ada": 10, "Grace": 9}
print(scores["Grace"])
print(scores.get("Guido", 0))
```

```output
9
0
```
:::

:::cell
Use `items()` when the loop needs both keys and values. It avoids looping over keys and then indexing back into the dictionary.

```python
for name, score in scores.items():
    print(f"{name}: {score}")
```

```output
Ada: 10
Grace: 9
```
:::

:::cell
Mutating a dictionary while iterating it raises `RuntimeError`. Snapshot the keys with `list(d.keys())` (or build a list of changes and apply them after the loop) so the iteration sees a stable view.

```python
inventory = {"apple": 0, "pear": 3, "plum": 0}
for name in list(inventory.keys()):
    if inventory[name] == 0:
        del inventory[name]
print(inventory)
```

```output
{'pear': 3}
```
:::

:::note
- Dictionaries preserve insertion order in modern Python.
- Use `get()` when a missing key has a reasonable default.
- Use direct indexing when a missing key should be treated as an error.
- Snapshot keys with `list(d.keys())` before deleting items in a loop; mutating during iteration raises `RuntimeError`.
:::
