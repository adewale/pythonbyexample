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
             'line': 17}]},
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
             'line': 17},
            {'prose': ['Methods and operators evaluate to new values. The original `text`, `count`, and `ratio` '
                       'bindings remain ordinary objects you can reuse.'],
             'code': 'print(text.upper())\nprint(count + 4)\nprint(ratio * 2)',
             'output': 'PYTHON\n7\n5.0',
             'line': 35},
            {'prose': ['Boolean expressions combine facts, and `None` is checked by identity because it is a singleton '
                       'absence marker.'],
             'code': 'print(ready and count > 0)\nprint(missing is None)',
             'output': 'True\nTrue',
             'line': 51}]},
 {'slug': 'numbers',
  'title': 'Numbers',
  'section': 'Basics',
  'summary': 'Python numbers include integers and floating-point values.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#numeric-types-int-float-complex',
  'code': 'count = 10\n'
          'ratio = 0.25\n'
          '\n'
          'print(count + 5)\n'
          'print(count / 4)\n'
          'print(count // 4)\n'
          'print(count % 4)\n'
          'print(2 ** 5)\n'
          'print(round(3.14159, 2))\n',
  'expected_output': '15\n2.5\n2\n2\n32\n3.14\n',
  'notes': ["Python's `int` has arbitrary precision; it grows as large as memory allows.",
            "Python's `float` is the usual double-precision floating-point type; core Python does not expose separate "
            '`float32` and `float64` syntax.',
            'Use `/` for true division and `//` for floor division.'],
  'cells': [{'prose': ['Python has `int` for whole numbers and `float` for floating-point numbers. You usually write '
                       'them directly as literals.',
                       'Arithmetic operators return new numeric values. True division with `/` returns a `float`, even '
                       'when both inputs are integers.'],
             'code': 'count = 10\nratio = 0.25\n\nprint(count + 5)\nprint(count / 4)',
             'output': '15\n2.5',
             'line': 17},
            {'prose': ['Floor division and modulo are useful when you need quotient and remainder behavior. Powers use '
                       '`**`, not `^`.'],
             'code': 'print(count // 4)\nprint(count % 4)\nprint(2 ** 5)',
             'output': '2\n2\n32',
             'line': 36},
            {'prose': ['Floating-point values are approximate, so examples often round display output when the lesson '
                       'is about presentation rather than precision.'],
             'code': 'print(round(3.14159, 2))',
             'output': '3.14',
             'line': 52}]},
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
             'line': 17},
            {'prose': ['Comparisons produce booleans too, so they compose naturally with logical operators in '
                       'conditions and validation checks.'],
             'code': 'name = "Ada"\nprint(name == "Ada" and len(name) > 0)',
             'output': 'True',
             'line': 38}]},
 {'slug': 'operators-and-literals',
  'title': 'Operators and Literals',
  'section': 'Basics',
  'summary': 'Python has specialized operators and literal forms for particular data shapes.',
  'doc_url': 'https://docs.python.org/3.13/reference/lexical_analysis.html#literals',
  'code': 'pattern = r"\\d+"\n'
          'data = b"py"\n'
          'number = 2 + 3j\n'
          'print(pattern)\n'
          'print(data)\n'
          'print(number.real)\n'
          '\n'
          'flags = 0b0011\n'
          'print(flags ^ 0b0101)\n'
          'print(flags << 1)\n'
          'print(~0)\n'
          'print(sorted({"python", "go"} ^ {"go", "rust"}))\n'
          '\n'
          'class Scale:\n'
          '    def __init__(self, value):\n'
          '        self.value = value\n'
          '\n'
          '    def __matmul__(self, other):\n'
          '        return self.value * other.value\n'
          '\n'
          'print(Scale(2) @ Scale(3))\n'
          'print(...)\n',
  'expected_output': "\\d+\nb'py'\n2.0\n6\n6\n-1\n['python', 'rust']\n6\nEllipsis\n",
  'notes': ['Raw strings are useful when backslashes are part of the data, such as regular expressions.',
            'Bytes literals represent binary data, not text strings.',
            'Prefer everyday strings, numbers, and operators until the data shape calls for these specialized forms.',
            'Specialized operators should make the data model clearer, not more mysterious.'],
  'cells': [{'prose': ['Raw strings keep backslashes literal, bytes literals store binary data, and complex literals '
                       'use `j` for the imaginary part.'],
             'code': 'pattern = r"\\d+"\n'
                     'data = b"py"\n'
                     'number = 2 + 3j\n'
                     'print(pattern)\n'
                     'print(data)\n'
                     'print(number.real)',
             'output': "\\d+\nb'py'\n2.0",
             'line': 22},
            {'prose': ['Bit operators work on integers and some collection types. For sets, `^` means symmetric '
                       'difference: values in either set but not both.'],
             'code': 'flags = 0b0011\n'
                     'print(flags ^ 0b0101)\n'
                     'print(flags << 1)\n'
                     'print(~0)\n'
                     'print(sorted({"python", "go"} ^ {"go", "rust"}))',
             'output': "6\n6\n-1\n['python', 'rust']",
             'line': 41},
            {'prose': ['The `@` operator calls `__matmul__` on custom objects. `...` is the `Ellipsis` literal, '
                       'commonly used as a placeholder in stubs and slicing APIs.'],
             'code': 'class Scale:\n'
                     '    def __init__(self, value):\n'
                     '        self.value = value\n'
                     '\n'
                     '    def __matmul__(self, other):\n'
                     '        return self.value * other.value\n'
                     '\n'
                     'print(Scale(2) @ Scale(3))\n'
                     'print(...)',
             'output': '6\nEllipsis',
             'line': 60}]},
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
             'line': 17},
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
             'line': 30},
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
             'line': 48}]},
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
             'line': 19},
            {'prose': ['Assignment can rebind the same name to a different value. The name is not permanently attached '
                       'to the first object.'],
             'code': 'message = "hello"\nprint(message)',
             'output': 'hello',
             'line': 32},
            {'prose': ['Augmented assignment reads the current binding, computes an updated value, and stores the '
                       'result back under the same name.'],
             'code': 'count = 3\ncount += 1\nprint(count)',
             'output': '4',
             'line': 45}]},
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
             'line': 17},
            {'prose': ['Constants are useful for configuration values that should be named once and reused instead of '
                       'repeated as magic literals.'],
             'code': 'print(API_VERSION)',
             'output': '2026-05',
             'line': 37}]},
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
             'line': 17},
            {'prose': ['Use truthiness when it reads naturally, but choose explicit comparisons when the distinction '
                       'matters, such as checking whether a value is exactly None.'],
             'code': 'if name:\n    print("has a name")',
             'output': 'has a name',
             'line': 35},
            {'prose': ['Use truthiness when it reads naturally, but choose explicit comparisons when the distinction '
                       'matters, such as checking whether a value is exactly None.'],
             'code': 'print(bool(0))\nprint(bool(42))',
             'output': 'False\nTrue',
             'line': 48}]},
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
             'line': 17},
            {'prose': ['Identity matters when objects are mutable. `same` is another name for `left`, so mutating '
                       'through one name changes the object seen through the other.'],
             'code': 'same = left\nsame.append(4)\nprint(left)\nprint(same is left)',
             'output': '[1, 2, 3, 4]\nTrue',
             'line': 33},
            {'prose': ['Use `is` for singleton identity checks such as `None`. This asks whether the value is the one '
                       'special `None` object.'],
             'code': 'value = None\nprint(value is None)',
             'output': 'True',
             'line': 49}]},
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
             'line': 17},
            {'prose': ['Immutable objects do not change in place. String methods such as `upper()` return a new '
                       'string, leaving the original string unchanged.'],
             'code': 'text = "python"\nupper_text = text.upper()\nprint(text)\nprint(upper_text)',
             'output': 'python\nPYTHON',
             'line': 34},
            {'prose': ['Some APIs make the boundary explicit. `sorted()` returns a new list, while methods such as '
                       '`append()` and `list.sort()` mutate an existing list.'],
             'code': 'numbers = [3, 1, 2]\nordered = sorted(numbers)\nprint(ordered)\nprint(numbers)',
             'output': '[1, 2, 3]\n[3, 1, 2]',
             'line': 50}]},
 {'slug': 'strings',
  'title': 'Strings',
  'section': 'Text',
  'summary': 'Strings are immutable Unicode text sequences.',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#text-sequence-type-str',
  'code': 'language = "Python"\n'
          'message = "  Python by Example  "\n'
          '\n'
          'print(language[0])\n'
          'print(language.lower())\n'
          'print(message.strip())\n'
          'print(f"Hello, {language}!")\n'
          'print(", ".join(["lists", "dicts", "sets"]))\n',
  'expected_output': 'P\npython\nPython by Example\nHello, Python!\nlists, dicts, sets\n',
  'notes': ['Strings are sequences of Unicode characters, so indexing and many sequence operations work.',
            'String methods return new strings because strings are immutable.',
            'Use `join()` when building text from many pieces; it makes the separator explicit.'],
  'cells': [{'prose': ['Strings store Unicode text and can be indexed like other sequences.'],
             'code': 'language = "Python"\nmessage = "  Python by Example  "\n\nprint(language[0])',
             'output': 'P',
             'line': 17},
            {'prose': ['Methods such as `lower()` and `strip()` return transformed strings. They do not mutate the '
                       'original value.'],
             'code': 'print(language.lower())\nprint(message.strip())',
             'output': 'python\nPython by Example',
             'line': 32},
            {'prose': ['Use f-strings for readable interpolation and `join()` when a separator belongs between several '
                       'pieces.'],
             'code': 'print(f"Hello, {language}!")\nprint(", ".join(["lists", "dicts", "sets"]))',
             'output': 'Hello, Python!\nlists, dicts, sets',
             'line': 46}]},
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
             'line': 17},
            {'prose': ['Format specifications after `:` control display without changing the underlying values. Here '
                       'the rank is right-aligned, the name is left-aligned, and the score is padded to one decimal '
                       'place.'],
             'code': 'row = f"{rank:>2} | {name:<8} | {score:05.1f}"\nprint(row)',
             'output': ' 1 | Ada      | 009.5',
             'line': 34},
            {'prose': ['The debug form with `=` is useful while learning or logging because it prints both the '
                       'expression and the value.'],
             'code': 'print(f"{score = }")',
             'output': 'score = 9.5',
             'line': 47}]},
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
             'line': 17},
            {'prose': ['Truthiness is part of conditional flow. Empty collections are false, so `if items:` reads as '
                       '“if there is anything to work with.”'],
             'code': 'items = ["coat", "hat"]\nif items:\n    print(f"packing {len(items)} items")',
             'output': 'packing 2 items',
             'line': 38},
            {'prose': ['Use the ternary expression when you are choosing a value. If either side needs multiple '
                       'statements, use a normal `if` block instead.'],
             'code': 'status = "ok" if temperature < 90 else "danger"\nprint(status)',
             'output': 'ok',
             'line': 52}]},
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
             'line': 22},
            {'prose': ['The same idea works in loops that read state until a sentinel appears. The assignment and '
                       'comparison stay together.'],
             'code': 'queue = ["retry", "ok"]\n'
                     'while (status := queue.pop(0)) != "ok":\n'
                     '    print(status)\n'
                     'print(status)',
             'output': 'retry\nok',
             'line': 39}]},
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
             'line': 17},
            {'prose': ['range() is itself an iterable that produces numbers lazily. Use it when you need a sequence of '
                       'integers, but prefer direct iteration when you already have a collection.'],
             'code': 'for number in range(3):\n    print(number)',
             'output': '0\n1\n2',
             'line': 32}]},
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
             'line': 22},
            {'prose': ['`break` exits the loop immediately. The value after `stop` is never processed because the loop '
                       'has already ended.'],
             'code': 'commands = ["load", "save", "stop", "delete"]\n'
                     'for command in commands:\n'
                     '    if command == "stop":\n'
                     '        break\n'
                     '    print(command)',
             'output': 'load\nsave',
             'line': 39}]},
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
             'line': 22},
            {'prose': ['If the loop finishes without `break`, the `else` block runs. This branch means the search '
                       'examined every value and found nothing.'],
             'code': 'for name in names:\n'
                     '    if name == "Linus":\n'
                     '        print("found")\n'
                     '        break\n'
                     'else:\n'
                     '    print("missing")',
             'output': 'missing',
             'line': 41}]},
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
             'line': 17},
            {'prose': ['When you need both a position and a value, use `enumerate()`. It produces index/value pairs '
                       'without manual indexing.'],
             'code': 'for index, name in enumerate(names):\n    print(index, name)',
             'output': '0 Ada\n1 Grace\n2 Guido',
             'line': 36},
            {'prose': ['Dictionaries are iterable too, but `dict.items()` is the clearest way to say that the loop '
                       'needs keys and values together.'],
             'code': 'scores = {"Ada": 10, "Grace": 9}\nfor name, score in scores.items():\n    print(name, score)',
             'output': 'Ada 10\nGrace 9',
             'line': 51}]},
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
             'line': 17},
            {'prose': ['A `for` loop consumes the same iterator protocol. Because two values were already consumed, '
                       'the loop sees only the remaining value.'],
             'code': 'for name in iterator:\n    print(name)',
             'output': 'Guido',
             'line': 33},
            {'prose': ['The list itself is reusable. Asking it for a fresh iterator starts a new pass over the same '
                       'stored values.'],
             'code': 'again = iter(names)\nprint(next(again))',
             'output': 'Ada',
             'line': 46}]},
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
             'line': 17},
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
             'line': 33},
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
             'line': 51}]},
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
             'line': 22},
            {'prose': ['An OR pattern accepts several alternatives in one case. A star pattern captures the rest of a '
                       'sequence.'],
             'code': 'print(describe(["exit"]))\nprint(describe(["echo", "hello", "python"]))',
             'output': 'stop\nhello python',
             'line': 45},
            {'prose': ['The wildcard `_` catches values that did not match earlier cases. Here the guard rejects the '
                       'negative coordinate.'],
             'code': 'print(describe(["move", -1, 3]))',
             'output': 'unknown',
             'line': 59}]},
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
             'line': 17},
            {'prose': ['A sentinel loop stops when a special value appears. The loop does not know in advance how many '
                       'retries it will need; it keeps going until the state says to stop.'],
             'code': 'responses = iter(["retry", "retry", "ok"])\n'
                     'status = next(responses)\n'
                     'while status != "ok":\n'
                     '    print(f"status: {status}")\n'
                     '    status = next(responses)\n'
                     'print(f"status: {status}")',
             'output': 'status: retry\nstatus: retry\nstatus: ok',
             'line': 36}]},
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
             'line': 17},
            {'prose': ['Use indexes to read positions. Negative indexes are convenient for reading from the end.'],
             'code': 'print(numbers[0])\nprint(numbers[-1])',
             'output': '3\n1',
             'line': 32},
            {'prose': ['Use `sorted()` when you want an ordered copy and still need the original order afterward.'],
             'code': 'print(sorted(numbers))\nprint(numbers)',
             'output': '[1, 1, 3, 4]\n[3, 1, 4, 1]',
             'line': 46}]},
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
             'line': 17},
            {'prose': ['Tuples are sequences, so indexing and `len()` work. They are different from lists because '
                       'their length and item references are fixed after creation.'],
             'code': 'red = (255, 0, 0)\nprint(red[0])\nprint(len(red))',
             'output': '255\n3',
             'line': 31},
            {'prose': ['Tuples pair naturally with multiple return values and unpacking. If the fields need names '
                       'everywhere, graduate to a dataclass or named tuple.'],
             'code': 'record = ("Ada", 10)\nname, score = record\nprint(f"{name}: {score}")',
             'output': 'Ada: 10',
             'line': 46}]},
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
             'line': 17},
            {'prose': ['Starred unpacking handles variable-length sequences by collecting the middle or remaining '
                       'values. This keeps common head-tail patterns readable.'],
             'code': 'first, *middle, last = [1, 2, 3, 4]\nprint(first, middle, last)',
             'output': '1 [2, 3] 4',
             'line': 31},
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
             'line': 44}]},
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
             'line': 17},
            {'prose': ['Use a dictionary as a lookup table when keys identify values. This is different from a list, '
                       'where numeric position is the lookup key.'],
             'code': 'scores = {"Ada": 10, "Grace": 9}\nprint(scores["Grace"])\nprint(scores.get("Guido", 0))',
             'output': '9\n0',
             'line': 33},
            {'prose': ['Use `items()` when the loop needs both keys and values. It avoids looping over keys and then '
                       'indexing back into the dictionary.'],
             'code': 'for name, score in scores.items():\n    print(f"{name}: {score}")',
             'output': 'Ada: 10\nGrace: 9',
             'line': 48}]},
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
             'line': 17},
            {'prose': ['Membership checks are the everyday set operation. A list can also use `in`, but a set says '
                       'that membership is central to the data shape.'],
             'code': 'allowed = {"python", "rust"}\nprint("python" in allowed)\nprint("ruby" in allowed)',
             'output': 'True\nFalse',
             'line': 31},
            {'prose': ['Union, intersection, and difference describe relationships between groups without manual '
                       'loops.'],
             'code': 'compiled = {"go", "rust"}\n'
                     'print(sorted(allowed | compiled))\n'
                     'print(sorted(allowed & compiled))\n'
                     'print(sorted(allowed - compiled))',
             'output': "['go', 'python', 'rust']\n['rust']\n['python']",
             'line': 46}]},
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
             'line': 17},
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
             'line': 34}]},
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
             'line': 17},
            {'prose': ['Add an `if` clause when only some items should appear. A dictionary comprehension can '
                       'transform key/value pairs while preserving the dictionary shape.'],
             'code': 'scores = {"Ada": 10, "Guido": 8, "Grace": 10}\n'
                     'high_scores = {name: score for name, score in scores.items() if score >= 10}\n'
                     'print(high_scores)',
             'output': "{'Ada': 10, 'Grace': 10}",
             'line': 31},
            {'prose': ['A set comprehension keeps only unique results. Here two people have the same score, so the '
                       'resulting set has two values.'],
             'code': 'unique_scores = {score for score in scores.values()}\nprint(unique_scores)',
             'output': '{8, 10}',
             'line': 45}]},
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
             'line': 22},
            {'prose': ['Multiple `if` clauses filter values. They are useful for simple conditions, but an explicit '
                       'loop is clearer when the rules need names or explanation.'],
             'code': 'numbers = range(10)\nfiltered = [n for n in numbers if n % 2 == 0 if n > 2]\nprint(filtered)',
             'output': '[4, 6, 8]',
             'line': 37}]},
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
             'line': 17},
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
             'line': 32},
            {'prose': ['`list.sort()` sorts the list in place. Use it when mutation is the point and no separate '
                       'sorted copy is needed.'],
             'code': 'users.sort(key=lambda user: user["name"])\nprint([user["name"] for user in users])',
             'output': "['Ada', 'Grace', 'Guido']",
             'line': 50}]},
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
             'line': 17},
            {'prose': ['Default arguments provide common values. Keyword arguments make it clear which option is being '
                       'overridden.'],
             'code': 'def format_total(amount, currency="USD"):\n'
                     '    return f"{amount} {currency}"\n'
                     '\n'
                     'print(format_total(10))\n'
                     'print(format_total(10, currency="EUR"))',
             'output': '10 USD\n10 EUR',
             'line': 32},
            {'prose': ['A function without an explicit `return` returns `None`. That makes side-effect-only functions '
                       'easy to distinguish from value-producing ones.'],
             'code': 'def log(message):\n    print(f"log: {message}")\n\nresult = log("saved")\nprint(result)',
             'output': 'log: saved\nNone',
             'line': 49}]},
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
             'line': 17},
            {'prose': ['Naming the option makes the call site explicit. A reader does not have to remember which '
                       'positional slot controls the timeout.'],
             'code': 'connect("example.com", timeout=10)',
             'output': 'https://example.com timeout=10',
             'line': 33},
            {'prose': ['Flags are especially good keyword-only arguments because a bare positional `False` is hard to '
                       'interpret.'],
             'code': 'connect("localhost", secure=False)',
             'output': 'http://localhost timeout=5',
             'line': 45}]},
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
             'line': 22},
            {'prose': ['Parameters after `*` are keyword-only. That makes options such as `clamp` explicit at the call '
                       'site.'],
             'code': 'print(scale(4, clamp=True))',
             'output': '8',
             'line': 42}]},
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
             'line': 17},
            {'prose': ['`**kwargs` collects named arguments into a dictionary. The names become string keys.'],
             'code': 'def describe(**metadata):\n    print(metadata)\n\ndescribe(owner="Ada", public=True)',
             'output': "{'owner': 'Ada', 'public': True}",
             'line': 32},
            {'prose': ['A function can combine explicit parameters, `*args`, and `**kwargs`. Put the flexible parts '
                       'last so the fixed shape remains visible.'],
             'code': 'def report(title, *items, **metadata):\n'
                     '    print(title)\n'
                     '    print(items)\n'
                     '    print(metadata)\n'
                     '\n'
                     'report("scores", 10, 9, owner="Ada")',
             'output': "scores\n(10, 9)\n{'owner': 'Ada'}",
             'line': 47}]},
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
             'line': 17},
            {'prose': ['Callers usually unpack the tuple immediately or soon after. The names at the call site '
                       'document what each position means.'],
             'code': 'boxes, leftover = result\nprint(boxes)\nprint(leftover)',
             'output': '3\n2',
             'line': 35}]},
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
             'line': 17},
            {'prose': ['Calling the outer function again creates a separate closure. `triple` uses the same inner '
                       'code, but remembers a different `factor`.'],
             'code': 'triple = make_multiplier(3)\nprint(triple(5))',
             'output': '15',
             'line': 35}]},
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
             'line': 22},
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
             'line': 41}]},
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
             'line': 17},
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
             'line': 35}]},
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
             'line': 17},
            {'prose': ['Lambdas are most idiomatic when passed directly to another function. `sorted()` calls this key '
                       'function once for each item.'],
             'code': 'items = [("notebook", 5), ("pen", 2), ("bag", 20)]\n'
                     'by_price = sorted(items, key=lambda item: item[1])\n'
                     'print(by_price)',
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]",
             'line': 30},
            {'prose': ['A named function is better when the behavior should be reused or explained. It produces the '
                       'same sort key, but gives the operation a name.'],
             'code': 'def price(item):\n    return item[1]\n\nprint(sorted(items, key=price))',
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]",
             'line': 44}]},
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
             'line': 17},
            {'prose': ['A `for` loop repeatedly calls `next()` for you. The loop stops when the generator is '
                       'exhausted.'],
             'code': 'for value in countdown(3):\n    print(value)',
             'output': '3\n2\n1',
             'line': 37}]},
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
             'line': 22},
            {'prose': ['Delegation is useful when flattening nested iterables. `yield from row` replaces an inner loop '
                       'that would yield each item by hand.'],
             'code': 'def flatten(rows):\n'
                     '    for row in rows:\n'
                     '        yield from row\n'
                     '\n'
                     'print(list(flatten([[1, 2], [3]])))',
             'output': '[1, 2, 3]',
             'line': 39}]},
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
             'line': 17},
            {'prose': ['A generator expression is lazy: it creates an iterator that produces values as they are '
                       'consumed. After two `next()` calls, only the remaining squares are left.'],
             'code': 'stream_squares = (number * number for number in numbers)\n'
                     'print(next(stream_squares))\n'
                     'print(next(stream_squares))\n'
                     'print(list(stream_squares))',
             'output': '1\n4\n[9, 16]',
             'line': 31},
            {'prose': ['Generator expressions are common inside reducing functions. When a generator expression is the '
                       'only argument, the extra parentheses can be omitted.'],
             'code': 'print(sum(number * number for number in numbers))',
             'output': '30',
             'line': 48}]},
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
             'line': 17},
            {'prose': ['`chain()` presents several iterables as one stream. This avoids building an intermediate list '
                       'just to loop over combined inputs.'],
             'code': 'pages = itertools.chain(["intro", "setup"], ["deploy"])\nprint(list(pages))',
             'output': "['intro', 'setup', 'deploy']",
             'line': 32},
            {'prose': ['Iterator helpers compose with ordinary Python expressions. `compress()` keeps items whose '
                       'corresponding selector is true.'],
             'code': 'scores = [7, 10, 8, 10]\n'
                     'high_scores = itertools.compress(scores, [score >= 9 for score in scores])\n'
                     'print(list(high_scores))',
             'output': '[10, 10]',
             'line': 45}]},
 {'slug': 'decorators',
  'title': 'Decorators',
  'section': 'Functions',
  'summary': 'Decorators wrap or register functions using @ syntax.',
  'doc_url': 'https://docs.python.org/3.13/glossary.html#term-decorator',
  'code': 'def loud(func):\n'
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
          '    return f"welcome {name}"\n'
          '\n'
          'print(welcome("workers"))\n',
  'expected_output': 'HELLO PYTHON\nWELCOME WORKERS\n',
  'notes': ['`@decorator` is shorthand for assigning `func = decorator(func)`.',
            'Decorators can wrap, replace, or register functions.',
            'Use `functools.wraps` in production wrappers that should preserve metadata.'],
  'cells': [{'prose': ['A decorator is just a function that takes a function and returns another callable. Applying it '
                       'manually shows the wrapping step.'],
             'code': 'def loud(func):\n'
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
             'line': 17},
            {'prose': ['The `@loud` syntax performs the same rebinding at definition time. After decoration, `welcome` '
                       'refers to the wrapper returned by `loud`.'],
             'code': '@loud\ndef welcome(name):\n    return f"welcome {name}"\n\nprint(welcome("workers"))',
             'output': 'WELCOME WORKERS',
             'line': 39}]},
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
             'line': 17},
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
             'line': 37}]},
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
             'line': 22},
            {'prose': ['`super()` delegates to the parent implementation. The child method can reuse the parent result '
                       'and then add specialized behavior.'],
             'code': 'print(pet.speak())\nprint(isinstance(pet, Animal))',
             'output': 'Nina makes a sound; Nina barks\nTrue',
             'line': 47}]},
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
             'line': 17},
            {'prose': ['The generated instance still exposes ordinary attributes. A dataclass is a regular class with '
                       'useful methods filled in.'],
             'code': 'print(user.name)',
             'output': 'Ada',
             'line': 37},
            {'prose': ['Defaults can be overridden by keyword. The generated representation includes the field names, '
                       'which is useful during debugging.'],
             'code': 'inactive = User("Guido", active=False)\nprint(inactive)\nprint(inactive.active)',
             'output': "User(name='Guido', active=False)\nFalse",
             'line': 49}]},
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
             'line': 17},
            {'prose': ['A setter lets assignment keep normal attribute syntax while the class validates or normalizes '
                       'the value.'],
             'code': 'box.width = 5\nprint(box.area)',
             'output': '20',
             'line': 49},
            {'prose': ['Validation belongs inside the class when every caller should obey the same rule. Invalid '
                       'assignment raises an exception at the boundary.'],
             'code': 'try:\n    box.width = 0\nexcept ValueError as error:\n    print(error)',
             'output': 'width must be positive',
             'line': 62}]},
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
             'line': 17},
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
             'line': 34},
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
             'line': 54},
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
             'line': 77}]},
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
             'line': 22},
            {'prose': ['The `metaclass=` keyword applies that class-building rule. Here the metaclass adds a `tag` '
                       'attribute to the new class.'],
             'code': 'class Event(metaclass=Tagged):\n    pass\n\nprint(Event.tag)\nprint(type(Event).__name__)',
             'output': 'event\nTagged',
             'line': 39}]},
 {'slug': 'context-managers',
  'title': 'Context Managers',
  'section': 'Data Model',
  'summary': 'with ensures setup and cleanup happen together.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#context-managers',
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
          'with tag("section"):\n'
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
            'Use `finally` when cleanup must happen after errors too.'],
  'cells': [{'prose': ['A context manager surrounds a block. Code before `yield` is setup, and code after `yield` is '
                       'cleanup.'],
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
                     'with tag("section"):\n'
                     '    print("content")',
             'output': '<section>\ncontent\n</section>',
             'line': 17},
            {'prose': ['Putting cleanup in `finally` ensures it runs even when the block raises. The surrounding `try` '
                       'catches the error after cleanup has happened.'],
             'code': 'try:\n'
                     '    with tag("error"):\n'
                     '        raise ValueError("boom")\n'
                     'except ValueError:\n'
                     '    print("handled")',
             'output': '<error>\n</error>\nhandled',
             'line': 42}]},
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
             'line': 22},
            {'prose': ['Deleting a list item removes that position and shifts later items left.'],
             'code': 'items = ["a", "b", "c"]\ndel items[1]\nprint(items)',
             'output': "['a', 'c']",
             'line': 36},
            {'prose': ['Deleting a name removes the binding from the current namespace. It is different from rebinding '
                       'the name to `None`.'],
             'code': 'value = "cached"\ndel value\nprint("value" in locals())',
             'output': 'False',
             'line': 50}]},
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
             'line': 19},
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
             'line': 43}]},
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
             'line': 22},
            {'prose': ['When the assertion is false, Python raises `AssertionError`. This signals a broken assumption, '
                       'not a normal recovery path.'],
             'code': 'try:\n    average([])\nexcept AssertionError as error:\n    print(error)',
             'output': 'scores must not be empty',
             'line': 38}]},
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
             'line': 22},
            {'prose': ['The caller handles the domain error. The original `ValueError` remains available as '
                       '`__cause__`.'],
             'code': 'try:\n'
                     '    read_port("abc")\n'
                     'except ConfigError as error:\n'
                     '    print(error)\n'
                     '    print(type(error.__cause__).__name__)',
             'output': 'port must be a number\nValueError',
             'line': 44}]},
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
             'line': 22},
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
             'line': 38}]},
 {'slug': 'modules',
  'title': 'Modules',
  'section': 'Modules',
  'summary': 'Modules organize code into namespaces and expose reusable definitions.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/modules.html',
  'code': 'import math\n'
          'from statistics import mean\n'
          '\n'
          'radius = 3\n'
          'area = math.pi * radius ** 2\n'
          'print(round(area, 2))\n'
          '\n'
          'scores = [8, 10, 9]\n'
          'print(mean(scores))\n'
          '\n'
          'print(math.__name__)\n',
  'expected_output': '28.27\n9\nmath\n',
  'notes': ['Prefer plain `import module` when the namespace improves readability.',
            'Use focused imports for a small number of clear names.',
            'Place imports near the top of the file.'],
  'cells': [{'prose': ['Importing a module gives access to its namespace. The `math.` prefix makes it clear where `pi` '
                       'came from.'],
             'code': 'import math\n\nradius = 3\narea = math.pi * radius ** 2\nprint(round(area, 2))',
             'output': '28.27',
             'line': 17},
            {'prose': ['A focused `from ... import ...` brings one definition into the current namespace. This keeps a '
                       'common operation concise without importing every name.'],
             'code': 'from statistics import mean\n\nscores = [8, 10, 9]\nprint(mean(scores))',
             'output': '9',
             'line': 33},
            {'prose': ['Modules are objects too. Their attributes include metadata such as `__name__`, which records '
                       "the module's import name."],
             'code': 'print(math.__name__)',
             'output': 'math',
             'line': 48}]},
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
             'line': 21},
            {'prose': ['A name imported with `from` can also be aliased. Use this when the local name explains the '
                       'role better than the original name.'],
             'code': 'from math import sqrt as square_root\n\nprint(square_root(81))\nprint(square_root.__name__)',
             'output': '9.0\nsqrt',
             'line': 38}]},
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
             'line': 17},
            {'prose': ['Python stores annotations on the function object for tools and introspection. Type checkers '
                       'use this information without changing the function call syntax.'],
             'code': 'print(total.__annotations__)',
             'output': "{'numbers': list[int], 'return': <class 'int'>}",
             'line': 32},
            {'prose': ['Most hints are not runtime validation. This call passes a string where the hint says `int`; '
                       'Python still calls the function because the body can format any value.'],
             'code': 'def label(score: int) -> str:\n    return f"score={score}"\n\nprint(label("high"))',
             'output': 'score=high',
             'line': 44}]},
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
             'line': 17},
            {'prose': ['Compare enum members with enum members, not with raw strings. This keeps the set of valid '
                       'states explicit.'],
             'code': 'print(current is Status.PENDING)\nprint(current == "pending")',
             'output': 'True\nFalse',
             'line': 38}]},
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
          'print(bool(re.search(r"Grace", text)))\n',
  'expected_output': 'Ada 10\nGrace 9\nTrue\n',
  'notes': ['Use raw strings for regex patterns so backslashes are easier to read.',
            'For simple substring checks, ordinary string methods are often clearer than regex.'],
  'cells': [{'prose': ['Regular expressions are a compact language for searching and extracting text patterns. '
                       "Python's re module provides the standard interface.",
                       'Regex is powerful for structured text with repeated patterns, such as names followed by '
                       'numbers. Capturing groups return just the pieces you care about.',
                       'They are not always the right tool. Prefer ordinary string methods when the pattern is simple, '
                       'because simpler code is easier to maintain.'],
             'code': 'import re\n'
                     '\n'
                     'text = "Ada: 10, Grace: 9"\n'
                     'pattern = r"([A-Za-z]+): (\\d+)"\n'
                     '\n'
                     'for name, score in re.findall(pattern, text):\n'
                     '    print(name, int(score))',
             'output': 'Ada 10\nGrace 9',
             'line': 17},
            {'prose': ['They are not always the right tool. Prefer ordinary string methods when the pattern is simple, '
                       'because simpler code is easier to maintain.'],
             'code': 'print(bool(re.search(r"Grace", text)))',
             'output': 'True',
             'line': 40}]},
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
             'line': 17},
            {'prose': ['Bad numeric text raises `ValueError`. Catch that specific exception when invalid input is part '
                       'of the normal flow.'],
             'code': 'try:\n    int("python")\nexcept ValueError as error:\n    print(type(error).__name__)',
             'output': 'ValueError',
             'line': 31}]},
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
             'line': 17},
            {'prose': ['Raise the custom exception where the invalid state is detected. Normal inputs still follow the '
                       'ordinary success path.'],
             'code': 'def checkout(items):\n'
                     '    if not items:\n'
                     '        raise EmptyCartError("cart is empty")\n'
                     '    return "paid"\n'
                     '\n'
                     'print(checkout(["book"]))',
             'output': 'paid',
             'line': 32},
            {'prose': ['Callers can catch the precise error type without accidentally catching unrelated failures.'],
             'code': 'try:\n    checkout([])\nexcept EmptyCartError as error:\n    print(error)',
             'output': 'cart is empty',
             'line': 49}]},
 {'slug': 'json',
  'title': 'JSON',
  'section': 'Standard Library',
  'summary': 'json encodes Python values as JSON text and decodes them back.',
  'doc_url': 'https://docs.python.org/3.13/library/json.html',
  'code': 'import json\n'
          '\n'
          'payload = {"language": "Python", "versions": [3, 13], "stable": True}\n'
          'text = json.dumps(payload, sort_keys=True)\n'
          'print(text)\n'
          '\n'
          'decoded = json.loads(text)\n'
          'print(decoded["language"])\n'
          'print(decoded["stable"])\n',
  'expected_output': '{"language": "Python", "stable": true, "versions": [3, 13]}\nPython\nTrue\n',
  'notes': ['`dumps()` returns a string; `loads()` accepts a string.',
            'JSON `true`, `false`, and `null` become Python `True`, `False`, and `None`.',
            'Use `sort_keys=True` when stable text output matters.'],
  'cells': [{'prose': ['`dumps()` encodes Python data as JSON text. `sort_keys=True` keeps dictionary keys in a stable '
                       'order for reproducible output.'],
             'code': 'import json\n'
                     '\n'
                     'payload = {"language": "Python", "versions": [3, 13], "stable": True}\n'
                     'text = json.dumps(payload, sort_keys=True)\n'
                     'print(text)',
             'output': '{"language": "Python", "stable": true, "versions": [3, 13]}',
             'line': 17},
            {'prose': ['`loads()` decodes JSON text back into Python values. JSON booleans become Python booleans, '
                       'arrays become lists, and objects become dictionaries.'],
             'code': 'decoded = json.loads(text)\nprint(decoded["language"])\nprint(decoded["stable"])',
             'output': 'Python\nTrue',
             'line': 33}]},
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
             'line': 17},
            {'prose': ['Use `timedelta` for durations. Adding one to a `datetime` produces another `datetime` without '
                       'manually changing calendar fields.'],
             'code': 'expires_at = created_at + timedelta(days=7, hours=2)\nprint(expires_at.isoformat())',
             'output': '2026-05-11T14:30:00+00:00',
             'line': 43},
            {'prose': ['Use `strftime()` for human-facing formatting and `fromisoformat()` when reading ISO 8601 text '
                       'back into a `datetime`.'],
             'code': 'print(created_at.strftime("%Y-%m-%d %H:%M %Z"))\n'
                     'parsed = datetime.fromisoformat("2026-05-04T12:30:00+00:00")\n'
                     'print(parsed == created_at)',
             'output': '2026-05-04 12:30 UTC\nTrue',
             'line': 56}]},
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
             'line': 19},
            {'prose': ['Use `await` inside another coroutine to get the eventual result. `asyncio.run()` starts an '
                       'event loop for the top-level coroutine.'],
             'code': 'async def main():\n'
                     '    title = await fetch_title("async-await")\n'
                     '    print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': 'Async Await',
             'line': 39},
            {'prose': ['`asyncio.gather()` awaits several awaitables and returns their results in order. This is the '
                       'shape used when independent I/O operations can progress together.'],
             'code': 'async def main():\n'
                     '    titles = await asyncio.gather(fetch_title("json"), fetch_title("datetime"))\n'
                     '    print(titles)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': "['Json', 'Datetime']",
             'line': 55}]},
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
             'line': 24},
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
             'line': 43},
            {'prose': ['The top-level coroutine combines both protocols: open the async resource, then consume the '
                       'async stream inside it.'],
             'code': 'async def main():\n'
                     '    async with Session():\n'
                     '        async for title in titles():\n'
                     '            print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': 'open\nValues\nAsync Await\nclose',
             'line': 63}]}]
