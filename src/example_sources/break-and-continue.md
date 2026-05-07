+++
slug = "break-and-continue"
title = "Break and Continue"
section = "Control Flow"
summary = "break exits a loop early, while continue skips to the next iteration."
doc_path = "/tutorial/controlflow.html#break-and-continue-statements"
see_also = [
  "for-loops",
  "while-loops",
  "loop-else",
]
+++

`break` and `continue` control the nearest enclosing loop. They exist for loops whose body discovers an early stop rule or an item-level skip rule.

Use `continue` when the current item should not run the rest of the body. Use `break` when no later item should be processed.

The alternative is ordinary `if`/`else` nesting. Prefer `break` and `continue` when they keep the normal path flatter and easier to read.

:::program
```python
names = ["Ada", "", "Grace"]
for name in names:
    if not name:
        continue
    print(name)

commands = ["load", "save", "stop", "delete"]
for command in commands:
    if command == "stop":
        break
    print(command)
```
:::

:::cell
`continue` skips the rest of the current iteration. The empty name is ignored, and the loop moves on to the next value.

```python
names = ["Ada", "", "Grace"]
for name in names:
    if not name:
        continue
    print(name)
```

```output
Ada
Grace
```
:::

:::cell
`break` exits the loop immediately. The value after `stop` is never processed because the loop has already ended.

```python
commands = ["load", "save", "stop", "delete"]
for command in commands:
    if command == "stop":
        break
    print(command)
```

```output
load
save
```
:::

:::note
- `continue` skips to the next loop iteration.
- `break` exits the nearest enclosing loop immediately.
- Prefer plain `if`/`else` when the loop does not need early skip or early stop behavior.
:::
