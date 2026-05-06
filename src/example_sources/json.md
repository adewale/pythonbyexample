+++
slug = "json"
title = "JSON"
section = "Standard Library"
summary = "json encodes Python values as JSON text and decodes them back."
doc_path = "/library/json.html"
+++

The `json` module converts between Python values and JSON text. Dictionaries, lists, strings, numbers, booleans, and `None` map naturally to JSON structures.

Use `dumps()` when you need a string and `loads()` when you need Python objects back. Deterministic options such as `sort_keys=True` make output stable for examples, tests, and caches.

JSON is a data format, not a way to preserve arbitrary Python objects. Encode simple data structures at service boundaries and decode them before using the values.

:::program
```python
import json

payload = {"language": "Python", "versions": [3, 13], "stable": True}
text = json.dumps(payload, sort_keys=True)
print(text)

decoded = json.loads(text)
print(decoded["language"])
print(decoded["stable"])
```
:::

:::cell
`dumps()` encodes Python data as JSON text. `sort_keys=True` keeps dictionary keys in a stable order for reproducible output.

```python
import json

payload = {"language": "Python", "versions": [3, 13], "stable": True}
text = json.dumps(payload, sort_keys=True)
print(text)
```

```output
{"language": "Python", "stable": true, "versions": [3, 13]}
```
:::

:::cell
`loads()` decodes JSON text back into Python values. JSON booleans become Python booleans, arrays become lists, and objects become dictionaries.

```python
decoded = json.loads(text)
print(decoded["language"])
print(decoded["stable"])
```

```output
Python
True
```
:::

:::note
- `dumps()` returns a string; `loads()` accepts a string.
- JSON `true`, `false`, and `null` become Python `True`, `False`, and `None`.
- Use `sort_keys=True` when stable text output matters.
:::
