# Markdown cell migration investigation

The rollback showed that the migration problem is not Markdown itself. The problem is coupling three different things into one source block:

1. the full editable program;
2. the literate source fragment shown beside prose;
3. the executable unit used by the verifier.

The first migration derived the full editor program by joining cells. That made non-executable explanatory fragments impossible and caused several examples to collapse into one large cell. The better model is:

- `:::program` owns the full editable source and must match the current `src/examples.py` code byte-for-byte during migration;
- `:::cell` owns a verified teaching fragment with nearby output;
- cells may restate earlier definitions to stay executable;
- cells are not concatenated to make the editor program.

## Examples that lost fine-grained cells

These examples collapsed during the attempted migration:

- `match-statements`
- `recursion`
- `classes`
- `properties`
- `special-methods`
- `type-hints`

## Proposed executable cell rewrites

These sketches preserve fine-grained teaching while keeping cells executable.

### `match-statements`

Use separate complete `match` statements with different command values:

```python
command = {"action": "move", "x": 3, "y": 4}

match command:
    case {"action": "move", "x": x, "y": y}:
        print(f"move to {x},{y}")
```

```output
move to 3,4
```

```python
command = {"action": "quit"}

match command:
    case {"action": "move", "x": x, "y": y}:
        print(f"move to {x},{y}")
    case {"action": "quit"}:
        print("quit")
```

```output
quit
```

```python
command = {"action": "jump"}

match command:
    case {"action": "move", "x": x, "y": y}:
        print(f"move to {x},{y}")
    case {"action": "quit"}:
        print("quit")
    case {"action": action}:
        print(f"unknown action: {action}")
    case _:
        print("invalid command")
```

```output
unknown action: jump
```

### `recursion`

Show the base case first, then the recursive case:

```python
def factorial(n):
    if n == 0:
        return 1

print(factorial(0))
```

```output
1
```

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

```output
120
```

### `classes`

Restate the class as it gains behavior:

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

first = Counter()
second = Counter(10)
print(first.value)
print(second.value)
```

```output
0
10
```

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self, amount=1):
        self.value += amount
        return self.value

first = Counter()
second = Counter(10)
print(first.increment())
print(second.increment(5))
```

```output
1
15
```

### `properties`

Show stored attributes first, then the computed property:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

box = Rectangle(3, 4)
print(box.width)
print(box.height)
```

```output
3
4
```

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

box = Rectangle(3, 4)
print(box.area)
```

```output
12
```

### `special-methods`

Restate the class as each protocol method is added:

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

bag = Bag(["a", "b"])
print(bag.items)
```

```output
['a', 'b']
```

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

bag = Bag(["a", "b"])
print(len(bag))
```

```output
2
```

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

bag = Bag(["a", "b"])
print(list(bag))
```

```output
['a', 'b']
```

```python
class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __repr__(self):
        return f"Bag({self.items!r})"

bag = Bag(["a", "b"])
print(bag)
```

```output
Bag(['a', 'b'])
```

### `type-hints`

Show runtime behavior separately from stored annotations:

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

print(total([1, 2, 3]))
```

```output
6
```

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)

print(total.__annotations__)
```

```output
{'numbers': list[int], 'return': <class 'int'>}
```

## Recommendation

Before another Markdown migration, first update the current examples or golden fixture to use executable fine-grained teaching cells. Then migrate to Markdown with `:::program` preserving the editor source exactly and `:::cell` preserving the literate teaching structure.
