+++
slug = "string-formatting"
title = "String Formatting"
section = "Text"
summary = "f-strings turn values into readable text at the point of use."
doc_path = "/tutorial/inputoutput.html#formatted-string-literals"
see_also = [
  "strings",
  "logging",
  "csv-data",
  "values",
]
+++

Formatted string literals, or f-strings, exist because programs constantly need to turn values into human-readable text. They keep the expression next to the words it explains.

Format specifications after `:` control presentation details such as width, alignment, padding, and precision. This separates the value being computed from the way it should be displayed.

Use f-strings for most new formatting code. They relate directly to expressions: anything inside braces is evaluated, then formatted into the surrounding string.

:::program
```python
name = "Ada"
score = 9.5
rank = 1

message = f"{name} scored {score}"
print(message)

row = f"{rank:>2} | {name:<8} | {score:05.1f}"
print(row)

print(f"{score = }")
```
:::

:::cell
An f-string evaluates expressions inside braces and inserts their string form into the surrounding text. This is clearer than joining several converted values by hand.

```python
name = "Ada"
score = 9.5
rank = 1

message = f"{name} scored {score}"
print(message)
```

```output
Ada scored 9.5
```
:::

:::cell
Format specifications after `:` control display without changing the underlying values. Here the rank is right-aligned, the name is left-aligned, and the score is padded to one decimal place.

```python
row = f"{rank:>2} | {name:<8} | {score:05.1f}"
print(row)
```

```output
 1 | Ada      | 009.5
```
:::

:::cell
The debug form with `=` is useful while learning or logging because it prints both the expression and the value.

```python
print(f"{score = }")
```

```output
score = 9.5
```
:::

:::note
- Use `f"..."` strings for most new formatting code.
- Expressions inside braces are evaluated before formatting.
- Format specifications after `:` control alignment, width, padding, and precision.
:::
