+++
slug = "lambdas"
title = "Lambdas"
section = "Functions"
summary = "lambda creates small anonymous functions."
doc_path = "/tutorial/controlflow.html#lambda-expressions"
+++

lambda creates a small anonymous function expression. It is most useful when a function is needed briefly, such as a sort key or callback.

Because lambdas are limited to one expression, they should stay simple. Use def when the behavior needs a name, statements, or explanation.

Lambdas are expressions, not statements. They are often passed as key functions.

:::cell
lambda creates a small anonymous function expression. It is most useful when a function is needed briefly, such as a sort key or callback.

```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
by_number = sorted(pairs, key=lambda item: item[1])
print(by_number)
```

```output
[('c', 1), ('b', 2), ('a', 3)]
```
:::

:::note
- Lambdas are expressions, not statements.
- They are often passed as key functions.
:::
