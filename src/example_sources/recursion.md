+++
slug = "recursion"
title = "Recursion"
section = "Functions"
summary = "Recursive functions solve nested problems by calling themselves on smaller pieces."
doc_path = "/tutorial/controlflow.html#defining-functions"
see_also = [
  "functions",
  "conditionals",
  "generators",
]
+++

A recursive function calls itself to solve a smaller piece of the same problem. Recursion exists for data that is naturally nested: trees, menus, expression nodes, and directory-like structures.

Every recursive function needs a base case that can be answered directly. The recursive case must move toward that base case by passing a smaller part of the data.

Prefer loops for simple repetition over a flat sequence. Prefer recursion when the data shape is recursive too.

:::program
```python
tree = {
    "value": 1,
    "children": [
        {"value": 2, "children": []},
        {"value": 3, "children": [{"value": 4, "children": []}]},
    ],
}

def total(node):
    subtotal = node["value"]
    for child in node["children"]:
        subtotal += total(child)
    return subtotal

print(total({"value": 2, "children": []}))
print(total(tree))
```
:::

:::cell
A leaf node is the base case. It has no children, so the function can return its own value without making another recursive call.

```python
def total(node):
    subtotal = node["value"]
    for child in node["children"]:
        subtotal += total(child)
    return subtotal

print(total({"value": 2, "children": []}))
```

```output
2
```
:::

:::cell
A non-leaf node solves the same problem for each child, then combines those smaller totals with its own value.

```python
tree = {
    "value": 1,
    "children": [
        {"value": 2, "children": []},
        {"value": 3, "children": [{"value": 4, "children": []}]},
    ],
}

print(total(tree))
```

```output
10
```
:::

:::note
- Every recursive function needs a base case that stops the calls.
- Recursion fits nested data better than flat repetition.
- Python limits recursion depth, so loops are often better for very deep or simple repetition.
:::
