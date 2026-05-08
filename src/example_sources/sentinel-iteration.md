+++
slug = "sentinel-iteration"
title = "Sentinel Iteration"
section = "Iteration"
summary = "iter(callable, sentinel) repeats calls until a marker value appears."
doc_path = "/library/functions.html#iter"
+++

iter(callable, sentinel) repeats calls until a marker value appears. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

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
