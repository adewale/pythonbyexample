+++
slug = "equality-and-identity"
title = "Equality and Identity"
section = "Data Model"
summary = "== compares values, while is compares object identity."
doc_path = "/reference/expressions.html#is-not"
+++

Python separates equality from identity. Equality asks whether two objects should be considered the same value, while identity asks whether two names point to the same object.

This distinction matters for mutable containers because two equal lists can still be independent objects. Mutating one should not imply mutating the other unless they share identity.

The is operator is best reserved for identity checks against singletons such as None. For ordinary values, == is the comparison readers expect.

:::cell
Python separates equality from identity. Equality asks whether two objects should be considered the same value, while identity asks whether two names point to the same object.

This distinction matters for mutable containers because two equal lists can still be independent objects. Mutating one should not imply mutating the other unless they share identity.

```python
left = [1, 2, 3]
right = [1, 2, 3]
same = left

print(left == right)
print(left is right)
print(left is same)
print(None is None)
```

```output
True
False
True
True
```
:::

:::note
- Use == for ordinary value comparisons.
- Use is primarily for singletons such as None, True, and False.
:::
