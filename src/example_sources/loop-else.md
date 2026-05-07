+++
slug = "loop-else"
title = "Loop Else"
section = "Control Flow"
summary = "A loop else block runs only when the loop did not end with break."
doc_path = "/tutorial/controlflow.html#else-clauses-on-loops"
see_also = [
  "break-and-continue",
  "for-loops",
  "while-loops",
]
+++

Python loops can have an `else` clause. The name is surprising at first: loop `else` means “no `break` happened,” not “the loop condition was false.”

This is useful for searches. Put the successful early exit in `break`, then put the not-found path in `else`.

Use loop `else` sparingly. It is clearest when the loop is visibly searching for something.

:::program
```python
names = ["Ada", "Grace", "Guido"]

for name in names:
    if name == "Grace":
        print("found")
        break
else:
    print("missing")

for name in names:
    if name == "Linus":
        print("found")
        break
else:
    print("missing")
```
:::

:::cell
If the loop reaches `break`, the `else` block is skipped. This branch means the search succeeded early.

```python
names = ["Ada", "Grace", "Guido"]

for name in names:
    if name == "Grace":
        print("found")
        break
else:
    print("missing")
```

```output
found
```
:::

:::cell
If the loop finishes without `break`, the `else` block runs. This branch means the search examined every value and found nothing.

```python
for name in names:
    if name == "Linus":
        print("found")
        break
else:
    print("missing")
```

```output
missing
```
:::

:::note
- Loop `else` runs when the loop was not ended by `break`.
- It is best for search loops with a clear found/not-found split.
- It works with both `for` and `while` loops.
:::
