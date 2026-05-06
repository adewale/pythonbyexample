+++
slug = "string-formatting"
title = "String Formatting"
section = "Text"
summary = "f-strings format values directly inside string literals."
doc_path = "/tutorial/inputoutput.html#formatted-string-literals"
+++

Formatted string literals, or f-strings, are the everyday way to combine text with Python expressions. They keep the expression close to the words it explains.

Format specifications after `:` control presentation details such as width, alignment, padding, and precision. This is useful for reports and aligned terminal output.

The debug form with `=` is convenient while learning because it prints both the expression and its value without writing the name twice.

:::program
```python
name = "Ada"
score = 9.5

print(f"{name} scored {score}")
print(f"{name:>8} | {score:05.1f}")
print(f"{score = }")
```
:::

:::cell
An f-string evaluates expressions inside braces and inserts their string form into the surrounding text.

```python
name = "Ada"
score = 9.5

print(f"{name} scored {score}")
```

```output
Ada scored 9.5
```
:::

:::cell
Format specifications after `:` control presentation. Here the name is right-aligned and the score is padded with one decimal place.

```python
print(f"{name:>8} | {score:05.1f}")
```

```output
     Ada | 009.5
```
:::

:::cell
The debug form `name =` is handy while learning or logging because it prints both the expression and the value.

```python
print(f"{score = }")
```

```output
score = 9.5
```
:::

:::note
- Use `f"..."` strings for most new formatting code.
- Format specifications after `:` control alignment, width, padding, and precision.
:::
