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

`break` and `continue` control the nearest enclosing loop. They are useful when the loop body discovers a reason to stop early or skip one item.

Use `continue` for a skip rule: the current item should not run the rest of the body. Use `break` for a stop rule: no later item should be processed.

Keep both rules close to the top of the loop when possible. That makes the normal path easier to read.

:::program
```python
names = ["Ada", "", "Grace", "stop", "Guido"]

for name in names:
    if not name:
        continue
    if name == "stop":
        break
    print(name)
```
:::

:::cell
`continue` skips the rest of the current iteration. The empty name is ignored, and the loop moves on to the next value.

```python
names = ["Ada", "", "Grace", "stop", "Guido"]

for name in names:
    if not name:
        continue
    if name == "stop":
        break
    print(name)
```

```output
Ada
Grace
```
:::

:::note
- `continue` skips to the next loop iteration.
- `break` exits the nearest enclosing loop immediately.
- Prefer plain `if`/`else` when the loop does not need early skip or early stop behavior.
:::
