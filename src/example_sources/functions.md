+++
slug = "functions"
title = "Functions"
section = "Functions"
summary = "Use def to name reusable behavior and return results."
doc_path = "/tutorial/controlflow.html#defining-functions"
+++

Functions package behavior behind a name. `def` creates a function object that can accept arguments, compute values, and return a result.

Default arguments make common calls short, and keyword arguments make call sites easier to read. A function that reaches the end without `return` produces `None`.

Use functions when a calculation has a useful name, when code repeats, or when a piece of behavior should be tested independently.

:::program
```python
def greet(name):
    return f"Hello, {name}."

print(greet("Python"))


def format_total(amount, currency="USD"):
    return f"{amount} {currency}"

print(format_total(10))
print(format_total(10, currency="EUR"))


def log(message):
    print(f"log: {message}")

result = log("saved")
print(result)
```
:::

:::cell
`return` sends a value back to the caller. The caller can print it, store it, or pass it to another function.

```python
def greet(name):
    return f"Hello, {name}."

print(greet("Python"))
```

```output
Hello, Python.
```
:::

:::cell
Default arguments provide common values. Keyword arguments make it clear which option is being overridden.

```python
def format_total(amount, currency="USD"):
    return f"{amount} {currency}"

print(format_total(10))
print(format_total(10, currency="EUR"))
```

```output
10 USD
10 EUR
```
:::

:::cell
A function without an explicit `return` returns `None`. That makes side-effect-only functions easy to distinguish from value-producing ones.

```python
def log(message):
    print(f"log: {message}")

result = log("saved")
print(result)
```

```output
log: saved
None
```
:::

:::note
- Use `return` for values the caller should receive.
- Defaults keep common calls concise.
- Keyword arguments make options readable at the call site.
:::
