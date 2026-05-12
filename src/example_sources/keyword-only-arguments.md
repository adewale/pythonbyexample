+++
slug = "keyword-only-arguments"
title = "Keyword-only Arguments"
section = "Functions"
summary = "Use * to require selected function arguments to be named."
doc_path = "/tutorial/controlflow.html#special-parameters"
see_also = [
  "functions",
  "args-and-kwargs",
  "positional-only-parameters",
  "partial-functions",
]
+++

A bare `*` in a function signature marks the following parameters as keyword-only. Callers must name those arguments explicitly.

Keyword-only arguments are useful for options such as timeouts, flags, and modes where positional calls would be ambiguous or easy to misread.

They let the required data stay positional while optional controls remain self-documenting at the call site.

:::program
```python
def connect(host, *, timeout=5, secure=True):
    scheme = "https" if secure else "http"
    print(f"{scheme}://{host} timeout={timeout}")

connect("example.com")
connect("example.com", timeout=10)
connect("localhost", secure=False)
```
:::

:::cell
Parameters after `*` must be named. The default options still apply when the caller omits them.

```python
def connect(host, *, timeout=5, secure=True):
    scheme = "https" if secure else "http"
    print(f"{scheme}://{host} timeout={timeout}")

connect("example.com")
```

```output
https://example.com timeout=5
```
:::

:::cell
Naming the option makes the call site explicit. A reader does not have to remember which positional slot controls the timeout.

```python
connect("example.com", timeout=10)
```

```output
https://example.com timeout=10
```
:::

:::cell
Flags are especially good keyword-only arguments because a bare positional `False` is hard to interpret.

```python
connect("localhost", secure=False)
```

```output
http://localhost timeout=5
```
:::

:::note
- Put `*` before options that callers should name.
- Keyword-only flags avoid mysterious positional `True` and `False` arguments.
- Defaults work normally for keyword-only parameters.
:::
