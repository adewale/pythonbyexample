+++
slug = "type-aliases"
title = "Type Aliases"
section = "Types"
summary = "Type aliases give a meaningful name to a repeated type shape."
doc_path = "/library/typing.html#type-aliases"
see_also = [
  "type-hints",
  "newtype",
  "union-and-optional-types",
]
+++

A type alias gives a name to an annotation shape. It helps readers and type checkers understand the role of a value without repeating a long type expression everywhere.

Python 3.13 supports the `type` statement for explicit aliases. Older assignment-style aliases still appear in code, but the `type` statement makes the intent clear and creates a `TypeAliasType` object at runtime.

An alias does not create a new runtime type. If you need a static distinction between compatible values such as user IDs and order IDs, use `NewType` instead.

:::program
```python
type UserId = int
type Scores = dict[UserId, int]
LegacyName = str


def best_user(scores: Scores) -> UserId:
    return max(scores, key=scores.get)

scores: Scores = {1: 98, 2: 91}
print(best_user(scores))
print(UserId.__name__)
print(LegacyName("Ada"))
```
:::

:::cell
The `type` statement names an annotation shape. Here `Scores` means a dictionary from user IDs to integer scores.

```python
type UserId = int
type Scores = dict[UserId, int]


def best_user(scores: Scores) -> UserId:
    return max(scores, key=scores.get)

scores: Scores = {1: 98, 2: 91}
print(best_user(scores))
```

```output
1
```
:::

:::cell
Modern aliases are runtime objects that keep their alias name for introspection.

```python
print(UserId.__name__)
print(Scores.__name__)
```

```output
UserId
Scores
```
:::

:::cell
Assignment-style aliases are still common, but they are just ordinary names bound to existing objects.

```python
LegacyName = str
print(LegacyName("Ada"))
print(LegacyName is str)
```

```output
Ada
True
```
:::

:::note
- Use aliases to name repeated or domain-specific annotation shapes.
- A type alias does not validate values at runtime.
- Use `NewType` when two values share a runtime representation but should not be mixed statically.
:::
