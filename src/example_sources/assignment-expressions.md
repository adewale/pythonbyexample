+++
slug = "assignment-expressions"
title = "Assignment Expressions"
section = "Control Flow"
summary = "The walrus operator assigns a value inside an expression."
doc_path = "/reference/expressions.html#assignment-expressions"
see_also = [
  "conditionals",
  "while-loops",
  "variables",
]
+++

The assignment expression operator `:=` assigns a name while evaluating an expression. It is often called the walrus operator.

Use it when computing a value and testing it are naturally one step. Avoid it when a separate assignment would make the code easier to read.

The boundary is readability: the walrus operator can remove duplication, but it should not hide important state changes.

:::program
```python
messages = ["hello", "", "python"]

for message in messages:
    if length := len(message):
        print(message, length)

queue = ["retry", "ok"]
while (status := queue.pop(0)) != "ok":
    print(status)
print(status)
```
:::

:::cell
An assignment expression can name a computed value while a condition tests it. Here empty strings are skipped because their length is zero.

```python
messages = ["hello", "", "python"]

for message in messages:
    if length := len(message):
        print(message, length)
```

```output
hello 5
python 6
```
:::

:::cell
The same idea works in loops that read state until a sentinel appears. The assignment and comparison stay together.

```python
queue = ["retry", "ok"]
while (status := queue.pop(0)) != "ok":
    print(status)
print(status)
```

```output
retry
ok
```
:::

:::note
- `name := expression` assigns and evaluates to the assigned value.
- Use it to avoid computing the same value twice.
- Prefer a normal assignment when the expression becomes hard to scan.
:::
