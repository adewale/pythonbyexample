+++
slug = "json"
title = "JSON"
section = "Standard Library"
summary = "json encodes Python values as JSON text and decodes them back."
doc_path = "/library/json.html"
see_also = [
  "dicts",
  "typed-dicts",
  "strings",
]
+++

The `json` module converts between Python values and JSON text. Dictionaries, lists, strings, numbers, booleans, and `None` map naturally to JSON structures.

Use `dumps()` when you need a string and `loads()` when you need Python objects back. Options such as `sort_keys=True` and `indent=2` control stable, readable output.

JSON is a data format, not a way to preserve arbitrary Python objects. Encode simple data structures at service boundaries, and expect decode errors when the incoming text is not valid JSON.

:::program
```python
import json

payload = {"language": "Python", "versions": [3, 13], "stable": True, "missing": None}
text = json.dumps(payload, sort_keys=True)
print(text)

pretty = json.dumps({"language": "Python", "stable": True}, indent=2, sort_keys=True)
print(pretty.splitlines()[0])
print(pretty.splitlines()[1])

decoded = json.loads(text)
print(decoded["language"])
print(decoded["missing"] is None)

try:
    json.loads("{bad json}")
except json.JSONDecodeError as error:
    print(error.__class__.__name__)
```
:::

:::cell
`dumps()` encodes Python data as JSON text. `sort_keys=True` keeps dictionary keys in a stable order for reproducible output.

```python
import json

payload = {"language": "Python", "versions": [3, 13], "stable": True, "missing": None}
text = json.dumps(payload, sort_keys=True)
print(text)
```

```output
{"language": "Python", "missing": null, "stable": true, "versions": [3, 13]}
```
:::

:::cell
Formatting options change the JSON text, not the Python value. `indent=2` is useful for human-readable output.

```python
pretty = json.dumps({"language": "Python", "stable": True}, indent=2, sort_keys=True)
print(pretty.splitlines()[0])
print(pretty.splitlines()[1])
```

```output
{
  "language": "Python",
```
:::

:::cell
`loads()` decodes JSON text back into Python values. JSON `null` becomes Python `None`.

```python
decoded = json.loads(text)
print(decoded["language"])
print(decoded["missing"] is None)
```

```output
Python
True
```
:::

:::cell
Invalid JSON raises `JSONDecodeError`, so input boundaries should handle decode failures explicitly.

```python
try:
    json.loads("{bad json}")
except json.JSONDecodeError as error:
    print(error.__class__.__name__)
```

```output
JSONDecodeError
```
:::

:::note
- `dumps()` returns a string; `loads()` accepts a string.
- JSON `true`, `false`, and `null` become Python `True`, `False`, and `None`.
- Use `sort_keys=True` when stable text output matters.
- JSON only represents data shapes, not arbitrary Python objects or behavior.
:::
