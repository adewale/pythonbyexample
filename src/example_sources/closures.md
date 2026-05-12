+++
slug = "closures"
title = "Closures"
section = "Functions"
summary = "Inner functions can remember values from an enclosing scope."
doc_path = "/reference/executionmodel.html#binding-of-names"
see_also = [
  "functions",
  "lambdas",
  "decorators",
  "partial-functions",
]
+++

A closure is a function that remembers names from the scope where it was created. This lets you configure behavior once and call it later.

Each call to the outer function creates a separate remembered environment. That is why `double` and `triple` can share the same code but keep different factors.

Closures are a foundation for decorators, callbacks, and small function factories.

:::program
```python
def make_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply

double = make_multiplier(2)
print(double(5))

triple = make_multiplier(3)
print(triple(5))

late = []
for i in range(3):
    late.append(lambda: i)
print([f() for f in late])

bound = []
for i in range(3):
    bound.append(lambda i=i: i)
print([f() for f in bound])
```
:::

:::cell
Define a function inside another function when the inner behavior needs to remember setup from the outer call. The returned function keeps access to `factor`.

```python
def make_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply

double = make_multiplier(2)
print(double(5))
```

```output
10
```
:::

:::cell
Calling the outer function again creates a separate closure. `triple` uses the same inner code, but remembers a different `factor`.

```python
triple = make_multiplier(3)
print(triple(5))
```

```output
15
```
:::

:::cell
Closures bind names, not values. Lambdas defined in a loop all reference the same loop variable, so calling them later sees its final value. Capture the value at definition time by binding it as a default argument — `lambda i=i: i` — so each closure remembers its own `i`.

```python
late = []
for i in range(3):
    late.append(lambda: i)
print([f() for f in late])

bound = []
for i in range(3):
    bound.append(lambda i=i: i)
print([f() for f in bound])
```

```output
[2, 2, 2]
[0, 1, 2]
```
:::

:::note
- A closure keeps access to names from the scope where the inner function was created.
- Each call to the outer function can create a separate remembered environment.
- Closures are useful for callbacks, small factories, and decorators.
- Closures bind names, not values; capture loop variables with `lambda x=x: ...` to freeze them at definition time.
:::
