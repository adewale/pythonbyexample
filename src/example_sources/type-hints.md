+++
slug = "type-hints"
title = "Type Hints"
section = "Types"
summary = "Annotations document expected types and power static analysis."
doc_path = "/library/typing.html"
scope_first_pass = true
see_also = [
  "union-and-optional-types",
  "type-aliases",
  "protocols",
  "generics-and-typevar",
  "runtime-type-checks",
]
+++

Type hints are annotations that document expected shapes for values, parameters, and return results. They exist so tools and readers can understand API boundaries before the program runs.

Python stores many annotations but does not enforce most of them at runtime. Use type hints for communication and static analysis; use validation or exceptions when runtime checks are required.

The alternative to an annotation is prose, tests, or runtime validation. Good Python code often uses all three at important boundaries.

:::program
```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

print(total([1, 2, 3]))
print(total.__annotations__)


def label(score: int) -> str:
    return f"score={score}"

print(label("high"))
```
:::

:::cell
Type hints document expected parameter and return shapes. Python still runs the function normally at runtime.

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

print(total([1, 2, 3]))
```

```output
6
```
:::

:::cell
Python stores annotations on the function object for tools and introspection. Type checkers use this information without changing the function call syntax.

```python
print(total.__annotations__)
```

```output
{'numbers': list[int], 'return': <class 'int'>}
```
:::

:::cell
Most hints are not runtime validation. This call passes a string where the hint says `int`; Python still calls the function because the body can format any value.

```python
def label(score: int) -> str:
    return f"score={score}"

print(label("high"))
```

```output
score=high
```
:::

:::note
- Python does not enforce most type hints at runtime.
- Tools like type checkers and editors use annotations to catch mistakes earlier.
- Use runtime validation when untrusted input must be rejected while the program runs.
:::
