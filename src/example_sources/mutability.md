+++
slug = "mutability"
title = "Mutability"
section = "Data Model"
summary = "Some objects can change in place, and names can share one object."
doc_path = "/reference/datamodel.html#objects-values-and-types"
+++

Objects in Python can be mutable or immutable. Mutable objects such as lists can change in place, while immutable objects such as strings produce new values instead.

Names can share one mutable object, so a change through one name is visible through another. This is powerful, but it is also the source of many beginner surprises.

Understanding mutability explains why copying containers, avoiding mutable defaults, and returning new values are recurring Python design choices.

:::program
```python
first = ["python"]
second = first
second.append("workers")

print(first)
print(second)

text = "python"
text.upper()
print(text)
```
:::

:::cell
Objects in Python can be mutable or immutable. Mutable objects such as lists can change in place, while immutable objects such as strings produce new values instead.

Names can share one mutable object, so a change through one name is visible through another. This is powerful, but it is also the source of many beginner surprises.

```python
first = ["python"]
second = first
second.append("workers")

print(first)
print(second)
```

```output
['python', 'workers']
['python', 'workers']
```
:::

:::cell
Understanding mutability explains why copying containers, avoiding mutable defaults, and returning new values are recurring Python design choices.

```python
text = "python"
text.upper()
print(text)
```

```output
python
```
:::

:::note
- Lists and dictionaries are mutable; strings and tuples are immutable.
- Aliasing is useful, but copy mutable containers when independent changes are needed.
:::
