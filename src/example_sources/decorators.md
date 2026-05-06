+++
slug = "decorators"
title = "Decorators"
section = "Functions"
summary = "Decorators wrap or register functions using @ syntax."
doc_path = "/glossary.html#term-decorator"
+++

A decorator is a callable that receives a function and returns a replacement. The `@` syntax applies that transformation at function definition time.

Decorators are common in frameworks because they can register handlers or add behavior while keeping the decorated function focused on the core action.

`@decorator` is shorthand for rebinding a function to the decorator's return value. Understanding that expansion makes decorators feel less magical.

:::program
```python
def loud(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper


def greet(name):
    return f"hello {name}"

manual_greet = loud(greet)
print(manual_greet("python"))

@loud
def welcome(name):
    return f"welcome {name}"

print(welcome("workers"))
```
:::

:::cell
A decorator is just a function that takes a function and returns another callable. Applying it manually shows the wrapping step.

```python
def loud(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper


def greet(name):
    return f"hello {name}"

manual_greet = loud(greet)
print(manual_greet("python"))
```

```output
HELLO PYTHON
```
:::

:::cell
The `@loud` syntax performs the same rebinding at definition time. After decoration, `welcome` refers to the wrapper returned by `loud`.

```python
@loud
def welcome(name):
    return f"welcome {name}"

print(welcome("workers"))
```

```output
WELCOME WORKERS
```
:::

:::note
- `@decorator` is shorthand for assigning `func = decorator(func)`.
- Decorators can wrap, replace, or register functions.
- Use `functools.wraps` in production wrappers that should preserve metadata.
:::
