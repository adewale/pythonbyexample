+++
slug = "conditionals"
title = "Conditionals"
section = "Control Flow"
summary = "if, elif, and else choose which block runs."
doc_path = "/tutorial/controlflow.html#if-statements"
+++

`if`, `elif`, and `else` let a program choose one path based on a condition. Python uses indentation to show which statements belong to each branch.

Conditions use Python truthiness: booleans work directly, and many objects such as empty lists or empty strings are considered false. Order branches from most specific to most general.

Use `elif` to keep one decision flat instead of nested. Use Python's ternary expression only when you are choosing between two values.

:::program
```python
temperature = 72

if temperature < 60:
    print("cold")
elif temperature < 80:
    print("comfortable")
else:
    print("hot")

items = ["coat", "hat"]
if items:
    print(f"packing {len(items)} items")

status = "ok" if temperature < 90 else "danger"
print(status)
```
:::

:::cell
Start with the value that the branches will test. A conditional is only useful when the branch condition is visible and meaningful.

Use `if`, `elif`, and `else` for one ordered choice. Python tests the branches from top to bottom and runs only the first matching block.

```python
temperature = 72

if temperature < 60:
    print("cold")
elif temperature < 80:
    print("comfortable")
else:
    print("hot")
```

```output
comfortable
```
:::

:::cell
Truthiness is part of conditional flow. Empty collections are false, so `if items:` reads as “if there is anything to work with.”

```python
items = ["coat", "hat"]
if items:
    print(f"packing {len(items)} items")
```

```output
packing 2 items
```
:::

:::cell
Use the ternary expression when you are choosing a value. If either side needs multiple statements, use a normal `if` block instead.

```python
status = "ok" if temperature < 90 else "danger"
print(status)
```

```output
ok
```
:::

:::note
- Python has no mandatory parentheses around conditions; the colon and indentation define the block.
- Comparison operators such as `<` and `==` can be chained, as in `0 < value < 10`.
- Keep branch bodies short; move larger work into functions so the decision remains easy to scan.
:::
