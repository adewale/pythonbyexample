+++
slug = "decorators"
title = "Decorators"
section = "Functions"
summary = "Decorators wrap or register functions using @ syntax."
doc_path = "/glossary.html#term-decorator"
+++

A decorator is a callable that receives a function and returns a replacement. The @ syntax applies that transformation at function definition time.

Decorators are common in frameworks because they can register handlers or add behavior while keeping the decorated function focused on the core action.

@decorator is shorthand for rebinding a function. Frameworks often use decorators to register handlers.

:::cell
A decorator is a callable that receives a function and returns a replacement. The @ syntax applies that transformation at function definition time.

Decorators are common in frameworks because they can register handlers or add behavior while keeping the decorated function focused on the core action.

@decorator is shorthand for rebinding a function. Frameworks often use decorators to register handlers.

```python
def loud(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@loud
def greet(name):
    return f"hello {name}"

print(greet("python"))
```

```output
HELLO PYTHON
```
:::

:::note
- @decorator is shorthand for rebinding a function.
- Frameworks often use decorators to register handlers.
:::
