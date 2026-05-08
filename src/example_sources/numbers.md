+++
slug = "numbers"
title = "Numbers"
section = "Basics"
summary = "Python numbers include integers, floats, and complex values."
doc_path = "/library/stdtypes.html#numeric-types-int-float-complex"
see_also = [
  "literals",
  "operators",
]
+++

Python's numeric model starts with `int`, `float`, and `complex`. Integers are arbitrary precision, floats are approximate double-precision values, and complex numbers carry real and imaginary parts.

Operators encode different numeric questions. `/` means true division and returns a float, `//` means floor division, `%` gives the remainder, and `**` computes powers.

Use rounding for display, not as a substitute for understanding floating-point approximation. Financial code usually needs `decimal.Decimal`, which is a separate precision topic.

:::program
```python
count = 10
ratio = 0.25
z = 2 + 3j

print(count + 5)
print(count / 4)
print(count // 4)
print(count % 4)
print(2 ** 5)
print(z.real, z.imag)
print(0.1 + 0.2)
print(round(3.14159, 2))
```
:::

:::cell
Python has `int` for whole numbers and `float` for approximate real-valued arithmetic. True division with `/` returns a `float`, even when both inputs are integers.

```python
count = 10
ratio = 0.25

print(count + 5)
print(count / 4)
print(ratio * 2)
```

```output
15
2.5
0.5
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
Complex numbers are built in. The literal suffix `j` marks the imaginary part.

```python
z = 2 + 3j
print(z.real, z.imag)
```

```output
2.0 3.0
```
:::

:::cell
Floating-point values are approximate. Round for display when the exact binary representation is not the lesson.

```python
print(0.1 + 0.2)
print(round(3.14159, 2))
```

```output
0.30000000000000004
3.14
```
:::

:::note
- Python's `int` has arbitrary precision; it grows as large as memory allows.
- Python's `float` is approximate double-precision floating point.
- Use `/` for true division and `//` for floor division.
- Use `decimal.Decimal` when decimal precision is the domain requirement, not just display polish.
:::
