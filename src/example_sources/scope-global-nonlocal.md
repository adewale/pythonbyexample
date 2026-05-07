+++
slug = "scope-global-nonlocal"
title = "Global and Nonlocal"
section = "Functions"
summary = "global and nonlocal choose which outer binding assignment should update."
doc_path = "/reference/simple_stmts.html#the-global-statement"
see_also = [
  "variables",
  "closures",
  "functions",
]
+++

Assignment normally creates or updates a local name inside the current function. `global` and `nonlocal` are explicit escape hatches for rebinding names outside that local scope.

Use `nonlocal` when an inner function should update a name in an enclosing function. Use `global` rarely; passing values and returning results is usually clearer.

These statements affect name binding, not object mutation. Mutating a shared list is different from rebinding the name itself.

:::program
```python
count = 0

def bump_global():
    global count
    count += 1

bump_global()
print(count)


def make_counter():
    total = 0
    def bump():
        nonlocal total
        total += 1
        return total
    return bump

counter = make_counter()
print(counter())
print(counter())
```
:::

:::cell
`global` tells assignment to update a module-level binding. Without it, `count += 1` would try to assign a local `count`.

```python
count = 0

def bump_global():
    global count
    count += 1

bump_global()
print(count)
```

```output
1
```
:::

:::cell
`nonlocal` tells assignment to update a binding in the nearest enclosing function scope. This is useful for small closures that keep state.

```python
def make_counter():
    total = 0
    def bump():
        nonlocal total
        total += 1
        return total
    return bump

counter = make_counter()
print(counter())
print(counter())
```

```output
1
2
```
:::

:::note
- Assignment inside a function is local unless declared otherwise.
- Prefer `nonlocal` for closure state and avoid `global` unless module state is truly intended.
- Passing values and returning results is usually easier to test than rebinding outer names.
:::
