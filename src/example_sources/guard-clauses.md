+++
slug = "guard-clauses"
title = "Guard Clauses"
section = "Control Flow"
summary = "Guard clauses handle boundary cases early so the main path stays flat."
doc_path = "/tutorial/controlflow.html#if-statements"
see_also = [
  "conditionals",
  "exceptions",
  "functions",
]
+++

A guard clause is an early `return`, `raise`, `break`, or `continue` that handles a case the rest of the function should not process. The point is not new syntax; the point is moving boundaries out of the way so the successful path can be read straight through.

Use guards when a function has clear invalid, empty, or already-finished cases. If every branch is equally important, an ordinary `if`/`elif` chain may be clearer.

The contrast below shows the payoff: the nested version makes the valid path live inside two conditions, while the guard version names the invalid cases first and leaves the calculation at the outer indentation level.

:::program
```python
def nested_discount(price, percent):
    if price >= 0:
        if 0 <= percent <= 100:
            return round(price - price * percent / 100, 2)
        return "invalid discount"
    return "invalid price"


def guarded_discount(price, percent):
    if price < 0:
        return "invalid price"
    if not 0 <= percent <= 100:
        return "invalid discount"

    return round(price - price * percent / 100, 2)

print(nested_discount(100, 15))
print(guarded_discount(-5, 10))
print(guarded_discount(100, 120))
```
:::

:::cell
The nested version is correct, but the useful work is buried inside both tests.

```python
def nested_discount(price, percent):
    if price >= 0:
        if 0 <= percent <= 100:
            return round(price - price * percent / 100, 2)
        return "invalid discount"
    return "invalid price"

print(nested_discount(100, 15))
```

```output
85.0
```
:::

:::cell
The guard-clause version handles impossible inputs first, then lets the ordinary calculation sit at the top level of the function body.

```python
def guarded_discount(price, percent):
    if price < 0:
        return "invalid price"
    if not 0 <= percent <= 100:
        return "invalid discount"

    return round(price - price * percent / 100, 2)

print(guarded_discount(-5, 10))
print(guarded_discount(100, 120))
```

```output
invalid price
invalid discount
```
:::

:::note
- Guard clauses are a readability pattern, not a separate Python feature.
- They work best when the early cases are true boundaries.
- For exceptional failures, raise an exception instead of returning a sentinel string.
:::
