+++
slug = "json"
title = "JSON"
section = "Standard Library"
summary = "json encodes and decodes JSON data."
doc_path = "/library/json.html"
+++

The json module converts between Python values and JSON text. Dictionaries, lists, strings, numbers, booleans, and None map naturally to JSON structures.

Use dumps() when you need a string and loads() when you need Python objects back. Deterministic options such as sort_keys make output stable for examples and tests.

JSON maps naturally to dicts, lists, strings, numbers, booleans, and None. Use sort_keys for deterministic output.

:::program
```python
import json

data = {"language": "Python", "versions": [3, 13]}
text = json.dumps(data, sort_keys=True)
print(text)
print(json.loads(text)["language"])
```
:::

:::cell
The json module converts between Python values and JSON text. Dictionaries, lists, strings, numbers, booleans, and None map naturally to JSON structures.

Use dumps() when you need a string and loads() when you need Python objects back. Deterministic options such as sort_keys make output stable for examples and tests.

```python
import json

data = {"language": "Python", "versions": [3, 13]}
text = json.dumps(data, sort_keys=True)
print(text)
print(json.loads(text)["language"])
```

```output
{"language": "Python", "versions": [3, 13]}
Python
```
:::

:::note
- JSON maps naturally to dicts, lists, strings, numbers, booleans, and None.
- Use sort_keys for deterministic output.
:::
