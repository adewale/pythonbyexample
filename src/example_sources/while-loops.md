+++
slug = "while-loops"
title = "While Loops"
section = "Control Flow"
summary = "while repeats as long as a condition is true."
doc_path = "/reference/compound_stmts.html#while"
+++

A `while` loop repeats as long as its condition remains true. It is useful when you are waiting for state to change rather than consuming an existing iterable.

The loop body must make progress toward the stopping condition. Here decrementing `remaining` prevents an infinite loop.

Many Python loops should be `for` loops, but `while` is the right tool for countdowns, sentinels, polling, and other condition-driven repetition.

:::cell
Start with the state that controls the loop. The condition will be checked before every iteration.

The body runs while the condition is true. Updating `remaining` moves the program toward stopping.

```python
remaining = 3

while remaining > 0:
    print(f"launch in {remaining}")
    remaining -= 1
```

```output
launch in 3
launch in 2
launch in 1
```
:::

:::cell
Execution continues after the loop once the condition becomes false.

```python
print("liftoff")
```

```output
liftoff
```
:::

:::note
- Use `while` when the stopping condition matters more than a fixed iterable.
- Update loop state inside the body so the condition can become false.
- Prefer `for` when you already have a collection or range to consume.
:::
