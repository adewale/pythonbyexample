+++
slug = "equality-and-identity"
title = "Equality and Identity"
section = "Data Model"
summary = "== compares values, while is compares object identity."
doc_path = "/reference/expressions.html#is-not"
see_also = [
  "none",
  "values",
  "object-lifecycle",
  "mutability",
]
+++

Python separates equality from identity. Equality asks whether two objects should be considered the same value, while identity asks whether two names point to the same object.

This distinction matters for mutable containers because two equal lists can still be independent objects. Mutating one should not imply mutating the other unless they share identity.

The `is` operator is best reserved for identity checks against singletons such as `None`. For ordinary values, `==` is the comparison readers expect.

:::program
```python
left = [1, 2, 3]
right = [1, 2, 3]
print(left == right)
print(left is right)

same = left
same.append(4)
print(left)
print(same is left)

value = None
print(value is None)

small_a = 100
small_b = 100
print(small_a is small_b)

big_a = int("1000")
big_b = int("1000")
print(big_a is big_b)
print(big_a == big_b)
```
:::

:::cell
Equal containers can be different objects. `==` compares list contents, while `is` checks whether both names refer to the same list object.

```python
left = [1, 2, 3]
right = [1, 2, 3]
print(left == right)
print(left is right)
```

```output
True
False
```
:::

:::cell
Identity matters when objects are mutable. `same` is another name for `left`, so mutating through one name changes the object seen through the other.

```python
same = left
same.append(4)
print(left)
print(same is left)
```

```output
[1, 2, 3, 4]
True
```
:::

:::cell
Use `is` for singleton identity checks such as `None`. This asks whether the value is the one special `None` object.

```python
value = None
print(value is None)
```

```output
True
```
:::

:::cell
`is` for integers is unreliable because CPython caches small integers (roughly `-5` to `256`) but not larger ones. Two equal large integers can be different objects. Use `==` for value comparisons; reserve `is` for singletons.

```python
small_a = 100
small_b = 100
print(small_a is small_b)

big_a = int("1000")
big_b = int("1000")
print(big_a is big_b)
print(big_a == big_b)
```

```output
True
False
True
```
:::

:::note
- Use `==` for ordinary value comparisons.
- Use `is` primarily for identity checks against singletons such as `None`.
- Equal mutable containers can still be independent objects.
- Never use `is` to compare numbers; CPython's small-integer cache makes the result an implementation detail.
:::
