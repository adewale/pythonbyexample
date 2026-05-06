+++
slug = "type-hints"
title = "Type Hints"
section = "Types"
summary = "Annotations document expected types and power static analysis."
doc_path = "/library/typing.html"
+++

Type hints are annotations that document expected shapes for values, parameters, and return results. Python stores many annotations but does not enforce most of them at runtime.

Editors, linters, and type checkers use annotations to catch mistakes earlier. They are especially valuable at API boundaries and in larger codebases.

Python does not enforce most type hints at runtime. Tools like type checkers and editors use annotations.

:::cell
Type hints are annotations that document expected shapes for values, parameters, and return results. Python stores many annotations but does not enforce most of them at runtime.

Editors, linters, and type checkers use annotations to catch mistakes earlier. They are especially valuable at API boundaries and in larger codebases.

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

print(total([1, 2, 3]))
print(total.__annotations__)
```

```output
6
{'numbers': list[int], 'return': <class 'int'>}
```
:::

:::note
- Python does not enforce most type hints at runtime.
- Tools like type checkers and editors use annotations.
:::
