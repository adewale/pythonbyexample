+++
slug = "testing"
title = "Testing"
section = "Standard Library"
summary = "Tests make expected behavior executable and repeatable."
doc_path = "/library/unittest.html"
scope_first_pass = true
see_also = [
  "assertions",
  "exceptions",
  "modules",
]
+++

Tests turn expected behavior into code that can be run again. The useful unit is usually a small example of behavior with clear input, action, and assertion.

Python's `unittest` library provides test cases, assertions, suites, and runners. Projects often use `pytest` for ergonomics, but the same idea remains: a test names behavior and fails when the behavior changes.

A broad testing practice also includes fixtures, integration tests, property tests, and coverage. This example stays on the smallest standard-library loop: define behavior, assert the result, run the suite, inspect success.

:::program
```python
import io
import unittest


def add(left, right):
    return left + right

class AddTests(unittest.TestCase):
    def test_adds_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_adds_empty_strings(self):
        self.assertEqual(add("", "py"), "py")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(AddTests)
stream = io.StringIO()
result = unittest.TextTestRunner(stream=stream, verbosity=0).run(suite)
print(result.testsRun)
print(result.wasSuccessful())
```
:::

:::cell
A test starts with behavior small enough to name. The function can be ordinary code; the test supplies a representative input and expected result.

```python
def add(left, right):
    return left + right

print(add(2, 3))
```

```output
5
```
:::

:::cell
`unittest.TestCase` groups test methods. Assertion methods such as `assertEqual` make the expected behavior explicit.

```python
import unittest

class AddTests(unittest.TestCase):
    def test_adds_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_adds_empty_strings(self):
        self.assertEqual(add("", "py"), "py")

print([name for name in dir(AddTests) if name.startswith("test_")])
```

```output
['test_adds_empty_strings', 'test_adds_numbers']
```
:::

:::cell
A runner executes the suite and records whether every assertion passed. Capturing the runner stream keeps this page's output deterministic.

```python
import io

suite = unittest.defaultTestLoader.loadTestsFromTestCase(AddTests)
stream = io.StringIO()
result = unittest.TextTestRunner(stream=stream, verbosity=0).run(suite)
print(result.testsRun)
print(result.wasSuccessful())
```

```output
2
True
```
:::

:::note
- Test method names should describe behavior, not implementation details.
- A good unit test is deterministic and independent of test order.
- Use broader integration tests when the behavior depends on several components working together.
:::
