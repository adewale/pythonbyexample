+++
slug = "advanced-match-patterns"
title = "Advanced Match Patterns"
section = "Control Flow"
summary = "match patterns can destructure sequences, combine alternatives, and add guards."
doc_path = "/tutorial/controlflow.html#match-statements"
see_also = [
  "match-statements",
  "tuples",
  "classes",
]
+++

Structural pattern matching is more than equality checks. Patterns can destructure sequences, match several alternatives, capture the rest of a sequence, and use guards.

Use these forms when the shape of data is the decision. If the decision is only a single boolean condition, ordinary `if` statements are usually clearer.

The wildcard `_` catches everything not matched earlier.

:::program
```python
def describe(command):
    match command:
        case ["move", x, y] if x >= 0 and y >= 0:
            return f"move to {x},{y}"
        case ["quit" | "exit"]:
            return "stop"
        case ["echo", *words]:
            return " ".join(words)
        case _:
            return "unknown"

print(describe(["move", 2, 3]))
print(describe(["exit"]))
print(describe(["echo", "hello", "python"]))
print(describe(["move", -1, 3]))
```
:::

:::cell
Sequence patterns match by position. A guard after `if` adds a condition that must also be true.

```python
def describe(command):
    match command:
        case ["move", x, y] if x >= 0 and y >= 0:
            return f"move to {x},{y}"
        case ["quit" | "exit"]:
            return "stop"
        case ["echo", *words]:
            return " ".join(words)
        case _:
            return "unknown"

print(describe(["move", 2, 3]))
```

```output
move to 2,3
```
:::

:::cell
An OR pattern accepts several alternatives in one case. A star pattern captures the rest of a sequence.

```python
print(describe(["exit"]))
print(describe(["echo", "hello", "python"]))
```

```output
stop
hello python
```
:::

:::cell
The wildcard `_` catches values that did not match earlier cases. Here the guard rejects the negative coordinate.

```python
print(describe(["move", -1, 3]))
```

```output
unknown
```
:::

:::note
- Use `case _` as a wildcard fallback.
- Guards refine a pattern after the structure matches.
- OR patterns and star patterns keep shape-based branches compact.
:::
