+++
slug = "guard-clauses"
title = "Guard Clauses"
section = "Control Flow"
summary = "Guard clauses handle exceptional cases early so the main path stays flat."
doc_path = "/tutorial/controlflow.html#if-statements"
+++

Guard clauses handle exceptional cases early so the main path stays flat. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
def price_after_discount(price, percent):
    if price < 0:
        return "invalid price"
    if not 0 <= percent <= 100:
        return "invalid discount"

    discount = price * percent / 100
    return round(price - discount, 2)

print(price_after_discount(100, 15))
print(price_after_discount(-5, 10))
print(price_after_discount(100, 120))
```
:::

:::cell
Return early when inputs cannot be handled.

```python
def price_after_discount(price, percent):
    if price < 0:
        return "invalid price"
    if not 0 <= percent <= 100:
        return "invalid discount"

    discount = price * percent / 100
    return round(price - discount, 2)

print(price_after_discount(100, 15))
print(price_after_discount(-5, 10))
print(price_after_discount(100, 120))
```

```output
85.0
invalid price
invalid discount
```
:::

:::note
- Return early when inputs cannot be handled.
- After the guards, the remaining code can read as the normal path.
- Guard clauses are a style choice, not new syntax.
:::
