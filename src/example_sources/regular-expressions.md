+++
slug = "regular-expressions"
title = "Regular Expressions"
section = "Text"
summary = "The re module searches and extracts text using regular expressions."
doc_path = "/library/re.html"
+++

Regular expressions are a compact language for searching and extracting text patterns. Python's `re` module provides the standard interface.

Use regex when the pattern has structure: repeated records, alternatives, optional parts, or pieces you want to capture. Prefer ordinary string methods for simple substring checks because simpler code is easier to maintain.

This page is a first regex pass, not the whole language. It focuses on raw pattern strings, capturing groups, repeated matches, and the boundary where a string method is enough.

:::program
```python
import re

text = "Ada: 10, Grace: 9"
pattern = r"([A-Za-z]+): (\d+)"

for name, score in re.findall(pattern, text):
    print(name, int(score))

match = re.search(r"Grace: (\d+)", text)
print(match.group(1))
print("Grace" in text)
```
:::

:::cell
Raw strings keep backslashes readable in regex patterns. Capturing groups return just the pieces inside parentheses.

```python
import re

text = "Ada: 10, Grace: 9"
pattern = r"([A-Za-z]+): (\d+)"

for name, score in re.findall(pattern, text):
    print(name, int(score))
```

```output
Ada 10
Grace 9
```
:::

:::cell
`re.search()` finds the first match. A match object exposes captured groups by position.

```python
match = re.search(r"Grace: (\d+)", text)
print(match.group(1))
```

```output
9
```
:::

:::cell
For a simple substring check, ordinary string membership is clearer than regex.

```python
print("Grace" in text)
```

```output
True
```
:::

:::note
- Use raw strings for regex patterns so backslashes are easier to read.
- Use capturing groups when the point is extraction, not just matching.
- Reach for string methods before regex when the pattern is simple.
:::
