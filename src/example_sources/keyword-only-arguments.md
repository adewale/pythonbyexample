+++
slug = "keyword-only-arguments"
title = "Keyword-only Arguments"
section = "Functions"
summary = "Use * to require selected arguments to be named."
doc_path = "/tutorial/controlflow.html#special-parameters"
+++

A bare * in a function signature marks the following parameters as keyword-only. Callers must name those arguments explicitly.

This is useful for options such as timeouts, flags, and modes where positional calls would be ambiguous or easy to misread.

Keyword-only arguments make call sites explicit. They are useful for options and flags.

:::cell
A bare * in a function signature marks the following parameters as keyword-only. Callers must name those arguments explicitly.

This is useful for options such as timeouts, flags, and modes where positional calls would be ambiguous or easy to misread.

```python
def connect(host, *, timeout=5, secure=True):
    print(host, timeout, secure)

connect("example.com", timeout=10)
```

```output
example.com 10 True
```
:::

:::note
- Keyword-only arguments make call sites explicit.
- They are useful for options and flags.
:::
