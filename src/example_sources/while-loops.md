+++
slug = "while-loops"
title = "While Loops"
section = "Control Flow"
summary = "while repeats until changing state makes a condition false."
doc_path = "/reference/compound_stmts.html#while"
+++

A `while` loop repeats while a condition remains true. Unlike `for`, which consumes an existing iterable, `while` is for state-driven repetition where the next step depends on what happened so far.

The loop body must make progress toward stopping. That progress might be decrementing a counter, reading until a sentinel value, or waiting until some external state changes.

Reach for `for` when you already have values to consume. Reach for `while` when the loop's own state decides whether another iteration is needed.

:::program
```python
remaining = 3
while remaining > 0:
    print(f"launch in {remaining}")
    remaining -= 1
print("liftoff")

responses = iter(["retry", "retry", "ok"])
status = next(responses)
while status != "ok":
    print(f"status: {status}")
    status = next(responses)
print(f"status: {status}")
```
:::

:::cell
Use `while` when the condition, not an iterable, controls repetition. Here the loop owns the countdown state and updates it each time through the body.

```python
remaining = 3
while remaining > 0:
    print(f"launch in {remaining}")
    remaining -= 1
print("liftoff")
```

```output
launch in 3
launch in 2
launch in 1
liftoff
```
:::

:::cell
A sentinel loop stops when a special value appears. The loop does not know in advance how many retries it will need; it keeps going until the state says to stop.

```python
responses = iter(["retry", "retry", "ok"])
status = next(responses)
while status != "ok":
    print(f"status: {status}")
    status = next(responses)
print(f"status: {status}")
```

```output
status: retry
status: retry
status: ok
```
:::

:::note
- Use `while` when changing state decides whether the loop continues.
- Update loop state inside the body so the condition can become false.
- Prefer `for` when you already have a collection, range, iterator, or generator to consume.
:::
