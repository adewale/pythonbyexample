+++
slug = "lambdas"
title = "Lambdas"
section = "Functions"
summary = "lambda creates small anonymous function expressions."
doc_path = "/tutorial/controlflow.html#lambda-expressions"
see_also = [
  "functions",
  "sorting",
  "callable-objects",
]
+++

`lambda` creates a small anonymous function expression. It is most useful when Python asks for a function and the behavior is short enough to read inline.

A lambda can only contain one expression. Use `def` when the behavior deserves a name, needs statements, or would be easier to test separately.

Lambdas often appear as key functions, callbacks, and tiny adapters. Keep them simple enough that the call site remains clearer than a named helper.

:::program
```python
add_tax = lambda price: round(price * 1.08, 2)
print(add_tax(10))

items = [("notebook", 5), ("pen", 2), ("bag", 20)]
by_price = sorted(items, key=lambda item: item[1])
print(by_price)

def price(item):
    return item[1]

print(sorted(items, key=price))
```
:::

:::cell
A lambda is a function expression. Assigning one to a name works, although `def` is usually clearer for reusable behavior.

```python
add_tax = lambda price: round(price * 1.08, 2)
print(add_tax(10))
```

```output
10.8
```
:::

:::cell
Lambdas are most idiomatic when passed directly to another function. `sorted()` calls this key function once for each item.

```python
items = [("notebook", 5), ("pen", 2), ("bag", 20)]
by_price = sorted(items, key=lambda item: item[1])
print(by_price)
```

```output
[('pen', 2), ('notebook', 5), ('bag', 20)]
```
:::

:::cell
A named function is better when the behavior should be reused or explained. It produces the same sort key, but gives the operation a name.

```python
def price(item):
    return item[1]

print(sorted(items, key=price))
```

```output
[('pen', 2), ('notebook', 5), ('bag', 20)]
```
:::

:::note
- Lambdas are expressions, not statements.
- Prefer `def` for multi-step or reused behavior.
- Lambdas are common as `key=` functions because the behavior is local to one call.
:::
