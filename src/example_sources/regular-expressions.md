+++
slug = "regular-expressions"
title = "Regular Expressions"
section = "Text"
summary = "The re module searches and extracts text using regular expressions."
doc_path = "/library/re.html"
see_also = [
  "strings",
  "string-formatting",
]
+++

Regular expressions are a compact language for searching and extracting text patterns. Python's `re` module provides the standard interface: `re.match` anchors at the start of the string, `re.search` finds the first occurrence anywhere, `re.findall` collects every match, `re.sub` rewrites matches, and `re.compile` reuses a pattern.

Use regex when the pattern has structure: repeated records, alternatives, optional parts, or pieces you want to capture. Prefer ordinary string methods for simple substring checks because simpler code is easier to maintain.

Flags such as `re.IGNORECASE` adjust matching behavior without rewriting the pattern. Pair them with `re.compile` when the same pattern is used repeatedly.

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

start = re.match(r"Ada", text)
print(start is not None)
print(re.match(r"Grace", text))

scoreline = re.compile(pattern)
print(scoreline.findall(text))

casey = "ADA: 11"
print(re.search(r"ada", casey, flags=re.IGNORECASE).group(0))

print(re.sub(r"\d+", "?", text))
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

:::cell
`re.match` only matches at the start of the string; `re.search` finds the first match anywhere. Picking the right one keeps anchoring intent visible without an explicit `^`.

```python
start = re.match(r"Ada", text)
print(start is not None)
print(re.match(r"Grace", text))
```

```output
True
None
```
:::

:::cell
`re.compile` produces a reusable pattern object whose methods skip the parser on each call. Reach for it when the same pattern runs in a loop.

```python
scoreline = re.compile(pattern)
print(scoreline.findall(text))
```

```output
[('Ada', '10'), ('Grace', '9')]
```
:::

:::cell
Flags such as `re.IGNORECASE` adjust matching without changing the pattern. `re.sub` replaces every match with a replacement string and returns the rewritten text.

```python
casey = "ADA: 11"
print(re.search(r"ada", casey, flags=re.IGNORECASE).group(0))

print(re.sub(r"\d+", "?", text))
```

```output
ADA
Ada: ?, Grace: ?
```
:::

:::note
- Use raw strings for regex patterns so backslashes are easier to read.
- Use capturing groups when the point is extraction, not just matching.
- `re.match` anchors at the start; `re.search` finds the first match anywhere.
- `re.compile` saves work when the pattern runs more than once.
- `re.sub` rewrites matches; flags like `re.IGNORECASE` change matching behavior without rewriting the pattern.
- Reach for string methods before regex when the pattern is simple.
:::
