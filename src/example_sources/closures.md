+++
slug = "closures"
title = "Closures"
section = "Functions"
summary = "Inner functions can remember values from an enclosing scope."
doc_path = "/reference/executionmodel.html#binding-of-names"
+++

A closure is a function that remembers names from the scope where it was created. This lets you configure behavior once and call it later.

Each call to the outer function creates a separate remembered environment. That is why `double` and `triple` can share the same code but keep different factors.

Closures are a foundation for decorators, callbacks, and small function factories.

:::cell
Define a function inside another function when the inner behavior needs to remember some setup value.

Each call creates a new closure. `double` remembers `factor == 2`, while `triple` remembers `factor == 3`.

Calling the returned function later still has access to the captured value.

```python
def make_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
```

```output
10
15
```
:::

:::note
- A closure keeps access to names from the scope where the inner function was created.
- Closures are useful for callbacks, small factories, and decorators.
:::
