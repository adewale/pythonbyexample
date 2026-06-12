"""Structural snapshot of the example catalog (generated).

Regenerate with scripts/refresh_golden_fixture.py after intentional
content changes; review the printed structural summary before
committing. check_example_migration_parity.py fails the build whenever
the loader's output stops matching this snapshot, so an accidental
loader/parser change cannot silently rewrite the teaching structure.
"""

PYTHON_VERSION = '3.13'
REFERENCE_URL = 'https://docs.python.org/3.13/'

EXAMPLES = [{'slug': 'hello-world',
  'title': 'Hello World',
  'section': 'Basics',
  'summary': 'The first Python program prints a line of text.',
  'doc_path': '/tutorial/introduction.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/introduction.html',
  'explanation': ['Every Python program starts by executing statements from top to bottom. Calling '
                  '`print()` is the smallest useful program because it shows how Python evaluates '
                  'an expression and sends text to standard output.',
                  'Strings are ordinary values, so the message passed to `print()` can be changed, '
                  'stored in a variable, or produced by a function. This example keeps the first '
                  'program intentionally small.',
                  'Run the program and compare what you see with the source: the text appears on '
                  'standard output followed by a newline, which is why successive `print()` calls '
                  'land on separate lines.'],
  'notes': ['`print()` writes text followed by a newline.',
            'Strings can be delimited with single or double quotes.'],
  'see_also': ['values', 'variables'],
  'cells': [{'kind': 'cell',
             'prose': ['The whole program is one statement. Python evaluates the string literal '
                       '`"hello world"` and passes that value to `print()`, which writes it to '
                       'standard output — the output panel shows exactly that line.'],
             'code': 'print("hello world")',
             'output': 'hello world'}],
  'code': 'print("hello world")\n',
  'expected_output': 'hello world\n'},
 {'slug': 'values',
  'title': 'Values',
  'section': 'Basics',
  'summary': 'Python programs evaluate expressions into objects such as text, numbers, booleans, '
             'and None.',
  'doc_path': '/library/stdtypes.html',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html',
  'explanation': ['A Python program works by evaluating expressions into values. Values are '
                  'objects: text, integers, floats, booleans, `None`, and many richer types '
                  'introduced later.',
                  'Names point to values; they are not declarations that permanently fix a type. '
                  'Operations usually produce new values, which you can print, store, compare, or '
                  'pass to functions.',
                  'This page is a map, not the whole territory. Later pages explain the '
                  'boundaries: equality vs identity, mutable vs immutable values, truthiness vs '
                  'literal booleans, and `None` vs a missing key or an exception.'],
  'notes': ['Values are objects; names point to them and operations usually create new values.',
            'Use `is None` for the absence marker, not `== None`.',
            'This overview introduces boundaries that later pages explain in detail.'],
  'see_also': ['variables', 'booleans', 'none', 'literals'],
  'cells': [{'kind': 'cell',
             'prose': ['Start with several built-in values. Python does not require declarations '
                       'before binding these names, and each value is still an object with a '
                       'type.'],
             'code': 'text = "python"\n'
                     'count = 3\n'
                     'ratio = 2.5\n'
                     'ready = True\n'
                     'missing = None\n'
                     '\n'
                     'print(type(text).__name__)',
             'output': 'str'},
            {'kind': 'cell',
             'prose': ['Methods and operators evaluate to new values. The original `text`, '
                       '`count`, and `ratio` bindings remain ordinary objects you can reuse.'],
             'code': 'print(text.upper())\nprint(count + 4)\nprint(ratio * 2)',
             'output': 'PYTHON\n7\n5.0'},
            {'kind': 'cell',
             'prose': ['Boolean expressions combine facts, and `None` is checked by identity '
                       'because it is a singleton absence marker.'],
             'code': 'print(ready and count > 0)\nprint(missing is None)',
             'output': 'True\nTrue'}],
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
  'expected_output': 'str\nPYTHON\n7\n5.0\nTrue\nTrue\n'},
 {'slug': 'literals',
  'title': 'Literals',
  'section': 'Basics',
  'summary': 'Literals write values directly in Python source code.',
  'doc_path': '/reference/lexical_analysis.html#literals',
  'doc_url': 'https://docs.python.org/3.13/reference/lexical_analysis.html#literals',
  'explanation': ['Literals are source-code forms for values: numbers, text, bytes, containers, '
                  'booleans, `None`, and a few specialized markers. They are how a program writes '
                  'small values directly.',
                  'The literal form is only the beginning. Later examples explain each value '
                  'family in depth: strings are Unicode text, bytes are binary data, lists and '
                  'dicts are containers, and `None` represents intentional absence.',
                  'Use literals when the value is small and local. Give repeated or meaningful '
                  'values a name so the program explains why that value matters.'],
  'notes': ['Literals are good for small local values; constants are better for repeated values '
            'with meaning.',
            '`{}` is an empty dictionary. Use `set()` for an empty set.',
            'Bytes literals are binary data; string literals are Unicode text.',
            '`...` evaluates to the `Ellipsis` object.'],
  'see_also': ['values', 'strings', 'numbers', 'string-formatting'],
  'cells': [{'kind': 'cell',
             'prose': ['Numeric literals write numbers directly. Complex literals use `j` for the '
                       'imaginary part.'],
             'code': 'whole = 42\n'
                     'fraction = 3.5\n'
                     'complex_number = 2 + 3j\n'
                     'print(whole, fraction, complex_number.imag)',
             'output': '42 3.5 3.0'},
            {'kind': 'cell',
             'prose': ['Integer literals also accept hexadecimal (`0x`), binary (`0b`), and octal '
                       '(`0o`) prefixes. Underscores group digits visually without changing the '
                       'value.'],
             'code': 'flags = 0xFF\n'
                     'mask = 0b1010\n'
                     'million = 1_000_000\n'
                     'print(flags, mask, million)',
             'output': '255 10 1000000'},
            {'kind': 'cell',
             'prose': ['String literals write Unicode text. Raw strings keep backslashes literal, '
                       'bytes literals write binary data rather than text, and f-strings '
                       '(`f"..."`) embed expressions inline.'],
             'code': 'text = "python"\n'
                     'raw_pattern = r"\\d+"\n'
                     'data = b"py"\n'
                     'score = 98\n'
                     'formatted = f"score={score}"\n'
                     'print(text)\n'
                     'print(raw_pattern)\n'
                     'print(data)\n'
                     'print(formatted)',
             'output': "python\n\\d+\nb'py'\nscore=98"},
            {'kind': 'cell',
             'prose': ['Container literals create tuples, lists, dictionaries, and sets. Each '
                       'container answers a different question about order, position, lookup, or '
                       'uniqueness.'],
             'code': 'point = (2, 3)\n'
                     'names = ["Ada", "Grace"]\n'
                     'scores = {"Ada": 98}\n'
                     'unique = {"py", "go"}\n'
                     'print(point)\n'
                     'print(names[0])\n'
                     'print(scores["Ada"])\n'
                     'print(sorted(unique))',
             'output': "(2, 3)\nAda\n98\n['go', 'py']"},
            {'kind': 'cell',
             'prose': ['`True`, `False`, `None`, and `...` are singleton literal-like constants '
                       'used for truth values, absence, and placeholders.'],
             'code': 'print(True, False, None)\nprint(...)',
             'output': 'True False None\nEllipsis'},
            {'kind': 'cell',
             'prose': ['Curly-brace literals are dictionaries by default. The empty form `{}` is '
                       'an empty dictionary, not an empty set; use `set()` for that. A non-empty '
                       '`{1, 2}` is a set because keyless items can only be a set.'],
             'code': 'print(type({}).__name__)\n'
                     'print(type(set()).__name__)\n'
                     'print(type({1, 2}).__name__)',
             'output': 'dict\nset\nset'}],
  'code': 'whole = 42\n'
          'fraction = 3.5\n'
          'complex_number = 2 + 3j\n'
          'print(whole, fraction, complex_number.imag)\n'
          '\n'
          'flags = 0xFF\n'
          'mask = 0b1010\n'
          'million = 1_000_000\n'
          'print(flags, mask, million)\n'
          '\n'
          'text = "python"\n'
          'raw_pattern = r"\\d+"\n'
          'data = b"py"\n'
          'score = 98\n'
          'formatted = f"score={score}"\n'
          'print(text)\n'
          'print(raw_pattern)\n'
          'print(data)\n'
          'print(formatted)\n'
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
          'print(...)\n'
          '\n'
          'print(type({}).__name__)\n'
          'print(type(set()).__name__)\n'
          'print(type({1, 2}).__name__)\n',
  'expected_output': '42 3.5 3.0\n'
                     '255 10 1000000\n'
                     'python\n'
                     '\\d+\n'
                     "b'py'\n"
                     'score=98\n'
                     '(2, 3)\n'
                     'Ada\n'
                     '98\n'
                     "['go', 'py']\n"
                     'True False None\n'
                     'Ellipsis\n'
                     'dict\n'
                     'set\n'
                     'set\n'},
 {'slug': 'numbers',
  'title': 'Numbers',
  'section': 'Basics',
  'summary': 'Python numbers include integers, floats, and complex values.',
  'doc_path': '/library/stdtypes.html#numeric-types-int-float-complex',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#numeric-types-int-float-complex',
  'explanation': ["Python's numeric model starts with `int`, `float`, and `complex`. Integers are "
                  'arbitrary precision, floats are approximate double-precision values, and '
                  'complex numbers carry real and imaginary parts.',
                  'Operators encode different numeric questions. `/` means true division and '
                  'returns a float, `//` means floor division, `%` gives the remainder, and `**` '
                  'computes powers.',
                  'Use rounding for display, not as a substitute for understanding floating-point '
                  'approximation. Financial code usually needs `decimal.Decimal`, which is a '
                  'separate precision topic.'],
  'notes': ["Python's `int` has arbitrary precision; it grows as large as memory allows.",
            "Python's `float` is approximate double-precision floating point.",
            'Use `/` for true division and `//` for floor division.',
            'Use `math.isclose` instead of `==` for floating-point comparison; reach for '
            '`decimal.Decimal` when exact decimal precision is the domain requirement.'],
  'see_also': ['literals', 'operators'],
  'cells': [{'kind': 'cell',
             'prose': ['Python has `int` for whole numbers and `float` for approximate real-valued '
                       'arithmetic. True division with `/` returns a `float`, even when both '
                       'inputs are integers.'],
             'code': 'count = 10\n'
                     'ratio = 0.25\n'
                     '\n'
                     'print(count + 5)\n'
                     'print(count / 4)\n'
                     'print(ratio * 2)',
             'output': '15\n2.5\n0.5'},
            {'kind': 'cell',
             'prose': ['Floor division and modulo are useful when you need quotient and remainder '
                       'behavior. Powers use `**`, not `^`.'],
             'code': 'print(count // 4)\nprint(count % 4)\nprint(2 ** 5)',
             'output': '2\n2\n32'},
            {'kind': 'cell',
             'prose': ['Complex numbers are built in. The literal suffix `j` marks the imaginary '
                       'part.'],
             'code': 'z = 2 + 3j\nprint(z.real, z.imag)',
             'output': '2.0 3.0'},
            {'kind': 'cell',
             'prose': ['Floating-point values are approximate, so `==` between expected and '
                       'computed floats is rarely the right test. Compare with `math.isclose` (or '
                       'work in `decimal.Decimal`) when the question is "are these the same number '
                       'to within tolerance".'],
             'code': 'import math\n'
                     '\n'
                     'print(0.1 + 0.2)\n'
                     'print(0.1 + 0.2 == 0.3)\n'
                     'print(math.isclose(0.1 + 0.2, 0.3))\n'
                     'print(round(3.14159, 2))',
             'output': '0.30000000000000004\nFalse\nTrue\n3.14'}],
  'code': 'import math\n'
          '\n'
          'count = 10\n'
          'ratio = 0.25\n'
          'z = 2 + 3j\n'
          '\n'
          'print(count + 5)\n'
          'print(count / 4)\n'
          'print(ratio * 2)\n'
          'print(count // 4)\n'
          'print(count % 4)\n'
          'print(2 ** 5)\n'
          'print(z.real, z.imag)\n'
          'print(0.1 + 0.2)\n'
          'print(0.1 + 0.2 == 0.3)\n'
          'print(math.isclose(0.1 + 0.2, 0.3))\n'
          'print(round(3.14159, 2))\n',
  'expected_output': '15\n2.5\n0.5\n2\n2\n32\n2.0 3.0\n0.30000000000000004\nFalse\nTrue\n3.14\n'},
 {'slug': 'booleans',
  'title': 'Booleans',
  'section': 'Basics',
  'summary': 'Booleans represent truth values and combine with logical operators.',
  'doc_path': '/library/stdtypes.html#boolean-type-bool',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#boolean-type-bool',
  'explanation': ['Booleans are the values `True` and `False`. They are produced by comparisons '
                  'and combined with `and`, `or`, and `not`.',
                  "Python's logical operators short-circuit. That means the right side is "
                  'evaluated only when needed, which keeps guard checks efficient and safe.',
                  'Booleans are also connected to truthiness: many objects can be tested in '
                  'conditions even when they are not literally `True` or `False`.'],
  'notes': ['Boolean constants are `True` and `False`, with capital letters.',
            '`and` and `or` short-circuit: Python does not evaluate the right side if the left '
            'side already determines the result.',
            'Prefer truthiness for containers and explicit comparisons when the exact boolean '
            'condition matters.',
            '`bool` subclasses `int`; `isinstance(True, int)` is `True`. Exclude booleans '
            'explicitly when only "real" integers should pass.'],
  'see_also': ['truthiness', 'operators', 'conditionals'],
  'cells': [{'kind': 'cell',
             'prose': ['Use booleans for facts that are either true or false. Python spells the '
                       'constants `True` and `False`.',
                       'Use `and`, `or`, and `not` to combine truth values. These operators read '
                       'like English and short-circuit when possible.'],
             'code': 'logged_in = True\n'
                     'has_permission = False\n'
                     '\n'
                     'print(logged_in and has_permission)\n'
                     'print(logged_in or has_permission)\n'
                     'print(not has_permission)',
             'output': 'False\nTrue\nTrue'},
            {'kind': 'cell',
             'prose': ['Comparisons produce booleans too, so they compose naturally with logical '
                       'operators in conditions and validation checks.'],
             'code': 'name = "Ada"\nprint(name == "Ada" and len(name) > 0)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ['`bool` is a subclass of `int`, which is occasionally a footgun. `True` '
                       'behaves as `1` and `False` as `0` in arithmetic, and `isinstance(True, '
                       'int)` is `True`. When a function must reject booleans, exclude them '
                       'explicitly with `isinstance(value, int) and not isinstance(value, bool)`.'],
             'code': 'print(isinstance(True, int))\n'
                     'print(True + True)\n'
                     'print(sum([True, True, False, True]))\n'
                     '\n'
                     'def is_strict_int(value):\n'
                     '    return isinstance(value, int) and not isinstance(value, bool)\n'
                     '\n'
                     'print(is_strict_int(True))\n'
                     'print(is_strict_int(1))',
             'output': 'True\n2\n3\nFalse\nTrue'}],
  'code': 'logged_in = True\n'
          'has_permission = False\n'
          '\n'
          'print(logged_in and has_permission)\n'
          'print(logged_in or has_permission)\n'
          'print(not has_permission)\n'
          '\n'
          'name = "Ada"\n'
          'print(name == "Ada" and len(name) > 0)\n'
          '\n'
          'print(isinstance(True, int))\n'
          'print(True + True)\n'
          'print(sum([True, True, False, True]))\n'
          '\n'
          'def is_strict_int(value):\n'
          '    return isinstance(value, int) and not isinstance(value, bool)\n'
          '\n'
          'print(is_strict_int(True))\n'
          'print(is_strict_int(1))\n',
  'expected_output': 'False\nTrue\nTrue\nTrue\nTrue\n2\n3\nFalse\nTrue\n'},
 {'slug': 'operators',
  'title': 'Operators',
  'section': 'Basics',
  'summary': 'Operators combine, compare, and test values in expressions.',
  'doc_path': '/reference/expressions.html#operator-precedence',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#operator-precedence',
  'explanation': ['Operators are the punctuation and keywords that combine values into '
                  'expressions. Some operators compute new values, some compare values, and some '
                  'ask relationship questions such as membership or identity.',
                  'This page is the surface map. Focused examples explain the deeper behavior of '
                  'numbers, booleans, conditions, sets, assignment expressions, and operator '
                  'overloading.',
                  'Read operators by the question they ask: arithmetic computes, comparison '
                  'answers true or false, boolean operators combine truth values, membership '
                  'searches a container, and specialized operators should only appear when the '
                  'data shape calls for them.'],
  'notes': ['Use the clearest operator for the question: arithmetic, comparison, boolean logic, '
            'membership, identity, or bitwise manipulation.',
            '`and` and `or` short-circuit, so the right side may not run.',
            'Operators have precedence; use parentheses when grouping would otherwise be hard to '
            'read.',
            'Custom operator behavior should make an object feel more natural, not more clever.'],
  'see_also': ['numbers',
               'equality-and-identity',
               'assignment-expressions',
               'operator-overloading'],
  'cells': [{'kind': 'cell',
             'prose': ['Arithmetic operators compute new values. Use `//` for floor division, `%` '
                       'for remainder, and `**` for powers.'],
             'code': 'count = 10\n'
                     'print(count + 5)\n'
                     'print(count // 4)\n'
                     'print(count % 4)\n'
                     'print(2 ** 5)',
             'output': '15\n2\n2\n32'},
            {'kind': 'cell',
             'prose': ['Comparison operators produce booleans. Python comparisons can chain, which '
                       'keeps range checks readable.'],
             'code': 'score = 91\n'
                     'print(80 <= score < 100)\n'
                     'print(score == 100 or score >= 90)\n'
                     'print("py" in "python")',
             'output': 'True\nTrue\nTrue'},
            {'kind': 'cell',
             'prose': ['Bitwise operators work on integer bit patterns. They are useful for masks '
                       'and flags, not ordinary boolean logic. `&` is bitwise AND, `|` is bitwise '
                       'OR, `^` is exclusive OR, and `<<` shifts left.'],
             'code': 'flags = 0b0011\n'
                     'print(flags & 0b0101)\n'
                     'print(flags | 0b0100)\n'
                     'print(flags ^ 0b0101)\n'
                     'print(flags << 1)',
             'output': '1\n7\n6\n6'},
            {'kind': 'cell',
             'prose': ['The `@` operator is reserved for matrix-like multiplication and custom '
                       'types that define `__matmul__`.'],
             'code': 'class Scale:\n'
                     '    def __init__(self, value):\n'
                     '        self.value = value\n'
                     '\n'
                     '    def __matmul__(self, other):\n'
                     '        return self.value * other.value\n'
                     '\n'
                     'print(Scale(2) @ Scale(3))',
             'output': '6'},
            {'kind': 'cell',
             'prose': ['The walrus operator `:=` assigns inside an expression. Use it when naming '
                       'a value avoids repeating work in a condition.'],
             'code': 'items = ["a", "b"]\nif (size := len(items)) > 0:\n    print(size)',
             'output': '2'},
            {'kind': 'cell',
             'prose': ['`and` and `or` short-circuit: the right side runs only when the left side '
                       'cannot already determine the result. That makes them safe for guard '
                       'expressions like `obj and obj.value` where the right side would fail on '
                       '`None`.'],
             'code': 'def loud():\n'
                     '    print("ran")\n'
                     '    return True\n'
                     '\n'
                     'print(False and loud())\n'
                     'print(True or loud())\n'
                     'print(True and loud())',
             'output': 'False\nTrue\nran\nTrue'}],
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
          'print(flags & 0b0101)\n'
          'print(flags | 0b0100)\n'
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
          '    print(size)\n'
          '\n'
          'def loud():\n'
          '    print("ran")\n'
          '    return True\n'
          '\n'
          'print(False and loud())\n'
          'print(True or loud())\n'
          'print(True and loud())\n',
  'expected_output': '15\n2\n2\n32\nTrue\nTrue\nTrue\n1\n7\n6\n6\n6\n2\nFalse\nTrue\nran\nTrue\n'},
 {'slug': 'none',
  'title': 'None',
  'section': 'Basics',
  'summary': 'None represents expected absence, distinct from missing keys and errors.',
  'doc_path': '/library/constants.html#None',
  'doc_url': 'https://docs.python.org/3.13/library/constants.html#None',
  'explanation': ['`None` represents the absence of a value. It is the usual sentinel when a '
                  'function has no result to return but the absence itself is meaningful.',
                  'Because `None` is a singleton, idiomatic Python checks it with `is None` or `is '
                  'not None`. This avoids confusing identity with value equality.',
                  'Absence has several nearby shapes in Python. A function can return `None`, a '
                  'dictionary lookup can supply a default for a missing key, and an invalid '
                  'operation can raise an exception.'],
  'notes': ['Use `is None` rather than `== None`; `None` is a singleton identity value.',
            'Use `None` for expected absence that callers can test.',
            'Use dictionary defaults for missing mapping keys and exceptions for invalid '
            'operations.'],
  'see_also': ['values', 'truthiness', 'exceptions', 'dicts'],
  'cells': [{'kind': 'cell',
             'prose': ["`None` is Python's value for “nothing here.” Check it with `is None` "
                       'because it is a singleton identity value.'],
             'code': 'result = None\nprint(result is None)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ['Functions often return `None` when absence is expected and callers can '
                       'continue. The function name and surrounding code should make that '
                       'possibility clear.'],
             'code': 'def find_score(name):\n'
                     '    if name == "Ada":\n'
                     '        return 10\n'
                     '    return None\n'
                     '\n'
                     'score = find_score("Grace")\n'
                     'print(score is None)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ['A missing dictionary key is another absence boundary. Use `get()` when the '
                       'mapping can supply a default, and use exceptions for invalid operations '
                       'that cannot produce a value.'],
             'code': 'profile = {"name": "Ada"}\n'
                     'print(profile.get("timezone", "UTC"))\n'
                     '\n'
                     'try:\n'
                     '    int("python")\n'
                     'except ValueError:\n'
                     '    print("invalid number")',
             'output': 'UTC\ninvalid number'}],
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
  'expected_output': 'True\nTrue\nUTC\ninvalid number\n'},
 {'slug': 'variables',
  'title': 'Variables',
  'section': 'Basics',
  'summary': 'Names are bound to values with assignment.',
  'doc_path': '/reference/simple_stmts.html#assignment-statements',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#assignment-statements',
  'explanation': ['Python variables are names bound to objects. Assignment creates or rebinds a '
                  'name; it does not require a declaration and it does not permanently attach a '
                  'type to the name.',
                  'Rebinding changes which object a name refers to. Augmented assignment such as '
                  '`+=` is the idiomatic way to update counters and accumulators.',
                  "Use clear names for values that matter later. Python's flexibility makes naming "
                  'more important, not less.',
                  'Use assignment when a value needs a name for reuse or explanation. Prefer a '
                  'direct expression when naming the intermediate value would add noise.'],
  'notes': ['Python variables are names bound to objects, not boxes with fixed types.',
            'Rebinding a name is normal.',
            'Use augmented assignment for counters and accumulators.'],
  'see_also': ['values', 'mutability', 'object-lifecycle', 'constants'],
  'cells': [{'kind': 'cell',
             'prose': ['Assignment binds a name to a value. Once bound, the name can be used '
                       'anywhere that value is needed.'],
             'code': 'message = "hi"\nprint(message)',
             'output': 'hi'},
            {'kind': 'cell',
             'prose': ['Assignment can rebind the same name to a different value. The name is not '
                       'permanently attached to the first object.'],
             'code': 'message = "hello"\nprint(message)',
             'output': 'hello'},
            {'kind': 'cell',
             'prose': ['Augmented assignment reads the current binding, computes an updated value, '
                       'and stores the result back under the same name.'],
             'code': 'count = 3\ncount += 1\nprint(count)',
             'output': '4'}],
  'code': 'message = "hi"\n'
          'print(message)\n'
          '\n'
          'message = "hello"\n'
          'print(message)\n'
          '\n'
          'count = 3\n'
          'count += 1\n'
          'print(count)\n',
  'expected_output': 'hi\nhello\n4\n'},
 {'slug': 'constants',
  'title': 'Constants',
  'section': 'Basics',
  'summary': 'Python uses naming conventions and optional types for values that should not change.',
  'doc_path': '/library/typing.html#typing.Final',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Final',
  'explanation': ['Python has no `const` keyword for ordinary names. Modules use all-caps names '
                  'such as `MAX_RETRIES` to say “treat this as fixed configuration, not changing '
                  'state.”',
                  'The interpreter will still let code rebind the name. That is why constants are '
                  'primarily an API and readability convention. If a project also uses static '
                  'typing, `Final` can make the convention machine-checkable.',
                  'Named constants remove magic values from code and give repeated literals one '
                  'place to change.'],
  'notes': ['Python constants are a convention, not a runtime lock.',
            'Use all-caps names for fixed module-level configuration.',
            'Add `Final` when static tooling should flag accidental rebinding.'],
  'see_also': ['variables', 'literal-and-final', 'type-hints'],
  'cells': [{'kind': 'cell',
             'prose': ['All-caps names communicate design intent: this value is configuration that '
                       'callers should treat as fixed.'],
             'code': 'MAX_RETRIES = 3\n'
                     '\n'
                     'for attempt in range(1, MAX_RETRIES + 1):\n'
                     '    print(f"attempt {attempt} of {MAX_RETRIES}")',
             'output': 'attempt 1 of 3\nattempt 2 of 3\nattempt 3 of 3'},
            {'kind': 'cell',
             'prose': ['Constants are useful when a repeated literal deserves a name at the domain '
                       'boundary.'],
             'code': 'API_VERSION = "2026-05"\nprint(API_VERSION)',
             'output': '2026-05'},
            {'kind': 'cell',
             'prose': ['`Final` lets type checkers reject reassignment, but Python still runs '
                       'ordinary rebinding at runtime.'],
             'code': 'from typing import Final\n'
                     '\n'
                     'MAX_RETRIES: Final = 3\n'
                     'MAX_RETRIES = 5\n'
                     'print(MAX_RETRIES)',
             'output': '5'}],
  'code': 'from typing import Final\n'
          '\n'
          'MAX_RETRIES: Final = 3\n'
          'API_VERSION = "2026-05"\n'
          '\n'
          'for attempt in range(1, MAX_RETRIES + 1):\n'
          '    print(f"attempt {attempt} of {MAX_RETRIES}")\n'
          '\n'
          'print(API_VERSION)\n'
          '\n'
          'MAX_RETRIES = 5\n'
          'print(MAX_RETRIES)\n',
  'expected_output': 'attempt 1 of 3\nattempt 2 of 3\nattempt 3 of 3\n2026-05\n5\n'},
 {'slug': 'truthiness',
  'title': 'Truthiness',
  'section': 'Basics',
  'summary': 'Python conditions use truthiness, not only explicit booleans.',
  'doc_path': '/library/stdtypes.html#truth-value-testing',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing',
  'explanation': ["Truthiness is one of Python's most important conveniences: conditions can test "
                  'objects directly instead of requiring explicit boolean comparisons everywhere.',
                  'Empty containers, numeric zero, None, and False are false; most other values '
                  'are true. This makes common checks such as if items: concise and idiomatic.',
                  'Use truthiness when it reads naturally, but choose explicit comparisons when '
                  'the distinction matters, such as checking whether a value is exactly None.'],
  'notes': ['Empty containers and zero-like numbers are false in conditions.',
            'Use explicit comparisons when they communicate intent better than truthiness.'],
  'see_also': ['booleans', 'none', 'conditionals', 'special-methods'],
  'cells': [{'kind': 'cell',
             'prose': ['An empty list is false, so `not items` reads as "items is empty". The '
                       'condition tests the object directly — no `len(items) == 0` comparison is '
                       'needed.'],
             'code': 'items = []\nname = "Ada"\n\nif not items:\n    print("no items")',
             'output': 'no items'},
            {'kind': 'cell',
             'prose': ['A non-empty string is true, so `if name:` asks "did we get a name?" in one '
                       'word. Reach for an explicit comparison instead when the distinction '
                       'matters — `if name is not None:` treats an empty string differently from a '
                       'missing one.'],
             'code': 'if name:\n    print("has a name")',
             'output': 'has a name'},
            {'kind': 'cell',
             'prose': ['`bool()` reveals the truth value any condition would use. Zero-like '
                       'numbers convert to `False`; other numbers convert to `True`.'],
             'code': 'print(bool(0))\nprint(bool(42))',
             'output': 'False\nTrue'}],
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
  'expected_output': 'no items\nhas a name\nFalse\nTrue\n'},
 {'slug': 'equality-and-identity',
  'title': 'Equality and Identity',
  'section': 'Data Model',
  'summary': '== compares values, while is compares object identity.',
  'doc_path': '/reference/expressions.html#is-not',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#is-not',
  'explanation': ['Python separates equality from identity. Equality asks whether two objects '
                  'should be considered the same value, while identity asks whether two names '
                  'point to the same object.',
                  'This distinction matters for mutable containers because two equal lists can '
                  'still be independent objects. Mutating one should not imply mutating the other '
                  'unless they share identity.',
                  'The `is` operator is best reserved for identity checks against singletons such '
                  'as `None`. For ordinary values, `==` is the comparison readers expect.'],
  'notes': ['Use `==` for ordinary value comparisons.',
            'Use `is` primarily for identity checks against singletons such as `None`.',
            'Equal mutable containers can still be independent objects.',
            "Never use `is` to compare numbers; CPython's small-integer cache makes the result an "
            'implementation detail.'],
  'see_also': ['none', 'values', 'object-lifecycle', 'mutability'],
  'cells': [{'kind': 'cell',
             'prose': ['Equal containers can be different objects. `==` compares list contents, '
                       'while `is` checks whether both names refer to the same list object.'],
             'code': 'left = [1, 2, 3]\n'
                     'right = [1, 2, 3]\n'
                     'print(left == right)\n'
                     'print(left is right)',
             'output': 'True\nFalse'},
            {'kind': 'cell',
             'prose': ['Identity matters when objects are mutable. `same` is another name for '
                       '`left`, so mutating through one name changes the object seen through the '
                       'other.'],
             'code': 'same = left\nsame.append(4)\nprint(left)\nprint(same is left)',
             'output': '[1, 2, 3, 4]\nTrue'},
            {'kind': 'cell',
             'prose': ['Use `is` for singleton identity checks such as `None`. This asks whether '
                       'the value is the one special `None` object.'],
             'code': 'value = None\nprint(value is None)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ['`is` for integers is unreliable because CPython caches small integers '
                       '(roughly `-5` to `256`) but not larger ones. Two equal large integers can '
                       'be different objects. Use `==` for value comparisons; reserve `is` for '
                       'singletons.'],
             'code': 'small_a = 100\n'
                     'small_b = 100\n'
                     'print(small_a is small_b)\n'
                     '\n'
                     'big_a = int("1000")\n'
                     'big_b = int("1000")\n'
                     'print(big_a is big_b)\n'
                     'print(big_a == big_b)',
             'output': 'True\nFalse\nTrue'}],
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
          'print(value is None)\n'
          '\n'
          'small_a = 100\n'
          'small_b = 100\n'
          'print(small_a is small_b)\n'
          '\n'
          'big_a = int("1000")\n'
          'big_b = int("1000")\n'
          'print(big_a is big_b)\n'
          'print(big_a == big_b)\n',
  'expected_output': 'True\nFalse\n[1, 2, 3, 4]\nTrue\nTrue\nTrue\nFalse\nTrue\n'},
 {'slug': 'mutability',
  'title': 'Mutability',
  'section': 'Data Model',
  'summary': 'Some objects change in place, while others return new values.',
  'doc_path': '/reference/datamodel.html#objects-values-and-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types',
  'explanation': ['Objects in Python can be mutable or immutable. Mutable objects such as lists '
                  'and dictionaries can change in place, while immutable objects such as strings '
                  'and tuples produce new values instead.',
                  'Names can share one mutable object, so a change through one name is visible '
                  'through another. This is powerful, but it is also the source of many beginner '
                  'surprises.',
                  'The boundary matters across Python: `append()` mutates a list, string methods '
                  'return new strings, and `sorted()` returns a new list while `list.sort()` '
                  'mutates an existing one.'],
  'notes': ['Lists and dictionaries are mutable; strings and tuples are immutable.',
            'Aliasing is useful, but copy mutable containers when independent changes are needed.',
            'Pay attention to whether an operation mutates in place or returns a new value.'],
  'see_also': ['variables', 'object-lifecycle', 'copying-collections', 'lists'],
  'cells': [{'kind': 'cell',
             'prose': ['Mutable objects can change in place. `first` and `second` point to the '
                       'same list, so appending through one name changes the object seen through '
                       'both names.'],
             'code': 'first = ["python"]\n'
                     'second = first\n'
                     'second.append("workers")\n'
                     'print(first)\n'
                     'print(second)',
             'output': "['python', 'workers']\n['python', 'workers']"},
            {'kind': 'cell',
             'prose': ['Immutable objects do not change in place. String methods such as `upper()` '
                       'return a new string, leaving the original string unchanged.'],
             'code': 'text = "python"\nupper_text = text.upper()\nprint(text)\nprint(upper_text)',
             'output': 'python\nPYTHON'},
            {'kind': 'cell',
             'prose': ['Some APIs make the boundary explicit. `sorted()` returns a new list, while '
                       'methods such as `append()` and `list.sort()` mutate an existing list.'],
             'code': 'numbers = [3, 1, 2]\n'
                     'ordered = sorted(numbers)\n'
                     'print(ordered)\n'
                     'print(numbers)',
             'output': '[1, 2, 3]\n[3, 1, 2]'}],
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
  'expected_output': "['python', 'workers']\n"
                     "['python', 'workers']\n"
                     'python\n'
                     'PYTHON\n'
                     '[1, 2, 3]\n'
                     '[3, 1, 2]\n'},
 {'slug': 'object-lifecycle',
  'title': 'Object Lifecycle',
  'section': 'Basics',
  'summary': 'Names keep objects reachable until the last reference goes away.',
  'doc_path': '/reference/datamodel.html#objects-values-and-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types',
  'explanation': ['Python objects live independently from the names that refer to them. Assignment '
                  'adds another reference to an object; rebinding a name points that name '
                  'somewhere else; `del` removes a name. The object can be reclaimed only after it '
                  'is no longer reachable.',
                  'Most programs do not manually destroy objects. They control lifetime by '
                  'controlling which containers, local variables, and object attributes still hold '
                  'references.',
                  'This example uses a small class so the object has visible state. The important '
                  'evidence is that deleting one name does not destroy the object while another '
                  'name still refers to it.'],
  'notes': ['Assignment binds names to objects; it does not copy the object.',
            '`del name` removes one reference, not necessarily the object itself.',
            'Python reclaims unreachable objects automatically, so lifetime bugs usually come from '
            'keeping references longer than intended.'],
  'see_also': ['variables', 'mutability', 'classes'],
  'cells': [{'kind': 'cell',
             'prose': ['Two names can refer to the same object. Mutating through one name would '
                       'affect the object seen through the other.'],
             'code': 'class Box:\n'
                     '    def __init__(self, label):\n'
                     '        self.label = label\n'
                     '\n'
                     'box = Box("draft")\n'
                     'alias = box\n'
                     '\n'
                     'print(box is alias)\n'
                     'print(alias.label)',
             'output': 'True\ndraft'},
            {'kind': 'cell',
             'prose': ['Rebinding `box` does not change the original object. `alias` still reaches '
                       'the first `Box` until that reference is removed too.'],
             'code': 'box = Box("published")\n'
                     'print(alias.label)\n'
                     'print(box.label)\n'
                     '\n'
                     'del alias\n'
                     'print("old object unreachable")',
             'output': 'draft\npublished\nold object unreachable'}],
  'code': 'class Box:\n'
          '    def __init__(self, label):\n'
          '        self.label = label\n'
          '\n'
          'box = Box("draft")\n'
          'alias = box\n'
          '\n'
          'print(box is alias)\n'
          'print(alias.label)\n'
          '\n'
          'box = Box("published")\n'
          'print(alias.label)\n'
          'print(box.label)\n'
          '\n'
          'del alias\n'
          'print("old object unreachable")\n',
  'expected_output': 'True\ndraft\ndraft\npublished\nold object unreachable\n'},
 {'slug': 'strings',
  'title': 'Strings',
  'section': 'Text',
  'summary': 'Strings are immutable Unicode text sequences.',
  'doc_path': '/library/stdtypes.html#text-sequence-type-str',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#text-sequence-type-str',
  'explanation': ['Python strings are immutable Unicode text sequences. A `str` stores text as '
                  'Unicode code points, so it can represent English, Thai, accented letters, '
                  'emoji, and ordinary ASCII with the same type.',
                  'Unicode matters because text length and byte length are different questions. '
                  'The English word `"hello"` uses five code points and five UTF-8 bytes because '
                  'ASCII characters encode as one byte each. The Thai greeting `"สวัสดี"` has six '
                  'code points but needs eighteen UTF-8 bytes.',
                  'Use `str` when you mean text, and encode to `bytes` only at boundaries such as '
                  'files, network protocols, and binary APIs. String operations such as `upper()` '
                  'and `strip()` return new strings instead of changing the original.'],
  'notes': ['Use `str` for text and `bytes` for binary data.',
            '`len(text)` counts Unicode code points; `len(text.encode("utf-8"))` counts encoded '
            'bytes.',
            'ASCII text is a useful baseline because each ASCII code point is one UTF-8 byte.',
            'String methods return new strings because strings are immutable.',
            'User-visible “characters” can be more subtle than code points; combining marks and '
            'emoji sequences may need specialized text handling.'],
  'see_also': ['values', 'string-formatting', 'bytes-and-bytearray', 'regular-expressions'],
  'cells': [{'kind': 'cell',
             'prose': ['Compare three words by code-point count and UTF-8 byte count. ASCII '
                       'characters take one byte each (`hello` → 5 bytes); the `é` in `café` is '
                       'one code point but two UTF-8 bytes; each Thai character takes three. The '
                       '`str` type abstracts over all three.'],
             'code': 'english = "hello"\n'
                     'french = "café"\n'
                     'thai = "สวัสดี"\n'
                     '\n'
                     'for label, word in [("English", english), ("French", french), ("Thai", '
                     'thai)]:\n'
                     '    print(label, word, len(word), len(word.encode("utf-8")))',
             'output': 'English hello 5 5\nFrench café 4 5\nThai สวัสดี 6 18'},
            {'kind': 'cell',
             'prose': ['Indexing and iteration work with Unicode code points, not encoded bytes. '
                       '`ord()` returns the integer code point, which is often displayed in '
                       'hexadecimal when teaching text encoding.'],
             'code': 'print(thai[0])\nprint([hex(ord(char)) for char in thai[:2]])',
             'output': "ส\n['0xe2a', '0xe27']"},
            {'kind': 'cell',
             'prose': ['String methods return new strings because strings are immutable. Encoding '
                       'turns text into bytes when another system needs a byte representation.'],
             'code': 'text = "  café  "\n'
                     'clean = text.strip()\n'
                     'print(clean)\n'
                     'print(clean.upper())\n'
                     'print(clean.encode("utf-8"))',
             'output': "café\nCAFÉ\nb'caf\\xc3\\xa9'"}],
  'code': 'english = "hello"\n'
          'french = "café"\n'
          'thai = "สวัสดี"\n'
          '\n'
          'for label, word in [("English", english), ("French", french), ("Thai", thai)]:\n'
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
  'expected_output': 'English hello 5 5\n'
                     'French café 4 5\n'
                     'Thai สวัสดี 6 18\n'
                     'ส\n'
                     "['0xe2a', '0xe27']\n"
                     'café\n'
                     'CAFÉ\n'
                     "b'caf\\xc3\\xa9'\n"},
 {'slug': 'bytes-and-bytearray',
  'title': 'Bytes and Bytearray',
  'section': 'Text',
  'summary': 'bytes and bytearray store binary data, not Unicode text.',
  'doc_path': '/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview',
  'explanation': ['`str` stores Unicode text. `bytes` stores raw byte values. The boundary matters '
                  'whenever text leaves Python for a file, network protocol, subprocess, or binary '
                  'format.',
                  'Encoding turns text into bytes with a named encoding such as UTF-8. Decoding '
                  'turns bytes back into text. The lengths can differ because one Unicode '
                  'character may require several bytes.',
                  'Use immutable `bytes` for stable binary data and `bytearray` when the bytes '
                  'must be changed in place.'],
  'notes': ['Encode text when an external boundary needs bytes.',
            'Decode bytes when you want text again.',
            'Indexing `bytes` returns integers from 0 to 255.',
            'Use `bytearray` when binary data must be changed in place.'],
  'see_also': ['strings', 'literals', 'networking'],
  'cells': [{'kind': 'cell',
             'prose': ['Encode text when an external boundary needs bytes. UTF-8 uses one byte for '
                       'ASCII characters and more than one byte for many other characters.'],
             'code': 'text = "café"\n'
                     'data = text.encode("utf-8")\n'
                     'print(data)\n'
                     'print(len(text), len(data))',
             'output': "b'caf\\xc3\\xa9'\n4 5"},
            {'kind': 'cell',
             'prose': ['Decode bytes when the program needs text again. The decoder must match the '
                       'encoding used at the boundary.'],
             'code': 'print(data.decode("utf-8"))',
             'output': 'café'},
            {'kind': 'cell',
             'prose': ['Indexing a `bytes` object returns an integer byte value, not a '
                       'one-character `bytes` object.'],
             'code': 'print(data[0])',
             'output': '99'},
            {'kind': 'cell',
             'prose': ['`bytes` is immutable. Use `bytearray` when binary data must be changed in '
                       'place.'],
             'code': 'packet = bytearray(b"py")\npacket[0] = ord("P")\nprint(packet)',
             'output': "bytearray(b'Py')"}],
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
  'expected_output': "b'caf\\xc3\\xa9'\n4 5\ncafé\n99\nbytearray(b'Py')\n"},
 {'slug': 'string-formatting',
  'title': 'String Formatting',
  'section': 'Text',
  'summary': 'f-strings turn values into readable text at the point of use.',
  'doc_path': '/tutorial/inputoutput.html#formatted-string-literals',
  'doc_url': 'https://docs.python.org/3.13/tutorial/inputoutput.html#formatted-string-literals',
  'explanation': ['Formatted string literals, or f-strings, exist because programs constantly need '
                  'to turn values into human-readable text. They keep the expression next to the '
                  'words it explains.',
                  'Format specifications after `:` control presentation details such as width, '
                  'alignment, padding, and precision. This separates the value being computed from '
                  'the way it should be displayed.',
                  'Use f-strings for most new formatting code. They relate directly to '
                  'expressions: anything inside braces is evaluated, then formatted into the '
                  'surrounding string.'],
  'notes': ['Use `f"..."` strings for most new formatting code.',
            'Expressions inside braces are evaluated before formatting.',
            'Format specifications after `:` control alignment, width, padding, and precision.'],
  'see_also': ['strings', 'logging', 'csv-data', 'values'],
  'cells': [{'kind': 'cell',
             'prose': ['An f-string evaluates expressions inside braces and inserts their string '
                       'form into the surrounding text. This is clearer than joining several '
                       'converted values by hand.'],
             'code': 'name = "Ada"\n'
                     'score = 9.5\n'
                     'rank = 1\n'
                     '\n'
                     'message = f"{name} scored {score}"\n'
                     'print(message)',
             'output': 'Ada scored 9.5'},
            {'kind': 'cell',
             'prose': ['Format specifications after `:` control display without changing the '
                       'underlying values. Here the rank is right-aligned, the name is '
                       'left-aligned, and `05.1f` zero-pads the score to a width of five '
                       'characters with one decimal place.'],
             'code': 'row = f"{rank:>2} | {name:<8} | {score:05.1f}"\nprint(row)',
             'output': ' 1 | Ada      | 009.5'},
            {'kind': 'cell',
             'prose': ['The debug form with `=` is useful while learning or logging because it '
                       'prints both the expression and the value.'],
             'code': 'print(f"{score = }")',
             'output': 'score = 9.5'}],
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
  'expected_output': 'Ada scored 9.5\n 1 | Ada      | 009.5\nscore = 9.5\n'},
 {'slug': 'conditionals',
  'title': 'Conditionals',
  'section': 'Control Flow',
  'summary': 'if, elif, and else choose which block runs.',
  'doc_path': '/tutorial/controlflow.html#if-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#if-statements',
  'explanation': ['`if`, `elif`, and `else` let a program choose one path based on a condition. '
                  'Python uses indentation to show which statements belong to each branch.',
                  'Conditions use Python truthiness: booleans work directly, and many objects such '
                  'as empty lists or empty strings are considered false. Order branches from most '
                  'specific to most general.',
                  "Use `elif` to keep one decision flat instead of nested. Use Python's ternary "
                  'expression only when you are choosing between two values.'],
  'notes': ['Python has no mandatory parentheses around conditions; the colon and indentation '
            'define the block.',
            'Comparison operators such as `<` and `==` can be chained, as in `0 < value < 10`.',
            'Keep branch bodies short; move larger work into functions so the decision remains '
            'easy to scan.'],
  'see_also': ['booleans', 'truthiness', 'guard-clauses', 'match-statements'],
  'cells': [{'kind': 'cell',
             'prose': ['Start with the value that the branches will test. A conditional is only '
                       'useful when the branch condition is visible and meaningful.',
                       'Use `if`, `elif`, and `else` for one ordered choice. Python tests the '
                       'branches from top to bottom and runs only the first matching block.'],
             'code': 'temperature = 72\n'
                     '\n'
                     'if temperature < 60:\n'
                     '    print("cold")\n'
                     'elif temperature < 80:\n'
                     '    print("comfortable")\n'
                     'else:\n'
                     '    print("hot")',
             'output': 'comfortable'},
            {'kind': 'cell',
             'prose': ['Truthiness is part of conditional flow. Empty collections are false, so '
                       '`if items:` reads as “if there is anything to work with.”'],
             'code': 'items = ["coat", "hat"]\nif items:\n    print(f"packing {len(items)} items")',
             'output': 'packing 2 items'},
            {'kind': 'cell',
             'prose': ['Use the ternary expression when you are choosing a value. If either side '
                       'needs multiple statements, use a normal `if` block instead.'],
             'code': 'status = "ok" if temperature < 90 else "danger"\nprint(status)',
             'output': 'ok'}],
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
  'expected_output': 'comfortable\npacking 2 items\nok\n'},
 {'slug': 'guard-clauses',
  'title': 'Guard Clauses',
  'section': 'Control Flow',
  'summary': 'Guard clauses handle boundary cases early so the main path stays flat.',
  'doc_path': '/tutorial/controlflow.html#if-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#if-statements',
  'explanation': ['A guard clause is an early `return`, `raise`, `break`, or `continue` that '
                  'handles a case the rest of the function should not process. The point is not '
                  'new syntax; the point is moving boundaries out of the way so the successful '
                  'path can be read straight through.',
                  'Use guards when a function has clear invalid, empty, or already-finished cases. '
                  'If every branch is equally important, an ordinary `if`/`elif` chain may be '
                  'clearer.',
                  'The contrast below shows the payoff: the nested version makes the valid path '
                  'live inside two conditions, while the guard version names the invalid cases '
                  'first and leaves the calculation at the outer indentation level.'],
  'notes': ['Guard clauses are a readability pattern, not a separate Python feature.',
            'They work best when the early cases are true boundaries.',
            'For exceptional failures, raise an exception instead of returning a sentinel string.'],
  'see_also': ['conditionals', 'exceptions', 'functions'],
  'cells': [{'kind': 'cell',
             'prose': ['The nested version is correct, but the useful work is buried inside both '
                       'tests.'],
             'code': 'def nested_discount(price, percent):\n'
                     '    if price >= 0:\n'
                     '        if 0 <= percent <= 100:\n'
                     '            return round(price - price * percent / 100, 2)\n'
                     '        return "invalid discount"\n'
                     '    return "invalid price"\n'
                     '\n'
                     'print(nested_discount(100, 15))',
             'output': '85.0'},
            {'kind': 'cell',
             'prose': ['The guard-clause version handles impossible inputs first, then lets the '
                       'ordinary calculation sit at the top level of the function body.'],
             'code': 'def guarded_discount(price, percent):\n'
                     '    if price < 0:\n'
                     '        return "invalid price"\n'
                     '    if not 0 <= percent <= 100:\n'
                     '        return "invalid discount"\n'
                     '\n'
                     '    return round(price - price * percent / 100, 2)\n'
                     '\n'
                     'print(guarded_discount(-5, 10))\n'
                     'print(guarded_discount(100, 120))',
             'output': 'invalid price\ninvalid discount'}],
  'code': 'def nested_discount(price, percent):\n'
          '    if price >= 0:\n'
          '        if 0 <= percent <= 100:\n'
          '            return round(price - price * percent / 100, 2)\n'
          '        return "invalid discount"\n'
          '    return "invalid price"\n'
          '\n'
          '\n'
          'def guarded_discount(price, percent):\n'
          '    if price < 0:\n'
          '        return "invalid price"\n'
          '    if not 0 <= percent <= 100:\n'
          '        return "invalid discount"\n'
          '\n'
          '    return round(price - price * percent / 100, 2)\n'
          '\n'
          'print(nested_discount(100, 15))\n'
          'print(guarded_discount(-5, 10))\n'
          'print(guarded_discount(100, 120))\n',
  'expected_output': '85.0\ninvalid price\ninvalid discount\n'},
 {'slug': 'assignment-expressions',
  'title': 'Assignment Expressions',
  'section': 'Control Flow',
  'summary': 'The walrus operator assigns a value inside an expression.',
  'doc_path': '/reference/expressions.html#assignment-expressions',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#assignment-expressions',
  'explanation': ['The assignment expression operator `:=` assigns a name while evaluating an '
                  'expression. It is often called the walrus operator.',
                  'Use it when computing a value and testing it are naturally one step. Avoid it '
                  'when a separate assignment would make the code easier to read.',
                  'The boundary is readability: the walrus operator can remove duplication, but it '
                  'should not hide important state changes.'],
  'notes': ['`name := expression` assigns and evaluates to the assigned value.',
            'Use it to avoid computing the same value twice.',
            'Prefer a normal assignment when the expression becomes hard to scan.'],
  'see_also': ['conditionals', 'while-loops', 'variables'],
  'cells': [{'kind': 'cell',
             'prose': ['An assignment expression can name a computed value while a condition tests '
                       'it. Here empty strings are skipped because their length is zero.'],
             'code': 'messages = ["hello", "", "python"]\n'
                     '\n'
                     'for message in messages:\n'
                     '    if length := len(message):\n'
                     '        print(message, length)',
             'output': 'hello 5\npython 6'},
            {'kind': 'cell',
             'prose': ['The same idea works in loops that read state until a sentinel appears. The '
                       'assignment and comparison stay together.'],
             'code': 'queue = ["retry", "ok"]\n'
                     'while (status := queue.pop(0)) != "ok":\n'
                     '    print(status)\n'
                     'print(status)',
             'output': 'retry\nok'}],
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
  'expected_output': 'hello 5\npython 6\nretry\nok\n'},
 {'slug': 'for-loops',
  'title': 'For Loops',
  'section': 'Control Flow',
  'summary': 'for iterates over values produced by an iterable.',
  'doc_path': '/tutorial/controlflow.html#for-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#for-statements',
  'explanation': ['A `for` loop asks an iterable for values and runs the indented block once per '
                  "value. Python's loop is not primarily a numeric counter; it is a consumer of "
                  'lists, ranges, files, generators, and any object that implements the iterator '
                  'protocol.',
                  'Prefer direct iteration when you need each value. Use `range()` when the '
                  'numbers themselves are the data, and use `enumerate()` when the position and '
                  'the value both matter.',
                  'The loop body is the indented block. When the iterable is exhausted, execution '
                  'continues after the block. The neighboring `while` loop shape is for conditions '
                  'that must be rechecked manually.'],
  'notes': ['A `for` loop consumes an iterable until it is exhausted.',
            'Reach for `while` when the stopping condition must be rechecked manually.',
            '`iter()` and `next()` expose the protocol that `for` uses internally.'],
  'see_also': ['while-loops', 'iterating-over-iterables', 'iterators'],
  'cells': [{'kind': 'cell',
             'prose': ['Direct iteration keeps the code focused on the values in the collection.'],
             'code': 'for name in ["Ada", "Grace", "Guido"]:\n    print(name)',
             'output': 'Ada\nGrace\nGuido'},
            {'kind': 'cell',
             'prose': ['`range(3)` yields `0`, `1`, and `2` lazily. Use it when those integers are '
                       'the thing being iterated over.'],
             'code': 'for number in range(3):\n    print(number)',
             'output': '0\n1\n2'},
            {'kind': 'cell',
             'prose': ['`enumerate()` is the usual Python way to keep a counter beside each value '
                       'without indexing back into the list.'],
             'code': 'for index, name in enumerate(["Ada", "Grace"], start=1):\n'
                     '    print(index, name)',
             'output': '1 Ada\n2 Grace'}],
  'code': 'for name in ["Ada", "Grace", "Guido"]:\n'
          '    print(name)\n'
          '\n'
          'for number in range(3):\n'
          '    print(number)\n'
          '\n'
          'for index, name in enumerate(["Ada", "Grace"], start=1):\n'
          '    print(index, name)\n',
  'expected_output': 'Ada\nGrace\nGuido\n0\n1\n2\n1 Ada\n2 Grace\n'},
 {'slug': 'break-and-continue',
  'title': 'Break and Continue',
  'section': 'Control Flow',
  'summary': 'break exits a loop early, while continue skips to the next iteration.',
  'doc_path': '/tutorial/controlflow.html#break-and-continue-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements',
  'explanation': ['`break` and `continue` control the nearest enclosing loop. They exist for loops '
                  'whose body discovers an early stop rule or an item-level skip rule.',
                  'Use `continue` when the current item should not run the rest of the body. Use '
                  '`break` when no later item should be processed.',
                  'The alternative is ordinary `if`/`else` nesting. Prefer `break` and `continue` '
                  'when they keep the normal path flatter and easier to read.'],
  'notes': ['`continue` skips to the next loop iteration.',
            '`break` exits the nearest enclosing loop immediately.',
            'Prefer plain `if`/`else` when the loop does not need early skip or early stop '
            'behavior.'],
  'see_also': ['for-loops', 'while-loops', 'loop-else'],
  'cells': [{'kind': 'cell',
             'prose': ['`continue` skips the rest of the current iteration. The empty name is '
                       'ignored, and the loop moves on to the next value.'],
             'code': 'names = ["Ada", "", "Grace"]\n'
                     'for name in names:\n'
                     '    if not name:\n'
                     '        continue\n'
                     '    print(name)',
             'output': 'Ada\nGrace'},
            {'kind': 'cell',
             'prose': ['`break` exits the loop immediately. The value after `stop` is never '
                       'processed because the loop has already ended.'],
             'code': 'commands = ["load", "save", "stop", "delete"]\n'
                     'for command in commands:\n'
                     '    if command == "stop":\n'
                     '        break\n'
                     '    print(command)',
             'output': 'load\nsave'}],
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
  'expected_output': 'Ada\nGrace\nload\nsave\n'},
 {'slug': 'loop-else',
  'title': 'Loop Else',
  'section': 'Control Flow',
  'summary': 'A loop else block runs only when the loop did not end with break.',
  'doc_path': '/tutorial/controlflow.html#else-clauses-on-loops',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#else-clauses-on-loops',
  'explanation': ['Python loops can have an `else` clause. The name is surprising at first: loop '
                  '`else` means “no `break` happened,” not “the loop condition was false.”',
                  'This is useful for searches. Put the successful early exit in `break`, then put '
                  'the not-found path in `else`.',
                  'Use loop `else` sparingly. It is clearest when the loop is visibly searching '
                  'for something.'],
  'notes': ['Loop `else` runs when the loop was not ended by `break`.',
            'It is best for search loops with a clear found/not-found split.',
            'It works with both `for` and `while` loops.'],
  'see_also': ['break-and-continue', 'for-loops', 'while-loops'],
  'cells': [{'kind': 'cell',
             'prose': ['If the loop reaches `break`, the `else` block is skipped. This branch '
                       'means the search succeeded early.'],
             'code': 'names = ["Ada", "Grace", "Guido"]\n'
                     '\n'
                     'for name in names:\n'
                     '    if name == "Grace":\n'
                     '        print("found")\n'
                     '        break\n'
                     'else:\n'
                     '    print("missing")',
             'output': 'found'},
            {'kind': 'cell',
             'prose': ['If the loop finishes without `break`, the `else` block runs. This branch '
                       'means the search examined every value and found nothing.'],
             'code': 'for name in names:\n'
                     '    if name == "Linus":\n'
                     '        print("found")\n'
                     '        break\n'
                     'else:\n'
                     '    print("missing")',
             'output': 'missing'}],
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
  'expected_output': 'found\nmissing\n'},
 {'slug': 'iterating-over-iterables',
  'title': 'Iterating over Iterables',
  'section': 'Iteration',
  'summary': 'for loops consume values from any iterable object.',
  'doc_path': '/tutorial/controlflow.html#for-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#for-statements',
  'explanation': ["Python's `for` statement consumes values from any iterable object: lists, "
                  'strings, dictionaries, ranges, generators, files, and many standard-library '
                  'helpers.',
                  'This makes iteration a value-stream protocol rather than a special case for '
                  'arrays. The producer decides how values are made, and the loop consumes them '
                  'one at a time.',
                  'Use `enumerate()` when you need positions and values together, and '
                  '`dict.items()` when you need keys and values. These helpers express intent '
                  'better than manual indexing.'],
  'notes': ['A `for` loop consumes values from an iterable.',
            'Different producers can feed the same loop protocol.',
            'Prefer `enumerate()` over `range(len(...))` when you need an index.'],
  'see_also': ['iterators', 'iterator-vs-iterable', 'for-loops'],
  'cells': [{'kind': 'cell',
             'prose': ['Start with an ordinary list. A list stores values, and a `for` loop asks '
                       'it for one value at a time.',
                       'When you only need the values, iterate over the collection directly. There '
                       'is no index variable because the loop body does not need one.'],
             'code': 'names = ["Ada", "Grace", "Guido"]\n\nfor name in names:\n    print(name)',
             'output': 'Ada\nGrace\nGuido'},
            {'kind': 'cell',
             'prose': ['When you need both a position and a value, use `enumerate()`. It produces '
                       'index/value pairs without manual indexing.'],
             'code': 'for index, name in enumerate(names):\n    print(index, name)',
             'output': '0 Ada\n1 Grace\n2 Guido'},
            {'kind': 'cell',
             'prose': ['Dictionaries are iterable too, but `dict.items()` is the clearest way to '
                       'say that the loop needs keys and values together.'],
             'code': 'scores = {"Ada": 10, "Grace": 9}\n'
                     'for name, score in scores.items():\n'
                     '    print(name, score)',
             'output': 'Ada 10\nGrace 9'}],
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
  'expected_output': 'Ada\nGrace\nGuido\n0 Ada\n1 Grace\n2 Guido\nAda 10\nGrace 9\n'},
 {'slug': 'iterators',
  'title': 'Iterators',
  'section': 'Iteration',
  'summary': 'iter and next expose the protocol behind for loops.',
  'doc_path': '/library/stdtypes.html#iterator-types',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#iterator-types',
  'explanation': ['An iterable is an object that can produce values for a loop. An iterator is the '
                  'object that remembers where that production currently is.',
                  '`iter()` asks an iterable for an iterator, and `next()` consumes one value from '
                  'that iterator. A `for` loop performs those steps for you until the iterator is '
                  'exhausted.',
                  'This is the core value-stream protocol in Python: one object produces values, '
                  'another piece of code consumes them, and many streams are one-pass.'],
  'notes': ['Iterables produce iterators; iterators produce values.',
            '`next()` consumes one value from an iterator.',
            'Many iterators are one-pass even when the original collection is reusable.'],
  'see_also': ['iterating-over-iterables', 'iterator-vs-iterable', 'generators'],
  'cells': [{'kind': 'cell',
             'prose': ['`iter()` asks an iterable for an iterator. `next()` consumes one value and '
                       "advances the iterator's position."],
             'code': 'names = ["Ada", "Grace", "Guido"]\n'
                     'iterator = iter(names)\n'
                     'print(next(iterator))\n'
                     'print(next(iterator))',
             'output': 'Ada\nGrace'},
            {'kind': 'cell',
             'prose': ['A `for` loop consumes the same iterator protocol. Because two values were '
                       'already consumed, the loop sees only the remaining value.'],
             'code': 'for name in iterator:\n    print(name)',
             'output': 'Guido'},
            {'kind': 'cell',
             'prose': ['The list itself is reusable. Asking it for a fresh iterator starts a new '
                       'pass over the same stored values.'],
             'code': 'again = iter(names)\nprint(next(again))',
             'output': 'Ada'}],
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
  'expected_output': 'Ada\nGrace\nGuido\nAda\n'},
 {'slug': 'iterator-vs-iterable',
  'title': 'Iterator vs Iterable',
  'section': 'Iteration',
  'summary': 'Iterables produce fresh iterators; iterators are one-pass.',
  'doc_path': '/glossary.html#term-iterable',
  'doc_url': 'https://docs.python.org/3.13/glossary.html#term-iterable',
  'explanation': ['An iterable can produce values when asked. An iterator is the object that '
                  'remembers where the production currently is. The distinction matters because '
                  'iterables can be traversed many times, while many iterators can be traversed '
                  'only once.',
                  '`iter(iterable)` returns a fresh iterator each call. `iter(iterator)` returns '
                  'the iterator itself. That self-iteration property is how `for` loops can accept '
                  'either kind, and it is also why a function that loops over its argument twice '
                  'silently breaks when called with a generator instead of a list.',
                  'The takeaway for API design: receive iterables when the caller may want a '
                  'second pass, and materialize once at the boundary if you must.'],
  'notes': ['An iterable produces an iterator each time `iter()` is called on it; an iterator '
            'produces values until it is exhausted.',
            '`iter(iterable)` returns a fresh iterator; `iter(iterator)` returns the same '
            'iterator.',
            'Functions that traverse their input more than once must accept an iterable or '
            'materialize the input at the boundary.'],
  'see_also': ['iterators', 'iterating-over-iterables', 'generators'],
  'cells': [{'kind': 'cell',
             'prose': ['A list is iterable. Each `for` loop or `list()` call asks the list for a '
                       'fresh iterator under the hood, so the same data can be traversed many '
                       'times.'],
             'code': 'names = ["Ada", "Grace"]\nprint(list(names))\nprint(list(names))',
             'output': "['Ada', 'Grace']\n['Ada', 'Grace']"},
            {'kind': 'cell',
             'prose': ['An iterator is one-pass. Calling `iter()` returns a position-tracking '
                       'object; once it has been exhausted, it stays exhausted.'],
             'code': 'stream = iter(names)\nprint(list(stream))\nprint(list(stream))',
             'output': "['Ada', 'Grace']\n[]"},
            {'kind': 'cell',
             'prose': ['Calling `iter()` on an iterable returns a brand-new iterator each time. '
                       'Calling `iter()` on an iterator returns the same object — that is the rule '
                       'that lets a `for` loop accept either kind.'],
             'code': 'first = iter(names)\n'
                     'second = iter(names)\n'
                     'print(first is second)\n'
                     'print(iter(first) is first)',
             'output': 'False\nTrue'},
            {'kind': 'cell',
             'prose': ['The distinction shows up at API boundaries. A function that loops over its '
                       'argument twice works for an iterable but silently produces wrong answers '
                       'for an iterator, because the second pass finds the iterator already '
                       'exhausted. Materialize once at the boundary when both passes matter.'],
             'code': 'def total_and_count(numbers):\n'
                     '    total = sum(numbers)\n'
                     '    count = sum(1 for _ in numbers)\n'
                     '    return total, count\n'
                     '\n'
                     'def values():\n'
                     '    yield from [10, 9, 8]\n'
                     '\n'
                     'print(total_and_count([10, 9, 8]))\n'
                     'print(total_and_count(values()))\n'
                     '\n'
                     'def total_and_count_safe(numbers):\n'
                     '    items = list(numbers)\n'
                     '    return sum(items), len(items)\n'
                     '\n'
                     'print(total_and_count_safe(values()))',
             'output': '(27, 3)\n(27, 0)\n(27, 3)'}],
  'code': 'names = ["Ada", "Grace"]\n'
          '\n'
          'print(list(names))\n'
          'print(list(names))\n'
          '\n'
          'stream = iter(names)\n'
          'print(list(stream))\n'
          'print(list(stream))\n'
          '\n'
          'first = iter(names)\n'
          'second = iter(names)\n'
          'print(first is second)\n'
          'print(iter(first) is first)\n'
          '\n'
          'def total_and_count(numbers):\n'
          '    total = sum(numbers)\n'
          '    count = sum(1 for _ in numbers)\n'
          '    return total, count\n'
          '\n'
          'def values():\n'
          '    yield from [10, 9, 8]\n'
          '\n'
          'print(total_and_count([10, 9, 8]))\n'
          'print(total_and_count(values()))\n'
          '\n'
          'def total_and_count_safe(numbers):\n'
          '    items = list(numbers)\n'
          '    return sum(items), len(items)\n'
          '\n'
          'print(total_and_count_safe(values()))\n',
  'expected_output': "['Ada', 'Grace']\n"
                     "['Ada', 'Grace']\n"
                     "['Ada', 'Grace']\n"
                     '[]\n'
                     'False\n'
                     'True\n'
                     '(27, 3)\n'
                     '(27, 0)\n'
                     '(27, 3)\n'},
 {'slug': 'sentinel-iteration',
  'title': 'Sentinel Iteration',
  'section': 'Iteration',
  'summary': 'iter(callable, sentinel) repeats calls until a marker value appears.',
  'doc_path': '/library/functions.html#iter',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#iter',
  'explanation': ['`iter(callable, sentinel)` calls a zero-argument callable over and over. It '
                  'yields each result until the callable returns the sentinel value, and the '
                  'sentinel itself is not yielded.',
                  'This shape is useful for repeated reads: file blocks until `b""`, socket chunks '
                  'until an empty response, queue items until a stop marker. It removes the common '
                  '`while True` plus `break` scaffolding when the loop body is otherwise just '
                  '"read, then process".',
                  'The callable must take no arguments. Wrap a parameterized reader in a `lambda`, '
                  '`functools.partial`, or object method when the underlying API needs '
                  'parameters.'],
  'notes': ['The callable passed to `iter(callable, sentinel)` must take no arguments.',
            'The sentinel stops iteration and is not yielded.',
            'When the loop needs richer branching, an explicit `while` loop may be clearer.'],
  'see_also': ['iterators', 'while-loops', 'break-and-continue'],
  'cells': [{'kind': 'cell',
             'prose': ['The two-argument form turns a polling callable into an iterator. The empty '
                       'string stops the loop without appearing in the result.'],
             'code': 'chunks = iter(["py", "thon", ""])\n'
                     '\n'
                     '\n'
                     'def read_chunk():\n'
                     '    return next(chunks)\n'
                     '\n'
                     'print(list(iter(read_chunk, "")))',
             'output': "['py', 'thon']"},
            {'kind': 'cell',
             'prose': ['The equivalent manual loop needs an explicit read, comparison, and '
                       '`break`. Use this shape when the stop condition is more complicated than a '
                       'single sentinel value.'],
             'code': 'chunks = iter(["py", "thon", ""])\n'
                     'word = ""\n'
                     'while True:\n'
                     '    chunk = next(chunks)\n'
                     '    if chunk == "":\n'
                     '        break\n'
                     '    word += chunk\n'
                     'print(word)',
             'output': 'python'}],
  'code': 'chunks = iter(["py", "thon", ""])\n'
          '\n'
          '\n'
          'def read_chunk():\n'
          '    return next(chunks)\n'
          '\n'
          'print(list(iter(read_chunk, "")))\n'
          '\n'
          'chunks = iter(["py", "thon", ""])\n'
          'word = ""\n'
          'while True:\n'
          '    chunk = next(chunks)\n'
          '    if chunk == "":\n'
          '        break\n'
          '    word += chunk\n'
          'print(word)\n',
  'expected_output': "['py', 'thon']\npython\n"},
 {'slug': 'match-statements',
  'title': 'Match Statements',
  'section': 'Control Flow',
  'summary': 'match selects cases using structural pattern matching.',
  'doc_path': '/tutorial/controlflow.html#match-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#match-statements',
  'explanation': ['Structural pattern matching lets a program choose a branch based on the shape '
                  'of data. It is especially useful when commands, messages, or parsed data have a '
                  'few known forms.',
                  'A `case` pattern can both check constants and bind names. The move case checks '
                  'the action and extracts `x` and `y` in one readable step.',
                  'Order matters because Python tries cases from top to bottom. Specific shapes '
                  'should appear before broad fallback cases such as `_`.'],
  'notes': ['`match` compares structure, not just equality.',
            'Patterns can bind names such as `x` and `y` while matching.',
            'Mapping patterns match when the named keys are present; extra keys in the subject are '
            'ignored rather than failing the case.',
            'Put the catch-all `_` case last, because cases are tried from top to bottom.'],
  'see_also': ['conditionals', 'advanced-match-patterns', 'structured-data-shapes', 'dicts'],
  'cells': [{'kind': 'cell',
             'prose': ['Use `match` when the shape of a value is the decision. This command is a '
                       'dictionary with an action and coordinates; the first case checks that '
                       'shape and binds `x` and `y`.'],
             'code': 'command = {"action": "move", "x": 3, "y": 4}\n'
                     '\n'
                     'match command:\n'
                     '    case {"action": "move", "x": x, "y": y}:\n'
                     '        print(f"move to {x},{y}")',
             'output': 'move to 3,4'},
            {'kind': 'cell',
             'prose': ['Other cases describe other valid shapes. This complete fragment changes '
                       'the command so the `quit` case is the first matching pattern.'],
             'code': 'command = {"action": "quit"}\n'
                     '\n'
                     'match command:\n'
                     '    case {"action": "move", "x": x, "y": y}:\n'
                     '        print(f"move to {x},{y}")\n'
                     '    case {"action": "quit"}:\n'
                     '        print("quit")',
             'output': 'quit'},
            {'kind': 'cell',
             'prose': ['Broader patterns and the `_` catch-all belong after specific cases. This '
                       'fragment extracts an unknown action before the final fallback would run.'],
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
             'output': 'unknown action: jump'}],
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
  'expected_output': 'move to 3,4\n'},
 {'slug': 'advanced-match-patterns',
  'title': 'Advanced Match Patterns',
  'section': 'Control Flow',
  'summary': 'match patterns can destructure sequences, combine alternatives, and add guards.',
  'doc_path': '/tutorial/controlflow.html#match-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#match-statements',
  'explanation': ['Structural pattern matching is more than equality checks. Patterns can '
                  'destructure sequences, match several alternatives, capture the rest of a '
                  'sequence, and use guards.',
                  'Use these forms when the shape of data is the decision. If the decision is only '
                  'a single boolean condition, ordinary `if` statements are usually clearer.',
                  'The wildcard `_` catches everything not matched earlier.'],
  'notes': ['Use `case _` as a wildcard fallback.',
            'Guards refine a pattern after the structure matches.',
            'OR patterns and star patterns keep shape-based branches compact.'],
  'see_also': ['match-statements', 'tuples', 'classes'],
  'cells': [{'kind': 'cell',
             'prose': ['Sequence patterns match by position. A guard after `if` adds a condition '
                       'that must also be true.'],
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
             'output': 'move to 2,3'},
            {'kind': 'cell',
             'prose': ['An OR pattern accepts several alternatives in one case. A star pattern '
                       'captures the rest of a sequence.'],
             'code': 'print(describe(["exit"]))\nprint(describe(["echo", "hello", "python"]))',
             'output': 'stop\nhello python'},
            {'kind': 'cell',
             'prose': ['The wildcard `_` catches values that did not match earlier cases. Here the '
                       'guard rejects the negative coordinate.'],
             'code': 'print(describe(["move", -1, 3]))',
             'output': 'unknown'}],
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
  'expected_output': 'move to 2,3\nstop\nhello python\nunknown\n'},
 {'slug': 'while-loops',
  'title': 'While Loops',
  'section': 'Control Flow',
  'summary': 'while repeats until changing state makes a condition false.',
  'doc_path': '/reference/compound_stmts.html#while',
  'doc_url': 'https://docs.python.org/3.13/reference/compound_stmts.html#while',
  'explanation': ['A `while` loop repeats while a condition remains true. Unlike `for`, which '
                  'consumes an existing iterable, `while` is for state-driven repetition where the '
                  'next step depends on what happened so far.',
                  'The loop body must make progress toward stopping. That progress might be '
                  'decrementing a counter, reading until a sentinel value, or waiting until some '
                  'external state changes.',
                  'Reach for `for` when you already have values to consume. Reach for `while` when '
                  "the loop's own state decides whether another iteration is needed."],
  'notes': ['Use `while` when changing state decides whether the loop continues.',
            'Update loop state inside the body so the condition can become false.',
            'Prefer `for` when you already have a collection, range, iterator, or generator to '
            'consume.'],
  'see_also': ['for-loops', 'sentinel-iteration', 'break-and-continue'],
  'cells': [{'kind': 'cell',
             'prose': ['Use `while` when the condition, not an iterable, controls repetition. Here '
                       'the loop owns the countdown state and updates it each time through the '
                       'body.'],
             'code': 'remaining = 3\n'
                     'while remaining > 0:\n'
                     '    print(f"launch in {remaining}")\n'
                     '    remaining -= 1\n'
                     'print("liftoff")',
             'output': 'launch in 3\nlaunch in 2\nlaunch in 1\nliftoff'},
            {'kind': 'cell',
             'prose': ['A sentinel loop stops when a special value appears. The loop does not know '
                       'in advance how many retries it will need; it keeps going until the state '
                       'says to stop.'],
             'code': 'responses = iter(["retry", "retry", "ok"])\n'
                     'status = next(responses)\n'
                     'while status != "ok":\n'
                     '    print(f"status: {status}")\n'
                     '    status = next(responses)\n'
                     'print(f"status: {status}")',
             'output': 'status: retry\nstatus: retry\nstatus: ok'}],
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
  'expected_output': 'launch in 3\n'
                     'launch in 2\n'
                     'launch in 1\n'
                     'liftoff\n'
                     'status: retry\n'
                     'status: retry\n'
                     'status: ok\n'},
 {'slug': 'lists',
  'title': 'Lists',
  'section': 'Collections',
  'summary': 'Lists are ordered, mutable collections.',
  'doc_path': '/tutorial/datastructures.html#more-on-lists',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#more-on-lists',
  'explanation': ["Lists are Python's general-purpose mutable sequence type. Use them when order "
                  'matters and the collection may grow, shrink, or be rearranged.',
                  'Indexing reads individual positions. `0` is the first item, and negative '
                  'indexes count backward from the end.',
                  'Mutation and copying matter: `append()` changes the list, while `sorted()` '
                  'returns a new ordered list and leaves the original alone.'],
  'notes': ['Lists are mutable sequences: methods such as `append()` change the list in place.',
            'Negative indexes count from the end.',
            '`sorted()` returns a new list; `list.sort()` sorts the existing list in place.'],
  'see_also': ['tuples', 'sets', 'slices', 'copying-collections'],
  'cells': [{'kind': 'cell',
             'prose': ['Create a list with square brackets. Because lists are mutable, `append()` '
                       'changes this same list object.'],
             'code': 'numbers = [3, 1, 4]\nnumbers.append(1)\n\nprint(numbers)',
             'output': '[3, 1, 4, 1]'},
            {'kind': 'cell',
             'prose': ['Use indexes to read positions. Negative indexes are convenient for reading '
                       'from the end.'],
             'code': 'print(numbers[0])\nprint(numbers[-1])',
             'output': '3\n1'},
            {'kind': 'cell',
             'prose': ['Use `sorted()` when you want an ordered copy and still need the original '
                       'order afterward.'],
             'code': 'print(sorted(numbers))\nprint(numbers)',
             'output': '[1, 1, 3, 4]\n[3, 1, 4, 1]'}],
  'code': 'numbers = [3, 1, 4]\n'
          'numbers.append(1)\n'
          '\n'
          'print(numbers)\n'
          'print(numbers[0])\n'
          'print(numbers[-1])\n'
          'print(sorted(numbers))\n'
          'print(numbers)\n',
  'expected_output': '[3, 1, 4, 1]\n3\n1\n[1, 1, 3, 4]\n[3, 1, 4, 1]\n'},
 {'slug': 'tuples',
  'title': 'Tuples',
  'section': 'Collections',
  'summary': 'Tuples group a fixed number of positional values.',
  'doc_path': '/tutorial/datastructures.html#tuples-and-sequences',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'explanation': ['Tuples are ordered, immutable sequences. They exist for small fixed groups '
                  'where position has meaning: coordinates, RGB colors, database rows, and '
                  'multiple return values.',
                  'Use lists for variable-length collections of similar items. Use tuples when the '
                  'number of positions is part of the data shape and unpacking can give each '
                  'position a useful name.',
                  'Because tuples are immutable, you cannot append or replace positions in place. '
                  'If the shape needs to grow or change, a list or dataclass is usually a better '
                  'fit.'],
  'notes': ['Tuples are immutable sequences with fixed length.',
            'Use tuples for small records where position has meaning.',
            'Use lists for variable-length collections of similar items.',
            "Reach for a dataclass or `NamedTuple` when fields deserve names everywhere they're "
            'used.'],
  'see_also': ['lists', 'unpacking', 'structured-data-shapes'],
  'cells': [{'kind': 'cell',
             'prose': ['Use a tuple for a fixed-size record where each position has a known '
                       'meaning. Unpacking turns those positions into names at the point of use.'],
             'code': 'point = (3, 4)\nx, y = point\nprint(x + y)',
             'output': '7'},
            {'kind': 'cell',
             'prose': ['Tuples are sequences, so indexing and `len()` work. They are different '
                       'from lists because their length and item references are fixed after '
                       'creation.'],
             'code': 'red = (255, 0, 0)\nprint(red[0])\nprint(len(red))',
             'output': '255\n3'},
            {'kind': 'cell',
             'prose': ['Tuples pair naturally with multiple return values and unpacking. If the '
                       'fields need names everywhere, graduate to a dataclass or named tuple.'],
             'code': 'record = ("Ada", 10)\nname, score = record\nprint(f"{name}: {score}")',
             'output': 'Ada: 10'},
            {'kind': 'cell',
             'prose': ['Lists and tuples carry different intent. A list holds a variable number of '
                       'similar items and grows with `append`; a tuple has a fixed shape where '
                       'each position has its own meaning, and unpacking gives those positions '
                       'names.'],
             'code': 'scores = [10, 9, 8]\n'
                     'scores.append(7)\n'
                     'print(scores)\n'
                     '\n'
                     'student = ("Ada", 2024, "math")\n'
                     'name, year, subject = student\n'
                     'print(name, year, subject)',
             'output': '[10, 9, 8, 7]\nAda 2024 math'}],
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
          'print(f"{name}: {score}")\n'
          '\n'
          'scores = [10, 9, 8]\n'
          'scores.append(7)\n'
          'print(scores)\n'
          '\n'
          'student = ("Ada", 2024, "math")\n'
          'name, year, subject = student\n'
          'print(name, year, subject)\n',
  'expected_output': '7\n255\n3\nAda: 10\n[10, 9, 8, 7]\nAda 2024 math\n'},
 {'slug': 'unpacking',
  'title': 'Unpacking',
  'section': 'Collections',
  'summary': 'Unpacking binds names from sequences and mappings concisely.',
  'doc_path': '/tutorial/datastructures.html#tuples-and-sequences',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'explanation': ['Unpacking binds multiple names from one iterable or mapping. It makes the '
                  'structure of data visible at the point where values are introduced.',
                  'Starred unpacking handles variable-length sequences by collecting the middle or '
                  'remaining values. This keeps common head-tail patterns readable.',
                  'Dictionary unpacking with ** connects structured data to function calls. It is '
                  'widely used in configuration, adapters, and code that bridges APIs.'],
  'notes': ['Starred unpacking collects the remaining values into a list.',
            'Dictionary unpacking with ** is common when calling functions with structured data.',
            'Prefer indexing when you need one position; prefer unpacking when naming several '
            'positions makes the shape clearer.'],
  'see_also': ['tuples', 'multiple-return-values', 'args-and-kwargs', 'dicts'],
  'cells': [{'kind': 'cell',
             'prose': ['Tuple unpacking assigns each position to a name in one statement: `x` '
                       'receives the first element of `point` and `y` the second. The assignment '
                       'fails loudly if the number of names and elements disagree, which catches '
                       'shape mistakes early.'],
             'code': 'point = (3, 4)\nx, y = point\nprint(x, y)',
             'output': '3 4'},
            {'kind': 'cell',
             'prose': ["The starred name collects however many elements the head and tail don't "
                       'claim — here `first` and `last` take the ends and `*middle` gathers the '
                       'rest into a list. The same list works whether it has four elements or '
                       'forty.'],
             'code': 'first, *middle, last = [1, 2, 3, 4]\nprint(first, middle, last)',
             'output': '1 [2, 3] 4'},
            {'kind': 'cell',
             'prose': ["`describe(**data)` spreads the dictionary's keys as keyword arguments, so "
                       'the call site never repeats `name=` and `language=` by hand. This is the '
                       'bridge between dict-shaped data (configuration, parsed JSON) and function '
                       'signatures.'],
             'code': 'def describe(name, language):\n'
                     '    print(name, language)\n'
                     '\n'
                     'data = {"name": "Ada", "language": "Python"}\n'
                     'describe(**data)',
             'output': 'Ada Python'}],
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
  'expected_output': '3 4\n1 [2, 3] 4\nAda Python\n'},
 {'slug': 'dicts',
  'title': 'Dictionaries',
  'section': 'Collections',
  'summary': 'Dictionaries map keys to values for records, lookup, and structured data.',
  'doc_path': '/tutorial/datastructures.html#dictionaries',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#dictionaries',
  'explanation': ["Dictionaries are Python's built-in mapping type. They exist for data where "
                  'names or keys are more meaningful than numeric positions: records, lookup '
                  'tables, counters, and JSON-like payloads.',
                  'Use direct indexing when a key is required. Use `get()` when absence is '
                  'expected and the code has a reasonable fallback.',
                  'Unlike lists, dictionaries answer “what value belongs to this key?” rather than '
                  '“what value is at this position?” Iterating with `items()` keeps each key next '
                  'to its value.'],
  'notes': ['Dictionaries preserve insertion order in modern Python.',
            'Use `get()` when a missing key has a reasonable default.',
            'Use direct indexing when a missing key should be treated as an error.',
            'Snapshot keys with `list(d.keys())` before deleting items in a loop; adding or '
            'removing keys during iteration raises `RuntimeError`.'],
  'see_also': ['lists', 'sets', 'typed-dicts', 'json'],
  'cells': [{'kind': 'cell',
             'prose': ['Use a dictionary as a small record when fields have names. Direct indexing '
                       'communicates that the key is required, while `get()` communicates that a '
                       'missing key has a fallback.'],
             'code': 'profile = {"name": "Ada", "language": "Python"}\n'
                     'profile["year"] = 1843\n'
                     'print(profile["name"])\n'
                     'print(profile.get("timezone", "UTC"))',
             'output': 'Ada\nUTC'},
            {'kind': 'cell',
             'prose': ['Use a dictionary as a lookup table when keys identify values. This is '
                       'different from a list, where numeric position is the lookup key.'],
             'code': 'scores = {"Ada": 10, "Grace": 9}\n'
                     'print(scores["Grace"])\n'
                     'print(scores.get("Guido", 0))',
             'output': '9\n0'},
            {'kind': 'cell',
             'prose': ['Use `items()` when the loop needs both keys and values. It avoids looping '
                       'over keys and then indexing back into the dictionary.'],
             'code': 'for name, score in scores.items():\n    print(f"{name}: {score}")',
             'output': 'Ada: 10\nGrace: 9'},
            {'kind': 'cell',
             'prose': ['Adding or removing keys while iterating a dictionary raises `RuntimeError` '
                       '("dictionary changed size during iteration"); reassigning an existing '
                       "key's value is allowed. Snapshot the keys with `list(d.keys())` (or build "
                       'a list of changes and apply them after the loop) so deletions see a stable '
                       'view.'],
             'code': 'inventory = {"apple": 0, "pear": 3, "plum": 0}\n'
                     'for name in list(inventory.keys()):\n'
                     '    if inventory[name] == 0:\n'
                     '        del inventory[name]\n'
                     'print(inventory)',
             'output': "{'pear': 3}"}],
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
          '    print(f"{name}: {score}")\n'
          '\n'
          'inventory = {"apple": 0, "pear": 3, "plum": 0}\n'
          'for name in list(inventory.keys()):\n'
          '    if inventory[name] == 0:\n'
          '        del inventory[name]\n'
          'print(inventory)\n',
  'expected_output': "Ada\nUTC\n9\n0\nAda: 10\nGrace: 9\n{'pear': 3}\n"},
 {'slug': 'sets',
  'title': 'Sets',
  'section': 'Collections',
  'summary': 'Sets store unique values and make membership checks explicit.',
  'doc_path': '/tutorial/datastructures.html#sets',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#sets',
  'explanation': ['Sets store unique hashable values. Use them when membership and de-duplication '
                  'matter more than order.',
                  'A list can answer membership with `in`, but a set communicates that membership '
                  'is the main operation. Set algebra then expresses how groups relate to each '
                  'other.',
                  'Because sets are unordered, examples often wrap output in `sorted()` so the '
                  'display is deterministic.'],
  'notes': ['Use sets when uniqueness and membership are the main operations.',
            'Prefer lists when order or repeated values are part of the meaning.',
            'Sets are unordered, so sort them when examples need deterministic display.'],
  'see_also': ['lists', 'dicts', 'comprehensions'],
  'cells': [{'kind': 'cell',
             'prose': ['Creating a set removes duplicates. Keep a list when order and repeated '
                       'values matter; convert to a set when uniqueness is the point.'],
             'code': 'languages = ["python", "go", "python"]\n'
                     'unique_languages = set(languages)\n'
                     'print(sorted(unique_languages))',
             'output': "['go', 'python']"},
            {'kind': 'cell',
             'prose': ['Membership checks are the everyday set operation. A list can also use '
                       '`in`, but a set says that membership is central to the data shape.'],
             'code': 'allowed = {"python", "rust"}\n'
                     'print("python" in allowed)\n'
                     'print("ruby" in allowed)',
             'output': 'True\nFalse'},
            {'kind': 'cell',
             'prose': ['Union, intersection, and difference describe relationships between groups '
                       'without manual loops.'],
             'code': 'compiled = {"go", "rust"}\n'
                     'print(sorted(allowed | compiled))\n'
                     'print(sorted(allowed & compiled))\n'
                     'print(sorted(allowed - compiled))',
             'output': "['go', 'python', 'rust']\n['rust']\n['python']"}],
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
  'expected_output': "['go', 'python']\n"
                     'True\n'
                     'False\n'
                     "['go', 'python', 'rust']\n"
                     "['rust']\n"
                     "['python']\n"},
 {'slug': 'slices',
  'title': 'Slices',
  'section': 'Collections',
  'summary': 'Slices copy meaningful ranges from ordered sequences.',
  'doc_path': '/tutorial/introduction.html#lists',
  'doc_url': 'https://docs.python.org/3.13/tutorial/introduction.html#lists',
  'explanation': ['Slicing reads a range from an ordered sequence with `start:stop:step`. It '
                  'exists because Python code often needs a meaningful piece of a sequence: a '
                  'page, a prefix, a tail, a stride, or a reversed view.',
                  'The stop index is excluded. That convention makes lengths and adjacent ranges '
                  'line up: `items[:3]` and `items[3:]` split a sequence without overlap.',
                  'Slices return new sequence objects for built-in lists and strings. Use indexing '
                  'for one item; use slicing when the result should still be a sequence.'],
  'notes': ['Slice stop indexes are excluded, so adjacent ranges compose cleanly.',
            'Omitted bounds mean the beginning or end of the sequence.',
            'A negative step walks backward; `[::-1]` is a common reversed-copy idiom.'],
  'see_also': ['lists', 'tuples', 'strings'],
  'cells': [{'kind': 'cell',
             'prose': ['Omitted bounds mean “from the beginning” or “through the end.” Because the '
                       'stop index is excluded, adjacent slices split a sequence cleanly.'],
             'code': 'letters = ["a", "b", "c", "d", "e", "f"]\n'
                     'first_page = letters[:3]\n'
                     'rest = letters[3:]\n'
                     'print(first_page)\n'
                     'print(rest)',
             'output': "['a', 'b', 'c']\n['d', 'e', 'f']"},
            {'kind': 'cell',
             'prose': ['Use `start:stop` for a middle range and `step` when you want to skip or '
                       'walk backward. These operations return new lists; the original list is '
                       'unchanged.'],
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
                       "['a', 'b', 'c', 'd', 'e', 'f']"}],
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
                     "['a', 'b', 'c', 'd', 'e', 'f']\n"},
 {'slug': 'comprehensions',
  'title': 'Comprehensions',
  'section': 'Collections',
  'summary': 'Comprehensions build collections by mapping and filtering iterables.',
  'doc_path': '/tutorial/datastructures.html#list-comprehensions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions',
  'explanation': ['Comprehensions are expression forms for building concrete collections from '
                  'iterables. Read them from left to right: produce this value, for each item, '
                  'optionally only when a condition is true.',
                  'They are best for direct transformations where the expression is still easy to '
                  'scan. When the work needs several statements or names, an explicit loop is '
                  'usually clearer.',
                  'List, dictionary, and set comprehensions are eager: they build collections '
                  'immediately. Generator expressions use similar syntax to stream values later '
                  'and are covered in the Iteration section.'],
  'notes': ['The left side says what to produce; the `for` clause says where values come from.',
            'Use an `if` clause for simple filters.',
            'List, dict, and set comprehensions build concrete collections immediately.',
            'Switch to a loop when the transformation needs multiple steps or explanations.'],
  'see_also': ['for-loops', 'generator-expressions', 'comprehension-patterns', 'lists'],
  'cells': [{'kind': 'cell',
             'prose': ['A list comprehension maps each input item to one output item. This one '
                       'calls `title()` for every name and collects the results in a new list.'],
             'code': 'names = ["ada", "guido", "grace"]\n'
                     'titled = [name.title() for name in names]\n'
                     'print(titled)',
             'output': "['Ada', 'Guido', 'Grace']"},
            {'kind': 'cell',
             'prose': ['Add an `if` clause when only some items should appear. A dictionary '
                       'comprehension can transform key/value pairs while preserving the '
                       'dictionary shape.'],
             'code': 'scores = {"Ada": 10, "Guido": 8, "Grace": 10}\n'
                     'high_scores = {name: score for name, score in scores.items() if score >= '
                     '10}\n'
                     'print(high_scores)',
             'output': "{'Ada': 10, 'Grace': 10}"},
            {'kind': 'cell',
             'prose': ['A set comprehension keeps only unique results. Here two people have the '
                       'same score, so the resulting set has two values — printed through '
                       '`sorted()` because sets have no display order to rely on.'],
             'code': 'unique_scores = {score for score in scores.values()}\n'
                     'print(sorted(unique_scores))',
             'output': '[8, 10]'}],
  'code': 'names = ["ada", "guido", "grace"]\n'
          'titled = [name.title() for name in names]\n'
          'print(titled)\n'
          '\n'
          'scores = {"Ada": 10, "Guido": 8, "Grace": 10}\n'
          'high_scores = {name: score for name, score in scores.items() if score >= 10}\n'
          'print(high_scores)\n'
          '\n'
          'unique_scores = {score for score in scores.values()}\n'
          'print(sorted(unique_scores))\n',
  'expected_output': "['Ada', 'Guido', 'Grace']\n{'Ada': 10, 'Grace': 10}\n[8, 10]\n"},
 {'slug': 'comprehension-patterns',
  'title': 'Comprehension Patterns',
  'section': 'Collections',
  'summary': 'Comprehensions can use multiple for clauses and filters when the shape stays clear.',
  'doc_path': '/tutorial/datastructures.html#list-comprehensions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions',
  'explanation': ['Comprehensions can contain more than one `for` clause and more than one `if` '
                  'filter. The clauses are read in the same order as nested loops.',
                  'Use these forms only while the shape remains easy to scan. If a comprehension '
                  'starts needing several names, comments, or branches, an explicit loop is '
                  'usually better.',
                  'Nested comprehensions build concrete collections immediately, just like simpler '
                  'list, dict, and set comprehensions.'],
  'notes': ['Read comprehension clauses from left to right.',
            'Multiple `for` clauses act like nested loops.',
            'Prefer an explicit loop when the comprehension stops being obvious.'],
  'see_also': ['comprehensions', 'generator-expressions', 'for-loops'],
  'cells': [{'kind': 'cell',
             'prose': ['Multiple `for` clauses behave like nested loops. The leftmost `for` is the '
                       'outer loop, and the next `for` runs inside it.'],
             'code': 'colors = ["red", "blue"]\n'
                     'sizes = ["S", "M"]\n'
                     'variants = [(color, size) for color in colors for size in sizes]\n'
                     'print(variants)',
             'output': "[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]"},
            {'kind': 'cell',
             'prose': ['Multiple `if` clauses filter values. They are useful for simple '
                       'conditions, but an explicit loop is clearer when the rules need names or '
                       'explanation.'],
             'code': 'numbers = range(10)\n'
                     'filtered = [n for n in numbers if n % 2 == 0 if n > 2]\n'
                     'print(filtered)',
             'output': '[4, 6, 8]'}],
  'code': 'colors = ["red", "blue"]\n'
          'sizes = ["S", "M"]\n'
          'variants = [(color, size) for color in colors for size in sizes]\n'
          'print(variants)\n'
          '\n'
          'numbers = range(10)\n'
          'filtered = [n for n in numbers if n % 2 == 0 if n > 2]\n'
          'print(filtered)\n',
  'expected_output': "[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]\n[4, 6, 8]\n"},
 {'slug': 'sorting',
  'title': 'Sorting',
  'section': 'Collections',
  'summary': 'sorted returns a new ordered list and key functions choose the sort value.',
  'doc_path': '/howto/sorting.html',
  'doc_url': 'https://docs.python.org/3.13/howto/sorting.html',
  'explanation': ['`sorted()` accepts any iterable and returns a new list. The original collection '
                  'is left untouched, which makes `sorted()` useful in expressions and pipelines.',
                  'Use `key=` to say what value should be compared for each item. This is the '
                  'idiomatic way to sort records, tuples, dictionaries, and objects by a field.',
                  'Use `reverse=True` for descending order. Use `list.sort()` instead when you '
                  'intentionally want to mutate an existing list in place.'],
  'notes': ['`sorted()` makes a new list; `list.sort()` mutates an existing list.',
            '`key=` should return the value Python compares for each item.',
            "Python's sort is stable, so equal keys keep their original relative order."],
  'see_also': ['lists', 'lambdas', 'functions'],
  'cells': [{'kind': 'cell',
             'prose': ['`sorted()` returns a new list. Printing the original list afterward shows '
                       'that the input order did not change.'],
             'code': 'names = ["Guido", "Ada", "Grace"]\nprint(sorted(names))\nprint(names)',
             'output': "['Ada', 'Grace', 'Guido']\n['Guido', 'Ada', 'Grace']"},
            {'kind': 'cell',
             'prose': ['A key function computes the value to compare. Here the records are sorted '
                       'by score, highest first, and the output shows the resulting order.'],
             'code': 'users = [\n'
                     '    {"name": "Ada", "score": 10},\n'
                     '    {"name": "Guido", "score": 8},\n'
                     '    {"name": "Grace", "score": 10},\n'
                     ']\n'
                     'ranked = sorted(users, key=lambda user: user["score"], reverse=True)\n'
                     'print([user["name"] for user in ranked])',
             'output': "['Ada', 'Grace', 'Guido']"},
            {'kind': 'cell',
             'prose': ['`list.sort()` sorts the list in place. Use it when mutation is the point '
                       'and no separate sorted copy is needed.'],
             'code': 'users.sort(key=lambda user: user["name"])\n'
                     'print([user["name"] for user in users])',
             'output': "['Ada', 'Grace', 'Guido']"}],
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
                     "['Ada', 'Grace', 'Guido']\n"},
 {'slug': 'collections-module',
  'title': 'Collections Module',
  'section': 'Collections',
  'summary': 'collections provides specialized containers for common data shapes.',
  'doc_path': '/library/collections.html',
  'doc_url': 'https://docs.python.org/3.13/library/collections.html',
  'explanation': ['`collections` provides specialized containers for common shapes that would '
                  'otherwise require repetitive plumbing. Use it when the shape has a name: '
                  'counting, grouping, queueing, or lightweight records.',
                  'These types are not replacements for `list`, `dict`, `tuple`, and `set`. They '
                  'are small standard-library tools for cases where an ordinary container would '
                  'hide the intent behind manual bookkeeping.',
                  'The examples below map each type to the question it answers.'],
  'notes': ['`Counter` counts, `defaultdict` groups, `deque` queues, and `namedtuple` names record '
            'fields.',
            'Prefer the built-in containers until a specialized shape makes the code clearer.',
            'For new structured records with defaults and methods, consider `dataclasses` instead '
            'of `namedtuple`.'],
  'see_also': ['dicts', 'lists', 'tuples', 'sets'],
  'cells': [{'kind': 'cell',
             'prose': ['Use `Counter` when the question is "how many times did each value '
                       'appear?"'],
             'code': 'from collections import Counter\n'
                     '\n'
                     'counts = Counter("banana")\n'
                     'print(counts.most_common(2))',
             'output': "[('a', 3), ('n', 2)]"},
            {'kind': 'cell',
             'prose': ['Use `defaultdict(list)` when each key gathers multiple values and the '
                       'missing-key case should create an empty list automatically.'],
             'code': 'from collections import defaultdict\n'
                     '\n'
                     'groups = defaultdict(list)\n'
                     'for name, team in [("Ada", "red"), ("Grace", "blue"), ("Lin", "red")]:\n'
                     '    groups[team].append(name)\n'
                     'print(dict(groups))',
             'output': "{'red': ['Ada', 'Lin'], 'blue': ['Grace']}"},
            {'kind': 'cell',
             'prose': ['Use `deque` for queue operations at both ends, and `namedtuple` when a '
                       'tiny immutable record needs names as well as positions.'],
             'code': 'from collections import deque, namedtuple\n'
                     '\n'
                     'queue = deque(["first"])\n'
                     'queue.append("second")\n'
                     'print(queue.popleft())\n'
                     '\n'
                     'Point = namedtuple("Point", "x y")\n'
                     'print(Point(2, 3).x)',
             'output': 'first\n2'}],
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
  'expected_output': "[('a', 3), ('n', 2)]\n"
                     "{'red': ['Ada', 'Lin'], 'blue': ['Grace']}\n"
                     'first\n'
                     '2\n'},
 {'slug': 'copying-collections',
  'title': 'Copying Collections',
  'section': 'Collections',
  'summary': 'Copies can duplicate the outer container while nested objects may still be shared.',
  'doc_path': '/library/copy.html',
  'doc_url': 'https://docs.python.org/3.13/library/copy.html',
  'explanation': ['Copying answers two different questions: do you need a new outer container, or '
                  'do you also need independent nested objects? A plain assignment gives another '
                  'name for the same object. A shallow copy duplicates only the outer container. '
                  '`copy.deepcopy()` recursively copies contained objects.',
                  'Most Python code wants a shallow copy or a deliberate rebuild. Use a deep copy '
                  'only when shared nested state would be wrong and the objects involved are safe '
                  'to duplicate.',
                  'The outputs below show the footgun directly: a shallow copy has a different '
                  'outer list, but its inner lists are still the same objects.'],
  'notes': ['Assignment aliases; it does not copy.',
            'Shallow copies duplicate the outer container only.',
            'Deep copies are useful for nested independence, but they can be expensive and '
            'surprising for objects with external resources.'],
  'see_also': ['mutability', 'lists', 'dicts'],
  'cells': [{'kind': 'cell',
             'prose': ['Assignment does not copy a collection. It gives the same list another '
                       'name.'],
             'code': 'rows = [["Ada"], ["Grace"]]\nalias = rows\n\nprint(alias is rows)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ['A shallow copy creates a new outer list, but nested lists are still '
                       'shared.'],
             'code': 'shallow = rows.copy()\n'
                     'rows[0].append("Lovelace")\n'
                     '\n'
                     'print(shallow is rows)\n'
                     'print(rows[0] is shallow[0])\n'
                     'print(shallow)',
             'output': "False\nTrue\n[['Ada', 'Lovelace'], ['Grace']]"},
            {'kind': 'cell',
             'prose': ['A deep copy is independent at the nested level, so later mutation of '
                       '`rows[0]` does not appear in `deep`.'],
             'code': 'import copy\n'
                     '\n'
                     'rows = [["Ada"], ["Grace"]]\n'
                     'deep = copy.deepcopy(rows)\n'
                     'rows[0].append("Lovelace")\n'
                     '\n'
                     'print(rows[0] is deep[0])\n'
                     'print(deep)',
             'output': "False\n[['Ada'], ['Grace']]"}],
  'code': 'import copy\n'
          '\n'
          'rows = [["Ada"], ["Grace"]]\n'
          'alias = rows\n'
          'shallow = rows.copy()\n'
          'deep = copy.deepcopy(rows)\n'
          '\n'
          'rows[0].append("Lovelace")\n'
          '\n'
          'print(alias is rows)\n'
          'print(shallow is rows)\n'
          'print(rows[0] is shallow[0])\n'
          'print(rows[0] is deep[0])\n'
          'print(shallow)\n'
          'print(deep)\n',
  'expected_output': 'True\n'
                     'False\n'
                     'True\n'
                     'False\n'
                     "[['Ada', 'Lovelace'], ['Grace']]\n"
                     "[['Ada'], ['Grace']]\n"},
 {'slug': 'functions',
  'title': 'Functions',
  'section': 'Functions',
  'summary': 'Use def to name reusable behavior and return results.',
  'doc_path': '/tutorial/controlflow.html#defining-functions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions',
  'explanation': ['Functions package behavior behind a name. `def` creates a function object that '
                  'can accept arguments, compute values, and return a result.',
                  'Default arguments make common calls short, and keyword arguments make call '
                  'sites easier to read. A function that reaches the end without `return` produces '
                  '`None`.',
                  'Use functions when a calculation has a useful name, when code repeats, or when '
                  'a piece of behavior should be tested independently.'],
  'notes': ['Use `return` for values the caller should receive.',
            'Defaults keep common calls concise.',
            'Keyword arguments make options readable at the call site.',
            'Never use a mutable value as a default argument; use `None` and build the container '
            'inside the function body.'],
  'see_also': ['variables', 'args-and-kwargs', 'keyword-only-arguments', 'closures'],
  'cells': [{'kind': 'cell',
             'prose': ['`return` sends a value back to the caller. The caller can print it, store '
                       'it, or pass it to another function.'],
             'code': 'def greet(name):\n    return f"Hello, {name}."\n\nprint(greet("Python"))',
             'output': 'Hello, Python.'},
            {'kind': 'cell',
             'prose': ['Default arguments provide common values. Keyword arguments make it clear '
                       'which option is being overridden.'],
             'code': 'def format_total(amount, currency="USD"):\n'
                     '    return f"{amount} {currency}"\n'
                     '\n'
                     'print(format_total(10))\n'
                     'print(format_total(10, currency="EUR"))',
             'output': '10 USD\n10 EUR'},
            {'kind': 'cell',
             'prose': ['A function without an explicit `return` returns `None`. That makes '
                       'side-effect-only functions easy to distinguish from value-producing ones.'],
             'code': 'def log(message):\n'
                     '    print(f"log: {message}")\n'
                     '\n'
                     'result = log("saved")\n'
                     'print(result)',
             'output': 'log: saved\nNone'},
            {'kind': 'cell',
             'prose': ['Mutable default arguments are evaluated once when the function is defined, '
                       'not on each call. The same list is shared across calls, so successive '
                       "calls see each other's mutations. Use `None` as the sentinel and create a "
                       'fresh container inside the body.'],
             'code': 'def append_broken(item, items=[]):\n'
                     '    items.append(item)\n'
                     '    return items\n'
                     '\n'
                     'print(append_broken("a"))\n'
                     'print(append_broken("b"))\n'
                     '\n'
                     '\n'
                     'def append_fixed(item, items=None):\n'
                     '    if items is None:\n'
                     '        items = []\n'
                     '    items.append(item)\n'
                     '    return items\n'
                     '\n'
                     'print(append_fixed("a"))\n'
                     'print(append_fixed("b"))',
             'output': "['a']\n['a', 'b']\n['a']\n['b']"}],
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
          'print(result)\n'
          '\n'
          '\n'
          'def append_broken(item, items=[]):\n'
          '    items.append(item)\n'
          '    return items\n'
          '\n'
          'print(append_broken("a"))\n'
          'print(append_broken("b"))\n'
          '\n'
          '\n'
          'def append_fixed(item, items=None):\n'
          '    if items is None:\n'
          '        items = []\n'
          '    items.append(item)\n'
          '    return items\n'
          '\n'
          'print(append_fixed("a"))\n'
          'print(append_fixed("b"))\n',
  'expected_output': 'Hello, Python.\n'
                     '10 USD\n'
                     '10 EUR\n'
                     'log: saved\n'
                     'None\n'
                     "['a']\n"
                     "['a', 'b']\n"
                     "['a']\n"
                     "['b']\n"},
 {'slug': 'keyword-only-arguments',
  'title': 'Keyword-only Arguments',
  'section': 'Functions',
  'summary': 'Use * to require selected function arguments to be named.',
  'doc_path': '/tutorial/controlflow.html#special-parameters',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#special-parameters',
  'explanation': ['A bare `*` in a function signature marks the following parameters as '
                  'keyword-only. Callers must name those arguments explicitly.',
                  'Keyword-only arguments are useful for options such as timeouts, flags, and '
                  'modes where positional calls would be ambiguous or easy to misread.',
                  'They let the required data stay positional while optional controls remain '
                  'self-documenting at the call site.'],
  'notes': ['Put `*` before options that callers should name.',
            'Keyword-only flags avoid mysterious positional `True` and `False` arguments.',
            'Defaults work normally for keyword-only parameters.'],
  'see_also': ['functions', 'args-and-kwargs', 'positional-only-parameters', 'partial-functions'],
  'cells': [{'kind': 'cell',
             'prose': ['Parameters after `*` must be named. The default options still apply when '
                       'the caller omits them.'],
             'code': 'def connect(host, *, timeout=5, secure=True):\n'
                     '    scheme = "https" if secure else "http"\n'
                     '    print(f"{scheme}://{host} timeout={timeout}")\n'
                     '\n'
                     'connect("example.com")',
             'output': 'https://example.com timeout=5'},
            {'kind': 'cell',
             'prose': ['Naming the option makes the call site explicit. A reader does not have to '
                       'remember which positional slot controls the timeout.'],
             'code': 'connect("example.com", timeout=10)',
             'output': 'https://example.com timeout=10'},
            {'kind': 'cell',
             'prose': ['Flags are especially good keyword-only arguments because a bare positional '
                       '`False` is hard to interpret.'],
             'code': 'connect("localhost", secure=False)',
             'output': 'http://localhost timeout=5'},
            {'kind': 'cell',
             'prose': ['The bare `*` is enforced at the call site: passing the timeout '
                       'positionally raises `TypeError` instead of silently filling the wrong '
                       'slot.'],
             'code': 'try:\n'
                     '    connect("example.com", 10)\n'
                     'except TypeError as error:\n'
                     '    print(type(error).__name__)',
             'output': 'TypeError'}],
  'code': 'def connect(host, *, timeout=5, secure=True):\n'
          '    scheme = "https" if secure else "http"\n'
          '    print(f"{scheme}://{host} timeout={timeout}")\n'
          '\n'
          'connect("example.com")\n'
          'connect("example.com", timeout=10)\n'
          'connect("localhost", secure=False)\n'
          '\n'
          'try:\n'
          '    connect("example.com", 10)\n'
          'except TypeError as error:\n'
          '    print(type(error).__name__)\n',
  'expected_output': 'https://example.com timeout=5\n'
                     'https://example.com timeout=10\n'
                     'http://localhost timeout=5\n'
                     'TypeError\n'},
 {'slug': 'positional-only-parameters',
  'title': 'Positional-only Parameters',
  'section': 'Functions',
  'summary': 'Use / to mark parameters that callers must pass by position.',
  'doc_path': '/tutorial/controlflow.html#special-parameters',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#special-parameters',
  'explanation': ['A `/` in a function signature marks the parameters before it as '
                  'positional-only. Callers must pass those arguments by position, not by keyword.',
                  'This is useful when parameter names are implementation details or when an API '
                  'should match built-in functions that accept positional values.',
                  'Together, `/` and `*` let a signature draw clear boundaries: positional-only '
                  'inputs, ordinary inputs, and keyword-only options.'],
  'notes': ['`/` marks parameters before it as positional-only.',
            '`*` marks parameters after it as keyword-only.',
            'Use these markers when the call shape is part of the API design.'],
  'see_also': ['keyword-only-arguments', 'functions', 'args-and-kwargs'],
  'cells': [{'kind': 'cell',
             'prose': ['Parameters before `/` are positional-only. `value` is the main input, '
                       'while `factor` remains an ordinary parameter that can be named.'],
             'code': 'def scale(value, /, factor=2, *, clamp=False):\n'
                     '    result = value * factor\n'
                     '    if clamp:\n'
                     '        result = min(result, 10)\n'
                     '    return result\n'
                     '\n'
                     'print(scale(4))\n'
                     'print(scale(4, factor=3))',
             'output': '8\n12'},
            {'kind': 'cell',
             'prose': ['Parameters after `*` are keyword-only. That makes options such as `clamp` '
                       'explicit at the call site — here `4 * 3` would be `12`, and the clamp '
                       'visibly caps the result at `10`.'],
             'code': 'print(scale(4, factor=3, clamp=True))',
             'output': '10'},
            {'kind': 'cell',
             'prose': ['The restriction is enforced, not advisory: passing the positional-only '
                       '`value` by keyword raises `TypeError` at the call site.'],
             'code': 'try:\n'
                     '    scale(value=4)\n'
                     'except TypeError as error:\n'
                     '    print(type(error).__name__)',
             'output': 'TypeError'}],
  'code': 'def scale(value, /, factor=2, *, clamp=False):\n'
          '    result = value * factor\n'
          '    if clamp:\n'
          '        result = min(result, 10)\n'
          '    return result\n'
          '\n'
          'print(scale(4))\n'
          'print(scale(4, factor=3))\n'
          'print(scale(4, factor=3, clamp=True))\n'
          '\n'
          'try:\n'
          '    scale(value=4)\n'
          'except TypeError as error:\n'
          '    print(type(error).__name__)\n',
  'expected_output': '8\n12\n10\nTypeError\n'},
 {'slug': 'args-and-kwargs',
  'title': 'Args and Kwargs',
  'section': 'Functions',
  'summary': '*args collects extra positional arguments and **kwargs collects named ones.',
  'doc_path': '/tutorial/controlflow.html#arbitrary-argument-lists',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists',
  'explanation': ['`*args` and `**kwargs` let a function accept flexible positional and keyword '
                  'arguments. They are the function-definition counterpart to unpacking at a call '
                  'site.',
                  'These parameters are useful for wrappers, decorators, logging helpers, and APIs '
                  'that forward arguments to another function.',
                  'They should not replace clear signatures. If a function has a stable interface, '
                  'explicit parameters document expectations better than a bag of arguments.'],
  'notes': ['Use these tools when a function naturally accepts a flexible shape.',
            'Prefer explicit parameters when the accepted arguments are known and fixed.',
            '`*args` is a tuple; `**kwargs` is a dictionary.'],
  'see_also': ['functions', 'keyword-only-arguments', 'partial-functions', 'paramspec'],
  'cells': [{'kind': 'cell',
             'prose': ['`*args` collects extra positional arguments into a tuple. This fits '
                       'functions that naturally accept any number of similar values.'],
             'code': 'def total(*numbers):\n    return sum(numbers)\n\nprint(total(2, 3, 5))',
             'output': '10'},
            {'kind': 'cell',
             'prose': ['`**kwargs` collects named arguments into a dictionary. The names become '
                       'string keys.'],
             'code': 'def describe(**metadata):\n'
                     '    print(metadata)\n'
                     '\n'
                     'describe(owner="Ada", public=True)',
             'output': "{'owner': 'Ada', 'public': True}"},
            {'kind': 'cell',
             'prose': ['A function can combine explicit parameters, `*args`, and `**kwargs`. Put '
                       'the flexible parts last so the fixed shape remains visible.'],
             'code': 'def report(title, *items, **metadata):\n'
                     '    print(title)\n'
                     '    print(items)\n'
                     '    print(metadata)\n'
                     '\n'
                     'report("scores", 10, 9, owner="Ada")',
             'output': "scores\n(10, 9)\n{'owner': 'Ada'}"}],
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
  'expected_output': "10\n{'owner': 'Ada', 'public': True}\nscores\n(10, 9)\n{'owner': 'Ada'}\n"},
 {'slug': 'multiple-return-values',
  'title': 'Multiple Return Values',
  'section': 'Functions',
  'summary': 'Python returns multiple values by returning a tuple and unpacking it.',
  'doc_path': '/tutorial/datastructures.html#tuples-and-sequences',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'explanation': ['Python multiple return values are tuple return values with friendly syntax. '
                  '`return a, b` creates one tuple containing two positions.',
                  'Most callers unpack that tuple immediately. Good target names make the meaning '
                  'of each returned position explicit.',
                  'Use this for small, fixed groups of results. For larger records, a dataclass or '
                  'named tuple usually communicates better.'],
  'notes': ['A comma creates a tuple; `return a, b` returns one tuple containing two values.',
            'Unpacking at the call site gives each returned position a meaningful name.',
            'Use a class-like record when the result has many fields.'],
  'see_also': ['tuples', 'unpacking', 'functions'],
  'cells': [{'kind': 'cell',
             'prose': ['Returning values separated by commas returns one tuple. The tuple is '
                       'visible if the caller stores the result directly.'],
             'code': 'def divide_with_remainder(total, size):\n'
                     '    quotient = total // size\n'
                     '    remainder = total % size\n'
                     '    return quotient, remainder\n'
                     '\n'
                     'result = divide_with_remainder(17, 5)\n'
                     'print(result)',
             'output': '(3, 2)'},
            {'kind': 'cell',
             'prose': ['Callers usually unpack the tuple immediately or soon after. The names at '
                       'the call site document what each position means.'],
             'code': 'boxes, leftover = result\nprint(boxes)\nprint(leftover)',
             'output': '3\n2'}],
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
  'expected_output': '(3, 2)\n3\n2\n'},
 {'slug': 'closures',
  'title': 'Closures',
  'section': 'Functions',
  'summary': 'Inner functions can remember values from an enclosing scope.',
  'doc_path': '/reference/executionmodel.html#binding-of-names',
  'doc_url': 'https://docs.python.org/3.13/reference/executionmodel.html#binding-of-names',
  'explanation': ['A closure is a function that remembers names from the scope where it was '
                  'created. This lets you configure behavior once and call it later.',
                  'Each call to the outer function creates a separate remembered environment. That '
                  'is why `double` and `triple` can share the same code but keep different '
                  'factors.',
                  'Closures are a foundation for decorators, callbacks, and small function '
                  'factories.'],
  'notes': ['A closure keeps access to names from the scope where the inner function was created.',
            'Each call to the outer function can create a separate remembered environment.',
            'Closures are useful for callbacks, small factories, and decorators.',
            'Closures bind names, not values; capture loop variables with `lambda x=x: ...` to '
            'freeze them at definition time.'],
  'see_also': ['functions', 'lambdas', 'decorators', 'partial-functions'],
  'cells': [{'kind': 'cell',
             'prose': ['Define a function inside another function when the inner behavior needs to '
                       'remember setup from the outer call. The returned function keeps access to '
                       '`factor`.'],
             'code': 'def make_multiplier(factor):\n'
                     '    def multiply(value):\n'
                     '        return value * factor\n'
                     '    return multiply\n'
                     '\n'
                     'double = make_multiplier(2)\n'
                     'print(double(5))',
             'output': '10'},
            {'kind': 'cell',
             'prose': ['Calling the outer function again creates a separate closure. `triple` uses '
                       'the same inner code, but remembers a different `factor`.'],
             'code': 'triple = make_multiplier(3)\nprint(triple(5))',
             'output': '15'},
            {'kind': 'cell',
             'prose': ['Closures bind names, not values. Lambdas defined in a loop all reference '
                       'the same loop variable, so calling them later sees its final value. '
                       'Capture the value at definition time by binding it as a default argument — '
                       '`lambda i=i: i` — so each closure remembers its own `i`.'],
             'code': 'late = []\n'
                     'for i in range(3):\n'
                     '    late.append(lambda: i)\n'
                     'print([f() for f in late])\n'
                     '\n'
                     'bound = []\n'
                     'for i in range(3):\n'
                     '    bound.append(lambda i=i: i)\n'
                     'print([f() for f in bound])',
             'output': '[2, 2, 2]\n[0, 1, 2]'}],
  'code': 'def make_multiplier(factor):\n'
          '    def multiply(value):\n'
          '        return value * factor\n'
          '    return multiply\n'
          '\n'
          'double = make_multiplier(2)\n'
          'print(double(5))\n'
          '\n'
          'triple = make_multiplier(3)\n'
          'print(triple(5))\n'
          '\n'
          'late = []\n'
          'for i in range(3):\n'
          '    late.append(lambda: i)\n'
          'print([f() for f in late])\n'
          '\n'
          'bound = []\n'
          'for i in range(3):\n'
          '    bound.append(lambda i=i: i)\n'
          'print([f() for f in bound])\n',
  'expected_output': '10\n15\n[2, 2, 2]\n[0, 1, 2]\n'},
 {'slug': 'partial-functions',
  'title': 'Partial Functions',
  'section': 'Functions',
  'summary': 'functools.partial pre-fills arguments to make a more specific callable.',
  'doc_path': '/library/functools.html#functools.partial',
  'doc_url': 'https://docs.python.org/3.13/library/functools.html#functools.partial',
  'explanation': ['`functools.partial` turns a general callable into a more specific callable by '
                  'remembering some positional or keyword arguments. It is useful when another API '
                  'wants a one-argument callback but your underlying function needs more context.',
                  'A partial object is still callable. It keeps the original function in `.func`, '
                  'pre-filled positional arguments in `.args`, and pre-filled keyword arguments in '
                  '`.keywords`.',
                  'Prefer a named wrapper function when the adapted behavior needs branching, '
                  'validation, or a docstring. Use `partial` when the adaptation is simply "call '
                  'this function with these arguments already supplied."'],
  'notes': ['`partial` adapts a callable by pre-filling arguments.',
            'The resulting object can be passed anywhere a callable with the remaining parameters '
            'is expected.',
            'Use a regular function when the adapter needs more logic than argument binding.'],
  'see_also': ['functions', 'args-and-kwargs', 'callable-objects'],
  'cells': [{'kind': 'cell',
             'prose': ['Without `partial`, callers repeat the same fixed argument every time they '
                       'want the specialized behavior.'],
             'code': 'def apply_tax(rate, amount):\n'
                     '    return round(amount * (1 + rate), 2)\n'
                     '\n'
                     'print(apply_tax(0.2, 50))',
             'output': '60.0'},
            {'kind': 'cell',
             'prose': ['`partial` stores that fixed argument and returns a callable shaped for the '
                       'remaining arguments.'],
             'code': 'from functools import partial\n'
                     '\n'
                     'vat = partial(apply_tax, 0.2)\n'
                     'service_tax = partial(apply_tax, rate=0.1)\n'
                     '\n'
                     'print(vat(50))\n'
                     'print(service_tax(amount=80))',
             'output': '60.0\n88.0'},
            {'kind': 'cell',
             'prose': ['Partial objects expose the function and stored arguments, which is helpful '
                       'when debugging callback wiring.'],
             'code': 'print(vat.func.__name__)\nprint(vat.args)',
             'output': 'apply_tax\n(0.2,)'}],
  'code': 'from functools import partial\n'
          '\n'
          '\n'
          'def apply_tax(rate, amount):\n'
          '    return round(amount * (1 + rate), 2)\n'
          '\n'
          'vat = partial(apply_tax, 0.2)\n'
          'service_tax = partial(apply_tax, rate=0.1)\n'
          '\n'
          'print(apply_tax(0.2, 50))\n'
          'print(vat(50))\n'
          'print(service_tax(amount=80))\n'
          'print(vat.func.__name__)\n'
          'print(vat.args)\n',
  'expected_output': '60.0\n60.0\n88.0\napply_tax\n(0.2,)\n'},
 {'slug': 'scope-global-nonlocal',
  'title': 'Global and Nonlocal',
  'section': 'Functions',
  'summary': 'global and nonlocal choose which outer binding assignment should update.',
  'doc_path': '/reference/simple_stmts.html#the-global-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-global-statement',
  'explanation': ['Assignment normally creates or updates a local name inside the current '
                  'function. `global` and `nonlocal` are explicit escape hatches for rebinding '
                  'names outside that local scope.',
                  'Use `nonlocal` when an inner function should update a name in an enclosing '
                  'function. Use `global` rarely; passing values and returning results is usually '
                  'clearer.',
                  'These statements affect name binding, not object mutation. Mutating a shared '
                  'list is different from rebinding the name itself.'],
  'notes': ['Assignment inside a function is local unless declared otherwise.',
            'Prefer `nonlocal` for closure state and avoid `global` unless module state is truly '
            'intended.',
            'Passing values and returning results is usually easier to test than rebinding outer '
            'names.'],
  'see_also': ['variables', 'closures', 'functions'],
  'cells': [{'kind': 'cell',
             'prose': ['`global` tells assignment to update a module-level binding. Without it, '
                       '`count += 1` would try to assign a local `count`.'],
             'code': 'count = 0\n'
                     '\n'
                     'def bump_global():\n'
                     '    global count\n'
                     '    count += 1\n'
                     '\n'
                     'bump_global()\n'
                     'print(count)',
             'output': '1'},
            {'kind': 'cell',
             'prose': ['`nonlocal` tells assignment to update a binding in the nearest enclosing '
                       'function scope. This is useful for small closures that keep state.'],
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
             'output': '1\n2'}],
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
  'expected_output': '1\n1\n2\n'},
 {'slug': 'recursion',
  'title': 'Recursion',
  'section': 'Functions',
  'summary': 'Recursive functions solve nested problems by calling themselves on smaller pieces.',
  'doc_path': '/tutorial/controlflow.html#defining-functions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions',
  'explanation': ['A recursive function calls itself to solve a smaller piece of the same problem. '
                  'Recursion exists for data that is naturally nested: trees, menus, expression '
                  'nodes, and directory-like structures.',
                  'Every recursive function needs a base case that can be answered directly. The '
                  'recursive case must move toward that base case by passing a smaller part of the '
                  'data.',
                  'Prefer loops for simple repetition over a flat sequence. Prefer recursion when '
                  'the data shape is recursive too.'],
  'notes': ['Every recursive function needs a base case that stops the calls.',
            'Recursion fits nested data better than flat repetition.',
            'Python limits recursion depth, so loops are often better for very deep or simple '
            'repetition.'],
  'see_also': ['functions', 'conditionals', 'generators'],
  'cells': [{'kind': 'cell',
             'prose': ['A leaf node is the base case. It has no children, so the function can '
                       'return its own value without making another recursive call.'],
             'code': 'def total(node):\n'
                     '    subtotal = node["value"]\n'
                     '    for child in node["children"]:\n'
                     '        subtotal += total(child)\n'
                     '    return subtotal\n'
                     '\n'
                     'print(total({"value": 2, "children": []}))',
             'output': '2'},
            {'kind': 'cell',
             'prose': ['A non-leaf node solves the same problem for each child, then combines '
                       'those smaller totals with its own value.'],
             'code': 'tree = {\n'
                     '    "value": 1,\n'
                     '    "children": [\n'
                     '        {"value": 2, "children": []},\n'
                     '        {"value": 3, "children": [{"value": 4, "children": []}]},\n'
                     '    ],\n'
                     '}\n'
                     '\n'
                     'print(total(tree))',
             'output': '10'}],
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
  'expected_output': '2\n10\n'},
 {'slug': 'lambdas',
  'title': 'Lambdas',
  'section': 'Functions',
  'summary': 'lambda creates small anonymous function expressions.',
  'doc_path': '/tutorial/controlflow.html#lambda-expressions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#lambda-expressions',
  'explanation': ['`lambda` creates a small anonymous function expression. It is most useful when '
                  'Python asks for a function and the behavior is short enough to read inline.',
                  'A lambda can only contain one expression. Use `def` when the behavior deserves '
                  'a name, needs statements, or would be easier to test separately.',
                  'Lambdas often appear as key functions, callbacks, and tiny adapters. Keep them '
                  'simple enough that the call site remains clearer than a named helper.'],
  'notes': ['Lambdas are expressions, not statements.',
            'Prefer `def` for multi-step or reused behavior.',
            'Lambdas are common as `key=` functions because the behavior is local to one call.'],
  'see_also': ['functions', 'sorting', 'callable-objects'],
  'cells': [{'kind': 'cell',
             'prose': ['A lambda is a function expression. Assigning one to a name works, although '
                       '`def` is usually clearer for reusable behavior.'],
             'code': 'add_tax = lambda price: round(price * 1.08, 2)\nprint(add_tax(10))',
             'output': '10.8'},
            {'kind': 'cell',
             'prose': ['Lambdas are most idiomatic when passed directly to another function. '
                       '`sorted()` calls this key function once for each item.'],
             'code': 'items = [("notebook", 5), ("pen", 2), ("bag", 20)]\n'
                     'by_price = sorted(items, key=lambda item: item[1])\n'
                     'print(by_price)',
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]"},
            {'kind': 'cell',
             'prose': ['A named function is better when the behavior should be reused or '
                       'explained. It produces the same sort key, but gives the operation a name.'],
             'code': 'def price(item):\n    return item[1]\n\nprint(sorted(items, key=price))',
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]"}],
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
  'expected_output': '10.8\n'
                     "[('pen', 2), ('notebook', 5), ('bag', 20)]\n"
                     "[('pen', 2), ('notebook', 5), ('bag', 20)]\n"},
 {'slug': 'generators',
  'title': 'Generators',
  'section': 'Iteration',
  'summary': 'yield creates an iterator that produces values on demand.',
  'doc_path': '/tutorial/classes.html#generators',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#generators',
  'explanation': ['A generator function is a convenient way to write your own iterator. `yield` '
                  'produces one value, pauses the function, and resumes when the next value is '
                  'requested.',
                  'Generators are useful for pipelines, large inputs, and infinite sequences '
                  'because they avoid building an entire collection in memory.',
                  'Use `next()` to request one value manually, or loop over the generator to '
                  'consume values until it is exhausted.'],
  'notes': ['Generator functions are a concise way to create custom iterators; every generator is '
            'an iterator.',
            '`yield` defers work and streams values; `return` produces the whole result up front.',
            'A generator is consumed as you iterate over it.',
            'Prefer a list when you need to reuse stored results; prefer a generator when values '
            'can be streamed once.'],
  'see_also': ['iterators', 'iterator-vs-iterable', 'generator-expressions'],
  'cells': [{'kind': 'cell',
             'prose': ['Calling a generator function returns an iterator. `next()` asks for one '
                       'value and resumes the function until the next `yield`.'],
             'code': 'def countdown(n):\n'
                     '    while n > 0:\n'
                     '        yield n\n'
                     '        n -= 1\n'
                     '\n'
                     'numbers = countdown(3)\n'
                     'print(next(numbers))\n'
                     'print(next(numbers))',
             'output': '3\n2'},
            {'kind': 'cell',
             'prose': ['A `for` loop repeatedly calls `next()` for you. The loop stops when the '
                       'generator is exhausted.'],
             'code': 'for value in countdown(3):\n    print(value)',
             'output': '3\n2\n1'},
            {'kind': 'cell',
             'prose': ['`return` builds the entire result before handing it back; `yield` produces '
                       'values on demand. The list keeps its values for repeated use, while the '
                       'generator is exhausted after one pass.'],
             'code': 'def countdown_eager(n):\n'
                     '    result = []\n'
                     '    while n > 0:\n'
                     '        result.append(n)\n'
                     '        n -= 1\n'
                     '    return result\n'
                     '\n'
                     'values = countdown_eager(3)\n'
                     'print(values)\n'
                     'print(values)\n'
                     '\n'
                     'stream = countdown(3)\n'
                     'print(list(stream))\n'
                     'print(list(stream))',
             'output': '[3, 2, 1]\n[3, 2, 1]\n[3, 2, 1]\n[]'},
            {'kind': 'cell',
             'prose': ['Every generator is an iterator. The same countdown written by hand needs '
                       '`__iter__` and `__next__` and an explicit `StopIteration`. The generator '
                       'function expresses the same protocol with one `yield`.'],
             'code': 'class Countdown:\n'
                     '    def __init__(self, n):\n'
                     '        self.n = n\n'
                     '\n'
                     '    def __iter__(self):\n'
                     '        return self\n'
                     '\n'
                     '    def __next__(self):\n'
                     '        if self.n <= 0:\n'
                     '            raise StopIteration\n'
                     '        value = self.n\n'
                     '        self.n -= 1\n'
                     '        return value\n'
                     '\n'
                     'print(list(Countdown(3)))',
             'output': '[3, 2, 1]'}],
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
          '    print(value)\n'
          '\n'
          'def countdown_eager(n):\n'
          '    result = []\n'
          '    while n > 0:\n'
          '        result.append(n)\n'
          '        n -= 1\n'
          '    return result\n'
          '\n'
          'values = countdown_eager(3)\n'
          'print(values)\n'
          'print(values)\n'
          '\n'
          'stream = countdown(3)\n'
          'print(list(stream))\n'
          'print(list(stream))\n'
          '\n'
          'class Countdown:\n'
          '    def __init__(self, n):\n'
          '        self.n = n\n'
          '\n'
          '    def __iter__(self):\n'
          '        return self\n'
          '\n'
          '    def __next__(self):\n'
          '        if self.n <= 0:\n'
          '            raise StopIteration\n'
          '        value = self.n\n'
          '        self.n -= 1\n'
          '        return value\n'
          '\n'
          'print(list(Countdown(3)))\n',
  'expected_output': '3\n2\n3\n2\n1\n[3, 2, 1]\n[3, 2, 1]\n[3, 2, 1]\n[]\n[3, 2, 1]\n'},
 {'slug': 'yield-from',
  'title': 'Yield From',
  'section': 'Iteration',
  'summary': 'yield from delegates part of a generator to another iterable.',
  'doc_path': '/reference/expressions.html#yield-expressions',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#yield-expressions',
  'explanation': ['`yield from` lets one generator yield every value from another iterable. It is '
                  'a compact way to delegate part of a stream.',
                  'Use it when a generator is mostly stitching together other iterables or '
                  'sub-generators. It keeps the producer pipeline visible without writing a nested '
                  '`for` loop.',
                  'The consumer still sees one stream of values.'],
  'notes': ['`yield from iterable` yields each value from that iterable.',
            'It keeps generator pipelines compact.',
            'Use a plain `yield` when producing one value directly.'],
  'see_also': ['generators', 'generator-expressions', 'itertools'],
  'cells': [{'kind': 'cell',
             'prose': ['`yield from` delegates to another iterable. The caller receives one stream '
                       'even though part of it came from a list.'],
             'code': 'def page():\n'
                     '    yield "header"\n'
                     '    yield from ["intro", "body"]\n'
                     '    yield "footer"\n'
                     '\n'
                     'print(list(page()))',
             'output': "['header', 'intro', 'body', 'footer']"},
            {'kind': 'cell',
             'prose': ['Delegation is useful when flattening nested iterables. `yield from row` '
                       'replaces an inner loop that would yield each item by hand.'],
             'code': 'def flatten(rows):\n'
                     '    for row in rows:\n'
                     '        yield from row\n'
                     '\n'
                     'print(list(flatten([[1, 2], [3]])))',
             'output': '[1, 2, 3]'}],
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
  'expected_output': "['header', 'intro', 'body', 'footer']\n[1, 2, 3]\n"},
 {'slug': 'generator-expressions',
  'title': 'Generator Expressions',
  'section': 'Iteration',
  'summary': 'Generator expressions use comprehension-like syntax to stream values lazily.',
  'doc_path': '/tutorial/classes.html#generator-expressions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#generator-expressions',
  'explanation': ['Generator expressions look like list comprehensions with parentheses, but they '
                  'produce an iterator instead of building a concrete collection immediately.',
                  'Use them when a consumer such as `sum()`, `any()`, or a `for` loop can use '
                  'values one at a time. This keeps the transformation close to the consumer and '
                  'avoids storing intermediate lists.',
                  'Like other iterators, a generator expression is consumed as values are '
                  'requested. Create a new generator expression when you need another pass.'],
  'notes': ['List, dict, and set comprehensions build concrete collections.',
            'Generator expressions produce one-pass iterators.',
            'Use generator expressions when the consumer can process values one at a time.'],
  'see_also': ['comprehensions', 'generators', 'itertools', 'yield-from'],
  'cells': [{'kind': 'cell',
             'prose': ['A list comprehension is eager: it builds a list immediately. That is '
                       'useful when you need to store or reuse the results.'],
             'code': 'numbers = [1, 2, 3, 4]\n'
                     'list_squares = [number * number for number in numbers]\n'
                     'print(list_squares)',
             'output': '[1, 4, 9, 16]'},
            {'kind': 'cell',
             'prose': ['A generator expression is lazy: it creates an iterator that produces '
                       'values as they are consumed. After two `next()` calls, only the remaining '
                       'squares are left.'],
             'code': 'stream_squares = (number * number for number in numbers)\n'
                     'print(next(stream_squares))\n'
                     'print(next(stream_squares))\n'
                     'print(list(stream_squares))',
             'output': '1\n4\n[9, 16]'},
            {'kind': 'cell',
             'prose': ['Generator expressions are common inside reducing functions. When a '
                       'generator expression is the only argument, the extra parentheses can be '
                       'omitted.'],
             'code': 'print(sum(number * number for number in numbers))',
             'output': '30'}],
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
  'expected_output': '[1, 4, 9, 16]\n1\n4\n[9, 16]\n30\n'},
 {'slug': 'itertools',
  'title': 'Itertools',
  'section': 'Iteration',
  'summary': 'itertools composes lazy iterator streams.',
  'doc_path': '/library/itertools.html',
  'doc_url': 'https://docs.python.org/3.13/library/itertools.html',
  'explanation': ['The `itertools` module contains tools for composing iterator streams: '
                  'combining, slicing, grouping, and repeating values without changing the '
                  'consumer protocol.',
                  'Many `itertools` functions are lazy. They describe work to do later instead of '
                  'building a list immediately, so helpers such as `islice()` are useful when '
                  'taking a finite window.',
                  'Iterator pipelines let each step stay small: one object produces values, '
                  'another transforms them, and a final consumer such as `list()` or a loop pulls '
                  'values through the pipeline.'],
  'notes': ['`itertools` composes producer and transformer streams.',
            'Iterator pipelines avoid building intermediate lists.',
            'Use `islice()` to take a finite piece from an infinite iterator.',
            'Convert to a list only when you need concrete results.'],
  'see_also': ['iterators',
               'generator-expressions',
               'sentinel-iteration',
               'comprehension-patterns'],
  'cells': [{'kind': 'cell',
             'prose': ['`count()` can produce values forever, so `islice()` takes a finite window. '
                       'Nothing is materialized until `list()` consumes the iterator.'],
             'code': 'import itertools\n'
                     '\n'
                     'counter = itertools.count(10)\n'
                     'print(list(itertools.islice(counter, 3)))',
             'output': '[10, 11, 12]'},
            {'kind': 'cell',
             'prose': ['`chain()` presents several iterables as one stream. This avoids building '
                       'an intermediate list just to loop over combined inputs.'],
             'code': 'pages = itertools.chain(["intro", "setup"], ["deploy"])\nprint(list(pages))',
             'output': "['intro', 'setup', 'deploy']"},
            {'kind': 'cell',
             'prose': ['Iterator helpers compose with ordinary Python expressions. `compress()` '
                       'keeps items whose corresponding selector is true.'],
             'code': 'scores = [7, 10, 8, 10]\n'
                     'high_scores = itertools.compress(scores, [score >= 9 for score in scores])\n'
                     'print(list(high_scores))',
             'output': '[10, 10]'}],
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
  'expected_output': "[10, 11, 12]\n['intro', 'setup', 'deploy']\n[10, 10]\n"},
 {'slug': 'decorators',
  'title': 'Decorators',
  'section': 'Functions',
  'summary': 'Decorators wrap or register functions using @ syntax.',
  'doc_path': '/glossary.html#term-decorator',
  'doc_url': 'https://docs.python.org/3.13/glossary.html#term-decorator',
  'explanation': ['A decorator is a callable that receives a function and returns a replacement. '
                  'The `@` syntax applies that transformation at function definition time.',
                  'Decorators are common in frameworks because they can register handlers or add '
                  'behavior while keeping the decorated function focused on the core action.',
                  "`@decorator` is shorthand for rebinding a function to the decorator's return "
                  'value. Production wrappers usually use `functools.wraps` so debugging, help '
                  'text, and framework introspection still see the original function metadata.'],
  'notes': ['`@decorator` is shorthand for assigning `func = decorator(func)`.',
            'Decorators can wrap, replace, or register functions.',
            'Use `functools.wraps` in production wrappers that should preserve metadata.'],
  'see_also': ['closures', 'functions', 'callable-types', 'classmethods-and-staticmethods'],
  'cells': [{'kind': 'cell',
             'prose': ['A decorator is just a function that takes a function and returns another '
                       'callable. Applying it manually shows the wrapping step.'],
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
             'output': 'HELLO PYTHON'},
            {'kind': 'cell',
             'prose': ['The `@loud` syntax performs the same rebinding at definition time. After '
                       'decoration, `welcome` refers to the wrapper returned by `loud`.'],
             'code': '@loud\n'
                     'def welcome(name):\n'
                     '    """Return a welcome message."""\n'
                     '    return f"welcome {name}"\n'
                     '\n'
                     'print(welcome("workers"))',
             'output': 'WELCOME WORKERS'},
            {'kind': 'cell',
             'prose': ['`functools.wraps` copies useful metadata from the original function onto '
                       'the wrapper.'],
             'code': 'print(welcome.__name__)\nprint(welcome.__doc__)',
             'output': 'welcome\nReturn a welcome message.'}],
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
          'print(welcome.__name__)\n'
          'print(welcome.__doc__)\n',
  'expected_output': 'HELLO PYTHON\nWELCOME WORKERS\nwelcome\nReturn a welcome message.\n'},
 {'slug': 'classes',
  'title': 'Classes',
  'section': 'Classes',
  'summary': 'Classes bundle data and behavior into new object types.',
  'doc_path': '/tutorial/classes.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html',
  'explanation': ['Classes define new object types by bundling data with behavior. They are useful '
                  'when several values and operations belong together and should travel as one '
                  'object.',
                  'The alternative is often a dictionary plus separate functions. That is fine for '
                  'loose data, but a class gives the data a stable API and keeps behavior next to '
                  'the state it changes.',
                  '`__init__` initializes each instance, and methods receive the instance as '
                  '`self`. Separate instances keep separate state because each object has its own '
                  'attributes.'],
  'notes': ['`self` is the instance the method is operating on.',
            '`__init__` initializes each new object.',
            'Class attributes are shared across instances; instance attributes belong to one '
            'object.',
            'Put mutable defaults in `__init__`, not on the class body.',
            'Use classes when behavior belongs with state; use dictionaries for looser structured '
            'data.'],
  'see_also': ['inheritance-and-super',
               'classmethods-and-staticmethods',
               'bound-and-unbound-methods',
               'dataclasses'],
  'cells': [{'kind': 'cell',
             'prose': ['Define a class when data and behavior should travel together. The '
                       'initializer gives each object its starting state.'],
             'code': 'class Counter:\n'
                     '    def __init__(self, start=0):\n'
                     '        self.value = start\n'
                     '\n'
                     'first = Counter()\n'
                     'second = Counter(10)\n'
                     'print(first.value)\n'
                     'print(second.value)',
             'output': '0\n10'},
            {'kind': 'cell',
             'prose': ['Methods are functions attached to the class. `self` is the particular '
                       'object receiving the method call, so separate instances keep separate '
                       'state.'],
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
             'output': '1\n15'},
            {'kind': 'cell',
             'prose': ['A name defined directly on the class body is a class attribute, shared by '
                       'every instance. Reading falls back to the class when the instance has no '
                       'attribute of that name; assigning to the class itself changes the value '
                       'for every instance at once.'],
             'code': 'class Counter:\n'
                     '    step = 1\n'
                     '\n'
                     '    def __init__(self, start=0):\n'
                     '        self.value = start\n'
                     '\n'
                     'first = Counter()\n'
                     'second = Counter()\n'
                     'print(first.step)\n'
                     'Counter.step = 5\n'
                     'print(second.step)',
             'output': '1\n5'},
            {'kind': 'cell',
             'prose': ['A mutable class attribute is shared mutable state — the classic footgun. '
                       'Define per-instance containers in `__init__` so each object owns its own '
                       'copy.'],
             'code': 'class Cart:\n'
                     '    items = []\n'
                     '\n'
                     '    def add(self, item):\n'
                     '        self.items.append(item)\n'
                     '\n'
                     'shared_a = Cart()\n'
                     'shared_b = Cart()\n'
                     'shared_a.add("apple")\n'
                     'print(shared_b.items)\n'
                     '\n'
                     'class FixedCart:\n'
                     '    def __init__(self):\n'
                     '        self.items = []\n'
                     '\n'
                     '    def add(self, item):\n'
                     '        self.items.append(item)\n'
                     '\n'
                     'own_a = FixedCart()\n'
                     'own_b = FixedCart()\n'
                     'own_a.add("apple")\n'
                     'print(own_b.items)',
             'output': "['apple']\n[]"}],
  'code': 'class Counter:\n'
          '    step = 1\n'
          '\n'
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
          'print(second.increment(5))\n'
          'print(first.step)\n'
          'Counter.step = 5\n'
          'print(second.step)\n'
          '\n'
          'class Cart:\n'
          '    items = []\n'
          '\n'
          '    def add(self, item):\n'
          '        self.items.append(item)\n'
          '\n'
          'shared_a = Cart()\n'
          'shared_b = Cart()\n'
          'shared_a.add("apple")\n'
          'print(shared_b.items)\n'
          '\n'
          'class FixedCart:\n'
          '    def __init__(self):\n'
          '        self.items = []\n'
          '\n'
          '    def add(self, item):\n'
          '        self.items.append(item)\n'
          '\n'
          'own_a = FixedCart()\n'
          'own_b = FixedCart()\n'
          'own_a.add("apple")\n'
          'print(own_b.items)\n',
  'expected_output': "0\n10\n1\n15\n1\n5\n['apple']\n[]\n"},
 {'slug': 'inheritance-and-super',
  'title': 'Inheritance and Super',
  'section': 'Classes',
  'summary': 'Inheritance reuses behavior, and super delegates to a parent implementation.',
  'doc_path': '/tutorial/classes.html#inheritance',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#inheritance',
  'explanation': ['Inheritance lets one class specialize another class. The child class gets '
                  'parent behavior and can add or override methods.',
                  'Use `super()` when the child method should extend the parent implementation '
                  'instead of replacing it entirely.',
                  'Prefer composition when objects merely collaborate. Inheritance is best when '
                  'the child really is a specialized version of the parent.'],
  'notes': ['Inheritance models an “is a specialized kind of” relationship.',
            '`super()` calls the next implementation in the method resolution order.',
            'Prefer composition when an object only needs to use another object.'],
  'see_also': ['classes',
               'abstract-base-classes',
               'classmethods-and-staticmethods',
               'special-methods'],
  'cells': [{'kind': 'cell',
             'prose': ['A child class names its parent in parentheses. `Dog` instances get the '
                       '`Animal.__init__` method because `Dog` does not define its own '
                       'initializer.'],
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
             'output': 'Nina'},
            {'kind': 'cell',
             'prose': ['`super()` delegates to the parent implementation. The child method can '
                       'reuse the parent result and then add specialized behavior.'],
             'code': 'print(pet.speak())\nprint(isinstance(pet, Animal))',
             'output': 'Nina makes a sound; Nina barks\nTrue'}],
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
  'expected_output': 'Nina\nNina makes a sound; Nina barks\nTrue\n'},
 {'slug': 'classmethods-and-staticmethods',
  'title': 'Classmethods and Staticmethods',
  'section': 'Classes',
  'summary': 'Three method shapes: instance, class, and static — each receives a different first '
             'argument.',
  'doc_path': '/library/functions.html#classmethod',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#classmethod',
  'explanation': ['A regular method receives the instance as `self`. `@classmethod` makes a method '
                  'receive the class as `cls` instead, which is the standard shape for alternate '
                  'constructors. `@staticmethod` removes the implicit first argument entirely, '
                  'leaving a plain function attached to the class for namespacing.',
                  'The pressure that justifies the decorators is name organization. '
                  '`Date.from_string("2026-05-09")` reads better than a free-floating `parse_date` '
                  'function, and `Date.is_leap_year(2024)` keeps the helper next to the class it '
                  'belongs to even when the helper does not need any class state.',
                  'Pick instance methods when the work depends on instance state, classmethods '
                  'when an alternate constructor or class-level operation is the right shape, and '
                  'staticmethods when the function only happens to live near a class.'],
  'notes': ['Instance methods need an instance; classmethods and staticmethods can be called on '
            'the class.',
            'Use `@classmethod` for alternate constructors and class-level operations that respect '
            'subclassing.',
            'Use `@staticmethod` only when a function is truly independent of instance and class '
            "state but still belongs in the class's namespace.",
            'A free function is often the right answer when neither decorator applies.'],
  'see_also': ['classes', 'decorators', 'inheritance-and-super'],
  'cells': [{'kind': 'cell',
             'prose': ['An instance method receives the instance as `self` and reads its state. '
                       'This is the default and the right shape when the work depends on a '
                       "particular object's data."],
             'code': 'class Date:\n'
                     '    def __init__(self, year, month, day):\n'
                     '        self.year = year\n'
                     '        self.month = month\n'
                     '        self.day = day\n'
                     '\n'
                     '    def display(self):\n'
                     '        return f"{self.year}-{self.month:02d}-{self.day:02d}"\n'
                     '\n'
                     'today = Date(2026, 5, 9)\n'
                     'print(today.display())',
             'output': '2026-05-09'},
            {'kind': 'cell',
             'prose': ['`@classmethod` makes the method receive the class itself as `cls`. The '
                       'canonical use is an alternate constructor that parses some other input '
                       'format and calls `cls(...)`. Because `cls` is the actual class, subclasses '
                       'calling the same method get an instance of their own type.'],
             'code': 'class Date:\n'
                     '    def __init__(self, year, month, day):\n'
                     '        self.year = year\n'
                     '        self.month = month\n'
                     '        self.day = day\n'
                     '\n'
                     '    @classmethod\n'
                     '    def from_string(cls, text):\n'
                     '        year, month, day = (int(part) for part in text.split("-"))\n'
                     '        return cls(year, month, day)\n'
                     '\n'
                     'later = Date.from_string("2026-12-31")\n'
                     'print(later.year, later.month, later.day)',
             'output': '2026 12 31'},
            {'kind': 'cell',
             'prose': ['`@staticmethod` strips the implicit first argument. The function lives on '
                       'the class for namespacing — like `Date.is_leap_year(2024)` — but does not '
                       'touch any instance or class state.'],
             'code': 'class Date:\n'
                     '    @staticmethod\n'
                     '    def is_leap_year(year):\n'
                     '        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)\n'
                     '\n'
                     'print(Date.is_leap_year(2024))\n'
                     'print(Date.is_leap_year(2025))',
             'output': 'True\nFalse'},
            {'kind': 'cell',
             'prose': ['Side by side: instance methods receive the instance, classmethods receive '
                       'the class, staticmethods receive nothing. Classmethods and staticmethods '
                       'can be called on either the class or an instance.'],
             'code': 'class Demo:\n'
                     '    def instance_method(self):\n'
                     '        return type(self).__name__\n'
                     '\n'
                     '    @classmethod\n'
                     '    def class_method(cls):\n'
                     '        return cls.__name__\n'
                     '\n'
                     '    @staticmethod\n'
                     '    def static_method():\n'
                     '        return "no receiver"\n'
                     '\n'
                     'print(Demo().instance_method())\n'
                     'print(Demo.class_method())\n'
                     'print(Demo.static_method())',
             'output': 'Demo\nDemo\nno receiver'}],
  'code': 'class Date:\n'
          '    def __init__(self, year, month, day):\n'
          '        self.year = year\n'
          '        self.month = month\n'
          '        self.day = day\n'
          '\n'
          '    def display(self):\n'
          '        return f"{self.year}-{self.month:02d}-{self.day:02d}"\n'
          '\n'
          '    @classmethod\n'
          '    def from_string(cls, text):\n'
          '        year, month, day = (int(part) for part in text.split("-"))\n'
          '        return cls(year, month, day)\n'
          '\n'
          '    @staticmethod\n'
          '    def is_leap_year(year):\n'
          '        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)\n'
          '\n'
          'today = Date(2026, 5, 9)\n'
          'print(today.display())\n'
          '\n'
          'later = Date.from_string("2026-12-31")\n'
          'print(later.display())\n'
          '\n'
          'print(Date.is_leap_year(2024))\n'
          'print(Date.is_leap_year(2025))\n'
          '\n'
          'class Demo:\n'
          '    def instance_method(self):\n'
          '        return type(self).__name__\n'
          '\n'
          '    @classmethod\n'
          '    def class_method(cls):\n'
          '        return cls.__name__\n'
          '\n'
          '    @staticmethod\n'
          '    def static_method():\n'
          '        return "no receiver"\n'
          '\n'
          'print(Demo().instance_method())\n'
          'print(Demo.class_method())\n'
          'print(Demo.static_method())\n',
  'expected_output': '2026-05-09\n2026-12-31\nTrue\nFalse\nDemo\nDemo\nno receiver\n'},
 {'slug': 'dataclasses',
  'title': 'Dataclasses',
  'section': 'Classes',
  'summary': 'dataclass generates common class methods for data containers.',
  'doc_path': '/library/dataclasses.html',
  'doc_url': 'https://docs.python.org/3.13/library/dataclasses.html',
  'explanation': ['`dataclass` is a standard-library decorator for classes that mainly store data. '
                  'It generates methods such as `__init__` and `__repr__` from type-annotated '
                  'fields.',
                  'Dataclasses reduce boilerplate while keeping classes explicit. They are a good '
                  'fit for simple records, configuration objects, and values passed between '
                  'layers.',
                  'Type annotations define fields. Defaults work like normal class attributes and '
                  'appear in the generated initializer.'],
  'notes': ['Type annotations define dataclass fields.',
            'Dataclasses generate methods but remain normal Python classes.',
            'Use `field()` for advanced defaults such as per-instance lists or dictionaries.'],
  'see_also': ['structured-data-shapes', 'classes', 'type-hints'],
  'cells': [{'kind': 'cell',
             'prose': ['A dataclass uses annotations to define fields. Python generates an '
                       'initializer, so the class can be constructed without writing `__init__` by '
                       'hand.'],
             'code': 'from dataclasses import dataclass\n'
                     '\n'
                     '@dataclass\n'
                     'class User:\n'
                     '    name: str\n'
                     '    active: bool = True\n'
                     '\n'
                     'user = User("Ada")\n'
                     'print(user)',
             'output': "User(name='Ada', active=True)"},
            {'kind': 'cell',
             'prose': ['The generated instance still exposes ordinary attributes. A dataclass is a '
                       'regular class with useful methods filled in.'],
             'code': 'print(user.name)',
             'output': 'Ada'},
            {'kind': 'cell',
             'prose': ['Defaults can be overridden by keyword. The generated representation '
                       'includes the field names, which is useful during debugging.'],
             'code': 'inactive = User("Guido", active=False)\n'
                     'print(inactive)\n'
                     'print(inactive.active)',
             'output': "User(name='Guido', active=False)\nFalse"}],
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
  'expected_output': "User(name='Ada', active=True)\n"
                     'Ada\n'
                     "User(name='Guido', active=False)\n"
                     'False\n'},
 {'slug': 'properties',
  'title': 'Properties',
  'section': 'Classes',
  'summary': '@property keeps attribute syntax while adding computation or validation.',
  'doc_path': '/library/functions.html#property',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#property',
  'explanation': ['Properties let a class keep a simple attribute-style API while running code '
                  'behind the scenes. Callers write `box.area`, but the class can compute the '
                  'value from current state.',
                  'A property setter can validate assignment without changing the public spelling '
                  'of the attribute. This is the boundary: plain attributes are enough for plain '
                  'data, while properties are for computed or protected data.',
                  'Use properties for cheap, attribute-like operations. Expensive work or actions '
                  'with side effects should usually remain explicit methods.'],
  'notes': ['Properties let APIs start simple and grow validation or computation later.',
            'Callers access a property like an attribute, not like a method.',
            'Use methods instead when work is expensive or action-like.'],
  'see_also': ['classes', 'attribute-access', 'descriptors', 'dataclasses'],
  'cells': [{'kind': 'cell',
             'prose': ['A read-only property exposes computed data through attribute access. '
                       '`area` stays current because it is calculated from `width` and `height` '
                       'each time it is read.'],
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
             'output': '12'},
            {'kind': 'cell',
             'prose': ['A setter lets assignment keep normal attribute syntax while the class '
                       'validates or normalizes the value.'],
             'code': 'box.width = 5\nprint(box.area)',
             'output': '20'},
            {'kind': 'cell',
             'prose': ['Validation belongs inside the class when every caller should obey the same '
                       'rule. Invalid assignment raises an exception at the boundary.'],
             'code': 'try:\n    box.width = 0\nexcept ValueError as error:\n    print(error)',
             'output': 'width must be positive'}],
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
  'expected_output': '12\n20\nwidth must be positive\n'},
 {'slug': 'special-methods',
  'title': 'Special Methods',
  'section': 'Data Model',
  'summary': 'Special methods connect your objects to Python syntax and built-ins.',
  'doc_path': '/reference/datamodel.html#special-method-names',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#special-method-names',
  'explanation': ['Special methods, often called dunder methods, connect user-defined classes to '
                  'Python syntax and built-ins such as len(), iter(), and repr().',
                  'Implementing these methods lets your objects participate in Python protocols '
                  'rather than forcing callers to learn custom method names for common operations.',
                  'Good special methods make objects feel boring in the best way: they work with '
                  'the language features Python programmers already know.'],
  'notes': ["Dunder methods are looked up by Python's data model protocols.",
            '`__repr__` is the developer-facing form; `__str__` is the user-facing form. `print()` '
            'falls back to `__repr__` when `__str__` is missing.',
            'Defining `__eq__` removes the default `__hash__`; restore it when the type should be '
            'hashable.',
            'Container protocols (`__contains__`, `__getitem__`, `__setitem__`, `__bool__`) make '
            'instances behave like built-in containers.',
            '`__call__` makes instances callable; `__enter__`/`__exit__` make them context '
            'managers.',
            'Implement the smallest protocol that makes your object feel native.'],
  'see_also': ['container-protocols',
               'operator-overloading',
               'callable-objects',
               'context-managers'],
  'cells': [{'kind': 'cell',
             'prose': ['Start with a normal class that stores its data. Special methods build on '
                       'ordinary instance state.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(bag.items)',
             'output': "['a', 'b']"},
            {'kind': 'cell',
             'prose': ['Implement `__len__` to let `len()` ask the object for its size using '
                       "Python's standard protocol."],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(len(bag))',
             'output': '2'},
            {'kind': 'cell',
             'prose': ['Implement `__iter__` to make the object iterable. Then tools such as '
                       '`list()` can consume it without a custom method name.'],
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
             'output': "['a', 'b']"},
            {'kind': 'cell',
             'prose': ['Implement `__repr__` to give the object a useful developer-facing '
                       'representation when it is printed or inspected. With no `__str__` defined, '
                       '`print()` falls back to `__repr__`.'],
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
             'output': "Bag(['a', 'b'])"},
            {'kind': 'cell',
             'prose': ['Add `__str__` for an end-user representation. `print()` and `str()` prefer '
                       '`__str__`; `repr()` and the REPL still use `__repr__`. Keep `__repr__` '
                       'unambiguous for debugging and let `__str__` be the friendly form.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __repr__(self):\n'
                     '        return f"Bag({self.items!r})"\n'
                     '\n'
                     '    def __str__(self):\n'
                     '        return ", ".join(self.items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(bag)\n'
                     'print(repr(bag))',
             'output': "a, b\nBag(['a', 'b'])"},
            {'kind': 'cell',
             'prose': ['`__eq__` decides what equality means for the type. Defining `__eq__` '
                       'removes the default `__hash__`, so add `__hash__` back when instances '
                       'should work in sets or as dict keys — but only for types treated as '
                       'immutable: this `Bag` hashes its current items, so mutating one after '
                       'adding it to a set makes it unfindable. `__lt__` alone is enough for `<` '
                       'and for `sorted()`.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __eq__(self, other):\n'
                     '        return isinstance(other, Bag) and self.items == other.items\n'
                     '\n'
                     '    def __hash__(self):\n'
                     '        return hash(tuple(self.items))\n'
                     '\n'
                     '    def __lt__(self, other):\n'
                     '        return len(self.items) < len(other.items)\n'
                     '\n'
                     'print(Bag(["a", "b"]) == Bag(["a", "b"]))\n'
                     'print(Bag(["a"]) < Bag(["a", "b"]))\n'
                     'print(hash(Bag(["a"])) == hash(Bag(["a"])))',
             'output': 'True\nTrue\nTrue'},
            {'kind': 'cell',
             'prose': ['The container protocols make instances behave like built-in containers. '
                       '`__contains__` powers `in`, `__getitem__`/`__setitem__` power '
                       'subscription, and `__bool__` decides truthiness for `if` and `while`. See '
                       '[container-protocols](/examples/container-protocols) for the full '
                       'surface.'],
             'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __contains__(self, item):\n'
                     '        return item in self.items\n'
                     '\n'
                     '    def __getitem__(self, index):\n'
                     '        return self.items[index]\n'
                     '\n'
                     '    def __setitem__(self, index, value):\n'
                     '        self.items[index] = value\n'
                     '\n'
                     '    def __bool__(self):\n'
                     '        return bool(self.items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print("a" in bag)\n'
                     'print(bag[0])\n'
                     'bag[1] = "z"\n'
                     'print(bag.items)\n'
                     'print(bool(Bag([])))',
             'output': "True\na\n['a', 'z']\nFalse"},
            {'kind': 'cell',
             'prose': ['`__call__` makes an instance callable like a function — useful for '
                       'stateful operations whose configuration deserves a name. `__enter__` and '
                       '`__exit__` make a class a context manager so it can be used with `with`. '
                       'The focused [callable-objects](/examples/callable-objects) and '
                       '[context-managers](/examples/context-managers) pages go deeper.'],
             'code': 'class Multiplier:\n'
                     '    def __init__(self, factor):\n'
                     '        self.factor = factor\n'
                     '\n'
                     '    def __call__(self, value):\n'
                     '        return value * self.factor\n'
                     '\n'
                     'triple = Multiplier(3)\n'
                     'print(triple(5))\n'
                     '\n'
                     '\n'
                     'class Trace:\n'
                     '    def __enter__(self):\n'
                     '        print("enter")\n'
                     '        return self\n'
                     '\n'
                     '    def __exit__(self, *exc):\n'
                     '        print("exit")\n'
                     '        return False\n'
                     '\n'
                     'with Trace():\n'
                     '    print("inside")',
             'output': '15\nenter\ninside\nexit'}],
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
          '    def __str__(self):\n'
          '        return ", ".join(self.items)\n'
          '\n'
          '    def __eq__(self, other):\n'
          '        return isinstance(other, Bag) and self.items == other.items\n'
          '\n'
          '    def __hash__(self):\n'
          '        return hash(tuple(self.items))\n'
          '\n'
          '    def __lt__(self, other):\n'
          '        return len(self.items) < len(other.items)\n'
          '\n'
          '    def __contains__(self, item):\n'
          '        return item in self.items\n'
          '\n'
          '    def __getitem__(self, index):\n'
          '        return self.items[index]\n'
          '\n'
          '    def __setitem__(self, index, value):\n'
          '        self.items[index] = value\n'
          '\n'
          '    def __bool__(self):\n'
          '        return bool(self.items)\n'
          '\n'
          'bag = Bag(["a", "b"])\n'
          'print(len(bag))\n'
          'print(list(bag))\n'
          'print(bag)\n'
          'print(repr(bag))\n'
          'print(Bag(["a", "b"]) == Bag(["a", "b"]))\n'
          'print(Bag(["a"]) < Bag(["a", "b"]))\n'
          'print(hash(Bag(["a"])) == hash(Bag(["a"])))\n'
          'print("a" in bag)\n'
          'print(bag[0])\n'
          'bag[1] = "z"\n'
          'print(list(bag))\n'
          'print(bool(Bag([])))\n'
          '\n'
          '\n'
          'class Multiplier:\n'
          '    def __init__(self, factor):\n'
          '        self.factor = factor\n'
          '\n'
          '    def __call__(self, value):\n'
          '        return value * self.factor\n'
          '\n'
          'triple = Multiplier(3)\n'
          'print(triple(5))\n'
          '\n'
          '\n'
          'class Trace:\n'
          '    def __enter__(self):\n'
          '        print("enter")\n'
          '        return self\n'
          '\n'
          '    def __exit__(self, *exc):\n'
          '        print("exit")\n'
          '        return False\n'
          '\n'
          'with Trace():\n'
          '    print("inside")\n',
  'expected_output': '2\n'
                     "['a', 'b']\n"
                     'a, b\n'
                     "Bag(['a', 'b'])\n"
                     'True\n'
                     'True\n'
                     'True\n'
                     'True\n'
                     'a\n'
                     "['a', 'z']\n"
                     'False\n'
                     '15\n'
                     'enter\n'
                     'inside\n'
                     'exit\n'},
 {'slug': 'truth-and-size',
  'title': 'Truth and Size',
  'section': 'Data Model',
  'summary': '__bool__ and __len__ decide how objects behave in truth tests and len().',
  'doc_path': '/reference/datamodel.html#object.__bool__',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#object.__bool__',
  'explanation': ['Truth tests ask an object whether it should count as true. Containers usually '
                  'answer through their size, while domain objects can answer with `__bool__` when '
                  'emptiness is not the right idea.',
                  '`__len__` supports `len(obj)` and also provides a fallback truth value: length '
                  'zero is false, non-zero length is true. `__bool__` is more direct and wins when '
                  'both are present.',
                  'Use these methods to match the meaning of your object. A queue can be false '
                  'when it has no items; an account might be true only when it is active, '
                  'regardless of its balance.'],
  'notes': ['Prefer `__len__` for sized containers.',
            'Prefer `__bool__` when truth has domain meaning.',
            'Keep truth tests unsurprising; surprising falsy objects make conditionals harder to '
            'read.'],
  'see_also': ['truthiness', 'special-methods', 'container-protocols'],
  'cells': [{'kind': 'cell',
             'prose': ['`__len__` lets `len()` ask an object for its size.'],
             'code': 'class Inbox:\n'
                     '    def __init__(self, messages):\n'
                     '        self.messages = list(messages)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.messages)\n'
                     '\n'
                     'print(len(Inbox(["hi", "bye"])))',
             'output': '2'},
            {'kind': 'cell',
             'prose': ['If a class has `__len__` but no `__bool__`, Python uses zero length as '
                       'false.'],
             'code': 'print(bool(Inbox([])))',
             'output': 'False'},
            {'kind': 'cell',
             'prose': ['`__bool__` expresses truth directly when the answer is not just container '
                       'size.'],
             'code': 'class Account:\n'
                     '    def __init__(self, active):\n'
                     '        self.active = active\n'
                     '\n'
                     '    def __bool__(self):\n'
                     '        return self.active\n'
                     '\n'
                     'print(bool(Account(False)))',
             'output': 'False'}],
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
  'expected_output': '2\nFalse\nFalse\n'},
 {'slug': 'container-protocols',
  'title': 'Container Protocols',
  'section': 'Data Model',
  'summary': 'Container methods connect objects to indexing, membership, and item assignment.',
  'doc_path': '/reference/datamodel.html#emulating-container-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#emulating-container-types',
  'explanation': ['Container protocols let a class behave like the collection it represents. '
                  'Instead of inventing method names such as `has()` or `lookup()`, the object can '
                  'support `in`, indexing, and assignment.',
                  'The key methods are small and familiar: `__contains__` powers `in`, '
                  '`__getitem__` powers `obj[key]`, and `__setitem__` powers `obj[key] = value`. '
                  'Add only the operations the object can honestly support.',
                  "This keeps the public interface aligned with Python's built-in containers. "
                  'Callers can use the same syntax for custom records, caches, tables, and '
                  'sequence-like objects.'],
  'notes': ['Implement the narrowest container protocol your object needs.',
            'Use `KeyError` and `IndexError` consistently with built-in containers.',
            'If a plain `dict` or `list` is enough, prefer it over a custom container.'],
  'see_also': ['lists', 'dicts', 'special-methods'],
  'cells': [{'kind': 'cell',
             'prose': ['`__setitem__` gives assignment syntax to a custom container.'],
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
             'output': "{'Ada': 98}"},
            {'kind': 'cell',
             'prose': ['`__contains__` answers membership tests written with `in`.'],
             'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {"Ada": 98}\n'
                     '\n'
                     '    def __contains__(self, name):\n'
                     '        return name in self._scores\n'
                     '\n'
                     'scores = Scores()\n'
                     'print("Ada" in scores)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ['`__getitem__` connects bracket lookup to your internal storage.'],
             'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {"Ada": 98}\n'
                     '\n'
                     '    def __getitem__(self, name):\n'
                     '        return self._scores[name]\n'
                     '\n'
                     'scores = Scores()\n'
                     'print(scores["Ada"])',
             'output': '98'}],
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
  'expected_output': 'True\n98\n'},
 {'slug': 'callable-objects',
  'title': 'Callable Objects',
  'section': 'Data Model',
  'summary': '__call__ lets an instance behave like a function while keeping state.',
  'doc_path': '/reference/datamodel.html#object.__call__',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#object.__call__',
  'explanation': ['Functions are not the only callable objects in Python. Any instance can be '
                  'called with parentheses when its class defines `__call__`.',
                  'Callable objects are useful when behavior needs remembered configuration or '
                  'evolving state. A closure can do this too; a class is often clearer when the '
                  'state has multiple fields or needs named methods.',
                  'The tradeoff is ceremony. Use a function for simple behavior, a closure for '
                  'small captured state, and a callable object when naming the state improves the '
                  'interface.'],
  'notes': ['`callable(obj)` checks whether an object can be called.',
            'Callable objects are good for named, stateful behavior.',
            'Prefer plain functions when no instance state is needed.'],
  'see_also': ['functions', 'closures', 'callable-types', 'bound-and-unbound-methods'],
  'cells': [{'kind': 'cell',
             'prose': ['A callable object starts as ordinary state stored on an instance.'],
             'code': 'class Multiplier:\n'
                     '    def __init__(self, factor):\n'
                     '        self.factor = factor\n'
                     '        self.calls = 0\n'
                     '\n'
                     'double = Multiplier(2)\n'
                     'print(double.factor)',
             'output': '2'},
            {'kind': 'cell',
             'prose': ['`__call__` makes the instance usable with function-call syntax.'],
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
             'output': '10\n14'},
            {'kind': 'cell',
             'prose': ['Because the callable is still an object, it can remember state across '
                       'calls.'],
             'code': 'print(double.calls)',
             'output': '2'}],
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
  'expected_output': '10\n14\n2\n'},
 {'slug': 'operator-overloading',
  'title': 'Operator Overloading',
  'section': 'Data Model',
  'summary': 'Operator methods let objects define arithmetic and comparison syntax.',
  'doc_path': '/reference/datamodel.html#emulating-numeric-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#emulating-numeric-types',
  'explanation': ['Operator overloading lets a class define what expressions such as `a + b` mean '
                  'for its objects. This is useful when the operation is part of the domain '
                  'vocabulary.',
                  'The method should preserve the meaning readers expect from the operator. '
                  'Vectors can add component by component; money can add amounts in the same '
                  'currency; surprising overloads make code harder to trust.',
                  'Python also has reflected methods such as `__radd__` for cases where the left '
                  'operand does not know how to handle the right operand. That keeps mixed '
                  'operations possible without making every type know every other type.'],
  'notes': ['Overload operators only when the operation is unsurprising.',
            'Return `NotImplemented` when an operand type is unsupported.',
            'Implement equality deliberately when value comparison matters.'],
  'see_also': ['operators', 'special-methods', 'equality-and-identity'],
  'cells': [{'kind': 'cell',
             'prose': ['`__add__` defines how the `+` operator combines two objects. Checking the '
                       'operand type and returning `NotImplemented` for foreign types lets Python '
                       "try the other operand's reflected method instead of crashing inside "
                       'yours.'],
             'code': 'class Vector:\n'
                     '    def __init__(self, x, y):\n'
                     '        self.x = x\n'
                     '        self.y = y\n'
                     '\n'
                     '    def __add__(self, other):\n'
                     '        if not isinstance(other, Vector):\n'
                     '            return NotImplemented\n'
                     '        return Vector(self.x + other.x, self.y + other.y)\n'
                     '\n'
                     '    def __repr__(self):\n'
                     '        return f"Vector({self.x}, {self.y})"\n'
                     '\n'
                     'print(Vector(2, 3) + Vector(4, 5))',
             'output': 'Vector(6, 8)'},
            {'kind': 'cell',
             'prose': ['`__eq__` defines value equality for `==`. Without it, user-defined objects '
                       'compare by identity. Returning `NotImplemented` for foreign types matters '
                       'most here: equality against an unrelated value should answer `False`, '
                       'never raise — Python falls back to identity when both sides decline.'],
             'code': 'class Vector:\n'
                     '    def __init__(self, x, y):\n'
                     '        self.x = x\n'
                     '        self.y = y\n'
                     '\n'
                     '    def __eq__(self, other):\n'
                     '        if not isinstance(other, Vector):\n'
                     '            return NotImplemented\n'
                     '        return (self.x, self.y) == (other.x, other.y)\n'
                     '\n'
                     'print(Vector(1, 1) == Vector(1, 1))\n'
                     'print(Vector(1, 1) == 5)',
             'output': 'True\nFalse'},
            {'kind': 'cell',
             'prose': ['A useful `__repr__` makes operator results inspectable while debugging.'],
             'code': 'class Vector:\n'
                     '    def __init__(self, x, y):\n'
                     '        self.x = x\n'
                     '        self.y = y\n'
                     '\n'
                     '    def __add__(self, other):\n'
                     '        if not isinstance(other, Vector):\n'
                     '            return NotImplemented\n'
                     '        return Vector(self.x + other.x, self.y + other.y)\n'
                     '\n'
                     '    def __repr__(self):\n'
                     '        return f"Vector({self.x}, {self.y})"\n'
                     '\n'
                     'print(repr(Vector(2, 3) + Vector(4, 5)))',
             'output': 'Vector(6, 8)'}],
  'code': 'class Vector:\n'
          '    def __init__(self, x, y):\n'
          '        self.x = x\n'
          '        self.y = y\n'
          '\n'
          '    def __add__(self, other):\n'
          '        if not isinstance(other, Vector):\n'
          '            return NotImplemented\n'
          '        return Vector(self.x + other.x, self.y + other.y)\n'
          '\n'
          '    def __eq__(self, other):\n'
          '        if not isinstance(other, Vector):\n'
          '            return NotImplemented\n'
          '        return (self.x, self.y) == (other.x, other.y)\n'
          '\n'
          '    def __repr__(self):\n'
          '        return f"Vector({self.x}, {self.y})"\n'
          '\n'
          'print(Vector(2, 3) + Vector(4, 5))\n'
          'print(Vector(1, 1) == Vector(1, 1))\n'
          'print(Vector(1, 1) == 5)\n',
  'expected_output': 'Vector(6, 8)\nTrue\nFalse\n'},
 {'slug': 'attribute-access',
  'title': 'Attribute Access',
  'section': 'Data Model',
  'summary': 'Attribute hooks customize lookup, missing attributes, and assignment.',
  'doc_path': '/reference/datamodel.html#customizing-attribute-access',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#customizing-attribute-access',
  'explanation': ['Attribute access is usually simple: `obj.name` looks up an attribute. Python '
                  'exposes hooks for the uncommon cases where lookup or assignment needs to be '
                  'customized.',
                  '`__getattr__` runs only when normal lookup fails, which makes it a safer hook '
                  'for computed fallback attributes. `__setattr__` runs for every assignment, so '
                  'it should be used sparingly and carefully.',
                  'Prefer ordinary attributes and `@property` first. Reach for these hooks when an '
                  'object is intentionally adapting another interface, validating all assignments, '
                  'or exposing dynamic fields.'],
  'notes': ['`__getattr__` is narrower than `__getattribute__` because it handles only missing '
            'attributes.',
            '`__setattr__` affects every assignment on the instance.',
            'Use `property` or descriptors when the behavior is attached to a known attribute '
            'name.'],
  'see_also': ['properties', 'descriptors', 'special-methods', 'bound-and-unbound-methods'],
  'cells': [{'kind': 'cell',
             'prose': ['The starting point is ordinary: `__init__` stores one real attribute, the '
                       '`_values` backing dictionary. The hooks in the next cells customize lookup '
                       'and assignment around it.'],
             'code': 'class Settings:\n'
                     '    def __init__(self, values):\n'
                     '        self._values = dict(values)\n'
                     '\n'
                     'settings = Settings({"theme": "dark"})\n'
                     'print(settings._values)',
             'output': "{'theme': 'dark'}"},
            {'kind': 'cell',
             'prose': ['`__getattr__` runs only for missing attributes, so it can provide fallback '
                       'lookup.'],
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
             'output': 'dark'},
            {'kind': 'cell',
             'prose': ['`__setattr__` intercepts every assignment, including the ones in '
                       '`__init__`. Underscore names are stored as real attributes through '
                       '`object.__setattr__`, which avoids recursing through your own hook; public '
                       'names go to the backing dictionary.'],
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
             'output': '7'}],
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
  'expected_output': 'dark\n7\n'},
 {'slug': 'bound-and-unbound-methods',
  'title': 'Bound and Unbound Methods',
  'section': 'Data Model',
  'summary': 'instance.method binds self automatically; Class.method is a plain function.',
  'doc_path': '/reference/datamodel.html#instance-methods',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#instance-methods',
  'explanation': ['When you write `instance.method`, Python returns a bound method — a callable '
                  'that already remembers which instance to pass as `self`. When you write '
                  '`Class.method`, you get the underlying function back, and calling it requires '
                  'passing an instance yourself.',
                  'That distinction is why methods can be stored in collections, passed as '
                  'callbacks, and called later without losing track of the object they belong to. '
                  'Each bound method carries its own `__self__`, so two callables produced from '
                  'two different instances stay independent even when their underlying function is '
                  'the same.',
                  'The mechanism is the descriptor protocol: a function attached to a class '
                  'implements `__get__`, and that hook turns attribute access on an instance into '
                  'a bound method. The page does not need that detail to use methods, but it '
                  'explains what is happening underneath.'],
  'notes': ['`instance.method` produces a bound method whose `__self__` is the instance.',
            '`Class.method` produces the plain function and requires you to pass the instance.',
            '"Unbound method" is the historical Python 2 term; since Python 3, `Class.method` is '
            'simply a function, which is what this page demonstrates.',
            'Each bound method is its own object; storing one captures its instance.',
            'The binding is implemented by the descriptor protocol on the function object.'],
  'see_also': ['classes', 'attribute-access', 'descriptors', 'callable-objects'],
  'cells': [{'kind': 'cell',
             'prose': ['`instance.method` returns a bound method. The method already remembers the '
                       'instance through `__self__`, so calling it does not require passing `self` '
                       'again.'],
             'code': 'class Counter:\n'
                     '    def __init__(self, start=0):\n'
                     '        self.value = start\n'
                     '\n'
                     '    def increment(self):\n'
                     '        self.value += 1\n'
                     '        return self.value\n'
                     '\n'
                     'bound_counter = Counter(10)\n'
                     'm = bound_counter.increment\n'
                     'print(m.__self__ is bound_counter)\n'
                     'print(m())\n'
                     'print(m())',
             'output': 'True\n11\n12'},
            {'kind': 'cell',
             'prose': ['`Class.method` returns the underlying function — there is no `self` '
                       'attached. Calling it requires passing the instance as the first argument '
                       'explicitly. Using a fresh counter here makes the output independent of the '
                       'previous cell.'],
             'code': 'unbound_counter = Counter(0)\n'
                     'unbound = Counter.increment\n'
                     'print(type(unbound).__name__)\n'
                     'print(unbound(unbound_counter))\n'
                     'print(unbound(unbound_counter))',
             'output': 'function\n1\n2'},
            {'kind': 'cell',
             'prose': ['Bound methods are first-class values. They can be stored in lists, passed '
                       'to other functions, and called later. Each bound method carries its own '
                       '`__self__`, so two methods produced from two different instances stay '
                       'independent.'],
             'code': 'handlers = []\n'
                     'for _ in range(2):\n'
                     '    handlers.append(Counter().increment)\n'
                     '\n'
                     'print(handlers[0]())\n'
                     'print(handlers[0]())\n'
                     'print(handlers[1]())',
             'output': '1\n2\n1'},
            {'kind': 'cell',
             'prose': ['The binding is the descriptor protocol at work. The function lives on the '
                       'class as a plain function; instance attribute access invokes `__get__`, '
                       'which returns a bound method that knows the instance.'],
             'code': 'descriptor_counter = Counter(0)\n'
                     'func = Counter.__dict__["increment"]\n'
                     'print(type(func).__name__)\n'
                     'rebound = func.__get__(descriptor_counter, Counter)\n'
                     'print(type(rebound).__name__)\n'
                     'print(rebound.__self__ is descriptor_counter)',
             'output': 'function\nmethod\nTrue'}],
  'code': 'class Counter:\n'
          '    def __init__(self, start=0):\n'
          '        self.value = start\n'
          '\n'
          '    def increment(self):\n'
          '        self.value += 1\n'
          '        return self.value\n'
          '\n'
          'bound_counter = Counter(10)\n'
          'm = bound_counter.increment\n'
          'print(m.__self__ is bound_counter)\n'
          'print(m())\n'
          'print(m())\n'
          '\n'
          'unbound_counter = Counter(0)\n'
          'unbound = Counter.increment\n'
          'print(type(unbound).__name__)\n'
          'print(unbound(unbound_counter))\n'
          'print(unbound(unbound_counter))\n'
          '\n'
          'handlers = []\n'
          'for _ in range(2):\n'
          '    handlers.append(Counter().increment)\n'
          '\n'
          'print(handlers[0]())\n'
          'print(handlers[0]())\n'
          'print(handlers[1]())\n'
          '\n'
          'descriptor_counter = Counter(0)\n'
          'func = Counter.__dict__["increment"]\n'
          'print(type(func).__name__)\n'
          'rebound = func.__get__(descriptor_counter, Counter)\n'
          'print(type(rebound).__name__)\n'
          'print(rebound.__self__ is descriptor_counter)\n',
  'expected_output': 'True\n11\n12\nfunction\n1\n2\n1\n2\n1\nfunction\nmethod\nTrue\n'},
 {'slug': 'descriptors',
  'title': 'Descriptors',
  'section': 'Data Model',
  'summary': 'Descriptors customize attribute access through __get__, __set__, or __delete__.',
  'doc_path': '/howto/descriptor.html',
  'doc_url': 'https://docs.python.org/3.13/howto/descriptor.html',
  'explanation': ['A descriptor is an object stored on a class that defines `__get__`, `__set__`, '
                  'or `__delete__`. When an instance attribute lookup finds that object on the '
                  'class, Python calls the descriptor method instead of returning the descriptor '
                  'object directly.',
                  'Descriptors are the machinery behind methods, `property`, validators, and many '
                  'ORM fields. Use them when one reusable object should control access for many '
                  'attributes or classes; use `property` for a single simple managed attribute.',
                  'This example implements a positive-number validator. `__set_name__` learns the '
                  'attribute name when the owner class is created, `__set__` validates writes, and '
                  '`__get__` reads the stored value back from the instance.'],
  'notes': ['Descriptors are class attributes that participate in instance attribute access.',
            'Data descriptors with `__set__` can validate or transform assignments.',
            '`property` is usually simpler for one-off managed attributes; descriptors shine when '
            'the behavior is reusable.'],
  'see_also': ['attribute-access', 'properties', 'bound-and-unbound-methods'],
  'cells': [{'kind': 'cell',
             'prose': ['A descriptor object lives on the class. `__set_name__` lets it learn which '
                       'managed attribute it is serving.'],
             'code': 'class Positive:\n'
                     '    def __set_name__(self, owner, name):\n'
                     '        self.private_name = "_" + name\n'
                     '\n'
                     '    def __get__(self, obj, owner):\n'
                     '        if obj is None:\n'
                     '            return self\n'
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
                     'print(Product.price.private_name)',
             'output': '_price'},
            {'kind': 'cell',
             'prose': ['Assigning `item.price` calls `Positive.__set__`, and reading it calls '
                       '`Positive.__get__`.'],
             'code': 'class Product:\n'
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
             'output': '10\nmust be positive'}],
  'code': 'class Positive:\n'
          '    def __set_name__(self, owner, name):\n'
          '        self.private_name = "_" + name\n'
          '\n'
          '    def __get__(self, obj, owner):\n'
          '        if obj is None:\n'
          '            return self\n'
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
          'print(Product.price.private_name)\n'
          'try:\n'
          '    item.price = -1\n'
          'except ValueError as error:\n'
          '    print(error)\n',
  'expected_output': '10\n_price\nmust be positive\n'},
 {'slug': 'metaclasses',
  'title': 'Metaclasses',
  'section': 'Classes',
  'summary': 'A metaclass customizes how classes themselves are created.',
  'doc_path': '/reference/datamodel.html#metaclasses',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#metaclasses',
  'explanation': ['A metaclass is the class of a class. Most Python code never needs one, but the '
                  'syntax appears in frameworks that register, validate, or modify classes as they '
                  'are created.',
                  'The `metaclass=` keyword in a class statement chooses the object that builds '
                  'the class. This is advanced machinery; decorators and ordinary functions are '
                  'usually simpler.',
                  'Use metaclasses only when class creation itself is the problem being solved.'],
  'notes': ['Metaclasses customize class creation, not instance behavior directly.',
            'Most code should prefer class decorators, functions, or ordinary inheritance.',
            'You are most likely to meet metaclasses inside frameworks and ORMs.'],
  'see_also': ['classes', 'inheritance-and-super', 'special-methods'],
  'cells': [{'kind': 'cell',
             'prose': ['A metaclass customizes class creation. `__new__` receives the class name, '
                       'bases, and namespace before the class object exists.'],
             'code': 'class Tagged(type):\n'
                     '    def __new__(mcls, name, bases, namespace):\n'
                     '        namespace["tag"] = name.lower()\n'
                     '        return super().__new__(mcls, name, bases, namespace)\n'
                     '\n'
                     'print(Tagged.__name__)',
             'output': 'Tagged'},
            {'kind': 'cell',
             'prose': ['The `metaclass=` keyword applies that class-building rule. Here the '
                       'metaclass adds a `tag` attribute to the new class.'],
             'code': 'class Event(metaclass=Tagged):\n'
                     '    pass\n'
                     '\n'
                     'print(Event.tag)\n'
                     'print(type(Event).__name__)',
             'output': 'event\nTagged'}],
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
  'expected_output': 'event\nTagged\n'},
 {'slug': 'context-managers',
  'title': 'Context Managers',
  'section': 'Data Model',
  'summary': 'with ensures setup and cleanup happen together.',
  'doc_path': '/reference/datamodel.html#context-managers',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#context-managers',
  'explanation': ['Context managers define setup and cleanup around a block of code. The `with` '
                  'statement guarantees that cleanup runs when the block exits, even when an '
                  'exception is raised.',
                  'The protocol is powered by `__enter__` and `__exit__`. The '
                  '`contextlib.contextmanager` decorator is a concise way to write the same idea '
                  'as a generator when a full class would be noisy.',
                  'Production code often uses `with` for files, locks, transactions, temporary '
                  'state, and resources that need reliable release.'],
  'notes': ['Files, locks, and temporary state commonly use context managers.',
            '`__enter__` and `__exit__` power the protocol.',
            'Use `finally` when cleanup must happen after errors too.',
            'Returning true from `__exit__` suppresses an exception; do that only intentionally.'],
  'see_also': ['exceptions', 'special-methods', 'descriptors'],
  'cells': [{'kind': 'cell',
             'prose': ['A class-based context manager implements `__enter__` and `__exit__`. The '
                       'value returned by `__enter__` is bound by `as` when the `with` statement '
                       'uses it.'],
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
             'output': '<section>\ncontent\n</section>'},
            {'kind': 'cell',
             'prose': ['`contextlib.contextmanager` writes the same setup/cleanup shape as a '
                       'generator. Code before `yield` is setup, and code after `yield` is '
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
                     'with tag("note"):\n'
                     '    print("body")',
             'output': '<note>\nbody\n</note>'},
            {'kind': 'cell',
             'prose': ['Cleanup still runs when the block raises. Returning `False` from '
                       '`__exit__`, or letting a generator context manager re-raise, allows the '
                       'exception to keep propagating.'],
             'code': 'try:\n'
                     '    with tag("error"):\n'
                     '        raise ValueError("boom")\n'
                     'except ValueError:\n'
                     '    print("handled")',
             'output': '<error>\n</error>\nhandled'}],
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
  'expected_output': '<section>\ncontent\n</section>\n<error>\n</error>\nhandled\n'},
 {'slug': 'delete-statements',
  'title': 'Delete Statements',
  'section': 'Data Model',
  'summary': 'del removes bindings, items, and attributes rather than producing a value.',
  'doc_path': '/reference/simple_stmts.html#the-del-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-del-statement',
  'explanation': ['`del` removes a binding or an item. It is a statement, not a function, and it '
                  'does not return the removed value.',
                  'Use `del name` when a name should no longer be bound. Use `del mapping[key]` or '
                  '`del sequence[index]` when mutating a container by removing one part.',
                  'This is different from assigning `None`: `None` is still a value, while `del` '
                  'removes the binding or slot.'],
  'notes': ['`del` removes bindings or container entries.',
            'Assign `None` when absence should remain an explicit value.',
            'Use container methods such as `pop()` when you need the removed value back.'],
  'see_also': ['variables', 'dicts', 'mutability'],
  'cells': [{'kind': 'cell',
             'prose': ['Deleting a dictionary key mutates the dictionary. The key is gone; it has '
                       'not been set to `None`.'],
             'code': 'profile = {"name": "Ada", "temporary": True}\n'
                     'del profile["temporary"]\n'
                     'print(profile)',
             'output': "{'name': 'Ada'}"},
            {'kind': 'cell',
             'prose': ['Deleting a list item removes that position and shifts later items left.'],
             'code': 'items = ["a", "b", "c"]\ndel items[1]\nprint(items)',
             'output': "['a', 'c']"},
            {'kind': 'cell',
             'prose': ['Deleting a name removes the binding from the current namespace. It is '
                       'different from rebinding the name to `None`.'],
             'code': 'value = "cached"\ndel value\nprint("value" in locals())',
             'output': 'False'}],
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
  'expected_output': "{'name': 'Ada'}\n['a', 'c']\nFalse\n"},
 {'slug': 'exceptions',
  'title': 'Exceptions',
  'section': 'Errors',
  'summary': 'Use try, except, else, and finally to separate success, recovery, and cleanup.',
  'doc_path': '/tutorial/errors.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html',
  'explanation': ['Exceptions represent errors or unusual conditions that interrupt normal control '
                  'flow. `try` marks the operation that may fail, and `except` handles a specific '
                  'failure where recovery makes sense.',
                  'Keep the successful path separate from the recovery path. `else` runs only when '
                  'no exception was raised, while `finally` runs either way for cleanup or '
                  'bookkeeping.',
                  'Use exceptions when an operation cannot produce a valid result. Prefer ordinary '
                  'conditionals for expected branches that are not errors.',
                  'Catch specific exceptions whenever possible. A broad catch can hide programming '
                  'mistakes, while a targeted `ValueError` handler documents exactly what failure '
                  'is expected.'],
  'notes': ['Catch the most specific exception you can.',
            '`else` is for success code that should run only if the `try` block did not fail.',
            '`finally` runs whether the operation succeeded or failed.',
            'Avoid bare `except:` and broad `except Exception:` — they hide bugs and absorb '
            'signals like `KeyboardInterrupt`.'],
  'see_also': ['conditionals', 'guard-clauses', 'custom-exceptions', 'warnings'],
  'cells': [{'kind': 'cell',
             'prose': ['When no exception is raised, the `else` block runs. Keeping success in '
                       '`else` makes the `try` block contain only the operation that might fail.'],
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
             'output': '42: 42\nchecked 42'},
            {'kind': 'cell',
             'prose': ['When parsing fails, `int()` raises `ValueError`. Catching that specific '
                       'exception makes the expected recovery path explicit.'],
             'code': 'text = "python"\n'
                     'try:\n'
                     '    number = parse_int(text)\n'
                     'except ValueError:\n'
                     '    print(f"{text}: invalid")\n'
                     'else:\n'
                     '    print(f"{text}: {number}")\n'
                     'finally:\n'
                     '    print(f"checked {text}")',
             'output': 'python: invalid\nchecked python'},
            {'kind': 'cell',
             'prose': ['Bare `except:` and broad `except Exception:` swallow far more than the '
                       'failure you meant to handle, including `KeyboardInterrupt` (bare) and most '
                       'programming bugs (broad). The two functions look interchangeable on good '
                       'input — the divergence appears on a buggy call: passing a list is a '
                       'programming error, yet the broad version converts it into a quiet `None` '
                       'while the specific version lets the `TypeError` surface.'],
             'code': 'def safe_parse_broken(text):\n'
                     '    try:\n'
                     '        return int(text)\n'
                     '    except Exception:\n'
                     '        return None\n'
                     '\n'
                     'def safe_parse_fixed(text):\n'
                     '    try:\n'
                     '        return int(text)\n'
                     '    except ValueError:\n'
                     '        return None\n'
                     '\n'
                     'print(safe_parse_broken("42"))\n'
                     'print(safe_parse_fixed("42"))\n'
                     'print(safe_parse_broken(["4", "2"]))\n'
                     '\n'
                     'try:\n'
                     '    safe_parse_fixed(["4", "2"])\n'
                     'except TypeError as error:\n'
                     '    print(type(error).__name__)',
             'output': '42\n42\nNone\nTypeError'}],
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
          '        print(f"checked {text}")\n'
          '\n'
          '\n'
          'def safe_parse_broken(text):\n'
          '    try:\n'
          '        return int(text)\n'
          '    except Exception:\n'
          '        return None\n'
          '\n'
          'def safe_parse_fixed(text):\n'
          '    try:\n'
          '        return int(text)\n'
          '    except ValueError:\n'
          '        return None\n'
          '\n'
          'print(safe_parse_broken("42"))\n'
          'print(safe_parse_fixed("42"))\n'
          'print(safe_parse_broken(["4", "2"]))\n'
          '\n'
          'try:\n'
          '    safe_parse_fixed(["4", "2"])\n'
          'except TypeError as error:\n'
          '    print(type(error).__name__)\n',
  'expected_output': '42: 42\n'
                     'checked 42\n'
                     'python: invalid\n'
                     'checked python\n'
                     '42\n'
                     '42\n'
                     'None\n'
                     'TypeError\n'},
 {'slug': 'assertions',
  'title': 'Assertions',
  'section': 'Errors',
  'summary': 'assert documents internal assumptions and fails loudly when they are false.',
  'doc_path': '/reference/simple_stmts.html#the-assert-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-assert-statement',
  'explanation': ['`assert` checks an internal assumption. If the condition is false, Python '
                  'raises `AssertionError` with an optional message.',
                  'Use assertions for programmer assumptions, not for validating user input or '
                  'external data. Input validation should raise ordinary exceptions that '
                  'production code expects to handle.',
                  'Assertions make invariants executable while keeping the successful path '
                  'compact.'],
  'notes': ['Use `assert` for internal invariants and debugging assumptions.',
            'Use explicit exceptions for user input, files, network responses, and other expected '
            'failures.',
            'Assertions can be disabled with Python optimization flags, so do not rely on them for '
            'security checks.'],
  'see_also': ['exceptions', 'custom-exceptions', 'type-hints'],
  'cells': [{'kind': 'cell',
             'prose': ['When the assertion is true, execution continues normally. The assertion '
                       "documents the function's internal expectation."],
             'code': 'def average(scores):\n'
                     '    assert scores, "scores must not be empty"\n'
                     '    return sum(scores) / len(scores)\n'
                     '\n'
                     'print(average([8, 10]))',
             'output': '9.0'},
            {'kind': 'cell',
             'prose': ['When the assertion is false, Python raises `AssertionError`. This signals '
                       'a broken assumption, not a normal recovery path.'],
             'code': 'try:\n    average([])\nexcept AssertionError as error:\n    print(error)',
             'output': 'scores must not be empty'}],
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
  'expected_output': '9.0\nscores must not be empty\n'},
 {'slug': 'exception-chaining',
  'title': 'Exception Chaining',
  'section': 'Errors',
  'summary': 'raise from preserves the original cause when translating exceptions.',
  'doc_path': '/tutorial/errors.html#exception-chaining',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#exception-chaining',
  'explanation': ['Exception chaining connects a higher-level error to the lower-level exception '
                  'that caused it. The syntax is `raise NewError(...) from error`.',
                  'Use chaining when translating implementation details into a domain-specific '
                  'error while preserving the original cause for debugging.',
                  'This is different from hiding the original exception. The caller can catch the '
                  'domain error, and tooling can still inspect `__cause__`.'],
  'notes': ['Use `raise ... from error` when translating exceptions across a boundary.',
            "The new exception's `__cause__` points to the original exception.",
            'Chaining keeps user-facing errors clear without losing debugging context.'],
  'see_also': ['exceptions', 'custom-exceptions', 'assertions'],
  'cells': [{'kind': 'cell',
             'prose': ['Catch the low-level exception where it happens, then raise a '
                       'domain-specific exception from it.'],
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
             'output': 'ConfigError'},
            {'kind': 'cell',
             'prose': ['The caller handles the domain error. The original `ValueError` remains '
                       'available as `__cause__`.'],
             'code': 'try:\n'
                     '    read_port("abc")\n'
                     'except ConfigError as error:\n'
                     '    print(error)\n'
                     '    print(type(error.__cause__).__name__)',
             'output': 'port must be a number\nValueError'}],
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
  'expected_output': 'ConfigError\nport must be a number\nValueError\n'},
 {'slug': 'exception-groups',
  'title': 'Exception Groups',
  'section': 'Errors',
  'summary': 'except* handles matching exceptions inside an ExceptionGroup.',
  'doc_path': '/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions',
  'explanation': ['`ExceptionGroup` represents several unrelated exceptions raised together. '
                  '`except*` exists for code that may receive multiple failures at once, '
                  'especially concurrent work.',
                  'Use ordinary `except` for one exception. Use `except*` only when the value '
                  'being handled is an exception group and each matching subgroup needs its own '
                  'handling.',
                  'Each `except*` clause receives a smaller exception group containing the '
                  'matching exceptions.'],
  'notes': ['`except*` is for `ExceptionGroup`, not ordinary single exceptions.',
            'Each `except*` clause handles matching members of the group.',
            'Exception groups often appear around concurrent work.'],
  'see_also': ['exceptions', 'exception-chaining', 'async-await'],
  'cells': [{'kind': 'cell',
             'prose': ['An exception group bundles several exception objects. This is different '
                       'from an ordinary exception because more than one failure is present.'],
             'code': 'errors = ExceptionGroup(\n'
                     '    "batch failed",\n'
                     '    [ValueError("bad port"), TypeError("bad mode")],\n'
                     ')\n'
                     'print(len(errors.exceptions))',
             'output': '2'},
            {'kind': 'cell',
             'prose': ['`except*` handles matching members of the group. The `ValueError` handler '
                       'sees the value error, and the `TypeError` handler sees the type error.'],
             'code': 'try:\n'
                     '    raise errors\n'
                     'except* ValueError as group:\n'
                     '    print(type(group).__name__)\n'
                     '    print(group.exceptions[0])\n'
                     'except* TypeError as group:\n'
                     '    print(group.exceptions[0])',
             'output': 'ExceptionGroup\nbad port\nbad mode'}],
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
  'expected_output': '2\nExceptionGroup\nbad port\nbad mode\n'},
 {'slug': 'warnings',
  'title': 'Warnings',
  'section': 'Errors',
  'summary': 'warnings report soft problems without immediately stopping the program.',
  'doc_path': '/library/warnings.html',
  'doc_url': 'https://docs.python.org/3.13/library/warnings.html',
  'explanation': ['A warning reports a problem that callers should know about, but it does not '
                  'have to stop the current operation. Deprecations are the classic case: the old '
                  'API can still return a value while telling users to migrate.',
                  'Warnings sit between logging and exceptions. Logging records operational '
                  'evidence; exceptions stop the current path; warnings make compatibility or '
                  'correctness concerns visible according to a filter.',
                  'Tests often capture warnings so deprecations are asserted instead of merely '
                  'printed. Filters can also turn warnings into errors when a project wants to '
                  'enforce cleanup.'],
  'notes': ['Use warnings for soft problems callers can act on later.',
            'Use exceptions when the current operation cannot continue.',
            '`stacklevel` should point the warning at the caller rather than inside the helper.'],
  'see_also': ['exceptions', 'logging', 'testing'],
  'cells': [{'kind': 'cell',
             'prose': ['Capture warnings in tests when the returned value still matters but the '
                       'migration notice must be asserted.'],
             'code': 'import warnings\n'
                     '\n'
                     '\n'
                     'def old_name():\n'
                     '    warnings.warn("old_name is deprecated", DeprecationWarning, '
                     'stacklevel=2)\n'
                     '    return "result"\n'
                     '\n'
                     'with warnings.catch_warnings(record=True) as caught:\n'
                     '    warnings.simplefilter("always", DeprecationWarning)\n'
                     '    print(old_name())\n'
                     '    print(caught[0].category.__name__)\n'
                     '    print(str(caught[0].message))',
             'output': 'result\nDeprecationWarning\nold_name is deprecated'},
            {'kind': 'cell',
             'prose': ['A filter can promote selected warnings to exceptions, which is useful in '
                       'CI when deprecated calls should fail the build.'],
             'code': 'with warnings.catch_warnings():\n'
                     '    warnings.simplefilter("error", DeprecationWarning)\n'
                     '    try:\n'
                     '        old_name()\n'
                     '    except DeprecationWarning:\n'
                     '        print("warning became error")',
             'output': 'warning became error'}],
  'code': 'import warnings\n'
          '\n'
          '\n'
          'def old_name():\n'
          '    warnings.warn("old_name is deprecated", DeprecationWarning, stacklevel=2)\n'
          '    return "result"\n'
          '\n'
          'with warnings.catch_warnings(record=True) as caught:\n'
          '    warnings.simplefilter("always", DeprecationWarning)\n'
          '    print(old_name())\n'
          '    print(caught[0].category.__name__)\n'
          '    print(str(caught[0].message))\n'
          '\n'
          'with warnings.catch_warnings():\n'
          '    warnings.simplefilter("error", DeprecationWarning)\n'
          '    try:\n'
          '        old_name()\n'
          '    except DeprecationWarning:\n'
          '        print("warning became error")\n',
  'expected_output': 'result\nDeprecationWarning\nold_name is deprecated\nwarning became error\n'},
 {'slug': 'modules',
  'title': 'Modules',
  'section': 'Modules',
  'summary': 'Modules organize code into namespaces and expose reusable definitions.',
  'doc_path': '/tutorial/modules.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/modules.html',
  'explanation': ['Modules organize Python code into files and namespaces. `import` executes a '
                  "module once, stores it in Python's import cache, and gives your program access "
                  'to its definitions.',
                  'This page focuses on import forms and module namespaces. Package layout, '
                  'aliases, and dynamic imports have their own neighboring examples.',
                  'Use module namespaces such as `math.sqrt` when the source of a name should stay '
                  'visible. Use focused imports such as `from statistics import mean` when the '
                  'imported name is clear at the call site.'],
  'notes': ['Prefer plain `import module` when the namespace improves readability.',
            'Use focused imports for a small number of clear names.',
            'Place imports near the top of the file.',
            'Imports execute module top-level code once, then reuse the cached module object.'],
  'see_also': ['import-aliases', 'packages'],
  'cells': [{'kind': 'cell',
             'prose': ['Importing a module gives access to its namespace. The `math.` prefix makes '
                       'it clear where `pi` came from.'],
             'code': 'import math\n'
                     '\n'
                     'radius = 3\n'
                     'area = math.pi * radius ** 2\n'
                     'print(round(area, 2))',
             'output': '28.27'},
            {'kind': 'cell',
             'prose': ['A focused `from ... import ...` brings one definition into the current '
                       'namespace. This keeps a common operation concise without importing every '
                       'name.'],
             'code': 'from statistics import mean\n\nscores = [8, 10, 9]\nprint(mean(scores))',
             'output': '9'},
            {'kind': 'cell',
             'prose': ['Modules are objects too. Their attributes include metadata such as '
                       "`__name__`, which records the module's import name."],
             'code': 'print(math.__name__)',
             'output': 'math'},
            {'kind': 'cell',
             'prose': ['Imported modules are cached in `sys.modules`. Later imports reuse the '
                       'module object instead of executing the file again.'],
             'code': 'import sys\nprint("math" in sys.modules)',
             'output': 'True'}],
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
  'expected_output': '28.27\n9\nmath\nTrue\n'},
 {'slug': 'import-aliases',
  'title': 'Import Aliases',
  'section': 'Modules',
  'summary': 'as gives imported modules or names a local alias.',
  'doc_path': '/reference/simple_stmts.html#the-import-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-import-statement',
  'explanation': ['`as` gives an imported module or imported name a local alias. Use it when a '
                  'conventional short name improves readability or when two imports would '
                  'otherwise collide.',
                  'The alternative is a plain import, which is usually better when the module name '
                  'is already clear. Avoid aliases that make readers guess where a name came from.',
                  'Avoid star imports in examples and production modules because they hide '
                  'dependencies and blur the boundary between modules.'],
  'notes': ['`import module as alias` keeps module-style access under a shorter or clearer name.',
            '`from module import name as alias` imports one name under a local alias.',
            'Prefer plain imports unless an alias improves clarity or follows a strong convention.',
            'Avoid `from module import *` because it makes dependencies harder to see.'],
  'see_also': ['modules', 'functions'],
  'cells': [{'kind': 'cell',
             'prose': ['A module alias keeps the namespace but changes the local name. Here '
                       '`stats` is shorter, but readers can still see that `mean` belongs to the '
                       'statistics module.'],
             'code': 'import statistics as stats\n'
                     '\n'
                     'scores = [8, 10, 9]\n'
                     'print(stats.mean(scores))\n'
                     'print(stats.__name__)',
             'output': '9\nstatistics'},
            {'kind': 'cell',
             'prose': ['A name imported with `from` can also be aliased. Use this when the local '
                       'name explains the role better than the original name.'],
             'code': 'from math import sqrt as square_root\n'
                     '\n'
                     'print(square_root(81))\n'
                     'print(square_root.__name__)',
             'output': '9.0\nsqrt'}],
  'code': 'import statistics as stats\n'
          'from math import sqrt as square_root\n'
          '\n'
          'scores = [8, 10, 9]\n'
          'print(stats.mean(scores))\n'
          'print(stats.__name__)\n'
          '\n'
          'print(square_root(81))\n'
          'print(square_root.__name__)\n',
  'expected_output': '9\nstatistics\n9.0\nsqrt\n'},
 {'slug': 'packages',
  'title': 'Packages',
  'section': 'Modules',
  'summary': 'Packages organize modules into importable directories.',
  'doc_path': '/tutorial/modules.html#packages',
  'doc_url': 'https://docs.python.org/3.13/tutorial/modules.html#packages',
  'explanation': ['Packages are modules that can contain other modules. They let a project group '
                  'related code behind dotted import paths such as `json.decoder` or '
                  '`email.message`.',
                  'At runtime, importing a submodule gives Python a path through that package '
                  'structure. In a project on disk, that structure is usually a directory with '
                  'Python files and often an `__init__.py` file.',
                  'Use packages when one module has grown into a small namespace of related '
                  'modules. Keep module names boring and explicit so readers can tell where '
                  'imported definitions come from.'],
  'notes': ['A package is a module that can contain submodules.',
            'Dotted imports should mirror a meaningful project structure.',
            'Use `from .submodule import name` inside a package to re-export submodule names; set '
            '`__all__` to declare the public surface.',
            'Prefer ordinary imports unless the module name is truly dynamic.'],
  'see_also': ['modules', 'import-aliases', 'virtual-environments'],
  'cells': [{'kind': 'cell',
             'prose': ['A package is itself a module. The `json` package exposes a namespace that '
                       'can contain submodules.'],
             'code': 'import json\n\nprint(json.__name__)',
             'output': 'json'},
            {'kind': 'cell',
             'prose': ['Dotted imports name a path through a package. Importing `json.decoder` '
                       'makes that submodule available under the package namespace.'],
             'code': 'import json.decoder\n'
                     '\n'
                     'print(json.decoder.__name__)\n'
                     'print(json.decoder.JSONDecoder.__name__)',
             'output': 'json.decoder\nJSONDecoder'},
            {'kind': 'cell',
             'prose': ['`importlib.import_module()` imports by string. It is useful for plugin '
                       'systems and dynamic imports, but ordinary `import` is clearer when the '
                       'dependency is known.'],
             'code': 'import importlib\n'
                     '\n'
                     'module = importlib.import_module("json.decoder")\n'
                     'print(module is json.decoder)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ["Inside a package's `__init__.py`, `from .submodule import name` re-exports "
                       "a submodule's name at the package root, and `__all__` lists the names that "
                       '`from package import *` should make visible. This cell builds a temporary '
                       '`shapes` package on disk to make both forms concrete.'],
             'code': 'import os\n'
                     'import sys\n'
                     'import tempfile\n'
                     '\n'
                     'with tempfile.TemporaryDirectory() as tmp:\n'
                     '    pkg = os.path.join(tmp, "shapes")\n'
                     '    os.makedirs(pkg)\n'
                     '    with open(os.path.join(pkg, "__init__.py"), "w") as init:\n'
                     '        init.write("from .square import area\\n__all__ = [\'area\']\\n")\n'
                     '    with open(os.path.join(pkg, "square.py"), "w") as square:\n'
                     '        square.write("def area(side):\\n    return side * side\\n")\n'
                     '    sys.path.insert(0, tmp)\n'
                     '    try:\n'
                     '        import shapes\n'
                     '        print(shapes.area(3))\n'
                     '        print(shapes.__all__)\n'
                     '    finally:\n'
                     '        sys.path.remove(tmp)\n'
                     '        sys.modules.pop("shapes", None)\n'
                     '        sys.modules.pop("shapes.square", None)',
             'output': "9\n['area']"}],
  'code': 'import importlib\n'
          'import json\n'
          'import json.decoder\n'
          '\n'
          'module = importlib.import_module("json.decoder")\n'
          '\n'
          'print(json.__name__)\n'
          'print(json.decoder.__name__)\n'
          'print(module.JSONDecoder.__name__)\n'
          'print(module is json.decoder)\n'
          '\n'
          '\n'
          'import os\n'
          'import sys\n'
          'import tempfile\n'
          '\n'
          'with tempfile.TemporaryDirectory() as tmp:\n'
          '    pkg = os.path.join(tmp, "shapes")\n'
          '    os.makedirs(pkg)\n'
          '    with open(os.path.join(pkg, "__init__.py"), "w") as init:\n'
          '        init.write("from .square import area\\n__all__ = [\'area\']\\n")\n'
          '    with open(os.path.join(pkg, "square.py"), "w") as square:\n'
          '        square.write("def area(side):\\n    return side * side\\n")\n'
          '    sys.path.insert(0, tmp)\n'
          '    try:\n'
          '        import shapes\n'
          '        print(shapes.area(3))\n'
          '        print(shapes.__all__)\n'
          '    finally:\n'
          '        sys.path.remove(tmp)\n'
          '        sys.modules.pop("shapes", None)\n'
          '        sys.modules.pop("shapes.square", None)\n',
  'expected_output': "json\njson.decoder\nJSONDecoder\nTrue\n9\n['area']\n"},
 {'slug': 'virtual-environments',
  'title': 'Virtual Environments',
  'section': 'Modules',
  'summary': "Virtual environments isolate a project's Python packages.",
  'doc_path': '/library/venv.html',
  'doc_url': 'https://docs.python.org/3.13/library/venv.html',
  'explanation': ["Virtual environments isolate a project's installed packages from the global "
                  'Python installation and from other projects. The usual workflow is a '
                  'command-line one: create `.venv`, activate it, then install project '
                  'dependencies there.',
                  "In standard Python, `python -m venv .venv` is the everyday command. This site's "
                  'live example runner is built from declared dependencies rather than an '
                  'activated shell environment, so the runnable part keeps to deterministic '
                  'evidence while the page still teaches the standard-Python workflow.',
                  'A virtual environment changes installation and import paths. It does not change '
                  'the Python language, package layout rules, or module names.'],
  'notes': ['Use `python -m venv .venv` for everyday standard-Python project setup.',
            'A venv isolates installed packages; it does not change how imports are written.',
            "This site's runner uses a deployment dependency model, not an activated shell "
            'environment.',
            'That runner constraint is separate from the standard Python `venv` workflow you would '
            'use in local projects.'],
  'see_also': ['packages', 'modules', 'import-aliases'],
  'cells': [{'kind': 'unsupported',
             'prose': ['The standard project setup command is `python -m venv .venv`. It creates a '
                       'directory with its own interpreter entry points and package install '
                       'location. After activation, `python -m pip install ...` installs into that '
                       'environment rather than into another project. (This workflow is for '
                       'standard Python projects. The Python By Example runner is deployed from '
                       'declared dependencies instead of an activated shell environment.)'],
             'code': 'import subprocess\n'
                     'import sys\n'
                     '\n'
                     'subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)\n'
                     'subprocess.run([".venv/bin/python", "-m", "pip", "install", "requests"], '
                     'check=True)',
             'output': ''},
            {'kind': 'cell',
             'prose': ['`venv.EnvBuilder` exposes the same environment-creation mechanism as '
                       '`python -m venv`. A temporary directory keeps the example from leaving '
                       'project files behind.'],
             'code': 'import pathlib\n'
                     'import tempfile\n'
                     'import venv\n'
                     '\n'
                     'with tempfile.TemporaryDirectory() as directory:\n'
                     '    env_path = pathlib.Path(directory) / ".venv"\n'
                     '    builder = venv.EnvBuilder(with_pip=False)\n'
                     '    builder.create(env_path)\n'
                     '\n'
                     '    config = (env_path / "pyvenv.cfg").read_text()\n'
                     '    print(env_path.name)\n'
                     '    print("home" in config)',
             'output': '.venv\nTrue'}],
  'code': 'import pathlib\n'
          'import tempfile\n'
          'import venv\n'
          '\n'
          'with tempfile.TemporaryDirectory() as directory:\n'
          '    env_path = pathlib.Path(directory) / ".venv"\n'
          '    builder = venv.EnvBuilder(with_pip=False)\n'
          '    builder.create(env_path)\n'
          '\n'
          '    config = (env_path / "pyvenv.cfg").read_text()\n'
          '    print(env_path.name)\n'
          '    print("home" in config)\n',
  'expected_output': '.venv\nTrue\n'},
 {'slug': 'type-hints',
  'title': 'Type Hints',
  'section': 'Types',
  'summary': 'Annotations document expected types and power static analysis.',
  'doc_path': '/library/typing.html',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html',
  'explanation': ['Type hints are annotations that document expected shapes for values, '
                  'parameters, and return results. They exist so tools and readers can understand '
                  'API boundaries before the program runs.',
                  'Python stores many annotations but does not enforce most of them at runtime. '
                  'Use type hints for communication and static analysis; use validation or '
                  'exceptions when runtime checks are required.',
                  'The alternative to an annotation is prose, tests, or runtime validation. Good '
                  'Python code often uses all three at important boundaries.'],
  'notes': ['Python does not enforce most type hints at runtime.',
            'Tools like type checkers and editors use annotations to catch mistakes earlier.',
            'Use `X | Y` for unions and `Optional[X]` for "X or None"; both spellings mean the '
            'same thing.',
            'Reach for a `type` alias when a domain name reads better than a raw primitive type.',
            'Use runtime validation when untrusted input must be rejected while the program runs.'],
  'see_also': ['union-and-optional-types',
               'type-aliases',
               'generics-and-typevar',
               'runtime-type-checks'],
  'cells': [{'kind': 'cell',
             'prose': ['Type hints document expected parameter and return shapes. Python still '
                       'runs the function normally at runtime.'],
             'code': 'def total(numbers: list[int]) -> int:\n'
                     '    return sum(numbers)\n'
                     '\n'
                     'print(total([1, 2, 3]))',
             'output': '6'},
            {'kind': 'cell',
             'prose': ['Python stores annotations on the function object for tools and '
                       'introspection. Type checkers use this information without changing the '
                       'function call syntax.'],
             'code': 'print(total.__annotations__)',
             'output': "{'numbers': list[int], 'return': <class 'int'>}"},
            {'kind': 'cell',
             'prose': ['Most hints are not runtime validation. This call passes a string where the '
                       'hint says `int`; Python still calls the function because the body can '
                       'format any value.'],
             'code': 'def label(score: int) -> str:\n'
                     '    return f"score={score}"\n'
                     '\n'
                     'print(label("high"))',
             'output': 'score=high'},
            {'kind': 'cell',
             'prose': ['Use `X | Y` (PEP 604) to express "either type". `str | None` says the '
                       'result is a string or absent. `typing.Optional[X]` is the older, '
                       'still-supported spelling for the same idea — `Optional[X]` is equivalent '
                       'to `X | None`.'],
             'code': 'def find(name: str, options: list[str]) -> str | None:\n'
                     '    return name if name in options else None\n'
                     '\n'
                     'print(find("Ada", ["Ada", "Grace"]))\n'
                     'print(find("Guido", ["Ada", "Grace"]))\n'
                     '\n'
                     '\n'
                     'from typing import Optional\n'
                     '\n'
                     'def lookup(name: str) -> Optional[int]:\n'
                     '    table = {"Ada": 1815, "Grace": 1906}\n'
                     '    return table.get(name)\n'
                     '\n'
                     'print(lookup("Ada"))\n'
                     'print(lookup("Guido"))',
             'output': 'Ada\nNone\n1815\nNone'},
            {'kind': 'cell',
             'prose': ['The `type` statement names a type so it can be reused with intent. `type '
                       'Score = int` keeps the underlying type at runtime but lets the API talk '
                       'about a domain concept rather than a primitive. Older code spells this '
                       '`Score: TypeAlias = int`; `typing.TypeAlias` is deprecated since Python '
                       '3.12, and the type-aliases page covers the modern statement in depth.'],
             'code': 'type Score = int\n'
                     '\n'
                     'def grade(score: Score) -> str:\n'
                     '    return "pass" if score >= 50 else "fail"\n'
                     '\n'
                     'print(grade(72))',
             'output': 'pass'}],
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
          'print(label("high"))\n'
          '\n'
          '\n'
          'def find(name: str, options: list[str]) -> str | None:\n'
          '    return name if name in options else None\n'
          '\n'
          'print(find("Ada", ["Ada", "Grace"]))\n'
          'print(find("Guido", ["Ada", "Grace"]))\n'
          '\n'
          '\n'
          'from typing import Optional\n'
          '\n'
          'def lookup(name: str) -> Optional[int]:\n'
          '    table = {"Ada": 1815, "Grace": 1906}\n'
          '    return table.get(name)\n'
          '\n'
          'print(lookup("Ada"))\n'
          'print(lookup("Guido"))\n'
          '\n'
          '\n'
          'type Score = int\n'
          '\n'
          'def grade(score: Score) -> str:\n'
          '    return "pass" if score >= 50 else "fail"\n'
          '\n'
          'print(grade(72))\n',
  'expected_output': '6\n'
                     "{'numbers': list[int], 'return': <class 'int'>}\n"
                     'score=high\n'
                     'Ada\n'
                     'None\n'
                     '1815\n'
                     'None\n'
                     'pass\n'},
 {'slug': 'runtime-type-checks',
  'title': 'Runtime Type Checks',
  'section': 'Types',
  'summary': 'type, isinstance, and issubclass inspect runtime relationships.',
  'doc_path': '/library/functions.html#isinstance',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#isinstance',
  'explanation': ['Runtime type checks inspect real objects while the program is running. They are '
                  'different from type hints, which mostly guide tools before the program runs.',
                  'Use `type()` when the exact class matters, `isinstance()` when subclasses '
                  'should count, and `issubclass()` when checking class relationships. Most APIs '
                  'prefer behavior over type checks, but runtime checks are useful at input '
                  'boundaries.',
                  'Do not turn every function into a wall of `isinstance()` calls. If the code '
                  'only needs an object that can perform an operation, duck typing or a protocol '
                  'may be clearer.'],
  'notes': ['`type()` is exact; `isinstance()` follows inheritance.',
            'Runtime checks inspect objects, not static annotations.',
            'Prefer behavior, protocols, or clear validation over scattered type checks.'],
  'see_also': ['type-hints', 'protocols', 'casts-and-any', 'abstract-base-classes'],
  'cells': [{'kind': 'cell',
             'prose': ['`type()` reports the exact runtime class. A `Dog` instance is not exactly '
                       'an `Animal` instance.'],
             'code': 'class Animal:\n'
                     '    pass\n'
                     '\n'
                     'class Dog(Animal):\n'
                     '    pass\n'
                     '\n'
                     'pet = Dog()\n'
                     'print(type(pet).__name__)\n'
                     'print(type(pet) is Animal)',
             'output': 'Dog\nFalse'},
            {'kind': 'cell',
             'prose': ['`isinstance()` accepts subclasses, which is usually what API boundaries '
                       'want.'],
             'code': 'print(isinstance(pet, Dog))\nprint(isinstance(pet, Animal))',
             'output': 'True\nTrue'},
            {'kind': 'cell',
             'prose': ['`issubclass()` checks class relationships rather than individual objects.'],
             'code': 'print(issubclass(Dog, Animal))',
             'output': 'True'}],
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
  'expected_output': 'Dog\nFalse\nTrue\nTrue\n'},
 {'slug': 'union-and-optional-types',
  'title': 'Union and Optional Types',
  'section': 'Types',
  'summary': 'The | operator describes values that may have more than one static type.',
  'doc_path': '/library/typing.html#typing.Optional',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Optional',
  'explanation': ['A union type says that a value may have one of several static shapes. `int | '
                  'str` means callers may pass either an integer or a string.',
                  '`T | None` is the modern spelling for an optional value. The annotation '
                  'documents that absence is expected, but the code still needs to handle `None` '
                  'before using the non-optional behavior.',
                  'Unions are useful at boundaries where input is flexible. Inside a function, '
                  'narrow the value with an `is None`, `isinstance()`, or pattern check so the '
                  'rest of the code has one clear shape.'],
  'notes': ['Use `A | B` when a value may have either type.',
            '`T | None` means absence is an expected case, not an error by itself.',
            'Narrow unions before using behavior that belongs to only one member type.'],
  'see_also': ['none', 'type-hints', 'match-statements'],
  'cells': [{'kind': 'cell',
             'prose': ['Use `A | B` when a value may have either type. The function body should '
                       'use operations that make sense for every member of the union.'],
             'code': 'def label(value: int | str) -> str:\n'
                     '    return f"item-{value}"\n'
                     '\n'
                     'print(label(3))\n'
                     'print(label("A"))',
             'output': 'item-3\nitem-A'},
            {'kind': 'cell',
             'prose': ['`str | None` means the function accepts either a string or explicit '
                       'absence. Check for `None` before calling string methods.'],
             'code': 'def greeting(name: str | None) -> str:\n'
                     '    if name is None:\n'
                     '        return "hello guest"\n'
                     '    return f"hello {name.upper()}"\n'
                     '\n'
                     'print(greeting(None))\n'
                     'print(greeting("Ada"))',
             'output': 'hello guest\nhello ADA'},
            {'kind': 'cell',
             'prose': ['Union annotations are visible at runtime, but Python does not enforce them '
                       'when the function is called.'],
             'code': 'print(greeting.__annotations__)',
             'output': "{'name': str | None, 'return': <class 'str'>}"}],
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
  'expected_output': 'item-3\n'
                     'item-A\n'
                     'hello guest\n'
                     'hello ADA\n'
                     "{'name': str | None, 'return': <class 'str'>}\n"},
 {'slug': 'type-aliases',
  'title': 'Type Aliases',
  'section': 'Types',
  'summary': 'Type aliases give a meaningful name to a repeated type shape.',
  'doc_path': '/library/typing.html#type-aliases',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#type-aliases',
  'explanation': ['A type alias gives a name to an annotation shape. It helps readers and type '
                  'checkers understand the role of a value without repeating a long type '
                  'expression everywhere.',
                  'Python 3.13 supports the `type` statement for explicit aliases. Older '
                  'assignment-style aliases still appear in code, but the `type` statement makes '
                  'the intent clear and creates a `TypeAliasType` object at runtime.',
                  'An alias does not create a new runtime type. If you need a static distinction '
                  'between compatible values such as user IDs and order IDs, use `NewType` '
                  'instead.'],
  'notes': ['Use aliases to name repeated or domain-specific annotation shapes.',
            'A type alias does not validate values at runtime.',
            'Use `NewType` when two values share a runtime representation but should not be mixed '
            'statically.'],
  'see_also': ['type-hints', 'newtype', 'union-and-optional-types'],
  'cells': [{'kind': 'cell',
             'prose': ['The `type` statement names an annotation shape. Here `Scores` means a '
                       'dictionary from user IDs to integer scores.'],
             'code': 'type UserId = int\n'
                     'type Scores = dict[UserId, int]\n'
                     '\n'
                     '\n'
                     'def best_user(scores: Scores) -> UserId:\n'
                     '    return max(scores, key=scores.get)\n'
                     '\n'
                     'scores: Scores = {1: 98, 2: 91}\n'
                     'print(best_user(scores))',
             'output': '1'},
            {'kind': 'cell',
             'prose': ['Modern aliases are runtime objects that keep their alias name for '
                       'introspection.'],
             'code': 'print(UserId.__name__)\nprint(Scores.__name__)',
             'output': 'UserId\nScores'},
            {'kind': 'cell',
             'prose': ['Assignment-style aliases are still common, but they are just ordinary '
                       'names bound to existing objects.'],
             'code': 'LegacyName = str\nprint(LegacyName("Ada"))\nprint(LegacyName is str)',
             'output': 'Ada\nTrue'}],
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
  'expected_output': '1\nUserId\nAda\n'},
 {'slug': 'typed-dicts',
  'title': 'TypedDict',
  'section': 'Types',
  'summary': 'TypedDict describes dictionaries with known string keys.',
  'doc_path': '/library/typing.html#typing.TypedDict',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.TypedDict',
  'explanation': ['`TypedDict` describes dictionary records with known keys. It is useful for '
                  'JSON-like data that should remain a dictionary instead of becoming a class '
                  'instance.',
                  'The important boundary is static versus runtime behavior. Type checkers can '
                  'know that `name` is a string and `score` is an integer, but at runtime the '
                  'value is still an ordinary `dict`.',
                  'Use `TypedDict` for external records and `dataclass` when your own program '
                  'wants attribute access, methods, and construction behavior.'],
  'notes': ['Use `TypedDict` for dictionary records from JSON or APIs.',
            'Type checkers understand required and optional keys.',
            'Runtime behavior is still ordinary dictionary behavior.'],
  'see_also': ['dicts', 'json', 'dataclasses', 'structured-data-shapes'],
  'cells': [{'kind': 'cell',
             'prose': ['Use `TypedDict` for JSON-like records that remain dictionaries.'],
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
             'output': 'Ada: 98'},
            {'kind': 'cell',
             'prose': ['At runtime, a `TypedDict` value is still a plain dictionary.'],
             'code': 'print(isinstance(record, dict))\nprint(type(record).__name__)',
             'output': 'True\ndict'},
            {'kind': 'cell',
             'prose': ['`NotRequired` marks a key that type checkers should treat as optional. '
                       'Runtime lookup still uses normal dictionary tools such as `get()`.'],
             'code': 'from typing import NotRequired\n'
                     '\n'
                     'class UserWithNickname(TypedDict):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '    nickname: NotRequired[str]\n'
                     '\n'
                     'record: UserWithNickname = {"name": "Ada", "score": 98}\n'
                     'print(record.get("nickname", "none"))',
             'output': 'none'}],
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
  'expected_output': 'Ada: 98\nTrue\nnone\n'},
 {'slug': 'structured-data-shapes',
  'title': 'Structured Data Shapes',
  'section': 'Classes',
  'summary': 'dataclass, NamedTuple, and TypedDict each model records with different trade-offs.',
  'doc_path': '/library/dataclasses.html',
  'doc_url': 'https://docs.python.org/3.13/library/dataclasses.html',
  'explanation': ['`@dataclass`, `typing.NamedTuple`, and `typing.TypedDict` are three ways to '
                  'give a record a name and a schema. They model the same data but differ in '
                  'mutability, access syntax, and what the type information costs at runtime.',
                  'A dataclass is a regular class with `__init__` and `__repr__` generated for '
                  'you, so instances are mutable and attribute-accessed. A `NamedTuple` is a tuple '
                  'subclass with named positions, so instances are immutable and support both '
                  '`obj.field` and `obj[index]`. A `TypedDict` is a plain dict at runtime; the '
                  'schema lives only in the type checker.',
                  'Pick the shape that matches the problem: a dataclass when methods or mutability '
                  'help; a `NamedTuple` for small immutable records that benefit from unpacking; a '
                  '`TypedDict` for JSON-shaped data that should stay as a dict at the boundary.'],
  'notes': ['`@dataclass` — mutable, attribute access, methods; good default when behavior travels '
            'with data.',
            '`typing.NamedTuple` — immutable, attribute + index access, tuple semantics; good for '
            'small records that flow through unpacking.',
            '`typing.TypedDict` — runtime is `dict`, schema is type-checker-only; good for '
            'JSON-shaped data.',
            '`collections.namedtuple` is the older, untyped form of `NamedTuple`; prefer the '
            '`typing` version in new code.'],
  'see_also': ['dataclasses', 'typed-dicts', 'tuples', 'classes'],
  'cells': [{'kind': 'cell',
             'prose': ['A dataclass is a normal class with `__init__` and `__repr__` generated '
                       'from the annotated fields. Instances are mutable, support attribute '
                       'access, and can carry methods like any other class.'],
             'code': 'from dataclasses import dataclass\n'
                     '\n'
                     '@dataclass\n'
                     'class UserClass:\n'
                     '    name: str\n'
                     '    score: int\n'
                     '\n'
                     'a = UserClass("Ada", 98)\n'
                     'print(a)\n'
                     'a.score = 100\n'
                     'print(a.score)',
             'output': "UserClass(name='Ada', score=98)\n100"},
            {'kind': 'cell',
             'prose': ['A `NamedTuple` is a tuple subclass with named positions. Instances are '
                       'immutable, support both `obj.field` and `obj[index]`, and the helper '
                       '`_replace` produces a modified copy without mutating the original (since '
                       'assigning to a field would fail).'],
             'code': 'from typing import NamedTuple\n'
                     '\n'
                     'class UserTuple(NamedTuple):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '\n'
                     'b = UserTuple("Ada", 98)\n'
                     'print(b)\n'
                     'print(b.name, b[1])\n'
                     'print(b._replace(score=100))',
             'output': "UserTuple(name='Ada', score=98)\nAda 98\nUserTuple(name='Ada', score=100)"},
            {'kind': 'cell',
             'prose': ['A `TypedDict` is a plain dictionary at runtime. The annotations exist only '
                       'for the type checker, so the value behaves like any `dict` — useful for '
                       'JSON-shaped data that crosses an API boundary as a mapping.'],
             'code': 'from typing import TypedDict\n'
                     '\n'
                     'class UserDict(TypedDict):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '\n'
                     'c: UserDict = {"name": "Ada", "score": 98}\n'
                     'print(c)\n'
                     'print(c["name"])\n'
                     'print(type(c).__name__)',
             'output': "{'name': 'Ada', 'score': 98}\nAda\ndict"},
            {'kind': 'cell',
             'prose': ['Same record, three runtime identities. The dataclass is its own class. The '
                       '`NamedTuple` is literally a tuple. The `TypedDict` is literally a dict. '
                       'That difference drives the choice: pick the form whose runtime behavior '
                       'matches what the rest of the program already expects.'],
             'code': 'print(isinstance(a, UserClass))\n'
                     'print(isinstance(b, tuple))\n'
                     'print(isinstance(c, dict))',
             'output': 'True\nTrue\nTrue'}],
  'code': 'from dataclasses import dataclass\n'
          'from typing import NamedTuple, TypedDict\n'
          '\n'
          '@dataclass\n'
          'class UserClass:\n'
          '    name: str\n'
          '    score: int\n'
          '\n'
          'class UserTuple(NamedTuple):\n'
          '    name: str\n'
          '    score: int\n'
          '\n'
          'class UserDict(TypedDict):\n'
          '    name: str\n'
          '    score: int\n'
          '\n'
          'a = UserClass("Ada", 98)\n'
          'print(a)\n'
          'a.score = 100\n'
          'print(a.score)\n'
          '\n'
          'b = UserTuple("Ada", 98)\n'
          'print(b)\n'
          'print(b.name, b[1])\n'
          'print(b._replace(score=100))\n'
          '\n'
          'c: UserDict = {"name": "Ada", "score": 98}\n'
          'print(c)\n'
          'print(c["name"])\n'
          'print(type(c).__name__)\n'
          '\n'
          'print(isinstance(a, UserClass))\n'
          'print(isinstance(b, tuple))\n'
          'print(isinstance(c, dict))\n',
  'expected_output': "UserClass(name='Ada', score=98)\n"
                     '100\n'
                     "UserTuple(name='Ada', score=98)\n"
                     'Ada 98\n'
                     "UserTuple(name='Ada', score=100)\n"
                     "{'name': 'Ada', 'score': 98}\n"
                     'Ada\n'
                     'dict\n'
                     'True\n'
                     'True\n'
                     'True\n'},
 {'slug': 'literal-and-final',
  'title': 'Literal and Final',
  'section': 'Types',
  'summary': 'Literal restricts exact values, while Final marks names that should not be rebound.',
  'doc_path': '/library/typing.html#typing.Literal',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Literal',
  'explanation': ['`Literal` and `Final` make two different static promises. `Literal` narrows a '
                  'value to exact allowed options. `Final` tells a type checker that a name should '
                  'not be rebound after its first assignment.',
                  'Both annotations help at API boundaries: a function can accept only known '
                  'modes, and a module can publish a constant that other code should treat as '
                  'fixed. Python still runs the same assignment rules at runtime, so these are '
                  'promises for tools and readers rather than runtime locks.',
                  'Use `Literal` when a small closed set is clearer than a broad `str` or `int`. '
                  'Use `Final` when rebinding would be a bug in the design, especially for module '
                  'constants and class attributes.'],
  'notes': ['`Literal` narrows values to a small exact set.',
            '`Final` prevents rebinding in static analysis, not at runtime.',
            'Use enums when the option set needs names, behavior, or iteration over members.'],
  'see_also': ['type-hints', 'constants', 'union-and-optional-types', 'overloads'],
  'cells': [{'kind': 'cell',
             'prose': ['`Literal` describes exact allowed values. A type checker can reject '
                       '`"debug"` as a `Mode` even though it is an ordinary string at runtime.'],
             'code': 'from typing import Final, Literal\n'
                     '\n'
                     'Mode = Literal["read", "write"]\n'
                     '\n'
                     '\n'
                     'def open_label(mode: Mode) -> str:\n'
                     '    return f"opening for {mode}"\n'
                     '\n'
                     'print(open_label("write"))',
             'output': 'opening for write'},
            {'kind': 'cell',
             'prose': ['`Final` marks a name that should not be rebound. It is stronger '
                       'documentation than the all-caps constant convention because static tools '
                       'can flag reassignment.'],
             'code': 'DEFAULT_MODE: Final[Mode] = "read"\nprint(open_label(DEFAULT_MODE))',
             'output': 'opening for read'},
            {'kind': 'cell',
             'prose': ['The annotation is not a runtime lock. Python still rebinds the name; the '
                       'mistake is that a type checker and human reader should reject the design.'],
             'code': 'DEFAULT_MODE = "debug"\nprint(DEFAULT_MODE)',
             'output': 'debug'}],
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
          '\n'
          'DEFAULT_MODE = "debug"\n'
          'print(DEFAULT_MODE)\n',
  'expected_output': 'opening for read\nopening for write\ndebug\n'},
 {'slug': 'callable-types',
  'title': 'Callable Types',
  'section': 'Types',
  'summary': 'Callable annotations describe functions passed as values.',
  'doc_path': '/library/typing.html#annotating-callable-objects',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#annotating-callable-objects',
  'explanation': ['Callable annotations describe values that can be called like functions. They '
                  'are useful when a function accepts a callback, strategy, predicate, or '
                  'transformation.',
                  '`Callable[[int], int]` says how the callback will be called: one integer '
                  'argument, integer result. The annotation helps tools and readers, while runtime '
                  'still only needs an object that is actually callable.',
                  'Use `Callable` for simple call shapes. Use a protocol when the callback needs '
                  'named attributes, overloaded signatures, or a more descriptive interface.'],
  'notes': ['Use `Callable[[Arg], Return]` for simple function-shaped values.',
            'The annotation documents how the callback will be called.',
            'For complex call signatures, protocols can be clearer.'],
  'see_also': ['functions', 'callable-objects', 'protocols'],
  'cells': [{'kind': 'cell',
             'prose': ['Use `Callable[[Arg], Return]` for function-shaped values. The callback is '
                       'passed in and called by the receiving function.'],
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
             'output': '5'},
            {'kind': 'cell',
             'prose': ['Callable annotations are structural: an object with `__call__` can also '
                       'satisfy the shape.'],
             'code': 'class Doubler:\n'
                     '    def __call__(self, number: int) -> int:\n'
                     '        return number * 2\n'
                     '\n'
                     'print(apply_twice(3, Doubler()))',
             'output': '12'},
            {'kind': 'cell',
             'prose': ['Runtime callability is a separate question from static annotation. '
                       '`callable()` checks whether Python can call the object.'],
             'code': 'print(callable(add_one), callable(Doubler()))',
             'output': 'True True'}],
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
  'expected_output': '5\n12\nTrue True\n'},
 {'slug': 'generics-and-typevar',
  'title': 'Generics and TypeVar',
  'section': 'Types',
  'summary': 'Generics preserve type information across reusable functions and classes.',
  'doc_path': '/library/typing.html#generics',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#generics',
  'explanation': ['Generics connect types across an API. A plain function that returns `object` '
                  'loses information; a generic function can say that the returned value has the '
                  'same type as the input element.',
                  'A `TypeVar` stands for a type chosen by the caller. In `list[T] -> T`, the same '
                  '`T` says that a list of strings produces a string and a list of integers '
                  'produces an integer.',
                  'Use generics when a function or class is reusable but still preserves a '
                  'relationship between input and output types.'],
  'notes': ['A `TypeVar` stands for a type chosen by the caller.',
            'Python 3.12+ also accepts the inline PEP 695 spelling `def first[T](items: list[T]) '
            '-> T`, which declares the variable without a separate `TypeVar` line; the explicit '
            'form shown here works everywhere and reads the same way.',
            'Generic functions avoid losing information to `object` or `Any`.',
            'Use generics when input and output types are connected.'],
  'see_also': ['type-hints', 'collections-module', 'casts-and-any'],
  'cells': [{'kind': 'cell',
             'prose': ['A `TypeVar` stands for a type chosen by the caller. The return type '
                       'follows the list element type.'],
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
             'output': '1\nAda'},
            {'kind': 'cell',
             'prose': ['Reusing the same `TypeVar` expresses a relationship between parameters and '
                       'results.'],
             'code': 'def pair(left: T, right: T) -> tuple[T, T]:\n'
                     '    return (left, right)\n'
                     '\n'
                     'print(pair("x", "y"))',
             'output': "('x', 'y')"},
            {'kind': 'cell',
             'prose': ['`TypeVar` is visible at runtime, but the relationship is mainly for type '
                       'checkers.'],
             'code': 'print(T.__name__)\nprint(first.__annotations__)',
             'output': "T\n{'items': list[~T], 'return': ~T}"}],
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
  'expected_output': "1\nAda\n('x', 'y')\nT\n"},
 {'slug': 'paramspec',
  'title': 'ParamSpec',
  'section': 'Types',
  'summary': 'ParamSpec preserves callable parameter types through wrappers.',
  'doc_path': '/library/typing.html#typing.ParamSpec',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.ParamSpec',
  'explanation': ['`ParamSpec` is for decorators and wrapper functions that should keep the '
                  "wrapped callable's parameter shape. Without it, a generic decorator often falls "
                  'back to `Callable[..., R]`, which says “this returns the right type, but I no '
                  'longer know what arguments are valid.”',
                  'Use `ParamSpec` when the wrapper forwards `*args` and `**kwargs` to the '
                  'original function without changing the signature. Use a plain `Callable` when '
                  'the wrapper deliberately accepts a different set of parameters.',
                  "`P.args` and `P.kwargs` annotate the wrapper's forwarded arguments. A separate "
                  "`TypeVar` keeps the return type tied to the wrapped function's return type."],
  'notes': ["`ParamSpec` preserves a callable's parameter list through transparent wrappers.",
            'Pair `ParamSpec` with a `TypeVar` when the return type should also be preserved.',
            'Python 3.12+ also accepts the inline PEP 695 spelling `def wrap[**P, R](func: '
            'Callable[P, R])`, which declares both variables in the signature itself.',
            'If the wrapper changes the public signature, write that new signature directly '
            'instead.'],
  'see_also': ['callable-types', 'decorators', 'generics-and-typevar'],
  'cells': [{'kind': 'cell',
             'prose': ['`Callable[..., R]` is sometimes too broad. It preserves the return type, '
                       'but the ellipsis means the callable accepts any argument list as far as '
                       'the type checker can tell.'],
             'code': 'from collections.abc import Callable\n'
                     'from typing import ParamSpec, TypeVar\n'
                     '\n'
                     'R = TypeVar("R")\n'
                     '\n'
                     '\n'
                     'def erased(func: Callable[..., R]) -> Callable[..., R]:\n'
                     '    return func\n'
                     '\n'
                     'print(erased.__name__)',
             'output': 'erased'},
            {'kind': 'cell',
             'prose': ['`ParamSpec` captures the original parameters and lets the wrapper forward '
                       'exactly that shape.'],
             'code': 'P = ParamSpec("P")\n'
                     '\n'
                     '\n'
                     'def logged(func: Callable[P, R]) -> Callable[P, R]:\n'
                     '    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:\n'
                     '        print("calling", func.__name__)\n'
                     '        return func(*args, **kwargs)\n'
                     '    return wrapper\n'
                     '\n'
                     'print(logged.__name__)',
             'output': 'logged'},
            {'kind': 'cell',
             'prose': ['The decorated function still runs normally. The benefit is static: tools '
                       'can keep checking that `add` receives two integers.'],
             'code': '@logged\n'
                     'def add(left: int, right: int) -> int:\n'
                     '    return left + right\n'
                     '\n'
                     'print(erased(add)(2, 3))\n'
                     'print(add(2, 3))',
             'output': 'calling add\n5\ncalling add\n5'}],
  'code': 'from collections.abc import Callable\n'
          'from typing import ParamSpec, TypeVar\n'
          '\n'
          'P = ParamSpec("P")\n'
          'R = TypeVar("R")\n'
          '\n'
          '\n'
          'def erased(func: Callable[..., R]) -> Callable[..., R]:\n'
          '    return func\n'
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
          'print(erased(add)(2, 3))\n'
          'print(add(2, 3))\n',
  'expected_output': 'calling add\n5\ncalling add\n5\n'},
 {'slug': 'overloads',
  'title': 'Overloads',
  'section': 'Types',
  'summary': 'overload describes APIs whose return type depends on argument types.',
  'doc_path': '/library/typing.html#typing.overload',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.overload',
  'explanation': ['`@overload` lets type checkers describe a function whose return type depends on '
                  'the argument types. The overload declarations are static-only promises; the '
                  'runtime function is still the single implementation that appears after them.',
                  'Use overloads when a union return type would be too vague for callers. For '
                  'example, `double(4)` returns an `int`, while `double("ha")` returns a `str`; '
                  '`int | str` loses that relationship.',
                  'At runtime the overload stubs are not dispatch cases. The implementation must '
                  'inspect or operate on the value just like any other Python function.'],
  'notes': ['Put `@overload` declarations immediately before the implementation.',
            'Overloads improve static precision; they do not create runtime dispatch.',
            'If all callers can work with one broad return type, a simple union annotation is '
            'usually enough.'],
  'see_also': ['type-hints', 'union-and-optional-types', 'generics-and-typevar'],
  'cells': [{'kind': 'cell',
             'prose': ['The overload stubs give static tools precise call shapes: integer in, '
                       'integer out; string in, string out.'],
             'code': 'from typing import overload\n'
                     '\n'
                     '@overload\n'
                     'def double(value: int) -> int: ...\n'
                     '\n'
                     '@overload\n'
                     'def double(value: str) -> str: ...\n'
                     '\n'
                     'print("static signatures only")',
             'output': 'static signatures only'},
            {'kind': 'cell',
             'prose': ['There is still one runtime implementation. It must accept every shape '
                       'promised by the overloads.'],
             'code': 'def double(value: int | str) -> int | str:\n'
                     '    return value * 2\n'
                     '\n'
                     'print(double(4))\n'
                     'print(double("ha"))',
             'output': '8\nhaha'},
            {'kind': 'cell',
             'prose': ["Only the implementation's annotations are visible on the runtime function. "
                       'The overload declarations were for the type checker.'],
             'code': 'print(double.__annotations__)',
             'output': "{'value': int | str, 'return': int | str}"}],
  'code': 'from typing import overload\n'
          '\n'
          '@overload\n'
          'def double(value: int) -> int: ...\n'
          '\n'
          '@overload\n'
          'def double(value: str) -> str: ...\n'
          '\n'
          'def double(value: int | str) -> int | str:\n'
          '    return value * 2\n'
          '\n'
          'print(double(4))\n'
          'print(double("ha"))\n'
          'print(double.__annotations__)\n',
  'expected_output': "8\nhaha\n{'value': int | str, 'return': int | str}\n"},
 {'slug': 'casts-and-any',
  'title': 'Casts and Any',
  'section': 'Types',
  'summary': 'Any and cast are escape hatches for places static analysis cannot prove.',
  'doc_path': '/library/typing.html#typing.cast',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.cast',
  'explanation': ['`Any` and `cast()` are escape hatches. They are useful at messy boundaries '
                  'where a type checker cannot prove what a value is, but they also remove '
                  'protection when overused.',
                  '`Any` tells static tools to stop checking most operations on a value. `cast(T, '
                  'value)` tells the type checker to treat a value as `T`, but it returns the same '
                  'runtime object unchanged.',
                  'Prefer narrowing with runtime checks when possible. Use `cast()` when another '
                  'invariant already proves the type and the checker cannot see that proof.'],
  'notes': ['`Any` disables most static checking for a value.',
            '`cast()` tells the type checker to trust you without changing the runtime object.',
            'Prefer narrowing with checks when possible.'],
  'see_also': ['type-hints', 'runtime-type-checks', 'typed-dicts'],
  'cells': [{'kind': 'cell',
             'prose': ['`Any` disables most static checking for a value. The runtime object is '
                       'still whatever value was actually assigned.'],
             'code': 'from typing import Any, cast\n'
                     '\n'
                     'raw: Any = {"score": "98"}\n'
                     'score_text = cast(dict[str, str], raw)["score"]\n'
                     'score = int(score_text)\n'
                     'print(score + 2)',
             'output': '100'},
            {'kind': 'cell',
             'prose': ['`cast()` does not convert or validate the value. It returns the same '
                       'object at runtime.'],
             'code': 'print(cast(list[int], raw) is raw)\nprint(type(raw).__name__)',
             'output': 'True\ndict'},
            {'kind': 'cell',
             'prose': ['A real runtime check narrows by inspecting the value. This is safer when '
                       'the input is untrusted.'],
             'code': 'value: object = {"score": "98"}\n'
                     'if isinstance(value, dict):\n'
                     '    print(value["score"])',
             'output': '98'}],
  'code': 'from typing import Any, cast\n'
          '\n'
          'raw: Any = {"score": "98"}\n'
          'score_text = cast(dict[str, str], raw)["score"]\n'
          'score = int(score_text)\n'
          '\n'
          'print(score + 2)\n'
          'print(cast(list[int], raw) is raw)\n'
          'print(type(raw).__name__)\n'
          '\n'
          'value: object = {"score": "98"}\n'
          'if isinstance(value, dict):\n'
          '    print(value["score"])\n',
  'expected_output': '100\nTrue\ndict\n98\n'},
 {'slug': 'newtype',
  'title': 'NewType',
  'section': 'Types',
  'summary': 'NewType creates distinct static identities for runtime-compatible values.',
  'doc_path': '/library/typing.html#typing.NewType',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.NewType',
  'explanation': ['`NewType` creates a distinct static identity for a value that is represented by '
                  'an existing runtime type. It is useful for IDs, units, and other values that '
                  'should not be mixed accidentally.',
                  'The key boundary is static versus runtime behavior. A type checker can '
                  'distinguish `UserId` from `OrderId`, but at runtime both values are plain '
                  'integers.',
                  'Use a type alias when you only want a clearer name for a shape. Use `NewType` '
                  'when mixing two compatible shapes should be treated as a mistake by static '
                  'analysis.'],
  'notes': ['`NewType` helps type checkers distinguish values that share a runtime representation.',
            'At runtime, the value is still the underlying type.',
            'Use aliases for readability; use `NewType` for static separation.'],
  'see_also': ['type-aliases', 'type-hints', 'runtime-type-checks'],
  'cells': [{'kind': 'cell',
             'prose': ['`NewType` helps type checkers distinguish values that share a runtime '
                       'representation.'],
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
             'output': 'user 42'},
            {'kind': 'cell',
             'prose': ['At runtime, a `NewType` value is the underlying value. It compares like '
                       'that value and has the same runtime type.'],
             'code': 'oid = OrderId(42)\nprint(uid == oid)\nprint(type(uid).__name__)',
             'output': 'True\nint'},
            {'kind': 'cell',
             'prose': ['The `NewType` constructor keeps a name for static tools and '
                       'introspection.'],
             'code': 'print(UserId.__name__)\nprint(OrderId.__name__)',
             'output': 'UserId\nOrderId'}],
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
  'expected_output': 'user 42\nTrue\nint\nUserId\n'},
 {'slug': 'protocols',
  'title': 'Protocols',
  'section': 'Types',
  'summary': 'Protocol describes required behavior for structural typing.',
  'doc_path': '/library/typing.html#typing.Protocol',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Protocol',
  'explanation': ['`Protocol` describes the methods or attributes an object must provide. It '
                  'exists for structural typing: if an object has the right shape, type checkers '
                  'can treat it as compatible.',
                  'This is different from inheritance. Inheritance says a class is explicitly '
                  'derived from a parent; a protocol says callers only need a particular behavior.',
                  'At runtime, ordinary method lookup still applies. Protocols are mainly for '
                  'static analysis, documentation, and API boundaries.'],
  'notes': ['Protocols are for structural typing: compatibility by shape rather than explicit '
            'inheritance.',
            'Type checkers understand protocols; normal runtime method calls still do the work.',
            'Prefer inheritance when shared implementation matters, and protocols when only '
            'required behavior matters.'],
  'see_also': ['type-hints', 'classes', 'inheritance-and-super', 'abstract-base-classes'],
  'cells': [{'kind': 'cell',
             'prose': ['A protocol names required behavior. The ellipsis marks the method body as '
                       'intentionally unspecified, similar to an interface declaration.'],
             'code': 'from typing import Protocol\n'
                     '\n'
                     'class Greeter(Protocol):\n'
                     '    def greet(self) -> str:\n'
                     '        ...\n'
                     '\n'
                     'print(Greeter.__name__)',
             'output': 'Greeter'},
            {'kind': 'cell',
             'prose': ['A class can satisfy the protocol without inheriting from it. `Person` has '
                       'a compatible `greet()` method, so it has the right shape for static type '
                       'checkers.'],
             'code': 'class Person:\n'
                     '    def __init__(self, name):\n'
                     '        self.name = name\n'
                     '\n'
                     '    def greet(self):\n'
                     '        return f"hello {self.name}"\n'
                     '\n'
                     'print(Person("Ada").greet())',
             'output': 'hello Ada'},
            {'kind': 'cell',
             'prose': ['Use the protocol as an annotation at the API boundary. The function only '
                       'cares that the object can greet; it does not care about the concrete '
                       'class.'],
             'code': 'def welcome(greeter: Greeter):\n'
                     '    print(greeter.greet())\n'
                     '\n'
                     'welcome(Person("Ada"))',
             'output': 'hello Ada'}],
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
  'expected_output': 'hello Ada\nGreeter\n'},
 {'slug': 'abstract-base-classes',
  'title': 'Abstract Base Classes',
  'section': 'Classes',
  'summary': 'ABC and abstractmethod enforce that subclasses implement required methods.',
  'doc_path': '/library/abc.html',
  'doc_url': 'https://docs.python.org/3.13/library/abc.html',
  'explanation': ['`ABC` and `@abstractmethod` describe an interface that subclasses must '
                  'implement. The base class refuses to instantiate until a concrete subclass '
                  'provides every abstract method, which catches "I forgot to implement this" at '
                  'construction time rather than at the first method call.',
                  'ABCs are different from `Protocol`. An ABC is nominal: a class participates in '
                  'the contract by inheriting from it. A `Protocol` is structural: any class with '
                  'the right methods qualifies, no inheritance required. Reach for an ABC when you '
                  'want shared implementation in the base class or you want `isinstance()` to mean '
                  '"explicitly opted in"; reach for a `Protocol` when you only care about behavior '
                  'at the API boundary.',
                  'The cost is a small amount of ceremony at the type level. The benefit is that a '
                  'half-implemented subclass cannot be created by accident.'],
  'notes': ['`ABC` plus `@abstractmethod` blocks instantiation until every abstract method has an '
            'implementation.',
            'ABCs are nominal — subclasses opt in by inheriting; `isinstance()` reflects that '
            'opt-in.',
            'Protocols are structural — any class with the right shape qualifies, regardless of '
            'inheritance.',
            'Prefer an ABC when shared implementation or explicit opt-in matters; prefer a '
            'Protocol when only behavior at the API boundary matters.'],
  'see_also': ['protocols', 'inheritance-and-super', 'classes'],
  'cells': [{'kind': 'cell',
             'prose': ['`ABC` plus `@abstractmethod` declares the contract. Trying to construct '
                       'the base class itself fails because at least one method has no '
                       'implementation. A concrete `describe()` lives alongside the abstract '
                       '`area()` so subclasses inherit shared behavior for free.'],
             'code': 'from abc import ABC, abstractmethod\n'
                     '\n'
                     'class Shape(ABC):\n'
                     '    @abstractmethod\n'
                     '    def area(self) -> float:\n'
                     '        ...\n'
                     '\n'
                     '    def describe(self) -> str:\n'
                     '        return f"shape with area {self.area()}"\n'
                     '\n'
                     'try:\n'
                     '    Shape()\n'
                     'except TypeError as error:\n'
                     '    print(error)',
             'output': "Can't instantiate abstract class Shape without an implementation for "
                       "abstract method 'area'"},
            {'kind': 'cell',
             'prose': ['A subclass that implements every abstract method is concrete and can be '
                       'instantiated. It also inherits the non-abstract methods from the base '
                       'class.'],
             'code': 'class Square(Shape):\n'
                     '    def __init__(self, side):\n'
                     '        self.side = side\n'
                     '\n'
                     '    def area(self):\n'
                     '        return self.side ** 2\n'
                     '\n'
                     'print(Square(3).area())\n'
                     'print(Square(3).describe())',
             'output': '9\nshape with area 9'},
            {'kind': 'cell',
             'prose': ['A subclass that forgets to implement an abstract method also cannot be '
                       'instantiated — that is the value the ABC adds. The error fires at '
                       'construction, not when something later tries to call the missing method.'],
             'code': 'class Incomplete(Shape):\n'
                     '    pass\n'
                     '\n'
                     'try:\n'
                     '    Incomplete()\n'
                     'except TypeError as error:\n'
                     '    print(error)',
             'output': "Can't instantiate abstract class Incomplete without an implementation for "
                       "abstract method 'area'"},
            {'kind': 'cell',
             'prose': ['Contrast with `Protocol`. A `HasArea` protocol accepts any class with an '
                       '`area()` method, no inheritance required. `Triangle` does not inherit from '
                       '`Shape`, so it satisfies the protocol but fails `isinstance(_, Shape)`. '
                       '`Square` satisfies both because it explicitly inherited from the ABC.'],
             'code': 'from typing import Protocol\n'
                     '\n'
                     'class HasArea(Protocol):\n'
                     '    def area(self) -> float:\n'
                     '        ...\n'
                     '\n'
                     'class Triangle:\n'
                     '    def __init__(self, base, height):\n'
                     '        self.base = base\n'
                     '        self.height = height\n'
                     '\n'
                     '    def area(self):\n'
                     '        return 0.5 * self.base * self.height\n'
                     '\n'
                     'def total_area(shapes: list[HasArea]) -> float:\n'
                     '    return sum(shape.area() for shape in shapes)\n'
                     '\n'
                     'print(total_area([Square(3), Triangle(4, 3)]))\n'
                     'print(isinstance(Triangle(4, 3), Shape))\n'
                     'print(isinstance(Square(3), Shape))',
             'output': '15.0\nFalse\nTrue'}],
  'code': 'from abc import ABC, abstractmethod\n'
          'from typing import Protocol\n'
          '\n'
          'class Shape(ABC):\n'
          '    @abstractmethod\n'
          '    def area(self) -> float:\n'
          '        ...\n'
          '\n'
          '    def describe(self) -> str:\n'
          '        return f"shape with area {self.area()}"\n'
          '\n'
          'try:\n'
          '    Shape()\n'
          'except TypeError as error:\n'
          '    print(error)\n'
          '\n'
          'class Square(Shape):\n'
          '    def __init__(self, side):\n'
          '        self.side = side\n'
          '\n'
          '    def area(self):\n'
          '        return self.side ** 2\n'
          '\n'
          'print(Square(3).area())\n'
          'print(Square(3).describe())\n'
          '\n'
          'class Incomplete(Shape):\n'
          '    pass\n'
          '\n'
          'try:\n'
          '    Incomplete()\n'
          'except TypeError as error:\n'
          '    print(error)\n'
          '\n'
          'class HasArea(Protocol):\n'
          '    def area(self) -> float:\n'
          '        ...\n'
          '\n'
          'class Triangle:\n'
          '    def __init__(self, base, height):\n'
          '        self.base = base\n'
          '        self.height = height\n'
          '\n'
          '    def area(self):\n'
          '        return 0.5 * self.base * self.height\n'
          '\n'
          'def total_area(shapes: list[HasArea]) -> float:\n'
          '    return sum(shape.area() for shape in shapes)\n'
          '\n'
          'print(total_area([Square(3), Triangle(4, 3)]))\n'
          'print(isinstance(Triangle(4, 3), Shape))\n'
          'print(isinstance(Square(3), Shape))\n',
  'expected_output': "Can't instantiate abstract class Shape without an implementation for "
                     "abstract method 'area'\n"
                     '9\n'
                     'shape with area 9\n'
                     "Can't instantiate abstract class Incomplete without an implementation for "
                     "abstract method 'area'\n"
                     '15.0\n'
                     'False\n'
                     'True\n'},
 {'slug': 'enums',
  'title': 'Enums',
  'section': 'Types',
  'summary': 'Enum defines symbolic names for a fixed set of values.',
  'doc_path': '/library/enum.html',
  'doc_url': 'https://docs.python.org/3.13/library/enum.html',
  'explanation': ['`Enum` defines a fixed set of named values. This makes states and modes easier '
                  'to read than raw strings scattered through a program.',
                  'Each enum member has a name and a value. Comparing enum members is explicit and '
                  'helps avoid typos that plain strings would allow.',
                  'Use enums when a value must be one of a small known set: statuses, modes, '
                  'directions, roles, and similar choices.'],
  'notes': ['Enums make states and choices explicit.',
            'Members have names and values.',
            'Comparing enum members avoids string typo bugs.',
            'Prefer raw strings for open-ended text; prefer enums for a closed set of named '
            'choices.'],
  'see_also': ['literals', 'classes', 'literal-and-final'],
  'cells': [{'kind': 'cell',
             'prose': ['An enum member has a symbolic name and an underlying value. The symbolic '
                       'name is what readers usually care about in code.'],
             'code': 'from enum import Enum\n'
                     '\n'
                     'class Status(Enum):\n'
                     '    PENDING = "pending"\n'
                     '    DONE = "done"\n'
                     '\n'
                     'current = Status.PENDING\n'
                     'print(current.name)\n'
                     'print(current.value)',
             'output': 'PENDING\npending'},
            {'kind': 'cell',
             'prose': ['Compare enum members with enum members, not with raw strings. This keeps '
                       'the set of valid states explicit.'],
             'code': 'print(current is Status.PENDING)\nprint(current == "pending")',
             'output': 'True\nFalse'}],
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
  'expected_output': 'PENDING\npending\nTrue\nFalse\n'},
 {'slug': 'regular-expressions',
  'title': 'Regular Expressions',
  'section': 'Text',
  'summary': 'The re module searches and extracts text using regular expressions.',
  'doc_path': '/library/re.html',
  'doc_url': 'https://docs.python.org/3.13/library/re.html',
  'explanation': ['Regular expressions are a compact language for searching and extracting text '
                  "patterns. Python's `re` module provides the standard interface: `re.match` "
                  'anchors at the start of the string, `re.search` finds the first occurrence '
                  'anywhere, `re.findall` collects every match, `re.sub` rewrites matches, and '
                  '`re.compile` reuses a pattern.',
                  'Use regex when the pattern has structure: repeated records, alternatives, '
                  'optional parts, or pieces you want to capture. Prefer ordinary string methods '
                  'for simple substring checks because simpler code is easier to maintain.',
                  'Flags such as `re.IGNORECASE` adjust matching behavior without rewriting the '
                  'pattern. Pair them with `re.compile` when the same pattern is used repeatedly.'],
  'notes': ['Use raw strings for regex patterns so backslashes are easier to read.',
            'Use capturing groups when the point is extraction, not just matching.',
            '`re.match` anchors at the start; `re.search` finds the first match anywhere.',
            '`re.compile` saves work when the pattern runs more than once.',
            '`re.sub` rewrites matches; flags like `re.IGNORECASE` change matching behavior '
            'without rewriting the pattern.',
            'Reach for string methods before regex when the pattern is simple.'],
  'see_also': ['strings', 'string-formatting'],
  'cells': [{'kind': 'cell',
             'prose': ['Raw strings keep backslashes readable in regex patterns. Capturing groups '
                       'return just the pieces inside parentheses.'],
             'code': 'import re\n'
                     '\n'
                     'text = "Ada: 10, Grace: 9"\n'
                     'pattern = r"([A-Za-z]+): (\\d+)"\n'
                     '\n'
                     'for name, score in re.findall(pattern, text):\n'
                     '    print(name, int(score))',
             'output': 'Ada 10\nGrace 9'},
            {'kind': 'cell',
             'prose': ['`re.search()` finds the first match. A match object exposes captured '
                       'groups by position.'],
             'code': 'match = re.search(r"Grace: (\\d+)", text)\nprint(match.group(1))',
             'output': '9'},
            {'kind': 'cell',
             'prose': ['For a simple substring check, ordinary string membership is clearer than '
                       'regex.'],
             'code': 'print("Grace" in text)',
             'output': 'True'},
            {'kind': 'cell',
             'prose': ['`re.match` only matches at the start of the string; `re.search` finds the '
                       'first match anywhere. Picking the right one keeps anchoring intent visible '
                       'without an explicit `^`.'],
             'code': 'start = re.match(r"Ada", text)\n'
                     'print(start is not None)\n'
                     'print(re.match(r"Grace", text))',
             'output': 'True\nNone'},
            {'kind': 'cell',
             'prose': ['`re.compile` produces a reusable pattern object and gives the pattern a '
                       'name. The `re` module also caches recently compiled patterns internally, '
                       'so the practical wins are readability and a place to attach flags more '
                       'than raw speed.'],
             'code': 'scoreline = re.compile(pattern)\nprint(scoreline.findall(text))',
             'output': "[('Ada', '10'), ('Grace', '9')]"},
            {'kind': 'cell',
             'prose': ['Flags such as `re.IGNORECASE` adjust matching without changing the '
                       'pattern. `re.sub` replaces every match with a replacement string and '
                       'returns the rewritten text.'],
             'code': 'casey = "ADA: 11"\n'
                     'print(re.search(r"ada", casey, flags=re.IGNORECASE).group(0))\n'
                     '\n'
                     'print(re.sub(r"\\d+", "?", text))',
             'output': 'ADA\nAda: ?, Grace: ?'}],
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
          'print("Grace" in text)\n'
          '\n'
          'start = re.match(r"Ada", text)\n'
          'print(start is not None)\n'
          'print(re.match(r"Grace", text))\n'
          '\n'
          'scoreline = re.compile(pattern)\n'
          'print(scoreline.findall(text))\n'
          '\n'
          'casey = "ADA: 11"\n'
          'print(re.search(r"ada", casey, flags=re.IGNORECASE).group(0))\n'
          '\n'
          'print(re.sub(r"\\d+", "?", text))\n',
  'expected_output': 'Ada 10\n'
                     'Grace 9\n'
                     '9\n'
                     'True\n'
                     'True\n'
                     'None\n'
                     "[('Ada', '10'), ('Grace', '9')]\n"
                     'ADA\n'
                     'Ada: ?, Grace: ?\n'},
 {'slug': 'number-parsing',
  'title': 'Number Parsing',
  'section': 'Standard Library',
  'summary': 'int() and float() parse text into numbers and raise ValueError on bad input.',
  'doc_path': '/library/functions.html#int',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#int',
  'explanation': ['Parsing turns text from files, forms, command lines, or network messages into '
                  'numeric objects. `int()` parses whole-number text, and `float()` parses decimal '
                  'or scientific-notation text.',
                  'Invalid numeric text raises `ValueError`. Catch that specific exception when '
                  'bad user input is expected and recoverable; let it fail loudly when the string '
                  'is supposed to be trusted program data.',
                  '`int()` also accepts a base, which is useful at protocol boundaries where '
                  'numbers are written in hexadecimal, binary, or another explicit notation.'],
  'notes': ['`int()` and `float()` are constructors that also parse strings.',
            '`int(text, base)` makes non-decimal input explicit.',
            'Catch `ValueError` for recoverable user input; do not hide unexpected data '
            'corruption.'],
  'see_also': ['exceptions', 'strings', 'numbers'],
  'cells': [{'kind': 'cell',
             'prose': ['Use `int()` for whole numbers and `float()` for decimal text. Parsed '
                       'values are real numbers, not strings.'],
             'code': 'print(int("42"))\nprint(float("3.5"))',
             'output': '42\n3.5'},
            {'kind': 'cell',
             'prose': ['Pass a base when the text format says the number is not decimal.'],
             'code': 'print(int("ff", 16))',
             'output': '255'},
            {'kind': 'cell',
             'prose': ['Catch `ValueError` at the input boundary when invalid text is normal and '
                       'recoverable.'],
             'code': 'texts = ["10", "python", "20"]\n'
                     'for text in texts:\n'
                     '    try:\n'
                     '        print(int(text) * 2)\n'
                     '    except ValueError:\n'
                     '        print(f"skip {text!r}")',
             'output': "20\nskip 'python'\n40"}],
  'code': 'print(int("42"))\n'
          'print(float("3.5"))\n'
          'print(int("ff", 16))\n'
          '\n'
          'texts = ["10", "python", "20"]\n'
          'for text in texts:\n'
          '    try:\n'
          '        print(int(text) * 2)\n'
          '    except ValueError:\n'
          '        print(f"skip {text!r}")\n',
  'expected_output': "42\n3.5\n255\n20\nskip 'python'\n40\n"},
 {'slug': 'custom-exceptions',
  'title': 'Custom Exceptions',
  'section': 'Errors',
  'summary': 'Custom exception classes name failures that belong to your domain.',
  'doc_path': '/tutorial/errors.html#user-defined-exceptions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#user-defined-exceptions',
  'explanation': ['Custom exceptions give names to failures in your problem domain. A named '
                  'exception is easier to catch and explain than a generic error with only a '
                  'string message.',
                  'Raise the custom exception at the point where the invalid state is discovered. '
                  'Include a message for the specific occurrence.',
                  'Catch custom exceptions at the boundary where recovery makes sense, such as '
                  'returning an error response or asking for corrected input.'],
  'notes': ['Subclass `Exception` for errors callers are expected to catch.',
            'A custom exception name can be clearer than reusing a generic `ValueError` '
            'everywhere.',
            'Catch custom exceptions at a boundary that can recover or report clearly.'],
  'see_also': ['exceptions', 'exception-chaining', 'warnings', 'logging'],
  'cells': [{'kind': 'cell',
             'prose': ['Create a custom exception when a failure has a name in your problem '
                       'domain. The class can be empty at first.'],
             'code': 'class EmptyCartError(Exception):\n    pass\n\nprint(EmptyCartError.__name__)',
             'output': 'EmptyCartError'},
            {'kind': 'cell',
             'prose': ['Raise the custom exception where the invalid state is detected. Normal '
                       'inputs still follow the ordinary success path.'],
             'code': 'def checkout(items):\n'
                     '    if not items:\n'
                     '        raise EmptyCartError("cart is empty")\n'
                     '    return "paid"\n'
                     '\n'
                     'print(checkout(["book"]))',
             'output': 'paid'},
            {'kind': 'cell',
             'prose': ['Callers can catch the precise error type without accidentally catching '
                       'unrelated failures.'],
             'code': 'try:\n    checkout([])\nexcept EmptyCartError as error:\n    print(error)',
             'output': 'cart is empty'}],
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
  'expected_output': 'EmptyCartError\npaid\ncart is empty\n'},
 {'slug': 'json',
  'title': 'JSON',
  'section': 'Standard Library',
  'summary': 'json encodes Python values as JSON text and decodes them back.',
  'doc_path': '/library/json.html',
  'doc_url': 'https://docs.python.org/3.13/library/json.html',
  'explanation': ['The `json` module converts between Python values and JSON text. Dictionaries, '
                  'lists, strings, numbers, booleans, and `None` map naturally to JSON structures.',
                  'Use `dumps()` when you need a string and `loads()` when you need Python objects '
                  'back. Options such as `sort_keys=True` and `indent=2` control stable, readable '
                  'output.',
                  'JSON is a data format, not a way to preserve arbitrary Python objects. Encode '
                  'simple data structures at service boundaries, and expect decode errors when the '
                  'incoming text is not valid JSON.'],
  'notes': ['`dumps()` returns a string; `loads()` accepts a string.',
            'JSON `true`, `false`, and `null` become Python `True`, `False`, and `None`.',
            'Use `sort_keys=True` when stable text output matters.',
            'JSON only represents data shapes, not arbitrary Python objects or behavior.'],
  'see_also': ['dicts', 'typed-dicts', 'strings'],
  'cells': [{'kind': 'cell',
             'prose': ['`dumps()` encodes Python data as JSON text. `sort_keys=True` keeps '
                       'dictionary keys in a stable order for reproducible output.'],
             'code': 'import json\n'
                     '\n'
                     'payload = {"language": "Python", "versions": [3, 13], "stable": True, '
                     '"missing": None}\n'
                     'text = json.dumps(payload, sort_keys=True)\n'
                     'print(text)',
             'output': '{"language": "Python", "missing": null, "stable": true, "versions": [3, '
                       '13]}'},
            {'kind': 'cell',
             'prose': ['Formatting options change the JSON text, not the Python value. `indent=2` '
                       'is useful for human-readable output.'],
             'code': 'pretty = json.dumps({"language": "Python", "stable": True}, indent=2, '
                     'sort_keys=True)\n'
                     'print(pretty.splitlines()[0])\n'
                     'print(pretty.splitlines()[1])',
             'output': '{\n  "language": "Python",'},
            {'kind': 'cell',
             'prose': ['`loads()` decodes JSON text back into Python values. JSON `null` becomes '
                       'Python `None`.'],
             'code': 'decoded = json.loads(text)\n'
                     'print(decoded["language"])\n'
                     'print(decoded["missing"] is None)',
             'output': 'Python\nTrue'},
            {'kind': 'cell',
             'prose': ['Invalid JSON raises `JSONDecodeError`, so input boundaries should handle '
                       'decode failures explicitly.'],
             'code': 'try:\n'
                     '    json.loads("{bad json}")\n'
                     'except json.JSONDecodeError as error:\n'
                     '    print(error.__class__.__name__)',
             'output': 'JSONDecodeError'}],
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
  'expected_output': '{"language": "Python", "missing": null, "stable": true, "versions": [3, '
                     '13]}\n'
                     '{\n'
                     '  "language": "Python",\n'
                     'Python\n'
                     'True\n'
                     'JSONDecodeError\n'},
 {'slug': 'logging',
  'title': 'Logging',
  'section': 'Standard Library',
  'summary': 'logging records operational events without using print as infrastructure.',
  'doc_path': '/library/logging.html',
  'doc_url': 'https://docs.python.org/3.13/library/logging.html',
  'explanation': ['`logging` records operational events without using `print` as infrastructure. A '
                  'logger names where an event came from, a handler decides where records go, a '
                  'formatter chooses their text shape, and a level decides which records are '
                  'important enough to emit.',
                  'Use logging for services, command-line tools, scheduled jobs, and libraries '
                  "that need diagnostics operators can filter. Use `print` for a program's "
                  'intentional user-facing output.',
                  'The example writes to stdout so the page stays deterministic. Real applications '
                  'usually configure handlers once at startup and then call '
                  '`logging.getLogger(__name__)` from each module.'],
  'notes': ['Configure logging once; call named loggers throughout the program.',
            'Logger and handler levels both participate in filtering.',
            'Use exceptions for control flow failures, logging for operational evidence, and '
            'warnings for soft compatibility problems.'],
  'see_also': ['exceptions', 'testing', 'modules'],
  'cells': [{'kind': 'cell',
             'prose': ['A logger name records which part of the program produced the event. The '
                       'handler and formatter choose where and how the event is shown.'],
             'code': 'import logging\n'
                     'import sys\n'
                     '\n'
                     'logger = logging.getLogger("example.worker")\n'
                     'logger.setLevel(logging.DEBUG)\n'
                     'handler = logging.StreamHandler(sys.stdout)\n'
                     'handler.setLevel(logging.INFO)\n'
                     'parts = ["%(levelname)s", "%(name)s", "%(message)s"]\n'
                     'formatter = logging.Formatter(":".join(parts))\n'
                     'handler.setFormatter(formatter)\n'
                     'logger.handlers[:] = [handler]\n'
                     'logger.propagate = False\n'
                     '\n'
                     'logger.debug("hidden detail")\n'
                     'logger.info("service started")\n'
                     'logger.warning("disk almost full")',
             'output': 'INFO:example.worker:service started\n'
                       'WARNING:example.worker:disk almost full'},
            {'kind': 'cell',
             'prose': ['Levels are thresholds. Raising the handler level to `WARNING` suppresses '
                       'later `INFO` records without changing the call sites.'],
             'code': 'import logging\n'
                     'import sys\n'
                     '\n'
                     'logger = logging.getLogger("example.worker")\n'
                     'logger.setLevel(logging.DEBUG)\n'
                     'handler = logging.StreamHandler(sys.stdout)\n'
                     'handler.setLevel(logging.WARNING)\n'
                     'parts = ["%(levelname)s", "%(name)s", "%(message)s"]\n'
                     'formatter = logging.Formatter(":".join(parts))\n'
                     'handler.setFormatter(formatter)\n'
                     'logger.handlers[:] = [handler]\n'
                     'logger.propagate = False\n'
                     '\n'
                     'logger.info("hidden after threshold change")\n'
                     'logger.error("write failed")',
             'output': 'ERROR:example.worker:write failed'}],
  'code': 'import logging\n'
          'import sys\n'
          '\n'
          'logger = logging.getLogger("example.worker")\n'
          'logger.setLevel(logging.DEBUG)\n'
          'handler = logging.StreamHandler(sys.stdout)\n'
          'handler.setLevel(logging.INFO)\n'
          'parts = ["%(levelname)s", "%(name)s", "%(message)s"]\n'
          'formatter = logging.Formatter(":".join(parts))\n'
          'handler.setFormatter(formatter)\n'
          'logger.handlers[:] = [handler]\n'
          'logger.propagate = False\n'
          '\n'
          'logger.debug("hidden detail")\n'
          'logger.info("service started")\n'
          'logger.warning("disk almost full")\n'
          '\n'
          'handler.setLevel(logging.WARNING)\n'
          'logger.info("hidden after threshold change")\n'
          'logger.error("write failed")\n',
  'expected_output': 'INFO:example.worker:service started\n'
                     'WARNING:example.worker:disk almost full\n'
                     'ERROR:example.worker:write failed\n'},
 {'slug': 'testing',
  'title': 'Testing',
  'section': 'Standard Library',
  'summary': 'Tests make expected behavior executable and repeatable.',
  'doc_path': '/library/unittest.html',
  'doc_url': 'https://docs.python.org/3.13/library/unittest.html',
  'explanation': ['Tests turn expected behavior into code that can be run again. The useful unit '
                  'is usually a small example of behavior with clear input, action, and assertion.',
                  "Python's `unittest` library provides test cases, assertions, suites, and "
                  'runners. Projects often use `pytest` for ergonomics, but the same idea remains: '
                  'a test names behavior and fails when the behavior changes.',
                  'A broad testing practice also includes fixtures, integration tests, property '
                  'tests, and coverage. This example stays on the smallest standard-library loop: '
                  'define behavior, assert the result, run the suite, inspect success.'],
  'notes': ['Test method names should describe behavior, not implementation details.',
            'A good unit test is deterministic and independent of test order.',
            'Use broader integration tests when the behavior depends on several components working '
            'together.'],
  'see_also': ['assertions', 'exceptions', 'modules'],
  'cells': [{'kind': 'cell',
             'prose': ['A test starts with behavior small enough to name. The function can be '
                       'ordinary code; the test supplies a representative input and expected '
                       'result.'],
             'code': 'def add(left, right):\n    return left + right\n\nprint(add(2, 3))',
             'output': '5'},
            {'kind': 'cell',
             'prose': ['`unittest.TestCase` groups test methods. `setUp` runs before each test '
                       'method to build per-test fixtures, `assertEqual` checks values, and '
                       '`assertRaises` asserts that a block raises the expected exception type.'],
             'code': 'import unittest\n'
                     '\n'
                     '\n'
                     'def divide(left, right):\n'
                     '    if right == 0:\n'
                     '        raise ZeroDivisionError("denominator is zero")\n'
                     '    return left / right\n'
                     '\n'
                     '\n'
                     'class AddTests(unittest.TestCase):\n'
                     '    def setUp(self):\n'
                     '        self.zero = 0\n'
                     '\n'
                     '    def test_adds_numbers(self):\n'
                     '        self.assertEqual(add(self.zero + 2, 3), 5)\n'
                     '\n'
                     '    def test_adds_empty_strings(self):\n'
                     '        self.assertEqual(add("", "py"), "py")\n'
                     '\n'
                     '    def test_divide_by_zero_raises(self):\n'
                     '        with self.assertRaises(ZeroDivisionError):\n'
                     '            divide(1, 0)\n'
                     '\n'
                     'print([name for name in dir(AddTests) if name.startswith("test_")])',
             'output': "['test_adds_empty_strings', 'test_adds_numbers', "
                       "'test_divide_by_zero_raises']"},
            {'kind': 'cell',
             'prose': ['A runner executes the suite and records whether every assertion passed. '
                       "Capturing the runner stream keeps this page's output deterministic."],
             'code': 'import io\n'
                     '\n'
                     'loader = unittest.defaultTestLoader\n'
                     'suite = loader.loadTestsFromTestCase(AddTests)\n'
                     'stream = io.StringIO()\n'
                     'runner = unittest.TextTestRunner(stream=stream, verbosity=0)\n'
                     'result = runner.run(suite)\n'
                     'print(result.testsRun)\n'
                     'print(result.wasSuccessful())',
             'output': '3\nTrue'}],
  'code': 'import io\n'
          'import unittest\n'
          '\n'
          '\n'
          'def add(left, right):\n'
          '    return left + right\n'
          '\n'
          '\n'
          'def divide(left, right):\n'
          '    if right == 0:\n'
          '        raise ZeroDivisionError("denominator is zero")\n'
          '    return left / right\n'
          '\n'
          '\n'
          'class AddTests(unittest.TestCase):\n'
          '    def setUp(self):\n'
          '        self.zero = 0\n'
          '\n'
          '    def test_adds_numbers(self):\n'
          '        self.assertEqual(add(self.zero + 2, 3), 5)\n'
          '\n'
          '    def test_adds_empty_strings(self):\n'
          '        self.assertEqual(add("", "py"), "py")\n'
          '\n'
          '    def test_divide_by_zero_raises(self):\n'
          '        with self.assertRaises(ZeroDivisionError):\n'
          '            divide(1, 0)\n'
          '\n'
          'loader = unittest.defaultTestLoader\n'
          'suite = loader.loadTestsFromTestCase(AddTests)\n'
          'stream = io.StringIO()\n'
          'runner = unittest.TextTestRunner(stream=stream, verbosity=0)\n'
          'result = runner.run(suite)\n'
          'print(result.testsRun)\n'
          'print(result.wasSuccessful())\n',
  'expected_output': '3\nTrue\n'},
 {'slug': 'subprocesses',
  'title': 'Subprocesses',
  'section': 'Standard Library',
  'summary': 'subprocess runs external commands with explicit arguments and captured outputs.',
  'doc_path': '/library/subprocess.html',
  'doc_url': 'https://docs.python.org/3.13/library/subprocess.html',
  'explanation': ['`subprocess` is the standard boundary for running external commands. It starts '
                  'another program, waits for it, and gives you a result object with the exit code '
                  'and captured output.',
                  'In standard Python this is the right tool for calling Git, compilers, shells, '
                  "or another Python interpreter. This site's live example runner does not expose "
                  'an operating-system process table, so the page teaches the proper '
                  '`subprocess.run()` contract and labels the runner boundary instead of '
                  'pretending the command can run here.',
                  'Use a list of arguments when possible, capture output when the parent program '
                  'needs to inspect it, and treat a non-zero return code as a failure. The '
                  'important boundary is between Python objects and the operating system: Python '
                  'prepares arguments and environment, then the child program reports back through '
                  'streams and an exit status.'],
  'notes': ['Use a list of arguments instead of shell strings when possible.',
            'Capture output when the parent program needs to inspect it.',
            '`check=True` turns non-zero exits into exceptions.',
            'The output shown here was produced by really spawning the child under standard '
            "CPython when the example was verified; the site's in-browser sandbox cannot create "
            'processes, so live runs of this page fail there.'],
  'see_also': ['virtual-environments', 'networking', 'threads-and-processes'],
  'cells': [{'kind': 'unsupported',
             'prose': ['`subprocess.run` spawns a child Python interpreter, captures its stdout '
                       'and stderr (`capture_output=True`), decodes them as text (`text=True`), '
                       'and raises `CalledProcessError` if the child exits non-zero '
                       '(`check=True`). The returned `result` holds the captured streams and exit '
                       'code as portable evidence the child ran. (The in-browser Run button cannot '
                       'spawn child processes, so pressing Run on this page fails in the sandbox; '
                       'the verified output below comes from standard CPython at build time.)'],
             'code': 'result = subprocess.run(\n'
                     '    [sys.executable, "-c", "print(\'child process\')"],\n'
                     '    text=True,\n'
                     '    capture_output=True,\n'
                     '    check=True,\n'
                     ')',
             'output': ''},
            {'kind': 'cell',
             'prose': ['`subprocess.run()` starts a child process and waits for it. '
                       "`capture_output=True` stores the child's standard output and error streams "
                       'on the result object.'],
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
             'output': 'child process\n0'}],
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
  'expected_output': 'child process\n0\n'},
 {'slug': 'threads-and-processes',
  'title': 'Threads and Processes',
  'section': 'Standard Library',
  'summary': 'Threads share memory, while processes run in separate interpreters.',
  'doc_path': '/library/concurrent.futures.html',
  'doc_url': 'https://docs.python.org/3.13/library/concurrent.futures.html',
  'explanation': ['Threads and processes are two ways to run work outside the current control '
                  'path. Threads are useful for overlapping I/O-shaped waits, while processes are '
                  'useful when CPU-bound work needs separate interpreter processes.',
                  'In standard Python, `ThreadPoolExecutor` and `ProcessPoolExecutor` are the '
                  "ordinary tools for this lesson. This site's live example runner does not expose "
                  'native threads or child processes, so this page keeps the proper executor model '
                  'visible and separates the standard Python idea from what can execute here.',
                  'This is different from `asyncio`: threads and processes run ordinary callables '
                  'through executors, while `async` code cooperatively awaits coroutines. Choose '
                  'the smallest concurrency model that matches the bottleneck.'],
  'notes': ['Threads share memory, so mutable shared state needs care.',
            'Processes avoid shared interpreter state but require values to cross a process '
            'boundary.',
            'Prefer `asyncio` for coroutine-based I/O and executors for ordinary blocking '
            'callables.',
            'The thread-pool output here was produced by real worker threads under standard '
            "CPython when the example was verified; the site's in-browser sandbox cannot create "
            'threads or processes, so live runs of this page fail there.'],
  'see_also': ['async-await', 'subprocesses', 'networking'],
  'cells': [{'kind': 'unsupported',
             'prose': ['`ThreadPoolExecutor` runs `square` across two worker threads sharing the '
                       'same interpreter (and the GIL); `ProcessPoolExecutor` runs `pow` across '
                       'two child processes with isolated memory. Each `pool.map` returns an '
                       'iterator over results in input order, and the surrounding `with` block '
                       'joins the workers when the body exits. (The in-browser Run button cannot '
                       'create native threads or child processes, so pressing Run on this page '
                       'fails in the sandbox; the verified thread-pool output below comes from '
                       'standard CPython at build time.)'],
             'code': 'with ThreadPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(square, [1, 2, 3])))\n'
                     '\n'
                     'with ProcessPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(pow, [4, 5], [2, 2])))',
             'output': ''},
            {'kind': 'cell',
             'prose': ['A thread pool runs ordinary callables while sharing memory with the '
                       'current process. `map()` returns results in input order.'],
             'code': 'from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor\n'
                     '\n'
                     '\n'
                     'def square(number):\n'
                     '    return number * number\n'
                     '\n'
                     'with ThreadPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(square, [1, 2, 3])))',
             'output': '[1, 4, 9]'},
            {'kind': 'cell',
             'prose': ['A process pool uses separate Python processes. That boundary is heavier, '
                       'but it can run CPU-bound work outside the current interpreter.'],
             'code': 'print(ProcessPoolExecutor.__name__)',
             'output': 'ProcessPoolExecutor'}],
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
  'expected_output': '[1, 4, 9]\nProcessPoolExecutor\n'},
 {'slug': 'networking',
  'title': 'Networking',
  'section': 'Standard Library',
  'summary': 'Networking code exchanges bytes across explicit protocol boundaries.',
  'doc_path': '/library/socket.html',
  'doc_url': 'https://docs.python.org/3.13/library/socket.html',
  'explanation': ['Networking code sends and receives bytes across protocol boundaries. '
                  'Higher-level HTTP clients hide many details, but the core rule remains: text is '
                  'encoded before it leaves the process and decoded after bytes come back.',
                  'In standard Python, the socket version of this lesson uses connected endpoints '
                  'such as `socket.create_connection()` or, for a local deterministic '
                  "demonstration, `socket.socketpair()`. This site's live example runner does not "
                  'expose arbitrary OS sockets or outbound calls, so this page teaches the socket '
                  'contract while making the runner constraint explicit.',
                  'The useful mental model is endpoint plus bytes plus cleanup. A socket connects '
                  'two endpoints, transfers byte strings, and must be closed when the conversation '
                  'is finished.'],
  'notes': ['Network protocols move bytes, not Python `str` objects.',
            'Close real sockets when finished, usually with a context manager or `finally` block.',
            'Use high-level HTTP libraries for application HTTP unless socket-level control is the '
            'lesson.',
            'Cloudflare Workers support HTTP-style networking through platform APIs; this example '
            'avoids outbound calls so the editable lesson stays deterministic and safe.'],
  'see_also': ['bytes-and-bytearray', 'subprocesses', 'async-await'],
  'cells': [{'kind': 'unsupported',
             'prose': ['`socketpair()` returns two connected endpoints. `sendall` writes encoded '
                       'bytes into one end, and `recv` reads up to 16 bytes off the other. The '
                       'byte boundary is the whole point: `"ping".encode("utf-8")` produces '
                       "`b'ping'`, which is what the socket actually moves. (The in-browser Run "
                       'button cannot open sockets — the sandbox disables outbound access — so '
                       'pressing Run on this page fails; the verified output below comes from a '
                       'real socket pair under standard CPython at build time.)'],
             'code': 'left, right = socket.socketpair()\n'
                     'left.sendall("ping".encode("utf-8"))\n'
                     'data = right.recv(16)',
             'output': ''},
            {'kind': 'cell',
             'prose': ['The complete version adds two things: a `try`/`finally` so both endpoints '
                       'close even if `recv` or the surrounding work raises, and a second `print` '
                       'that `decode`s the received bytes back into a Python `str` for display. '
                       "The first `print` shows the raw bytes `b'ping'`; the second shows the "
                       'decoded text `ping`.'],
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
             'output': "b'ping'\nping"}],
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
  'expected_output': "b'ping'\nping\n"},
 {'slug': 'datetime',
  'title': 'Dates and Times',
  'section': 'Standard Library',
  'summary': 'datetime represents dates, times, durations, formatting, and parsing.',
  'doc_path': '/library/datetime.html',
  'doc_url': 'https://docs.python.org/3.13/library/datetime.html',
  'explanation': ['The `datetime` module covers several related ideas: `date` for calendar days, '
                  '`time` for clock times, `datetime` for both together, and `timedelta` for '
                  'durations.',
                  'Timezone-aware datetimes avoid ambiguity in real systems. `timezone.utc` is a '
                  'clear default for examples because output stays stable and portable.',
                  'Use ISO formatting for interchange, `strftime()` for display, and parsing '
                  'helpers such as `fromisoformat()` to turn text back into datetime objects.'],
  'notes': ['Use timezone-aware datetimes for instants that cross system or user boundaries.',
            'Use `date` for calendar days, `time` for clock times, `datetime` for both, and '
            '`timedelta` for durations.',
            'Prefer ISO 8601 strings for interchange; use `strftime` for human-facing display.'],
  'see_also': ['string-formatting', 'json', 'number-parsing'],
  'cells': [{'kind': 'cell',
             'prose': ['The `datetime` module separates calendar dates, clock times, combined '
                       'datetimes, and durations. Import the types you need explicitly.',
                       'Use `date` for a calendar day and `time` for a time of day. Combine them '
                       'into a timezone-aware `datetime` when you mean an instant.',
                       '`isoformat()` produces stable machine-readable text. It is a good default '
                       'for examples, APIs, and logs.'],
             'code': 'from datetime import date, datetime, time, timedelta, timezone\n'
                     '\n'
                     'release_day = date(2026, 5, 4)\n'
                     'meeting_time = time(12, 30)\n'
                     'created_at = datetime.combine(release_day, meeting_time, '
                     'tzinfo=timezone.utc)\n'
                     '\n'
                     'print(release_day.isoformat())\n'
                     'print(meeting_time.isoformat())\n'
                     'print(created_at.isoformat())',
             'output': '2026-05-04\n12:30:00\n2026-05-04T12:30:00+00:00'},
            {'kind': 'cell',
             'prose': ['Use `timedelta` for durations. Adding one to a `datetime` produces another '
                       '`datetime` without manually changing calendar fields.'],
             'code': 'expires_at = created_at + timedelta(days=7, hours=2)\n'
                     'print(expires_at.isoformat())',
             'output': '2026-05-11T14:30:00+00:00'},
            {'kind': 'cell',
             'prose': ['Use `strftime()` for human-facing formatting and `fromisoformat()` when '
                       'reading ISO 8601 text back into a `datetime`.'],
             'code': 'print(created_at.strftime("%Y-%m-%d %H:%M %Z"))\n'
                     'iso_text = "2026-05-04T12:30:00+00:00"\n'
                     'parsed = datetime.fromisoformat(iso_text)\n'
                     'print(parsed == created_at)',
             'output': '2026-05-04 12:30 UTC\nTrue'}],
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
          'iso_text = "2026-05-04T12:30:00+00:00"\n'
          'parsed = datetime.fromisoformat(iso_text)\n'
          'print(parsed == created_at)\n',
  'expected_output': '2026-05-04\n'
                     '12:30:00\n'
                     '2026-05-04T12:30:00+00:00\n'
                     '2026-05-11T14:30:00+00:00\n'
                     '2026-05-04 12:30 UTC\n'
                     'True\n'},
 {'slug': 'csv-data',
  'title': 'CSV Data',
  'section': 'Standard Library',
  'summary': 'csv reads and writes row-shaped text data.',
  'doc_path': '/library/csv.html',
  'doc_url': 'https://docs.python.org/3.13/library/csv.html',
  'explanation': ['CSV is row-shaped text: each line is a record, and each comma-separated field '
                  'arrives as a string. The `csv` module understands quoting, delimiters, and '
                  'newlines, so it is safer than splitting lines by comma yourself.',
                  'Use `DictReader` when a header row names the columns. Convert fields explicitly '
                  'after reading, and use `DictWriter` when the program needs to produce the same '
                  'row shape again.',
                  'CSV is a good fit for flat tabular data. Use JSON or another structured format '
                  'when values are nested or when types need to survive the text boundary.'],
  'notes': ['Let `csv` handle quoting and delimiters instead of calling `split(",")`.',
            'CSV fields are text until your code converts them.',
            'Reach for JSON when records need nested lists, dictionaries, booleans, or numbers '
            'that preserve their type.'],
  'see_also': ['strings', 'dicts', 'json'],
  'cells': [{'kind': 'cell',
             'prose': ['`DictReader` uses the header row as dictionary keys. The values are still '
                       'strings because CSV is text.'],
             'code': 'import csv\n'
                     'import io\n'
                     '\n'
                     'text = "name,score\\nAda,98\\nGrace,95\\n"\n'
                     'rows = list(csv.DictReader(io.StringIO(text)))\n'
                     '\n'
                     'print(rows[0])\n'
                     'print(type(rows[0]["score"]).__name__)',
             'output': "{'name': 'Ada', 'score': '98'}\nstr"},
            {'kind': 'cell',
             'prose': ['Convert numeric fields at the boundary where the program leaves CSV text '
                       'and starts doing arithmetic.'],
             'code': 'print(sum(int(row["score"]) for row in rows))',
             'output': '193'},
            {'kind': 'cell',
             'prose': ['`DictWriter` turns dictionaries back into row-shaped text with the same '
                       'column order.'],
             'code': 'output = io.StringIO(newline="")\n'
                     'writer = csv.DictWriter(output, fieldnames=["name", "passed"])\n'
                     'writer.writeheader()\n'
                     'writer.writerow({"name": "Ada", "passed": True})\n'
                     '\n'
                     'print(output.getvalue().splitlines()[1])',
             'output': 'Ada,True'}],
  'code': 'import csv\n'
          'import io\n'
          '\n'
          'text = "name,score\\nAda,98\\nGrace,95\\n"\n'
          'rows = list(csv.DictReader(io.StringIO(text)))\n'
          'print(rows[0])\n'
          'print(sum(int(row["score"]) for row in rows))\n'
          '\n'
          'output = io.StringIO(newline="")\n'
          'writer = csv.DictWriter(output, fieldnames=["name", "passed"])\n'
          'writer.writeheader()\n'
          'writer.writerow({"name": "Ada", "passed": True})\n'
          'print(output.getvalue().splitlines()[1])\n',
  'expected_output': "{'name': 'Ada', 'score': '98'}\n193\nAda,True\n"},
 {'slug': 'async-await',
  'title': 'Async Await',
  'section': 'Async',
  'summary': 'async def creates coroutines, and await pauses until awaitable work completes.',
  'doc_path': '/library/asyncio-task.html',
  'doc_url': 'https://docs.python.org/3.13/library/asyncio-task.html',
  'explanation': ['`async def` creates a coroutine function. Calling it creates a coroutine '
                  'object; the body runs when an event loop awaits or schedules it.',
                  '`await` pauses the current coroutine until another awaitable completes. This '
                  'lets one event loop make progress on other work while a task waits for I/O.',
                  'Cloudflare Workers handlers are asynchronous, so understanding `await` is '
                  'practical for fetch calls, bindings, and service interactions even when a small '
                  'example uses `asyncio.sleep(0)` as a stand-in.',
                  'The alternative is ordinary `def` for work that completes immediately. Use '
                  'async code for I/O-shaped waiting, not as a faster replacement for CPU-bound '
                  'Python.'],
  'notes': ['Calling an async function creates a coroutine object.',
            '`await` yields control until an awaitable completes.',
            'Workers request handlers are async, so this pattern appears around fetches and '
            'bindings.',
            'Prefer ordinary functions when there is no awaitable work to coordinate.'],
  'see_also': ['async-iteration-and-context', 'functions', 'context-managers'],
  'cells': [{'kind': 'cell',
             'prose': ['An ordinary `def` function computes its result immediately: calling it '
                       'runs the body and hands the value straight back. This synchronous form is '
                       'the baseline the rest of the page contrasts against.'],
             'code': 'def slug_to_title(slug):\n'
                     '    return slug.replace("-", " ").title()\n'
                     '\n'
                     'print(slug_to_title("async-await"))',
             'output': 'Async Await'},
            {'kind': 'cell',
             'prose': ['An `async def` function returns a coroutine object when called. The '
                       'function body has not produced its final result yet.'],
             'code': 'import asyncio\n'
                     '\n'
                     'async def fetch_title(slug):\n'
                     '    await asyncio.sleep(0)\n'
                     '    return slug_to_title(slug)\n'
                     '\n'
                     'coroutine = fetch_title("async-await")\n'
                     'print(coroutine.__class__.__name__)\n'
                     'coroutine.close()',
             'output': 'coroutine'},
            {'kind': 'cell',
             'prose': ['Use `await` inside another coroutine to get the eventual result. '
                       '`asyncio.run()` starts an event loop for the top-level coroutine.'],
             'code': 'async def main():\n'
                     '    title = await fetch_title("async-await")\n'
                     '    print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': 'Async Await'},
            {'kind': 'cell',
             'prose': ['`asyncio.gather()` awaits several awaitables and returns their results in '
                       'order. This is the shape used when independent I/O operations can progress '
                       'together.'],
             'code': 'async def main():\n'
                     '    titles = await asyncio.gather(fetch_title("json"), '
                     'fetch_title("datetime"))\n'
                     '    print(titles)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': "['Json', 'Datetime']"},
            {'kind': 'cell',
             'prose': ['`async with` and `async for` are the asynchronous forms of context '
                       'managers and iteration. A class implements `__aenter__`/`__aexit__` to act '
                       'as an async context manager; an `async def` function with `yield` becomes '
                       'an async generator. The dedicated [async iteration and '
                       'context](/examples/async-iteration-and-context) page explains the '
                       'protocols in depth.'],
             'code': 'class Session:\n'
                     '    async def __aenter__(self):\n'
                     '        print("open")\n'
                     '        return self\n'
                     '\n'
                     '    async def __aexit__(self, *_):\n'
                     '        print("close")\n'
                     '        return False\n'
                     '\n'
                     '\n'
                     'async def stream():\n'
                     '    for slug in ["json", "datetime"]:\n'
                     '        await asyncio.sleep(0)\n'
                     '        yield slug\n'
                     '\n'
                     '\n'
                     'async def driver():\n'
                     '    async with Session():\n'
                     '        async for slug in stream():\n'
                     '            print(slug)\n'
                     '\n'
                     'asyncio.run(driver())',
             'output': 'open\njson\ndatetime\nclose'}],
  'code': 'import asyncio\n'
          '\n'
          'def slug_to_title(slug):\n'
          '    return slug.replace("-", " ").title()\n'
          '\n'
          'async def fetch_title(slug):\n'
          '    await asyncio.sleep(0)\n'
          '    return slug_to_title(slug)\n'
          '\n'
          'async def main():\n'
          '    title = await fetch_title("async-await")\n'
          '    print(title)\n'
          '    titles = await asyncio.gather(fetch_title("json"), fetch_title("datetime"))\n'
          '    print(titles)\n'
          '\n'
          'asyncio.run(main())\n'
          '\n'
          '\n'
          'class Session:\n'
          '    async def __aenter__(self):\n'
          '        print("open")\n'
          '        return self\n'
          '\n'
          '    async def __aexit__(self, *_):\n'
          '        print("close")\n'
          '        return False\n'
          '\n'
          '\n'
          'async def stream():\n'
          '    for slug in ["json", "datetime"]:\n'
          '        await asyncio.sleep(0)\n'
          '        yield slug\n'
          '\n'
          '\n'
          'async def driver():\n'
          '    async with Session():\n'
          '        async for slug in stream():\n'
          '            print(slug)\n'
          '\n'
          'asyncio.run(driver())\n',
  'expected_output': "Async Await\n['Json', 'Datetime']\nopen\njson\ndatetime\nclose\n"},
 {'slug': 'async-iteration-and-context',
  'title': 'Async Iteration and Context',
  'section': 'Async',
  'summary': 'async for and async with consume asynchronous streams and cleanup protocols.',
  'doc_path': '/reference/compound_stmts.html#async-for',
  'doc_url': 'https://docs.python.org/3.13/reference/compound_stmts.html#async-for',
  'explanation': ['`async for` consumes an asynchronous iterator: a stream whose next value may '
                  'require `await`. `async with` surrounds a block with asynchronous setup and '
                  'cleanup.',
                  'These forms appear around network streams, database cursors, locks, and service '
                  'clients where both iteration and cleanup may wait on I/O.',
                  'Use ordinary `for` and `with` when producing the next value or cleaning up does '
                  'not need to await anything.',
                  'The syntax mirrors `for` and `with`, but the protocol methods are '
                  'asynchronous.'],
  'notes': ['`async for` consumes asynchronous iterators.',
            '`async with` awaits asynchronous setup and cleanup.',
            'These forms are common around I/O-shaped resources.'],
  'see_also': ['async-await', 'iterators', 'context-managers'],
  'cells': [{'kind': 'cell',
             'prose': ['An async generator can `await` before yielding each value. `async for` '
                       'consumes those values with the asynchronous iteration protocol.'],
             'code': 'import asyncio\n'
                     '\n'
                     'async def titles():\n'
                     '    for slug in ["values", "async-await"]:\n'
                     '        await asyncio.sleep(0)\n'
                     '        yield slug.replace("-", " ").title()\n'
                     '\n'
                     'print(titles.__name__)',
             'output': 'titles'},
            {'kind': 'cell',
             'prose': ['An async context manager defines `__aenter__` and `__aexit__`. `async '
                       'with` awaits setup and cleanup around the block.'],
             'code': 'class Session:\n'
                     '    async def __aenter__(self):\n'
                     '        print("open")\n'
                     '        return self\n'
                     '\n'
                     '    async def __aexit__(self, exc_type, exc, tb):\n'
                     '        print("close")\n'
                     '\n'
                     'print(Session.__name__)',
             'output': 'Session'},
            {'kind': 'cell',
             'prose': ['The top-level coroutine combines both protocols: open the async resource, '
                       'then consume the async stream inside it.'],
             'code': 'async def main():\n'
                     '    async with Session():\n'
                     '        async for title in titles():\n'
                     '            print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': 'open\nValues\nAsync Await\nclose'}],
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
  'expected_output': 'open\nValues\nAsync Await\nclose\n'}]
