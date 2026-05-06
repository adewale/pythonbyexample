+++
slug = "dicts"
title = "Dictionaries"
section = "Collections"
summary = "Dictionaries map keys to values."
doc_path = "/tutorial/datastructures.html#dictionaries"
+++

Dictionaries are Python's built-in mapping type. They connect keys to values and are the natural shape for records, lookup tables, and JSON-like data.

Direct indexing communicates that a key must exist. `get()` communicates that absence is expected and supplies a default value.

Iterating with `items()` gives each key and value together, which is clearer than looping over keys and indexing again.

:::program
```python
profile = {"name": "Ada", "language": "Python"}
profile["year"] = 1843

print(profile["name"])
print(profile.get("timezone", "UTC"))

for key, value in profile.items():
    print(f"{key}: {value}")
```
:::

:::cell
Create a dictionary with literal key/value pairs, then add another key by assignment.

Use `[]` for required keys and `get()` when a missing key can use a default.

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
Use `items()` when the loop needs both the key and the value.

```python
for key, value in profile.items():
    print(f"{key}: {value}")
```

```output
name: Ada
language: Python
year: 1843
```
:::

:::note
- Dictionaries preserve insertion order in modern Python.
- Use `get()` when a missing key has a reasonable default.
- Use direct indexing when a missing key should be treated as an error.
:::
