+++
slug = "sentinel-iteration"
title = "Sentinel Iteration"
section = "Iteration"
summary = "iter(callable, sentinel) repeats calls until a marker value appears."
doc_path = "/library/functions.html#iter"
+++

`iter(callable, sentinel)` keeps calling a zero-argument callable and yields each result until the callable returns the sentinel value. It is the right shape for repeated reads from files, sockets, or queues — sources where each call produces the next chunk and a known marker means "no more".

Reach for it instead of writing `while True:` plus a manual break when the loop body would do nothing else but read and check. The two-argument form turns a polling callable into something that composes with `for` loops, comprehensions, and other iterator helpers.

The callable must take no arguments. Wrap a parameterized reader in a small lambda or method that closes over the parameters when the underlying API needs them.

:::program
```python
lines = iter(["alpha", "beta", ""])

def read_line():
    return next(lines)

for line in iter(read_line, ""):
    print(line.upper())
```
:::

:::cell
A zero-argument callable produces one value at a time.

```python
lines = iter(["alpha", "beta", ""])

def read_line():
    return next(lines)

for line in iter(read_line, ""):
    print(line.upper())
```

```output
ALPHA
BETA
```
:::

:::note
- A zero-argument callable produces one value at a time.
- The sentinel value stops the loop without appearing in the output.
- This form is useful for repeated reads from files, sockets, or queues.
:::
