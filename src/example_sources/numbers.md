+++
slug = "numbers"
title = "Numbers"
section = "Basics"
summary = "Python numbers include integers and floating-point values."
doc_path = "/library/stdtypes.html#numeric-types-int-float-complex"
+++

Python's numeric model starts with `int` and `float`. Integers are arbitrary precision, while floats are the ordinary double-precision floating-point values used for approximate decimal work.

The division operators are intentionally distinct: `/` means true division and produces a float, while `//` means floor division. `%` gives the remainder and `**` computes powers.

Use rounding for display, not as a substitute for understanding floating-point approximation. Financial code usually needs `decimal.Decimal`, which is a later standard-library topic.

:::cell
Python has `int` for whole numbers and `float` for floating-point numbers. You usually write them directly as literals.

Arithmetic operators return new numeric values. True division with `/` returns a `float`, even when both inputs are integers.

```python
count = 10
ratio = 0.25

print(count + 5)
print(count / 4)
```

```output
15
2.5
```
:::

:::cell
Floor division and modulo are useful when you need quotient and remainder behavior. Powers use `**`, not `^`.

```python
print(count // 4)
print(count % 4)
print(2 ** 5)
```

```output
2
2
32
```
:::

:::cell
Floating-point values are approximate, so examples often round display output when the lesson is about presentation rather than precision.

```python
print(round(3.14159, 2))
```

```output
3.14
```
:::

:::note
- Python's `int` has arbitrary precision; it grows as large as memory allows.
- Python's `float` is the usual double-precision floating-point type; core Python does not expose separate `float32` and `float64` syntax.
- Use `/` for true division and `//` for floor division.
:::
