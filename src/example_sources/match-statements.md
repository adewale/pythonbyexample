+++
slug = "match-statements"
title = "Match Statements"
section = "Control Flow"
summary = "match selects cases using structural pattern matching."
doc_path = "/tutorial/controlflow.html#match-statements"
+++

Structural pattern matching lets a program choose a branch based on the shape of data. It is especially useful when commands, messages, or parsed data have a few known forms.

A `case` pattern can both check constants and bind names. The move case checks the action and extracts `x` and `y` in one readable step.

Order matters because Python tries cases from top to bottom. Specific shapes should appear before broad fallback cases such as `_`.

:::cell
Structural pattern matching lets a program choose a branch based on the shape of data. It is especially useful when commands, messages, or parsed data have a few known forms.

A `case` pattern can both check constants and bind names. The move case checks the action and extracts `x` and `y` in one readable step.

Order matters because Python tries cases from top to bottom. Specific shapes should appear before broad fallback cases such as `_`.

```python
command = {"action": "move", "x": 3, "y": 4}

match command:
    case {"action": "move", "x": x, "y": y}:
        print(f"move to {x},{y}")
    case {"action": "quit"}:
        print("quit")
    case {"action": action}:
        print(f"unknown action: {action}")
    case _:
        print("invalid command")
```

```output
move to 3,4
```
:::

:::note
- `match` compares structure, not just equality.
- Patterns can bind names such as `x` and `y` while matching.
- Put the catch-all `_` case last, because cases are tried from top to bottom.
:::
