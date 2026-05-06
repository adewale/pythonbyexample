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

:::program
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
:::

:::cell
Use `match` when the shape of a value is the decision. This command is a dictionary with an action and coordinates; the first case checks that shape and binds `x` and `y`.

```python
command = {"action": "move", "x": 3, "y": 4}

match command:
    case {"action": "move", "x": x, "y": y}:
        print(f"move to {x},{y}")
```

```output
move to 3,4
```
:::

:::cell
Other cases describe other valid shapes. This complete fragment changes the command so the `quit` case is the first matching pattern.

```python
command = {"action": "quit"}

match command:
    case {"action": "move", "x": x, "y": y}:
        print(f"move to {x},{y}")
    case {"action": "quit"}:
        print("quit")
```

```output
quit
```
:::

:::cell
Broader patterns and the `_` catch-all belong after specific cases. This fragment extracts an unknown action before the final fallback would run.

```python
command = {"action": "jump"}

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
unknown action: jump
```
:::

:::note
- `match` compares structure, not just equality.
- Patterns can bind names such as `x` and `y` while matching.
- Put the catch-all `_` case last, because cases are tried from top to bottom.
:::
