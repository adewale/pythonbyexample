"""Versioned example catalog for Python By Example.

This fixture freezes the reviewed public catalog for migration/parity checks.
Update it intentionally after example rewrites have passed verification.
"""

PYTHON_VERSION = '3.13'
REFERENCE_URL = 'https://docs.python.org/3.13/'

EXAMPLES = [{'slug': 'hello-world',
  'title': 'Hello World',
  'section': 'Basics',
  'summary': 'The first Python program prints a line of text.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/introduction.html',
  'code': 'print("hello world")\n',
  'expected_output': 'hello world\n',
  'notes': ['`print()` writes text followed by a newline.', 'Strings can be delimited with single or double quotes.'],
  'cells': [{'prose': ['Every Python program starts by executing statements from top to bottom. Calling `print()` is '
                       'the smallest useful program because it shows how Python evaluates an expression and sends text '
                       'to standard output.'],
             'code': 'print("hello world")',
             'output': 'hello world',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'values',
  'title': 'Values',
  'section': 'Basics',
  'summary': 'Python programs evaluate expressions into objects such as text, numbers, booleans, and None.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html',
  'code': 'text = "python"\n'
          'count = 3\n'
          'ratio = 2.5\n'
          'ready = True\n'
          'missing = None\n'
          '\n'
          'print(type(text).__name__)\n'
          'print(text.upper())\n'
          'print(count + 4)\n'
          'print(ratio * 2)\n'
          '\n'
          'print(ready and count > 0)\n'
          'print(missing is None)\n',
  'expected_output': 'str\nPYTHON\n7\n5.0\nTrue\nTrue\n',
  'notes': ['Values are objects; names point to them and operations usually create new values.',
            'Use `is None` for the absence marker, not `== None`.',
            'This overview introduces boundaries that later pages explain in detail.'],
  'cells': [{'prose': ['Start with several built-in values. Python does not require declarations before binding these '
                       'names, and each value is still an object with a type.'],
             'code': 'text = "python"\n'
                     'count = 3\n'
                     'ratio = 2.5\n'
                     'ready = True\n'
                     'missing = None\n'
                     '\n'
                     'print(type(text).__name__)',
             'output': 'str',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Methods and operators evaluate to new values. The original `text`, `count`, and `ratio` '
                       'bindings remain ordinary objects you can reuse.'],
             'code': 'print(text.upper())\nprint(count + 4)\nprint(ratio * 2)',
             'output': 'PYTHON\n7\n5.0',
             'line': 35,
             'kind': 'cell'},
            {'prose': ['Boolean expressions combine facts, and `None` is checked by identity because it is a singleton '
                       'absence marker.'],
             'code': 'print(ready and count > 0)\nprint(missing is None)',
             'output': 'True\nTrue',
             'line': 51,
             'kind': 'cell'}]},
 {'slug': 'literals',
  'title': 'Literals',
  'section': 'Basics',
  'summary': 'Literals write values directly in Python source code.',
  'doc_url': 'https://docs.python.org/3.13/reference/lexical_analysis.html#literals',
  'code': 'whole = 42\n'
          'fraction = 3.5\n'
          'complex_number = 2 + 3j\n'
          'print(whole, fraction, complex_number.imag)\n'
          '\n'
          'text = "python"\n'
          'raw_pattern = r"\\d+"\n'
          'data = b"py"\n'
          'print(text)\n'
          'print(raw_pattern)\n'
          'print(data)\n'
          '\n'
          'point = (2, 3)\n'
          'names = ["Ada", "Grace"]\n'
          'scores = {"Ada": 98}\n'
          'unique = {"py", "go"}\n'
          'print(point)\n'
          'print(names[0])\n'
          'print(scores["Ada"])\n'
          'print(sorted(unique))\n'
          '\n'
          'print(True, False, None)\n'
          'print(...)\n',
  'expected_output': "42 3.5 3.0\npython\n\\d+\nb'py'\n(2, 3)\nAda\n98\n['go', 'py']\nTrue False None\nEllipsis\n",
  'notes': ['Literals are good for small local values; constants are better for repeated values with meaning.',
            '`{}` is an empty dictionary. Use `set()` for an empty set.',
            'Bytes literals are binary data; string literals are Unicode text.',
            '`...` evaluates to the `Ellipsis` object.'],
  'cells': [{'prose': ['Numeric literals write numbers directly. Complex literals use `j` for the imaginary part.'],
             'code': 'whole = 42\nfraction = 3.5\ncomplex_number = 2 + 3j\nprint(whole, fraction, complex_number.imag)',
             'output': '42 3.5 3.0',
             'line': 23,
             'kind': 'cell'},
            {'prose': ['String literals write Unicode text. Raw strings keep backslashes literal, and bytes literals '
                       'write binary data rather than text.'],
             'code': 'text = "python"\n'
                     'raw_pattern = r"\\d+"\n'
                     'data = b"py"\n'
                     'print(text)\n'
                     'print(raw_pattern)\n'
                     'print(data)',
             'output': "python\n\\d+\nb'py'",
             'line': 38,
             'kind': 'cell'},
            {'prose': ['Container literals create tuples, lists, dictionaries, and sets. Each container answers a '
                       'different question about order, position, lookup, or uniqueness.'],
             'code': 'point = (2, 3)\n'
                     'names = ["Ada", "Grace"]\n'
                     'scores = {"Ada": 98}\n'
                     'unique = {"py", "go"}\n'
                     'print(point)\n'
                     'print(names[0])\n'
                     'print(scores["Ada"])\n'
                     'print(sorted(unique))',
             'output': "(2, 3)\nAda\n98\n['go', 'py']",
             'line': 57,
             'kind': 'cell'},
            {'prose': ['`True`, `False`, `None`, and `...` are singleton literal-like constants used for truth values, '
                       'absence, and placeholders.'],
             'code': 'print(True, False, None)\nprint(...)',
             'output': 'True False None\nEllipsis',
             'line': 79,
             'kind': 'cell'}]},
 {'slug': 'numbers',
  'title': 'Numbers',
  'section': 'Basics',
  'summary': 'Python numbers include integers, floats, and complex values.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#numeric-types-int-float-complex',
  'code': 'count = 10\n'
          'ratio = 0.25\n'
          'z = 2 + 3j\n'
          '\n'
          'print(count + 5)\n'
          'print(count / 4)\n'
          'print(count // 4)\n'
          'print(count % 4)\n'
          'print(2 ** 5)\n'
          'print(z.real, z.imag)\n'
          'print(0.1 + 0.2)\n'
          'print(round(3.14159, 2))\n',
  'expected_output': '15\n2.5\n2\n2\n32\n2.0 3.0\n0.30000000000000004\n3.14\n',
  'notes': ["Python's `int` has arbitrary precision; it grows as large as memory allows.",
            "Python's `float` is approximate double-precision floating point.",
            'Use `/` for true division and `//` for floor division.',
            'Use `decimal.Decimal` when decimal precision is the domain requirement, not just display polish.'],
  'cells': [{'prose': ['Python has `int` for whole numbers and `float` for approximate real-valued arithmetic. True '
                       'division with `/` returns a `float`, even when both inputs are integers.'],
             'code': 'count = 10\nratio = 0.25\n\nprint(count + 5)\nprint(count / 4)\nprint(ratio * 2)',
             'output': '15\n2.5\n0.5',
             'line': 21,
             'kind': 'cell'},
            {'prose': ['Floor division and modulo are useful when you need quotient and remainder behavior. Powers use '
                       '`**`, not `^`.'],
             'code': 'print(count // 4)\nprint(count % 4)\nprint(2 ** 5)',
             'output': '2\n2\n32',
             'line': 40,
             'kind': 'cell'},
            {'prose': ['Complex numbers are built in. The literal suffix `j` marks the imaginary part.'],
             'code': 'z = 2 + 3j\nprint(z.real, z.imag)',
             'output': '2.0 3.0',
             'line': 56,
             'kind': 'cell'},
            {'prose': ['Floating-point values are approximate. Round for display when the exact binary representation '
                       'is not the lesson.'],
             'code': 'print(0.1 + 0.2)\nprint(round(3.14159, 2))',
             'output': '0.30000000000000004\n3.14',
             'line': 69,
             'kind': 'cell'}]},
 {'slug': 'booleans',
  'title': 'Booleans',
  'section': 'Basics',
  'summary': 'Booleans represent truth values and combine with logical operators.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#boolean-type-bool',
  'code': 'logged_in = True\n'
          'has_permission = False\n'
          '\n'
          'print(logged_in and has_permission)\n'
          'print(logged_in or has_permission)\n'
          'print(not has_permission)\n'
          '\n'
          'name = "Ada"\n'
          'print(name == "Ada" and len(name) > 0)\n',
  'expected_output': 'False\nTrue\nTrue\nTrue\n',
  'notes': ['Boolean constants are `True` and `False`, with capital letters.',
            '`and` and `or` short-circuit: Python does not evaluate the right side if the left side already determines '
            'the result.',
            'Prefer truthiness for containers and explicit comparisons when the exact boolean condition matters.'],
  'cells': [{'prose': ['Use booleans for facts that are either true or false. Python spells the constants `True` and '
                       '`False`.',
                       'Use `and`, `or`, and `not` to combine truth values. These operators read like English and '
                       'short-circuit when possible.'],
             'code': 'logged_in = True\n'
                     'has_permission = False\n'
                     '\n'
                     'print(logged_in and has_permission)\n'
                     'print(logged_in or has_permission)\n'
                     'print(not has_permission)',
             'output': 'False\nTrue\nTrue',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Comparisons produce booleans too, so they compose naturally with logical operators in '
                       'conditions and validation checks.'],
             'code': 'name = "Ada"\nprint(name == "Ada" and len(name) > 0)',
             'output': 'True',
             'line': 38,
             'kind': 'cell'}]},
 {'slug': 'operators',
  'title': 'Operators',
  'section': 'Basics',
  'summary': 'Operators combine, compare, and test values in expressions.',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#operator-precedence',
  'code': 'count = 10\n'
          'print(count + 5)\n'
          'print(count // 4)\n'
          'print(count % 4)\n'
          'print(2 ** 5)\n'
          '\n'
          'score = 91\n'
          'print(80 <= score < 100)\n'
          'print(score == 100 or score >= 90)\n'
          'print("py" in "python")\n'
          '\n'
          'flags = 0b0011\n'
          'print(flags ^ 0b0101)\n'
          'print(flags << 1)\n'
          '\n'
          'class Scale:\n'
          '    def __init__(self, value):\n'
          '        self.value = value\n'
          '\n'
          '    def __matmul__(self, other):\n'
          '        return self.value * other.value\n'
          '\n'
          'print(Scale(2) @ Scale(3))\n'
          '\n'
          'items = ["a", "b"]\n'
          'if (size := len(items)) > 0:\n'
          '    print(size)\n',
  'expected_output': '15\n2\n2\n32\nTrue\nTrue\nTrue\n6\n6\n6\n2\n',
  'notes': ['Use the clearest operator for the question: arithmetic, comparison, boolean logic, membership, identity, '
            'or bitwise manipulation.',
            '`and` and `or` short-circuit, so the right side may not run.',
            'Operators have precedence; use parentheses when grouping would otherwise be hard to read.',
            'Custom operator behavior should make an object feel more natural, not more clever.'],
  'cells': [{'prose': ['Arithmetic operators compute new values. Use `//` for floor division, `%` for remainder, and '
                       '`**` for powers.'],
             'code': 'count = 10\nprint(count + 5)\nprint(count // 4)\nprint(count % 4)\nprint(2 ** 5)',
             'output': '15\n2\n2\n32',
             'line': 23,
             'kind': 'cell'},
            {'prose': ['Comparison operators produce booleans. Python comparisons can chain, which keeps range checks '
                       'readable.'],
             'code': 'score = 91\n'
                     'print(80 <= score < 100)\n'
                     'print(score == 100 or score >= 90)\n'
                     'print("py" in "python")',
             'output': 'True\nTrue\nTrue',
             'line': 42,
             'kind': 'cell'},
            {'prose': ['Bitwise operators work on integer bit patterns. They are useful for masks and flags, not '
                       'ordinary boolean logic.'],
             'code': 'flags = 0b0011\nprint(flags ^ 0b0101)\nprint(flags << 1)',
             'output': '6\n6',
             'line': 59,
             'kind': 'cell'},
            {'prose': ['The `@` operator is reserved for matrix-like multiplication and custom types that define '
                       '`__matmul__`.'],
             'code': 'class Scale:\n'
                     '    def __init__(self, value):\n'
                     '        self.value = value\n'
                     '\n'
                     '    def __matmul__(self, other):\n'
                     '        return self.value * other.value\n'
                     '\n'
                     'print(Scale(2) @ Scale(3))',
             'output': '6',
             'line': 74,
             'kind': 'cell'},
            {'prose': ['The walrus operator `:=` assigns inside an expression. Use it when naming a value avoids '
                       'repeating work in a condition.'],
             'code': 'items = ["a", "b"]\nif (size := len(items)) > 0:\n    print(size)',
             'output': '2',
             'line': 93,
             'kind': 'cell'}]},
 {'slug': 'none',
  'title': 'None',
  'section': 'Basics',
  'summary': 'None represents expected absence, distinct from missing keys and errors.',
  'doc_url': 'https://docs.python.org/3.13/library/constants.html#None',
  'code': 'result = None\n'
          'print(result is None)\n'
          '\n'
          'def find_score(name):\n'
          '    if name == "Ada":\n'
          '        return 10\n'
          '    return None\n'
          '\n'
          'score = find_score("Grace")\n'
          'print(score is None)\n'
          '\n'
          'profile = {"name": "Ada"}\n'
          'print(profile.get("timezone", "UTC"))\n'
          '\n'
          'try:\n'
          '    int("python")\n'
          'except ValueError:\n'
          '    print("invalid number")\n',
  'expected_output': 'True\nTrue\nUTC\ninvalid number\n',
  'notes': ['Use `is None` rather than `== None`; `None` is a singleton identity value.',
            'Use `None` for expected absence that callers can test.',
            'Use dictionary defaults for missing mapping keys and exceptions for invalid operations.'],
  'cells': [{'prose': ["`None` is Python's value for “nothing here.” Check it with `is None` because it is a singleton "
                       'identity value.'],
             'code': 'result = None\nprint(result is None)',
             'output': 'True',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Functions often return `None` when absence is expected and callers can continue. The function '
                       'name and surrounding code should make that possibility clear.'],
             'code': 'def find_score(name):\n'
                     '    if name == "Ada":\n'
                     '        return 10\n'
                     '    return None\n'
                     '\n'
                     'score = find_score("Grace")\n'
                     'print(score is None)',
             'output': 'True',
             'line': 30,
             'kind': 'cell'},
            {'prose': ['A missing dictionary key is another absence boundary. Use `get()` when the mapping can supply '
                       'a default, and use exceptions for invalid operations that cannot produce a value.'],
             'code': 'profile = {"name": "Ada"}\n'
                     'print(profile.get("timezone", "UTC"))\n'
                     '\n'
                     'try:\n'
                     '    int("python")\n'
                     'except ValueError:\n'
                     '    print("invalid number")',
             'output': 'UTC\ninvalid number',
             'line': 48,
             'kind': 'cell'}]},
 {'slug': 'variables',
  'title': 'Variables',
  'section': 'Basics',
  'summary': 'Names are bound to values with assignment.',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#assignment-statements',
  'code': 'message = "hi"\n'
          'print(message)\n'
          '\n'
          'message = "hello"\n'
          'print(message)\n'
          '\n'
          'count = 3\n'
          'count += 1\n'
          'print(count)\n',
  'expected_output': 'hi\nhello\n4\n',
  'notes': ['Python variables are names bound to objects, not boxes with fixed types.',
            'Rebinding a name is normal.',
            'Use augmented assignment for counters and accumulators.'],
  'cells': [{'prose': ['Assignment binds a name to a value. Once bound, the name can be used anywhere that value is '
                       'needed.'],
             'code': 'message = "hi"\nprint(message)',
             'output': 'hi',
             'line': 19,
             'kind': 'cell'},
            {'prose': ['Assignment can rebind the same name to a different value. The name is not permanently attached '
                       'to the first object.'],
             'code': 'message = "hello"\nprint(message)',
             'output': 'hello',
             'line': 32,
             'kind': 'cell'},
            {'prose': ['Augmented assignment reads the current binding, computes an updated value, and stores the '
                       'result back under the same name.'],
             'code': 'count = 3\ncount += 1\nprint(count)',
             'output': '4',
             'line': 45,
             'kind': 'cell'}]},
 {'slug': 'constants',
  'title': 'Constants',
  'section': 'Basics',
  'summary': 'Python uses naming conventions for values that should not change.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#python-scopes-and-namespaces',
  'code': 'MAX_RETRIES = 3\n'
          'API_VERSION = "2026-05"\n'
          '\n'
          'for attempt in range(1, MAX_RETRIES + 1):\n'
          '    print(f"attempt {attempt} of {MAX_RETRIES}")\n'
          '\n'
          'print(API_VERSION)\n',
  'expected_output': 'attempt 1 of 3\nattempt 2 of 3\nattempt 3 of 3\n2026-05\n',
  'notes': ['Python has no `const` keyword for ordinary names.',
            'All-caps names such as `MAX_RETRIES` communicate that a value is intended to stay fixed.'],
  'cells': [{'prose': ['Python does not have a `const` declaration like Go or Rust. Instead, modules use all-caps '
                       'names for values callers should treat as fixed.',
                       'The interpreter will still let you rebind the name, but the convention is strong enough that '
                       'readers understand the design intent.'],
             'code': 'MAX_RETRIES = 3\n'
                     'API_VERSION = "2026-05"\n'
                     '\n'
                     'for attempt in range(1, MAX_RETRIES + 1):\n'
                     '    print(f"attempt {attempt} of {MAX_RETRIES}")',
             'output': 'attempt 1 of 3\nattempt 2 of 3\nattempt 3 of 3',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Constants are useful for configuration values that should be named once and reused instead of '
                       'repeated as magic literals.'],
             'code': 'print(API_VERSION)',
             'output': '2026-05',
             'line': 37,
             'kind': 'cell'}]},
 {'slug': 'truthiness',
  'title': 'Truthiness',
  'section': 'Basics',
  'summary': 'Python conditions use truthiness, not only explicit booleans.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing',
  'code': 'items = []\n'
          'name = "Ada"\n'
          '\n'
          'if not items:\n'
          '    print("no items")\n'
          '\n'
          'if name:\n'
          '    print("has a name")\n'
          '\n'
          'print(bool(0))\n'
          'print(bool(42))\n',
  'expected_output': 'no items\nhas a name\nFalse\nTrue\n',
  'notes': ['Empty containers and zero-like numbers are false in conditions.',
            'Use explicit comparisons when they communicate intent better than truthiness.'],
  'cells': [{'prose': ["Truthiness is one of Python's most important conveniences: conditions can test objects "
                       'directly instead of requiring explicit boolean comparisons everywhere.',
                       'Empty containers, numeric zero, None, and False are false; most other values are true. This '
                       'makes common checks such as if items: concise and idiomatic.'],
             'code': 'items = []\nname = "Ada"\n\nif not items:\n    print("no items")',
             'output': 'no items',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Use truthiness when it reads naturally, but choose explicit comparisons when the distinction '
                       'matters, such as checking whether a value is exactly None.'],
             'code': 'if name:\n    print("has a name")',
             'output': 'has a name',
             'line': 35,
             'kind': 'cell'},
            {'prose': ['Use truthiness when it reads naturally, but choose explicit comparisons when the distinction '
                       'matters, such as checking whether a value is exactly None.'],
             'code': 'print(bool(0))\nprint(bool(42))',
             'output': 'False\nTrue',
             'line': 48,
             'kind': 'cell'}]},
 {'slug': 'equality-and-identity',
  'title': 'Equality and Identity',
  'section': 'Data Model',
  'summary': '== compares values, while is compares object identity.',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#is-not',
  'code': 'left = [1, 2, 3]\n'
          'right = [1, 2, 3]\n'
          'print(left == right)\n'
          'print(left is right)\n'
          '\n'
          'same = left\n'
          'same.append(4)\n'
          'print(left)\n'
          'print(same is left)\n'
          '\n'
          'value = None\n'
          'print(value is None)\n',
  'expected_output': 'True\nFalse\n[1, 2, 3, 4]\nTrue\nTrue\n',
  'notes': ['Use `==` for ordinary value comparisons.',
            'Use `is` primarily for identity checks against singletons such as `None`.',
            'Equal mutable containers can still be independent objects.'],
  'cells': [{'prose': ['Equal containers can be different objects. `==` compares list contents, while `is` checks '
                       'whether both names refer to the same list object.'],
             'code': 'left = [1, 2, 3]\nright = [1, 2, 3]\nprint(left == right)\nprint(left is right)',
             'output': 'True\nFalse',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Identity matters when objects are mutable. `same` is another name for `left`, so mutating '
                       'through one name changes the object seen through the other.'],
             'code': 'same = left\nsame.append(4)\nprint(left)\nprint(same is left)',
             'output': '[1, 2, 3, 4]\nTrue',
             'line': 33,
             'kind': 'cell'},
            {'prose': ['Use `is` for singleton identity checks such as `None`. This asks whether the value is the one '
                       'special `None` object.'],
             'code': 'value = None\nprint(value is None)',
             'output': 'True',
             'line': 49,
             'kind': 'cell'}]},
 {'slug': 'mutability',
  'title': 'Mutability',
  'section': 'Data Model',
  'summary': 'Some objects change in place, while others return new values.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types',
  'code': 'first = ["python"]\n'
          'second = first\n'
          'second.append("workers")\n'
          'print(first)\n'
          'print(second)\n'
          '\n'
          'text = "python"\n'
          'upper_text = text.upper()\n'
          'print(text)\n'
          'print(upper_text)\n'
          '\n'
          'numbers = [3, 1, 2]\n'
          'ordered = sorted(numbers)\n'
          'print(ordered)\n'
          'print(numbers)\n',
  'expected_output': "['python', 'workers']\n['python', 'workers']\npython\nPYTHON\n[1, 2, 3]\n[3, 1, 2]\n",
  'notes': ['Lists and dictionaries are mutable; strings and tuples are immutable.',
            'Aliasing is useful, but copy mutable containers when independent changes are needed.',
            'Pay attention to whether an operation mutates in place or returns a new value.'],
  'cells': [{'prose': ['Mutable objects can change in place. `first` and `second` point to the same list, so appending '
                       'through one name changes the object seen through both names.'],
             'code': 'first = ["python"]\nsecond = first\nsecond.append("workers")\nprint(first)\nprint(second)',
             'output': "['python', 'workers']\n['python', 'workers']",
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Immutable objects do not change in place. String methods such as `upper()` return a new '
                       'string, leaving the original string unchanged.'],
             'code': 'text = "python"\nupper_text = text.upper()\nprint(text)\nprint(upper_text)',
             'output': 'python\nPYTHON',
             'line': 34,
             'kind': 'cell'},
            {'prose': ['Some APIs make the boundary explicit. `sorted()` returns a new list, while methods such as '
                       '`append()` and `list.sort()` mutate an existing list.'],
             'code': 'numbers = [3, 1, 2]\nordered = sorted(numbers)\nprint(ordered)\nprint(numbers)',
             'output': '[1, 2, 3]\n[3, 1, 2]',
             'line': 50,
             'kind': 'cell'}]},
 {'slug': 'object-lifecycle',
  'title': 'Object Lifecycle',
  'section': 'Basics',
  'summary': 'References keep objects alive until Python can reclaim them.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types',
  'code': 'import gc\n'
          '\n'
          'names = []\n'
          'alias = names\n'
          'alias.append("Ada")\n'
          '\n'
          'print(names is alias)\n'
          'print(names)\n'
          '\n'
          'object_id = id(names)\n'
          'del alias\n'
          'print(id(names) == object_id)\n'
          '\n'
          'del names\n'
          'print("object can be reclaimed")\n'
          'gc.collect()\n',
  'expected_output': "True\n['Ada']\nTrue\nobject can be reclaimed\n",
  'notes': ['Use `is` and `id()` to observe identity while two names refer to the same object.',
            'Deleting a name removes one reference; it does not directly destroy the object if another reference still '
            'exists.',
            'Python reclaims unreachable objects automatically, so programs usually manage ownership by controlling '
            'references.'],
  'cells': [{'prose': ['Use `is` and `id()` to observe identity while two names refer to the same object.'],
             'code': 'import gc\n'
                     '\n'
                     'names = []\n'
                     'alias = names\n'
                     'alias.append("Ada")\n'
                     '\n'
                     'print(names is alias)\n'
                     'print(names)\n'
                     '\n'
                     'object_id = id(names)\n'
                     'del alias\n'
                     'print(id(names) == object_id)\n'
                     '\n'
                     'del names\n'
                     'print("object can be reclaimed")\n'
                     'gc.collect()',
             'output': "True\n['Ada']\nTrue\nobject can be reclaimed",
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'strings',
  'title': 'Strings',
  'section': 'Text',
  'summary': 'Strings are immutable Unicode text sequences.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#text-sequence-type-str',
  'code': 'english = "hello"\n'
          'thai = "สวัสดี"\n'
          '\n'
          'for label, word in [("English", english), ("Thai", thai)]:\n'
          '    print(label, word, len(word), len(word.encode("utf-8")))\n'
          '\n'
          'print(thai[0])\n'
          'print([hex(ord(char)) for char in thai[:2]])\n'
          '\n'
          'text = "  café  "\n'
          'clean = text.strip()\n'
          'print(clean)\n'
          'print(clean.upper())\n'
          'print(clean.encode("utf-8"))\n',
  'expected_output': "English hello 5 5\nThai สวัสดี 6 18\nส\n['0xe2a', '0xe27']\ncafé\nCAFÉ\nb'caf\\xc3\\xa9'\n",
  'notes': ['Use `str` for text and `bytes` for binary data.',
            '`len(text)` counts Unicode code points; `len(text.encode("utf-8"))` counts encoded bytes.',
            'ASCII text is a useful baseline because each ASCII code point is one UTF-8 byte.',
            'String methods return new strings because strings are immutable.',
            'User-visible “characters” can be more subtle than code points; combining marks and emoji sequences may '
            'need specialized text handling.'],
  'cells': [{'prose': ['Compare an English greeting with a Thai greeting. Both are Python `str` values, but UTF-8 uses '
                       'one byte for each ASCII code point and multiple bytes for many non-ASCII code points.'],
             'code': 'english = "hello"\n'
                     'thai = "สวัสดี"\n'
                     '\n'
                     'for label, word in [("English", english), ("Thai", thai)]:\n'
                     '    print(label, word, len(word), len(word.encode("utf-8")))',
             'output': 'English hello 5 5\nThai สวัสดี 6 18',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Indexing and iteration work with Unicode code points, not encoded bytes. `ord()` returns the '
                       'integer code point, which is often displayed in hexadecimal when teaching text encoding.'],
             'code': 'print(thai[0])\nprint([hex(ord(char)) for char in thai[:2]])',
             'output': "ส\n['0xe2a', '0xe27']",
             'line': 34,
             'kind': 'cell'},
            {'prose': ['String methods return new strings because strings are immutable. Encoding turns text into '
                       'bytes when another system needs a byte representation.'],
             'code': 'text = "  café  "\n'
                     'clean = text.strip()\n'
                     'print(clean)\n'
                     'print(clean.upper())\n'
                     'print(clean.encode("utf-8"))',
             'output': "café\nCAFÉ\nb'caf\\xc3\\xa9'",
             'line': 48,
             'kind': 'cell'}]},
 {'slug': 'bytes-and-bytearray',
  'title': 'Bytes and Bytearray',
  'section': 'Basics',
  'summary': 'bytes and bytearray store binary data, not Unicode text.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview',
  'code': 'text = "café"\n'
          'data = text.encode("utf-8")\n'
          '\n'
          'print(data)\n'
          'print(len(text), len(data))\n'
          'print(data.decode("utf-8"))\n'
          'print(data[0])\n'
          '\n'
          'packet = bytearray(b"py")\n'
          'packet[0] = ord("P")\n'
          'print(packet)\n',
  'expected_output': "b'caf\\xc3\\xa9'\n4 5\ncafé\n99\nbytearray(b'Py')\n",
  'notes': ['Encode text when an external boundary needs bytes.',
            'Decode bytes when you want text again.',
            'Indexing `bytes` returns integers from 0 to 255.',
            'Use `bytearray` when binary data must be changed in place.'],
  'cells': [{'prose': ['Encode text when an external boundary needs bytes. UTF-8 uses one byte for ASCII characters '
                       'and more than one byte for many other characters.'],
             'code': 'text = "café"\ndata = text.encode("utf-8")\nprint(data)\nprint(len(text), len(data))',
             'output': "b'caf\\xc3\\xa9'\n4 5",
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Decode bytes when the program needs text again. The decoder must match the encoding used at '
                       'the boundary.'],
             'code': 'print(data.decode("utf-8"))',
             'output': 'café',
             'line': 38,
             'kind': 'cell'},
            {'prose': ['Indexing a `bytes` object returns an integer byte value, not a one-character `bytes` object.'],
             'code': 'print(data[0])',
             'output': '99',
             'line': 50,
             'kind': 'cell'},
            {'prose': ['`bytes` is immutable. Use `bytearray` when binary data must be changed in place.'],
             'code': 'packet = bytearray(b"py")\npacket[0] = ord("P")\nprint(packet)',
             'output': "bytearray(b'Py')",
             'line': 62,
             'kind': 'cell'}]},
 {'slug': 'string-formatting',
  'title': 'String Formatting',
  'section': 'Text',
  'summary': 'f-strings turn values into readable text at the point of use.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/inputoutput.html#formatted-string-literals',
  'code': 'name = "Ada"\n'
          'score = 9.5\n'
          'rank = 1\n'
          '\n'
          'message = f"{name} scored {score}"\n'
          'print(message)\n'
          '\n'
          'row = f"{rank:>2} | {name:<8} | {score:05.1f}"\n'
          'print(row)\n'
          '\n'
          'print(f"{score = }")\n',
  'expected_output': 'Ada scored 9.5\n 1 | Ada      | 009.5\nscore = 9.5\n',
  'notes': ['Use `f"..."` strings for most new formatting code.',
            'Expressions inside braces are evaluated before formatting.',
            'Format specifications after `:` control alignment, width, padding, and precision.'],
  'cells': [{'prose': ['An f-string evaluates expressions inside braces and inserts their string form into the '
                       'surrounding text. This is clearer than joining several converted values by hand.'],
             'code': 'name = "Ada"\nscore = 9.5\nrank = 1\n\nmessage = f"{name} scored {score}"\nprint(message)',
             'output': 'Ada scored 9.5',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Format specifications after `:` control display without changing the underlying values. Here '
                       'the rank is right-aligned, the name is left-aligned, and the score is padded to one decimal '
                       'place.'],
             'code': 'row = f"{rank:>2} | {name:<8} | {score:05.1f}"\nprint(row)',
             'output': ' 1 | Ada      | 009.5',
             'line': 34,
             'kind': 'cell'},
            {'prose': ['The debug form with `=` is useful while learning or logging because it prints both the '
                       'expression and the value.'],
             'code': 'print(f"{score = }")',
             'output': 'score = 9.5',
             'line': 47,
             'kind': 'cell'}]},
 {'slug': 'conditionals',
  'title': 'Conditionals',
  'section': 'Control Flow',
  'summary': 'if, elif, and else choose which block runs.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#if-statements',
  'code': 'temperature = 72\n'
          '\n'
          'if temperature < 60:\n'
          '    print("cold")\n'
          'elif temperature < 80:\n'
          '    print("comfortable")\n'
          'else:\n'
          '    print("hot")\n'
          '\n'
          'items = ["coat", "hat"]\n'
          'if items:\n'
          '    print(f"packing {len(items)} items")\n'
          '\n'
          'status = "ok" if temperature < 90 else "danger"\n'
          'print(status)\n',
  'expected_output': 'comfortable\npacking 2 items\nok\n',
  'notes': ['Python has no mandatory parentheses around conditions; the colon and indentation define the block.',
            'Comparison operators such as `<` and `==` can be chained, as in `0 < value < 10`.',
            'Keep branch bodies short; move larger work into functions so the decision remains easy to scan.'],
  'cells': [{'prose': ['Start with the value that the branches will test. A conditional is only useful when the branch '
                       'condition is visible and meaningful.',
                       'Use `if`, `elif`, and `else` for one ordered choice. Python tests the branches from top to '
                       'bottom and runs only the first matching block.'],
             'code': 'temperature = 72\n'
                     '\n'
                     'if temperature < 60:\n'
                     '    print("cold")\n'
                     'elif temperature < 80:\n'
                     '    print("comfortable")\n'
                     'else:\n'
                     '    print("hot")',
             'output': 'comfortable',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Truthiness is part of conditional flow. Empty collections are false, so `if items:` reads as '
                       '“if there is anything to work with.”'],
             'code': 'items = ["coat", "hat"]\nif items:\n    print(f"packing {len(items)} items")',
             'output': 'packing 2 items',
             'line': 38,
             'kind': 'cell'},
            {'prose': ['Use the ternary expression when you are choosing a value. If either side needs multiple '
                       'statements, use a normal `if` block instead.'],
             'code': 'status = "ok" if temperature < 90 else "danger"\nprint(status)',
             'output': 'ok',
             'line': 52,
             'kind': 'cell'}]},
 {'slug': 'guard-clauses',
  'title': 'Guard Clauses',
  'section': 'Control Flow',
  'summary': 'Guard clauses handle exceptional cases early so the main path stays flat.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#if-statements',
  'code': 'def price_after_discount(price, percent):\n'
          '    if price < 0:\n'
          '        return "invalid price"\n'
          '    if not 0 <= percent <= 100:\n'
          '        return "invalid discount"\n'
          '\n'
          '    discount = price * percent / 100\n'
          '    return round(price - discount, 2)\n'
          '\n'
          'print(price_after_discount(100, 15))\n'
          'print(price_after_discount(-5, 10))\n'
          'print(price_after_discount(100, 120))\n',
  'expected_output': '85.0\ninvalid price\ninvalid discount\n',
  'notes': ['Return early when inputs cannot be handled.',
            'After the guards, the remaining code can read as the normal path.',
            'Guard clauses are a style choice, not new syntax.'],
  'cells': [{'prose': ['Return early when inputs cannot be handled.'],
             'code': 'def price_after_discount(price, percent):\n'
                     '    if price < 0:\n'
                     '        return "invalid price"\n'
                     '    if not 0 <= percent <= 100:\n'
                     '        return "invalid discount"\n'
                     '\n'
                     '    discount = price * percent / 100\n'
                     '    return round(price - discount, 2)\n'
                     '\n'
                     'print(price_after_discount(100, 15))\n'
                     'print(price_after_discount(-5, 10))\n'
                     'print(price_after_discount(100, 120))',
             'output': '85.0\ninvalid price\ninvalid discount',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'assignment-expressions',
  'title': 'Assignment Expressions',
  'section': 'Control Flow',
  'summary': 'The walrus operator assigns a value inside an expression.',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#assignment-expressions',
  'code': 'messages = ["hello", "", "python"]\n'
          '\n'
          'for message in messages:\n'
          '    if length := len(message):\n'
          '        print(message, length)\n'
          '\n'
          'queue = ["retry", "ok"]\n'
          'while (status := queue.pop(0)) != "ok":\n'
          '    print(status)\n'
          'print(status)\n',
  'expected_output': 'hello 5\npython 6\nretry\nok\n',
  'notes': ['`name := expression` assigns and evaluates to the assigned value.',
            'Use it to avoid computing the same value twice.',
            'Prefer a normal assignment when the expression becomes hard to scan.'],
  'cells': [{'prose': ['An assignment expression can name a computed value while a condition tests it. Here empty '
                       'strings are skipped because their length is zero.'],
             'code': 'messages = ["hello", "", "python"]\n'
                     '\n'
                     'for message in messages:\n'
                     '    if length := len(message):\n'
                     '        print(message, length)',
             'output': 'hello 5\npython 6',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['The same idea works in loops that read state until a sentinel appears. The assignment and '
                       'comparison stay together.'],
             'code': 'queue = ["retry", "ok"]\n'
                     'while (status := queue.pop(0)) != "ok":\n'
                     '    print(status)\n'
                     'print(status)',
             'output': 'retry\nok',
             'line': 39,
             'kind': 'cell'}]},
 {'slug': 'for-loops',
  'title': 'For Loops',
  'section': 'Control Flow',
  'summary': 'for iterates over any iterable object.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#for-statements',
  'code': 'for name in ["Ada", "Grace", "Guido"]:\n    print(name)\n\nfor number in range(3):\n    print(number)\n',
  'expected_output': 'Ada\nGrace\nGuido\n0\n1\n2\n',
  'notes': ['Blocks are defined by indentation.', 'range(3) yields 0, 1, and 2.'],
  'cells': [{'prose': ['Python for loops iterate over values from an iterable. This is different from languages where '
                       'for primarily means incrementing a numeric counter.'],
             'code': 'for name in ["Ada", "Grace", "Guido"]:\n    print(name)',
             'output': 'Ada\nGrace\nGuido',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['range() is itself an iterable that produces numbers lazily. Use it when you need a sequence of '
                       'integers, but prefer direct iteration when you already have a collection.'],
             'code': 'for number in range(3):\n    print(number)',
             'output': '0\n1\n2',
             'line': 32,
             'kind': 'cell'}]},
 {'slug': 'break-and-continue',
  'title': 'Break and Continue',
  'section': 'Control Flow',
  'summary': 'break exits a loop early, while continue skips to the next iteration.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements',
  'code': 'names = ["Ada", "", "Grace"]\n'
          'for name in names:\n'
          '    if not name:\n'
          '        continue\n'
          '    print(name)\n'
          '\n'
          'commands = ["load", "save", "stop", "delete"]\n'
          'for command in commands:\n'
          '    if command == "stop":\n'
          '        break\n'
          '    print(command)\n',
  'expected_output': 'Ada\nGrace\nload\nsave\n',
  'notes': ['`continue` skips to the next loop iteration.',
            '`break` exits the nearest enclosing loop immediately.',
            'Prefer plain `if`/`else` when the loop does not need early skip or early stop behavior.'],
  'cells': [{'prose': ['`continue` skips the rest of the current iteration. The empty name is ignored, and the loop '
                       'moves on to the next value.'],
             'code': 'names = ["Ada", "", "Grace"]\n'
                     'for name in names:\n'
                     '    if not name:\n'
                     '        continue\n'
                     '    print(name)',
             'output': 'Ada\nGrace',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`break` exits the loop immediately. The value after `stop` is never processed because the loop '
                       'has already ended.'],
             'code': 'commands = ["load", "save", "stop", "delete"]\n'
                     'for command in commands:\n'
                     '    if command == "stop":\n'
                     '        break\n'
                     '    print(command)',
             'output': 'load\nsave',
             'line': 39,
             'kind': 'cell'}]},
 {'slug': 'loop-else',
  'title': 'Loop Else',
  'section': 'Control Flow',
  'summary': 'A loop else block runs only when the loop did not end with break.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#else-clauses-on-loops',
  'code': 'names = ["Ada", "Grace", "Guido"]\n'
          '\n'
          'for name in names:\n'
          '    if name == "Grace":\n'
          '        print("found")\n'
          '        break\n'
          'else:\n'
          '    print("missing")\n'
          '\n'
          'for name in names:\n'
          '    if name == "Linus":\n'
          '        print("found")\n'
          '        break\n'
          'else:\n'
          '    print("missing")\n',
  'expected_output': 'found\nmissing\n',
  'notes': ['Loop `else` runs when the loop was not ended by `break`.',
            'It is best for search loops with a clear found/not-found split.',
            'It works with both `for` and `while` loops.'],
  'cells': [{'prose': ['If the loop reaches `break`, the `else` block is skipped. This branch means the search '
                       'succeeded early.'],
             'code': 'names = ["Ada", "Grace", "Guido"]\n'
                     '\n'
                     'for name in names:\n'
                     '    if name == "Grace":\n'
                     '        print("found")\n'
                     '        break\n'
                     'else:\n'
                     '    print("missing")',
             'output': 'found',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['If the loop finishes without `break`, the `else` block runs. This branch means the search '
                       'examined every value and found nothing.'],
             'code': 'for name in names:\n'
                     '    if name == "Linus":\n'
                     '        print("found")\n'
                     '        break\n'
                     'else:\n'
                     '    print("missing")',
             'output': 'missing',
             'line': 41,
             'kind': 'cell'}]},
 {'slug': 'iterating-over-iterables',
  'title': 'Iterating over Iterables',
  'section': 'Iteration',
  'summary': 'for loops consume values from any iterable object.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#for-statements',
  'code': 'names = ["Ada", "Grace", "Guido"]\n'
          '\n'
          'for name in names:\n'
          '    print(name)\n'
          '\n'
          'for index, name in enumerate(names):\n'
          '    print(index, name)\n'
          '\n'
          'scores = {"Ada": 10, "Grace": 9}\n'
          'for name, score in scores.items():\n'
          '    print(name, score)\n',
  'expected_output': 'Ada\nGrace\nGuido\n0 Ada\n1 Grace\n2 Guido\nAda 10\nGrace 9\n',
  'notes': ['A `for` loop consumes values from an iterable.',
            'Different producers can feed the same loop protocol.',
            'Prefer `enumerate()` over `range(len(...))` when you need an index.'],
  'cells': [{'prose': ['Start with an ordinary list. A list stores values, and a `for` loop asks it for one value at a '
                       'time.',
                       'When you only need the values, iterate over the collection directly. There is no index '
                       'variable because the loop body does not need one.'],
             'code': 'names = ["Ada", "Grace", "Guido"]\n\nfor name in names:\n    print(name)',
             'output': 'Ada\nGrace\nGuido',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['When you need both a position and a value, use `enumerate()`. It produces index/value pairs '
                       'without manual indexing.'],
             'code': 'for index, name in enumerate(names):\n    print(index, name)',
             'output': '0 Ada\n1 Grace\n2 Guido',
             'line': 36,
             'kind': 'cell'},
            {'prose': ['Dictionaries are iterable too, but `dict.items()` is the clearest way to say that the loop '
                       'needs keys and values together.'],
             'code': 'scores = {"Ada": 10, "Grace": 9}\nfor name, score in scores.items():\n    print(name, score)',
             'output': 'Ada 10\nGrace 9',
             'line': 51,
             'kind': 'cell'}]},
 {'slug': 'iterators',
  'title': 'Iterators',
  'section': 'Iteration',
  'summary': 'iter and next expose the protocol behind for loops.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#iterator-types',
  'code': 'names = ["Ada", "Grace", "Guido"]\n'
          'iterator = iter(names)\n'
          'print(next(iterator))\n'
          'print(next(iterator))\n'
          '\n'
          'for name in iterator:\n'
          '    print(name)\n'
          '\n'
          'again = iter(names)\n'
          'print(next(again))\n',
  'expected_output': 'Ada\nGrace\nGuido\nAda\n',
  'notes': ['Iterables produce iterators; iterators produce values.',
            '`next()` consumes one value from an iterator.',
            'Many iterators are one-pass even when the original collection is reusable.'],
  'cells': [{'prose': ['`iter()` asks an iterable for an iterator. `next()` consumes one value and advances the '
                       "iterator's position."],
             'code': 'names = ["Ada", "Grace", "Guido"]\n'
                     'iterator = iter(names)\n'
                     'print(next(iterator))\n'
                     'print(next(iterator))',
             'output': 'Ada\nGrace',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['A `for` loop consumes the same iterator protocol. Because two values were already consumed, '
                       'the loop sees only the remaining value.'],
             'code': 'for name in iterator:\n    print(name)',
             'output': 'Guido',
             'line': 33,
             'kind': 'cell'},
            {'prose': ['The list itself is reusable. Asking it for a fresh iterator starts a new pass over the same '
                       'stored values.'],
             'code': 'again = iter(names)\nprint(next(again))',
             'output': 'Ada',
             'line': 46,
             'kind': 'cell'}]},
 {'slug': 'sentinel-iteration',
  'title': 'Sentinel Iteration',
  'section': 'Iteration',
  'summary': 'iter(callable, sentinel) repeats calls until a marker value appears.',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#iter',
  'code': 'lines = iter(["alpha", "beta", ""])\n'
          '\n'
          'def read_line():\n'
          '    return next(lines)\n'
          '\n'
          'for line in iter(read_line, ""):\n'
          '    print(line.upper())\n',
  'expected_output': 'ALPHA\nBETA\n',
  'notes': ['A zero-argument callable produces one value at a time.',
            'The sentinel value stops the loop without appearing in the output.',
            'This form is useful for repeated reads from files, sockets, or queues.'],
  'cells': [{'prose': ['A zero-argument callable produces one value at a time.'],
             'code': 'lines = iter(["alpha", "beta", ""])\n'
                     '\n'
                     'def read_line():\n'
                     '    return next(lines)\n'
                     '\n'
                     'for line in iter(read_line, ""):\n'
                     '    print(line.upper())',
             'output': 'ALPHA\nBETA',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'match-statements',
  'title': 'Match Statements',
  'section': 'Control Flow',
  'summary': 'match selects cases using structural pattern matching.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#match-statements',
  'code': 'command = {"action": "move", "x": 3, "y": 4}\n'
          '\n'
          'match command:\n'
          '    case {"action": "move", "x": x, "y": y}:\n'
          '        print(f"move to {x},{y}")\n'
          '    case {"action": "quit"}:\n'
          '        print("quit")\n'
          '    case {"action": action}:\n'
          '        print(f"unknown action: {action}")\n'
          '    case _:\n'
          '        print("invalid command")\n',
  'expected_output': 'move to 3,4\n',
  'notes': ['`match` compares structure, not just equality.',
            'Patterns can bind names such as `x` and `y` while matching.',
            'Put the catch-all `_` case last, because cases are tried from top to bottom.'],
  'cells': [{'prose': ['Use `match` when the shape of a value is the decision. This command is a dictionary with an '
                       'action and coordinates; the first case checks that shape and binds `x` and `y`.'],
             'code': 'command = {"action": "move", "x": 3, "y": 4}\n'
                     '\n'
                     'match command:\n'
                     '    case {"action": "move", "x": x, "y": y}:\n'
                     '        print(f"move to {x},{y}")',
             'output': 'move to 3,4',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Other cases describe other valid shapes. This complete fragment changes the command so the '
                       '`quit` case is the first matching pattern.'],
             'code': 'command = {"action": "quit"}\n'
                     '\n'
                     'match command:\n'
                     '    case {"action": "move", "x": x, "y": y}:\n'
                     '        print(f"move to {x},{y}")\n'
                     '    case {"action": "quit"}:\n'
                     '        print("quit")',
             'output': 'quit',
             'line': 33,
             'kind': 'cell'},
            {'prose': ['Broader patterns and the `_` catch-all belong after specific cases. This fragment extracts an '
                       'unknown action before the final fallback would run.'],
             'code': 'command = {"action": "jump"}\n'
                     '\n'
                     'match command:\n'
                     '    case {"action": "move", "x": x, "y": y}:\n'
                     '        print(f"move to {x},{y}")\n'
                     '    case {"action": "quit"}:\n'
                     '        print("quit")\n'
                     '    case {"action": action}:\n'
                     '        print(f"unknown action: {action}")\n'
                     '    case _:\n'
                     '        print("invalid command")',
             'output': 'unknown action: jump',
             'line': 51,
             'kind': 'cell'}]},
 {'slug': 'advanced-match-patterns',
  'title': 'Advanced Match Patterns',
  'section': 'Control Flow',
  'summary': 'match patterns can destructure sequences, combine alternatives, and add guards.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#match-statements',
  'code': 'def describe(command):\n'
          '    match command:\n'
          '        case ["move", x, y] if x >= 0 and y >= 0:\n'
          '            return f"move to {x},{y}"\n'
          '        case ["quit" | "exit"]:\n'
          '            return "stop"\n'
          '        case ["echo", *words]:\n'
          '            return " ".join(words)\n'
          '        case _:\n'
          '            return "unknown"\n'
          '\n'
          'print(describe(["move", 2, 3]))\n'
          'print(describe(["exit"]))\n'
          'print(describe(["echo", "hello", "python"]))\n'
          'print(describe(["move", -1, 3]))\n',
  'expected_output': 'move to 2,3\nstop\nhello python\nunknown\n',
  'notes': ['Use `case _` as a wildcard fallback.',
            'Guards refine a pattern after the structure matches.',
            'OR patterns and star patterns keep shape-based branches compact.'],
  'cells': [{'prose': ['Sequence patterns match by position. A guard after `if` adds a condition that must also be '
                       'true.'],
             'code': 'def describe(command):\n'
                     '    match command:\n'
                     '        case ["move", x, y] if x >= 0 and y >= 0:\n'
                     '            return f"move to {x},{y}"\n'
                     '        case ["quit" | "exit"]:\n'
                     '            return "stop"\n'
                     '        case ["echo", *words]:\n'
                     '            return " ".join(words)\n'
                     '        case _:\n'
                     '            return "unknown"\n'
                     '\n'
                     'print(describe(["move", 2, 3]))',
             'output': 'move to 2,3',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['An OR pattern accepts several alternatives in one case. A star pattern captures the rest of a '
                       'sequence.'],
             'code': 'print(describe(["exit"]))\nprint(describe(["echo", "hello", "python"]))',
             'output': 'stop\nhello python',
             'line': 45,
             'kind': 'cell'},
            {'prose': ['The wildcard `_` catches values that did not match earlier cases. Here the guard rejects the '
                       'negative coordinate.'],
             'code': 'print(describe(["move", -1, 3]))',
             'output': 'unknown',
             'line': 59,
             'kind': 'cell'}]},
 {'slug': 'while-loops',
  'title': 'While Loops',
  'section': 'Control Flow',
  'summary': 'while repeats until changing state makes a condition false.',
  'doc_url': 'https://docs.python.org/3.13/reference/compound_stmts.html#while',
  'code': 'remaining = 3\n'
          'while remaining > 0:\n'
          '    print(f"launch in {remaining}")\n'
          '    remaining -= 1\n'
          'print("liftoff")\n'
          '\n'
          'responses = iter(["retry", "retry", "ok"])\n'
          'status = next(responses)\n'
          'while status != "ok":\n'
          '    print(f"status: {status}")\n'
          '    status = next(responses)\n'
          'print(f"status: {status}")\n',
  'expected_output': 'launch in 3\nlaunch in 2\nlaunch in 1\nliftoff\nstatus: retry\nstatus: retry\nstatus: ok\n',
  'notes': ['Use `while` when changing state decides whether the loop continues.',
            'Update loop state inside the body so the condition can become false.',
            'Prefer `for` when you already have a collection, range, iterator, or generator to consume.'],
  'cells': [{'prose': ['Use `while` when the condition, not an iterable, controls repetition. Here the loop owns the '
                       'countdown state and updates it each time through the body.'],
             'code': 'remaining = 3\n'
                     'while remaining > 0:\n'
                     '    print(f"launch in {remaining}")\n'
                     '    remaining -= 1\n'
                     'print("liftoff")',
             'output': 'launch in 3\nlaunch in 2\nlaunch in 1\nliftoff',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['A sentinel loop stops when a special value appears. The loop does not know in advance how many '
                       'retries it will need; it keeps going until the state says to stop.'],
             'code': 'responses = iter(["retry", "retry", "ok"])\n'
                     'status = next(responses)\n'
                     'while status != "ok":\n'
                     '    print(f"status: {status}")\n'
                     '    status = next(responses)\n'
                     'print(f"status: {status}")',
             'output': 'status: retry\nstatus: retry\nstatus: ok',
             'line': 36,
             'kind': 'cell'}]},
 {'slug': 'lists',
  'title': 'Lists',
  'section': 'Collections',
  'summary': 'Lists are ordered, mutable collections.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#more-on-lists',
  'code': 'numbers = [3, 1, 4]\n'
          'numbers.append(1)\n'
          '\n'
          'print(numbers)\n'
          'print(numbers[0])\n'
          'print(numbers[-1])\n'
          'print(sorted(numbers))\n'
          'print(numbers)\n',
  'expected_output': '[3, 1, 4, 1]\n3\n1\n[1, 1, 3, 4]\n[3, 1, 4, 1]\n',
  'notes': ['Lists are mutable sequences: methods such as `append()` change the list in place.',
            'Negative indexes count from the end.',
            '`sorted()` returns a new list; `list.sort()` sorts the existing list in place.'],
  'cells': [{'prose': ['Create a list with square brackets. Because lists are mutable, `append()` changes this same '
                       'list object.'],
             'code': 'numbers = [3, 1, 4]\nnumbers.append(1)\n\nprint(numbers)',
             'output': '[3, 1, 4, 1]',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Use indexes to read positions. Negative indexes are convenient for reading from the end.'],
             'code': 'print(numbers[0])\nprint(numbers[-1])',
             'output': '3\n1',
             'line': 32,
             'kind': 'cell'},
            {'prose': ['Use `sorted()` when you want an ordered copy and still need the original order afterward.'],
             'code': 'print(sorted(numbers))\nprint(numbers)',
             'output': '[1, 1, 3, 4]\n[3, 1, 4, 1]',
             'line': 46,
             'kind': 'cell'}]},
 {'slug': 'tuples',
  'title': 'Tuples',
  'section': 'Collections',
  'summary': 'Tuples group a fixed number of positional values.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'code': 'point = (3, 4)\n'
          'x, y = point\n'
          'print(x + y)\n'
          '\n'
          'red = (255, 0, 0)\n'
          'print(red[0])\n'
          'print(len(red))\n'
          '\n'
          'record = ("Ada", 10)\n'
          'name, score = record\n'
          'print(f"{name}: {score}")\n',
  'expected_output': '7\n255\n3\nAda: 10\n',
  'notes': ['Tuples are immutable sequences with fixed length.',
            'Use tuples for small records where position has meaning.',
            'Use lists for variable-length collections of similar items.'],
  'cells': [{'prose': ['Use a tuple for a fixed-size record where each position has a known meaning. Unpacking turns '
                       'those positions into names at the point of use.'],
             'code': 'point = (3, 4)\nx, y = point\nprint(x + y)',
             'output': '7',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Tuples are sequences, so indexing and `len()` work. They are different from lists because '
                       'their length and item references are fixed after creation.'],
             'code': 'red = (255, 0, 0)\nprint(red[0])\nprint(len(red))',
             'output': '255\n3',
             'line': 31,
             'kind': 'cell'},
            {'prose': ['Tuples pair naturally with multiple return values and unpacking. If the fields need names '
                       'everywhere, graduate to a dataclass or named tuple.'],
             'code': 'record = ("Ada", 10)\nname, score = record\nprint(f"{name}: {score}")',
             'output': 'Ada: 10',
             'line': 46,
             'kind': 'cell'}]},
 {'slug': 'unpacking',
  'title': 'Unpacking',
  'section': 'Collections',
  'summary': 'Unpacking binds names from sequences and mappings concisely.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'code': 'point = (3, 4)\n'
          'x, y = point\n'
          'print(x, y)\n'
          '\n'
          'first, *middle, last = [1, 2, 3, 4]\n'
          'print(first, middle, last)\n'
          '\n'
          'def describe(name, language):\n'
          '    print(name, language)\n'
          '\n'
          'data = {"name": "Ada", "language": "Python"}\n'
          'describe(**data)\n',
  'expected_output': '3 4\n1 [2, 3] 4\nAda Python\n',
  'notes': ['Starred unpacking collects the remaining values into a list.',
            'Dictionary unpacking with ** is common when calling functions with structured data.',
            'Prefer indexing when you need one position; prefer unpacking when naming several positions makes the '
            'shape clearer.'],
  'cells': [{'prose': ['Unpacking binds multiple names from one iterable or mapping. It makes the structure of data '
                       'visible at the point where values are introduced.'],
             'code': 'point = (3, 4)\nx, y = point\nprint(x, y)',
             'output': '3 4',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Starred unpacking handles variable-length sequences by collecting the middle or remaining '
                       'values. This keeps common head-tail patterns readable.'],
             'code': 'first, *middle, last = [1, 2, 3, 4]\nprint(first, middle, last)',
             'output': '1 [2, 3] 4',
             'line': 31,
             'kind': 'cell'},
            {'prose': ['Dictionary unpacking with ** connects structured data to function calls. It is widely used in '
                       'configuration, adapters, and code that bridges APIs.',
                       'Dictionary unpacking with ** connects structured data to function calls. It is widely used in '
                       'configuration, adapters, and code that bridges APIs.'],
             'code': 'def describe(name, language):\n'
                     '    print(name, language)\n'
                     '\n'
                     'data = {"name": "Ada", "language": "Python"}\n'
                     'describe(**data)',
             'output': 'Ada Python',
             'line': 44,
             'kind': 'cell'}]},
 {'slug': 'dicts',
  'title': 'Dictionaries',
  'section': 'Collections',
  'summary': 'Dictionaries map keys to values for records, lookup, and structured data.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#dictionaries',
  'code': 'profile = {"name": "Ada", "language": "Python"}\n'
          'profile["year"] = 1843\n'
          'print(profile["name"])\n'
          'print(profile.get("timezone", "UTC"))\n'
          '\n'
          'scores = {"Ada": 10, "Grace": 9}\n'
          'print(scores["Grace"])\n'
          'print(scores.get("Guido", 0))\n'
          '\n'
          'for name, score in scores.items():\n'
          '    print(f"{name}: {score}")\n',
  'expected_output': 'Ada\nUTC\n9\n0\nAda: 10\nGrace: 9\n',
  'notes': ['Dictionaries preserve insertion order in modern Python.',
            'Use `get()` when a missing key has a reasonable default.',
            'Use direct indexing when a missing key should be treated as an error.'],
  'cells': [{'prose': ['Use a dictionary as a small record when fields have names. Direct indexing communicates that '
                       'the key is required, while `get()` communicates that a missing key has a fallback.'],
             'code': 'profile = {"name": "Ada", "language": "Python"}\n'
                     'profile["year"] = 1843\n'
                     'print(profile["name"])\n'
                     'print(profile.get("timezone", "UTC"))',
             'output': 'Ada\nUTC',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Use a dictionary as a lookup table when keys identify values. This is different from a list, '
                       'where numeric position is the lookup key.'],
             'code': 'scores = {"Ada": 10, "Grace": 9}\nprint(scores["Grace"])\nprint(scores.get("Guido", 0))',
             'output': '9\n0',
             'line': 33,
             'kind': 'cell'},
            {'prose': ['Use `items()` when the loop needs both keys and values. It avoids looping over keys and then '
                       'indexing back into the dictionary.'],
             'code': 'for name, score in scores.items():\n    print(f"{name}: {score}")',
             'output': 'Ada: 10\nGrace: 9',
             'line': 48,
             'kind': 'cell'}]},
 {'slug': 'sets',
  'title': 'Sets',
  'section': 'Collections',
  'summary': 'Sets store unique values and make membership checks explicit.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#sets',
  'code': 'languages = ["python", "go", "python"]\n'
          'unique_languages = set(languages)\n'
          'print(sorted(unique_languages))\n'
          '\n'
          'allowed = {"python", "rust"}\n'
          'print("python" in allowed)\n'
          'print("ruby" in allowed)\n'
          '\n'
          'compiled = {"go", "rust"}\n'
          'print(sorted(allowed | compiled))\n'
          'print(sorted(allowed & compiled))\n'
          'print(sorted(allowed - compiled))\n',
  'expected_output': "['go', 'python']\nTrue\nFalse\n['go', 'python', 'rust']\n['rust']\n['python']\n",
  'notes': ['Use lists when order and repeated values matter.',
            'Use sets when uniqueness and membership are the main operations.',
            'Prefer lists when order or repeated values are part of the meaning.',
            'Sets are unordered, so sort them when examples need deterministic display.'],
  'cells': [{'prose': ['Creating a set removes duplicates. Keep a list when order and repeated values matter; convert '
                       'to a set when uniqueness is the point.'],
             'code': 'languages = ["python", "go", "python"]\n'
                     'unique_languages = set(languages)\n'
                     'print(sorted(unique_languages))',
             'output': "['go', 'python']",
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Membership checks are the everyday set operation. A list can also use `in`, but a set says '
                       'that membership is central to the data shape.'],
             'code': 'allowed = {"python", "rust"}\nprint("python" in allowed)\nprint("ruby" in allowed)',
             'output': 'True\nFalse',
             'line': 31,
             'kind': 'cell'},
            {'prose': ['Union, intersection, and difference describe relationships between groups without manual '
                       'loops.'],
             'code': 'compiled = {"go", "rust"}\n'
                     'print(sorted(allowed | compiled))\n'
                     'print(sorted(allowed & compiled))\n'
                     'print(sorted(allowed - compiled))',
             'output': "['go', 'python', 'rust']\n['rust']\n['python']",
             'line': 46,
             'kind': 'cell'}]},
 {'slug': 'slices',
  'title': 'Slices',
  'section': 'Collections',
  'summary': 'Slices copy meaningful ranges from ordered sequences.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/introduction.html#lists',
  'code': 'letters = ["a", "b", "c", "d", "e", "f"]\n'
          'first_page = letters[:3]\n'
          'rest = letters[3:]\n'
          'print(first_page)\n'
          'print(rest)\n'
          '\n'
          'middle = letters[1:5]\n'
          'every_other = letters[::2]\n'
          'reversed_letters = letters[::-1]\n'
          'print(middle)\n'
          'print(every_other)\n'
          'print(reversed_letters)\n'
          'print(letters)\n',
  'expected_output': "['a', 'b', 'c']\n"
                     "['d', 'e', 'f']\n"
                     "['b', 'c', 'd', 'e']\n"
                     "['a', 'c', 'e']\n"
                     "['f', 'e', 'd', 'c', 'b', 'a']\n"
                     "['a', 'b', 'c', 'd', 'e', 'f']\n",
  'notes': ['Slice stop indexes are excluded, so adjacent ranges compose cleanly.',
            'Omitted bounds mean the beginning or end of the sequence.',
            'A negative step walks backward; `[::-1]` is a common reversed-copy idiom.'],
  'cells': [{'prose': ['Omitted bounds mean “from the beginning” or “through the end.” Because the stop index is '
                       'excluded, adjacent slices split a sequence cleanly.'],
             'code': 'letters = ["a", "b", "c", "d", "e", "f"]\n'
                     'first_page = letters[:3]\n'
                     'rest = letters[3:]\n'
                     'print(first_page)\n'
                     'print(rest)',
             'output': "['a', 'b', 'c']\n['d', 'e', 'f']",
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Use `start:stop` for a middle range and `step` when you want to skip or walk backward. These '
                       'operations return new lists; the original list is unchanged.'],
             'code': 'middle = letters[1:5]\n'
                     'every_other = letters[::2]\n'
                     'reversed_letters = letters[::-1]\n'
                     'print(middle)\n'
                     'print(every_other)\n'
                     'print(reversed_letters)\n'
                     'print(letters)',
             'output': "['b', 'c', 'd', 'e']\n"
                       "['a', 'c', 'e']\n"
                       "['f', 'e', 'd', 'c', 'b', 'a']\n"
                       "['a', 'b', 'c', 'd', 'e', 'f']",
             'line': 34,
             'kind': 'cell'}]},
 {'slug': 'comprehensions',
  'title': 'Comprehensions',
  'section': 'Collections',
  'summary': 'Comprehensions build collections by mapping and filtering iterables.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions',
  'code': 'names = ["ada", "guido", "grace"]\n'
          'titled = [name.title() for name in names]\n'
          'print(titled)\n'
          '\n'
          'scores = {"Ada": 10, "Guido": 8, "Grace": 10}\n'
          'high_scores = {name: score for name, score in scores.items() if score >= 10}\n'
          'print(high_scores)\n'
          '\n'
          'unique_scores = {score for score in scores.values()}\n'
          'print(unique_scores)\n',
  'expected_output': "['Ada', 'Guido', 'Grace']\n{'Ada': 10, 'Grace': 10}\n{8, 10}\n",
  'notes': ['The left side says what to produce; the `for` clause says where values come from.',
            'Use an `if` clause for simple filters.',
            'List, dict, and set comprehensions build concrete collections immediately.',
            'Switch to a loop when the transformation needs multiple steps or explanations.'],
  'cells': [{'prose': ['A list comprehension maps each input item to one output item. This one calls `title()` for '
                       'every name and collects the results in a new list.'],
             'code': 'names = ["ada", "guido", "grace"]\ntitled = [name.title() for name in names]\nprint(titled)',
             'output': "['Ada', 'Guido', 'Grace']",
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Add an `if` clause when only some items should appear. A dictionary comprehension can '
                       'transform key/value pairs while preserving the dictionary shape.'],
             'code': 'scores = {"Ada": 10, "Guido": 8, "Grace": 10}\n'
                     'high_scores = {name: score for name, score in scores.items() if score >= 10}\n'
                     'print(high_scores)',
             'output': "{'Ada': 10, 'Grace': 10}",
             'line': 31,
             'kind': 'cell'},
            {'prose': ['A set comprehension keeps only unique results. Here two people have the same score, so the '
                       'resulting set has two values.'],
             'code': 'unique_scores = {score for score in scores.values()}\nprint(unique_scores)',
             'output': '{8, 10}',
             'line': 45,
             'kind': 'cell'}]},
 {'slug': 'comprehension-patterns',
  'title': 'Comprehension Patterns',
  'section': 'Collections',
  'summary': 'Comprehensions can use multiple for clauses and filters when the shape stays clear.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions',
  'code': 'colors = ["red", "blue"]\n'
          'sizes = ["S", "M"]\n'
          'variants = [(color, size) for color in colors for size in sizes]\n'
          'print(variants)\n'
          '\n'
          'numbers = range(10)\n'
          'filtered = [n for n in numbers if n % 2 == 0 if n > 2]\n'
          'print(filtered)\n',
  'expected_output': "[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]\n[4, 6, 8]\n",
  'notes': ['Read comprehension clauses from left to right.',
            'Multiple `for` clauses act like nested loops.',
            'Prefer an explicit loop when the comprehension stops being obvious.'],
  'cells': [{'prose': ['Multiple `for` clauses behave like nested loops. The leftmost `for` is the outer loop, and the '
                       'next `for` runs inside it.'],
             'code': 'colors = ["red", "blue"]\n'
                     'sizes = ["S", "M"]\n'
                     'variants = [(color, size) for color in colors for size in sizes]\n'
                     'print(variants)',
             'output': "[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]",
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Multiple `if` clauses filter values. They are useful for simple conditions, but an explicit '
                       'loop is clearer when the rules need names or explanation.'],
             'code': 'numbers = range(10)\nfiltered = [n for n in numbers if n % 2 == 0 if n > 2]\nprint(filtered)',
             'output': '[4, 6, 8]',
             'line': 37,
             'kind': 'cell'}]},
 {'slug': 'sorting',
  'title': 'Sorting',
  'section': 'Collections',
  'summary': 'sorted returns a new ordered list and key functions choose the sort value.',
  'doc_url': 'https://docs.python.org/3.13/howto/sorting.html',
  'code': 'names = ["Guido", "Ada", "Grace"]\n'
          'print(sorted(names))\n'
          'print(names)\n'
          '\n'
          'users = [\n'
          '    {"name": "Ada", "score": 10},\n'
          '    {"name": "Guido", "score": 8},\n'
          '    {"name": "Grace", "score": 10},\n'
          ']\n'
          'ranked = sorted(users, key=lambda user: user["score"], reverse=True)\n'
          'print([user["name"] for user in ranked])\n'
          '\n'
          'users.sort(key=lambda user: user["name"])\n'
          'print([user["name"] for user in users])\n',
  'expected_output': "['Ada', 'Grace', 'Guido']\n"
                     "['Guido', 'Ada', 'Grace']\n"
                     "['Ada', 'Grace', 'Guido']\n"
                     "['Ada', 'Grace', 'Guido']\n",
  'notes': ['`sorted()` makes a new list; `list.sort()` mutates an existing list.',
            '`key=` should return the value Python compares for each item.',
            "Python's sort is stable, so equal keys keep their original relative order."],
  'cells': [{'prose': ['`sorted()` returns a new list. Printing the original list afterward shows that the input order '
                       'did not change.'],
             'code': 'names = ["Guido", "Ada", "Grace"]\nprint(sorted(names))\nprint(names)',
             'output': "['Ada', 'Grace', 'Guido']\n['Guido', 'Ada', 'Grace']",
             'line': 17,
             'kind': 'cell'},
            {'prose': ['A key function computes the value to compare. Here the records are sorted by score, highest '
                       'first, and the output shows the resulting order.'],
             'code': 'users = [\n'
                     '    {"name": "Ada", "score": 10},\n'
                     '    {"name": "Guido", "score": 8},\n'
                     '    {"name": "Grace", "score": 10},\n'
                     ']\n'
                     'ranked = sorted(users, key=lambda user: user["score"], reverse=True)\n'
                     'print([user["name"] for user in ranked])',
             'output': "['Ada', 'Grace', 'Guido']",
             'line': 32,
             'kind': 'cell'},
            {'prose': ['`list.sort()` sorts the list in place. Use it when mutation is the point and no separate '
                       'sorted copy is needed.'],
             'code': 'users.sort(key=lambda user: user["name"])\nprint([user["name"] for user in users])',
             'output': "['Ada', 'Grace', 'Guido']",
             'line': 50,
             'kind': 'cell'}]},
 {'slug': 'collections-module',
  'title': 'Collections Module',
  'section': 'Collections',
  'summary': 'collections provides specialized containers for common data shapes.',
  'doc_url': 'https://docs.python.org/3.13/library/collections.html',
  'code': 'from collections import Counter, defaultdict, deque, namedtuple\n'
          '\n'
          'counts = Counter("banana")\n'
          'print(counts.most_common(2))\n'
          '\n'
          'groups = defaultdict(list)\n'
          'for name, team in [("Ada", "red"), ("Grace", "blue"), ("Lin", "red")]:\n'
          '    groups[team].append(name)\n'
          'print(dict(groups))\n'
          '\n'
          'queue = deque(["first"])\n'
          'queue.append("second")\n'
          'print(queue.popleft())\n'
          '\n'
          'Point = namedtuple("Point", "x y")\n'
          'print(Point(2, 3).x)\n',
  'expected_output': "[('a', 3), ('n', 2)]\n{'red': ['Ada', 'Lin'], 'blue': ['Grace']}\nfirst\n2\n",
  'notes': ['Use `Counter` when counting is the data shape.',
            'Use `defaultdict` when grouping values by key.',
            'Use `deque` for efficient queue operations and `namedtuple` for lightweight named records.'],
  'cells': [{'prose': ['Use `Counter` when counting is the data shape.'],
             'code': 'from collections import Counter, defaultdict, deque, namedtuple\n'
                     '\n'
                     'counts = Counter("banana")\n'
                     'print(counts.most_common(2))\n'
                     '\n'
                     'groups = defaultdict(list)\n'
                     'for name, team in [("Ada", "red"), ("Grace", "blue"), ("Lin", "red")]:\n'
                     '    groups[team].append(name)\n'
                     'print(dict(groups))\n'
                     '\n'
                     'queue = deque(["first"])\n'
                     'queue.append("second")\n'
                     'print(queue.popleft())\n'
                     '\n'
                     'Point = namedtuple("Point", "x y")\n'
                     'print(Point(2, 3).x)',
             'output': "[('a', 3), ('n', 2)]\n{'red': ['Ada', 'Lin'], 'blue': ['Grace']}\nfirst\n2",
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'copying-collections',
  'title': 'Copying Collections',
  'section': 'Collections',
  'summary': 'Copies can duplicate a container while still sharing nested objects.',
  'doc_url': 'https://docs.python.org/3.13/library/copy.html',
  'code': 'import copy\n'
          '\n'
          'rows = [["Ada"], ["Grace"]]\n'
          'shallow = rows.copy()\n'
          'deep = copy.deepcopy(rows)\n'
          '\n'
          'rows[0].append("Lovelace")\n'
          '\n'
          'print(shallow)\n'
          'print(deep)\n'
          'print(rows[0] is shallow[0])\n'
          'print(rows[0] is deep[0])\n',
  'expected_output': "[['Ada', 'Lovelace'], ['Grace']]\n[['Ada'], ['Grace']]\nTrue\nFalse\n",
  'notes': ['A shallow copy makes a new outer container.',
            'Nested objects are still shared by a shallow copy.',
            'Use `copy.deepcopy()` only when nested independence is required.'],
  'cells': [{'prose': ['A shallow copy makes a new outer container.'],
             'code': 'import copy\n'
                     '\n'
                     'rows = [["Ada"], ["Grace"]]\n'
                     'shallow = rows.copy()\n'
                     'deep = copy.deepcopy(rows)\n'
                     '\n'
                     'rows[0].append("Lovelace")\n'
                     '\n'
                     'print(shallow)\n'
                     'print(deep)\n'
                     'print(rows[0] is shallow[0])\n'
                     'print(rows[0] is deep[0])',
             'output': "[['Ada', 'Lovelace'], ['Grace']]\n[['Ada'], ['Grace']]\nTrue\nFalse",
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'functions',
  'title': 'Functions',
  'section': 'Functions',
  'summary': 'Use def to name reusable behavior and return results.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions',
  'code': 'def greet(name):\n'
          '    return f"Hello, {name}."\n'
          '\n'
          'print(greet("Python"))\n'
          '\n'
          '\n'
          'def format_total(amount, currency="USD"):\n'
          '    return f"{amount} {currency}"\n'
          '\n'
          'print(format_total(10))\n'
          'print(format_total(10, currency="EUR"))\n'
          '\n'
          '\n'
          'def log(message):\n'
          '    print(f"log: {message}")\n'
          '\n'
          'result = log("saved")\n'
          'print(result)\n',
  'expected_output': 'Hello, Python.\n10 USD\n10 EUR\nlog: saved\nNone\n',
  'notes': ['Use `return` for values the caller should receive.',
            'Defaults keep common calls concise.',
            'Keyword arguments make options readable at the call site.'],
  'cells': [{'prose': ['`return` sends a value back to the caller. The caller can print it, store it, or pass it to '
                       'another function.'],
             'code': 'def greet(name):\n    return f"Hello, {name}."\n\nprint(greet("Python"))',
             'output': 'Hello, Python.',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Default arguments provide common values. Keyword arguments make it clear which option is being '
                       'overridden.'],
             'code': 'def format_total(amount, currency="USD"):\n'
                     '    return f"{amount} {currency}"\n'
                     '\n'
                     'print(format_total(10))\n'
                     'print(format_total(10, currency="EUR"))',
             'output': '10 USD\n10 EUR',
             'line': 32,
             'kind': 'cell'},
            {'prose': ['A function without an explicit `return` returns `None`. That makes side-effect-only functions '
                       'easy to distinguish from value-producing ones.'],
             'code': 'def log(message):\n    print(f"log: {message}")\n\nresult = log("saved")\nprint(result)',
             'output': 'log: saved\nNone',
             'line': 49,
             'kind': 'cell'}]},
 {'slug': 'keyword-only-arguments',
  'title': 'Keyword-only Arguments',
  'section': 'Functions',
  'summary': 'Use * to require selected function arguments to be named.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#special-parameters',
  'code': 'def connect(host, *, timeout=5, secure=True):\n'
          '    scheme = "https" if secure else "http"\n'
          '    print(f"{scheme}://{host} timeout={timeout}")\n'
          '\n'
          'connect("example.com")\n'
          'connect("example.com", timeout=10)\n'
          'connect("localhost", secure=False)\n',
  'expected_output': 'https://example.com timeout=5\nhttps://example.com timeout=10\nhttp://localhost timeout=5\n',
  'notes': ['Put `*` before options that callers should name.',
            'Keyword-only flags avoid mysterious positional `True` and `False` arguments.',
            'Defaults work normally for keyword-only parameters.'],
  'cells': [{'prose': ['Parameters after `*` must be named. The default options still apply when the caller omits '
                       'them.'],
             'code': 'def connect(host, *, timeout=5, secure=True):\n'
                     '    scheme = "https" if secure else "http"\n'
                     '    print(f"{scheme}://{host} timeout={timeout}")\n'
                     '\n'
                     'connect("example.com")',
             'output': 'https://example.com timeout=5',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Naming the option makes the call site explicit. A reader does not have to remember which '
                       'positional slot controls the timeout.'],
             'code': 'connect("example.com", timeout=10)',
             'output': 'https://example.com timeout=10',
             'line': 33,
             'kind': 'cell'},
            {'prose': ['Flags are especially good keyword-only arguments because a bare positional `False` is hard to '
                       'interpret.'],
             'code': 'connect("localhost", secure=False)',
             'output': 'http://localhost timeout=5',
             'line': 45,
             'kind': 'cell'}]},
 {'slug': 'positional-only-parameters',
  'title': 'Positional-only Parameters',
  'section': 'Functions',
  'summary': 'Use / to mark parameters that callers must pass by position.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#special-parameters',
  'code': 'def scale(value, /, factor=2, *, clamp=False):\n'
          '    result = value * factor\n'
          '    if clamp:\n'
          '        result = min(result, 10)\n'
          '    return result\n'
          '\n'
          'print(scale(4))\n'
          'print(scale(4, factor=3))\n'
          'print(scale(4, clamp=True))\n',
  'expected_output': '8\n12\n8\n',
  'notes': ['`/` marks parameters before it as positional-only.',
            '`*` marks parameters after it as keyword-only.',
            'Use these markers when the call shape is part of the API design.'],
  'cells': [{'prose': ['Parameters before `/` are positional-only. `value` is the main input, while `factor` remains '
                       'an ordinary parameter that can be named.'],
             'code': 'def scale(value, /, factor=2, *, clamp=False):\n'
                     '    result = value * factor\n'
                     '    if clamp:\n'
                     '        result = min(result, 10)\n'
                     '    return result\n'
                     '\n'
                     'print(scale(4))\n'
                     'print(scale(4, factor=3))',
             'output': '8\n12',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Parameters after `*` are keyword-only. That makes options such as `clamp` explicit at the call '
                       'site.'],
             'code': 'print(scale(4, clamp=True))',
             'output': '8',
             'line': 42,
             'kind': 'cell'}]},
 {'slug': 'args-and-kwargs',
  'title': 'Args and Kwargs',
  'section': 'Functions',
  'summary': '*args collects extra positional arguments and **kwargs collects named ones.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists',
  'code': 'def total(*numbers):\n'
          '    return sum(numbers)\n'
          '\n'
          'print(total(2, 3, 5))\n'
          '\n'
          '\n'
          'def describe(**metadata):\n'
          '    print(metadata)\n'
          '\n'
          'describe(owner="Ada", public=True)\n'
          '\n'
          '\n'
          'def report(title, *items, **metadata):\n'
          '    print(title)\n'
          '    print(items)\n'
          '    print(metadata)\n'
          '\n'
          'report("scores", 10, 9, owner="Ada")\n',
  'expected_output': "10\n{'owner': 'Ada', 'public': True}\nscores\n(10, 9)\n{'owner': 'Ada'}\n",
  'notes': ['Use these tools when a function naturally accepts a flexible shape.',
            'Prefer explicit parameters when the accepted arguments are known and fixed.',
            '`*args` is a tuple; `**kwargs` is a dictionary.'],
  'cells': [{'prose': ['`*args` collects extra positional arguments into a tuple. This fits functions that naturally '
                       'accept any number of similar values.'],
             'code': 'def total(*numbers):\n    return sum(numbers)\n\nprint(total(2, 3, 5))',
             'output': '10',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['`**kwargs` collects named arguments into a dictionary. The names become string keys.'],
             'code': 'def describe(**metadata):\n    print(metadata)\n\ndescribe(owner="Ada", public=True)',
             'output': "{'owner': 'Ada', 'public': True}",
             'line': 32,
             'kind': 'cell'},
            {'prose': ['A function can combine explicit parameters, `*args`, and `**kwargs`. Put the flexible parts '
                       'last so the fixed shape remains visible.'],
             'code': 'def report(title, *items, **metadata):\n'
                     '    print(title)\n'
                     '    print(items)\n'
                     '    print(metadata)\n'
                     '\n'
                     'report("scores", 10, 9, owner="Ada")',
             'output': "scores\n(10, 9)\n{'owner': 'Ada'}",
             'line': 47,
             'kind': 'cell'}]},
 {'slug': 'multiple-return-values',
  'title': 'Multiple Return Values',
  'section': 'Functions',
  'summary': 'Python returns multiple values by returning a tuple and unpacking it.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'code': 'def divide_with_remainder(total, size):\n'
          '    quotient = total // size\n'
          '    remainder = total % size\n'
          '    return quotient, remainder\n'
          '\n'
          'result = divide_with_remainder(17, 5)\n'
          'print(result)\n'
          '\n'
          'boxes, leftover = result\n'
          'print(boxes)\n'
          'print(leftover)\n',
  'expected_output': '(3, 2)\n3\n2\n',
  'notes': ['A comma creates a tuple; `return a, b` returns one tuple containing two values.',
            'Unpacking at the call site gives each returned position a meaningful name.',
            'Use a class-like record when the result has many fields.'],
  'cells': [{'prose': ['Returning values separated by commas returns one tuple. The tuple is visible if the caller '
                       'stores the result directly.'],
             'code': 'def divide_with_remainder(total, size):\n'
                     '    quotient = total // size\n'
                     '    remainder = total % size\n'
                     '    return quotient, remainder\n'
                     '\n'
                     'result = divide_with_remainder(17, 5)\n'
                     'print(result)',
             'output': '(3, 2)',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Callers usually unpack the tuple immediately or soon after. The names at the call site '
                       'document what each position means.'],
             'code': 'boxes, leftover = result\nprint(boxes)\nprint(leftover)',
             'output': '3\n2',
             'line': 35,
             'kind': 'cell'}]},
 {'slug': 'closures',
  'title': 'Closures',
  'section': 'Functions',
  'summary': 'Inner functions can remember values from an enclosing scope.',
  'doc_url': 'https://docs.python.org/3.13/reference/executionmodel.html#binding-of-names',
  'code': 'def make_multiplier(factor):\n'
          '    def multiply(value):\n'
          '        return value * factor\n'
          '    return multiply\n'
          '\n'
          'double = make_multiplier(2)\n'
          'print(double(5))\n'
          '\n'
          'triple = make_multiplier(3)\n'
          'print(triple(5))\n',
  'expected_output': '10\n15\n',
  'notes': ['A closure keeps access to names from the scope where the inner function was created.',
            'Each call to the outer function can create a separate remembered environment.',
            'Closures are useful for callbacks, small factories, and decorators.'],
  'cells': [{'prose': ['Define a function inside another function when the inner behavior needs to remember setup from '
                       'the outer call. The returned function keeps access to `factor`.'],
             'code': 'def make_multiplier(factor):\n'
                     '    def multiply(value):\n'
                     '        return value * factor\n'
                     '    return multiply\n'
                     '\n'
                     'double = make_multiplier(2)\n'
                     'print(double(5))',
             'output': '10',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Calling the outer function again creates a separate closure. `triple` uses the same inner '
                       'code, but remembers a different `factor`.'],
             'code': 'triple = make_multiplier(3)\nprint(triple(5))',
             'output': '15',
             'line': 35,
             'kind': 'cell'}]},
 {'slug': 'partial-functions',
  'title': 'Partial Functions',
  'section': 'Functions',
  'summary': 'functools.partial pre-fills arguments to make a more specific callable.',
  'doc_url': 'https://docs.python.org/3.13/library/functools.html#functools.partial',
  'code': 'from functools import partial\n'
          '\n'
          '\n'
          'def apply_tax(rate, amount):\n'
          '    return round(amount * (1 + rate), 2)\n'
          '\n'
          'vat = partial(apply_tax, 0.2)\n'
          'service_tax = partial(apply_tax, rate=0.1)\n'
          '\n'
          'print(vat(50))\n'
          'print(service_tax(amount=80))\n'
          'print(vat.func.__name__)\n',
  'expected_output': '60.0\n88.0\napply_tax\n',
  'notes': ['A partial object remembers some arguments.',
            'The resulting callable can be passed where an ordinary function is expected.',
            'Prefer a named function when the pre-filled behavior needs richer logic.'],
  'cells': [{'prose': ['A partial object remembers some arguments.'],
             'code': 'from functools import partial\n'
                     '\n'
                     '\n'
                     'def apply_tax(rate, amount):\n'
                     '    return round(amount * (1 + rate), 2)\n'
                     '\n'
                     'vat = partial(apply_tax, 0.2)\n'
                     'service_tax = partial(apply_tax, rate=0.1)\n'
                     '\n'
                     'print(vat(50))\n'
                     'print(service_tax(amount=80))\n'
                     'print(vat.func.__name__)',
             'output': '60.0\n88.0\napply_tax',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'scope-global-nonlocal',
  'title': 'Global and Nonlocal',
  'section': 'Functions',
  'summary': 'global and nonlocal choose which outer binding assignment should update.',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-global-statement',
  'code': 'count = 0\n'
          '\n'
          'def bump_global():\n'
          '    global count\n'
          '    count += 1\n'
          '\n'
          'bump_global()\n'
          'print(count)\n'
          '\n'
          '\n'
          'def make_counter():\n'
          '    total = 0\n'
          '    def bump():\n'
          '        nonlocal total\n'
          '        total += 1\n'
          '        return total\n'
          '    return bump\n'
          '\n'
          'counter = make_counter()\n'
          'print(counter())\n'
          'print(counter())\n',
  'expected_output': '1\n1\n2\n',
  'notes': ['Assignment inside a function is local unless declared otherwise.',
            'Prefer `nonlocal` for closure state and avoid `global` unless module state is truly intended.',
            'Passing values and returning results is usually easier to test than rebinding outer names.'],
  'cells': [{'prose': ['`global` tells assignment to update a module-level binding. Without it, `count += 1` would try '
                       'to assign a local `count`.'],
             'code': 'count = 0\n\ndef bump_global():\n    global count\n    count += 1\n\nbump_global()\nprint(count)',
             'output': '1',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`nonlocal` tells assignment to update a binding in the nearest enclosing function scope. This '
                       'is useful for small closures that keep state.'],
             'code': 'def make_counter():\n'
                     '    total = 0\n'
                     '    def bump():\n'
                     '        nonlocal total\n'
                     '        total += 1\n'
                     '        return total\n'
                     '    return bump\n'
                     '\n'
                     'counter = make_counter()\n'
                     'print(counter())\n'
                     'print(counter())',
             'output': '1\n2',
             'line': 41,
             'kind': 'cell'}]},
 {'slug': 'recursion',
  'title': 'Recursion',
  'section': 'Functions',
  'summary': 'Recursive functions solve nested problems by calling themselves on smaller pieces.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions',
  'code': 'tree = {\n'
          '    "value": 1,\n'
          '    "children": [\n'
          '        {"value": 2, "children": []},\n'
          '        {"value": 3, "children": [{"value": 4, "children": []}]},\n'
          '    ],\n'
          '}\n'
          '\n'
          'def total(node):\n'
          '    subtotal = node["value"]\n'
          '    for child in node["children"]:\n'
          '        subtotal += total(child)\n'
          '    return subtotal\n'
          '\n'
          'print(total({"value": 2, "children": []}))\n'
          'print(total(tree))\n',
  'expected_output': '2\n10\n',
  'notes': ['Every recursive function needs a base case that stops the calls.',
            'Recursion fits nested data better than flat repetition.',
            'Python limits recursion depth, so loops are often better for very deep or simple repetition.'],
  'cells': [{'prose': ['A leaf node is the base case. It has no children, so the function can return its own value '
                       'without making another recursive call.'],
             'code': 'def total(node):\n'
                     '    subtotal = node["value"]\n'
                     '    for child in node["children"]:\n'
                     '        subtotal += total(child)\n'
                     '    return subtotal\n'
                     '\n'
                     'print(total({"value": 2, "children": []}))',
             'output': '2',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['A non-leaf node solves the same problem for each child, then combines those smaller totals '
                       'with its own value.'],
             'code': 'tree = {\n'
                     '    "value": 1,\n'
                     '    "children": [\n'
                     '        {"value": 2, "children": []},\n'
                     '        {"value": 3, "children": [{"value": 4, "children": []}]},\n'
                     '    ],\n'
                     '}\n'
                     '\n'
                     'print(total(tree))',
             'output': '10',
             'line': 35,
             'kind': 'cell'}]},
 {'slug': 'lambdas',
  'title': 'Lambdas',
  'section': 'Functions',
  'summary': 'lambda creates small anonymous function expressions.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#lambda-expressions',
  'code': 'add_tax = lambda price: round(price * 1.08, 2)\n'
          'print(add_tax(10))\n'
          '\n'
          'items = [("notebook", 5), ("pen", 2), ("bag", 20)]\n'
          'by_price = sorted(items, key=lambda item: item[1])\n'
          'print(by_price)\n'
          '\n'
          'def price(item):\n'
          '    return item[1]\n'
          '\n'
          'print(sorted(items, key=price))\n',
  'expected_output': "10.8\n[('pen', 2), ('notebook', 5), ('bag', 20)]\n[('pen', 2), ('notebook', 5), ('bag', 20)]\n",
  'notes': ['Lambdas are expressions, not statements.',
            'Prefer `def` for multi-step or reused behavior.',
            'Lambdas are common as `key=` functions because the behavior is local to one call.'],
  'cells': [{'prose': ['A lambda is a function expression. Assigning one to a name works, although `def` is usually '
                       'clearer for reusable behavior.'],
             'code': 'add_tax = lambda price: round(price * 1.08, 2)\nprint(add_tax(10))',
             'output': '10.8',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Lambdas are most idiomatic when passed directly to another function. `sorted()` calls this key '
                       'function once for each item.'],
             'code': 'items = [("notebook", 5), ("pen", 2), ("bag", 20)]\n'
                     'by_price = sorted(items, key=lambda item: item[1])\n'
                     'print(by_price)',
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]",
             'line': 30,
             'kind': 'cell'},
            {'prose': ['A named function is better when the behavior should be reused or explained. It produces the '
                       'same sort key, but gives the operation a name.'],
             'code': 'def price(item):\n    return item[1]\n\nprint(sorted(items, key=price))',
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]",
             'line': 44,
             'kind': 'cell'}]},
 {'slug': 'generators',
  'title': 'Generators',
  'section': 'Iteration',
  'summary': 'yield creates an iterator that produces values on demand.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#generators',
  'code': 'def countdown(n):\n'
          '    while n > 0:\n'
          '        yield n\n'
          '        n -= 1\n'
          '\n'
          'numbers = countdown(3)\n'
          'print(next(numbers))\n'
          'print(next(numbers))\n'
          '\n'
          'for value in countdown(3):\n'
          '    print(value)\n',
  'expected_output': '3\n2\n3\n2\n1\n',
  'notes': ['Generator functions are a concise way to create custom iterators.',
            'Values are produced on demand.',
            'A generator is consumed as you iterate over it.',
            'Prefer a list when you need to reuse stored results; prefer a generator when values can be streamed '
            'once.'],
  'cells': [{'prose': ['Calling a generator function returns an iterator. `next()` asks for one value and resumes the '
                       'function until the next `yield`.'],
             'code': 'def countdown(n):\n'
                     '    while n > 0:\n'
                     '        yield n\n'
                     '        n -= 1\n'
                     '\n'
                     'numbers = countdown(3)\n'
                     'print(next(numbers))\n'
                     'print(next(numbers))',
             'output': '3\n2',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['A `for` loop repeatedly calls `next()` for you. The loop stops when the generator is '
                       'exhausted.'],
             'code': 'for value in countdown(3):\n    print(value)',
             'output': '3\n2\n1',
             'line': 37,
             'kind': 'cell'}]},
 {'slug': 'yield-from',
  'title': 'Yield From',
  'section': 'Iteration',
  'summary': 'yield from delegates part of a generator to another iterable.',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#yield-expressions',
  'code': 'def page():\n'
          '    yield "header"\n'
          '    yield from ["intro", "body"]\n'
          '    yield "footer"\n'
          '\n'
          'print(list(page()))\n'
          '\n'
          '\n'
          'def flatten(rows):\n'
          '    for row in rows:\n'
          '        yield from row\n'
          '\n'
          'print(list(flatten([[1, 2], [3]])))\n',
  'expected_output': "['header', 'intro', 'body', 'footer']\n[1, 2, 3]\n",
  'notes': ['`yield from iterable` yields each value from that iterable.',
            'It keeps generator pipelines compact.',
            'Use a plain `yield` when producing one value directly.'],
  'cells': [{'prose': ['`yield from` delegates to another iterable. The caller receives one stream even though part of '
                       'it came from a list.'],
             'code': 'def page():\n'
                     '    yield "header"\n'
                     '    yield from ["intro", "body"]\n'
                     '    yield "footer"\n'
                     '\n'
                     'print(list(page()))',
             'output': "['header', 'intro', 'body', 'footer']",
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Delegation is useful when flattening nested iterables. `yield from row` replaces an inner loop '
                       'that would yield each item by hand.'],
             'code': 'def flatten(rows):\n'
                     '    for row in rows:\n'
                     '        yield from row\n'
                     '\n'
                     'print(list(flatten([[1, 2], [3]])))',
             'output': '[1, 2, 3]',
             'line': 39,
             'kind': 'cell'}]},
 {'slug': 'generator-expressions',
  'title': 'Generator Expressions',
  'section': 'Iteration',
  'summary': 'Generator expressions use comprehension-like syntax to stream values lazily.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#generator-expressions',
  'code': 'numbers = [1, 2, 3, 4]\n'
          'list_squares = [number * number for number in numbers]\n'
          'print(list_squares)\n'
          '\n'
          'stream_squares = (number * number for number in numbers)\n'
          'print(next(stream_squares))\n'
          'print(next(stream_squares))\n'
          'print(list(stream_squares))\n'
          '\n'
          'print(sum(number * number for number in numbers))\n',
  'expected_output': '[1, 4, 9, 16]\n1\n4\n[9, 16]\n30\n',
  'notes': ['List, dict, and set comprehensions build concrete collections.',
            'Generator expressions produce one-pass iterators.',
            'Use generator expressions when the consumer can process values one at a time.'],
  'cells': [{'prose': ['A list comprehension is eager: it builds a list immediately. That is useful when you need to '
                       'store or reuse the results.'],
             'code': 'numbers = [1, 2, 3, 4]\n'
                     'list_squares = [number * number for number in numbers]\n'
                     'print(list_squares)',
             'output': '[1, 4, 9, 16]',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['A generator expression is lazy: it creates an iterator that produces values as they are '
                       'consumed. After two `next()` calls, only the remaining squares are left.'],
             'code': 'stream_squares = (number * number for number in numbers)\n'
                     'print(next(stream_squares))\n'
                     'print(next(stream_squares))\n'
                     'print(list(stream_squares))',
             'output': '1\n4\n[9, 16]',
             'line': 31,
             'kind': 'cell'},
            {'prose': ['Generator expressions are common inside reducing functions. When a generator expression is the '
                       'only argument, the extra parentheses can be omitted.'],
             'code': 'print(sum(number * number for number in numbers))',
             'output': '30',
             'line': 48,
             'kind': 'cell'}]},
 {'slug': 'itertools',
  'title': 'Itertools',
  'section': 'Iteration',
  'summary': 'itertools composes lazy iterator streams.',
  'doc_url': 'https://docs.python.org/3.13/library/itertools.html',
  'code': 'import itertools\n'
          '\n'
          'counter = itertools.count(10)\n'
          'print(list(itertools.islice(counter, 3)))\n'
          '\n'
          'pages = itertools.chain(["intro", "setup"], ["deploy"])\n'
          'print(list(pages))\n'
          '\n'
          'scores = [7, 10, 8, 10]\n'
          'high_scores = itertools.compress(scores, [score >= 9 for score in scores])\n'
          'print(list(high_scores))\n',
  'expected_output': "[10, 11, 12]\n['intro', 'setup', 'deploy']\n[10, 10]\n",
  'notes': ['`itertools` composes producer and transformer streams.',
            'Iterator pipelines avoid building intermediate lists.',
            'Use `islice()` to take a finite piece from an infinite iterator.',
            'Convert to a list only when you need concrete results.'],
  'cells': [{'prose': ['`count()` can produce values forever, so `islice()` takes a finite window. Nothing is '
                       'materialized until `list()` consumes the iterator.'],
             'code': 'import itertools\n\ncounter = itertools.count(10)\nprint(list(itertools.islice(counter, 3)))',
             'output': '[10, 11, 12]',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['`chain()` presents several iterables as one stream. This avoids building an intermediate list '
                       'just to loop over combined inputs.'],
             'code': 'pages = itertools.chain(["intro", "setup"], ["deploy"])\nprint(list(pages))',
             'output': "['intro', 'setup', 'deploy']",
             'line': 32,
             'kind': 'cell'},
            {'prose': ['Iterator helpers compose with ordinary Python expressions. `compress()` keeps items whose '
                       'corresponding selector is true.'],
             'code': 'scores = [7, 10, 8, 10]\n'
                     'high_scores = itertools.compress(scores, [score >= 9 for score in scores])\n'
                     'print(list(high_scores))',
             'output': '[10, 10]',
             'line': 45,
             'kind': 'cell'}]},
 {'slug': 'decorators',
  'title': 'Decorators',
  'section': 'Functions',
  'summary': 'Decorators wrap or register functions using @ syntax.',
  'doc_url': 'https://docs.python.org/3.13/glossary.html#term-decorator',
  'code': 'from functools import wraps\n'
          '\n'
          '\n'
          'def loud(func):\n'
          '    @wraps(func)\n'
          '    def wrapper(name):\n'
          '        return func(name).upper()\n'
          '    return wrapper\n'
          '\n'
          '\n'
          'def greet(name):\n'
          '    return f"hello {name}"\n'
          '\n'
          'manual_greet = loud(greet)\n'
          'print(manual_greet("python"))\n'
          '\n'
          '@loud\n'
          'def welcome(name):\n'
          '    """Return a welcome message."""\n'
          '    return f"welcome {name}"\n'
          '\n'
          'print(welcome("workers"))\n'
          'print(welcome.__name__)\n',
  'expected_output': 'HELLO PYTHON\nWELCOME WORKERS\nwelcome\n',
  'notes': ['`@decorator` is shorthand for assigning `func = decorator(func)`.',
            'Decorators can wrap, replace, or register functions.',
            'Use `functools.wraps` in production wrappers that should preserve metadata.'],
  'cells': [{'prose': ['A decorator is just a function that takes a function and returns another callable. Applying it '
                       'manually shows the wrapping step.'],
             'code': 'from functools import wraps\n'
                     '\n'
                     '\n'
                     'def loud(func):\n'
                     '    @wraps(func)\n'
                     '    def wrapper(name):\n'
                     '        return func(name).upper()\n'
                     '    return wrapper\n'
                     '\n'
                     '\n'
                     'def greet(name):\n'
                     '    return f"hello {name}"\n'
                     '\n'
                     'manual_greet = loud(greet)\n'
                     'print(manual_greet("python"))',
             'output': 'HELLO PYTHON',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['The `@loud` syntax performs the same rebinding at definition time. After decoration, `welcome` '
                       'refers to the wrapper returned by `loud`.'],
             'code': '@loud\n'
                     'def welcome(name):\n'
                     '    """Return a welcome message."""\n'
                     '    return f"welcome {name}"\n'
                     '\n'
                     'print(welcome("workers"))',
             'output': 'WELCOME WORKERS',
             'line': 48,
             'kind': 'cell'},
            {'prose': ['`functools.wraps` copies useful metadata from the original function onto the wrapper.'],
             'code': 'print(welcome.__name__)\nprint(welcome.__doc__)',
             'output': 'welcome\nReturn a welcome message.',
             'line': 65,
             'kind': 'cell'}]},
 {'slug': 'classes',
  'title': 'Classes',
  'section': 'Classes',
  'summary': 'Classes bundle data and behavior into new object types.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html',
  'code': 'class Counter:\n'
          '    def __init__(self, start=0):\n'
          '        self.value = start\n'
          '\n'
          '    def increment(self, amount=1):\n'
          '        self.value += amount\n'
          '        return self.value\n'
          '\n'
          'first = Counter()\n'
          'second = Counter(10)\n'
          '\n'
          'print(first.value)\n'
          'print(second.value)\n'
          'print(first.increment())\n'
          'print(second.increment(5))\n',
  'expected_output': '0\n10\n1\n15\n',
  'notes': ['`self` is the instance the method is operating on.',
            '`__init__` initializes each new object.',
            'Use classes when behavior belongs with state; use dictionaries for looser structured data.',
            'Instance attributes belong to one object, not to the class as a whole.'],
  'cells': [{'prose': ['Define a class when data and behavior should travel together. The initializer gives each '
                       'object its starting state.'],
             'code': 'class Counter:\n'
                     '    def __init__(self, start=0):\n'
                     '        self.value = start\n'
                     '\n'
                     'first = Counter()\n'
                     'second = Counter(10)\n'
                     'print(first.value)\n'
                     'print(second.value)',
             'output': '0\n10',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Methods are functions attached to the class. `self` is the particular object receiving the '
                       'method call, so separate instances keep separate state.'],
             'code': 'class Counter:\n'
                     '    def __init__(self, start=0):\n'
                     '        self.value = start\n'
                     '\n'
                     '    def increment(self, amount=1):\n'
                     '        self.value += amount\n'
                     '        return self.value\n'
                     '\n'
                     'first = Counter()\n'
                     'second = Counter(10)\n'
                     'print(first.increment())\n'
                     'print(second.increment(5))',
             'output': '1\n15',
             'line': 37,
             'kind': 'cell'}]},
 {'slug': 'inheritance-and-super',
  'title': 'Inheritance and Super',
  'section': 'Classes',
  'summary': 'Inheritance reuses behavior, and super delegates to a parent implementation.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#inheritance',
  'code': 'class Animal:\n'
          '    def __init__(self, name):\n'
          '        self.name = name\n'
          '\n'
          '    def speak(self):\n'
          '        return f"{self.name} makes a sound"\n'
          '\n'
          'class Dog(Animal):\n'
          '    def speak(self):\n'
          '        base = super().speak()\n'
          '        return f"{base}; {self.name} barks"\n'
          '\n'
          'pet = Dog("Nina")\n'
          'print(pet.name)\n'
          'print(pet.speak())\n'
          'print(isinstance(pet, Animal))\n',
  'expected_output': 'Nina\nNina makes a sound; Nina barks\nTrue\n',
  'notes': ['Inheritance models an “is a specialized kind of” relationship.',
            '`super()` calls the next implementation in the method resolution order.',
            'Prefer composition when an object only needs to use another object.'],
  'cells': [{'prose': ['A child class names its parent in parentheses. `Dog` instances get the `Animal.__init__` '
                       'method because `Dog` does not define its own initializer.'],
             'code': 'class Animal:\n'
                     '    def __init__(self, name):\n'
                     '        self.name = name\n'
                     '\n'
                     '    def speak(self):\n'
                     '        return f"{self.name} makes a sound"\n'
                     '\n'
                     'class Dog(Animal):\n'
                     '    def speak(self):\n'
                     '        base = super().speak()\n'
                     '        return f"{base}; {self.name} barks"\n'
                     '\n'
                     'pet = Dog("Nina")\n'
                     'print(pet.name)',
             'output': 'Nina',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`super()` delegates to the parent implementation. The child method can reuse the parent result '
                       'and then add specialized behavior.'],
             'code': 'print(pet.speak())\nprint(isinstance(pet, Animal))',
             'output': 'Nina makes a sound; Nina barks\nTrue',
             'line': 47,
             'kind': 'cell'}]},
 {'slug': 'dataclasses',
  'title': 'Dataclasses',
  'section': 'Classes',
  'summary': 'dataclass generates common class methods for data containers.',
  'doc_url': 'https://docs.python.org/3.13/library/dataclasses.html',
  'code': 'from dataclasses import dataclass\n'
          '\n'
          '@dataclass\n'
          'class User:\n'
          '    name: str\n'
          '    active: bool = True\n'
          '\n'
          'user = User("Ada")\n'
          'print(user)\n'
          'print(user.name)\n'
          '\n'
          'inactive = User("Guido", active=False)\n'
          'print(inactive)\n'
          'print(inactive.active)\n',
  'expected_output': "User(name='Ada', active=True)\nAda\nUser(name='Guido', active=False)\nFalse\n",
  'notes': ['Type annotations define dataclass fields.',
            'Dataclasses generate methods but remain normal Python classes.',
            'Use `field()` for advanced defaults such as per-instance lists or dictionaries.'],
  'cells': [{'prose': ['A dataclass uses annotations to define fields. Python generates an initializer, so the class '
                       'can be constructed without writing `__init__` by hand.'],
             'code': 'from dataclasses import dataclass\n'
                     '\n'
                     '@dataclass\n'
                     'class User:\n'
                     '    name: str\n'
                     '    active: bool = True\n'
                     '\n'
                     'user = User("Ada")\n'
                     'print(user)',
             'output': "User(name='Ada', active=True)",
             'line': 17,
             'kind': 'cell'},
            {'prose': ['The generated instance still exposes ordinary attributes. A dataclass is a regular class with '
                       'useful methods filled in.'],
             'code': 'print(user.name)',
             'output': 'Ada',
             'line': 37,
             'kind': 'cell'},
            {'prose': ['Defaults can be overridden by keyword. The generated representation includes the field names, '
                       'which is useful during debugging.'],
             'code': 'inactive = User("Guido", active=False)\nprint(inactive)\nprint(inactive.active)',
             'output': "User(name='Guido', active=False)\nFalse",
             'line': 49,
             'kind': 'cell'}]},
 {'slug': 'properties',
  'title': 'Properties',
  'section': 'Classes',
  'summary': '@property keeps attribute syntax while adding computation or validation.',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#property',
  'code': 'class Rectangle:\n'
          '    def __init__(self, width, height):\n'
          '        self.width = width\n'
          '        self.height = height\n'
          '\n'
          '    @property\n'
          '    def area(self):\n'
          '        return self.width * self.height\n'
          '\n'
          '    @property\n'
          '    def width(self):\n'
          '        return self._width\n'
          '\n'
          '    @width.setter\n'
          '    def width(self, value):\n'
          '        if value <= 0:\n'
          '            raise ValueError("width must be positive")\n'
          '        self._width = value\n'
          '\n'
          'box = Rectangle(3, 4)\n'
          'print(box.area)\n'
          '\n'
          'box.width = 5\n'
          'print(box.area)\n'
          '\n'
          'try:\n'
          '    box.width = 0\n'
          'except ValueError as error:\n'
          '    print(error)\n',
  'expected_output': '12\n20\nwidth must be positive\n',
  'notes': ['Properties let APIs start simple and grow validation or computation later.',
            'Callers access a property like an attribute, not like a method.',
            'Use methods instead when work is expensive or action-like.'],
  'cells': [{'prose': ['A read-only property exposes computed data through attribute access. `area` stays current '
                       'because it is calculated from `width` and `height` each time it is read.'],
             'code': 'class Rectangle:\n'
                     '    def __init__(self, width, height):\n'
                     '        self.width = width\n'
                     '        self.height = height\n'
                     '\n'
                     '    @property\n'
                     '    def area(self):\n'
                     '        return self.width * self.height\n'
                     '\n'
                     '    @property\n'
                     '    def width(self):\n'
                     '        return self._width\n'
                     '\n'
                     '    @width.setter\n'
                     '    def width(self, value):\n'
                     '        if value <= 0:\n'
                     '            raise ValueError("width must be positive")\n'
                     '        self._width = value\n'
                     '\n'
                     'box = Rectangle(3, 4)\n'
                     'print(box.area)',
             'output': '12',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['A setter lets assignment keep normal attribute syntax while the class validates or normalizes '
                       'the value.'],
             'code': 'box.width = 5\nprint(box.area)',
             'output': '20',
             'line': 49,
             'kind': 'cell'},
            {'prose': ['Validation belongs inside the class when every caller should obey the same rule. Invalid '
                       'assignment raises an exception at the boundary.'],
             'code': 'try:\n    box.width = 0\nexcept ValueError as error:\n    print(error)',
             'output': 'width must be positive',
             'line': 62,
             'kind': 'cell'}]},
 {'slug': 'special-methods',
  'title': 'Special Methods',
  'section': 'Data Model',
  'summary': 'Special methods connect your objects to Python syntax and built-ins.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#special-method-names',
  'code': 'class Bag:\n'
          '    def __init__(self, items):\n'
          '        self.items = list(items)\n'
          '\n'
          '    def __len__(self):\n'
          '        return len(self.items)\n'
          '\n'
          '    def __iter__(self):\n'
          '        return iter(self.items)\n'
          '\n'
          '    def __repr__(self):\n'
          '        return f"Bag({self.items!r})"\n'
          '\n'
          'bag = Bag(["a", "b"])\n'
          'print(len(bag))\n'
          'print(list(bag))\n'
          'print(bag)\n',
  'expected_output': "2\n['a', 'b']\nBag(['a', 'b'])\n",
  'notes': ["Dunder methods are looked up by Python's data model protocols.",
            'Implement the smallest protocol that makes your object feel native.'],
  'cells': [{'prose': ['Start with a normal class that stores its data. Special methods build on ordinary instance '
                       'state.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(bag.items)',
             'output': "['a', 'b']",
             'line': 17,
             'kind': 'cell'},
            {'prose': ["Implement `__len__` to let `len()` ask the object for its size using Python's standard "
                       'protocol.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(len(bag))',
             'output': '2',
             'line': 34,
             'kind': 'cell'},
            {'prose': ['Implement `__iter__` to make the object iterable. Then tools such as `list()` can consume it '
                       'without a custom method name.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.items)\n'
                     '\n'
                     '    def __iter__(self):\n'
                     '        return iter(self.items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(list(bag))',
             'output': "['a', 'b']",
             'line': 54,
             'kind': 'cell'},
            {'prose': ['Implement `__repr__` to give the object a useful developer-facing representation when it is '
                       'printed or inspected.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.items)\n'
                     '\n'
                     '    def __iter__(self):\n'
                     '        return iter(self.items)\n'
                     '\n'
                     '    def __repr__(self):\n'
                     '        return f"Bag({self.items!r})"\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(bag)',
             'output': "Bag(['a', 'b'])",
             'line': 77,
             'kind': 'cell'}]},
 {'slug': 'truth-and-size',
  'title': 'Truth and Size',
  'section': 'Data Model',
  'summary': '__bool__ and __len__ decide how objects behave in truth tests and len().',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#object.__bool__',
  'code': 'class Inbox:\n'
          '    def __init__(self, messages):\n'
          '        self.messages = list(messages)\n'
          '\n'
          '    def __len__(self):\n'
          '        return len(self.messages)\n'
          '\n'
          'class Account:\n'
          '    def __init__(self, active):\n'
          '        self.active = active\n'
          '\n'
          '    def __bool__(self):\n'
          '        return self.active\n'
          '\n'
          'print(len(Inbox(["hi", "bye"])))\n'
          'print(bool(Inbox([])))\n'
          'print(bool(Account(False)))\n',
  'expected_output': '2\nFalse\nFalse\n',
  'notes': ['Prefer `__len__` for sized containers.',
            'Prefer `__bool__` when truth has domain meaning.',
            'Keep truth tests unsurprising; surprising falsy objects make conditionals harder to read.'],
  'cells': [{'prose': ['`__len__` lets `len()` ask an object for its size.'],
             'code': 'class Inbox:\n'
                     '    def __init__(self, messages):\n'
                     '        self.messages = list(messages)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.messages)\n'
                     '\n'
                     'print(len(Inbox(["hi", "bye"])))',
             'output': '2',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['If a class has `__len__` but no `__bool__`, Python uses zero length as false.'],
             'code': 'print(bool(Inbox([])))',
             'output': 'False',
             'line': 41,
             'kind': 'cell'},
            {'prose': ['`__bool__` expresses truth directly when the answer is not just container size.'],
             'code': 'class Account:\n'
                     '    def __init__(self, active):\n'
                     '        self.active = active\n'
                     '\n'
                     '    def __bool__(self):\n'
                     '        return self.active\n'
                     '\n'
                     'print(bool(Account(False)))',
             'output': 'False',
             'line': 53,
             'kind': 'cell'}]},
 {'slug': 'container-protocols',
  'title': 'Container Protocols',
  'section': 'Data Model',
  'summary': 'Container methods connect objects to indexing, membership, and item assignment.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#emulating-container-types',
  'code': 'class Scores:\n'
          '    def __init__(self):\n'
          '        self._scores = {}\n'
          '\n'
          '    def __contains__(self, name):\n'
          '        return name in self._scores\n'
          '\n'
          '    def __getitem__(self, name):\n'
          '        return self._scores[name]\n'
          '\n'
          '    def __setitem__(self, name, score):\n'
          '        self._scores[name] = score\n'
          '\n'
          'scores = Scores()\n'
          'scores["Ada"] = 98\n'
          'print("Ada" in scores)\n'
          'print(scores["Ada"])\n',
  'expected_output': 'True\n98\n',
  'notes': ['Implement the narrowest container protocol your object needs.',
            'Use `KeyError` and `IndexError` consistently with built-in containers.',
            'If a plain `dict` or `list` is enough, prefer it over a custom container.'],
  'cells': [{'prose': ['`__setitem__` gives assignment syntax to a custom container.'],
             'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {}\n'
                     '\n'
                     '    def __setitem__(self, name, score):\n'
                     '        self._scores[name] = score\n'
                     '\n'
                     'scores = Scores()\n'
                     'scores["Ada"] = 98\n'
                     'print(scores._scores)',
             'output': "{'Ada': 98}",
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`__contains__` answers membership tests written with `in`.'],
             'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {"Ada": 98}\n'
                     '\n'
                     '    def __contains__(self, name):\n'
                     '        return name in self._scores\n'
                     '\n'
                     'scores = Scores()\n'
                     'print("Ada" in scores)',
             'output': 'True',
             'line': 43,
             'kind': 'cell'},
            {'prose': ['`__getitem__` connects bracket lookup to your internal storage.'],
             'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {"Ada": 98}\n'
                     '\n'
                     '    def __getitem__(self, name):\n'
                     '        return self._scores[name]\n'
                     '\n'
                     'scores = Scores()\n'
                     'print(scores["Ada"])',
             'output': '98',
             'line': 63,
             'kind': 'cell'}]},
 {'slug': 'callable-objects',
  'title': 'Callable Objects',
  'section': 'Data Model',
  'summary': '__call__ lets an instance behave like a function while keeping state.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#object.__call__',
  'code': 'class Multiplier:\n'
          '    def __init__(self, factor):\n'
          '        self.factor = factor\n'
          '        self.calls = 0\n'
          '\n'
          '    def __call__(self, value):\n'
          '        self.calls += 1\n'
          '        return value * self.factor\n'
          '\n'
          'double = Multiplier(2)\n'
          'print(double(5))\n'
          'print(double(7))\n'
          'print(double.calls)\n',
  'expected_output': '10\n14\n2\n',
  'notes': ['`callable(obj)` checks whether an object can be called.',
            'Callable objects are good for named, stateful behavior.',
            'Prefer plain functions when no instance state is needed.'],
  'cells': [{'prose': ['A callable object starts as ordinary state stored on an instance.'],
             'code': 'class Multiplier:\n'
                     '    def __init__(self, factor):\n'
                     '        self.factor = factor\n'
                     '        self.calls = 0\n'
                     '\n'
                     'double = Multiplier(2)\n'
                     'print(double.factor)',
             'output': '2',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`__call__` makes the instance usable with function-call syntax.'],
             'code': 'class Multiplier:\n'
                     '    def __init__(self, factor):\n'
                     '        self.factor = factor\n'
                     '        self.calls = 0\n'
                     '\n'
                     '    def __call__(self, value):\n'
                     '        self.calls += 1\n'
                     '        return value * self.factor\n'
                     '\n'
                     'double = Multiplier(2)\n'
                     'print(double(5))\n'
                     'print(double(7))',
             'output': '10\n14',
             'line': 40,
             'kind': 'cell'},
            {'prose': ['Because the callable is still an object, it can remember state across calls.'],
             'code': 'print(double.calls)',
             'output': '2',
             'line': 64,
             'kind': 'cell'}]},
 {'slug': 'operator-overloading',
  'title': 'Operator Overloading',
  'section': 'Data Model',
  'summary': 'Operator methods let objects define arithmetic and comparison syntax.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#emulating-numeric-types',
  'code': 'class Vector:\n'
          '    def __init__(self, x, y):\n'
          '        self.x = x\n'
          '        self.y = y\n'
          '\n'
          '    def __add__(self, other):\n'
          '        return Vector(self.x + other.x, self.y + other.y)\n'
          '\n'
          '    def __eq__(self, other):\n'
          '        return (self.x, self.y) == (other.x, other.y)\n'
          '\n'
          '    def __repr__(self):\n'
          '        return f"Vector({self.x}, {self.y})"\n'
          '\n'
          'print(Vector(2, 3) + Vector(4, 5))\n'
          'print(Vector(1, 1) == Vector(1, 1))\n',
  'expected_output': 'Vector(6, 8)\nTrue\n',
  'notes': ['Overload operators only when the operation is unsurprising.',
            'Return `NotImplemented` when an operand type is unsupported.',
            'Implement equality deliberately when value comparison matters.'],
  'cells': [{'prose': ['`__add__` defines how the `+` operator combines two objects.'],
             'code': 'class Vector:\n'
                     '    def __init__(self, x, y):\n'
                     '        self.x = x\n'
                     '        self.y = y\n'
                     '\n'
                     '    def __add__(self, other):\n'
                     '        return Vector(self.x + other.x, self.y + other.y)\n'
                     '\n'
                     '    def __repr__(self):\n'
                     '        return f"Vector({self.x}, {self.y})"\n'
                     '\n'
                     'print(Vector(2, 3) + Vector(4, 5))',
             'output': 'Vector(6, 8)',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`__eq__` defines value equality for `==`. Without it, user-defined objects compare by '
                       'identity.'],
             'code': 'class Vector:\n'
                     '    def __init__(self, x, y):\n'
                     '        self.x = x\n'
                     '        self.y = y\n'
                     '\n'
                     '    def __eq__(self, other):\n'
                     '        return (self.x, self.y) == (other.x, other.y)\n'
                     '\n'
                     'print(Vector(1, 1) == Vector(1, 1))',
             'output': 'True',
             'line': 45,
             'kind': 'cell'},
            {'prose': ['A useful `__repr__` makes operator results inspectable while debugging.'],
             'code': 'class Vector:\n'
                     '    def __init__(self, x, y):\n'
                     '        self.x = x\n'
                     '        self.y = y\n'
                     '\n'
                     '    def __add__(self, other):\n'
                     '        return Vector(self.x + other.x, self.y + other.y)\n'
                     '\n'
                     '    def __repr__(self):\n'
                     '        return f"Vector({self.x}, {self.y})"\n'
                     '\n'
                     'print(repr(Vector(2, 3) + Vector(4, 5)))',
             'output': 'Vector(6, 8)',
             'line': 65,
             'kind': 'cell'}]},
 {'slug': 'attribute-access',
  'title': 'Attribute Access',
  'section': 'Data Model',
  'summary': 'Attribute hooks customize lookup, missing attributes, and assignment.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#customizing-attribute-access',
  'code': 'class Settings:\n'
          '    def __init__(self, values):\n'
          '        self._values = dict(values)\n'
          '\n'
          '    def __getattr__(self, name):\n'
          '        try:\n'
          '            return self._values[name]\n'
          '        except KeyError as error:\n'
          '            raise AttributeError(name) from error\n'
          '\n'
          '    def __setattr__(self, name, value):\n'
          '        if name.startswith("_"):\n'
          '            object.__setattr__(self, name, value)\n'
          '        else:\n'
          '            self._values[name] = value\n'
          '\n'
          'settings = Settings({"theme": "dark"})\n'
          'print(settings.theme)\n'
          'settings.volume = 7\n'
          'print(settings._values["volume"])\n',
  'expected_output': 'dark\n7\n',
  'notes': ['`__getattr__` is narrower than `__getattribute__` because it handles only missing attributes.',
            '`__setattr__` affects every assignment on the instance.',
            'Use `property` or descriptors when the behavior is attached to a known attribute name.'],
  'cells': [{'prose': ['Normal initialization still needs to set real attributes. Calling `object.__setattr__` avoids '
                       'recursing through your own hook.'],
             'code': 'class Settings:\n'
                     '    def __init__(self, values):\n'
                     '        self._values = dict(values)\n'
                     '\n'
                     'settings = Settings({"theme": "dark"})\n'
                     'print(settings._values)',
             'output': "{'theme': 'dark'}",
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`__getattr__` runs only for missing attributes, so it can provide fallback lookup.'],
             'code': 'class Settings:\n'
                     '    def __init__(self, values):\n'
                     '        self._values = dict(values)\n'
                     '\n'
                     '    def __getattr__(self, name):\n'
                     '        try:\n'
                     '            return self._values[name]\n'
                     '        except KeyError as error:\n'
                     '            raise AttributeError(name) from error\n'
                     '\n'
                     'settings = Settings({"theme": "dark"})\n'
                     'print(settings.theme)',
             'output': 'dark',
             'line': 39,
             'kind': 'cell'},
            {'prose': ['`__setattr__` intercepts assignment. This example stores public names in the backing '
                       'dictionary.'],
             'code': 'class Settings:\n'
                     '    def __init__(self, values):\n'
                     '        self._values = dict(values)\n'
                     '\n'
                     '    def __setattr__(self, name, value):\n'
                     '        if name.startswith("_"):\n'
                     '            object.__setattr__(self, name, value)\n'
                     '        else:\n'
                     '            self._values[name] = value\n'
                     '\n'
                     'settings = Settings({"theme": "dark"})\n'
                     'settings.volume = 7\n'
                     'print(settings._values["volume"])',
             'output': '7',
             'line': 62,
             'kind': 'cell'}]},
 {'slug': 'descriptors',
  'title': 'Descriptors',
  'section': 'Data Model',
  'summary': 'Descriptors customize attribute access through __get__, __set__, or __delete__.',
  'doc_url': 'https://docs.python.org/3.13/howto/descriptor.html',
  'code': 'class Positive:\n'
          '    def __set_name__(self, owner, name):\n'
          '        self.private_name = "_" + name\n'
          '\n'
          '    def __get__(self, obj, owner):\n'
          '        return getattr(obj, self.private_name)\n'
          '\n'
          '    def __set__(self, obj, value):\n'
          '        if value <= 0:\n'
          '            raise ValueError("must be positive")\n'
          '        setattr(obj, self.private_name, value)\n'
          '\n'
          'class Product:\n'
          '    price = Positive()\n'
          '\n'
          '    def __init__(self, price):\n'
          '        self.price = price\n'
          '\n'
          'item = Product(10)\n'
          'print(item.price)\n'
          'try:\n'
          '    item.price = -1\n'
          'except ValueError as error:\n'
          '    print(error)\n',
  'expected_output': '10\nmust be positive\n',
  'notes': ['A descriptor object lives on the class.',
            'Attribute access on instances calls descriptor methods.',
            'Properties, methods, and many ORMs build on the descriptor protocol.'],
  'cells': [{'prose': ['A descriptor object lives on the class.'],
             'code': 'class Positive:\n'
                     '    def __set_name__(self, owner, name):\n'
                     '        self.private_name = "_" + name\n'
                     '\n'
                     '    def __get__(self, obj, owner):\n'
                     '        return getattr(obj, self.private_name)\n'
                     '\n'
                     '    def __set__(self, obj, value):\n'
                     '        if value <= 0:\n'
                     '            raise ValueError("must be positive")\n'
                     '        setattr(obj, self.private_name, value)\n'
                     '\n'
                     'class Product:\n'
                     '    price = Positive()\n'
                     '\n'
                     '    def __init__(self, price):\n'
                     '        self.price = price\n'
                     '\n'
                     'item = Product(10)\n'
                     'print(item.price)\n'
                     'try:\n'
                     '    item.price = -1\n'
                     'except ValueError as error:\n'
                     '    print(error)',
             'output': '10\nmust be positive',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'metaclasses',
  'title': 'Metaclasses',
  'section': 'Classes',
  'summary': 'A metaclass customizes how classes themselves are created.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#metaclasses',
  'code': 'class Tagged(type):\n'
          '    def __new__(mcls, name, bases, namespace):\n'
          '        namespace["tag"] = name.lower()\n'
          '        return super().__new__(mcls, name, bases, namespace)\n'
          '\n'
          'class Event(metaclass=Tagged):\n'
          '    pass\n'
          '\n'
          'print(Event.tag)\n'
          'print(type(Event).__name__)\n',
  'expected_output': 'event\nTagged\n',
  'notes': ['Metaclasses customize class creation, not instance behavior directly.',
            'Most code should prefer class decorators, functions, or ordinary inheritance.',
            'You are most likely to meet metaclasses inside frameworks and ORMs.'],
  'cells': [{'prose': ['A metaclass customizes class creation. `__new__` receives the class name, bases, and namespace '
                       'before the class object exists.'],
             'code': 'class Tagged(type):\n'
                     '    def __new__(mcls, name, bases, namespace):\n'
                     '        namespace["tag"] = name.lower()\n'
                     '        return super().__new__(mcls, name, bases, namespace)\n'
                     '\n'
                     'print(Tagged.__name__)',
             'output': 'Tagged',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['The `metaclass=` keyword applies that class-building rule. Here the metaclass adds a `tag` '
                       'attribute to the new class.'],
             'code': 'class Event(metaclass=Tagged):\n    pass\n\nprint(Event.tag)\nprint(type(Event).__name__)',
             'output': 'event\nTagged',
             'line': 39,
             'kind': 'cell'}]},
 {'slug': 'context-managers',
  'title': 'Context Managers',
  'section': 'Data Model',
  'summary': 'with ensures setup and cleanup happen together.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#context-managers',
  'code': 'from contextlib import contextmanager\n'
          '\n'
          'class Tag:\n'
          '    def __init__(self, name):\n'
          '        self.name = name\n'
          '\n'
          '    def __enter__(self):\n'
          '        print(f"<{self.name}>")\n'
          '        return self\n'
          '\n'
          '    def __exit__(self, exc_type, exc, tb):\n'
          '        print(f"</{self.name}>")\n'
          '        return False\n'
          '\n'
          '@contextmanager\n'
          'def tag(name):\n'
          '    print(f"<{name}>")\n'
          '    try:\n'
          '        yield\n'
          '    finally:\n'
          '        print(f"</{name}>")\n'
          '\n'
          'with Tag("section"):\n'
          '    print("content")\n'
          '\n'
          'try:\n'
          '    with tag("error"):\n'
          '        raise ValueError("boom")\n'
          'except ValueError:\n'
          '    print("handled")\n',
  'expected_output': '<section>\ncontent\n</section>\n<error>\n</error>\nhandled\n',
  'notes': ['Files, locks, and temporary state commonly use context managers.',
            '`__enter__` and `__exit__` power the protocol.',
            'Use `finally` when cleanup must happen after errors too.',
            'Returning true from `__exit__` suppresses an exception; do that only intentionally.'],
  'cells': [{'prose': ['A class-based context manager implements `__enter__` and `__exit__`. The value returned by '
                       '`__enter__` is bound by `as` when the `with` statement uses it.'],
             'code': 'class Tag:\n'
                     '    def __init__(self, name):\n'
                     '        self.name = name\n'
                     '\n'
                     '    def __enter__(self):\n'
                     '        print(f"<{self.name}>")\n'
                     '        return self\n'
                     '\n'
                     '    def __exit__(self, exc_type, exc, tb):\n'
                     '        print(f"</{self.name}>")\n'
                     '        return False\n'
                     '\n'
                     'with Tag("section"):\n'
                     '    print("content")',
             'output': '<section>\ncontent\n</section>',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`contextlib.contextmanager` writes the same setup/cleanup shape as a generator. Code before '
                       '`yield` is setup, and code after `yield` is cleanup.'],
             'code': 'from contextlib import contextmanager\n'
                     '\n'
                     '@contextmanager\n'
                     'def tag(name):\n'
                     '    print(f"<{name}>")\n'
                     '    try:\n'
                     '        yield\n'
                     '    finally:\n'
                     '        print(f"</{name}>")\n'
                     '\n'
                     'with tag("note"):\n'
                     '    print("body")',
             'output': '<note>\nbody\n</note>',
             'line': 49,
             'kind': 'cell'},
            {'prose': ['Cleanup still runs when the block raises. Returning `False` from `__exit__`, or letting a '
                       'generator context manager re-raise, allows the exception to keep propagating.'],
             'code': 'try:\n'
                     '    with tag("error"):\n'
                     '        raise ValueError("boom")\n'
                     'except ValueError:\n'
                     '    print("handled")',
             'output': '<error>\n</error>\nhandled',
             'line': 74,
             'kind': 'cell'}]},
 {'slug': 'delete-statements',
  'title': 'Delete Statements',
  'section': 'Data Model',
  'summary': 'del removes bindings, items, and attributes rather than producing a value.',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-del-statement',
  'code': 'profile = {"name": "Ada", "temporary": True}\n'
          'del profile["temporary"]\n'
          'print(profile)\n'
          '\n'
          'items = ["a", "b", "c"]\n'
          'del items[1]\n'
          'print(items)\n'
          '\n'
          'value = "cached"\n'
          'del value\n'
          'print("value" in locals())\n',
  'expected_output': "{'name': 'Ada'}\n['a', 'c']\nFalse\n",
  'notes': ['`del` removes bindings or container entries.',
            'Assign `None` when absence should remain an explicit value.',
            'Use container methods such as `pop()` when you need the removed value back.'],
  'cells': [{'prose': ['Deleting a dictionary key mutates the dictionary. The key is gone; it has not been set to '
                       '`None`.'],
             'code': 'profile = {"name": "Ada", "temporary": True}\ndel profile["temporary"]\nprint(profile)',
             'output': "{'name': 'Ada'}",
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Deleting a list item removes that position and shifts later items left.'],
             'code': 'items = ["a", "b", "c"]\ndel items[1]\nprint(items)',
             'output': "['a', 'c']",
             'line': 36,
             'kind': 'cell'},
            {'prose': ['Deleting a name removes the binding from the current namespace. It is different from rebinding '
                       'the name to `None`.'],
             'code': 'value = "cached"\ndel value\nprint("value" in locals())',
             'output': 'False',
             'line': 50,
             'kind': 'cell'}]},
 {'slug': 'exceptions',
  'title': 'Exceptions',
  'section': 'Errors',
  'summary': 'Use try, except, else, and finally to separate success, recovery, and cleanup.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html',
  'code': 'def parse_int(text):\n'
          '    return int(text)\n'
          '\n'
          'for text in ["42", "python"]:\n'
          '    try:\n'
          '        number = parse_int(text)\n'
          '    except ValueError:\n'
          '        print(f"{text}: invalid")\n'
          '    else:\n'
          '        print(f"{text}: {number}")\n'
          '    finally:\n'
          '        print(f"checked {text}")\n',
  'expected_output': '42: 42\nchecked 42\npython: invalid\nchecked python\n',
  'notes': ['Catch the most specific exception you can.',
            '`else` is for success code that should run only if the `try` block did not fail.',
            '`finally` runs whether the operation succeeded or failed.'],
  'cells': [{'prose': ['When no exception is raised, the `else` block runs. Keeping success in `else` makes the `try` '
                       'block contain only the operation that might fail.'],
             'code': 'def parse_int(text):\n'
                     '    return int(text)\n'
                     '\n'
                     'text = "42"\n'
                     'try:\n'
                     '    number = parse_int(text)\n'
                     'except ValueError:\n'
                     '    print(f"{text}: invalid")\n'
                     'else:\n'
                     '    print(f"{text}: {number}")\n'
                     'finally:\n'
                     '    print(f"checked {text}")',
             'output': '42: 42\nchecked 42',
             'line': 19,
             'kind': 'cell'},
            {'prose': ['When parsing fails, `int()` raises `ValueError`. Catching that specific exception makes the '
                       'expected recovery path explicit.'],
             'code': 'text = "python"\n'
                     'try:\n'
                     '    number = parse_int(text)\n'
                     'except ValueError:\n'
                     '    print(f"{text}: invalid")\n'
                     'else:\n'
                     '    print(f"{text}: {number}")\n'
                     'finally:\n'
                     '    print(f"checked {text}")',
             'output': 'python: invalid\nchecked python',
             'line': 43,
             'kind': 'cell'}]},
 {'slug': 'assertions',
  'title': 'Assertions',
  'section': 'Errors',
  'summary': 'assert documents internal assumptions and fails loudly when they are false.',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-assert-statement',
  'code': 'def average(scores):\n'
          '    assert scores, "scores must not be empty"\n'
          '    return sum(scores) / len(scores)\n'
          '\n'
          'print(average([8, 10]))\n'
          '\n'
          'try:\n'
          '    average([])\n'
          'except AssertionError as error:\n'
          '    print(error)\n',
  'expected_output': '9.0\nscores must not be empty\n',
  'notes': ['Use `assert` for internal invariants and debugging assumptions.',
            'Use explicit exceptions for user input, files, network responses, and other expected failures.',
            'Assertions can be disabled with Python optimization flags, so do not rely on them for security checks.'],
  'cells': [{'prose': ['When the assertion is true, execution continues normally. The assertion documents the '
                       "function's internal expectation."],
             'code': 'def average(scores):\n'
                     '    assert scores, "scores must not be empty"\n'
                     '    return sum(scores) / len(scores)\n'
                     '\n'
                     'print(average([8, 10]))',
             'output': '9.0',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['When the assertion is false, Python raises `AssertionError`. This signals a broken assumption, '
                       'not a normal recovery path.'],
             'code': 'try:\n    average([])\nexcept AssertionError as error:\n    print(error)',
             'output': 'scores must not be empty',
             'line': 38,
             'kind': 'cell'}]},
 {'slug': 'exception-chaining',
  'title': 'Exception Chaining',
  'section': 'Errors',
  'summary': 'raise from preserves the original cause when translating exceptions.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#exception-chaining',
  'code': 'class ConfigError(Exception):\n'
          '    pass\n'
          '\n'
          '\n'
          'def read_port(text):\n'
          '    try:\n'
          '        return int(text)\n'
          '    except ValueError as error:\n'
          '        raise ConfigError("port must be a number") from error\n'
          '\n'
          'print(ConfigError.__name__)\n'
          '\n'
          'try:\n'
          '    read_port("abc")\n'
          'except ConfigError as error:\n'
          '    print(error)\n'
          '    print(type(error.__cause__).__name__)\n',
  'expected_output': 'ConfigError\nport must be a number\nValueError\n',
  'notes': ['Use `raise ... from error` when translating exceptions across a boundary.',
            "The new exception's `__cause__` points to the original exception.",
            'Chaining keeps user-facing errors clear without losing debugging context.'],
  'cells': [{'prose': ['Catch the low-level exception where it happens, then raise a domain-specific exception from '
                       'it.'],
             'code': 'class ConfigError(Exception):\n'
                     '    pass\n'
                     '\n'
                     '\n'
                     'def read_port(text):\n'
                     '    try:\n'
                     '        return int(text)\n'
                     '    except ValueError as error:\n'
                     '        raise ConfigError("port must be a number") from error\n'
                     '\n'
                     'print(ConfigError.__name__)',
             'output': 'ConfigError',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['The caller handles the domain error. The original `ValueError` remains available as '
                       '`__cause__`.'],
             'code': 'try:\n'
                     '    read_port("abc")\n'
                     'except ConfigError as error:\n'
                     '    print(error)\n'
                     '    print(type(error.__cause__).__name__)',
             'output': 'port must be a number\nValueError',
             'line': 44,
             'kind': 'cell'}]},
 {'slug': 'exception-groups',
  'title': 'Exception Groups',
  'section': 'Errors',
  'summary': 'except* handles matching exceptions inside an ExceptionGroup.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions',
  'code': 'errors = ExceptionGroup(\n'
          '    "batch failed",\n'
          '    [ValueError("bad port"), TypeError("bad mode")],\n'
          ')\n'
          'print(len(errors.exceptions))\n'
          '\n'
          'try:\n'
          '    raise errors\n'
          'except* ValueError as group:\n'
          '    print(type(group).__name__)\n'
          '    print(group.exceptions[0])\n'
          'except* TypeError as group:\n'
          '    print(group.exceptions[0])\n',
  'expected_output': '2\nExceptionGroup\nbad port\nbad mode\n',
  'notes': ['`except*` is for `ExceptionGroup`, not ordinary single exceptions.',
            'Each `except*` clause handles matching members of the group.',
            'Exception groups often appear around concurrent work.'],
  'cells': [{'prose': ['An exception group bundles several exception objects. This is different from an ordinary '
                       'exception because more than one failure is present.'],
             'code': 'errors = ExceptionGroup(\n'
                     '    "batch failed",\n'
                     '    [ValueError("bad port"), TypeError("bad mode")],\n'
                     ')\n'
                     'print(len(errors.exceptions))',
             'output': '2',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`except*` handles matching members of the group. The `ValueError` handler sees the value '
                       'error, and the `TypeError` handler sees the type error.'],
             'code': 'try:\n'
                     '    raise errors\n'
                     'except* ValueError as group:\n'
                     '    print(type(group).__name__)\n'
                     '    print(group.exceptions[0])\n'
                     'except* TypeError as group:\n'
                     '    print(group.exceptions[0])',
             'output': 'ExceptionGroup\nbad port\nbad mode',
             'line': 38,
             'kind': 'cell'}]},
 {'slug': 'warnings',
  'title': 'Warnings',
  'section': 'Errors',
  'summary': 'warnings report soft problems without immediately stopping the program.',
  'doc_url': 'https://docs.python.org/3.13/library/warnings.html',
  'code': 'import warnings\n'
          '\n'
          '\n'
          'def old_name():\n'
          '    warnings.warn("old_name is deprecated", DeprecationWarning, stacklevel=2)\n'
          '    return "result"\n'
          '\n'
          'warnings.simplefilter("always", DeprecationWarning)\n'
          'with warnings.catch_warnings(record=True) as caught:\n'
          '    print(old_name())\n'
          '    print(caught[0].category.__name__)\n'
          '    print(str(caught[0].message))\n',
  'expected_output': 'result\nDeprecationWarning\nold_name is deprecated\n',
  'notes': ['Warnings are useful for deprecations and soft failures.',
            'Filters decide whether warnings are ignored, shown, or turned into errors.',
            'Tests often capture warnings to assert migration behavior.'],
  'cells': [{'prose': ['Warnings are useful for deprecations and soft failures.'],
             'code': 'import warnings\n'
                     '\n'
                     '\n'
                     'def old_name():\n'
                     '    warnings.warn("old_name is deprecated", DeprecationWarning, stacklevel=2)\n'
                     '    return "result"\n'
                     '\n'
                     'warnings.simplefilter("always", DeprecationWarning)\n'
                     'with warnings.catch_warnings(record=True) as caught:\n'
                     '    print(old_name())\n'
                     '    print(caught[0].category.__name__)\n'
                     '    print(str(caught[0].message))',
             'output': 'result\nDeprecationWarning\nold_name is deprecated',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'modules',
  'title': 'Modules',
  'section': 'Modules',
  'summary': 'Modules organize code into namespaces and expose reusable definitions.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/modules.html',
  'code': 'import math\n'
          'import sys\n'
          'from statistics import mean\n'
          '\n'
          'radius = 3\n'
          'area = math.pi * radius ** 2\n'
          'print(round(area, 2))\n'
          '\n'
          'scores = [8, 10, 9]\n'
          'print(mean(scores))\n'
          '\n'
          'print(math.__name__)\n'
          'print("math" in sys.modules)\n',
  'expected_output': '28.27\n9\nmath\nTrue\n',
  'notes': ['Prefer plain `import module` when the namespace improves readability.',
            'Use focused imports for a small number of clear names.',
            'Place imports near the top of the file.',
            'Imports execute module top-level code once, then reuse the cached module object.'],
  'cells': [{'prose': ['Importing a module gives access to its namespace. The `math.` prefix makes it clear where `pi` '
                       'came from.'],
             'code': 'import math\n\nradius = 3\narea = math.pi * radius ** 2\nprint(round(area, 2))',
             'output': '28.27',
             'line': 21,
             'kind': 'cell'},
            {'prose': ['A focused `from ... import ...` brings one definition into the current namespace. This keeps a '
                       'common operation concise without importing every name.'],
             'code': 'from statistics import mean\n\nscores = [8, 10, 9]\nprint(mean(scores))',
             'output': '9',
             'line': 37,
             'kind': 'cell'},
            {'prose': ['Modules are objects too. Their attributes include metadata such as `__name__`, which records '
                       "the module's import name."],
             'code': 'print(math.__name__)',
             'output': 'math',
             'line': 52,
             'kind': 'cell'},
            {'prose': ['Imported modules are cached in `sys.modules`. Later imports reuse the module object instead of '
                       'executing the file again.'],
             'code': 'import sys\nprint("math" in sys.modules)',
             'output': 'True',
             'line': 64,
             'kind': 'cell'}]},
 {'slug': 'import-aliases',
  'title': 'Import Aliases',
  'section': 'Modules',
  'summary': 'as gives imported modules or names a local alias.',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-import-statement',
  'code': 'import statistics as stats\n'
          'from math import sqrt as square_root\n'
          '\n'
          'scores = [8, 10, 9]\n'
          'print(stats.mean(scores))\n'
          'print(stats.__name__)\n'
          '\n'
          'print(square_root(81))\n'
          'print(square_root.__name__)\n',
  'expected_output': '9\nstatistics\n9.0\nsqrt\n',
  'notes': ['`import module as alias` keeps module-style access under a shorter or clearer name.',
            '`from module import name as alias` imports one name under a local alias.',
            'Prefer plain imports unless an alias improves clarity or follows a strong convention.',
            'Avoid `from module import *` because it makes dependencies harder to see.'],
  'cells': [{'prose': ['A module alias keeps the namespace but changes the local name. Here `stats` is shorter, but '
                       'readers can still see that `mean` belongs to the statistics module.'],
             'code': 'import statistics as stats\n'
                     '\n'
                     'scores = [8, 10, 9]\n'
                     'print(stats.mean(scores))\n'
                     'print(stats.__name__)',
             'output': '9\nstatistics',
             'line': 21,
             'kind': 'cell'},
            {'prose': ['A name imported with `from` can also be aliased. Use this when the local name explains the '
                       'role better than the original name.'],
             'code': 'from math import sqrt as square_root\n\nprint(square_root(81))\nprint(square_root.__name__)',
             'output': '9.0\nsqrt',
             'line': 38,
             'kind': 'cell'}]},
 {'slug': 'packages',
  'title': 'Packages',
  'section': 'Modules',
  'summary': 'Packages organize modules into importable directories.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/modules.html#packages',
  'code': 'import importlib\n'
          'import json\n'
          'import json.decoder\n'
          '\n'
          'module = importlib.import_module("json.decoder")\n'
          '\n'
          'print(json.__name__)\n'
          'print(json.decoder.__name__)\n'
          'print(module.JSONDecoder.__name__)\n'
          'print(module is json.decoder)\n',
  'expected_output': 'json\njson.decoder\nJSONDecoder\nTrue\n',
  'notes': ['A package is a module that can contain submodules.',
            'Dotted imports should mirror a meaningful project structure.',
            'Prefer ordinary imports unless the module name is truly dynamic.'],
  'cells': [{'prose': ['A package is itself a module. The `json` package exposes a namespace that can contain '
                       'submodules.'],
             'code': 'import json\n\nprint(json.__name__)',
             'output': 'json',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Dotted imports name a path through a package. Importing `json.decoder` makes that submodule '
                       'available under the package namespace.'],
             'code': 'import json.decoder\n\nprint(json.decoder.__name__)\nprint(json.decoder.JSONDecoder.__name__)',
             'output': 'json.decoder\nJSONDecoder',
             'line': 31,
             'kind': 'cell'},
            {'prose': ['`importlib.import_module()` imports by string. It is useful for plugin systems and dynamic '
                       'imports, but ordinary `import` is clearer when the dependency is known.'],
             'code': 'import importlib\n'
                     '\n'
                     'module = importlib.import_module("json.decoder")\n'
                     'print(module is json.decoder)',
             'output': 'True',
             'line': 47,
             'kind': 'cell'}]},
 {'slug': 'virtual-environments',
  'title': 'Virtual Environments',
  'section': 'Modules',
  'summary': "Virtual environments isolate a project's Python packages.",
  'doc_url': 'https://docs.python.org/3.13/library/venv.html',
  'code': 'import pathlib\n'
          'import tempfile\n'
          'import venv\n'
          '\n'
          'with tempfile.TemporaryDirectory() as directory:\n'
          '    env_path = pathlib.Path(directory) / ".venv"\n'
          '    builder = venv.EnvBuilder(with_pip=False)\n'
          '    builder.create(env_path)\n'
          '\n'
          '    print(env_path.name)\n'
          '    print((env_path / "pyvenv.cfg").exists())\n',
  'expected_output': '.venv\nTrue\n',
  'notes': ['A virtual environment gives a project its own install location.',
            'Inside a venv, `sys.prefix` usually differs from `sys.base_prefix`.',
            'Use `python -m venv .venv` at the command line for everyday project setup.'],
  'cells': [{'prose': ['Dynamic Workers do not provide the `venv` module or a project environment workflow.'],
             'code': 'builder = venv.EnvBuilder(with_pip=False)\nbuilder.create(".venv")',
             'output': '',
             'line': 18,
             'kind': 'unsupported'},
            {'prose': ['`venv.EnvBuilder` creates the same kind of isolated environment as `python -m venv`. A '
                       'temporary directory keeps the example from leaving project files behind.'],
             'code': 'import pathlib\n'
                     'import tempfile\n'
                     'import venv\n'
                     '\n'
                     'with tempfile.TemporaryDirectory() as directory:\n'
                     '    env_path = pathlib.Path(directory) / ".venv"\n'
                     '    builder = venv.EnvBuilder(with_pip=False)\n'
                     '    builder.create(env_path)\n'
                     '\n'
                     '    print(env_path.name)\n'
                     '    print((env_path / "pyvenv.cfg").exists())',
             'output': '.venv\nTrue',
             'line': 27,
             'kind': 'cell'}]},
 {'slug': 'type-hints',
  'title': 'Type Hints',
  'section': 'Types',
  'summary': 'Annotations document expected types and power static analysis.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html',
  'code': 'def total(numbers: list[int]) -> int:\n'
          '    return sum(numbers)\n'
          '\n'
          'print(total([1, 2, 3]))\n'
          'print(total.__annotations__)\n'
          '\n'
          '\n'
          'def label(score: int) -> str:\n'
          '    return f"score={score}"\n'
          '\n'
          'print(label("high"))\n',
  'expected_output': "6\n{'numbers': list[int], 'return': <class 'int'>}\nscore=high\n",
  'notes': ['Python does not enforce most type hints at runtime.',
            'Tools like type checkers and editors use annotations to catch mistakes earlier.',
            'Use runtime validation when untrusted input must be rejected while the program runs.'],
  'cells': [{'prose': ['Type hints document expected parameter and return shapes. Python still runs the function '
                       'normally at runtime.'],
             'code': 'def total(numbers: list[int]) -> int:\n    return sum(numbers)\n\nprint(total([1, 2, 3]))',
             'output': '6',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Python stores annotations on the function object for tools and introspection. Type checkers '
                       'use this information without changing the function call syntax.'],
             'code': 'print(total.__annotations__)',
             'output': "{'numbers': list[int], 'return': <class 'int'>}",
             'line': 32,
             'kind': 'cell'},
            {'prose': ['Most hints are not runtime validation. This call passes a string where the hint says `int`; '
                       'Python still calls the function because the body can format any value.'],
             'code': 'def label(score: int) -> str:\n    return f"score={score}"\n\nprint(label("high"))',
             'output': 'score=high',
             'line': 44,
             'kind': 'cell'}]},
 {'slug': 'runtime-type-checks',
  'title': 'Runtime Type Checks',
  'section': 'Types',
  'summary': 'type, isinstance, and issubclass inspect runtime relationships.',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#isinstance',
  'code': 'class Animal:\n'
          '    pass\n'
          '\n'
          'class Dog(Animal):\n'
          '    pass\n'
          '\n'
          'pet = Dog()\n'
          '\n'
          'print(type(pet).__name__)\n'
          'print(type(pet) is Animal)\n'
          'print(isinstance(pet, Animal))\n'
          'print(issubclass(Dog, Animal))\n',
  'expected_output': 'Dog\nFalse\nTrue\nTrue\n',
  'notes': ['`type()` is exact; `isinstance()` follows inheritance.',
            'Runtime checks inspect objects, not static annotations.',
            'Prefer behavior, protocols, or clear validation over scattered type checks.'],
  'cells': [{'prose': ['`type()` reports the exact runtime class. A `Dog` instance is not exactly an `Animal` '
                       'instance.'],
             'code': 'class Animal:\n'
                     '    pass\n'
                     '\n'
                     'class Dog(Animal):\n'
                     '    pass\n'
                     '\n'
                     'pet = Dog()\n'
                     'print(type(pet).__name__)\n'
                     'print(type(pet) is Animal)',
             'output': 'Dog\nFalse',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`isinstance()` accepts subclasses, which is usually what API boundaries want.'],
             'code': 'print(isinstance(pet, Dog))\nprint(isinstance(pet, Animal))',
             'output': 'True\nTrue',
             'line': 43,
             'kind': 'cell'},
            {'prose': ['`issubclass()` checks class relationships rather than individual objects.'],
             'code': 'print(issubclass(Dog, Animal))',
             'output': 'True',
             'line': 57,
             'kind': 'cell'}]},
 {'slug': 'union-and-optional-types',
  'title': 'Union and Optional Types',
  'section': 'Types',
  'summary': 'The | operator describes values that may have more than one static type.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Optional',
  'code': 'def label(value: int | str) -> str:\n'
          '    return f"item-{value}"\n'
          '\n'
          '\n'
          'def greeting(name: str | None) -> str:\n'
          '    if name is None:\n'
          '        return "hello guest"\n'
          '    return f"hello {name.upper()}"\n'
          '\n'
          'print(label(3))\n'
          'print(label("A"))\n'
          'print(greeting(None))\n'
          'print(greeting("Ada"))\n'
          'print(greeting.__annotations__)\n',
  'expected_output': "item-3\nitem-A\nhello guest\nhello ADA\n{'name': str | None, 'return': <class 'str'>}\n",
  'notes': ['Use `A | B` when a value may have either type.',
            '`T | None` means absence is an expected case, not an error by itself.',
            'Narrow unions before using behavior that belongs to only one member type.'],
  'cells': [{'prose': ['Use `A | B` when a value may have either type. The function body should use operations that '
                       'make sense for every member of the union.'],
             'code': 'def label(value: int | str) -> str:\n'
                     '    return f"item-{value}"\n'
                     '\n'
                     'print(label(3))\n'
                     'print(label("A"))',
             'output': 'item-3\nitem-A',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`str | None` means the function accepts either a string or explicit absence. Check for `None` '
                       'before calling string methods.'],
             'code': 'def greeting(name: str | None) -> str:\n'
                     '    if name is None:\n'
                     '        return "hello guest"\n'
                     '    return f"hello {name.upper()}"\n'
                     '\n'
                     'print(greeting(None))\n'
                     'print(greeting("Ada"))',
             'output': 'hello guest\nhello ADA',
             'line': 39,
             'kind': 'cell'},
            {'prose': ['Union annotations are visible at runtime, but Python does not enforce them when the function '
                       'is called.'],
             'code': 'print(greeting.__annotations__)',
             'output': "{'name': str | None, 'return': <class 'str'>}",
             'line': 58,
             'kind': 'cell'}]},
 {'slug': 'type-aliases',
  'title': 'Type Aliases',
  'section': 'Types',
  'summary': 'Type aliases give a meaningful name to a repeated type shape.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#type-aliases',
  'code': 'type UserId = int\n'
          'type Scores = dict[UserId, int]\n'
          'LegacyName = str\n'
          '\n'
          '\n'
          'def best_user(scores: Scores) -> UserId:\n'
          '    return max(scores, key=scores.get)\n'
          '\n'
          'scores: Scores = {1: 98, 2: 91}\n'
          'print(best_user(scores))\n'
          'print(UserId.__name__)\n'
          'print(LegacyName("Ada"))\n',
  'expected_output': '1\nUserId\nAda\n',
  'notes': ['Use aliases to name repeated or domain-specific annotation shapes.',
            'A type alias does not validate values at runtime.',
            'Use `NewType` when two values share a runtime representation but should not be mixed statically.'],
  'cells': [{'prose': ['The `type` statement names an annotation shape. Here `Scores` means a dictionary from user IDs '
                       'to integer scores.'],
             'code': 'type UserId = int\n'
                     'type Scores = dict[UserId, int]\n'
                     '\n'
                     '\n'
                     'def best_user(scores: Scores) -> UserId:\n'
                     '    return max(scores, key=scores.get)\n'
                     '\n'
                     'scores: Scores = {1: 98, 2: 91}\n'
                     'print(best_user(scores))',
             'output': '1',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Modern aliases are runtime objects that keep their alias name for introspection.'],
             'code': 'print(UserId.__name__)\nprint(Scores.__name__)',
             'output': 'UserId\nScores',
             'line': 42,
             'kind': 'cell'},
            {'prose': ['Assignment-style aliases are still common, but they are just ordinary names bound to existing '
                       'objects.'],
             'code': 'LegacyName = str\nprint(LegacyName("Ada"))\nprint(LegacyName is str)',
             'output': 'Ada\nTrue',
             'line': 56,
             'kind': 'cell'}]},
 {'slug': 'typed-dicts',
  'title': 'TypedDict',
  'section': 'Types',
  'summary': 'TypedDict describes dictionaries with known string keys.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.TypedDict',
  'code': 'from typing import NotRequired, TypedDict\n'
          '\n'
          'class User(TypedDict):\n'
          '    name: str\n'
          '    score: int\n'
          '    nickname: NotRequired[str]\n'
          '\n'
          '\n'
          'def describe(user: User) -> str:\n'
          '    return f"{user[\'name\']}: {user[\'score\']}"\n'
          '\n'
          'record: User = {"name": "Ada", "score": 98}\n'
          'print(describe(record))\n'
          'print(isinstance(record, dict))\n'
          'print(record.get("nickname", "none"))\n',
  'expected_output': 'Ada: 98\nTrue\nnone\n',
  'notes': ['Use `TypedDict` for dictionary records from JSON or APIs.',
            'Type checkers understand required and optional keys.',
            'Runtime behavior is still ordinary dictionary behavior.'],
  'cells': [{'prose': ['Use `TypedDict` for JSON-like records that remain dictionaries.'],
             'code': 'from typing import TypedDict\n'
                     '\n'
                     'class User(TypedDict):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '\n'
                     '\n'
                     'def describe(user: User) -> str:\n'
                     '    return f"{user[\'name\']}: {user[\'score\']}"\n'
                     '\n'
                     'record: User = {"name": "Ada", "score": 98}\n'
                     'print(describe(record))',
             'output': 'Ada: 98',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['At runtime, a `TypedDict` value is still a plain dictionary.'],
             'code': 'print(isinstance(record, dict))\nprint(type(record).__name__)',
             'output': 'True\ndict',
             'line': 45,
             'kind': 'cell'},
            {'prose': ['`NotRequired` marks a key that type checkers should treat as optional. Runtime lookup still '
                       'uses normal dictionary tools such as `get()`.'],
             'code': 'from typing import NotRequired\n'
                     '\n'
                     'class UserWithNickname(TypedDict):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '    nickname: NotRequired[str]\n'
                     '\n'
                     'record: UserWithNickname = {"name": "Ada", "score": 98}\n'
                     'print(record.get("nickname", "none"))',
             'output': 'none',
             'line': 59,
             'kind': 'cell'}]},
 {'slug': 'literal-and-final',
  'title': 'Literal and Final',
  'section': 'Types',
  'summary': 'Literal restricts values, while Final marks names that should not be rebound.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Literal',
  'code': 'from typing import Final, Literal\n'
          '\n'
          'Mode = Literal["read", "write"]\n'
          'DEFAULT_MODE: Final[Mode] = "read"\n'
          '\n'
          '\n'
          'def open_label(mode: Mode) -> str:\n'
          '    return f"opening for {mode}"\n'
          '\n'
          'print(open_label(DEFAULT_MODE))\n'
          'print(open_label("write"))\n'
          'print(DEFAULT_MODE)\n',
  'expected_output': 'opening for read\nopening for write\nread\n',
  'notes': ['`Literal` describes a small set of exact allowed values.',
            '`Final` tells type checkers that a name should not be rebound.',
            'Both are static promises; ordinary runtime assignment rules still apply.'],
  'cells': [{'prose': ['`Literal` describes a small set of exact allowed values.'],
             'code': 'from typing import Final, Literal\n'
                     '\n'
                     'Mode = Literal["read", "write"]\n'
                     'DEFAULT_MODE: Final[Mode] = "read"\n'
                     '\n'
                     '\n'
                     'def open_label(mode: Mode) -> str:\n'
                     '    return f"opening for {mode}"\n'
                     '\n'
                     'print(open_label(DEFAULT_MODE))\n'
                     'print(open_label("write"))\n'
                     'print(DEFAULT_MODE)',
             'output': 'opening for read\nopening for write\nread',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'callable-types',
  'title': 'Callable Types',
  'section': 'Types',
  'summary': 'Callable annotations describe functions passed as values.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#annotating-callable-objects',
  'code': 'from collections.abc import Callable\n'
          '\n'
          '\n'
          'def apply_twice(value: int, func: Callable[[int], int]) -> int:\n'
          '    return func(func(value))\n'
          '\n'
          '\n'
          'def add_one(number: int) -> int:\n'
          '    return number + 1\n'
          '\n'
          'class Doubler:\n'
          '    def __call__(self, number: int) -> int:\n'
          '        return number * 2\n'
          '\n'
          'print(apply_twice(3, add_one))\n'
          'print(apply_twice(3, Doubler()))\n'
          'print(callable(add_one), callable(Doubler()))\n',
  'expected_output': '5\n12\nTrue True\n',
  'notes': ['Use `Callable[[Arg], Return]` for simple function-shaped values.',
            'The annotation documents how the callback will be called.',
            'For complex call signatures, protocols can be clearer.'],
  'cells': [{'prose': ['Use `Callable[[Arg], Return]` for function-shaped values. The callback is passed in and called '
                       'by the receiving function.'],
             'code': 'from collections.abc import Callable\n'
                     '\n'
                     '\n'
                     'def apply_twice(value: int, func: Callable[[int], int]) -> int:\n'
                     '    return func(func(value))\n'
                     '\n'
                     '\n'
                     'def add_one(number: int) -> int:\n'
                     '    return number + 1\n'
                     '\n'
                     'print(apply_twice(3, add_one))',
             'output': '5',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Callable annotations are structural: an object with `__call__` can also satisfy the shape.'],
             'code': 'class Doubler:\n'
                     '    def __call__(self, number: int) -> int:\n'
                     '        return number * 2\n'
                     '\n'
                     'print(apply_twice(3, Doubler()))',
             'output': '12',
             'line': 44,
             'kind': 'cell'},
            {'prose': ['Runtime callability is a separate question from static annotation. `callable()` checks whether '
                       'Python can call the object.'],
             'code': 'print(callable(add_one), callable(Doubler()))',
             'output': 'True True',
             'line': 60,
             'kind': 'cell'}]},
 {'slug': 'generics-and-typevar',
  'title': 'Generics and TypeVar',
  'section': 'Types',
  'summary': 'Generics preserve type information across reusable functions and classes.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#generics',
  'code': 'from typing import TypeVar\n'
          '\n'
          'T = TypeVar("T")\n'
          '\n'
          '\n'
          'def first(items: list[T]) -> T:\n'
          '    return items[0]\n'
          '\n'
          '\n'
          'def pair(left: T, right: T) -> tuple[T, T]:\n'
          '    return (left, right)\n'
          '\n'
          'print(first([1, 2, 3]))\n'
          'print(first(["Ada", "Grace"]))\n'
          'print(pair("x", "y"))\n'
          'print(T.__name__)\n',
  'expected_output': "1\nAda\n('x', 'y')\nT\n",
  'notes': ['A `TypeVar` stands for a type chosen by the caller.',
            'Generic functions avoid losing information to `object` or `Any`.',
            'Use generics when input and output types are connected.'],
  'cells': [{'prose': ['A `TypeVar` stands for a type chosen by the caller. The return type follows the list element '
                       'type.'],
             'code': 'from typing import TypeVar\n'
                     '\n'
                     'T = TypeVar("T")\n'
                     '\n'
                     '\n'
                     'def first(items: list[T]) -> T:\n'
                     '    return items[0]\n'
                     '\n'
                     'print(first([1, 2, 3]))\n'
                     'print(first(["Ada", "Grace"]))',
             'output': '1\nAda',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Reusing the same `TypeVar` expresses a relationship between parameters and results.'],
             'code': 'def pair(left: T, right: T) -> tuple[T, T]:\n    return (left, right)\n\nprint(pair("x", "y"))',
             'output': "('x', 'y')",
             'line': 44,
             'kind': 'cell'},
            {'prose': ['`TypeVar` is visible at runtime, but the relationship is mainly for type checkers.'],
             'code': 'print(T.__name__)\nprint(first.__annotations__)',
             'output': "T\n{'items': list[~T], 'return': ~T}",
             'line': 59,
             'kind': 'cell'}]},
 {'slug': 'paramspec',
  'title': 'ParamSpec',
  'section': 'Types',
  'summary': 'ParamSpec preserves callable parameter types through wrappers.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.ParamSpec',
  'code': 'from collections.abc import Callable\n'
          'from typing import ParamSpec, TypeVar\n'
          '\n'
          'P = ParamSpec("P")\n'
          'R = TypeVar("R")\n'
          '\n'
          '\n'
          'def logged(func: Callable[P, R]) -> Callable[P, R]:\n'
          '    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:\n'
          '        print("calling", func.__name__)\n'
          '        return func(*args, **kwargs)\n'
          '    return wrapper\n'
          '\n'
          '@logged\n'
          'def add(left: int, right: int) -> int:\n'
          '    return left + right\n'
          '\n'
          'print(add(2, 3))\n',
  'expected_output': 'calling add\n5\n',
  'notes': ['`ParamSpec` captures the parameters of a callable.',
            'Wrappers can forward `*args` and `**kwargs` without erasing the original signature for type checkers.',
            'This matters most for decorators.'],
  'cells': [{'prose': ['`ParamSpec` captures the parameters of a callable.'],
             'code': 'from collections.abc import Callable\n'
                     'from typing import ParamSpec, TypeVar\n'
                     '\n'
                     'P = ParamSpec("P")\n'
                     'R = TypeVar("R")\n'
                     '\n'
                     '\n'
                     'def logged(func: Callable[P, R]) -> Callable[P, R]:\n'
                     '    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:\n'
                     '        print("calling", func.__name__)\n'
                     '        return func(*args, **kwargs)\n'
                     '    return wrapper\n'
                     '\n'
                     '@logged\n'
                     'def add(left: int, right: int) -> int:\n'
                     '    return left + right\n'
                     '\n'
                     'print(add(2, 3))',
             'output': 'calling add\n5',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'overloads',
  'title': 'Overloads',
  'section': 'Types',
  'summary': 'overload describes APIs whose return type depends on argument types.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.overload',
  'code': 'from typing import overload\n'
          '\n'
          '@overload\n'
          'def double(value: int) -> int: ...\n'
          '\n'
          '@overload\n'
          'def double(value: str) -> str: ...\n'
          '\n'
          'def double(value):\n'
          '    return value * 2\n'
          '\n'
          'print(double(4))\n'
          'print(double("ha"))\n'
          'print(double.__name__)\n',
  'expected_output': '8\nhaha\ndouble\n',
  'notes': ['`@overload` signatures are for static type checkers.',
            'The real implementation comes after the overload declarations.',
            'Use overloads when a single runtime function has multiple precise static shapes.'],
  'cells': [{'prose': ['`@overload` signatures are for static type checkers.'],
             'code': 'from typing import overload\n'
                     '\n'
                     '@overload\n'
                     'def double(value: int) -> int: ...\n'
                     '\n'
                     '@overload\n'
                     'def double(value: str) -> str: ...\n'
                     '\n'
                     'def double(value):\n'
                     '    return value * 2\n'
                     '\n'
                     'print(double(4))\n'
                     'print(double("ha"))\n'
                     'print(double.__name__)',
             'output': '8\nhaha\ndouble',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'casts-and-any',
  'title': 'Casts and Any',
  'section': 'Types',
  'summary': 'Any and cast are escape hatches for places static analysis cannot prove.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.cast',
  'code': 'from typing import Any, cast\n'
          '\n'
          'raw: Any = {"score": "98"}\n'
          'score_text = cast(dict[str, str], raw)["score"]\n'
          'score = int(score_text)\n'
          '\n'
          'print(score + 2)\n'
          'print(cast(list[int], raw) is raw)\n'
          'print(type(raw).__name__)\n',
  'expected_output': '100\nTrue\ndict\n',
  'notes': ['`Any` disables most static checking for a value.',
            '`cast()` tells the type checker to trust you without changing the runtime object.',
            'Prefer narrowing with checks when possible.'],
  'cells': [{'prose': ['`Any` disables most static checking for a value. The runtime object is still whatever value '
                       'was actually assigned.'],
             'code': 'from typing import Any, cast\n'
                     '\n'
                     'raw: Any = {"score": "98"}\n'
                     'score_text = cast(dict[str, str], raw)["score"]\n'
                     'score = int(score_text)\n'
                     'print(score + 2)',
             'output': '100',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['`cast()` does not convert or validate the value. It returns the same object at runtime.'],
             'code': 'print(cast(list[int], raw) is raw)\nprint(type(raw).__name__)',
             'output': 'True\ndict',
             'line': 39,
             'kind': 'cell'},
            {'prose': ['A real runtime check narrows by inspecting the value. This is safer when the input is '
                       'untrusted.'],
             'code': 'value: object = {"score": "98"}\nif isinstance(value, dict):\n    print(value["score"])',
             'output': '98',
             'line': 53,
             'kind': 'cell'}]},
 {'slug': 'newtype',
  'title': 'NewType',
  'section': 'Types',
  'summary': 'NewType creates distinct static identities for runtime-compatible values.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.NewType',
  'code': 'from typing import NewType\n'
          '\n'
          'UserId = NewType("UserId", int)\n'
          'OrderId = NewType("OrderId", int)\n'
          '\n'
          '\n'
          'def load_user(user_id: UserId) -> str:\n'
          '    return f"user {user_id}"\n'
          '\n'
          'uid = UserId(42)\n'
          'oid = OrderId(42)\n'
          'print(load_user(uid))\n'
          'print(uid == oid)\n'
          'print(type(uid).__name__)\n'
          'print(UserId.__name__)\n',
  'expected_output': 'user 42\nTrue\nint\nUserId\n',
  'notes': ['`NewType` helps type checkers distinguish values that share a runtime representation.',
            'At runtime, the value is still the underlying type.',
            'Use aliases for readability; use `NewType` for static separation.'],
  'cells': [{'prose': ['`NewType` helps type checkers distinguish values that share a runtime representation.'],
             'code': 'from typing import NewType\n'
                     '\n'
                     'UserId = NewType("UserId", int)\n'
                     'OrderId = NewType("OrderId", int)\n'
                     '\n'
                     '\n'
                     'def load_user(user_id: UserId) -> str:\n'
                     '    return f"user {user_id}"\n'
                     '\n'
                     'uid = UserId(42)\n'
                     'print(load_user(uid))',
             'output': 'user 42',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['At runtime, a `NewType` value is the underlying value. It compares like that value and has the '
                       'same runtime type.'],
             'code': 'oid = OrderId(42)\nprint(uid == oid)\nprint(type(uid).__name__)',
             'output': 'True\nint',
             'line': 44,
             'kind': 'cell'},
            {'prose': ['The `NewType` constructor keeps a name for static tools and introspection.'],
             'code': 'print(UserId.__name__)\nprint(OrderId.__name__)',
             'output': 'UserId\nOrderId',
             'line': 59,
             'kind': 'cell'}]},
 {'slug': 'protocols',
  'title': 'Protocols',
  'section': 'Types',
  'summary': 'Protocol describes required behavior for structural typing.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Protocol',
  'code': 'from typing import Protocol\n'
          '\n'
          'class Greeter(Protocol):\n'
          '    def greet(self) -> str:\n'
          '        ...\n'
          '\n'
          'class Person:\n'
          '    def __init__(self, name):\n'
          '        self.name = name\n'
          '\n'
          '    def greet(self):\n'
          '        return f"hello {self.name}"\n'
          '\n'
          '\n'
          'def welcome(greeter: Greeter):\n'
          '    print(greeter.greet())\n'
          '\n'
          'welcome(Person("Ada"))\n'
          'print(Greeter.__name__)\n',
  'expected_output': 'hello Ada\nGreeter\n',
  'notes': ['Protocols are for structural typing: compatibility by shape rather than explicit inheritance.',
            'Type checkers understand protocols; normal runtime method calls still do the work.',
            'Prefer inheritance when shared implementation matters, and protocols when only required behavior '
            'matters.'],
  'cells': [{'prose': ['A protocol names required behavior. The ellipsis marks the method body as intentionally '
                       'unspecified, similar to an interface declaration.'],
             'code': 'from typing import Protocol\n'
                     '\n'
                     'class Greeter(Protocol):\n'
                     '    def greet(self) -> str:\n'
                     '        ...\n'
                     '\n'
                     'print(Greeter.__name__)',
             'output': 'Greeter',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['A class can satisfy the protocol without inheriting from it. `Person` has a compatible '
                       '`greet()` method, so it has the right shape for static type checkers.'],
             'code': 'class Person:\n'
                     '    def __init__(self, name):\n'
                     '        self.name = name\n'
                     '\n'
                     '    def greet(self):\n'
                     '        return f"hello {self.name}"\n'
                     '\n'
                     'print(Person("Ada").greet())',
             'output': 'hello Ada',
             'line': 40,
             'kind': 'cell'},
            {'prose': ['Use the protocol as an annotation at the API boundary. The function only cares that the object '
                       'can greet; it does not care about the concrete class.'],
             'code': 'def welcome(greeter: Greeter):\n    print(greeter.greet())\n\nwelcome(Person("Ada"))',
             'output': 'hello Ada',
             'line': 59,
             'kind': 'cell'}]},
 {'slug': 'enums',
  'title': 'Enums',
  'section': 'Types',
  'summary': 'Enum defines symbolic names for a fixed set of values.',
  'doc_url': 'https://docs.python.org/3.13/library/enum.html',
  'code': 'from enum import Enum\n'
          '\n'
          'class Status(Enum):\n'
          '    PENDING = "pending"\n'
          '    DONE = "done"\n'
          '\n'
          'current = Status.PENDING\n'
          'print(current.name)\n'
          'print(current.value)\n'
          'print(current is Status.PENDING)\n'
          'print(current == "pending")\n',
  'expected_output': 'PENDING\npending\nTrue\nFalse\n',
  'notes': ['Enums make states and choices explicit.',
            'Members have names and values.',
            'Comparing enum members avoids string typo bugs.',
            'Prefer raw strings for open-ended text; prefer enums for a closed set of named choices.'],
  'cells': [{'prose': ['An enum member has a symbolic name and an underlying value. The symbolic name is what readers '
                       'usually care about in code.'],
             'code': 'from enum import Enum\n'
                     '\n'
                     'class Status(Enum):\n'
                     '    PENDING = "pending"\n'
                     '    DONE = "done"\n'
                     '\n'
                     'current = Status.PENDING\n'
                     'print(current.name)\n'
                     'print(current.value)',
             'output': 'PENDING\npending',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Compare enum members with enum members, not with raw strings. This keeps the set of valid '
                       'states explicit.'],
             'code': 'print(current is Status.PENDING)\nprint(current == "pending")',
             'output': 'True\nFalse',
             'line': 38,
             'kind': 'cell'}]},
 {'slug': 'regular-expressions',
  'title': 'Regular Expressions',
  'section': 'Text',
  'summary': 'The re module searches and extracts text using regular expressions.',
  'doc_url': 'https://docs.python.org/3.13/library/re.html',
  'code': 'import re\n'
          '\n'
          'text = "Ada: 10, Grace: 9"\n'
          'pattern = r"([A-Za-z]+): (\\d+)"\n'
          '\n'
          'for name, score in re.findall(pattern, text):\n'
          '    print(name, int(score))\n'
          '\n'
          'match = re.search(r"Grace: (\\d+)", text)\n'
          'print(match.group(1))\n'
          'print("Grace" in text)\n',
  'expected_output': 'Ada 10\nGrace 9\n9\nTrue\n',
  'notes': ['Use raw strings for regex patterns so backslashes are easier to read.',
            'Use capturing groups when the point is extraction, not just matching.',
            'Reach for string methods before regex when the pattern is simple.'],
  'cells': [{'prose': ['Raw strings keep backslashes readable in regex patterns. Capturing groups return just the '
                       'pieces inside parentheses.'],
             'code': 'import re\n'
                     '\n'
                     'text = "Ada: 10, Grace: 9"\n'
                     'pattern = r"([A-Za-z]+): (\\d+)"\n'
                     '\n'
                     'for name, score in re.findall(pattern, text):\n'
                     '    print(name, int(score))',
             'output': 'Ada 10\nGrace 9',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['`re.search()` finds the first match. A match object exposes captured groups by position.'],
             'code': 'match = re.search(r"Grace: (\\d+)", text)\nprint(match.group(1))',
             'output': '9',
             'line': 36,
             'kind': 'cell'},
            {'prose': ['For a simple substring check, ordinary string membership is clearer than regex.'],
             'code': 'print("Grace" in text)',
             'output': 'True',
             'line': 49,
             'kind': 'cell'}]},
 {'slug': 'number-parsing',
  'title': 'Number Parsing',
  'section': 'Standard Library',
  'summary': 'int() and float() parse text into numbers and raise ValueError on bad input.',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#int',
  'code': 'print(int("42"))\n'
          'print(float("3.5"))\n'
          '\n'
          'try:\n'
          '    int("python")\n'
          'except ValueError as error:\n'
          '    print(type(error).__name__)\n',
  'expected_output': '42\n3.5\nValueError\n',
  'notes': ['`int()` and `float()` are constructors that also parse strings.',
            'Catch `ValueError` when bad user input is expected and recoverable.'],
  'cells': [{'prose': ['Use `int()` for whole numbers and `float()` for decimal text. Parsed values are real numbers, '
                       'not strings.'],
             'code': 'print(int("42"))\nprint(float("3.5"))',
             'output': '42\n3.5',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Bad numeric text raises `ValueError`. Catch that specific exception when invalid input is part '
                       'of the normal flow.'],
             'code': 'try:\n    int("python")\nexcept ValueError as error:\n    print(type(error).__name__)',
             'output': 'ValueError',
             'line': 31,
             'kind': 'cell'}]},
 {'slug': 'custom-exceptions',
  'title': 'Custom Exceptions',
  'section': 'Errors',
  'summary': 'Custom exception classes name failures that belong to your domain.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#user-defined-exceptions',
  'code': 'class EmptyCartError(Exception):\n'
          '    pass\n'
          '\n'
          'print(EmptyCartError.__name__)\n'
          '\n'
          '\n'
          'def checkout(items):\n'
          '    if not items:\n'
          '        raise EmptyCartError("cart is empty")\n'
          '    return "paid"\n'
          '\n'
          'print(checkout(["book"]))\n'
          '\n'
          'try:\n'
          '    checkout([])\n'
          'except EmptyCartError as error:\n'
          '    print(error)\n',
  'expected_output': 'EmptyCartError\npaid\ncart is empty\n',
  'notes': ['Subclass `Exception` for errors callers are expected to catch.',
            'A custom exception name can be clearer than reusing a generic `ValueError` everywhere.',
            'Catch custom exceptions at a boundary that can recover or report clearly.'],
  'cells': [{'prose': ['Create a custom exception when a failure has a name in your problem domain. The class can be '
                       'empty at first.'],
             'code': 'class EmptyCartError(Exception):\n    pass\n\nprint(EmptyCartError.__name__)',
             'output': 'EmptyCartError',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Raise the custom exception where the invalid state is detected. Normal inputs still follow the '
                       'ordinary success path.'],
             'code': 'def checkout(items):\n'
                     '    if not items:\n'
                     '        raise EmptyCartError("cart is empty")\n'
                     '    return "paid"\n'
                     '\n'
                     'print(checkout(["book"]))',
             'output': 'paid',
             'line': 32,
             'kind': 'cell'},
            {'prose': ['Callers can catch the precise error type without accidentally catching unrelated failures.'],
             'code': 'try:\n    checkout([])\nexcept EmptyCartError as error:\n    print(error)',
             'output': 'cart is empty',
             'line': 49,
             'kind': 'cell'}]},
 {'slug': 'json',
  'title': 'JSON',
  'section': 'Standard Library',
  'summary': 'json encodes Python values as JSON text and decodes them back.',
  'doc_url': 'https://docs.python.org/3.13/library/json.html',
  'code': 'import json\n'
          '\n'
          'payload = {"language": "Python", "versions": [3, 13], "stable": True, "missing": None}\n'
          'text = json.dumps(payload, sort_keys=True)\n'
          'print(text)\n'
          '\n'
          'pretty = json.dumps({"language": "Python", "stable": True}, indent=2, sort_keys=True)\n'
          'print(pretty.splitlines()[0])\n'
          'print(pretty.splitlines()[1])\n'
          '\n'
          'decoded = json.loads(text)\n'
          'print(decoded["language"])\n'
          'print(decoded["missing"] is None)\n'
          '\n'
          'try:\n'
          '    json.loads("{bad json}")\n'
          'except json.JSONDecodeError as error:\n'
          '    print(error.__class__.__name__)\n',
  'expected_output': '{"language": "Python", "missing": null, "stable": true, "versions": [3, 13]}\n'
                     '{\n'
                     '  "language": "Python",\n'
                     'Python\n'
                     'True\n'
                     'JSONDecodeError\n',
  'notes': ['`dumps()` returns a string; `loads()` accepts a string.',
            'JSON `true`, `false`, and `null` become Python `True`, `False`, and `None`.',
            'Use `sort_keys=True` when stable text output matters.',
            'JSON only represents data shapes, not arbitrary Python objects or behavior.'],
  'cells': [{'prose': ['`dumps()` encodes Python data as JSON text. `sort_keys=True` keeps dictionary keys in a stable '
                       'order for reproducible output.'],
             'code': 'import json\n'
                     '\n'
                     'payload = {"language": "Python", "versions": [3, 13], "stable": True, "missing": None}\n'
                     'text = json.dumps(payload, sort_keys=True)\n'
                     'print(text)',
             'output': '{"language": "Python", "missing": null, "stable": true, "versions": [3, 13]}',
             'line': 22,
             'kind': 'cell'},
            {'prose': ['Formatting options change the JSON text, not the Python value. `indent=2` is useful for '
                       'human-readable output.'],
             'code': 'pretty = json.dumps({"language": "Python", "stable": True}, indent=2, sort_keys=True)\n'
                     'print(pretty.splitlines()[0])\n'
                     'print(pretty.splitlines()[1])',
             'output': '{\n  "language": "Python",',
             'line': 38,
             'kind': 'cell'},
            {'prose': ['`loads()` decodes JSON text back into Python values. JSON `null` becomes Python `None`.'],
             'code': 'decoded = json.loads(text)\nprint(decoded["language"])\nprint(decoded["missing"] is None)',
             'output': 'Python\nTrue',
             'line': 53,
             'kind': 'cell'},
            {'prose': ['Invalid JSON raises `JSONDecodeError`, so input boundaries should handle decode failures '
                       'explicitly.'],
             'code': 'try:\n'
                     '    json.loads("{bad json}")\n'
                     'except json.JSONDecodeError as error:\n'
                     '    print(error.__class__.__name__)',
             'output': 'JSONDecodeError',
             'line': 68,
             'kind': 'cell'}]},
 {'slug': 'logging',
  'title': 'Logging',
  'section': 'Standard Library',
  'summary': 'logging records operational events without using print as infrastructure.',
  'doc_url': 'https://docs.python.org/3.13/library/logging.html',
  'code': 'import logging\n'
          'import sys\n'
          '\n'
          'logger = logging.getLogger("example")\n'
          'logger.setLevel(logging.INFO)\n'
          'handler = logging.StreamHandler(sys.stdout)\n'
          'handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))\n'
          'logger.handlers[:] = [handler]\n'
          '\n'
          'logger.debug("hidden")\n'
          'logger.info("service started")\n'
          'logger.warning("disk almost full")\n',
  'expected_output': 'INFO:service started\nWARNING:disk almost full\n',
  'notes': ['Loggers name where an event came from.',
            'Handlers decide where records go.',
            'Levels let operators choose how much detail to see.'],
  'cells': [{'prose': ['Loggers name where an event came from.'],
             'code': 'import logging\n'
                     'import sys\n'
                     '\n'
                     'logger = logging.getLogger("example")\n'
                     'logger.setLevel(logging.INFO)\n'
                     'handler = logging.StreamHandler(sys.stdout)\n'
                     'handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))\n'
                     'logger.handlers[:] = [handler]\n'
                     '\n'
                     'logger.debug("hidden")\n'
                     'logger.info("service started")\n'
                     'logger.warning("disk almost full")',
             'output': 'INFO:service started\nWARNING:disk almost full',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'testing',
  'title': 'Testing',
  'section': 'Standard Library',
  'summary': 'Tests make expected behavior executable and repeatable.',
  'doc_url': 'https://docs.python.org/3.13/library/unittest.html',
  'code': 'import io\n'
          'import unittest\n'
          '\n'
          '\n'
          'def add(left, right):\n'
          '    return left + right\n'
          '\n'
          'class AddTests(unittest.TestCase):\n'
          '    def test_adds_numbers(self):\n'
          '        self.assertEqual(add(2, 3), 5)\n'
          '\n'
          '    def test_adds_empty_strings(self):\n'
          '        self.assertEqual(add("", "py"), "py")\n'
          '\n'
          'suite = unittest.defaultTestLoader.loadTestsFromTestCase(AddTests)\n'
          'stream = io.StringIO()\n'
          'result = unittest.TextTestRunner(stream=stream, verbosity=0).run(suite)\n'
          'print(result.testsRun)\n'
          'print(result.wasSuccessful())\n',
  'expected_output': '2\nTrue\n',
  'notes': ['Test method names should describe behavior, not implementation details.',
            'A good unit test is deterministic and independent of test order.',
            'Use broader integration tests when the behavior depends on several components working together.'],
  'cells': [{'prose': ['A test starts with behavior small enough to name. The function can be ordinary code; the test '
                       'supplies a representative input and expected result.'],
             'code': 'def add(left, right):\n    return left + right\n\nprint(add(2, 3))',
             'output': '5',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['`unittest.TestCase` groups test methods. Assertion methods such as `assertEqual` make the '
                       'expected behavior explicit.'],
             'code': 'import unittest\n'
                     '\n'
                     'class AddTests(unittest.TestCase):\n'
                     '    def test_adds_numbers(self):\n'
                     '        self.assertEqual(add(2, 3), 5)\n'
                     '\n'
                     '    def test_adds_empty_strings(self):\n'
                     '        self.assertEqual(add("", "py"), "py")\n'
                     '\n'
                     'print([name for name in dir(AddTests) if name.startswith("test_")])',
             'output': "['test_adds_empty_strings', 'test_adds_numbers']",
             'line': 32,
             'kind': 'cell'},
            {'prose': ['A runner executes the suite and records whether every assertion passed. Capturing the runner '
                       "stream keeps this page's output deterministic."],
             'code': 'import io\n'
                     '\n'
                     'suite = unittest.defaultTestLoader.loadTestsFromTestCase(AddTests)\n'
                     'stream = io.StringIO()\n'
                     'result = unittest.TextTestRunner(stream=stream, verbosity=0).run(suite)\n'
                     'print(result.testsRun)\n'
                     'print(result.wasSuccessful())',
             'output': '2\nTrue',
             'line': 53,
             'kind': 'cell'}]},
 {'slug': 'subprocesses',
  'title': 'Subprocesses',
  'section': 'Standard Library',
  'summary': 'subprocess runs external commands with explicit arguments and captured outputs.',
  'doc_url': 'https://docs.python.org/3.13/library/subprocess.html',
  'code': 'import subprocess\n'
          'import sys\n'
          '\n'
          'result = subprocess.run(\n'
          '    [sys.executable, "-c", "print(\'child process\')"],\n'
          '    text=True,\n'
          '    capture_output=True,\n'
          '    check=True,\n'
          ')\n'
          '\n'
          'print(result.stdout.strip())\n'
          'print(result.returncode)\n',
  'expected_output': 'child process\n0\n',
  'notes': ['Use a list of arguments instead of shell strings when possible.',
            'Capture output when the parent program needs to inspect it.',
            '`check=True` turns non-zero exits into exceptions.'],
  'cells': [{'prose': ['Dynamic Workers do not provide child processes.'],
             'code': 'result = subprocess.run(\n'
                     '    [sys.executable, "-c", "print(\'child process\')"],\n'
                     '    text=True,\n'
                     '    capture_output=True,\n'
                     '    check=True,\n'
                     ')',
             'output': '',
             'line': 18,
             'kind': 'unsupported'},
            {'prose': ['`subprocess.run()` starts a child process and waits for it. `capture_output=True` stores the '
                       "child's standard output and error streams on the result object."],
             'code': 'import subprocess\n'
                     'import sys\n'
                     '\n'
                     'result = subprocess.run(\n'
                     '    [sys.executable, "-c", "print(\'child process\')"],\n'
                     '    text=True,\n'
                     '    capture_output=True,\n'
                     '    check=True,\n'
                     ')\n'
                     '\n'
                     'print(result.stdout.strip())\n'
                     'print(result.returncode)',
             'output': 'child process\n0',
             'line': 31,
             'kind': 'cell'}]},
 {'slug': 'threads-and-processes',
  'title': 'Threads and Processes',
  'section': 'Standard Library',
  'summary': 'Threads share memory, while processes run in separate interpreters.',
  'doc_url': 'https://docs.python.org/3.13/library/concurrent.futures.html',
  'code': 'from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor\n'
          '\n'
          '\n'
          'def square(number):\n'
          '    return number * number\n'
          '\n'
          'with ThreadPoolExecutor(max_workers=2) as pool:\n'
          '    print(list(pool.map(square, [1, 2, 3])))\n'
          '\n'
          'print(ProcessPoolExecutor.__name__)\n',
  'expected_output': '[1, 4, 9]\nProcessPoolExecutor\n',
  'notes': ['Threads share memory, so mutable shared state needs care.',
            'Processes avoid shared interpreter state but require values to cross a process boundary.',
            'Prefer `asyncio` for coroutine-based I/O and executors for ordinary blocking callables.'],
  'cells': [{'prose': ['Dynamic Workers do not provide native threads or child processes.'],
             'code': 'with ThreadPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(square, [1, 2, 3])))\n'
                     '\n'
                     'with ProcessPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(pow, [4, 5], [2, 2])))',
             'output': '',
             'line': 18,
             'kind': 'unsupported'},
            {'prose': ['A thread pool runs ordinary callables while sharing memory with the current process. `map()` '
                       'returns results in input order.'],
             'code': 'from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor\n'
                     '\n'
                     '\n'
                     'def square(number):\n'
                     '    return number * number\n'
                     '\n'
                     'with ThreadPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(square, [1, 2, 3])))',
             'output': '[1, 4, 9]',
             'line': 30,
             'kind': 'cell'},
            {'prose': ['A process pool uses separate Python processes. That boundary is heavier, but it can run '
                       'CPU-bound work outside the current interpreter.'],
             'code': 'print(ProcessPoolExecutor.__name__)',
             'output': 'ProcessPoolExecutor',
             'line': 49,
             'kind': 'cell'}]},
 {'slug': 'networking',
  'title': 'Networking',
  'section': 'Standard Library',
  'summary': 'Networking code exchanges bytes across explicit protocol boundaries.',
  'doc_url': 'https://docs.python.org/3.13/library/socket.html',
  'code': 'import socket\n'
          '\n'
          'left, right = socket.socketpair()\n'
          'try:\n'
          '    message = "ping"\n'
          '    left.sendall(message.encode("utf-8"))\n'
          '    data = right.recv(16)\n'
          '    print(data)\n'
          '    print(data.decode("utf-8"))\n'
          'finally:\n'
          '    left.close()\n'
          '    right.close()\n',
  'expected_output': "b'ping'\nping\n",
  'notes': ['Network protocols move bytes, not Python `str` objects.',
            'Close real sockets when finished, usually with a context manager or `finally` block.',
            'Use high-level HTTP libraries for application HTTP unless socket-level control is the lesson.'],
  'cells': [{'prose': ['Dynamic Workers do not provide arbitrary low-level sockets, and this app disables Dynamic '
                       'Worker outbound access.'],
             'code': 'left, right = socket.socketpair()\nleft.sendall("ping".encode("utf-8"))\ndata = right.recv(16)',
             'output': '',
             'line': 18,
             'kind': 'unsupported'},
            {'prose': ['Sockets exchange bytes. Encoding and decoding make the boundary between Python text and '
                       'network data visible.'],
             'code': 'import socket\n'
                     '\n'
                     'left, right = socket.socketpair()\n'
                     'try:\n'
                     '    message = "ping"\n'
                     '    left.sendall(message.encode("utf-8"))\n'
                     '    data = right.recv(16)\n'
                     '    print(data)\n'
                     '    print(data.decode("utf-8"))\n'
                     'finally:\n'
                     '    left.close()\n'
                     '    right.close()',
             'output': "b'ping'\nping",
             'line': 28,
             'kind': 'cell'}]},
 {'slug': 'datetime',
  'title': 'Dates and Times',
  'section': 'Standard Library',
  'summary': 'datetime represents dates, times, durations, formatting, and parsing.',
  'doc_url': 'https://docs.python.org/3.13/library/datetime.html',
  'code': 'from datetime import date, datetime, time, timedelta, timezone\n'
          '\n'
          'release_day = date(2026, 5, 4)\n'
          'meeting_time = time(12, 30)\n'
          'created_at = datetime.combine(release_day, meeting_time, tzinfo=timezone.utc)\n'
          '\n'
          'print(release_day.isoformat())\n'
          'print(meeting_time.isoformat())\n'
          'print(created_at.isoformat())\n'
          '\n'
          'expires_at = created_at + timedelta(days=7, hours=2)\n'
          'print(expires_at.isoformat())\n'
          '\n'
          'print(created_at.strftime("%Y-%m-%d %H:%M %Z"))\n'
          'parsed = datetime.fromisoformat("2026-05-04T12:30:00+00:00")\n'
          'print(parsed == created_at)\n',
  'expected_output': '2026-05-04\n'
                     '12:30:00\n'
                     '2026-05-04T12:30:00+00:00\n'
                     '2026-05-11T14:30:00+00:00\n'
                     '2026-05-04 12:30 UTC\n'
                     'True\n',
  'notes': ['Use timezone-aware datetimes for instants that cross system or user boundaries.',
            'Use `date` for calendar days, `time` for clock times, `datetime` for both, and `timedelta` for durations.',
            'Prefer ISO 8601 strings for interchange; use `strftime` for human-facing display.'],
  'cells': [{'prose': ['The `datetime` module separates calendar dates, clock times, combined datetimes, and '
                       'durations. Import the types you need explicitly.',
                       'Use `date` for a calendar day and `time` for a time of day. Combine them into a timezone-aware '
                       '`datetime` when you mean an instant.',
                       '`isoformat()` produces stable machine-readable text. It is a good default for examples, APIs, '
                       'and logs.'],
             'code': 'from datetime import date, datetime, time, timedelta, timezone\n'
                     '\n'
                     'release_day = date(2026, 5, 4)\n'
                     'meeting_time = time(12, 30)\n'
                     'created_at = datetime.combine(release_day, meeting_time, tzinfo=timezone.utc)\n'
                     '\n'
                     'print(release_day.isoformat())\n'
                     'print(meeting_time.isoformat())\n'
                     'print(created_at.isoformat())',
             'output': '2026-05-04\n12:30:00\n2026-05-04T12:30:00+00:00',
             'line': 17,
             'kind': 'cell'},
            {'prose': ['Use `timedelta` for durations. Adding one to a `datetime` produces another `datetime` without '
                       'manually changing calendar fields.'],
             'code': 'expires_at = created_at + timedelta(days=7, hours=2)\nprint(expires_at.isoformat())',
             'output': '2026-05-11T14:30:00+00:00',
             'line': 43,
             'kind': 'cell'},
            {'prose': ['Use `strftime()` for human-facing formatting and `fromisoformat()` when reading ISO 8601 text '
                       'back into a `datetime`.'],
             'code': 'print(created_at.strftime("%Y-%m-%d %H:%M %Z"))\n'
                     'parsed = datetime.fromisoformat("2026-05-04T12:30:00+00:00")\n'
                     'print(parsed == created_at)',
             'output': '2026-05-04 12:30 UTC\nTrue',
             'line': 56,
             'kind': 'cell'}]},
 {'slug': 'csv-data',
  'title': 'CSV Data',
  'section': 'Standard Library',
  'summary': 'csv reads and writes row-shaped text data.',
  'doc_url': 'https://docs.python.org/3.13/library/csv.html',
  'code': 'import csv\n'
          'import io\n'
          '\n'
          'text = "name,score\\nAda,98\\nGrace,95\\n"\n'
          'reader = csv.DictReader(io.StringIO(text))\n'
          'rows = list(reader)\n'
          '\n'
          'print(rows[0]["name"])\n'
          'print(sum(int(row["score"]) for row in rows))\n'
          '\n'
          'output = io.StringIO()\n'
          'writer = csv.DictWriter(output, fieldnames=["name", "passed"])\n'
          'writer.writeheader()\n'
          'writer.writerow({"name": "Ada", "passed": True})\n'
          'print(output.getvalue().splitlines()[1])\n',
  'expected_output': 'Ada\n193\nAda,True\n',
  'notes': ['Use `DictReader` when column names should become dictionary keys.',
            'CSV fields arrive as text, so convert numbers explicitly.',
            '`DictWriter` writes dictionaries back to row-shaped text.'],
  'cells': [{'prose': ['Use `DictReader` when column names should become dictionary keys.'],
             'code': 'import csv\n'
                     'import io\n'
                     '\n'
                     'text = "name,score\\nAda,98\\nGrace,95\\n"\n'
                     'reader = csv.DictReader(io.StringIO(text))\n'
                     'rows = list(reader)\n'
                     '\n'
                     'print(rows[0]["name"])\n'
                     'print(sum(int(row["score"]) for row in rows))\n'
                     '\n'
                     'output = io.StringIO()\n'
                     'writer = csv.DictWriter(output, fieldnames=["name", "passed"])\n'
                     'writer.writeheader()\n'
                     'writer.writerow({"name": "Ada", "passed": True})\n'
                     'print(output.getvalue().splitlines()[1])',
             'output': 'Ada\n193\nAda,True',
             'line': 17,
             'kind': 'cell'}]},
 {'slug': 'async-await',
  'title': 'Async Await',
  'section': 'Async',
  'summary': 'async def creates coroutines, and await pauses until awaitable work completes.',
  'doc_url': 'https://docs.python.org/3.13/library/asyncio-task.html',
  'code': 'import asyncio\n'
          '\n'
          'async def fetch_title(slug):\n'
          '    await asyncio.sleep(0)\n'
          '    return slug.replace("-", " ").title()\n'
          '\n'
          'async def main():\n'
          '    title = await fetch_title("async-await")\n'
          '    print(title)\n'
          '    titles = await asyncio.gather(fetch_title("json"), fetch_title("datetime"))\n'
          '    print(titles)\n'
          '\n'
          'asyncio.run(main())\n',
  'expected_output': "Async Await\n['Json', 'Datetime']\n",
  'notes': ['Calling an async function creates a coroutine object.',
            '`await` yields control until an awaitable completes.',
            'Workers request handlers are async, so this pattern appears around fetches and bindings.',
            'Prefer ordinary functions when there is no awaitable work to coordinate.'],
  'cells': [{'prose': ['An `async def` function returns a coroutine object when called. The function body has not '
                       'produced its final result yet.'],
             'code': 'import asyncio\n'
                     '\n'
                     'async def fetch_title(slug):\n'
                     '    await asyncio.sleep(0)\n'
                     '    return slug.replace("-", " ").title()\n'
                     '\n'
                     'coroutine = fetch_title("async-await")\n'
                     'print(coroutine.__class__.__name__)\n'
                     'coroutine.close()',
             'output': 'coroutine',
             'line': 19,
             'kind': 'cell'},
            {'prose': ['Use `await` inside another coroutine to get the eventual result. `asyncio.run()` starts an '
                       'event loop for the top-level coroutine.'],
             'code': 'async def main():\n'
                     '    title = await fetch_title("async-await")\n'
                     '    print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': 'Async Await',
             'line': 39,
             'kind': 'cell'},
            {'prose': ['`asyncio.gather()` awaits several awaitables and returns their results in order. This is the '
                       'shape used when independent I/O operations can progress together.'],
             'code': 'async def main():\n'
                     '    titles = await asyncio.gather(fetch_title("json"), fetch_title("datetime"))\n'
                     '    print(titles)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': "['Json', 'Datetime']",
             'line': 55,
             'kind': 'cell'}]},
 {'slug': 'async-iteration-and-context',
  'title': 'Async Iteration and Context',
  'section': 'Async',
  'summary': 'async for and async with consume asynchronous streams and cleanup protocols.',
  'doc_url': 'https://docs.python.org/3.13/reference/compound_stmts.html#async-for',
  'code': 'import asyncio\n'
          '\n'
          'async def titles():\n'
          '    for slug in ["values", "async-await"]:\n'
          '        await asyncio.sleep(0)\n'
          '        yield slug.replace("-", " ").title()\n'
          '\n'
          'class Session:\n'
          '    async def __aenter__(self):\n'
          '        print("open")\n'
          '        return self\n'
          '\n'
          '    async def __aexit__(self, exc_type, exc, tb):\n'
          '        print("close")\n'
          '\n'
          'async def main():\n'
          '    async with Session():\n'
          '        async for title in titles():\n'
          '            print(title)\n'
          '\n'
          'asyncio.run(main())\n',
  'expected_output': 'open\nValues\nAsync Await\nclose\n',
  'notes': ['`async for` consumes asynchronous iterators.',
            '`async with` awaits asynchronous setup and cleanup.',
            'These forms are common around I/O-shaped resources.'],
  'cells': [{'prose': ['An async generator can `await` before yielding each value. `async for` consumes those values '
                       'with the asynchronous iteration protocol.'],
             'code': 'import asyncio\n'
                     '\n'
                     'async def titles():\n'
                     '    for slug in ["values", "async-await"]:\n'
                     '        await asyncio.sleep(0)\n'
                     '        yield slug.replace("-", " ").title()\n'
                     '\n'
                     'print(titles.__name__)',
             'output': 'titles',
             'line': 24,
             'kind': 'cell'},
            {'prose': ['An async context manager defines `__aenter__` and `__aexit__`. `async with` awaits setup and '
                       'cleanup around the block.'],
             'code': 'class Session:\n'
                     '    async def __aenter__(self):\n'
                     '        print("open")\n'
                     '        return self\n'
                     '\n'
                     '    async def __aexit__(self, exc_type, exc, tb):\n'
                     '        print("close")\n'
                     '\n'
                     'print(Session.__name__)',
             'output': 'Session',
             'line': 43,
             'kind': 'cell'},
            {'prose': ['The top-level coroutine combines both protocols: open the async resource, then consume the '
                       'async stream inside it.'],
             'code': 'async def main():\n'
                     '    async with Session():\n'
                     '        async for title in titles():\n'
                     '            print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': 'open\nValues\nAsync Await\nclose',
             'line': 63,
             'kind': 'cell'}]}]
