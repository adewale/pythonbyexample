+++
slug = "generator-expressions"
title = "Generator Expressions"
section = "Iteration"
summary = "Generator expressions use comprehension-like syntax to stream values lazily."
doc_path = "/tutorial/classes.html#generator-expressions"
+++

Generator expressions look like list comprehensions with parentheses, but they produce an iterator instead of building a concrete collection immediately.

Use them when a consumer such as `sum()`, `any()`, or a `for` loop can use values one at a time. This keeps the transformation close to the consumer and avoids storing intermediate lists.

Like other iterators, a generator expression is consumed as values are requested. Create a new generator expression when you need another pass.

:::program
```python
numbers = [1, 2, 3, 4]
list_squares = [number * number for number in numbers]
print(list_squares)

stream_squares = (number * number for number in numbers)
print(next(stream_squares))
print(next(stream_squares))
print(list(stream_squares))

print(sum(number * number for number in numbers))
```
:::

:::cell
A list comprehension is eager: it builds a list immediately. That is useful when you need to store or reuse the results.

```python
numbers = [1, 2, 3, 4]
list_squares = [number * number for number in numbers]
print(list_squares)
```

```output
[1, 4, 9, 16]
```
:::

:::cell
A generator expression is lazy: it creates an iterator that produces values as they are consumed. After two `next()` calls, only the remaining squares are left.

```python
stream_squares = (number * number for number in numbers)
print(next(stream_squares))
print(next(stream_squares))
print(list(stream_squares))
```

```output
1
4
[9, 16]
```
:::

:::cell
Generator expressions are common inside reducing functions. When a generator expression is the only argument, the extra parentheses can be omitted.

```python
print(sum(number * number for number in numbers))
```

```output
30
```
:::

:::note
- List, dict, and set comprehensions build concrete collections.
- Generator expressions produce one-pass iterators.
- Use generator expressions when the consumer can process values one at a time.
:::
