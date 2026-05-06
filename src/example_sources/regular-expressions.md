+++
slug = "regular-expressions"
title = "Regular Expressions"
section = "Text"
summary = "The re module searches and extracts text using regular expressions."
doc_path = "/library/re.html"
+++

Regular expressions are a compact language for searching and extracting text patterns. Python's re module provides the standard interface.

Regex is powerful for structured text with repeated patterns, such as names followed by numbers. Capturing groups return just the pieces you care about.

They are not always the right tool. Prefer ordinary string methods when the pattern is simple, because simpler code is easier to maintain.

:::cell
Regular expressions are a compact language for searching and extracting text patterns. Python's re module provides the standard interface.

Regex is powerful for structured text with repeated patterns, such as names followed by numbers. Capturing groups return just the pieces you care about.

They are not always the right tool. Prefer ordinary string methods when the pattern is simple, because simpler code is easier to maintain.

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
They are not always the right tool. Prefer ordinary string methods when the pattern is simple, because simpler code is easier to maintain.

```python
print(bool(re.search(r"Grace", text)))
```

```output
True
```
:::

:::note
- Use raw strings for regex patterns so backslashes are easier to read.
- For simple substring checks, ordinary string methods are often clearer than regex.
:::
