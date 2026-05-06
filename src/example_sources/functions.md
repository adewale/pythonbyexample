+++
slug = "functions"
title = "Functions"
section = "Functions"
summary = "Use def to package reusable behavior."
doc_path = "/tutorial/controlflow.html#defining-functions"
+++

Functions package behavior behind a name. def creates a function object that can accept arguments, compute values, and return a result.

Default and keyword arguments make call sites readable. A function that reaches the end without return produces None, which is itself a normal Python value.

Functions return None unless they execute a return statement. Keyword arguments make call sites easier to read.

:::program
```python
def greet(name, excited=False):
    ending = "!" if excited else "."
    return f"Hello, {name}{ending}"

print(greet("Python"))
print(greet("Workers", excited=True))
```
:::

:::cell
Functions package behavior behind a name. def creates a function object that can accept arguments, compute values, and return a result.

Default and keyword arguments make call sites readable. A function that reaches the end without return produces None, which is itself a normal Python value.

```python
def greet(name, excited=False):
    ending = "!" if excited else "."
    return f"Hello, {name}{ending}"

print(greet("Python"))
print(greet("Workers", excited=True))
```

```output
Hello, Python.
Hello, Workers!
```
:::

:::note
- Functions return None unless they execute a return statement.
- Keyword arguments make call sites easier to read.
:::
