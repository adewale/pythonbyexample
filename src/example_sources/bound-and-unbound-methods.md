+++
slug = "bound-and-unbound-methods"
title = "Bound and Unbound Methods"
section = "Data Model"
summary = "instance.method binds self automatically; Class.method is a plain function."
doc_path = "/reference/datamodel.html#instance-methods"
see_also = [
  "classes",
  "attribute-access",
  "descriptors",
  "callable-objects",
]
+++

When you write `instance.method`, Python returns a bound method — a callable that already remembers which instance to pass as `self`. When you write `Class.method`, you get the underlying function back, and calling it requires passing an instance yourself.

That distinction is why methods can be stored in collections, passed as callbacks, and called later without losing track of the object they belong to. Each bound method carries its own `__self__`, so two callables produced from two different instances stay independent even when their underlying function is the same.

The mechanism is the descriptor protocol: a function attached to a class implements `__get__`, and that hook turns attribute access on an instance into a bound method. The page does not need that detail to use methods, but it explains what is happening underneath.

:::program
```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1
        return self.value

bound_counter = Counter(10)
m = bound_counter.increment
print(m.__self__ is bound_counter)
print(m())
print(m())

unbound_counter = Counter(0)
unbound = Counter.increment
print(type(unbound).__name__)
print(unbound(unbound_counter))
print(unbound(unbound_counter))

handlers = []
for _ in range(2):
    handlers.append(Counter().increment)

print(handlers[0]())
print(handlers[0]())
print(handlers[1]())

descriptor_counter = Counter(0)
func = Counter.__dict__["increment"]
print(type(func).__name__)
rebound = func.__get__(descriptor_counter, Counter)
print(type(rebound).__name__)
print(rebound.__self__ is descriptor_counter)
```
:::

:::cell
`instance.method` returns a bound method. The method already remembers the instance through `__self__`, so calling it does not require passing `self` again.

```python
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1
        return self.value

bound_counter = Counter(10)
m = bound_counter.increment
print(m.__self__ is bound_counter)
print(m())
print(m())
```

```output
True
11
12
```
:::

:::cell
`Class.method` returns the underlying function — there is no `self` attached. Calling it requires passing the instance as the first argument explicitly. Using a fresh counter here makes the output independent of the previous cell.

```python
unbound_counter = Counter(0)
unbound = Counter.increment
print(type(unbound).__name__)
print(unbound(unbound_counter))
print(unbound(unbound_counter))
```

```output
function
1
2
```
:::

:::cell
Bound methods are first-class values. They can be stored in lists, passed to other functions, and called later. Each bound method carries its own `__self__`, so two methods produced from two different instances stay independent.

```python
handlers = []
for _ in range(2):
    handlers.append(Counter().increment)

print(handlers[0]())
print(handlers[0]())
print(handlers[1]())
```

```output
1
2
1
```
:::

:::cell
The binding is the descriptor protocol at work. The function lives on the class as a plain function; instance attribute access invokes `__get__`, which returns a bound method that knows the instance.

```python
descriptor_counter = Counter(0)
func = Counter.__dict__["increment"]
print(type(func).__name__)
rebound = func.__get__(descriptor_counter, Counter)
print(type(rebound).__name__)
print(rebound.__self__ is descriptor_counter)
```

```output
function
method
True
```
:::

:::note
- `instance.method` produces a bound method whose `__self__` is the instance.
- `Class.method` produces the plain function and requires you to pass the instance.
- Each bound method is its own object; storing one captures its instance.
- The binding is implemented by the descriptor protocol on the function object.
:::
