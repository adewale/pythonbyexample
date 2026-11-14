+++
slug = "operators"
title = "Operators"
section = "Basics"
summary = "Operators combine, compare, and test values in expressions."
doc_path = "/reference/expressions.html#operator-precedence"
see_also = [
  "numbers",
  "equality-and-identity",
  "assignment-expressions",
  "operator-overloading",
]
+++

Operators are the punctuation and keywords that combine values into expressions. Some operators compute new values, some compare values, and some ask relationship questions such as membership or identity.

This page is the surface map. Focused examples explain the deeper behavior of numbers, booleans, conditions, sets, assignment expressions, and operator overloading.

Read operators by the question they ask: arithmetic computes, comparison answers true or false, boolean operators combine truth values, membership searches a container, and specialized operators should only appear when the data shape calls for them.

:::program
```python
count = 10
print(count + 5)
print(count // 4)
print(count % 4)
print(2 ** 5)

score = 91
print(80 <= score < 100)
print(score == 100 or score >= 90)
print("py" in "python")

flags = 0b0011
print(flags & 0b0101)
print(flags | 0b0100)
print(flags ^ 0b0101)
print(flags << 1)

items = ["a", "b"]
print((size := len(items)) > 0)
print(size)

count = 0
print(count != 0 and 10 / count)
print(count == 0 or 10 / count)
print(count == 0 and "empty")
```
:::

:::cell
Arithmetic operators compute new values. Use `//` for floor division, `%` for remainder, and `**` for powers.

```python
count = 10
print(count + 5)
print(count // 4)
print(count % 4)
print(2 ** 5)
```

```output
15
2
2
32
```
:::

:::cell
Comparison operators produce booleans. Python comparisons can chain, which keeps range checks readable.

```python
score = 91
print(80 <= score < 100)
print(score == 100 or score >= 90)
print("py" in "python")
```

```output
True
True
True
```
:::

:::cell
Bitwise operators work on integer bit patterns. They are useful for masks and flags, not ordinary boolean logic. `&` is bitwise AND, `|` is bitwise OR, `^` is exclusive OR, and `<<` shifts left.

```python
flags = 0b0011
print(flags & 0b0101)
print(flags | 0b0100)
print(flags ^ 0b0101)
print(flags << 1)
```

```output
1
7
6
6
```
:::

:::cell
The walrus operator `:=` assigns inside an expression: the parenthesized part both names the length and passes it on to the comparison. [Assignment expressions](/examples/assignment-expressions) shows where that earns its place.

```python
items = ["a", "b"]
print((size := len(items)) > 0)
print(size)
```

```output
True
2
```
:::

:::cell
`and` and `or` short-circuit: the right side runs only when the left side cannot already determine the result. Here `10 / count` would fail with a division-by-zero error if it ran, but the left side settles both answers first. The result is the last operand evaluated, so `count == 0 and "empty"` produces `"empty"`.

```python
count = 0
print(count != 0 and 10 / count)
print(count == 0 or 10 / count)
print(count == 0 and "empty")
```

```output
False
True
empty
```
:::

:::note
- Use the clearest operator for the question: arithmetic, comparison, boolean logic, membership, identity, or bitwise manipulation.
- `and` and `or` short-circuit, so the right side may not run.
- Operators have precedence; use parentheses when grouping would otherwise be hard to read.
- `@` is the matrix-multiplication operator. No built-in type implements it; [operator overloading](/examples/operator-overloading) shows how a class gives `@`, `+`, or `==` its own meaning.
:::
