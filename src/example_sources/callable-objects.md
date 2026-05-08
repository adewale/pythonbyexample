+++
slug = "callable-objects"
title = "Callable Objects"
section = "Data Model"
summary = "__call__ lets an instance behave like a function while keeping state."
doc_path = "/reference/datamodel.html#object.__call__"
see_also = [
  "functions",
  "closures",
  "callable-types",
]
+++

Functions are not the only callable objects in Python. Any instance can be called with parentheses when its class defines `__call__`.

Callable objects are useful when behavior needs remembered configuration or evolving state. A closure can do this too; a class is often clearer when the state has multiple fields or needs named methods.

The tradeoff is ceremony. Use a function for simple behavior, a closure for small captured state, and a callable object when naming the state improves the interface.

:::program
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.calls = 0

    def __call__(self, value):
        self.calls += 1
        return value * self.factor

double = Multiplier(2)
print(double(5))
print(double(7))
print(double.calls)
```
:::

:::cell
A callable object starts as ordinary state stored on an instance.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.calls = 0

double = Multiplier(2)
print(double.factor)
```

```output
2
```
:::

:::cell
`__call__` makes the instance usable with function-call syntax.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        self.calls = 0

    def __call__(self, value):
        self.calls += 1
        return value * self.factor

double = Multiplier(2)
print(double(5))
print(double(7))
```

```output
10
14
```
:::

:::cell
Because the callable is still an object, it can remember state across calls.

```python
print(double.calls)
```

```output
2
```
:::

:::note
- `callable(obj)` checks whether an object can be called.
- Callable objects are good for named, stateful behavior.
- Prefer plain functions when no instance state is needed.
:::
