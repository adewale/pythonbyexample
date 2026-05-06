+++
slug = "recursion"
title = "Recursion"
section = "Functions"
summary = "Recursive functions solve a problem by calling themselves with a smaller input."
doc_path = "/tutorial/controlflow.html#defining-functions"
+++

A recursive function calls itself to solve a smaller version of the same problem. The base case is the input that can be answered directly.

The recursive case must move toward the base case. Without that progress, recursion becomes an infinite chain of calls until Python raises a recursion-depth error.

Python supports recursion, but it does not optimize tail calls. Prefer loops for very deep or simple repetition.

:::cell
Recursive functions solve a problem by calling themselves with a smaller input.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

```output
120
```
:::

:::note
- Every recursive function needs a base case that stops the calls.
- Python limits recursion depth, so loops are often better for very deep repetition.
:::
