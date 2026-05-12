+++
slug = "object-lifecycle"
title = "Object Lifecycle"
section = "Basics"
summary = "Names keep objects reachable until the last reference goes away."
doc_path = "/reference/datamodel.html#objects-values-and-types"
see_also = [
  "variables",
  "mutability",
  "classes",
]
+++

Python objects live independently from the names that refer to them. Assignment adds another reference to an object; rebinding a name points that name somewhere else; `del` removes a name. The object can be reclaimed only after it is no longer reachable.

Most programs do not manually destroy objects. They control lifetime by controlling which containers, local variables, and object attributes still hold references.

This example uses a small class so the object has visible state. The important evidence is that deleting one name does not destroy the object while another name still refers to it.

:::program
```python
class Box:
    def __init__(self, label):
        self.label = label

box = Box("draft")
alias = box

print(box is alias)
print(alias.label)

box = Box("published")
print(alias.label)
print(box.label)

del alias
print("old object unreachable")
```
:::

:::cell
Two names can refer to the same object. Mutating through one name would affect the object seen through the other.

```python
class Box:
    def __init__(self, label):
        self.label = label

box = Box("draft")
alias = box

print(box is alias)
print(alias.label)
```

```output
True
draft
```
:::

:::cell
Rebinding `box` does not change the original object. `alias` still reaches the first `Box` until that reference is removed too.

```python
box = Box("published")
print(alias.label)
print(box.label)

del alias
print("old object unreachable")
```

```output
draft
published
old object unreachable
```
:::

:::note
- Assignment binds names to objects; it does not copy the object.
- `del name` removes one reference, not necessarily the object itself.
- Python reclaims unreachable objects automatically, so lifetime bugs usually come from keeping references longer than intended.
:::
