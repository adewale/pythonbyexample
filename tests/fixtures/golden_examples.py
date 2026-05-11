"""Versioned example catalog for Python By Example.

This fixture freezes the reviewed public catalog for migration/parity checks.
Update it intentionally after example rewrites have passed verification.
"""

PYTHON_VERSION = '3.13'
REFERENCE_URL = 'https://docs.python.org/3.13/'

EXAMPLES = [{'cells': [{'code': 'print("hello world")',
             'kind': 'cell',
             'line': 17,
             'output': 'hello world',
             'prose': ['Every Python program starts by executing statements from top to bottom. '
                       'Calling `print()` is the smallest useful program because it shows how '
                       'Python evaluates an expression and sends text to standard output.']}],
  'code': 'print("hello world")\n',
  'doc_path': '/tutorial/introduction.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/introduction.html',
  'expected_output': 'hello world\n',
  'explanation': ['Every Python program starts by executing statements from top to bottom. Calling '
                  '`print()` is the smallest useful program because it shows how Python evaluates '
                  'an expression and sends text to standard output.',
                  'Strings are ordinary values, so the message passed to `print()` can be changed, '
                  'stored in a variable, or produced by a function. This example keeps the first '
                  'program intentionally small.',
                  '`print()` writes text followed by a newline. Strings can be delimited with '
                  'single or double quotes.'],
  'min_python': None,
  'notes': ['`print()` writes text followed by a newline.',
            'Strings can be delimited with single or double quotes.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'hello-world',
  'summary': 'The first Python program prints a line of text.',
  'title': 'Hello World',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'print("hello world")',
                   'prose': 'Every Python program starts by executing statements from top to '
                            'bottom. Calling `print()` is the smallest useful program because it '
                            'shows how Python evaluates an expression and sends text to standard '
                            'output.'}]},
 {'cells': [{'code': 'text = "python"\n'
                     'count = 3\n'
                     'ratio = 2.5\n'
                     'ready = True\n'
                     'missing = None\n'
                     '\n'
                     'print(type(text).__name__)',
             'kind': 'cell',
             'line': 17,
             'output': 'str',
             'prose': ['Start with several built-in values. Python does not require declarations '
                       'before binding these names, and each value is still an object with a '
                       'type.']},
            {'code': 'print(text.upper())\nprint(count + 4)\nprint(ratio * 2)',
             'kind': 'cell',
             'line': 35,
             'output': 'PYTHON\n7\n5.0',
             'prose': ['Methods and operators evaluate to new values. The original `text`, '
                       '`count`, and `ratio` bindings remain ordinary objects you can reuse.']},
            {'code': 'print(ready and count > 0)\nprint(missing is None)',
             'kind': 'cell',
             'line': 51,
             'output': 'True\nTrue',
             'prose': ['Boolean expressions combine facts, and `None` is checked by identity '
                       'because it is a singleton absence marker.']}],
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
  'doc_path': '/library/stdtypes.html',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html',
  'expected_output': 'str\nPYTHON\n7\n5.0\nTrue\nTrue\n',
  'explanation': ['A Python program works by evaluating expressions into values. Values are '
                  'objects: text, integers, floats, booleans, `None`, and many richer types '
                  'introduced later.',
                  'Names point to values; they are not declarations that permanently fix a type. '
                  'Operations usually produce new values, which you can print, store, compare, or '
                  'pass to functions.',
                  'This page is a map, not the whole territory. Later pages explain the '
                  'boundaries: equality vs identity, mutable vs immutable values, truthiness vs '
                  'literal booleans, and `None` vs a missing key or an exception.'],
  'min_python': None,
  'notes': ['Values are objects; names point to them and operations usually create new values.',
            'Use `is None` for the absence marker, not `== None`.',
            'This overview introduces boundaries that later pages explain in detail.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'values',
  'summary': 'Python programs evaluate expressions into objects such as text, numbers, booleans, '
             'and None.',
  'title': 'Values',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'text = "python"\n'
                           'count = 3\n'
                           'ratio = 2.5\n'
                           'ready = True\n'
                           'missing = None\n'
                           '\n'
                           'print(type(text).__name__)',
                   'prose': 'Start with several built-in values. Python does not require '
                            'declarations before binding these names, and each value is still an '
                            'object with a type.'},
                  {'code': 'print(text.upper())\nprint(count + 4)\nprint(ratio * 2)',
                   'prose': 'Methods and operators evaluate to new values. The original `text`, '
                            '`count`, and `ratio` bindings remain ordinary objects you can reuse.'},
                  {'code': 'print(ready and count > 0)\nprint(missing is None)',
                   'prose': 'Boolean expressions combine facts, and `None` is checked by identity '
                            'because it is a singleton absence marker.'}]},
 {'cells': [{'code': 'whole = 42\n'
                     'fraction = 3.5\n'
                     'complex_number = 2 + 3j\n'
                     'print(whole, fraction, complex_number.imag)',
             'kind': 'cell',
             'line': 23,
             'output': '42 3.5 3.0',
             'prose': ['Numeric literals write numbers directly. Complex literals use `j` for the '
                       'imaginary part.']},
            {'code': 'flags = 0xFF\n'
                     'mask = 0b1010\n'
                     'million = 1_000_000\n'
                     'print(flags, mask, million)',
             'kind': 'cell',
             'line': 38,
             'output': '255 10 1000000',
             'prose': ['Integer literals also accept hexadecimal (`0x`), binary (`0b`), and octal '
                       '(`0o`) prefixes. Underscores group digits visually without changing the '
                       'value.']},
            {'code': 'text = "python"\n'
                     'raw_pattern = r"\\d+"\n'
                     'data = b"py"\n'
                     'score = 98\n'
                     'formatted = f"score={score}"\n'
                     'print(text)\n'
                     'print(raw_pattern)\n'
                     'print(data)\n'
                     'print(formatted)',
             'kind': 'cell',
             'line': 53,
             'output': "python\n\\d+\nb'py'\nscore=98",
             'prose': ['String literals write Unicode text. Raw strings keep backslashes literal, '
                       'bytes literals write binary data rather than text, and f-strings '
                       '(`f"..."`) embed expressions inline.']},
            {'code': 'point = (2, 3)\n'
                     'names = ["Ada", "Grace"]\n'
                     'scores = {"Ada": 98}\n'
                     'unique = {"py", "go"}\n'
                     'print(point)\n'
                     'print(names[0])\n'
                     'print(scores["Ada"])\n'
                     'print(sorted(unique))',
             'kind': 'cell',
             'line': 76,
             'output': "(2, 3)\nAda\n98\n['go', 'py']",
             'prose': ['Container literals create tuples, lists, dictionaries, and sets. Each '
                       'container answers a different question about order, position, lookup, or '
                       'uniqueness.']},
            {'code': 'print(True, False, None)\nprint(...)',
             'kind': 'cell',
             'line': 98,
             'output': 'True False None\nEllipsis',
             'prose': ['`True`, `False`, `None`, and `...` are singleton literal-like constants '
                       'used for truth values, absence, and placeholders.']},
            {'code': 'print(type({}).__name__)\n'
                     'print(type(set()).__name__)\n'
                     'print(type({1, 2}).__name__)',
             'kind': 'cell',
             'line': 112,
             'output': 'dict\nset\nset',
             'prose': ['Curly-brace literals are dictionaries by default. The empty form `{}` is '
                       'an empty dictionary, not an empty set; use `set()` for that. A non-empty '
                       '`{1, 2}` is a set because keyless items can only be a set.']}],
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
  'doc_path': '/reference/lexical_analysis.html#literals',
  'doc_url': 'https://docs.python.org/3.13/reference/lexical_analysis.html#literals',
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
                     'set\n',
  'explanation': ['Literals are source-code forms for values: numbers, text, bytes, containers, '
                  'booleans, `None`, and a few specialized markers. They are how a program writes '
                  'small values directly.',
                  'The literal form is only the beginning. Later examples explain each value '
                  'family in depth: strings are Unicode text, bytes are binary data, lists and '
                  'dicts are containers, and `None` represents intentional absence.',
                  'Use literals when the value is small and local. Give repeated or meaningful '
                  'values a name so the program explains why that value matters.'],
  'min_python': None,
  'notes': ['Literals are good for small local values; constants are better for repeated values '
            'with meaning.',
            '`{}` is an empty dictionary. Use `set()` for an empty set.',
            'Bytes literals are binary data; string literals are Unicode text.',
            '`...` evaluates to the `Ellipsis` object.'],
  'section': 'Basics',
  'see_also': ['values', 'strings', 'numbers', 'string-formatting'],
  'slug': 'literals',
  'summary': 'Literals write values directly in Python source code.',
  'title': 'Literals',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'whole = 42\n'
                           'fraction = 3.5\n'
                           'complex_number = 2 + 3j\n'
                           'print(whole, fraction, complex_number.imag)',
                   'prose': 'Numeric literals write numbers directly. Complex literals use `j` for '
                            'the imaginary part.'},
                  {'code': 'flags = 0xFF\n'
                           'mask = 0b1010\n'
                           'million = 1_000_000\n'
                           'print(flags, mask, million)',
                   'prose': 'Integer literals also accept hexadecimal (`0x`), binary (`0b`), and '
                            'octal (`0o`) prefixes. Underscores group digits visually without '
                            'changing the value.'},
                  {'code': 'text = "python"\n'
                           'raw_pattern = r"\\d+"\n'
                           'data = b"py"\n'
                           'score = 98\n'
                           'formatted = f"score={score}"\n'
                           'print(text)\n'
                           'print(raw_pattern)\n'
                           'print(data)\n'
                           'print(formatted)',
                   'prose': 'String literals write Unicode text. Raw strings keep backslashes '
                            'literal, bytes literals write binary data rather than text, and '
                            'f-strings (`f"..."`) embed expressions inline.'},
                  {'code': 'point = (2, 3)\n'
                           'names = ["Ada", "Grace"]\n'
                           'scores = {"Ada": 98}\n'
                           'unique = {"py", "go"}\n'
                           'print(point)\n'
                           'print(names[0])\n'
                           'print(scores["Ada"])\n'
                           'print(sorted(unique))',
                   'prose': 'Container literals create tuples, lists, dictionaries, and sets. Each '
                            'container answers a different question about order, position, lookup, '
                            'or uniqueness.'},
                  {'code': 'print(True, False, None)\nprint(...)',
                   'prose': '`True`, `False`, `None`, and `...` are singleton literal-like '
                            'constants used for truth values, absence, and placeholders.'},
                  {'code': 'print(type({}).__name__)\n'
                           'print(type(set()).__name__)\n'
                           'print(type({1, 2}).__name__)',
                   'prose': 'Curly-brace literals are dictionaries by default. The empty form `{}` '
                            'is an empty dictionary, not an empty set; use `set()` for that. A '
                            'non-empty `{1, 2}` is a set because keyless items can only be a '
                            'set.'}]},
 {'cells': [{'code': 'count = 10\n'
                     'ratio = 0.25\n'
                     '\n'
                     'print(count + 5)\n'
                     'print(count / 4)\n'
                     'print(ratio * 2)',
             'kind': 'cell',
             'line': 21,
             'output': '15\n2.5\n0.5',
             'prose': ['Python has `int` for whole numbers and `float` for approximate real-valued '
                       'arithmetic. True division with `/` returns a `float`, even when both '
                       'inputs are integers.']},
            {'code': 'print(count // 4)\nprint(count % 4)\nprint(2 ** 5)',
             'kind': 'cell',
             'line': 40,
             'output': '2\n2\n32',
             'prose': ['Floor division and modulo are useful when you need quotient and remainder '
                       'behavior. Powers use `**`, not `^`.']},
            {'code': 'z = 2 + 3j\nprint(z.real, z.imag)',
             'kind': 'cell',
             'line': 56,
             'output': '2.0 3.0',
             'prose': ['Complex numbers are built in. The literal suffix `j` marks the imaginary '
                       'part.']},
            {'code': 'import math\n'
                     '\n'
                     'print(0.1 + 0.2)\n'
                     'print(0.1 + 0.2 == 0.3)\n'
                     'print(math.isclose(0.1 + 0.2, 0.3))\n'
                     'print(round(3.14159, 2))',
             'kind': 'cell',
             'line': 69,
             'output': '0.30000000000000004\nFalse\nTrue\n3.14',
             'prose': ['Floating-point values are approximate, so `==` between expected and '
                       'computed floats is rarely the right test. Compare with `math.isclose` (or '
                       'work in `decimal.Decimal`) when the question is "are these the same number '
                       'to within tolerance".']}],
  'code': 'import math\n'
          '\n'
          'count = 10\n'
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
          'print(0.1 + 0.2 == 0.3)\n'
          'print(math.isclose(0.1 + 0.2, 0.3))\n'
          'print(round(3.14159, 2))\n',
  'doc_path': '/library/stdtypes.html#numeric-types-int-float-complex',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#numeric-types-int-float-complex',
  'expected_output': '15\n2.5\n2\n2\n32\n2.0 3.0\n0.30000000000000004\nFalse\nTrue\n3.14\n',
  'explanation': ["Python's numeric model starts with `int`, `float`, and `complex`. Integers are "
                  'arbitrary precision, floats are approximate double-precision values, and '
                  'complex numbers carry real and imaginary parts.',
                  'Operators encode different numeric questions. `/` means true division and '
                  'returns a float, `//` means floor division, `%` gives the remainder, and `**` '
                  'computes powers.',
                  'Use rounding for display, not as a substitute for understanding floating-point '
                  'approximation. Financial code usually needs `decimal.Decimal`, which is a '
                  'separate precision topic.'],
  'min_python': None,
  'notes': ["Python's `int` has arbitrary precision; it grows as large as memory allows.",
            "Python's `float` is approximate double-precision floating point.",
            'Use `/` for true division and `//` for floor division.',
            'Use `math.isclose` instead of `==` for floating-point comparison; reach for '
            '`decimal.Decimal` when exact decimal precision is the domain requirement.'],
  'section': 'Basics',
  'see_also': ['literals', 'operators'],
  'slug': 'numbers',
  'summary': 'Python numbers include integers, floats, and complex values.',
  'title': 'Numbers',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'count = 10\n'
                           'ratio = 0.25\n'
                           '\n'
                           'print(count + 5)\n'
                           'print(count / 4)\n'
                           'print(ratio * 2)',
                   'prose': 'Python has `int` for whole numbers and `float` for approximate '
                            'real-valued arithmetic. True division with `/` returns a `float`, '
                            'even when both inputs are integers.'},
                  {'code': 'print(count // 4)\nprint(count % 4)\nprint(2 ** 5)',
                   'prose': 'Floor division and modulo are useful when you need quotient and '
                            'remainder behavior. Powers use `**`, not `^`.'},
                  {'code': 'z = 2 + 3j\nprint(z.real, z.imag)',
                   'prose': 'Complex numbers are built in. The literal suffix `j` marks the '
                            'imaginary part.'},
                  {'code': 'import math\n'
                           '\n'
                           'print(0.1 + 0.2)\n'
                           'print(0.1 + 0.2 == 0.3)\n'
                           'print(math.isclose(0.1 + 0.2, 0.3))\n'
                           'print(round(3.14159, 2))',
                   'prose': 'Floating-point values are approximate, so `==` between expected and '
                            'computed floats is rarely the right test. Compare with `math.isclose` '
                            '(or work in `decimal.Decimal`) when the question is "are these the '
                            'same number to within tolerance".'}]},
 {'cells': [{'code': 'logged_in = True\n'
                     'has_permission = False\n'
                     '\n'
                     'print(logged_in and has_permission)\n'
                     'print(logged_in or has_permission)\n'
                     'print(not has_permission)',
             'kind': 'cell',
             'line': 17,
             'output': 'False\nTrue\nTrue',
             'prose': ['Use booleans for facts that are either true or false. Python spells the '
                       'constants `True` and `False`.',
                       'Use `and`, `or`, and `not` to combine truth values. These operators read '
                       'like English and short-circuit when possible.']},
            {'code': 'name = "Ada"\nprint(name == "Ada" and len(name) > 0)',
             'kind': 'cell',
             'line': 38,
             'output': 'True',
             'prose': ['Comparisons produce booleans too, so they compose naturally with logical '
                       'operators in conditions and validation checks.']},
            {'code': 'print(isinstance(True, int))\n'
                     'print(True + True)\n'
                     'print(sum([True, True, False, True]))\n'
                     '\n'
                     'def is_strict_int(value):\n'
                     '    return isinstance(value, int) and not isinstance(value, bool)\n'
                     '\n'
                     'print(is_strict_int(True))\n'
                     'print(is_strict_int(1))',
             'kind': 'cell',
             'line': 51,
             'output': 'True\n2\n3\nFalse\nTrue',
             'prose': ['`bool` is a subclass of `int`, which is occasionally a footgun. `True` '
                       'behaves as `1` and `False` as `0` in arithmetic, and `isinstance(True, '
                       'int)` is `True`. When a function must reject booleans, exclude them '
                       'explicitly with `isinstance(value, int) and not isinstance(value, '
                       'bool)`.']}],
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
  'doc_path': '/library/stdtypes.html#boolean-type-bool',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#boolean-type-bool',
  'expected_output': 'False\nTrue\nTrue\nTrue\nTrue\n2\n3\nFalse\nTrue\n',
  'explanation': ['Booleans are the values `True` and `False`. They are produced by comparisons '
                  'and combined with `and`, `or`, and `not`.',
                  "Python's logical operators short-circuit. That means the right side is "
                  'evaluated only when needed, which keeps guard checks efficient and safe.',
                  'Booleans are also connected to truthiness: many objects can be tested in '
                  'conditions even when they are not literally `True` or `False`.'],
  'min_python': None,
  'notes': ['Boolean constants are `True` and `False`, with capital letters.',
            '`and` and `or` short-circuit: Python does not evaluate the right side if the left '
            'side already determines the result.',
            'Prefer truthiness for containers and explicit comparisons when the exact boolean '
            'condition matters.',
            '`bool` subclasses `int`; `isinstance(True, int)` is `True`. Exclude booleans '
            'explicitly when only "real" integers should pass.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'booleans',
  'summary': 'Booleans represent truth values and combine with logical operators.',
  'title': 'Booleans',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'logged_in = True\n'
                           'has_permission = False\n'
                           '\n'
                           'print(logged_in and has_permission)\n'
                           'print(logged_in or has_permission)\n'
                           'print(not has_permission)',
                   'prose': 'Use booleans for facts that are either true or false. Python spells '
                            'the constants `True` and `False`.'},
                  {'code': 'logged_in = True\n'
                           'has_permission = False\n'
                           '\n'
                           'print(logged_in and has_permission)\n'
                           'print(logged_in or has_permission)\n'
                           'print(not has_permission)',
                   'prose': 'Use `and`, `or`, and `not` to combine truth values. These operators '
                            'read like English and short-circuit when possible.'},
                  {'code': 'name = "Ada"\nprint(name == "Ada" and len(name) > 0)',
                   'prose': 'Comparisons produce booleans too, so they compose naturally with '
                            'logical operators in conditions and validation checks.'},
                  {'code': 'print(isinstance(True, int))\n'
                           'print(True + True)\n'
                           'print(sum([True, True, False, True]))\n'
                           '\n'
                           'def is_strict_int(value):\n'
                           '    return isinstance(value, int) and not isinstance(value, bool)\n'
                           '\n'
                           'print(is_strict_int(True))\n'
                           'print(is_strict_int(1))',
                   'prose': '`bool` is a subclass of `int`, which is occasionally a footgun. '
                            '`True` behaves as `1` and `False` as `0` in arithmetic, and '
                            '`isinstance(True, int)` is `True`. When a function must reject '
                            'booleans, exclude them explicitly with `isinstance(value, int) and '
                            'not isinstance(value, bool)`.'}]},
 {'cells': [{'code': 'count = 10\n'
                     'print(count + 5)\n'
                     'print(count // 4)\n'
                     'print(count % 4)\n'
                     'print(2 ** 5)',
             'kind': 'cell',
             'line': 23,
             'output': '15\n2\n2\n32',
             'prose': ['Arithmetic operators compute new values. Use `//` for floor division, `%` '
                       'for remainder, and `**` for powers.']},
            {'code': 'score = 91\n'
                     'print(80 <= score < 100)\n'
                     'print(score == 100 or score >= 90)\n'
                     'print("py" in "python")',
             'kind': 'cell',
             'line': 42,
             'output': 'True\nTrue\nTrue',
             'prose': ['Comparison operators produce booleans. Python comparisons can chain, which '
                       'keeps range checks readable.']},
            {'code': 'flags = 0b0011\n'
                     'print(flags & 0b0101)\n'
                     'print(flags | 0b0100)\n'
                     'print(flags ^ 0b0101)\n'
                     'print(flags << 1)',
             'kind': 'cell',
             'line': 59,
             'output': '1\n7\n6\n6',
             'prose': ['Bitwise operators work on integer bit patterns. They are useful for masks '
                       'and flags, not ordinary boolean logic. `&` is bitwise AND, `|` is bitwise '
                       'OR, `^` is exclusive OR, and `<<` shifts left.']},
            {'code': 'class Scale:\n'
                     '    def __init__(self, value):\n'
                     '        self.value = value\n'
                     '\n'
                     '    def __matmul__(self, other):\n'
                     '        return self.value * other.value\n'
                     '\n'
                     'print(Scale(2) @ Scale(3))',
             'kind': 'cell',
             'line': 78,
             'output': '6',
             'prose': ['The `@` operator is reserved for matrix-like multiplication and custom '
                       'types that define `__matmul__`.']},
            {'code': 'items = ["a", "b"]\nif (size := len(items)) > 0:\n    print(size)',
             'kind': 'cell',
             'line': 97,
             'output': '2',
             'prose': ['The walrus operator `:=` assigns inside an expression. Use it when naming '
                       'a value avoids repeating work in a condition.']},
            {'code': 'def loud():\n'
                     '    print("ran")\n'
                     '    return True\n'
                     '\n'
                     'print(False and loud())\n'
                     'print(True or loud())\n'
                     'print(True and loud())',
             'kind': 'cell',
             'line': 111,
             'output': 'False\nTrue\nran\nTrue',
             'prose': ['`and` and `or` short-circuit: the right side runs only when the left side '
                       'cannot already determine the result. That makes them safe for guard '
                       'expressions like `obj and obj.value` where the right side would fail on '
                       '`None`.']}],
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
          '    print(size)\n',
  'doc_path': '/reference/expressions.html#operator-precedence',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#operator-precedence',
  'expected_output': '15\n2\n2\n32\nTrue\nTrue\nTrue\n1\n7\n6\n6\n6\n2\n',
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
  'min_python': None,
  'notes': ['Use the clearest operator for the question: arithmetic, comparison, boolean logic, '
            'membership, identity, or bitwise manipulation.',
            '`and` and `or` short-circuit, so the right side may not run.',
            'Operators have precedence; use parentheses when grouping would otherwise be hard to '
            'read.',
            'Custom operator behavior should make an object feel more natural, not more clever.'],
  'section': 'Basics',
  'see_also': ['numbers',
               'equality-and-identity',
               'assignment-expressions',
               'operator-overloading'],
  'slug': 'operators',
  'summary': 'Operators combine, compare, and test values in expressions.',
  'title': 'Operators',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'count = 10\n'
                           'print(count + 5)\n'
                           'print(count // 4)\n'
                           'print(count % 4)\n'
                           'print(2 ** 5)',
                   'prose': 'Arithmetic operators compute new values. Use `//` for floor division, '
                            '`%` for remainder, and `**` for powers.'},
                  {'code': 'score = 91\n'
                           'print(80 <= score < 100)\n'
                           'print(score == 100 or score >= 90)\n'
                           'print("py" in "python")',
                   'prose': 'Comparison operators produce booleans. Python comparisons can chain, '
                            'which keeps range checks readable.'},
                  {'code': 'flags = 0b0011\n'
                           'print(flags & 0b0101)\n'
                           'print(flags | 0b0100)\n'
                           'print(flags ^ 0b0101)\n'
                           'print(flags << 1)',
                   'prose': 'Bitwise operators work on integer bit patterns. They are useful for '
                            'masks and flags, not ordinary boolean logic. `&` is bitwise AND, `|` '
                            'is bitwise OR, `^` is exclusive OR, and `<<` shifts left.'},
                  {'code': 'class Scale:\n'
                           '    def __init__(self, value):\n'
                           '        self.value = value\n'
                           '\n'
                           '    def __matmul__(self, other):\n'
                           '        return self.value * other.value\n'
                           '\n'
                           'print(Scale(2) @ Scale(3))',
                   'prose': 'The `@` operator is reserved for matrix-like multiplication and '
                            'custom types that define `__matmul__`.'},
                  {'code': 'items = ["a", "b"]\nif (size := len(items)) > 0:\n    print(size)',
                   'prose': 'The walrus operator `:=` assigns inside an expression. Use it when '
                            'naming a value avoids repeating work in a condition.'},
                  {'code': 'def loud():\n'
                           '    print("ran")\n'
                           '    return True\n'
                           '\n'
                           'print(False and loud())\n'
                           'print(True or loud())\n'
                           'print(True and loud())',
                   'prose': '`and` and `or` short-circuit: the right side runs only when the left '
                            'side cannot already determine the result. That makes them safe for '
                            'guard expressions like `obj and obj.value` where the right side would '
                            'fail on `None`.'}]},
 {'cells': [{'code': 'result = None\nprint(result is None)',
             'kind': 'cell',
             'line': 17,
             'output': 'True',
             'prose': ["`None` is Python's value for “nothing here.” Check it with `is None` "
                       'because it is a singleton identity value.']},
            {'code': 'def find_score(name):\n'
                     '    if name == "Ada":\n'
                     '        return 10\n'
                     '    return None\n'
                     '\n'
                     'score = find_score("Grace")\n'
                     'print(score is None)',
             'kind': 'cell',
             'line': 30,
             'output': 'True',
             'prose': ['Functions often return `None` when absence is expected and callers can '
                       'continue. The function name and surrounding code should make that '
                       'possibility clear.']},
            {'code': 'profile = {"name": "Ada"}\n'
                     'print(profile.get("timezone", "UTC"))\n'
                     '\n'
                     'try:\n'
                     '    int("python")\n'
                     'except ValueError:\n'
                     '    print("invalid number")',
             'kind': 'cell',
             'line': 48,
             'output': 'UTC\ninvalid number',
             'prose': ['A missing dictionary key is another absence boundary. Use `get()` when the '
                       'mapping can supply a default, and use exceptions for invalid operations '
                       'that cannot produce a value.']}],
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
  'doc_path': '/library/constants.html#None',
  'doc_url': 'https://docs.python.org/3.13/library/constants.html#None',
  'expected_output': 'True\nTrue\nUTC\ninvalid number\n',
  'explanation': ['`None` represents the absence of a value. It is the usual sentinel when a '
                  'function has no result to return but the absence itself is meaningful.',
                  'Because `None` is a singleton, idiomatic Python checks it with `is None` or `is '
                  'not None`. This avoids confusing identity with value equality.',
                  'Absence has several nearby shapes in Python. A function can return `None`, a '
                  'dictionary lookup can supply a default for a missing key, and an invalid '
                  'operation can raise an exception.'],
  'min_python': None,
  'notes': ['Use `is None` rather than `== None`; `None` is a singleton identity value.',
            'Use `None` for expected absence that callers can test.',
            'Use dictionary defaults for missing mapping keys and exceptions for invalid '
            'operations.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'none',
  'summary': 'None represents expected absence, distinct from missing keys and errors.',
  'title': 'None',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'result = None\nprint(result is None)',
                   'prose': "`None` is Python's value for “nothing here.” Check it with `is None` "
                            'because it is a singleton identity value.'},
                  {'code': 'def find_score(name):\n'
                           '    if name == "Ada":\n'
                           '        return 10\n'
                           '    return None\n'
                           '\n'
                           'score = find_score("Grace")\n'
                           'print(score is None)',
                   'prose': 'Functions often return `None` when absence is expected and callers '
                            'can continue. The function name and surrounding code should make that '
                            'possibility clear.'},
                  {'code': 'profile = {"name": "Ada"}\n'
                           'print(profile.get("timezone", "UTC"))\n'
                           '\n'
                           'try:\n'
                           '    int("python")\n'
                           'except ValueError:\n'
                           '    print("invalid number")',
                   'prose': 'A missing dictionary key is another absence boundary. Use `get()` '
                            'when the mapping can supply a default, and use exceptions for invalid '
                            'operations that cannot produce a value.'}]},
 {'cells': [{'code': 'message = "hi"\nprint(message)',
             'kind': 'cell',
             'line': 19,
             'output': 'hi',
             'prose': ['Assignment binds a name to a value. Once bound, the name can be used '
                       'anywhere that value is needed.']},
            {'code': 'message = "hello"\nprint(message)',
             'kind': 'cell',
             'line': 32,
             'output': 'hello',
             'prose': ['Assignment can rebind the same name to a different value. The name is not '
                       'permanently attached to the first object.']},
            {'code': 'count = 3\ncount += 1\nprint(count)',
             'kind': 'cell',
             'line': 45,
             'output': '4',
             'prose': ['Augmented assignment reads the current binding, computes an updated value, '
                       'and stores the result back under the same name.']}],
  'code': 'message = "hi"\n'
          'print(message)\n'
          '\n'
          'message = "hello"\n'
          'print(message)\n'
          '\n'
          'count = 3\n'
          'count += 1\n'
          'print(count)\n',
  'doc_path': '/reference/simple_stmts.html#assignment-statements',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#assignment-statements',
  'expected_output': 'hi\nhello\n4\n',
  'explanation': ['Python variables are names bound to objects. Assignment creates or rebinds a '
                  'name; it does not require a declaration and it does not permanently attach a '
                  'type to the name.',
                  'Rebinding changes which object a name refers to. Augmented assignment such as '
                  '`+=` is the idiomatic way to update counters and accumulators.',
                  "Use clear names for values that matter later. Python's flexibility makes naming "
                  'more important, not less.',
                  'Use assignment when a value needs a name for reuse or explanation. Prefer a '
                  'direct expression when naming the intermediate value would add noise.'],
  'min_python': None,
  'notes': ['Python variables are names bound to objects, not boxes with fixed types.',
            'Rebinding a name is normal.',
            'Use augmented assignment for counters and accumulators.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'variables',
  'summary': 'Names are bound to values with assignment.',
  'title': 'Variables',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'message = "hi"\nprint(message)',
                   'prose': 'Assignment binds a name to a value. Once bound, the name can be used '
                            'anywhere that value is needed.'},
                  {'code': 'message = "hello"\nprint(message)',
                   'prose': 'Assignment can rebind the same name to a different value. The name is '
                            'not permanently attached to the first object.'},
                  {'code': 'count = 3\ncount += 1\nprint(count)',
                   'prose': 'Augmented assignment reads the current binding, computes an updated '
                            'value, and stores the result back under the same name.'}]},
 {'cells': [{'code': 'MAX_RETRIES = 3\n'
                     'API_VERSION = "2026-05"\n'
                     '\n'
                     'for attempt in range(1, MAX_RETRIES + 1):\n'
                     '    print(f"attempt {attempt} of {MAX_RETRIES}")',
             'kind': 'cell',
             'line': 17,
             'output': 'attempt 1 of 3\nattempt 2 of 3\nattempt 3 of 3',
             'prose': ['Python does not have a `const` declaration like Go or Rust. Instead, '
                       'modules use all-caps names for values callers should treat as fixed.',
                       'The interpreter will still let you rebind the name, but the convention is '
                       'strong enough that readers understand the design intent.']},
            {'code': 'print(API_VERSION)',
             'kind': 'cell',
             'line': 37,
             'output': '2026-05',
             'prose': ['Constants are useful for configuration values that should be named once '
                       'and reused instead of repeated as magic literals.']}],
  'code': 'MAX_RETRIES = 3\n'
          'API_VERSION = "2026-05"\n'
          '\n'
          'for attempt in range(1, MAX_RETRIES + 1):\n'
          '    print(f"attempt {attempt} of {MAX_RETRIES}")\n'
          '\n'
          'print(API_VERSION)\n',
  'doc_path': '/tutorial/classes.html#python-scopes-and-namespaces',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#python-scopes-and-namespaces',
  'expected_output': 'attempt 1 of 3\nattempt 2 of 3\nattempt 3 of 3\n2026-05\n',
  'explanation': ['Python has no `const` keyword for ordinary variables. Instead, modules use '
                  'all-caps names to mark values that should be treated as constants by '
                  'convention.',
                  'The interpreter will not stop rebinding, but the convention is important API '
                  'communication. Readers understand that `MAX_RETRIES` is configuration, not loop '
                  'state.',
                  'Named constants remove magic values from code and give repeated literals one '
                  'place to change.'],
  'min_python': None,
  'notes': ['Python has no `const` keyword for ordinary names.',
            'All-caps names such as `MAX_RETRIES` communicate that a value is intended to stay '
            'fixed.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'constants',
  'summary': 'Python uses naming conventions for values that should not change.',
  'title': 'Constants',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'MAX_RETRIES = 3\n'
                           'API_VERSION = "2026-05"\n'
                           '\n'
                           'for attempt in range(1, MAX_RETRIES + 1):\n'
                           '    print(f"attempt {attempt} of {MAX_RETRIES}")',
                   'prose': 'Python does not have a `const` declaration like Go or Rust. Instead, '
                            'modules use all-caps names for values callers should treat as fixed.'},
                  {'code': 'MAX_RETRIES = 3\n'
                           'API_VERSION = "2026-05"\n'
                           '\n'
                           'for attempt in range(1, MAX_RETRIES + 1):\n'
                           '    print(f"attempt {attempt} of {MAX_RETRIES}")',
                   'prose': 'The interpreter will still let you rebind the name, but the '
                            'convention is strong enough that readers understand the design '
                            'intent.'},
                  {'code': 'print(API_VERSION)',
                   'prose': 'Constants are useful for configuration values that should be named '
                            'once and reused instead of repeated as magic literals.'}]},
 {'cells': [{'code': 'items = []\nname = "Ada"\n\nif not items:\n    print("no items")',
             'kind': 'cell',
             'line': 17,
             'output': 'no items',
             'prose': ["Truthiness is one of Python's most important conveniences: conditions can "
                       'test objects directly instead of requiring explicit boolean comparisons '
                       'everywhere.',
                       'Empty containers, numeric zero, None, and False are false; most other '
                       'values are true. This makes common checks such as if items: concise and '
                       'idiomatic.']},
            {'code': 'if name:\n    print("has a name")',
             'kind': 'cell',
             'line': 35,
             'output': 'has a name',
             'prose': ['Use truthiness when it reads naturally, but choose explicit comparisons '
                       'when the distinction matters, such as checking whether a value is exactly '
                       'None.']},
            {'code': 'print(bool(0))\nprint(bool(42))',
             'kind': 'cell',
             'line': 48,
             'output': 'False\nTrue',
             'prose': ['Use truthiness when it reads naturally, but choose explicit comparisons '
                       'when the distinction matters, such as checking whether a value is exactly '
                       'None.']}],
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
  'doc_path': '/library/stdtypes.html#truth-value-testing',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#truth-value-testing',
  'expected_output': 'no items\nhas a name\nFalse\nTrue\n',
  'explanation': ["Truthiness is one of Python's most important conveniences: conditions can test "
                  'objects directly instead of requiring explicit boolean comparisons everywhere.',
                  'Empty containers, numeric zero, None, and False are false; most other values '
                  'are true. This makes common checks such as if items: concise and idiomatic.',
                  'Use truthiness when it reads naturally, but choose explicit comparisons when '
                  'the distinction matters, such as checking whether a value is exactly None.'],
  'min_python': None,
  'notes': ['Empty containers and zero-like numbers are false in conditions.',
            'Use explicit comparisons when they communicate intent better than truthiness.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'truthiness',
  'summary': 'Python conditions use truthiness, not only explicit booleans.',
  'title': 'Truthiness',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'items = []\nname = "Ada"\n\nif not items:\n    print("no items")',
                   'prose': "Truthiness is one of Python's most important conveniences: conditions "
                            'can test objects directly instead of requiring explicit boolean '
                            'comparisons everywhere.'},
                  {'code': 'items = []\nname = "Ada"\n\nif not items:\n    print("no items")',
                   'prose': 'Empty containers, numeric zero, None, and False are false; most other '
                            'values are true. This makes common checks such as if items: concise '
                            'and idiomatic.'},
                  {'code': 'if name:\n    print("has a name")',
                   'prose': 'Use truthiness when it reads naturally, but choose explicit '
                            'comparisons when the distinction matters, such as checking whether a '
                            'value is exactly None.'},
                  {'code': 'print(bool(0))\nprint(bool(42))',
                   'prose': 'Use truthiness when it reads naturally, but choose explicit '
                            'comparisons when the distinction matters, such as checking whether a '
                            'value is exactly None.'}]},
 {'cells': [{'code': 'left = [1, 2, 3]\n'
                     'right = [1, 2, 3]\n'
                     'print(left == right)\n'
                     'print(left is right)',
             'kind': 'cell',
             'line': 17,
             'output': 'True\nFalse',
             'prose': ['Equal containers can be different objects. `==` compares list contents, '
                       'while `is` checks whether both names refer to the same list object.']},
            {'code': 'same = left\nsame.append(4)\nprint(left)\nprint(same is left)',
             'kind': 'cell',
             'line': 33,
             'output': '[1, 2, 3, 4]\nTrue',
             'prose': ['Identity matters when objects are mutable. `same` is another name for '
                       '`left`, so mutating through one name changes the object seen through the '
                       'other.']},
            {'code': 'value = None\nprint(value is None)',
             'kind': 'cell',
             'line': 49,
             'output': 'True',
             'prose': ['Use `is` for singleton identity checks such as `None`. This asks whether '
                       'the value is the one special `None` object.']},
            {'code': 'small_a = 100\n'
                     'small_b = 100\n'
                     'print(small_a is small_b)\n'
                     '\n'
                     'big_a = int("1000")\n'
                     'big_b = int("1000")\n'
                     'print(big_a is big_b)\n'
                     'print(big_a == big_b)',
             'kind': 'cell',
             'line': 62,
             'output': 'True\nFalse\nTrue',
             'prose': ['`is` for integers is unreliable because CPython caches small integers '
                       '(roughly `-5` to `256`) but not larger ones. Two equal large integers can '
                       'be different objects. Use `==` for value comparisons; reserve `is` for '
                       'singletons.']}],
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
  'doc_path': '/reference/expressions.html#is-not',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#is-not',
  'expected_output': 'True\nFalse\n[1, 2, 3, 4]\nTrue\nTrue\nTrue\nFalse\nTrue\n',
  'explanation': ['Python separates equality from identity. Equality asks whether two objects '
                  'should be considered the same value, while identity asks whether two names '
                  'point to the same object.',
                  'This distinction matters for mutable containers because two equal lists can '
                  'still be independent objects. Mutating one should not imply mutating the other '
                  'unless they share identity.',
                  'The `is` operator is best reserved for identity checks against singletons such '
                  'as `None`. For ordinary values, `==` is the comparison readers expect.'],
  'min_python': None,
  'notes': ['Use `==` for ordinary value comparisons.',
            'Use `is` primarily for identity checks against singletons such as `None`.',
            'Equal mutable containers can still be independent objects.',
            "Never use `is` to compare numbers; CPython's small-integer cache makes the result an "
            'implementation detail.'],
  'section': 'Data Model',
  'see_also': [],
  'slug': 'equality-and-identity',
  'summary': '== compares values, while is compares object identity.',
  'title': 'Equality and Identity',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'left = [1, 2, 3]\n'
                           'right = [1, 2, 3]\n'
                           'print(left == right)\n'
                           'print(left is right)',
                   'prose': 'Equal containers can be different objects. `==` compares list '
                            'contents, while `is` checks whether both names refer to the same list '
                            'object.'},
                  {'code': 'same = left\nsame.append(4)\nprint(left)\nprint(same is left)',
                   'prose': 'Identity matters when objects are mutable. `same` is another name for '
                            '`left`, so mutating through one name changes the object seen through '
                            'the other.'},
                  {'code': 'value = None\nprint(value is None)',
                   'prose': 'Use `is` for singleton identity checks such as `None`. This asks '
                            'whether the value is the one special `None` object.'},
                  {'code': 'small_a = 100\n'
                           'small_b = 100\n'
                           'print(small_a is small_b)\n'
                           '\n'
                           'big_a = int("1000")\n'
                           'big_b = int("1000")\n'
                           'print(big_a is big_b)\n'
                           'print(big_a == big_b)',
                   'prose': '`is` for integers is unreliable because CPython caches small integers '
                            '(roughly `-5` to `256`) but not larger ones. Two equal large integers '
                            'can be different objects. Use `==` for value comparisons; reserve '
                            '`is` for singletons.'}]},
 {'cells': [{'code': 'first = ["python"]\n'
                     'second = first\n'
                     'second.append("workers")\n'
                     'print(first)\n'
                     'print(second)',
             'kind': 'cell',
             'line': 17,
             'output': "['python', 'workers']\n['python', 'workers']",
             'prose': ['Mutable objects can change in place. `first` and `second` point to the '
                       'same list, so appending through one name changes the object seen through '
                       'both names.']},
            {'code': 'text = "python"\nupper_text = text.upper()\nprint(text)\nprint(upper_text)',
             'kind': 'cell',
             'line': 34,
             'output': 'python\nPYTHON',
             'prose': ['Immutable objects do not change in place. String methods such as `upper()` '
                       'return a new string, leaving the original string unchanged.']},
            {'code': 'numbers = [3, 1, 2]\n'
                     'ordered = sorted(numbers)\n'
                     'print(ordered)\n'
                     'print(numbers)',
             'kind': 'cell',
             'line': 50,
             'output': '[1, 2, 3]\n[3, 1, 2]',
             'prose': ['Some APIs make the boundary explicit. `sorted()` returns a new list, while '
                       'methods such as `append()` and `list.sort()` mutate an existing list.']}],
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
  'doc_path': '/reference/datamodel.html#objects-values-and-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types',
  'expected_output': "['python', 'workers']\n"
                     "['python', 'workers']\n"
                     'python\n'
                     'PYTHON\n'
                     '[1, 2, 3]\n'
                     '[3, 1, 2]\n',
  'explanation': ['Objects in Python can be mutable or immutable. Mutable objects such as lists '
                  'and dictionaries can change in place, while immutable objects such as strings '
                  'and tuples produce new values instead.',
                  'Names can share one mutable object, so a change through one name is visible '
                  'through another. This is powerful, but it is also the source of many beginner '
                  'surprises.',
                  'The boundary matters across Python: `append()` mutates a list, string methods '
                  'return new strings, and `sorted()` returns a new list while `list.sort()` '
                  'mutates an existing one.'],
  'min_python': None,
  'notes': ['Lists and dictionaries are mutable; strings and tuples are immutable.',
            'Aliasing is useful, but copy mutable containers when independent changes are needed.',
            'Pay attention to whether an operation mutates in place or returns a new value.'],
  'section': 'Data Model',
  'see_also': [],
  'slug': 'mutability',
  'summary': 'Some objects change in place, while others return new values.',
  'title': 'Mutability',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'first = ["python"]\n'
                           'second = first\n'
                           'second.append("workers")\n'
                           'print(first)\n'
                           'print(second)',
                   'prose': 'Mutable objects can change in place. `first` and `second` point to '
                            'the same list, so appending through one name changes the object seen '
                            'through both names.'},
                  {'code': 'text = "python"\n'
                           'upper_text = text.upper()\n'
                           'print(text)\n'
                           'print(upper_text)',
                   'prose': 'Immutable objects do not change in place. String methods such as '
                            '`upper()` return a new string, leaving the original string '
                            'unchanged.'},
                  {'code': 'numbers = [3, 1, 2]\n'
                           'ordered = sorted(numbers)\n'
                           'print(ordered)\n'
                           'print(numbers)',
                   'prose': 'Some APIs make the boundary explicit. `sorted()` returns a new list, '
                            'while methods such as `append()` and `list.sort()` mutate an existing '
                            'list.'}]},
 {'cells': [{'code': 'import gc\n'
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
             'kind': 'cell',
             'line': 17,
             'output': "True\n['Ada']\nTrue\nobject can be reclaimed",
             'prose': ['Use `is` and `id()` to observe identity while two names refer to the same '
                       'object.']}],
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
  'doc_path': '/reference/datamodel.html#objects-values-and-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types',
  'expected_output': "True\n['Ada']\nTrue\nobject can be reclaimed\n",
  'explanation': ['References keep objects alive until Python can reclaim them. It exists to make '
                  'a common boundary explicit instead of leaving the behavior implicit in a larger '
                  'program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['Use `is` and `id()` to observe identity while two names refer to the same object.',
            'Deleting a name removes one reference; it does not directly destroy the object if '
            'another reference still exists.',
            'Python reclaims unreachable objects automatically, so programs usually manage '
            'ownership by controlling references.'],
  'section': 'Basics',
  'see_also': [],
  'slug': 'object-lifecycle',
  'summary': 'References keep objects alive until Python can reclaim them.',
  'title': 'Object Lifecycle',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import gc\n'
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
                   'prose': 'Use `is` and `id()` to observe identity while two names refer to the '
                            'same object.'}]},
 {'cells': [{'code': 'english = "hello"\n'
                     'french = "café"\n'
                     'thai = "สวัสดี"\n'
                     '\n'
                     'for label, word in [("English", english), ("French", french), ("Thai", '
                     'thai)]:\n'
                     '    print(label, word, len(word), len(word.encode("utf-8")))',
             'kind': 'cell',
             'line': 17,
             'output': 'English hello 5 5\nFrench café 4 5\nThai สวัสดี 6 18',
             'prose': ['Compare three words by code-point count and UTF-8 byte count. ASCII '
                       'characters take one byte each (`hello` → 5 bytes); the `é` in `café` is '
                       'one code point but two UTF-8 bytes; each Thai character takes three. The '
                       '`str` type abstracts over all three.']},
            {'code': 'print(thai[0])\nprint([hex(ord(char)) for char in thai[:2]])',
             'kind': 'cell',
             'line': 36,
             'output': "ส\n['0xe2a', '0xe27']",
             'prose': ['Indexing and iteration work with Unicode code points, not encoded bytes. '
                       '`ord()` returns the integer code point, which is often displayed in '
                       'hexadecimal when teaching text encoding.']},
            {'code': 'text = "  café  "\n'
                     'clean = text.strip()\n'
                     'print(clean)\n'
                     'print(clean.upper())\n'
                     'print(clean.encode("utf-8"))',
             'kind': 'cell',
             'line': 50,
             'output': "café\nCAFÉ\nb'caf\\xc3\\xa9'",
             'prose': ['String methods return new strings because strings are immutable. Encoding '
                       'turns text into bytes when another system needs a byte representation.']}],
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
  'doc_path': '/library/stdtypes.html#text-sequence-type-str',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#text-sequence-type-str',
  'expected_output': 'English hello 5 5\n'
                     'French café 4 5\n'
                     'Thai สวัสดี 6 18\n'
                     'ส\n'
                     "['0xe2a', '0xe27']\n"
                     'café\n'
                     'CAFÉ\n'
                     "b'caf\\xc3\\xa9'\n",
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
  'min_python': None,
  'notes': ['Use `str` for text and `bytes` for binary data.',
            '`len(text)` counts Unicode code points; `len(text.encode("utf-8"))` counts encoded '
            'bytes.',
            'ASCII text is a useful baseline because each ASCII code point is one UTF-8 byte.',
            'String methods return new strings because strings are immutable.',
            'User-visible “characters” can be more subtle than code points; combining marks and '
            'emoji sequences may need specialized text handling.'],
  'section': 'Text',
  'see_also': [],
  'slug': 'strings',
  'summary': 'Strings are immutable Unicode text sequences.',
  'title': 'Strings',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'english = "hello"\n'
                           'french = "café"\n'
                           'thai = "สวัสดี"\n'
                           '\n'
                           'for label, word in [("English", english), ("French", french), ("Thai", '
                           'thai)]:\n'
                           '    print(label, word, len(word), len(word.encode("utf-8")))',
                   'prose': 'Compare three words by code-point count and UTF-8 byte count. ASCII '
                            'characters take one byte each (`hello` → 5 bytes); the `é` in `café` '
                            'is one code point but two UTF-8 bytes; each Thai character takes '
                            'three. The `str` type abstracts over all three.'},
                  {'code': 'print(thai[0])\nprint([hex(ord(char)) for char in thai[:2]])',
                   'prose': 'Indexing and iteration work with Unicode code points, not encoded '
                            'bytes. `ord()` returns the integer code point, which is often '
                            'displayed in hexadecimal when teaching text encoding.'},
                  {'code': 'text = "  café  "\n'
                           'clean = text.strip()\n'
                           'print(clean)\n'
                           'print(clean.upper())\n'
                           'print(clean.encode("utf-8"))',
                   'prose': 'String methods return new strings because strings are immutable. '
                            'Encoding turns text into bytes when another system needs a byte '
                            'representation.'}]},
 {'cells': [{'code': 'text = "café"\n'
                     'data = text.encode("utf-8")\n'
                     'print(data)\n'
                     'print(len(text), len(data))',
             'kind': 'cell',
             'line': 22,
             'output': "b'caf\\xc3\\xa9'\n4 5",
             'prose': ['Encode text when an external boundary needs bytes. UTF-8 uses one byte for '
                       'ASCII characters and more than one byte for many other characters.']},
            {'code': 'print(data.decode("utf-8"))',
             'kind': 'cell',
             'line': 38,
             'output': 'café',
             'prose': ['Decode bytes when the program needs text again. The decoder must match the '
                       'encoding used at the boundary.']},
            {'code': 'print(data[0])',
             'kind': 'cell',
             'line': 50,
             'output': '99',
             'prose': ['Indexing a `bytes` object returns an integer byte value, not a '
                       'one-character `bytes` object.']},
            {'code': 'packet = bytearray(b"py")\npacket[0] = ord("P")\nprint(packet)',
             'kind': 'cell',
             'line': 62,
             'output': "bytearray(b'Py')",
             'prose': ['`bytes` is immutable. Use `bytearray` when binary data must be changed in '
                       'place.']}],
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
  'doc_path': '/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview',
  'expected_output': "b'caf\\xc3\\xa9'\n4 5\ncafé\n99\nbytearray(b'Py')\n",
  'explanation': ['`str` stores Unicode text. `bytes` stores raw byte values. The boundary matters '
                  'whenever text leaves Python for a file, network protocol, subprocess, or binary '
                  'format.',
                  'Encoding turns text into bytes with a named encoding such as UTF-8. Decoding '
                  'turns bytes back into text. The lengths can differ because one Unicode '
                  'character may require several bytes.',
                  'Use immutable `bytes` for stable binary data and `bytearray` when the bytes '
                  'must be changed in place.'],
  'min_python': None,
  'notes': ['Encode text when an external boundary needs bytes.',
            'Decode bytes when you want text again.',
            'Indexing `bytes` returns integers from 0 to 255.',
            'Use `bytearray` when binary data must be changed in place.'],
  'section': 'Basics',
  'see_also': ['strings', 'literals', 'networking'],
  'slug': 'bytes-and-bytearray',
  'summary': 'bytes and bytearray store binary data, not Unicode text.',
  'title': 'Bytes and Bytearray',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'text = "café"\n'
                           'data = text.encode("utf-8")\n'
                           'print(data)\n'
                           'print(len(text), len(data))',
                   'prose': 'Encode text when an external boundary needs bytes. UTF-8 uses one '
                            'byte for ASCII characters and more than one byte for many other '
                            'characters.'},
                  {'code': 'print(data.decode("utf-8"))',
                   'prose': 'Decode bytes when the program needs text again. The decoder must '
                            'match the encoding used at the boundary.'},
                  {'code': 'print(data[0])',
                   'prose': 'Indexing a `bytes` object returns an integer byte value, not a '
                            'one-character `bytes` object.'},
                  {'code': 'packet = bytearray(b"py")\npacket[0] = ord("P")\nprint(packet)',
                   'prose': '`bytes` is immutable. Use `bytearray` when binary data must be '
                            'changed in place.'}]},
 {'cells': [{'code': 'name = "Ada"\n'
                     'score = 9.5\n'
                     'rank = 1\n'
                     '\n'
                     'message = f"{name} scored {score}"\n'
                     'print(message)',
             'kind': 'cell',
             'line': 17,
             'output': 'Ada scored 9.5',
             'prose': ['An f-string evaluates expressions inside braces and inserts their string '
                       'form into the surrounding text. This is clearer than joining several '
                       'converted values by hand.']},
            {'code': 'row = f"{rank:>2} | {name:<8} | {score:05.1f}"\nprint(row)',
             'kind': 'cell',
             'line': 34,
             'output': ' 1 | Ada      | 009.5',
             'prose': ['Format specifications after `:` control display without changing the '
                       'underlying values. Here the rank is right-aligned, the name is '
                       'left-aligned, and the score is padded to one decimal place.']},
            {'code': 'print(f"{score = }")',
             'kind': 'cell',
             'line': 47,
             'output': 'score = 9.5',
             'prose': ['The debug form with `=` is useful while learning or logging because it '
                       'prints both the expression and the value.']}],
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
  'doc_path': '/tutorial/inputoutput.html#formatted-string-literals',
  'doc_url': 'https://docs.python.org/3.13/tutorial/inputoutput.html#formatted-string-literals',
  'expected_output': 'Ada scored 9.5\n 1 | Ada      | 009.5\nscore = 9.5\n',
  'explanation': ['Formatted string literals, or f-strings, exist because programs constantly need '
                  'to turn values into human-readable text. They keep the expression next to the '
                  'words it explains.',
                  'Format specifications after `:` control presentation details such as width, '
                  'alignment, padding, and precision. This separates the value being computed from '
                  'the way it should be displayed.',
                  'Use f-strings for most new formatting code. They relate directly to '
                  'expressions: anything inside braces is evaluated, then formatted into the '
                  'surrounding string.'],
  'min_python': None,
  'notes': ['Use `f"..."` strings for most new formatting code.',
            'Expressions inside braces are evaluated before formatting.',
            'Format specifications after `:` control alignment, width, padding, and precision.'],
  'section': 'Text',
  'see_also': [],
  'slug': 'string-formatting',
  'summary': 'f-strings turn values into readable text at the point of use.',
  'title': 'String Formatting',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'name = "Ada"\n'
                           'score = 9.5\n'
                           'rank = 1\n'
                           '\n'
                           'message = f"{name} scored {score}"\n'
                           'print(message)',
                   'prose': 'An f-string evaluates expressions inside braces and inserts their '
                            'string form into the surrounding text. This is clearer than joining '
                            'several converted values by hand.'},
                  {'code': 'row = f"{rank:>2} | {name:<8} | {score:05.1f}"\nprint(row)',
                   'prose': 'Format specifications after `:` control display without changing the '
                            'underlying values. Here the rank is right-aligned, the name is '
                            'left-aligned, and the score is padded to one decimal place.'},
                  {'code': 'print(f"{score = }")',
                   'prose': 'The debug form with `=` is useful while learning or logging because '
                            'it prints both the expression and the value.'}]},
 {'cells': [{'code': 'temperature = 72\n'
                     '\n'
                     'if temperature < 60:\n'
                     '    print("cold")\n'
                     'elif temperature < 80:\n'
                     '    print("comfortable")\n'
                     'else:\n'
                     '    print("hot")',
             'kind': 'cell',
             'line': 17,
             'output': 'comfortable',
             'prose': ['Start with the value that the branches will test. A conditional is only '
                       'useful when the branch condition is visible and meaningful.',
                       'Use `if`, `elif`, and `else` for one ordered choice. Python tests the '
                       'branches from top to bottom and runs only the first matching block.']},
            {'code': 'items = ["coat", "hat"]\nif items:\n    print(f"packing {len(items)} items")',
             'kind': 'cell',
             'line': 38,
             'output': 'packing 2 items',
             'prose': ['Truthiness is part of conditional flow. Empty collections are false, so '
                       '`if items:` reads as “if there is anything to work with.”']},
            {'code': 'status = "ok" if temperature < 90 else "danger"\nprint(status)',
             'kind': 'cell',
             'line': 52,
             'output': 'ok',
             'prose': ['Use the ternary expression when you are choosing a value. If either side '
                       'needs multiple statements, use a normal `if` block instead.']}],
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
  'doc_path': '/tutorial/controlflow.html#if-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#if-statements',
  'expected_output': 'comfortable\npacking 2 items\nok\n',
  'explanation': ['`if`, `elif`, and `else` let a program choose one path based on a condition. '
                  'Python uses indentation to show which statements belong to each branch.',
                  'Conditions use Python truthiness: booleans work directly, and many objects such '
                  'as empty lists or empty strings are considered false. Order branches from most '
                  'specific to most general.',
                  "Use `elif` to keep one decision flat instead of nested. Use Python's ternary "
                  'expression only when you are choosing between two values.'],
  'min_python': None,
  'notes': ['Python has no mandatory parentheses around conditions; the colon and indentation '
            'define the block.',
            'Comparison operators such as `<` and `==` can be chained, as in `0 < value < 10`.',
            'Keep branch bodies short; move larger work into functions so the decision remains '
            'easy to scan.'],
  'section': 'Control Flow',
  'see_also': [],
  'slug': 'conditionals',
  'summary': 'if, elif, and else choose which block runs.',
  'title': 'Conditionals',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'temperature = 72\n'
                           '\n'
                           'if temperature < 60:\n'
                           '    print("cold")\n'
                           'elif temperature < 80:\n'
                           '    print("comfortable")\n'
                           'else:\n'
                           '    print("hot")',
                   'prose': 'Start with the value that the branches will test. A conditional is '
                            'only useful when the branch condition is visible and meaningful.'},
                  {'code': 'temperature = 72\n'
                           '\n'
                           'if temperature < 60:\n'
                           '    print("cold")\n'
                           'elif temperature < 80:\n'
                           '    print("comfortable")\n'
                           'else:\n'
                           '    print("hot")',
                   'prose': 'Use `if`, `elif`, and `else` for one ordered choice. Python tests the '
                            'branches from top to bottom and runs only the first matching block.'},
                  {'code': 'items = ["coat", "hat"]\n'
                           'if items:\n'
                           '    print(f"packing {len(items)} items")',
                   'prose': 'Truthiness is part of conditional flow. Empty collections are false, '
                            'so `if items:` reads as “if there is anything to work with.”'},
                  {'code': 'status = "ok" if temperature < 90 else "danger"\nprint(status)',
                   'prose': 'Use the ternary expression when you are choosing a value. If either '
                            'side needs multiple statements, use a normal `if` block instead.'}]},
 {'cells': [{'code': 'def price_after_discount(price, percent):\n'
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
             'kind': 'cell',
             'line': 17,
             'output': '85.0\ninvalid price\ninvalid discount',
             'prose': ['Return early when inputs cannot be handled.']}],
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
  'doc_path': '/tutorial/controlflow.html#if-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#if-statements',
  'expected_output': '85.0\ninvalid price\ninvalid discount\n',
  'explanation': ['Guard clauses handle exceptional cases early so the main path stays flat. It '
                  'exists to make a common boundary explicit instead of leaving the behavior '
                  'implicit in a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['Return early when inputs cannot be handled.',
            'After the guards, the remaining code can read as the normal path.',
            'Guard clauses are a style choice, not new syntax.'],
  'section': 'Control Flow',
  'see_also': [],
  'slug': 'guard-clauses',
  'summary': 'Guard clauses handle exceptional cases early so the main path stays flat.',
  'title': 'Guard Clauses',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def price_after_discount(price, percent):\n'
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
                   'prose': 'Return early when inputs cannot be handled.'}]},
 {'cells': [{'code': 'messages = ["hello", "", "python"]\n'
                     '\n'
                     'for message in messages:\n'
                     '    if length := len(message):\n'
                     '        print(message, length)',
             'kind': 'cell',
             'line': 22,
             'output': 'hello 5\npython 6',
             'prose': ['An assignment expression can name a computed value while a condition tests '
                       'it. Here empty strings are skipped because their length is zero.']},
            {'code': 'queue = ["retry", "ok"]\n'
                     'while (status := queue.pop(0)) != "ok":\n'
                     '    print(status)\n'
                     'print(status)',
             'kind': 'cell',
             'line': 39,
             'output': 'retry\nok',
             'prose': ['The same idea works in loops that read state until a sentinel appears. The '
                       'assignment and comparison stay together.']}],
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
  'doc_path': '/reference/expressions.html#assignment-expressions',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#assignment-expressions',
  'expected_output': 'hello 5\npython 6\nretry\nok\n',
  'explanation': ['The assignment expression operator `:=` assigns a name while evaluating an '
                  'expression. It is often called the walrus operator.',
                  'Use it when computing a value and testing it are naturally one step. Avoid it '
                  'when a separate assignment would make the code easier to read.',
                  'The boundary is readability: the walrus operator can remove duplication, but it '
                  'should not hide important state changes.'],
  'min_python': None,
  'notes': ['`name := expression` assigns and evaluates to the assigned value.',
            'Use it to avoid computing the same value twice.',
            'Prefer a normal assignment when the expression becomes hard to scan.'],
  'section': 'Control Flow',
  'see_also': ['conditionals', 'while-loops', 'variables'],
  'slug': 'assignment-expressions',
  'summary': 'The walrus operator assigns a value inside an expression.',
  'title': 'Assignment Expressions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'messages = ["hello", "", "python"]\n'
                           '\n'
                           'for message in messages:\n'
                           '    if length := len(message):\n'
                           '        print(message, length)',
                   'prose': 'An assignment expression can name a computed value while a condition '
                            'tests it. Here empty strings are skipped because their length is '
                            'zero.'},
                  {'code': 'queue = ["retry", "ok"]\n'
                           'while (status := queue.pop(0)) != "ok":\n'
                           '    print(status)\n'
                           'print(status)',
                   'prose': 'The same idea works in loops that read state until a sentinel '
                            'appears. The assignment and comparison stay together.'}]},
 {'cells': [{'code': 'for name in ["Ada", "Grace", "Guido"]:\n    print(name)',
             'kind': 'cell',
             'line': 17,
             'output': 'Ada\nGrace\nGuido',
             'prose': ['Python for loops iterate over values from an iterable. This is different '
                       'from languages where for primarily means incrementing a numeric counter.']},
            {'code': 'for number in range(3):\n    print(number)',
             'kind': 'cell',
             'line': 32,
             'output': '0\n1\n2',
             'prose': ['range() is itself an iterable that produces numbers lazily. Use it when '
                       'you need a sequence of integers, but prefer direct iteration when you '
                       'already have a collection.']}],
  'code': 'for name in ["Ada", "Grace", "Guido"]:\n'
          '    print(name)\n'
          '\n'
          'for number in range(3):\n'
          '    print(number)\n',
  'doc_path': '/tutorial/controlflow.html#for-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#for-statements',
  'expected_output': 'Ada\nGrace\nGuido\n0\n1\n2\n',
  'explanation': ['Python for loops iterate over values from an iterable. This is different from '
                  'languages where for primarily means incrementing a numeric counter.',
                  'range() is itself an iterable that produces numbers lazily. Use it when you '
                  'need a sequence of integers, but prefer direct iteration when you already have '
                  'a collection.',
                  'Blocks are defined by indentation. range(3) yields 0, 1, and 2.'],
  'min_python': None,
  'notes': ['Blocks are defined by indentation.', 'range(3) yields 0, 1, and 2.'],
  'section': 'Control Flow',
  'see_also': [],
  'slug': 'for-loops',
  'summary': 'for iterates over any iterable object.',
  'title': 'For Loops',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'for name in ["Ada", "Grace", "Guido"]:\n    print(name)',
                   'prose': 'Python for loops iterate over values from an iterable. This is '
                            'different from languages where for primarily means incrementing a '
                            'numeric counter.'},
                  {'code': 'for number in range(3):\n    print(number)',
                   'prose': 'range() is itself an iterable that produces numbers lazily. Use it '
                            'when you need a sequence of integers, but prefer direct iteration '
                            'when you already have a collection.'}]},
 {'cells': [{'code': 'names = ["Ada", "", "Grace"]\n'
                     'for name in names:\n'
                     '    if not name:\n'
                     '        continue\n'
                     '    print(name)',
             'kind': 'cell',
             'line': 22,
             'output': 'Ada\nGrace',
             'prose': ['`continue` skips the rest of the current iteration. The empty name is '
                       'ignored, and the loop moves on to the next value.']},
            {'code': 'commands = ["load", "save", "stop", "delete"]\n'
                     'for command in commands:\n'
                     '    if command == "stop":\n'
                     '        break\n'
                     '    print(command)',
             'kind': 'cell',
             'line': 39,
             'output': 'load\nsave',
             'prose': ['`break` exits the loop immediately. The value after `stop` is never '
                       'processed because the loop has already ended.']}],
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
  'doc_path': '/tutorial/controlflow.html#break-and-continue-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements',
  'expected_output': 'Ada\nGrace\nload\nsave\n',
  'explanation': ['`break` and `continue` control the nearest enclosing loop. They exist for loops '
                  'whose body discovers an early stop rule or an item-level skip rule.',
                  'Use `continue` when the current item should not run the rest of the body. Use '
                  '`break` when no later item should be processed.',
                  'The alternative is ordinary `if`/`else` nesting. Prefer `break` and `continue` '
                  'when they keep the normal path flatter and easier to read.'],
  'min_python': None,
  'notes': ['`continue` skips to the next loop iteration.',
            '`break` exits the nearest enclosing loop immediately.',
            'Prefer plain `if`/`else` when the loop does not need early skip or early stop '
            'behavior.'],
  'section': 'Control Flow',
  'see_also': ['for-loops', 'while-loops', 'loop-else'],
  'slug': 'break-and-continue',
  'summary': 'break exits a loop early, while continue skips to the next iteration.',
  'title': 'Break and Continue',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'names = ["Ada", "", "Grace"]\n'
                           'for name in names:\n'
                           '    if not name:\n'
                           '        continue\n'
                           '    print(name)',
                   'prose': '`continue` skips the rest of the current iteration. The empty name is '
                            'ignored, and the loop moves on to the next value.'},
                  {'code': 'commands = ["load", "save", "stop", "delete"]\n'
                           'for command in commands:\n'
                           '    if command == "stop":\n'
                           '        break\n'
                           '    print(command)',
                   'prose': '`break` exits the loop immediately. The value after `stop` is never '
                            'processed because the loop has already ended.'}]},
 {'cells': [{'code': 'names = ["Ada", "Grace", "Guido"]\n'
                     '\n'
                     'for name in names:\n'
                     '    if name == "Grace":\n'
                     '        print("found")\n'
                     '        break\n'
                     'else:\n'
                     '    print("missing")',
             'kind': 'cell',
             'line': 22,
             'output': 'found',
             'prose': ['If the loop reaches `break`, the `else` block is skipped. This branch '
                       'means the search succeeded early.']},
            {'code': 'for name in names:\n'
                     '    if name == "Linus":\n'
                     '        print("found")\n'
                     '        break\n'
                     'else:\n'
                     '    print("missing")',
             'kind': 'cell',
             'line': 41,
             'output': 'missing',
             'prose': ['If the loop finishes without `break`, the `else` block runs. This branch '
                       'means the search examined every value and found nothing.']}],
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
  'doc_path': '/tutorial/controlflow.html#else-clauses-on-loops',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#else-clauses-on-loops',
  'expected_output': 'found\nmissing\n',
  'explanation': ['Python loops can have an `else` clause. The name is surprising at first: loop '
                  '`else` means “no `break` happened,” not “the loop condition was false.”',
                  'This is useful for searches. Put the successful early exit in `break`, then put '
                  'the not-found path in `else`.',
                  'Use loop `else` sparingly. It is clearest when the loop is visibly searching '
                  'for something.'],
  'min_python': None,
  'notes': ['Loop `else` runs when the loop was not ended by `break`.',
            'It is best for search loops with a clear found/not-found split.',
            'It works with both `for` and `while` loops.'],
  'section': 'Control Flow',
  'see_also': ['break-and-continue', 'for-loops', 'while-loops'],
  'slug': 'loop-else',
  'summary': 'A loop else block runs only when the loop did not end with break.',
  'title': 'Loop Else',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'names = ["Ada", "Grace", "Guido"]\n'
                           '\n'
                           'for name in names:\n'
                           '    if name == "Grace":\n'
                           '        print("found")\n'
                           '        break\n'
                           'else:\n'
                           '    print("missing")',
                   'prose': 'If the loop reaches `break`, the `else` block is skipped. This branch '
                            'means the search succeeded early.'},
                  {'code': 'for name in names:\n'
                           '    if name == "Linus":\n'
                           '        print("found")\n'
                           '        break\n'
                           'else:\n'
                           '    print("missing")',
                   'prose': 'If the loop finishes without `break`, the `else` block runs. This '
                            'branch means the search examined every value and found nothing.'}]},
 {'cells': [{'code': 'names = ["Ada", "Grace", "Guido"]\n\nfor name in names:\n    print(name)',
             'kind': 'cell',
             'line': 22,
             'output': 'Ada\nGrace\nGuido',
             'prose': ['Start with an ordinary list. A list stores values, and a `for` loop asks '
                       'it for one value at a time.',
                       'When you only need the values, iterate over the collection directly. There '
                       'is no index variable because the loop body does not need one.']},
            {'code': 'for index, name in enumerate(names):\n    print(index, name)',
             'kind': 'cell',
             'line': 41,
             'output': '0 Ada\n1 Grace\n2 Guido',
             'prose': ['When you need both a position and a value, use `enumerate()`. It produces '
                       'index/value pairs without manual indexing.']},
            {'code': 'scores = {"Ada": 10, "Grace": 9}\n'
                     'for name, score in scores.items():\n'
                     '    print(name, score)',
             'kind': 'cell',
             'line': 56,
             'output': 'Ada 10\nGrace 9',
             'prose': ['Dictionaries are iterable too, but `dict.items()` is the clearest way to '
                       'say that the loop needs keys and values together.']}],
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
  'doc_path': '/tutorial/controlflow.html#for-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#for-statements',
  'expected_output': 'Ada\nGrace\nGuido\n0 Ada\n1 Grace\n2 Guido\nAda 10\nGrace 9\n',
  'explanation': ["Python's `for` statement consumes values from any iterable object: lists, "
                  'strings, dictionaries, ranges, generators, files, and many standard-library '
                  'helpers.',
                  'This makes iteration a value-stream protocol rather than a special case for '
                  'arrays. The producer decides how values are made, and the loop consumes them '
                  'one at a time.',
                  'Use `enumerate()` when you need positions and values together, and '
                  '`dict.items()` when you need keys and values. These helpers express intent '
                  'better than manual indexing.'],
  'min_python': None,
  'notes': ['A `for` loop consumes values from an iterable.',
            'Different producers can feed the same loop protocol.',
            'Prefer `enumerate()` over `range(len(...))` when you need an index.'],
  'section': 'Iteration',
  'see_also': ['iterators', 'iterator-vs-iterable', 'for-loops'],
  'slug': 'iterating-over-iterables',
  'summary': 'for loops consume values from any iterable object.',
  'title': 'Iterating over Iterables',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'names = ["Ada", "Grace", "Guido"]\n'
                           '\n'
                           'for name in names:\n'
                           '    print(name)',
                   'prose': 'Start with an ordinary list. A list stores values, and a `for` loop '
                            'asks it for one value at a time.'},
                  {'code': 'names = ["Ada", "Grace", "Guido"]\n'
                           '\n'
                           'for name in names:\n'
                           '    print(name)',
                   'prose': 'When you only need the values, iterate over the collection directly. '
                            'There is no index variable because the loop body does not need one.'},
                  {'code': 'for index, name in enumerate(names):\n    print(index, name)',
                   'prose': 'When you need both a position and a value, use `enumerate()`. It '
                            'produces index/value pairs without manual indexing.'},
                  {'code': 'scores = {"Ada": 10, "Grace": 9}\n'
                           'for name, score in scores.items():\n'
                           '    print(name, score)',
                   'prose': 'Dictionaries are iterable too, but `dict.items()` is the clearest way '
                            'to say that the loop needs keys and values together.'}]},
 {'cells': [{'code': 'names = ["Ada", "Grace", "Guido"]\n'
                     'iterator = iter(names)\n'
                     'print(next(iterator))\n'
                     'print(next(iterator))',
             'kind': 'cell',
             'line': 22,
             'output': 'Ada\nGrace',
             'prose': ['`iter()` asks an iterable for an iterator. `next()` consumes one value and '
                       "advances the iterator's position."]},
            {'code': 'for name in iterator:\n    print(name)',
             'kind': 'cell',
             'line': 38,
             'output': 'Guido',
             'prose': ['A `for` loop consumes the same iterator protocol. Because two values were '
                       'already consumed, the loop sees only the remaining value.']},
            {'code': 'again = iter(names)\nprint(next(again))',
             'kind': 'cell',
             'line': 51,
             'output': 'Ada',
             'prose': ['The list itself is reusable. Asking it for a fresh iterator starts a new '
                       'pass over the same stored values.']}],
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
  'doc_path': '/library/stdtypes.html#iterator-types',
  'doc_url': 'https://docs.python.org/3.13/library/stdtypes.html#iterator-types',
  'expected_output': 'Ada\nGrace\nGuido\nAda\n',
  'explanation': ['An iterable is an object that can produce values for a loop. An iterator is the '
                  'object that remembers where that production currently is.',
                  '`iter()` asks an iterable for an iterator, and `next()` consumes one value from '
                  'that iterator. A `for` loop performs those steps for you until the iterator is '
                  'exhausted.',
                  'This is the core value-stream protocol in Python: one object produces values, '
                  'another piece of code consumes them, and many streams are one-pass.'],
  'min_python': None,
  'notes': ['Iterables produce iterators; iterators produce values.',
            '`next()` consumes one value from an iterator.',
            'Many iterators are one-pass even when the original collection is reusable.'],
  'section': 'Iteration',
  'see_also': ['iterating-over-iterables', 'iterator-vs-iterable', 'generators'],
  'slug': 'iterators',
  'summary': 'iter and next expose the protocol behind for loops.',
  'title': 'Iterators',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'names = ["Ada", "Grace", "Guido"]\n'
                           'iterator = iter(names)\n'
                           'print(next(iterator))\n'
                           'print(next(iterator))',
                   'prose': '`iter()` asks an iterable for an iterator. `next()` consumes one '
                            "value and advances the iterator's position."},
                  {'code': 'for name in iterator:\n    print(name)',
                   'prose': 'A `for` loop consumes the same iterator protocol. Because two values '
                            'were already consumed, the loop sees only the remaining value.'},
                  {'code': 'again = iter(names)\nprint(next(again))',
                   'prose': 'The list itself is reusable. Asking it for a fresh iterator starts a '
                            'new pass over the same stored values.'}]},
 {'cells': [{'code': 'names = ["Ada", "Grace"]\nprint(list(names))\nprint(list(names))',
             'kind': 'cell',
             'line': 22,
             'output': "['Ada', 'Grace']\n['Ada', 'Grace']",
             'prose': ['A list is iterable. Each `for` loop or `list()` call asks the list for a '
                       'fresh iterator under the hood, so the same data can be traversed many '
                       'times.']},
            {'code': 'stream = iter(names)\nprint(list(stream))\nprint(list(stream))',
             'kind': 'cell',
             'line': 37,
             'output': "['Ada', 'Grace']\n[]",
             'prose': ['An iterator is one-pass. Calling `iter()` returns a position-tracking '
                       'object; once it has been exhausted, it stays exhausted.']},
            {'code': 'first = iter(names)\n'
                     'second = iter(names)\n'
                     'print(first is second)\n'
                     'print(iter(first) is first)',
             'kind': 'cell',
             'line': 52,
             'output': 'False\nTrue',
             'prose': ['Calling `iter()` on an iterable returns a brand-new iterator each time. '
                       'Calling `iter()` on an iterator returns the same object — that is the rule '
                       'that lets a `for` loop accept either kind.']},
            {'code': 'def total_and_count(numbers):\n'
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
             'kind': 'cell',
             'line': 68,
             'output': '(27, 3)\n(27, 0)\n(27, 3)',
             'prose': ['The distinction shows up at API boundaries. A function that loops over its '
                       'argument twice works for an iterable but silently produces wrong answers '
                       'for an iterator, because the second pass finds the iterator already '
                       'exhausted. Materialize once at the boundary when both passes matter.']}],
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
  'doc_path': '/glossary.html#term-iterable',
  'doc_url': 'https://docs.python.org/3.13/glossary.html#term-iterable',
  'expected_output': "['Ada', 'Grace']\n"
                     "['Ada', 'Grace']\n"
                     "['Ada', 'Grace']\n"
                     '[]\n'
                     'False\n'
                     'True\n'
                     '(27, 3)\n'
                     '(27, 0)\n'
                     '(27, 3)\n',
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
  'min_python': None,
  'notes': ['An iterable produces an iterator each time `iter()` is called on it; an iterator '
            'produces values until it is exhausted.',
            '`iter(iterable)` returns a fresh iterator; `iter(iterator)` returns the same '
            'iterator.',
            'Functions that traverse their input more than once must accept an iterable or '
            'materialize the input at the boundary.'],
  'section': 'Iteration',
  'see_also': ['iterators', 'iterating-over-iterables', 'generators'],
  'slug': 'iterator-vs-iterable',
  'summary': 'Iterables produce fresh iterators; iterators are one-pass.',
  'title': 'Iterator vs Iterable',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'names = ["Ada", "Grace"]\nprint(list(names))\nprint(list(names))',
                   'prose': 'A list is iterable. Each `for` loop or `list()` call asks the list '
                            'for a fresh iterator under the hood, so the same data can be '
                            'traversed many times.'},
                  {'code': 'stream = iter(names)\nprint(list(stream))\nprint(list(stream))',
                   'prose': 'An iterator is one-pass. Calling `iter()` returns a position-tracking '
                            'object; once it has been exhausted, it stays exhausted.'},
                  {'code': 'first = iter(names)\n'
                           'second = iter(names)\n'
                           'print(first is second)\n'
                           'print(iter(first) is first)',
                   'prose': 'Calling `iter()` on an iterable returns a brand-new iterator each '
                            'time. Calling `iter()` on an iterator returns the same object — that '
                            'is the rule that lets a `for` loop accept either kind.'},
                  {'code': 'def total_and_count(numbers):\n'
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
                   'prose': 'The distinction shows up at API boundaries. A function that loops '
                            'over its argument twice works for an iterable but silently produces '
                            'wrong answers for an iterator, because the second pass finds the '
                            'iterator already exhausted. Materialize once at the boundary when '
                            'both passes matter.'}]},
 {'cells': [{'code': 'lines = iter(["alpha", "beta", ""])\n'
                     '\n'
                     'def read_line():\n'
                     '    return next(lines)\n'
                     '\n'
                     'for line in iter(read_line, ""):\n'
                     '    print(line.upper())',
             'kind': 'cell',
             'line': 17,
             'output': 'ALPHA\nBETA',
             'prose': ['A zero-argument callable produces one value at a time.']}],
  'code': 'lines = iter(["alpha", "beta", ""])\n'
          '\n'
          'def read_line():\n'
          '    return next(lines)\n'
          '\n'
          'for line in iter(read_line, ""):\n'
          '    print(line.upper())\n',
  'doc_path': '/library/functions.html#iter',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#iter',
  'expected_output': 'ALPHA\nBETA\n',
  'explanation': ['`iter(callable, sentinel)` keeps calling a zero-argument callable and yields '
                  'each result until the callable returns the sentinel value. It is the right '
                  'shape for repeated reads from files, sockets, or queues — sources where each '
                  'call produces the next chunk and a known marker means "no more".',
                  'Reach for it instead of writing `while True:` plus a manual break when the loop '
                  'body would do nothing else but read and check. The two-argument form turns a '
                  'polling callable into something that composes with `for` loops, comprehensions, '
                  'and other iterator helpers.',
                  'The callable must take no arguments. Wrap a parameterized reader in a small '
                  'lambda or method that closes over the parameters when the underlying API needs '
                  'them.'],
  'min_python': None,
  'notes': ['A zero-argument callable produces one value at a time.',
            'The sentinel value stops the loop without appearing in the output.',
            'This form is useful for repeated reads from files, sockets, or queues.'],
  'section': 'Iteration',
  'see_also': [],
  'slug': 'sentinel-iteration',
  'summary': 'iter(callable, sentinel) repeats calls until a marker value appears.',
  'title': 'Sentinel Iteration',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'lines = iter(["alpha", "beta", ""])\n'
                           '\n'
                           'def read_line():\n'
                           '    return next(lines)\n'
                           '\n'
                           'for line in iter(read_line, ""):\n'
                           '    print(line.upper())',
                   'prose': 'A zero-argument callable produces one value at a time.'}]},
 {'cells': [{'code': 'command = {"action": "move", "x": 3, "y": 4}\n'
                     '\n'
                     'match command:\n'
                     '    case {"action": "move", "x": x, "y": y}:\n'
                     '        print(f"move to {x},{y}")',
             'kind': 'cell',
             'line': 17,
             'output': 'move to 3,4',
             'prose': ['Use `match` when the shape of a value is the decision. This command is a '
                       'dictionary with an action and coordinates; the first case checks that '
                       'shape and binds `x` and `y`.']},
            {'code': 'command = {"action": "quit"}\n'
                     '\n'
                     'match command:\n'
                     '    case {"action": "move", "x": x, "y": y}:\n'
                     '        print(f"move to {x},{y}")\n'
                     '    case {"action": "quit"}:\n'
                     '        print("quit")',
             'kind': 'cell',
             'line': 33,
             'output': 'quit',
             'prose': ['Other cases describe other valid shapes. This complete fragment changes '
                       'the command so the `quit` case is the first matching pattern.']},
            {'code': 'command = {"action": "jump"}\n'
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
             'kind': 'cell',
             'line': 51,
             'output': 'unknown action: jump',
             'prose': ['Broader patterns and the `_` catch-all belong after specific cases. This '
                       'fragment extracts an unknown action before the final fallback would '
                       'run.']}],
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
  'doc_path': '/tutorial/controlflow.html#match-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#match-statements',
  'expected_output': 'move to 3,4\n',
  'explanation': ['Structural pattern matching lets a program choose a branch based on the shape '
                  'of data. It is especially useful when commands, messages, or parsed data have a '
                  'few known forms.',
                  'A `case` pattern can both check constants and bind names. The move case checks '
                  'the action and extracts `x` and `y` in one readable step.',
                  'Order matters because Python tries cases from top to bottom. Specific shapes '
                  'should appear before broad fallback cases such as `_`.'],
  'min_python': None,
  'notes': ['`match` compares structure, not just equality.',
            'Patterns can bind names such as `x` and `y` while matching.',
            'Put the catch-all `_` case last, because cases are tried from top to bottom.'],
  'section': 'Control Flow',
  'see_also': [],
  'slug': 'match-statements',
  'summary': 'match selects cases using structural pattern matching.',
  'title': 'Match Statements',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'command = {"action": "move", "x": 3, "y": 4}\n'
                           '\n'
                           'match command:\n'
                           '    case {"action": "move", "x": x, "y": y}:\n'
                           '        print(f"move to {x},{y}")',
                   'prose': 'Use `match` when the shape of a value is the decision. This command '
                            'is a dictionary with an action and coordinates; the first case checks '
                            'that shape and binds `x` and `y`.'},
                  {'code': 'command = {"action": "quit"}\n'
                           '\n'
                           'match command:\n'
                           '    case {"action": "move", "x": x, "y": y}:\n'
                           '        print(f"move to {x},{y}")\n'
                           '    case {"action": "quit"}:\n'
                           '        print("quit")',
                   'prose': 'Other cases describe other valid shapes. This complete fragment '
                            'changes the command so the `quit` case is the first matching '
                            'pattern.'},
                  {'code': 'command = {"action": "jump"}\n'
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
                   'prose': 'Broader patterns and the `_` catch-all belong after specific cases. '
                            'This fragment extracts an unknown action before the final fallback '
                            'would run.'}]},
 {'cells': [{'code': 'def describe(command):\n'
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
             'kind': 'cell',
             'line': 22,
             'output': 'move to 2,3',
             'prose': ['Sequence patterns match by position. A guard after `if` adds a condition '
                       'that must also be true.']},
            {'code': 'print(describe(["exit"]))\nprint(describe(["echo", "hello", "python"]))',
             'kind': 'cell',
             'line': 45,
             'output': 'stop\nhello python',
             'prose': ['An OR pattern accepts several alternatives in one case. A star pattern '
                       'captures the rest of a sequence.']},
            {'code': 'print(describe(["move", -1, 3]))',
             'kind': 'cell',
             'line': 59,
             'output': 'unknown',
             'prose': ['The wildcard `_` catches values that did not match earlier cases. Here the '
                       'guard rejects the negative coordinate.']}],
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
  'doc_path': '/tutorial/controlflow.html#match-statements',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#match-statements',
  'expected_output': 'move to 2,3\nstop\nhello python\nunknown\n',
  'explanation': ['Structural pattern matching is more than equality checks. Patterns can '
                  'destructure sequences, match several alternatives, capture the rest of a '
                  'sequence, and use guards.',
                  'Use these forms when the shape of data is the decision. If the decision is only '
                  'a single boolean condition, ordinary `if` statements are usually clearer.',
                  'The wildcard `_` catches everything not matched earlier.'],
  'min_python': None,
  'notes': ['Use `case _` as a wildcard fallback.',
            'Guards refine a pattern after the structure matches.',
            'OR patterns and star patterns keep shape-based branches compact.'],
  'section': 'Control Flow',
  'see_also': ['match-statements', 'tuples', 'classes'],
  'slug': 'advanced-match-patterns',
  'summary': 'match patterns can destructure sequences, combine alternatives, and add guards.',
  'title': 'Advanced Match Patterns',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def describe(command):\n'
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
                   'prose': 'Sequence patterns match by position. A guard after `if` adds a '
                            'condition that must also be true.'},
                  {'code': 'print(describe(["exit"]))\n'
                           'print(describe(["echo", "hello", "python"]))',
                   'prose': 'An OR pattern accepts several alternatives in one case. A star '
                            'pattern captures the rest of a sequence.'},
                  {'code': 'print(describe(["move", -1, 3]))',
                   'prose': 'The wildcard `_` catches values that did not match earlier cases. '
                            'Here the guard rejects the negative coordinate.'}]},
 {'cells': [{'code': 'remaining = 3\n'
                     'while remaining > 0:\n'
                     '    print(f"launch in {remaining}")\n'
                     '    remaining -= 1\n'
                     'print("liftoff")',
             'kind': 'cell',
             'line': 17,
             'output': 'launch in 3\nlaunch in 2\nlaunch in 1\nliftoff',
             'prose': ['Use `while` when the condition, not an iterable, controls repetition. Here '
                       'the loop owns the countdown state and updates it each time through the '
                       'body.']},
            {'code': 'responses = iter(["retry", "retry", "ok"])\n'
                     'status = next(responses)\n'
                     'while status != "ok":\n'
                     '    print(f"status: {status}")\n'
                     '    status = next(responses)\n'
                     'print(f"status: {status}")',
             'kind': 'cell',
             'line': 36,
             'output': 'status: retry\nstatus: retry\nstatus: ok',
             'prose': ['A sentinel loop stops when a special value appears. The loop does not know '
                       'in advance how many retries it will need; it keeps going until the state '
                       'says to stop.']}],
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
  'doc_path': '/reference/compound_stmts.html#while',
  'doc_url': 'https://docs.python.org/3.13/reference/compound_stmts.html#while',
  'expected_output': 'launch in 3\n'
                     'launch in 2\n'
                     'launch in 1\n'
                     'liftoff\n'
                     'status: retry\n'
                     'status: retry\n'
                     'status: ok\n',
  'explanation': ['A `while` loop repeats while a condition remains true. Unlike `for`, which '
                  'consumes an existing iterable, `while` is for state-driven repetition where the '
                  'next step depends on what happened so far.',
                  'The loop body must make progress toward stopping. That progress might be '
                  'decrementing a counter, reading until a sentinel value, or waiting until some '
                  'external state changes.',
                  'Reach for `for` when you already have values to consume. Reach for `while` when '
                  "the loop's own state decides whether another iteration is needed."],
  'min_python': None,
  'notes': ['Use `while` when changing state decides whether the loop continues.',
            'Update loop state inside the body so the condition can become false.',
            'Prefer `for` when you already have a collection, range, iterator, or generator to '
            'consume.'],
  'section': 'Control Flow',
  'see_also': [],
  'slug': 'while-loops',
  'summary': 'while repeats until changing state makes a condition false.',
  'title': 'While Loops',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'remaining = 3\n'
                           'while remaining > 0:\n'
                           '    print(f"launch in {remaining}")\n'
                           '    remaining -= 1\n'
                           'print("liftoff")',
                   'prose': 'Use `while` when the condition, not an iterable, controls repetition. '
                            'Here the loop owns the countdown state and updates it each time '
                            'through the body.'},
                  {'code': 'responses = iter(["retry", "retry", "ok"])\n'
                           'status = next(responses)\n'
                           'while status != "ok":\n'
                           '    print(f"status: {status}")\n'
                           '    status = next(responses)\n'
                           'print(f"status: {status}")',
                   'prose': 'A sentinel loop stops when a special value appears. The loop does not '
                            'know in advance how many retries it will need; it keeps going until '
                            'the state says to stop.'}]},
 {'cells': [{'code': 'numbers = [3, 1, 4]\nnumbers.append(1)\n\nprint(numbers)',
             'kind': 'cell',
             'line': 17,
             'output': '[3, 1, 4, 1]',
             'prose': ['Create a list with square brackets. Because lists are mutable, `append()` '
                       'changes this same list object.']},
            {'code': 'print(numbers[0])\nprint(numbers[-1])',
             'kind': 'cell',
             'line': 32,
             'output': '3\n1',
             'prose': ['Use indexes to read positions. Negative indexes are convenient for reading '
                       'from the end.']},
            {'code': 'print(sorted(numbers))\nprint(numbers)',
             'kind': 'cell',
             'line': 46,
             'output': '[1, 1, 3, 4]\n[3, 1, 4, 1]',
             'prose': ['Use `sorted()` when you want an ordered copy and still need the original '
                       'order afterward.']}],
  'code': 'numbers = [3, 1, 4]\n'
          'numbers.append(1)\n'
          '\n'
          'print(numbers)\n'
          'print(numbers[0])\n'
          'print(numbers[-1])\n'
          'print(sorted(numbers))\n'
          'print(numbers)\n',
  'doc_path': '/tutorial/datastructures.html#more-on-lists',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#more-on-lists',
  'expected_output': '[3, 1, 4, 1]\n3\n1\n[1, 1, 3, 4]\n[3, 1, 4, 1]\n',
  'explanation': ["Lists are Python's general-purpose mutable sequence type. Use them when order "
                  'matters and the collection may grow, shrink, or be rearranged.',
                  'Indexing reads individual positions. `0` is the first item, and negative '
                  'indexes count backward from the end.',
                  'Mutation and copying matter: `append()` changes the list, while `sorted()` '
                  'returns a new ordered list and leaves the original alone.'],
  'min_python': None,
  'notes': ['Lists are mutable sequences: methods such as `append()` change the list in place.',
            'Negative indexes count from the end.',
            '`sorted()` returns a new list; `list.sort()` sorts the existing list in place.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'lists',
  'summary': 'Lists are ordered, mutable collections.',
  'title': 'Lists',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'numbers = [3, 1, 4]\nnumbers.append(1)\n\nprint(numbers)',
                   'prose': 'Create a list with square brackets. Because lists are mutable, '
                            '`append()` changes this same list object.'},
                  {'code': 'print(numbers[0])\nprint(numbers[-1])',
                   'prose': 'Use indexes to read positions. Negative indexes are convenient for '
                            'reading from the end.'},
                  {'code': 'print(sorted(numbers))\nprint(numbers)',
                   'prose': 'Use `sorted()` when you want an ordered copy and still need the '
                            'original order afterward.'}]},
 {'cells': [{'code': 'point = (3, 4)\nx, y = point\nprint(x + y)',
             'kind': 'cell',
             'line': 22,
             'output': '7',
             'prose': ['Use a tuple for a fixed-size record where each position has a known '
                       'meaning. Unpacking turns those positions into names at the point of use.']},
            {'code': 'red = (255, 0, 0)\nprint(red[0])\nprint(len(red))',
             'kind': 'cell',
             'line': 36,
             'output': '255\n3',
             'prose': ['Tuples are sequences, so indexing and `len()` work. They are different '
                       'from lists because their length and item references are fixed after '
                       'creation.']},
            {'code': 'record = ("Ada", 10)\nname, score = record\nprint(f"{name}: {score}")',
             'kind': 'cell',
             'line': 51,
             'output': 'Ada: 10',
             'prose': ['Tuples pair naturally with multiple return values and unpacking. If the '
                       'fields need names everywhere, graduate to a dataclass or named tuple.']},
            {'code': 'scores = [10, 9, 8]\n'
                     'scores.append(7)\n'
                     'print(scores)\n'
                     '\n'
                     'student = ("Ada", 2024, "math")\n'
                     'name, year, subject = student\n'
                     'print(name, year, subject)',
             'kind': 'cell',
             'line': 65,
             'output': '[10, 9, 8, 7]\nAda 2024 math',
             'prose': ['Lists and tuples carry different intent. A list holds a variable number of '
                       'similar items and grows with `append`; a tuple has a fixed shape where '
                       'each position has its own meaning, and unpacking gives those positions '
                       'names.']}],
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
  'doc_path': '/tutorial/datastructures.html#tuples-and-sequences',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'expected_output': '7\n255\n3\nAda: 10\n[10, 9, 8, 7]\nAda 2024 math\n',
  'explanation': ['Tuples are ordered, immutable sequences. They exist for small fixed groups '
                  'where position has meaning: coordinates, RGB colors, database rows, and '
                  'multiple return values.',
                  'Use lists for variable-length collections of similar items. Use tuples when the '
                  'number of positions is part of the data shape and unpacking can give each '
                  'position a useful name.',
                  'Because tuples are immutable, you cannot append or replace positions in place. '
                  'If the shape needs to grow or change, a list or dataclass is usually a better '
                  'fit.'],
  'min_python': None,
  'notes': ['Tuples are immutable sequences with fixed length.',
            'Use tuples for small records where position has meaning.',
            'Use lists for variable-length collections of similar items.',
            "Reach for a dataclass or `NamedTuple` when fields deserve names everywhere they're "
            'used.'],
  'section': 'Collections',
  'see_also': ['lists', 'unpacking', 'structured-data-shapes'],
  'slug': 'tuples',
  'summary': 'Tuples group a fixed number of positional values.',
  'title': 'Tuples',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'point = (3, 4)\nx, y = point\nprint(x + y)',
                   'prose': 'Use a tuple for a fixed-size record where each position has a known '
                            'meaning. Unpacking turns those positions into names at the point of '
                            'use.'},
                  {'code': 'red = (255, 0, 0)\nprint(red[0])\nprint(len(red))',
                   'prose': 'Tuples are sequences, so indexing and `len()` work. They are '
                            'different from lists because their length and item references are '
                            'fixed after creation.'},
                  {'code': 'record = ("Ada", 10)\nname, score = record\nprint(f"{name}: {score}")',
                   'prose': 'Tuples pair naturally with multiple return values and unpacking. If '
                            'the fields need names everywhere, graduate to a dataclass or named '
                            'tuple.'},
                  {'code': 'scores = [10, 9, 8]\n'
                           'scores.append(7)\n'
                           'print(scores)\n'
                           '\n'
                           'student = ("Ada", 2024, "math")\n'
                           'name, year, subject = student\n'
                           'print(name, year, subject)',
                   'prose': 'Lists and tuples carry different intent. A list holds a variable '
                            'number of similar items and grows with `append`; a tuple has a fixed '
                            'shape where each position has its own meaning, and unpacking gives '
                            'those positions names.'}]},
 {'cells': [{'code': 'point = (3, 4)\nx, y = point\nprint(x, y)',
             'kind': 'cell',
             'line': 17,
             'output': '3 4',
             'prose': ['Unpacking binds multiple names from one iterable or mapping. It makes the '
                       'structure of data visible at the point where values are introduced.']},
            {'code': 'first, *middle, last = [1, 2, 3, 4]\nprint(first, middle, last)',
             'kind': 'cell',
             'line': 31,
             'output': '1 [2, 3] 4',
             'prose': ['Starred unpacking handles variable-length sequences by collecting the '
                       'middle or remaining values. This keeps common head-tail patterns '
                       'readable.']},
            {'code': 'def describe(name, language):\n'
                     '    print(name, language)\n'
                     '\n'
                     'data = {"name": "Ada", "language": "Python"}\n'
                     'describe(**data)',
             'kind': 'cell',
             'line': 44,
             'output': 'Ada Python',
             'prose': ['Dictionary unpacking with ** connects structured data to function calls. '
                       'It is widely used in configuration, adapters, and code that bridges APIs.',
                       'Dictionary unpacking with ** connects structured data to function calls. '
                       'It is widely used in configuration, adapters, and code that bridges '
                       'APIs.']}],
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
  'doc_path': '/tutorial/datastructures.html#tuples-and-sequences',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'expected_output': '3 4\n1 [2, 3] 4\nAda Python\n',
  'explanation': ['Unpacking binds multiple names from one iterable or mapping. It makes the '
                  'structure of data visible at the point where values are introduced.',
                  'Starred unpacking handles variable-length sequences by collecting the middle or '
                  'remaining values. This keeps common head-tail patterns readable.',
                  'Dictionary unpacking with ** connects structured data to function calls. It is '
                  'widely used in configuration, adapters, and code that bridges APIs.'],
  'min_python': None,
  'notes': ['Starred unpacking collects the remaining values into a list.',
            'Dictionary unpacking with ** is common when calling functions with structured data.',
            'Prefer indexing when you need one position; prefer unpacking when naming several '
            'positions makes the shape clearer.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'unpacking',
  'summary': 'Unpacking binds names from sequences and mappings concisely.',
  'title': 'Unpacking',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'point = (3, 4)\nx, y = point\nprint(x, y)',
                   'prose': 'Unpacking binds multiple names from one iterable or mapping. It makes '
                            'the structure of data visible at the point where values are '
                            'introduced.'},
                  {'code': 'first, *middle, last = [1, 2, 3, 4]\nprint(first, middle, last)',
                   'prose': 'Starred unpacking handles variable-length sequences by collecting the '
                            'middle or remaining values. This keeps common head-tail patterns '
                            'readable.'},
                  {'code': 'def describe(name, language):\n'
                           '    print(name, language)\n'
                           '\n'
                           'data = {"name": "Ada", "language": "Python"}\n'
                           'describe(**data)',
                   'prose': 'Dictionary unpacking with ** connects structured data to function '
                            'calls. It is widely used in configuration, adapters, and code that '
                            'bridges APIs.'},
                  {'code': 'def describe(name, language):\n'
                           '    print(name, language)\n'
                           '\n'
                           'data = {"name": "Ada", "language": "Python"}\n'
                           'describe(**data)',
                   'prose': 'Dictionary unpacking with ** connects structured data to function '
                            'calls. It is widely used in configuration, adapters, and code that '
                            'bridges APIs.'}]},
 {'cells': [{'code': 'profile = {"name": "Ada", "language": "Python"}\n'
                     'profile["year"] = 1843\n'
                     'print(profile["name"])\n'
                     'print(profile.get("timezone", "UTC"))',
             'kind': 'cell',
             'line': 17,
             'output': 'Ada\nUTC',
             'prose': ['Use a dictionary as a small record when fields have names. Direct indexing '
                       'communicates that the key is required, while `get()` communicates that a '
                       'missing key has a fallback.']},
            {'code': 'scores = {"Ada": 10, "Grace": 9}\n'
                     'print(scores["Grace"])\n'
                     'print(scores.get("Guido", 0))',
             'kind': 'cell',
             'line': 33,
             'output': '9\n0',
             'prose': ['Use a dictionary as a lookup table when keys identify values. This is '
                       'different from a list, where numeric position is the lookup key.']},
            {'code': 'for name, score in scores.items():\n    print(f"{name}: {score}")',
             'kind': 'cell',
             'line': 48,
             'output': 'Ada: 10\nGrace: 9',
             'prose': ['Use `items()` when the loop needs both keys and values. It avoids looping '
                       'over keys and then indexing back into the dictionary.']},
            {'code': 'inventory = {"apple": 0, "pear": 3, "plum": 0}\n'
                     'for name in list(inventory.keys()):\n'
                     '    if inventory[name] == 0:\n'
                     '        del inventory[name]\n'
                     'print(inventory)',
             'kind': 'cell',
             'line': 62,
             'output': "{'pear': 3}",
             'prose': ['Mutating a dictionary while iterating it raises `RuntimeError`. Snapshot '
                       'the keys with `list(d.keys())` (or build a list of changes and apply them '
                       'after the loop) so the iteration sees a stable view.']}],
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
  'doc_path': '/tutorial/datastructures.html#dictionaries',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#dictionaries',
  'expected_output': "Ada\nUTC\n9\n0\nAda: 10\nGrace: 9\n{'pear': 3}\n",
  'explanation': ["Dictionaries are Python's built-in mapping type. They exist for data where "
                  'names or keys are more meaningful than numeric positions: records, lookup '
                  'tables, counters, and JSON-like payloads.',
                  'Use direct indexing when a key is required. Use `get()` when absence is '
                  'expected and the code has a reasonable fallback.',
                  'Unlike lists, dictionaries answer “what value belongs to this key?” rather than '
                  '“what value is at this position?” Iterating with `items()` keeps each key next '
                  'to its value.'],
  'min_python': None,
  'notes': ['Dictionaries preserve insertion order in modern Python.',
            'Use `get()` when a missing key has a reasonable default.',
            'Use direct indexing when a missing key should be treated as an error.',
            'Snapshot keys with `list(d.keys())` before deleting items in a loop; mutating during '
            'iteration raises `RuntimeError`.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'dicts',
  'summary': 'Dictionaries map keys to values for records, lookup, and structured data.',
  'title': 'Dictionaries',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'profile = {"name": "Ada", "language": "Python"}\n'
                           'profile["year"] = 1843\n'
                           'print(profile["name"])\n'
                           'print(profile.get("timezone", "UTC"))',
                   'prose': 'Use a dictionary as a small record when fields have names. Direct '
                            'indexing communicates that the key is required, while `get()` '
                            'communicates that a missing key has a fallback.'},
                  {'code': 'scores = {"Ada": 10, "Grace": 9}\n'
                           'print(scores["Grace"])\n'
                           'print(scores.get("Guido", 0))',
                   'prose': 'Use a dictionary as a lookup table when keys identify values. This is '
                            'different from a list, where numeric position is the lookup key.'},
                  {'code': 'for name, score in scores.items():\n    print(f"{name}: {score}")',
                   'prose': 'Use `items()` when the loop needs both keys and values. It avoids '
                            'looping over keys and then indexing back into the dictionary.'},
                  {'code': 'inventory = {"apple": 0, "pear": 3, "plum": 0}\n'
                           'for name in list(inventory.keys()):\n'
                           '    if inventory[name] == 0:\n'
                           '        del inventory[name]\n'
                           'print(inventory)',
                   'prose': 'Mutating a dictionary while iterating it raises `RuntimeError`. '
                            'Snapshot the keys with `list(d.keys())` (or build a list of changes '
                            'and apply them after the loop) so the iteration sees a stable '
                            'view.'}]},
 {'cells': [{'code': 'languages = ["python", "go", "python"]\n'
                     'unique_languages = set(languages)\n'
                     'print(sorted(unique_languages))',
             'kind': 'cell',
             'line': 17,
             'output': "['go', 'python']",
             'prose': ['Creating a set removes duplicates. Keep a list when order and repeated '
                       'values matter; convert to a set when uniqueness is the point.']},
            {'code': 'allowed = {"python", "rust"}\n'
                     'print("python" in allowed)\n'
                     'print("ruby" in allowed)',
             'kind': 'cell',
             'line': 31,
             'output': 'True\nFalse',
             'prose': ['Membership checks are the everyday set operation. A list can also use '
                       '`in`, but a set says that membership is central to the data shape.']},
            {'code': 'compiled = {"go", "rust"}\n'
                     'print(sorted(allowed | compiled))\n'
                     'print(sorted(allowed & compiled))\n'
                     'print(sorted(allowed - compiled))',
             'kind': 'cell',
             'line': 46,
             'output': "['go', 'python', 'rust']\n['rust']\n['python']",
             'prose': ['Union, intersection, and difference describe relationships between groups '
                       'without manual loops.']}],
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
  'doc_path': '/tutorial/datastructures.html#sets',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#sets',
  'expected_output': "['go', 'python']\n"
                     'True\n'
                     'False\n'
                     "['go', 'python', 'rust']\n"
                     "['rust']\n"
                     "['python']\n",
  'explanation': ['Sets store unique hashable values. Use them when membership and de-duplication '
                  'matter more than order.',
                  'A list can answer membership with `in`, but a set communicates that membership '
                  'is the main operation. Set algebra then expresses how groups relate to each '
                  'other.',
                  'Because sets are unordered, examples often wrap output in `sorted()` so the '
                  'display is deterministic.'],
  'min_python': None,
  'notes': ['Use lists when order and repeated values matter.',
            'Use sets when uniqueness and membership are the main operations.',
            'Prefer lists when order or repeated values are part of the meaning.',
            'Sets are unordered, so sort them when examples need deterministic display.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'sets',
  'summary': 'Sets store unique values and make membership checks explicit.',
  'title': 'Sets',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'languages = ["python", "go", "python"]\n'
                           'unique_languages = set(languages)\n'
                           'print(sorted(unique_languages))',
                   'prose': 'Creating a set removes duplicates. Keep a list when order and '
                            'repeated values matter; convert to a set when uniqueness is the '
                            'point.'},
                  {'code': 'allowed = {"python", "rust"}\n'
                           'print("python" in allowed)\n'
                           'print("ruby" in allowed)',
                   'prose': 'Membership checks are the everyday set operation. A list can also use '
                            '`in`, but a set says that membership is central to the data shape.'},
                  {'code': 'compiled = {"go", "rust"}\n'
                           'print(sorted(allowed | compiled))\n'
                           'print(sorted(allowed & compiled))\n'
                           'print(sorted(allowed - compiled))',
                   'prose': 'Union, intersection, and difference describe relationships between '
                            'groups without manual loops.'}]},
 {'cells': [{'code': 'letters = ["a", "b", "c", "d", "e", "f"]\n'
                     'first_page = letters[:3]\n'
                     'rest = letters[3:]\n'
                     'print(first_page)\n'
                     'print(rest)',
             'kind': 'cell',
             'line': 17,
             'output': "['a', 'b', 'c']\n['d', 'e', 'f']",
             'prose': ['Omitted bounds mean “from the beginning” or “through the end.” Because the '
                       'stop index is excluded, adjacent slices split a sequence cleanly.']},
            {'code': 'middle = letters[1:5]\n'
                     'every_other = letters[::2]\n'
                     'reversed_letters = letters[::-1]\n'
                     'print(middle)\n'
                     'print(every_other)\n'
                     'print(reversed_letters)\n'
                     'print(letters)',
             'kind': 'cell',
             'line': 34,
             'output': "['b', 'c', 'd', 'e']\n"
                       "['a', 'c', 'e']\n"
                       "['f', 'e', 'd', 'c', 'b', 'a']\n"
                       "['a', 'b', 'c', 'd', 'e', 'f']",
             'prose': ['Use `start:stop` for a middle range and `step` when you want to skip or '
                       'walk backward. These operations return new lists; the original list is '
                       'unchanged.']}],
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
  'doc_path': '/tutorial/introduction.html#lists',
  'doc_url': 'https://docs.python.org/3.13/tutorial/introduction.html#lists',
  'expected_output': "['a', 'b', 'c']\n"
                     "['d', 'e', 'f']\n"
                     "['b', 'c', 'd', 'e']\n"
                     "['a', 'c', 'e']\n"
                     "['f', 'e', 'd', 'c', 'b', 'a']\n"
                     "['a', 'b', 'c', 'd', 'e', 'f']\n",
  'explanation': ['Slicing reads a range from an ordered sequence with `start:stop:step`. It '
                  'exists because Python code often needs a meaningful piece of a sequence: a '
                  'page, a prefix, a tail, a stride, or a reversed view.',
                  'The stop index is excluded. That convention makes lengths and adjacent ranges '
                  'line up: `items[:3]` and `items[3:]` split a sequence without overlap.',
                  'Slices return new sequence objects for built-in lists and strings. Use indexing '
                  'for one item; use slicing when the result should still be a sequence.'],
  'min_python': None,
  'notes': ['Slice stop indexes are excluded, so adjacent ranges compose cleanly.',
            'Omitted bounds mean the beginning or end of the sequence.',
            'A negative step walks backward; `[::-1]` is a common reversed-copy idiom.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'slices',
  'summary': 'Slices copy meaningful ranges from ordered sequences.',
  'title': 'Slices',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'letters = ["a", "b", "c", "d", "e", "f"]\n'
                           'first_page = letters[:3]\n'
                           'rest = letters[3:]\n'
                           'print(first_page)\n'
                           'print(rest)',
                   'prose': 'Omitted bounds mean “from the beginning” or “through the end.” '
                            'Because the stop index is excluded, adjacent slices split a sequence '
                            'cleanly.'},
                  {'code': 'middle = letters[1:5]\n'
                           'every_other = letters[::2]\n'
                           'reversed_letters = letters[::-1]\n'
                           'print(middle)\n'
                           'print(every_other)\n'
                           'print(reversed_letters)\n'
                           'print(letters)',
                   'prose': 'Use `start:stop` for a middle range and `step` when you want to skip '
                            'or walk backward. These operations return new lists; the original '
                            'list is unchanged.'}]},
 {'cells': [{'code': 'names = ["ada", "guido", "grace"]\n'
                     'titled = [name.title() for name in names]\n'
                     'print(titled)',
             'kind': 'cell',
             'line': 17,
             'output': "['Ada', 'Guido', 'Grace']",
             'prose': ['A list comprehension maps each input item to one output item. This one '
                       'calls `title()` for every name and collects the results in a new list.']},
            {'code': 'scores = {"Ada": 10, "Guido": 8, "Grace": 10}\n'
                     'high_scores = {name: score for name, score in scores.items() if score >= '
                     '10}\n'
                     'print(high_scores)',
             'kind': 'cell',
             'line': 31,
             'output': "{'Ada': 10, 'Grace': 10}",
             'prose': ['Add an `if` clause when only some items should appear. A dictionary '
                       'comprehension can transform key/value pairs while preserving the '
                       'dictionary shape.']},
            {'code': 'unique_scores = {score for score in scores.values()}\nprint(unique_scores)',
             'kind': 'cell',
             'line': 45,
             'output': '{8, 10}',
             'prose': ['A set comprehension keeps only unique results. Here two people have the '
                       'same score, so the resulting set has two values.']}],
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
  'doc_path': '/tutorial/datastructures.html#list-comprehensions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions',
  'expected_output': "['Ada', 'Guido', 'Grace']\n{'Ada': 10, 'Grace': 10}\n{8, 10}\n",
  'explanation': ['Comprehensions are expression forms for building concrete collections from '
                  'iterables. Read them from left to right: produce this value, for each item, '
                  'optionally only when a condition is true.',
                  'They are best for direct transformations where the expression is still easy to '
                  'scan. When the work needs several statements or names, an explicit loop is '
                  'usually clearer.',
                  'List, dictionary, and set comprehensions are eager: they build collections '
                  'immediately. Generator expressions use similar syntax to stream values later '
                  'and are covered in the Iteration section.'],
  'min_python': None,
  'notes': ['The left side says what to produce; the `for` clause says where values come from.',
            'Use an `if` clause for simple filters.',
            'List, dict, and set comprehensions build concrete collections immediately.',
            'Switch to a loop when the transformation needs multiple steps or explanations.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'comprehensions',
  'summary': 'Comprehensions build collections by mapping and filtering iterables.',
  'title': 'Comprehensions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'names = ["ada", "guido", "grace"]\n'
                           'titled = [name.title() for name in names]\n'
                           'print(titled)',
                   'prose': 'A list comprehension maps each input item to one output item. This '
                            'one calls `title()` for every name and collects the results in a new '
                            'list.'},
                  {'code': 'scores = {"Ada": 10, "Guido": 8, "Grace": 10}\n'
                           'high_scores = {name: score for name, score in scores.items() if score '
                           '>= 10}\n'
                           'print(high_scores)',
                   'prose': 'Add an `if` clause when only some items should appear. A dictionary '
                            'comprehension can transform key/value pairs while preserving the '
                            'dictionary shape.'},
                  {'code': 'unique_scores = {score for score in scores.values()}\n'
                           'print(unique_scores)',
                   'prose': 'A set comprehension keeps only unique results. Here two people have '
                            'the same score, so the resulting set has two values.'}]},
 {'cells': [{'code': 'colors = ["red", "blue"]\n'
                     'sizes = ["S", "M"]\n'
                     'variants = [(color, size) for color in colors for size in sizes]\n'
                     'print(variants)',
             'kind': 'cell',
             'line': 22,
             'output': "[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]",
             'prose': ['Multiple `for` clauses behave like nested loops. The leftmost `for` is the '
                       'outer loop, and the next `for` runs inside it.']},
            {'code': 'numbers = range(10)\n'
                     'filtered = [n for n in numbers if n % 2 == 0 if n > 2]\n'
                     'print(filtered)',
             'kind': 'cell',
             'line': 37,
             'output': '[4, 6, 8]',
             'prose': ['Multiple `if` clauses filter values. They are useful for simple '
                       'conditions, but an explicit loop is clearer when the rules need names or '
                       'explanation.']}],
  'code': 'colors = ["red", "blue"]\n'
          'sizes = ["S", "M"]\n'
          'variants = [(color, size) for color in colors for size in sizes]\n'
          'print(variants)\n'
          '\n'
          'numbers = range(10)\n'
          'filtered = [n for n in numbers if n % 2 == 0 if n > 2]\n'
          'print(filtered)\n',
  'doc_path': '/tutorial/datastructures.html#list-comprehensions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions',
  'expected_output': "[('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]\n[4, 6, 8]\n",
  'explanation': ['Comprehensions can contain more than one `for` clause and more than one `if` '
                  'filter. The clauses are read in the same order as nested loops.',
                  'Use these forms only while the shape remains easy to scan. If a comprehension '
                  'starts needing several names, comments, or branches, an explicit loop is '
                  'usually better.',
                  'Nested comprehensions build concrete collections immediately, just like simpler '
                  'list, dict, and set comprehensions.'],
  'min_python': None,
  'notes': ['Read comprehension clauses from left to right.',
            'Multiple `for` clauses act like nested loops.',
            'Prefer an explicit loop when the comprehension stops being obvious.'],
  'section': 'Collections',
  'see_also': ['comprehensions', 'generator-expressions', 'for-loops'],
  'slug': 'comprehension-patterns',
  'summary': 'Comprehensions can use multiple for clauses and filters when the shape stays clear.',
  'title': 'Comprehension Patterns',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'colors = ["red", "blue"]\n'
                           'sizes = ["S", "M"]\n'
                           'variants = [(color, size) for color in colors for size in sizes]\n'
                           'print(variants)',
                   'prose': 'Multiple `for` clauses behave like nested loops. The leftmost `for` '
                            'is the outer loop, and the next `for` runs inside it.'},
                  {'code': 'numbers = range(10)\n'
                           'filtered = [n for n in numbers if n % 2 == 0 if n > 2]\n'
                           'print(filtered)',
                   'prose': 'Multiple `if` clauses filter values. They are useful for simple '
                            'conditions, but an explicit loop is clearer when the rules need names '
                            'or explanation.'}]},
 {'cells': [{'code': 'names = ["Guido", "Ada", "Grace"]\nprint(sorted(names))\nprint(names)',
             'kind': 'cell',
             'line': 17,
             'output': "['Ada', 'Grace', 'Guido']\n['Guido', 'Ada', 'Grace']",
             'prose': ['`sorted()` returns a new list. Printing the original list afterward shows '
                       'that the input order did not change.']},
            {'code': 'users = [\n'
                     '    {"name": "Ada", "score": 10},\n'
                     '    {"name": "Guido", "score": 8},\n'
                     '    {"name": "Grace", "score": 10},\n'
                     ']\n'
                     'ranked = sorted(users, key=lambda user: user["score"], reverse=True)\n'
                     'print([user["name"] for user in ranked])',
             'kind': 'cell',
             'line': 32,
             'output': "['Ada', 'Grace', 'Guido']",
             'prose': ['A key function computes the value to compare. Here the records are sorted '
                       'by score, highest first, and the output shows the resulting order.']},
            {'code': 'users.sort(key=lambda user: user["name"])\n'
                     'print([user["name"] for user in users])',
             'kind': 'cell',
             'line': 50,
             'output': "['Ada', 'Grace', 'Guido']",
             'prose': ['`list.sort()` sorts the list in place. Use it when mutation is the point '
                       'and no separate sorted copy is needed.']}],
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
  'doc_path': '/howto/sorting.html',
  'doc_url': 'https://docs.python.org/3.13/howto/sorting.html',
  'expected_output': "['Ada', 'Grace', 'Guido']\n"
                     "['Guido', 'Ada', 'Grace']\n"
                     "['Ada', 'Grace', 'Guido']\n"
                     "['Ada', 'Grace', 'Guido']\n",
  'explanation': ['`sorted()` accepts any iterable and returns a new list. The original collection '
                  'is left untouched, which makes `sorted()` useful in expressions and pipelines.',
                  'Use `key=` to say what value should be compared for each item. This is the '
                  'idiomatic way to sort records, tuples, dictionaries, and objects by a field.',
                  'Use `reverse=True` for descending order. Use `list.sort()` instead when you '
                  'intentionally want to mutate an existing list in place.'],
  'min_python': None,
  'notes': ['`sorted()` makes a new list; `list.sort()` mutates an existing list.',
            '`key=` should return the value Python compares for each item.',
            "Python's sort is stable, so equal keys keep their original relative order."],
  'section': 'Collections',
  'see_also': [],
  'slug': 'sorting',
  'summary': 'sorted returns a new ordered list and key functions choose the sort value.',
  'title': 'Sorting',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'names = ["Guido", "Ada", "Grace"]\nprint(sorted(names))\nprint(names)',
                   'prose': '`sorted()` returns a new list. Printing the original list afterward '
                            'shows that the input order did not change.'},
                  {'code': 'users = [\n'
                           '    {"name": "Ada", "score": 10},\n'
                           '    {"name": "Guido", "score": 8},\n'
                           '    {"name": "Grace", "score": 10},\n'
                           ']\n'
                           'ranked = sorted(users, key=lambda user: user["score"], reverse=True)\n'
                           'print([user["name"] for user in ranked])',
                   'prose': 'A key function computes the value to compare. Here the records are '
                            'sorted by score, highest first, and the output shows the resulting '
                            'order.'},
                  {'code': 'users.sort(key=lambda user: user["name"])\n'
                           'print([user["name"] for user in users])',
                   'prose': '`list.sort()` sorts the list in place. Use it when mutation is the '
                            'point and no separate sorted copy is needed.'}]},
 {'cells': [{'code': 'from collections import Counter, defaultdict, deque, namedtuple\n'
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
             'kind': 'cell',
             'line': 17,
             'output': "[('a', 3), ('n', 2)]\n{'red': ['Ada', 'Lin'], 'blue': ['Grace']}\nfirst\n2",
             'prose': ['Use `Counter` when counting is the data shape.']}],
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
  'doc_path': '/library/collections.html',
  'doc_url': 'https://docs.python.org/3.13/library/collections.html',
  'expected_output': "[('a', 3), ('n', 2)]\n{'red': ['Ada', 'Lin'], 'blue': ['Grace']}\nfirst\n2\n",
  'explanation': ['collections provides specialized containers for common data shapes. It exists '
                  'to make a common boundary explicit instead of leaving the behavior implicit in '
                  'a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['Use `Counter` when counting is the data shape.',
            'Use `defaultdict` when grouping values by key.',
            'Use `deque` for efficient queue operations and `namedtuple` for lightweight named '
            'records.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'collections-module',
  'summary': 'collections provides specialized containers for common data shapes.',
  'title': 'Collections Module',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from collections import Counter, defaultdict, deque, namedtuple\n'
                           '\n'
                           'counts = Counter("banana")\n'
                           'print(counts.most_common(2))\n'
                           '\n'
                           'groups = defaultdict(list)\n'
                           'for name, team in [("Ada", "red"), ("Grace", "blue"), ("Lin", '
                           '"red")]:\n'
                           '    groups[team].append(name)\n'
                           'print(dict(groups))\n'
                           '\n'
                           'queue = deque(["first"])\n'
                           'queue.append("second")\n'
                           'print(queue.popleft())\n'
                           '\n'
                           'Point = namedtuple("Point", "x y")\n'
                           'print(Point(2, 3).x)',
                   'prose': 'Use `Counter` when counting is the data shape.'}]},
 {'cells': [{'code': 'import copy\n'
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
             'kind': 'cell',
             'line': 17,
             'output': "[['Ada', 'Lovelace'], ['Grace']]\n[['Ada'], ['Grace']]\nTrue\nFalse",
             'prose': ['A shallow copy makes a new outer container.']}],
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
  'doc_path': '/library/copy.html',
  'doc_url': 'https://docs.python.org/3.13/library/copy.html',
  'expected_output': "[['Ada', 'Lovelace'], ['Grace']]\n[['Ada'], ['Grace']]\nTrue\nFalse\n",
  'explanation': ['Copies can duplicate a container while still sharing nested objects. It exists '
                  'to make a common boundary explicit instead of leaving the behavior implicit in '
                  'a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['A shallow copy makes a new outer container.',
            'Nested objects are still shared by a shallow copy.',
            'Use `copy.deepcopy()` only when nested independence is required.'],
  'section': 'Collections',
  'see_also': [],
  'slug': 'copying-collections',
  'summary': 'Copies can duplicate a container while still sharing nested objects.',
  'title': 'Copying Collections',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import copy\n'
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
                   'prose': 'A shallow copy makes a new outer container.'}]},
 {'cells': [{'code': 'def greet(name):\n    return f"Hello, {name}."\n\nprint(greet("Python"))',
             'kind': 'cell',
             'line': 17,
             'output': 'Hello, Python.',
             'prose': ['`return` sends a value back to the caller. The caller can print it, store '
                       'it, or pass it to another function.']},
            {'code': 'def format_total(amount, currency="USD"):\n'
                     '    return f"{amount} {currency}"\n'
                     '\n'
                     'print(format_total(10))\n'
                     'print(format_total(10, currency="EUR"))',
             'kind': 'cell',
             'line': 32,
             'output': '10 USD\n10 EUR',
             'prose': ['Default arguments provide common values. Keyword arguments make it clear '
                       'which option is being overridden.']},
            {'code': 'def log(message):\n'
                     '    print(f"log: {message}")\n'
                     '\n'
                     'result = log("saved")\n'
                     'print(result)',
             'kind': 'cell',
             'line': 49,
             'output': 'log: saved\nNone',
             'prose': ['A function without an explicit `return` returns `None`. That makes '
                       'side-effect-only functions easy to distinguish from value-producing '
                       'ones.']},
            {'code': 'def append_broken(item, items=[]):\n'
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
             'kind': 'cell',
             'line': 66,
             'output': "['a']\n['a', 'b']\n['a']\n['b']",
             'prose': ['Mutable default arguments are evaluated once when the function is defined, '
                       'not on each call. The same list is shared across calls, so successive '
                       "calls see each other's mutations. Use `None` as the sentinel and create a "
                       'fresh container inside the body.']}],
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
  'doc_path': '/tutorial/controlflow.html#defining-functions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions',
  'expected_output': 'Hello, Python.\n'
                     '10 USD\n'
                     '10 EUR\n'
                     'log: saved\n'
                     'None\n'
                     "['a']\n"
                     "['a', 'b']\n"
                     "['a']\n"
                     "['b']\n",
  'explanation': ['Functions package behavior behind a name. `def` creates a function object that '
                  'can accept arguments, compute values, and return a result.',
                  'Default arguments make common calls short, and keyword arguments make call '
                  'sites easier to read. A function that reaches the end without `return` produces '
                  '`None`.',
                  'Use functions when a calculation has a useful name, when code repeats, or when '
                  'a piece of behavior should be tested independently.'],
  'min_python': None,
  'notes': ['Use `return` for values the caller should receive.',
            'Defaults keep common calls concise.',
            'Keyword arguments make options readable at the call site.',
            'Never use a mutable value as a default argument; use `None` and build the container '
            'inside the function body.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'functions',
  'summary': 'Use def to name reusable behavior and return results.',
  'title': 'Functions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def greet(name):\n'
                           '    return f"Hello, {name}."\n'
                           '\n'
                           'print(greet("Python"))',
                   'prose': '`return` sends a value back to the caller. The caller can print it, '
                            'store it, or pass it to another function.'},
                  {'code': 'def format_total(amount, currency="USD"):\n'
                           '    return f"{amount} {currency}"\n'
                           '\n'
                           'print(format_total(10))\n'
                           'print(format_total(10, currency="EUR"))',
                   'prose': 'Default arguments provide common values. Keyword arguments make it '
                            'clear which option is being overridden.'},
                  {'code': 'def log(message):\n'
                           '    print(f"log: {message}")\n'
                           '\n'
                           'result = log("saved")\n'
                           'print(result)',
                   'prose': 'A function without an explicit `return` returns `None`. That makes '
                            'side-effect-only functions easy to distinguish from value-producing '
                            'ones.'},
                  {'code': 'def append_broken(item, items=[]):\n'
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
                   'prose': 'Mutable default arguments are evaluated once when the function is '
                            'defined, not on each call. The same list is shared across calls, so '
                            "successive calls see each other's mutations. Use `None` as the "
                            'sentinel and create a fresh container inside the body.'}]},
 {'cells': [{'code': 'def connect(host, *, timeout=5, secure=True):\n'
                     '    scheme = "https" if secure else "http"\n'
                     '    print(f"{scheme}://{host} timeout={timeout}")\n'
                     '\n'
                     'connect("example.com")',
             'kind': 'cell',
             'line': 17,
             'output': 'https://example.com timeout=5',
             'prose': ['Parameters after `*` must be named. The default options still apply when '
                       'the caller omits them.']},
            {'code': 'connect("example.com", timeout=10)',
             'kind': 'cell',
             'line': 33,
             'output': 'https://example.com timeout=10',
             'prose': ['Naming the option makes the call site explicit. A reader does not have to '
                       'remember which positional slot controls the timeout.']},
            {'code': 'connect("localhost", secure=False)',
             'kind': 'cell',
             'line': 45,
             'output': 'http://localhost timeout=5',
             'prose': ['Flags are especially good keyword-only arguments because a bare positional '
                       '`False` is hard to interpret.']}],
  'code': 'def connect(host, *, timeout=5, secure=True):\n'
          '    scheme = "https" if secure else "http"\n'
          '    print(f"{scheme}://{host} timeout={timeout}")\n'
          '\n'
          'connect("example.com")\n'
          'connect("example.com", timeout=10)\n'
          'connect("localhost", secure=False)\n',
  'doc_path': '/tutorial/controlflow.html#special-parameters',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#special-parameters',
  'expected_output': 'https://example.com timeout=5\n'
                     'https://example.com timeout=10\n'
                     'http://localhost timeout=5\n',
  'explanation': ['A bare `*` in a function signature marks the following parameters as '
                  'keyword-only. Callers must name those arguments explicitly.',
                  'Keyword-only arguments are useful for options such as timeouts, flags, and '
                  'modes where positional calls would be ambiguous or easy to misread.',
                  'They let the required data stay positional while optional controls remain '
                  'self-documenting at the call site.'],
  'min_python': None,
  'notes': ['Put `*` before options that callers should name.',
            'Keyword-only flags avoid mysterious positional `True` and `False` arguments.',
            'Defaults work normally for keyword-only parameters.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'keyword-only-arguments',
  'summary': 'Use * to require selected function arguments to be named.',
  'title': 'Keyword-only Arguments',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def connect(host, *, timeout=5, secure=True):\n'
                           '    scheme = "https" if secure else "http"\n'
                           '    print(f"{scheme}://{host} timeout={timeout}")\n'
                           '\n'
                           'connect("example.com")',
                   'prose': 'Parameters after `*` must be named. The default options still apply '
                            'when the caller omits them.'},
                  {'code': 'connect("example.com", timeout=10)',
                   'prose': 'Naming the option makes the call site explicit. A reader does not '
                            'have to remember which positional slot controls the timeout.'},
                  {'code': 'connect("localhost", secure=False)',
                   'prose': 'Flags are especially good keyword-only arguments because a bare '
                            'positional `False` is hard to interpret.'}]},
 {'cells': [{'code': 'def scale(value, /, factor=2, *, clamp=False):\n'
                     '    result = value * factor\n'
                     '    if clamp:\n'
                     '        result = min(result, 10)\n'
                     '    return result\n'
                     '\n'
                     'print(scale(4))\n'
                     'print(scale(4, factor=3))',
             'kind': 'cell',
             'line': 22,
             'output': '8\n12',
             'prose': ['Parameters before `/` are positional-only. `value` is the main input, '
                       'while `factor` remains an ordinary parameter that can be named.']},
            {'code': 'print(scale(4, clamp=True))',
             'kind': 'cell',
             'line': 42,
             'output': '8',
             'prose': ['Parameters after `*` are keyword-only. That makes options such as `clamp` '
                       'explicit at the call site.']}],
  'code': 'def scale(value, /, factor=2, *, clamp=False):\n'
          '    result = value * factor\n'
          '    if clamp:\n'
          '        result = min(result, 10)\n'
          '    return result\n'
          '\n'
          'print(scale(4))\n'
          'print(scale(4, factor=3))\n'
          'print(scale(4, clamp=True))\n',
  'doc_path': '/tutorial/controlflow.html#special-parameters',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#special-parameters',
  'expected_output': '8\n12\n8\n',
  'explanation': ['A `/` in a function signature marks the parameters before it as '
                  'positional-only. Callers must pass those arguments by position, not by keyword.',
                  'This is useful when parameter names are implementation details or when an API '
                  'should match built-in functions that accept positional values.',
                  'Together, `/` and `*` let a signature draw clear boundaries: positional-only '
                  'inputs, ordinary inputs, and keyword-only options.'],
  'min_python': None,
  'notes': ['`/` marks parameters before it as positional-only.',
            '`*` marks parameters after it as keyword-only.',
            'Use these markers when the call shape is part of the API design.'],
  'section': 'Functions',
  'see_also': ['keyword-only-arguments', 'functions', 'args-and-kwargs'],
  'slug': 'positional-only-parameters',
  'summary': 'Use / to mark parameters that callers must pass by position.',
  'title': 'Positional-only Parameters',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def scale(value, /, factor=2, *, clamp=False):\n'
                           '    result = value * factor\n'
                           '    if clamp:\n'
                           '        result = min(result, 10)\n'
                           '    return result\n'
                           '\n'
                           'print(scale(4))\n'
                           'print(scale(4, factor=3))',
                   'prose': 'Parameters before `/` are positional-only. `value` is the main input, '
                            'while `factor` remains an ordinary parameter that can be named.'},
                  {'code': 'print(scale(4, clamp=True))',
                   'prose': 'Parameters after `*` are keyword-only. That makes options such as '
                            '`clamp` explicit at the call site.'}]},
 {'cells': [{'code': 'def total(*numbers):\n    return sum(numbers)\n\nprint(total(2, 3, 5))',
             'kind': 'cell',
             'line': 17,
             'output': '10',
             'prose': ['`*args` collects extra positional arguments into a tuple. This fits '
                       'functions that naturally accept any number of similar values.']},
            {'code': 'def describe(**metadata):\n'
                     '    print(metadata)\n'
                     '\n'
                     'describe(owner="Ada", public=True)',
             'kind': 'cell',
             'line': 32,
             'output': "{'owner': 'Ada', 'public': True}",
             'prose': ['`**kwargs` collects named arguments into a dictionary. The names become '
                       'string keys.']},
            {'code': 'def report(title, *items, **metadata):\n'
                     '    print(title)\n'
                     '    print(items)\n'
                     '    print(metadata)\n'
                     '\n'
                     'report("scores", 10, 9, owner="Ada")',
             'kind': 'cell',
             'line': 47,
             'output': "scores\n(10, 9)\n{'owner': 'Ada'}",
             'prose': ['A function can combine explicit parameters, `*args`, and `**kwargs`. Put '
                       'the flexible parts last so the fixed shape remains visible.']}],
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
  'doc_path': '/tutorial/controlflow.html#arbitrary-argument-lists',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#arbitrary-argument-lists',
  'expected_output': "10\n{'owner': 'Ada', 'public': True}\nscores\n(10, 9)\n{'owner': 'Ada'}\n",
  'explanation': ['`*args` and `**kwargs` let a function accept flexible positional and keyword '
                  'arguments. They are the function-definition counterpart to unpacking at a call '
                  'site.',
                  'These parameters are useful for wrappers, decorators, logging helpers, and APIs '
                  'that forward arguments to another function.',
                  'They should not replace clear signatures. If a function has a stable interface, '
                  'explicit parameters document expectations better than a bag of arguments.'],
  'min_python': None,
  'notes': ['Use these tools when a function naturally accepts a flexible shape.',
            'Prefer explicit parameters when the accepted arguments are known and fixed.',
            '`*args` is a tuple; `**kwargs` is a dictionary.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'args-and-kwargs',
  'summary': '*args collects extra positional arguments and **kwargs collects named ones.',
  'title': 'Args and Kwargs',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def total(*numbers):\n    return sum(numbers)\n\nprint(total(2, 3, 5))',
                   'prose': '`*args` collects extra positional arguments into a tuple. This fits '
                            'functions that naturally accept any number of similar values.'},
                  {'code': 'def describe(**metadata):\n'
                           '    print(metadata)\n'
                           '\n'
                           'describe(owner="Ada", public=True)',
                   'prose': '`**kwargs` collects named arguments into a dictionary. The names '
                            'become string keys.'},
                  {'code': 'def report(title, *items, **metadata):\n'
                           '    print(title)\n'
                           '    print(items)\n'
                           '    print(metadata)\n'
                           '\n'
                           'report("scores", 10, 9, owner="Ada")',
                   'prose': 'A function can combine explicit parameters, `*args`, and `**kwargs`. '
                            'Put the flexible parts last so the fixed shape remains visible.'}]},
 {'cells': [{'code': 'def divide_with_remainder(total, size):\n'
                     '    quotient = total // size\n'
                     '    remainder = total % size\n'
                     '    return quotient, remainder\n'
                     '\n'
                     'result = divide_with_remainder(17, 5)\n'
                     'print(result)',
             'kind': 'cell',
             'line': 17,
             'output': '(3, 2)',
             'prose': ['Returning values separated by commas returns one tuple. The tuple is '
                       'visible if the caller stores the result directly.']},
            {'code': 'boxes, leftover = result\nprint(boxes)\nprint(leftover)',
             'kind': 'cell',
             'line': 35,
             'output': '3\n2',
             'prose': ['Callers usually unpack the tuple immediately or soon after. The names at '
                       'the call site document what each position means.']}],
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
  'doc_path': '/tutorial/datastructures.html#tuples-and-sequences',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences',
  'expected_output': '(3, 2)\n3\n2\n',
  'explanation': ['Python multiple return values are tuple return values with friendly syntax. '
                  '`return a, b` creates one tuple containing two positions.',
                  'Most callers unpack that tuple immediately. Good target names make the meaning '
                  'of each returned position explicit.',
                  'Use this for small, fixed groups of results. For larger records, a dataclass or '
                  'named tuple usually communicates better.'],
  'min_python': None,
  'notes': ['A comma creates a tuple; `return a, b` returns one tuple containing two values.',
            'Unpacking at the call site gives each returned position a meaningful name.',
            'Use a class-like record when the result has many fields.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'multiple-return-values',
  'summary': 'Python returns multiple values by returning a tuple and unpacking it.',
  'title': 'Multiple Return Values',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def divide_with_remainder(total, size):\n'
                           '    quotient = total // size\n'
                           '    remainder = total % size\n'
                           '    return quotient, remainder\n'
                           '\n'
                           'result = divide_with_remainder(17, 5)\n'
                           'print(result)',
                   'prose': 'Returning values separated by commas returns one tuple. The tuple is '
                            'visible if the caller stores the result directly.'},
                  {'code': 'boxes, leftover = result\nprint(boxes)\nprint(leftover)',
                   'prose': 'Callers usually unpack the tuple immediately or soon after. The names '
                            'at the call site document what each position means.'}]},
 {'cells': [{'code': 'def make_multiplier(factor):\n'
                     '    def multiply(value):\n'
                     '        return value * factor\n'
                     '    return multiply\n'
                     '\n'
                     'double = make_multiplier(2)\n'
                     'print(double(5))',
             'kind': 'cell',
             'line': 17,
             'output': '10',
             'prose': ['Define a function inside another function when the inner behavior needs to '
                       'remember setup from the outer call. The returned function keeps access to '
                       '`factor`.']},
            {'code': 'triple = make_multiplier(3)\nprint(triple(5))',
             'kind': 'cell',
             'line': 35,
             'output': '15',
             'prose': ['Calling the outer function again creates a separate closure. `triple` uses '
                       'the same inner code, but remembers a different `factor`.']},
            {'code': 'late = []\n'
                     'for i in range(3):\n'
                     '    late.append(lambda: i)\n'
                     'print([f() for f in late])\n'
                     '\n'
                     'bound = []\n'
                     'for i in range(3):\n'
                     '    bound.append(lambda i=i: i)\n'
                     'print([f() for f in bound])',
             'kind': 'cell',
             'line': 48,
             'output': '[2, 2, 2]\n[0, 1, 2]',
             'prose': ['Closures bind names, not values. Lambdas defined in a loop all reference '
                       'the same loop variable, so calling them later sees its final value. '
                       'Capture the value at definition time by binding it as a default argument — '
                       '`lambda i=i: i` — so each closure remembers its own `i`.']}],
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
  'doc_path': '/reference/executionmodel.html#binding-of-names',
  'doc_url': 'https://docs.python.org/3.13/reference/executionmodel.html#binding-of-names',
  'expected_output': '10\n15\n[2, 2, 2]\n[0, 1, 2]\n',
  'explanation': ['A closure is a function that remembers names from the scope where it was '
                  'created. This lets you configure behavior once and call it later.',
                  'Each call to the outer function creates a separate remembered environment. That '
                  'is why `double` and `triple` can share the same code but keep different '
                  'factors.',
                  'Closures are a foundation for decorators, callbacks, and small function '
                  'factories.'],
  'min_python': None,
  'notes': ['A closure keeps access to names from the scope where the inner function was created.',
            'Each call to the outer function can create a separate remembered environment.',
            'Closures are useful for callbacks, small factories, and decorators.',
            'Closures bind names, not values; capture loop variables with `lambda x=x: ...` to '
            'freeze them at definition time.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'closures',
  'summary': 'Inner functions can remember values from an enclosing scope.',
  'title': 'Closures',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def make_multiplier(factor):\n'
                           '    def multiply(value):\n'
                           '        return value * factor\n'
                           '    return multiply\n'
                           '\n'
                           'double = make_multiplier(2)\n'
                           'print(double(5))',
                   'prose': 'Define a function inside another function when the inner behavior '
                            'needs to remember setup from the outer call. The returned function '
                            'keeps access to `factor`.'},
                  {'code': 'triple = make_multiplier(3)\nprint(triple(5))',
                   'prose': 'Calling the outer function again creates a separate closure. `triple` '
                            'uses the same inner code, but remembers a different `factor`.'},
                  {'code': 'late = []\n'
                           'for i in range(3):\n'
                           '    late.append(lambda: i)\n'
                           'print([f() for f in late])\n'
                           '\n'
                           'bound = []\n'
                           'for i in range(3):\n'
                           '    bound.append(lambda i=i: i)\n'
                           'print([f() for f in bound])',
                   'prose': 'Closures bind names, not values. Lambdas defined in a loop all '
                            'reference the same loop variable, so calling them later sees its '
                            'final value. Capture the value at definition time by binding it as a '
                            'default argument — `lambda i=i: i` — so each closure remembers its '
                            'own `i`.'}]},
 {'cells': [{'code': 'from functools import partial\n'
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
             'kind': 'cell',
             'line': 17,
             'output': '60.0\n88.0\napply_tax',
             'prose': ['A partial object remembers some arguments.']}],
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
  'doc_path': '/library/functools.html#functools.partial',
  'doc_url': 'https://docs.python.org/3.13/library/functools.html#functools.partial',
  'expected_output': '60.0\n88.0\napply_tax\n',
  'explanation': ['functools.partial pre-fills arguments to make a more specific callable. It '
                  'exists to make a common boundary explicit instead of leaving the behavior '
                  'implicit in a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['A partial object remembers some arguments.',
            'The resulting callable can be passed where an ordinary function is expected.',
            'Prefer a named function when the pre-filled behavior needs richer logic.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'partial-functions',
  'summary': 'functools.partial pre-fills arguments to make a more specific callable.',
  'title': 'Partial Functions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from functools import partial\n'
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
                   'prose': 'A partial object remembers some arguments.'}]},
 {'cells': [{'code': 'count = 0\n'
                     '\n'
                     'def bump_global():\n'
                     '    global count\n'
                     '    count += 1\n'
                     '\n'
                     'bump_global()\n'
                     'print(count)',
             'kind': 'cell',
             'line': 22,
             'output': '1',
             'prose': ['`global` tells assignment to update a module-level binding. Without it, '
                       '`count += 1` would try to assign a local `count`.']},
            {'code': 'def make_counter():\n'
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
             'kind': 'cell',
             'line': 41,
             'output': '1\n2',
             'prose': ['`nonlocal` tells assignment to update a binding in the nearest enclosing '
                       'function scope. This is useful for small closures that keep state.']}],
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
  'doc_path': '/reference/simple_stmts.html#the-global-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-global-statement',
  'expected_output': '1\n1\n2\n',
  'explanation': ['Assignment normally creates or updates a local name inside the current '
                  'function. `global` and `nonlocal` are explicit escape hatches for rebinding '
                  'names outside that local scope.',
                  'Use `nonlocal` when an inner function should update a name in an enclosing '
                  'function. Use `global` rarely; passing values and returning results is usually '
                  'clearer.',
                  'These statements affect name binding, not object mutation. Mutating a shared '
                  'list is different from rebinding the name itself.'],
  'min_python': None,
  'notes': ['Assignment inside a function is local unless declared otherwise.',
            'Prefer `nonlocal` for closure state and avoid `global` unless module state is truly '
            'intended.',
            'Passing values and returning results is usually easier to test than rebinding outer '
            'names.'],
  'section': 'Functions',
  'see_also': ['variables', 'closures', 'functions'],
  'slug': 'scope-global-nonlocal',
  'summary': 'global and nonlocal choose which outer binding assignment should update.',
  'title': 'Global and Nonlocal',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'count = 0\n'
                           '\n'
                           'def bump_global():\n'
                           '    global count\n'
                           '    count += 1\n'
                           '\n'
                           'bump_global()\n'
                           'print(count)',
                   'prose': '`global` tells assignment to update a module-level binding. Without '
                            'it, `count += 1` would try to assign a local `count`.'},
                  {'code': 'def make_counter():\n'
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
                   'prose': '`nonlocal` tells assignment to update a binding in the nearest '
                            'enclosing function scope. This is useful for small closures that keep '
                            'state.'}]},
 {'cells': [{'code': 'def total(node):\n'
                     '    subtotal = node["value"]\n'
                     '    for child in node["children"]:\n'
                     '        subtotal += total(child)\n'
                     '    return subtotal\n'
                     '\n'
                     'print(total({"value": 2, "children": []}))',
             'kind': 'cell',
             'line': 17,
             'output': '2',
             'prose': ['A leaf node is the base case. It has no children, so the function can '
                       'return its own value without making another recursive call.']},
            {'code': 'tree = {\n'
                     '    "value": 1,\n'
                     '    "children": [\n'
                     '        {"value": 2, "children": []},\n'
                     '        {"value": 3, "children": [{"value": 4, "children": []}]},\n'
                     '    ],\n'
                     '}\n'
                     '\n'
                     'print(total(tree))',
             'kind': 'cell',
             'line': 35,
             'output': '10',
             'prose': ['A non-leaf node solves the same problem for each child, then combines '
                       'those smaller totals with its own value.']}],
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
  'doc_path': '/tutorial/controlflow.html#defining-functions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions',
  'expected_output': '2\n10\n',
  'explanation': ['A recursive function calls itself to solve a smaller piece of the same problem. '
                  'Recursion exists for data that is naturally nested: trees, menus, expression '
                  'nodes, and directory-like structures.',
                  'Every recursive function needs a base case that can be answered directly. The '
                  'recursive case must move toward that base case by passing a smaller part of the '
                  'data.',
                  'Prefer loops for simple repetition over a flat sequence. Prefer recursion when '
                  'the data shape is recursive too.'],
  'min_python': None,
  'notes': ['Every recursive function needs a base case that stops the calls.',
            'Recursion fits nested data better than flat repetition.',
            'Python limits recursion depth, so loops are often better for very deep or simple '
            'repetition.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'recursion',
  'summary': 'Recursive functions solve nested problems by calling themselves on smaller pieces.',
  'title': 'Recursion',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def total(node):\n'
                           '    subtotal = node["value"]\n'
                           '    for child in node["children"]:\n'
                           '        subtotal += total(child)\n'
                           '    return subtotal\n'
                           '\n'
                           'print(total({"value": 2, "children": []}))',
                   'prose': 'A leaf node is the base case. It has no children, so the function can '
                            'return its own value without making another recursive call.'},
                  {'code': 'tree = {\n'
                           '    "value": 1,\n'
                           '    "children": [\n'
                           '        {"value": 2, "children": []},\n'
                           '        {"value": 3, "children": [{"value": 4, "children": []}]},\n'
                           '    ],\n'
                           '}\n'
                           '\n'
                           'print(total(tree))',
                   'prose': 'A non-leaf node solves the same problem for each child, then combines '
                            'those smaller totals with its own value.'}]},
 {'cells': [{'code': 'add_tax = lambda price: round(price * 1.08, 2)\nprint(add_tax(10))',
             'kind': 'cell',
             'line': 17,
             'output': '10.8',
             'prose': ['A lambda is a function expression. Assigning one to a name works, although '
                       '`def` is usually clearer for reusable behavior.']},
            {'code': 'items = [("notebook", 5), ("pen", 2), ("bag", 20)]\n'
                     'by_price = sorted(items, key=lambda item: item[1])\n'
                     'print(by_price)',
             'kind': 'cell',
             'line': 30,
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]",
             'prose': ['Lambdas are most idiomatic when passed directly to another function. '
                       '`sorted()` calls this key function once for each item.']},
            {'code': 'def price(item):\n    return item[1]\n\nprint(sorted(items, key=price))',
             'kind': 'cell',
             'line': 44,
             'output': "[('pen', 2), ('notebook', 5), ('bag', 20)]",
             'prose': ['A named function is better when the behavior should be reused or '
                       'explained. It produces the same sort key, but gives the operation a '
                       'name.']}],
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
  'doc_path': '/tutorial/controlflow.html#lambda-expressions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#lambda-expressions',
  'expected_output': '10.8\n'
                     "[('pen', 2), ('notebook', 5), ('bag', 20)]\n"
                     "[('pen', 2), ('notebook', 5), ('bag', 20)]\n",
  'explanation': ['`lambda` creates a small anonymous function expression. It is most useful when '
                  'Python asks for a function and the behavior is short enough to read inline.',
                  'A lambda can only contain one expression. Use `def` when the behavior deserves '
                  'a name, needs statements, or would be easier to test separately.',
                  'Lambdas often appear as key functions, callbacks, and tiny adapters. Keep them '
                  'simple enough that the call site remains clearer than a named helper.'],
  'min_python': None,
  'notes': ['Lambdas are expressions, not statements.',
            'Prefer `def` for multi-step or reused behavior.',
            'Lambdas are common as `key=` functions because the behavior is local to one call.'],
  'section': 'Functions',
  'see_also': [],
  'slug': 'lambdas',
  'summary': 'lambda creates small anonymous function expressions.',
  'title': 'Lambdas',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'add_tax = lambda price: round(price * 1.08, 2)\nprint(add_tax(10))',
                   'prose': 'A lambda is a function expression. Assigning one to a name works, '
                            'although `def` is usually clearer for reusable behavior.'},
                  {'code': 'items = [("notebook", 5), ("pen", 2), ("bag", 20)]\n'
                           'by_price = sorted(items, key=lambda item: item[1])\n'
                           'print(by_price)',
                   'prose': 'Lambdas are most idiomatic when passed directly to another function. '
                            '`sorted()` calls this key function once for each item.'},
                  {'code': 'def price(item):\n'
                           '    return item[1]\n'
                           '\n'
                           'print(sorted(items, key=price))',
                   'prose': 'A named function is better when the behavior should be reused or '
                            'explained. It produces the same sort key, but gives the operation a '
                            'name.'}]},
 {'cells': [{'code': 'def countdown(n):\n'
                     '    while n > 0:\n'
                     '        yield n\n'
                     '        n -= 1\n'
                     '\n'
                     'numbers = countdown(3)\n'
                     'print(next(numbers))\n'
                     'print(next(numbers))',
             'kind': 'cell',
             'line': 22,
             'output': '3\n2',
             'prose': ['Calling a generator function returns an iterator. `next()` asks for one '
                       'value and resumes the function until the next `yield`.']},
            {'code': 'for value in countdown(3):\n    print(value)',
             'kind': 'cell',
             'line': 42,
             'output': '3\n2\n1',
             'prose': ['A `for` loop repeatedly calls `next()` for you. The loop stops when the '
                       'generator is exhausted.']},
            {'code': 'def countdown_eager(n):\n'
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
             'kind': 'cell',
             'line': 57,
             'output': '[3, 2, 1]\n[3, 2, 1]\n[3, 2, 1]\n[]',
             'prose': ['`return` builds the entire result before handing it back; `yield` produces '
                       'values on demand. The list keeps its values for repeated use, while the '
                       'generator is exhausted after one pass.']},
            {'code': 'class Countdown:\n'
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
             'kind': 'cell',
             'line': 85,
             'output': '[3, 2, 1]',
             'prose': ['Every generator is an iterator. The same countdown written by hand needs '
                       '`__iter__` and `__next__` and an explicit `StopIteration`. The generator '
                       'function expresses the same protocol with one `yield`.']}],
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
  'doc_path': '/tutorial/classes.html#generators',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#generators',
  'expected_output': '3\n2\n3\n2\n1\n[3, 2, 1]\n[3, 2, 1]\n[3, 2, 1]\n[]\n[3, 2, 1]\n',
  'explanation': ['A generator function is a convenient way to write your own iterator. `yield` '
                  'produces one value, pauses the function, and resumes when the next value is '
                  'requested.',
                  'Generators are useful for pipelines, large inputs, and infinite sequences '
                  'because they avoid building an entire collection in memory.',
                  'Use `next()` to request one value manually, or loop over the generator to '
                  'consume values until it is exhausted.'],
  'min_python': None,
  'notes': ['Generator functions are a concise way to create custom iterators; every generator is '
            'an iterator.',
            '`yield` defers work and streams values; `return` produces the whole result up front.',
            'A generator is consumed as you iterate over it.',
            'Prefer a list when you need to reuse stored results; prefer a generator when values '
            'can be streamed once.'],
  'section': 'Iteration',
  'see_also': ['iterators', 'iterator-vs-iterable', 'generator-expressions'],
  'slug': 'generators',
  'summary': 'yield creates an iterator that produces values on demand.',
  'title': 'Generators',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def countdown(n):\n'
                           '    while n > 0:\n'
                           '        yield n\n'
                           '        n -= 1\n'
                           '\n'
                           'numbers = countdown(3)\n'
                           'print(next(numbers))\n'
                           'print(next(numbers))',
                   'prose': 'Calling a generator function returns an iterator. `next()` asks for '
                            'one value and resumes the function until the next `yield`.'},
                  {'code': 'for value in countdown(3):\n    print(value)',
                   'prose': 'A `for` loop repeatedly calls `next()` for you. The loop stops when '
                            'the generator is exhausted.'},
                  {'code': 'def countdown_eager(n):\n'
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
                   'prose': '`return` builds the entire result before handing it back; `yield` '
                            'produces values on demand. The list keeps its values for repeated '
                            'use, while the generator is exhausted after one pass.'},
                  {'code': 'class Countdown:\n'
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
                   'prose': 'Every generator is an iterator. The same countdown written by hand '
                            'needs `__iter__` and `__next__` and an explicit `StopIteration`. The '
                            'generator function expresses the same protocol with one `yield`.'}]},
 {'cells': [{'code': 'def page():\n'
                     '    yield "header"\n'
                     '    yield from ["intro", "body"]\n'
                     '    yield "footer"\n'
                     '\n'
                     'print(list(page()))',
             'kind': 'cell',
             'line': 22,
             'output': "['header', 'intro', 'body', 'footer']",
             'prose': ['`yield from` delegates to another iterable. The caller receives one stream '
                       'even though part of it came from a list.']},
            {'code': 'def flatten(rows):\n'
                     '    for row in rows:\n'
                     '        yield from row\n'
                     '\n'
                     'print(list(flatten([[1, 2], [3]])))',
             'kind': 'cell',
             'line': 39,
             'output': '[1, 2, 3]',
             'prose': ['Delegation is useful when flattening nested iterables. `yield from row` '
                       'replaces an inner loop that would yield each item by hand.']}],
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
  'doc_path': '/reference/expressions.html#yield-expressions',
  'doc_url': 'https://docs.python.org/3.13/reference/expressions.html#yield-expressions',
  'expected_output': "['header', 'intro', 'body', 'footer']\n[1, 2, 3]\n",
  'explanation': ['`yield from` lets one generator yield every value from another iterable. It is '
                  'a compact way to delegate part of a stream.',
                  'Use it when a generator is mostly stitching together other iterables or '
                  'sub-generators. It keeps the producer pipeline visible without writing a nested '
                  '`for` loop.',
                  'The consumer still sees one stream of values.'],
  'min_python': None,
  'notes': ['`yield from iterable` yields each value from that iterable.',
            'It keeps generator pipelines compact.',
            'Use a plain `yield` when producing one value directly.'],
  'section': 'Iteration',
  'see_also': ['generators', 'generator-expressions', 'itertools'],
  'slug': 'yield-from',
  'summary': 'yield from delegates part of a generator to another iterable.',
  'title': 'Yield From',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def page():\n'
                           '    yield "header"\n'
                           '    yield from ["intro", "body"]\n'
                           '    yield "footer"\n'
                           '\n'
                           'print(list(page()))',
                   'prose': '`yield from` delegates to another iterable. The caller receives one '
                            'stream even though part of it came from a list.'},
                  {'code': 'def flatten(rows):\n'
                           '    for row in rows:\n'
                           '        yield from row\n'
                           '\n'
                           'print(list(flatten([[1, 2], [3]])))',
                   'prose': 'Delegation is useful when flattening nested iterables. `yield from '
                            'row` replaces an inner loop that would yield each item by hand.'}]},
 {'cells': [{'code': 'numbers = [1, 2, 3, 4]\n'
                     'list_squares = [number * number for number in numbers]\n'
                     'print(list_squares)',
             'kind': 'cell',
             'line': 17,
             'output': '[1, 4, 9, 16]',
             'prose': ['A list comprehension is eager: it builds a list immediately. That is '
                       'useful when you need to store or reuse the results.']},
            {'code': 'stream_squares = (number * number for number in numbers)\n'
                     'print(next(stream_squares))\n'
                     'print(next(stream_squares))\n'
                     'print(list(stream_squares))',
             'kind': 'cell',
             'line': 31,
             'output': '1\n4\n[9, 16]',
             'prose': ['A generator expression is lazy: it creates an iterator that produces '
                       'values as they are consumed. After two `next()` calls, only the remaining '
                       'squares are left.']},
            {'code': 'print(sum(number * number for number in numbers))',
             'kind': 'cell',
             'line': 48,
             'output': '30',
             'prose': ['Generator expressions are common inside reducing functions. When a '
                       'generator expression is the only argument, the extra parentheses can be '
                       'omitted.']}],
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
  'doc_path': '/tutorial/classes.html#generator-expressions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#generator-expressions',
  'expected_output': '[1, 4, 9, 16]\n1\n4\n[9, 16]\n30\n',
  'explanation': ['Generator expressions look like list comprehensions with parentheses, but they '
                  'produce an iterator instead of building a concrete collection immediately.',
                  'Use them when a consumer such as `sum()`, `any()`, or a `for` loop can use '
                  'values one at a time. This keeps the transformation close to the consumer and '
                  'avoids storing intermediate lists.',
                  'Like other iterators, a generator expression is consumed as values are '
                  'requested. Create a new generator expression when you need another pass.'],
  'min_python': None,
  'notes': ['List, dict, and set comprehensions build concrete collections.',
            'Generator expressions produce one-pass iterators.',
            'Use generator expressions when the consumer can process values one at a time.'],
  'section': 'Iteration',
  'see_also': [],
  'slug': 'generator-expressions',
  'summary': 'Generator expressions use comprehension-like syntax to stream values lazily.',
  'title': 'Generator Expressions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'numbers = [1, 2, 3, 4]\n'
                           'list_squares = [number * number for number in numbers]\n'
                           'print(list_squares)',
                   'prose': 'A list comprehension is eager: it builds a list immediately. That is '
                            'useful when you need to store or reuse the results.'},
                  {'code': 'stream_squares = (number * number for number in numbers)\n'
                           'print(next(stream_squares))\n'
                           'print(next(stream_squares))\n'
                           'print(list(stream_squares))',
                   'prose': 'A generator expression is lazy: it creates an iterator that produces '
                            'values as they are consumed. After two `next()` calls, only the '
                            'remaining squares are left.'},
                  {'code': 'print(sum(number * number for number in numbers))',
                   'prose': 'Generator expressions are common inside reducing functions. When a '
                            'generator expression is the only argument, the extra parentheses can '
                            'be omitted.'}]},
 {'cells': [{'code': 'import itertools\n'
                     '\n'
                     'counter = itertools.count(10)\n'
                     'print(list(itertools.islice(counter, 3)))',
             'kind': 'cell',
             'line': 17,
             'output': '[10, 11, 12]',
             'prose': ['`count()` can produce values forever, so `islice()` takes a finite window. '
                       'Nothing is materialized until `list()` consumes the iterator.']},
            {'code': 'pages = itertools.chain(["intro", "setup"], ["deploy"])\nprint(list(pages))',
             'kind': 'cell',
             'line': 32,
             'output': "['intro', 'setup', 'deploy']",
             'prose': ['`chain()` presents several iterables as one stream. This avoids building '
                       'an intermediate list just to loop over combined inputs.']},
            {'code': 'scores = [7, 10, 8, 10]\n'
                     'high_scores = itertools.compress(scores, [score >= 9 for score in scores])\n'
                     'print(list(high_scores))',
             'kind': 'cell',
             'line': 45,
             'output': '[10, 10]',
             'prose': ['Iterator helpers compose with ordinary Python expressions. `compress()` '
                       'keeps items whose corresponding selector is true.']}],
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
  'doc_path': '/library/itertools.html',
  'doc_url': 'https://docs.python.org/3.13/library/itertools.html',
  'expected_output': "[10, 11, 12]\n['intro', 'setup', 'deploy']\n[10, 10]\n",
  'explanation': ['The `itertools` module contains tools for composing iterator streams: '
                  'combining, slicing, grouping, and repeating values without changing the '
                  'consumer protocol.',
                  'Many `itertools` functions are lazy. They describe work to do later instead of '
                  'building a list immediately, so helpers such as `islice()` are useful when '
                  'taking a finite window.',
                  'Iterator pipelines let each step stay small: one object produces values, '
                  'another transforms them, and a final consumer such as `list()` or a loop pulls '
                  'values through the pipeline.'],
  'min_python': None,
  'notes': ['`itertools` composes producer and transformer streams.',
            'Iterator pipelines avoid building intermediate lists.',
            'Use `islice()` to take a finite piece from an infinite iterator.',
            'Convert to a list only when you need concrete results.'],
  'section': 'Iteration',
  'see_also': [],
  'slug': 'itertools',
  'summary': 'itertools composes lazy iterator streams.',
  'title': 'Itertools',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import itertools\n'
                           '\n'
                           'counter = itertools.count(10)\n'
                           'print(list(itertools.islice(counter, 3)))',
                   'prose': '`count()` can produce values forever, so `islice()` takes a finite '
                            'window. Nothing is materialized until `list()` consumes the '
                            'iterator.'},
                  {'code': 'pages = itertools.chain(["intro", "setup"], ["deploy"])\n'
                           'print(list(pages))',
                   'prose': '`chain()` presents several iterables as one stream. This avoids '
                            'building an intermediate list just to loop over combined inputs.'},
                  {'code': 'scores = [7, 10, 8, 10]\n'
                           'high_scores = itertools.compress(scores, [score >= 9 for score in '
                           'scores])\n'
                           'print(list(high_scores))',
                   'prose': 'Iterator helpers compose with ordinary Python expressions. '
                            '`compress()` keeps items whose corresponding selector is true.'}]},
 {'cells': [{'code': 'from functools import wraps\n'
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
             'kind': 'cell',
             'line': 23,
             'output': 'HELLO PYTHON',
             'prose': ['A decorator is just a function that takes a function and returns another '
                       'callable. Applying it manually shows the wrapping step.']},
            {'code': '@loud\n'
                     'def welcome(name):\n'
                     '    """Return a welcome message."""\n'
                     '    return f"welcome {name}"\n'
                     '\n'
                     'print(welcome("workers"))',
             'kind': 'cell',
             'line': 49,
             'output': 'WELCOME WORKERS',
             'prose': ['The `@loud` syntax performs the same rebinding at definition time. After '
                       'decoration, `welcome` refers to the wrapper returned by `loud`.']},
            {'code': 'print(welcome.__name__)\nprint(welcome.__doc__)',
             'kind': 'cell',
             'line': 66,
             'output': 'welcome\nReturn a welcome message.',
             'prose': ['`functools.wraps` copies useful metadata from the original function onto '
                       'the wrapper.']}],
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
  'doc_path': '/glossary.html#term-decorator',
  'doc_url': 'https://docs.python.org/3.13/glossary.html#term-decorator',
  'expected_output': 'HELLO PYTHON\nWELCOME WORKERS\nwelcome\n',
  'explanation': ['A decorator is a callable that receives a function and returns a replacement. '
                  'The `@` syntax applies that transformation at function definition time.',
                  'Decorators are common in frameworks because they can register handlers or add '
                  'behavior while keeping the decorated function focused on the core action.',
                  "`@decorator` is shorthand for rebinding a function to the decorator's return "
                  'value. Production wrappers usually use `functools.wraps` so debugging, help '
                  'text, and framework introspection still see the original function metadata.'],
  'min_python': None,
  'notes': ['`@decorator` is shorthand for assigning `func = decorator(func)`.',
            'Decorators can wrap, replace, or register functions.',
            'Use `functools.wraps` in production wrappers that should preserve metadata.'],
  'section': 'Functions',
  'see_also': ['closures', 'functions', 'callable-types', 'classmethods-and-staticmethods'],
  'slug': 'decorators',
  'summary': 'Decorators wrap or register functions using @ syntax.',
  'title': 'Decorators',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from functools import wraps\n'
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
                   'prose': 'A decorator is just a function that takes a function and returns '
                            'another callable. Applying it manually shows the wrapping step.'},
                  {'code': '@loud\n'
                           'def welcome(name):\n'
                           '    """Return a welcome message."""\n'
                           '    return f"welcome {name}"\n'
                           '\n'
                           'print(welcome("workers"))',
                   'prose': 'The `@loud` syntax performs the same rebinding at definition time. '
                            'After decoration, `welcome` refers to the wrapper returned by '
                            '`loud`.'},
                  {'code': 'print(welcome.__name__)\nprint(welcome.__doc__)',
                   'prose': '`functools.wraps` copies useful metadata from the original function '
                            'onto the wrapper.'}]},
 {'cells': [{'code': 'class Counter:\n'
                     '    def __init__(self, start=0):\n'
                     '        self.value = start\n'
                     '\n'
                     'first = Counter()\n'
                     'second = Counter(10)\n'
                     'print(first.value)\n'
                     'print(second.value)',
             'kind': 'cell',
             'line': 23,
             'output': '0\n10',
             'prose': ['Define a class when data and behavior should travel together. The '
                       'initializer gives each object its starting state.']},
            {'code': 'class Counter:\n'
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
             'kind': 'cell',
             'line': 43,
             'output': '1\n15',
             'prose': ['Methods are functions attached to the class. `self` is the particular '
                       'object receiving the method call, so separate instances keep separate '
                       'state.']},
            {'code': 'class Counter:\n'
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
             'kind': 'cell',
             'line': 67,
             'output': '1\n5',
             'prose': ['A name defined directly on the class body is a class attribute, shared by '
                       'every instance. Reading falls back to the class when the instance has no '
                       'attribute of that name; assigning to the class itself changes the value '
                       'for every instance at once.']},
            {'code': 'class Cart:\n'
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
             'kind': 'cell',
             'line': 90,
             'output': "['apple']\n[]",
             'prose': ['A mutable class attribute is shared mutable state — the classic footgun. '
                       'Define per-instance containers in `__init__` so each object owns its own '
                       'copy.']}],
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
  'doc_path': '/tutorial/classes.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html',
  'expected_output': "0\n10\n1\n15\n1\n5\n['apple']\n[]\n",
  'explanation': ['Classes define new object types by bundling data with behavior. They are useful '
                  'when several values and operations belong together and should travel as one '
                  'object.',
                  'The alternative is often a dictionary plus separate functions. That is fine for '
                  'loose data, but a class gives the data a stable API and keeps behavior next to '
                  'the state it changes.',
                  '`__init__` initializes each instance, and methods receive the instance as '
                  '`self`. Separate instances keep separate state because each object has its own '
                  'attributes.'],
  'min_python': None,
  'notes': ['`self` is the instance the method is operating on.',
            '`__init__` initializes each new object.',
            'Class attributes are shared across instances; instance attributes belong to one '
            'object.',
            'Put mutable defaults in `__init__`, not on the class body.',
            'Use classes when behavior belongs with state; use dictionaries for looser structured '
            'data.'],
  'section': 'Classes',
  'see_also': ['inheritance-and-super',
               'classmethods-and-staticmethods',
               'bound-and-unbound-methods',
               'dataclasses'],
  'slug': 'classes',
  'summary': 'Classes bundle data and behavior into new object types.',
  'title': 'Classes',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Counter:\n'
                           '    def __init__(self, start=0):\n'
                           '        self.value = start\n'
                           '\n'
                           'first = Counter()\n'
                           'second = Counter(10)\n'
                           'print(first.value)\n'
                           'print(second.value)',
                   'prose': 'Define a class when data and behavior should travel together. The '
                            'initializer gives each object its starting state.'},
                  {'code': 'class Counter:\n'
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
                   'prose': 'Methods are functions attached to the class. `self` is the particular '
                            'object receiving the method call, so separate instances keep separate '
                            'state.'},
                  {'code': 'class Counter:\n'
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
                   'prose': 'A name defined directly on the class body is a class attribute, '
                            'shared by every instance. Reading falls back to the class when the '
                            'instance has no attribute of that name; assigning to the class itself '
                            'changes the value for every instance at once.'},
                  {'code': 'class Cart:\n'
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
                   'prose': 'A mutable class attribute is shared mutable state — the classic '
                            'footgun. Define per-instance containers in `__init__` so each object '
                            'owns its own copy.'}]},
 {'cells': [{'code': 'class Animal:\n'
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
             'kind': 'cell',
             'line': 23,
             'output': 'Nina',
             'prose': ['A child class names its parent in parentheses. `Dog` instances get the '
                       '`Animal.__init__` method because `Dog` does not define its own '
                       'initializer.']},
            {'code': 'print(pet.speak())\nprint(isinstance(pet, Animal))',
             'kind': 'cell',
             'line': 48,
             'output': 'Nina makes a sound; Nina barks\nTrue',
             'prose': ['`super()` delegates to the parent implementation. The child method can '
                       'reuse the parent result and then add specialized behavior.']}],
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
  'doc_path': '/tutorial/classes.html#inheritance',
  'doc_url': 'https://docs.python.org/3.13/tutorial/classes.html#inheritance',
  'expected_output': 'Nina\nNina makes a sound; Nina barks\nTrue\n',
  'explanation': ['Inheritance lets one class specialize another class. The child class gets '
                  'parent behavior and can add or override methods.',
                  'Use `super()` when the child method should extend the parent implementation '
                  'instead of replacing it entirely.',
                  'Prefer composition when objects merely collaborate. Inheritance is best when '
                  'the child really is a specialized version of the parent.'],
  'min_python': None,
  'notes': ['Inheritance models an “is a specialized kind of” relationship.',
            '`super()` calls the next implementation in the method resolution order.',
            'Prefer composition when an object only needs to use another object.'],
  'section': 'Classes',
  'see_also': ['classes',
               'abstract-base-classes',
               'classmethods-and-staticmethods',
               'special-methods'],
  'slug': 'inheritance-and-super',
  'summary': 'Inheritance reuses behavior, and super delegates to a parent implementation.',
  'title': 'Inheritance and Super',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Animal:\n'
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
                   'prose': 'A child class names its parent in parentheses. `Dog` instances get '
                            'the `Animal.__init__` method because `Dog` does not define its own '
                            'initializer.'},
                  {'code': 'print(pet.speak())\nprint(isinstance(pet, Animal))',
                   'prose': '`super()` delegates to the parent implementation. The child method '
                            'can reuse the parent result and then add specialized behavior.'}]},
 {'cells': [{'code': 'class Date:\n'
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
             'kind': 'cell',
             'line': 22,
             'output': '2026-05-09',
             'prose': ['An instance method receives the instance as `self` and reads its state. '
                       'This is the default and the right shape when the work depends on a '
                       "particular object's data."]},
            {'code': 'class Date:\n'
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
             'kind': 'cell',
             'line': 44,
             'output': '2026 12 31',
             'prose': ['`@classmethod` makes the method receive the class itself as `cls`. The '
                       'canonical use is an alternate constructor that parses some other input '
                       'format and calls `cls(...)`. Because `cls` is the actual class, subclasses '
                       'calling the same method get an instance of their own type.']},
            {'code': 'class Date:\n'
                     '    @staticmethod\n'
                     '    def is_leap_year(year):\n'
                     '        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)\n'
                     '\n'
                     'print(Date.is_leap_year(2024))\n'
                     'print(Date.is_leap_year(2025))',
             'kind': 'cell',
             'line': 68,
             'output': 'True\nFalse',
             'prose': ['`@staticmethod` strips the implicit first argument. The function lives on '
                       'the class for namespacing — like `Date.is_leap_year(2024)` — but does not '
                       'touch any instance or class state.']},
            {'code': 'class Demo:\n'
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
             'kind': 'cell',
             'line': 87,
             'output': 'Demo\nDemo\nno receiver',
             'prose': ['Side by side: instance methods receive the instance, classmethods receive '
                       'the class, staticmethods receive nothing. Classmethods and staticmethods '
                       'can be called on either the class or an instance.']}],
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
  'doc_path': '/library/functions.html#classmethod',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#classmethod',
  'expected_output': '2026-05-09\n2026-12-31\nTrue\nFalse\nDemo\nDemo\nno receiver\n',
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
  'min_python': None,
  'notes': ['Instance methods need an instance; classmethods and staticmethods can be called on '
            'the class.',
            'Use `@classmethod` for alternate constructors and class-level operations that respect '
            'subclassing.',
            'Use `@staticmethod` only when a function is truly independent of instance and class '
            "state but still belongs in the class's namespace.",
            'A free function is often the right answer when neither decorator applies.'],
  'section': 'Classes',
  'see_also': ['classes', 'decorators', 'inheritance-and-super'],
  'slug': 'classmethods-and-staticmethods',
  'summary': 'Three method shapes: instance, class, and static — each receives a different first '
             'argument.',
  'title': 'Classmethods and Staticmethods',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Date:\n'
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
                   'prose': 'An instance method receives the instance as `self` and reads its '
                            'state. This is the default and the right shape when the work depends '
                            "on a particular object's data."},
                  {'code': 'class Date:\n'
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
                   'prose': '`@classmethod` makes the method receive the class itself as `cls`. '
                            'The canonical use is an alternate constructor that parses some other '
                            'input format and calls `cls(...)`. Because `cls` is the actual class, '
                            'subclasses calling the same method get an instance of their own '
                            'type.'},
                  {'code': 'class Date:\n'
                           '    @staticmethod\n'
                           '    def is_leap_year(year):\n'
                           '        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)\n'
                           '\n'
                           'print(Date.is_leap_year(2024))\n'
                           'print(Date.is_leap_year(2025))',
                   'prose': '`@staticmethod` strips the implicit first argument. The function '
                            'lives on the class for namespacing — like `Date.is_leap_year(2024)` — '
                            'but does not touch any instance or class state.'},
                  {'code': 'class Demo:\n'
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
                   'prose': 'Side by side: instance methods receive the instance, classmethods '
                            'receive the class, staticmethods receive nothing. Classmethods and '
                            'staticmethods can be called on either the class or an instance.'}]},
 {'cells': [{'code': 'from dataclasses import dataclass\n'
                     '\n'
                     '@dataclass\n'
                     'class User:\n'
                     '    name: str\n'
                     '    active: bool = True\n'
                     '\n'
                     'user = User("Ada")\n'
                     'print(user)',
             'kind': 'cell',
             'line': 22,
             'output': "User(name='Ada', active=True)",
             'prose': ['A dataclass uses annotations to define fields. Python generates an '
                       'initializer, so the class can be constructed without writing `__init__` by '
                       'hand.']},
            {'code': 'print(user.name)',
             'kind': 'cell',
             'line': 42,
             'output': 'Ada',
             'prose': ['The generated instance still exposes ordinary attributes. A dataclass is a '
                       'regular class with useful methods filled in.']},
            {'code': 'inactive = User("Guido", active=False)\n'
                     'print(inactive)\n'
                     'print(inactive.active)',
             'kind': 'cell',
             'line': 54,
             'output': "User(name='Guido', active=False)\nFalse",
             'prose': ['Defaults can be overridden by keyword. The generated representation '
                       'includes the field names, which is useful during debugging.']}],
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
  'doc_path': '/library/dataclasses.html',
  'doc_url': 'https://docs.python.org/3.13/library/dataclasses.html',
  'expected_output': "User(name='Ada', active=True)\n"
                     'Ada\n'
                     "User(name='Guido', active=False)\n"
                     'False\n',
  'explanation': ['`dataclass` is a standard-library decorator for classes that mainly store data. '
                  'It generates methods such as `__init__` and `__repr__` from type-annotated '
                  'fields.',
                  'Dataclasses reduce boilerplate while keeping classes explicit. They are a good '
                  'fit for simple records, configuration objects, and values passed between '
                  'layers.',
                  'Type annotations define fields. Defaults work like normal class attributes and '
                  'appear in the generated initializer.'],
  'min_python': None,
  'notes': ['Type annotations define dataclass fields.',
            'Dataclasses generate methods but remain normal Python classes.',
            'Use `field()` for advanced defaults such as per-instance lists or dictionaries.'],
  'section': 'Classes',
  'see_also': ['structured-data-shapes', 'classes', 'type-hints'],
  'slug': 'dataclasses',
  'summary': 'dataclass generates common class methods for data containers.',
  'title': 'Dataclasses',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from dataclasses import dataclass\n'
                           '\n'
                           '@dataclass\n'
                           'class User:\n'
                           '    name: str\n'
                           '    active: bool = True\n'
                           '\n'
                           'user = User("Ada")\n'
                           'print(user)',
                   'prose': 'A dataclass uses annotations to define fields. Python generates an '
                            'initializer, so the class can be constructed without writing '
                            '`__init__` by hand.'},
                  {'code': 'print(user.name)',
                   'prose': 'The generated instance still exposes ordinary attributes. A dataclass '
                            'is a regular class with useful methods filled in.'},
                  {'code': 'inactive = User("Guido", active=False)\n'
                           'print(inactive)\n'
                           'print(inactive.active)',
                   'prose': 'Defaults can be overridden by keyword. The generated representation '
                            'includes the field names, which is useful during debugging.'}]},
 {'cells': [{'code': 'class Rectangle:\n'
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
             'kind': 'cell',
             'line': 17,
             'output': '12',
             'prose': ['A read-only property exposes computed data through attribute access. '
                       '`area` stays current because it is calculated from `width` and `height` '
                       'each time it is read.']},
            {'code': 'box.width = 5\nprint(box.area)',
             'kind': 'cell',
             'line': 49,
             'output': '20',
             'prose': ['A setter lets assignment keep normal attribute syntax while the class '
                       'validates or normalizes the value.']},
            {'code': 'try:\n    box.width = 0\nexcept ValueError as error:\n    print(error)',
             'kind': 'cell',
             'line': 62,
             'output': 'width must be positive',
             'prose': ['Validation belongs inside the class when every caller should obey the same '
                       'rule. Invalid assignment raises an exception at the boundary.']}],
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
  'doc_path': '/library/functions.html#property',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#property',
  'expected_output': '12\n20\nwidth must be positive\n',
  'explanation': ['Properties let a class keep a simple attribute-style API while running code '
                  'behind the scenes. Callers write `box.area`, but the class can compute the '
                  'value from current state.',
                  'A property setter can validate assignment without changing the public spelling '
                  'of the attribute. This is the boundary: plain attributes are enough for plain '
                  'data, while properties are for computed or protected data.',
                  'Use properties for cheap, attribute-like operations. Expensive work or actions '
                  'with side effects should usually remain explicit methods.'],
  'min_python': None,
  'notes': ['Properties let APIs start simple and grow validation or computation later.',
            'Callers access a property like an attribute, not like a method.',
            'Use methods instead when work is expensive or action-like.'],
  'section': 'Classes',
  'see_also': [],
  'slug': 'properties',
  'summary': '@property keeps attribute syntax while adding computation or validation.',
  'title': 'Properties',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Rectangle:\n'
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
                   'prose': 'A read-only property exposes computed data through attribute access. '
                            '`area` stays current because it is calculated from `width` and '
                            '`height` each time it is read.'},
                  {'code': 'box.width = 5\nprint(box.area)',
                   'prose': 'A setter lets assignment keep normal attribute syntax while the class '
                            'validates or normalizes the value.'},
                  {'code': 'try:\n    box.width = 0\nexcept ValueError as error:\n    print(error)',
                   'prose': 'Validation belongs inside the class when every caller should obey the '
                            'same rule. Invalid assignment raises an exception at the boundary.'}]},
 {'cells': [{'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(bag.items)',
             'kind': 'cell',
             'line': 23,
             'output': "['a', 'b']",
             'prose': ['Start with a normal class that stores its data. Special methods build on '
                       'ordinary instance state.']},
            {'code': 'class Bag:\n'
                     '    def __init__(self, items):\n'
                     '        self.items = list(items)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.items)\n'
                     '\n'
                     'bag = Bag(["a", "b"])\n'
                     'print(len(bag))',
             'kind': 'cell',
             'line': 40,
             'output': '2',
             'prose': ['Implement `__len__` to let `len()` ask the object for its size using '
                       "Python's standard protocol."]},
            {'code': 'class Bag:\n'
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
             'kind': 'cell',
             'line': 60,
             'output': "['a', 'b']",
             'prose': ['Implement `__iter__` to make the object iterable. Then tools such as '
                       '`list()` can consume it without a custom method name.']},
            {'code': 'class Bag:\n'
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
             'kind': 'cell',
             'line': 83,
             'output': "Bag(['a', 'b'])",
             'prose': ['Implement `__repr__` to give the object a useful developer-facing '
                       'representation when it is printed or inspected. With no `__str__` defined, '
                       '`print()` falls back to `__repr__`.']},
            {'code': 'class Bag:\n'
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
             'kind': 'cell',
             'line': 109,
             'output': "a, b\nBag(['a', 'b'])",
             'prose': ['Add `__str__` for an end-user representation. `print()` and `str()` prefer '
                       '`__str__`; `repr()` and the REPL still use `__repr__`. Keep `__repr__` '
                       'unambiguous for debugging and let `__str__` be the friendly form.']},
            {'code': 'class Bag:\n'
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
             'kind': 'cell',
             'line': 134,
             'output': 'True\nTrue\nTrue',
             'prose': ['`__eq__` decides what equality means for the type. Defining `__eq__` '
                       'removes the default `__hash__`, so add `__hash__` back when instances '
                       'should work in sets or as dict keys. `__lt__` enables `<` and, with the '
                       'rest of the order family, `sorted()`.']},
            {'code': 'class Bag:\n'
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
             'kind': 'cell',
             'line': 163,
             'output': "True\na\n['a', 'z']\nFalse",
             'prose': ['The container protocols make instances behave like built-in containers. '
                       '`__contains__` powers `in`, `__getitem__`/`__setitem__` power '
                       'subscription, and `__bool__` decides truthiness for `if` and `while`. See '
                       '[container-protocols](/data-model/container-protocols) for the full '
                       'surface.']},
            {'code': 'class Multiplier:\n'
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
             'kind': 'cell',
             'line': 199,
             'output': '15\nenter\ninside\nexit',
             'prose': ['`__call__` makes an instance callable like a function — useful for '
                       'stateful operations whose configuration deserves a name. `__enter__` and '
                       '`__exit__` make a class a context manager so it can be used with `with`. '
                       'The focused [callable-objects](/data-model/callable-objects) and '
                       '[context-managers](/data-model/context-managers) pages go deeper.']}],
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
  'doc_path': '/reference/datamodel.html#special-method-names',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#special-method-names',
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
                     'exit\n',
  'explanation': ['Special methods, often called dunder methods, connect user-defined classes to '
                  'Python syntax and built-ins such as len(), iter(), and repr().',
                  'Implementing these methods lets your objects participate in Python protocols '
                  'rather than forcing callers to learn custom method names for common operations.',
                  'Good special methods make objects feel boring in the best way: they work with '
                  'the language features Python programmers already know.'],
  'min_python': None,
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
  'section': 'Data Model',
  'see_also': ['container-protocols',
               'operator-overloading',
               'callable-objects',
               'context-managers'],
  'slug': 'special-methods',
  'summary': 'Special methods connect your objects to Python syntax and built-ins.',
  'title': 'Special Methods',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Bag:\n'
                           '    def __init__(self, items):\n'
                           '        self.items = list(items)\n'
                           '\n'
                           'bag = Bag(["a", "b"])\n'
                           'print(bag.items)',
                   'prose': 'Start with a normal class that stores its data. Special methods build '
                            'on ordinary instance state.'},
                  {'code': 'class Bag:\n'
                           '    def __init__(self, items):\n'
                           '        self.items = list(items)\n'
                           '\n'
                           '    def __len__(self):\n'
                           '        return len(self.items)\n'
                           '\n'
                           'bag = Bag(["a", "b"])\n'
                           'print(len(bag))',
                   'prose': 'Implement `__len__` to let `len()` ask the object for its size using '
                            "Python's standard protocol."},
                  {'code': 'class Bag:\n'
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
                   'prose': 'Implement `__iter__` to make the object iterable. Then tools such as '
                            '`list()` can consume it without a custom method name.'},
                  {'code': 'class Bag:\n'
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
                   'prose': 'Implement `__repr__` to give the object a useful developer-facing '
                            'representation when it is printed or inspected. With no `__str__` '
                            'defined, `print()` falls back to `__repr__`.'},
                  {'code': 'class Bag:\n'
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
                   'prose': 'Add `__str__` for an end-user representation. `print()` and `str()` '
                            'prefer `__str__`; `repr()` and the REPL still use `__repr__`. Keep '
                            '`__repr__` unambiguous for debugging and let `__str__` be the '
                            'friendly form.'},
                  {'code': 'class Bag:\n'
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
                   'prose': '`__eq__` decides what equality means for the type. Defining `__eq__` '
                            'removes the default `__hash__`, so add `__hash__` back when instances '
                            'should work in sets or as dict keys. `__lt__` enables `<` and, with '
                            'the rest of the order family, `sorted()`.'},
                  {'code': 'class Bag:\n'
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
                   'prose': 'The container protocols make instances behave like built-in '
                            'containers. `__contains__` powers `in`, `__getitem__`/`__setitem__` '
                            'power subscription, and `__bool__` decides truthiness for `if` and '
                            '`while`. See [container-protocols](/data-model/container-protocols) '
                            'for the full surface.'},
                  {'code': 'class Multiplier:\n'
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
                   'prose': '`__call__` makes an instance callable like a function — useful for '
                            'stateful operations whose configuration deserves a name. `__enter__` '
                            'and `__exit__` make a class a context manager so it can be used with '
                            '`with`. The focused [callable-objects](/data-model/callable-objects) '
                            'and [context-managers](/data-model/context-managers) pages go '
                            'deeper.'}]},
 {'cells': [{'code': 'class Inbox:\n'
                     '    def __init__(self, messages):\n'
                     '        self.messages = list(messages)\n'
                     '\n'
                     '    def __len__(self):\n'
                     '        return len(self.messages)\n'
                     '\n'
                     'print(len(Inbox(["hi", "bye"])))',
             'kind': 'cell',
             'line': 22,
             'output': '2',
             'prose': ['`__len__` lets `len()` ask an object for its size.']},
            {'code': 'print(bool(Inbox([])))',
             'kind': 'cell',
             'line': 41,
             'output': 'False',
             'prose': ['If a class has `__len__` but no `__bool__`, Python uses zero length as '
                       'false.']},
            {'code': 'class Account:\n'
                     '    def __init__(self, active):\n'
                     '        self.active = active\n'
                     '\n'
                     '    def __bool__(self):\n'
                     '        return self.active\n'
                     '\n'
                     'print(bool(Account(False)))',
             'kind': 'cell',
             'line': 53,
             'output': 'False',
             'prose': ['`__bool__` expresses truth directly when the answer is not just container '
                       'size.']}],
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
  'doc_path': '/reference/datamodel.html#object.__bool__',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#object.__bool__',
  'expected_output': '2\nFalse\nFalse\n',
  'explanation': ['Truth tests ask an object whether it should count as true. Containers usually '
                  'answer through their size, while domain objects can answer with `__bool__` when '
                  'emptiness is not the right idea.',
                  '`__len__` supports `len(obj)` and also provides a fallback truth value: length '
                  'zero is false, non-zero length is true. `__bool__` is more direct and wins when '
                  'both are present.',
                  'Use these methods to match the meaning of your object. A queue can be false '
                  'when it has no items; an account might be true only when it is active, '
                  'regardless of its balance.'],
  'min_python': None,
  'notes': ['Prefer `__len__` for sized containers.',
            'Prefer `__bool__` when truth has domain meaning.',
            'Keep truth tests unsurprising; surprising falsy objects make conditionals harder to '
            'read.'],
  'section': 'Data Model',
  'see_also': ['truthiness', 'special-methods', 'container-protocols'],
  'slug': 'truth-and-size',
  'summary': '__bool__ and __len__ decide how objects behave in truth tests and len().',
  'title': 'Truth and Size',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Inbox:\n'
                           '    def __init__(self, messages):\n'
                           '        self.messages = list(messages)\n'
                           '\n'
                           '    def __len__(self):\n'
                           '        return len(self.messages)\n'
                           '\n'
                           'print(len(Inbox(["hi", "bye"])))',
                   'prose': '`__len__` lets `len()` ask an object for its size.'},
                  {'code': 'print(bool(Inbox([])))',
                   'prose': 'If a class has `__len__` but no `__bool__`, Python uses zero length '
                            'as false.'},
                  {'code': 'class Account:\n'
                           '    def __init__(self, active):\n'
                           '        self.active = active\n'
                           '\n'
                           '    def __bool__(self):\n'
                           '        return self.active\n'
                           '\n'
                           'print(bool(Account(False)))',
                   'prose': '`__bool__` expresses truth directly when the answer is not just '
                            'container size.'}]},
 {'cells': [{'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {}\n'
                     '\n'
                     '    def __setitem__(self, name, score):\n'
                     '        self._scores[name] = score\n'
                     '\n'
                     'scores = Scores()\n'
                     'scores["Ada"] = 98\n'
                     'print(scores._scores)',
             'kind': 'cell',
             'line': 22,
             'output': "{'Ada': 98}",
             'prose': ['`__setitem__` gives assignment syntax to a custom container.']},
            {'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {"Ada": 98}\n'
                     '\n'
                     '    def __contains__(self, name):\n'
                     '        return name in self._scores\n'
                     '\n'
                     'scores = Scores()\n'
                     'print("Ada" in scores)',
             'kind': 'cell',
             'line': 43,
             'output': 'True',
             'prose': ['`__contains__` answers membership tests written with `in`.']},
            {'code': 'class Scores:\n'
                     '    def __init__(self):\n'
                     '        self._scores = {"Ada": 98}\n'
                     '\n'
                     '    def __getitem__(self, name):\n'
                     '        return self._scores[name]\n'
                     '\n'
                     'scores = Scores()\n'
                     'print(scores["Ada"])',
             'kind': 'cell',
             'line': 63,
             'output': '98',
             'prose': ['`__getitem__` connects bracket lookup to your internal storage.']}],
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
  'doc_path': '/reference/datamodel.html#emulating-container-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#emulating-container-types',
  'expected_output': 'True\n98\n',
  'explanation': ['Container protocols let a class behave like the collection it represents. '
                  'Instead of inventing method names such as `has()` or `lookup()`, the object can '
                  'support `in`, indexing, and assignment.',
                  'The key methods are small and familiar: `__contains__` powers `in`, '
                  '`__getitem__` powers `obj[key]`, and `__setitem__` powers `obj[key] = value`. '
                  'Add only the operations the object can honestly support.',
                  "This keeps the public interface aligned with Python's built-in containers. "
                  'Callers can use the same syntax for custom records, caches, tables, and '
                  'sequence-like objects.'],
  'min_python': None,
  'notes': ['Implement the narrowest container protocol your object needs.',
            'Use `KeyError` and `IndexError` consistently with built-in containers.',
            'If a plain `dict` or `list` is enough, prefer it over a custom container.'],
  'section': 'Data Model',
  'see_also': ['lists', 'dicts', 'special-methods'],
  'slug': 'container-protocols',
  'summary': 'Container methods connect objects to indexing, membership, and item assignment.',
  'title': 'Container Protocols',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Scores:\n'
                           '    def __init__(self):\n'
                           '        self._scores = {}\n'
                           '\n'
                           '    def __setitem__(self, name, score):\n'
                           '        self._scores[name] = score\n'
                           '\n'
                           'scores = Scores()\n'
                           'scores["Ada"] = 98\n'
                           'print(scores._scores)',
                   'prose': '`__setitem__` gives assignment syntax to a custom container.'},
                  {'code': 'class Scores:\n'
                           '    def __init__(self):\n'
                           '        self._scores = {"Ada": 98}\n'
                           '\n'
                           '    def __contains__(self, name):\n'
                           '        return name in self._scores\n'
                           '\n'
                           'scores = Scores()\n'
                           'print("Ada" in scores)',
                   'prose': '`__contains__` answers membership tests written with `in`.'},
                  {'code': 'class Scores:\n'
                           '    def __init__(self):\n'
                           '        self._scores = {"Ada": 98}\n'
                           '\n'
                           '    def __getitem__(self, name):\n'
                           '        return self._scores[name]\n'
                           '\n'
                           'scores = Scores()\n'
                           'print(scores["Ada"])',
                   'prose': '`__getitem__` connects bracket lookup to your internal storage.'}]},
 {'cells': [{'code': 'class Multiplier:\n'
                     '    def __init__(self, factor):\n'
                     '        self.factor = factor\n'
                     '        self.calls = 0\n'
                     '\n'
                     'double = Multiplier(2)\n'
                     'print(double.factor)',
             'kind': 'cell',
             'line': 23,
             'output': '2',
             'prose': ['A callable object starts as ordinary state stored on an instance.']},
            {'code': 'class Multiplier:\n'
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
             'kind': 'cell',
             'line': 41,
             'output': '10\n14',
             'prose': ['`__call__` makes the instance usable with function-call syntax.']},
            {'code': 'print(double.calls)',
             'kind': 'cell',
             'line': 65,
             'output': '2',
             'prose': ['Because the callable is still an object, it can remember state across '
                       'calls.']}],
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
  'doc_path': '/reference/datamodel.html#object.__call__',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#object.__call__',
  'expected_output': '10\n14\n2\n',
  'explanation': ['Functions are not the only callable objects in Python. Any instance can be '
                  'called with parentheses when its class defines `__call__`.',
                  'Callable objects are useful when behavior needs remembered configuration or '
                  'evolving state. A closure can do this too; a class is often clearer when the '
                  'state has multiple fields or needs named methods.',
                  'The tradeoff is ceremony. Use a function for simple behavior, a closure for '
                  'small captured state, and a callable object when naming the state improves the '
                  'interface.'],
  'min_python': None,
  'notes': ['`callable(obj)` checks whether an object can be called.',
            'Callable objects are good for named, stateful behavior.',
            'Prefer plain functions when no instance state is needed.'],
  'section': 'Data Model',
  'see_also': ['functions', 'closures', 'callable-types', 'bound-and-unbound-methods'],
  'slug': 'callable-objects',
  'summary': '__call__ lets an instance behave like a function while keeping state.',
  'title': 'Callable Objects',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Multiplier:\n'
                           '    def __init__(self, factor):\n'
                           '        self.factor = factor\n'
                           '        self.calls = 0\n'
                           '\n'
                           'double = Multiplier(2)\n'
                           'print(double.factor)',
                   'prose': 'A callable object starts as ordinary state stored on an instance.'},
                  {'code': 'class Multiplier:\n'
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
                   'prose': '`__call__` makes the instance usable with function-call syntax.'},
                  {'code': 'print(double.calls)',
                   'prose': 'Because the callable is still an object, it can remember state across '
                            'calls.'}]},
 {'cells': [{'code': 'class Vector:\n'
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
             'kind': 'cell',
             'line': 22,
             'output': 'Vector(6, 8)',
             'prose': ['`__add__` defines how the `+` operator combines two objects.']},
            {'code': 'class Vector:\n'
                     '    def __init__(self, x, y):\n'
                     '        self.x = x\n'
                     '        self.y = y\n'
                     '\n'
                     '    def __eq__(self, other):\n'
                     '        return (self.x, self.y) == (other.x, other.y)\n'
                     '\n'
                     'print(Vector(1, 1) == Vector(1, 1))',
             'kind': 'cell',
             'line': 45,
             'output': 'True',
             'prose': ['`__eq__` defines value equality for `==`. Without it, user-defined objects '
                       'compare by identity.']},
            {'code': 'class Vector:\n'
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
             'kind': 'cell',
             'line': 65,
             'output': 'Vector(6, 8)',
             'prose': ['A useful `__repr__` makes operator results inspectable while debugging.']}],
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
  'doc_path': '/reference/datamodel.html#emulating-numeric-types',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#emulating-numeric-types',
  'expected_output': 'Vector(6, 8)\nTrue\n',
  'explanation': ['Operator overloading lets a class define what expressions such as `a + b` mean '
                  'for its objects. This is useful when the operation is part of the domain '
                  'vocabulary.',
                  'The method should preserve the meaning readers expect from the operator. '
                  'Vectors can add component by component; money can add amounts in the same '
                  'currency; surprising overloads make code harder to trust.',
                  'Python also has reflected methods such as `__radd__` for cases where the left '
                  'operand does not know how to handle the right operand. That keeps mixed '
                  'operations possible without making every type know every other type.'],
  'min_python': None,
  'notes': ['Overload operators only when the operation is unsurprising.',
            'Return `NotImplemented` when an operand type is unsupported.',
            'Implement equality deliberately when value comparison matters.'],
  'section': 'Data Model',
  'see_also': ['operators', 'special-methods', 'equality-and-identity'],
  'slug': 'operator-overloading',
  'summary': 'Operator methods let objects define arithmetic and comparison syntax.',
  'title': 'Operator Overloading',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Vector:\n'
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
                   'prose': '`__add__` defines how the `+` operator combines two objects.'},
                  {'code': 'class Vector:\n'
                           '    def __init__(self, x, y):\n'
                           '        self.x = x\n'
                           '        self.y = y\n'
                           '\n'
                           '    def __eq__(self, other):\n'
                           '        return (self.x, self.y) == (other.x, other.y)\n'
                           '\n'
                           'print(Vector(1, 1) == Vector(1, 1))',
                   'prose': '`__eq__` defines value equality for `==`. Without it, user-defined '
                            'objects compare by identity.'},
                  {'code': 'class Vector:\n'
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
                   'prose': 'A useful `__repr__` makes operator results inspectable while '
                            'debugging.'}]},
 {'cells': [{'code': 'class Settings:\n'
                     '    def __init__(self, values):\n'
                     '        self._values = dict(values)\n'
                     '\n'
                     'settings = Settings({"theme": "dark"})\n'
                     'print(settings._values)',
             'kind': 'cell',
             'line': 23,
             'output': "{'theme': 'dark'}",
             'prose': ['Normal initialization still needs to set real attributes. Calling '
                       '`object.__setattr__` avoids recursing through your own hook.']},
            {'code': 'class Settings:\n'
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
             'kind': 'cell',
             'line': 40,
             'output': 'dark',
             'prose': ['`__getattr__` runs only for missing attributes, so it can provide fallback '
                       'lookup.']},
            {'code': 'class Settings:\n'
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
             'kind': 'cell',
             'line': 63,
             'output': '7',
             'prose': ['`__setattr__` intercepts assignment. This example stores public names in '
                       'the backing dictionary.']}],
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
  'doc_path': '/reference/datamodel.html#customizing-attribute-access',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#customizing-attribute-access',
  'expected_output': 'dark\n7\n',
  'explanation': ['Attribute access is usually simple: `obj.name` looks up an attribute. Python '
                  'exposes hooks for the uncommon cases where lookup or assignment needs to be '
                  'customized.',
                  '`__getattr__` runs only when normal lookup fails, which makes it a safer hook '
                  'for computed fallback attributes. `__setattr__` runs for every assignment, so '
                  'it should be used sparingly and carefully.',
                  'Prefer ordinary attributes and `@property` first. Reach for these hooks when an '
                  'object is intentionally adapting another interface, validating all assignments, '
                  'or exposing dynamic fields.'],
  'min_python': None,
  'notes': ['`__getattr__` is narrower than `__getattribute__` because it handles only missing '
            'attributes.',
            '`__setattr__` affects every assignment on the instance.',
            'Use `property` or descriptors when the behavior is attached to a known attribute '
            'name.'],
  'section': 'Data Model',
  'see_also': ['properties', 'descriptors', 'special-methods', 'bound-and-unbound-methods'],
  'slug': 'attribute-access',
  'summary': 'Attribute hooks customize lookup, missing attributes, and assignment.',
  'title': 'Attribute Access',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Settings:\n'
                           '    def __init__(self, values):\n'
                           '        self._values = dict(values)\n'
                           '\n'
                           'settings = Settings({"theme": "dark"})\n'
                           'print(settings._values)',
                   'prose': 'Normal initialization still needs to set real attributes. Calling '
                            '`object.__setattr__` avoids recursing through your own hook.'},
                  {'code': 'class Settings:\n'
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
                   'prose': '`__getattr__` runs only for missing attributes, so it can provide '
                            'fallback lookup.'},
                  {'code': 'class Settings:\n'
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
                   'prose': '`__setattr__` intercepts assignment. This example stores public names '
                            'in the backing dictionary.'}]},
 {'cells': [{'code': 'class Counter:\n'
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
             'kind': 'cell',
             'line': 23,
             'output': 'True\n11\n12',
             'prose': ['`instance.method` returns a bound method. The method already remembers the '
                       'instance through `__self__`, so calling it does not require passing `self` '
                       'again.']},
            {'code': 'unbound_counter = Counter(0)\n'
                     'unbound = Counter.increment\n'
                     'print(type(unbound).__name__)\n'
                     'print(unbound(unbound_counter))\n'
                     'print(unbound(unbound_counter))',
             'kind': 'cell',
             'line': 49,
             'output': 'function\n1\n2',
             'prose': ['`Class.method` returns the underlying function — there is no `self` '
                       'attached. Calling it requires passing the instance as the first argument '
                       'explicitly. Using a fresh counter here makes the output independent of the '
                       'previous cell.']},
            {'code': 'handlers = []\n'
                     'for _ in range(2):\n'
                     '    handlers.append(Counter().increment)\n'
                     '\n'
                     'print(handlers[0]())\n'
                     'print(handlers[0]())\n'
                     'print(handlers[1]())',
             'kind': 'cell',
             'line': 67,
             'output': '1\n2\n1',
             'prose': ['Bound methods are first-class values. They can be stored in lists, passed '
                       'to other functions, and called later. Each bound method carries its own '
                       '`__self__`, so two methods produced from two different instances stay '
                       'independent.']},
            {'code': 'descriptor_counter = Counter(0)\n'
                     'func = Counter.__dict__["increment"]\n'
                     'print(type(func).__name__)\n'
                     'rebound = func.__get__(descriptor_counter, Counter)\n'
                     'print(type(rebound).__name__)\n'
                     'print(rebound.__self__ is descriptor_counter)',
             'kind': 'cell',
             'line': 87,
             'output': 'function\nmethod\nTrue',
             'prose': ['The binding is the descriptor protocol at work. The function lives on the '
                       'class as a plain function; instance attribute access invokes `__get__`, '
                       'which returns a bound method that knows the instance.']}],
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
  'doc_path': '/reference/datamodel.html#instance-methods',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#instance-methods',
  'expected_output': 'True\n11\n12\nfunction\n1\n2\n1\n2\n1\nfunction\nmethod\nTrue\n',
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
  'min_python': None,
  'notes': ['`instance.method` produces a bound method whose `__self__` is the instance.',
            '`Class.method` produces the plain function and requires you to pass the instance.',
            'Each bound method is its own object; storing one captures its instance.',
            'The binding is implemented by the descriptor protocol on the function object.'],
  'section': 'Data Model',
  'see_also': ['classes', 'attribute-access', 'descriptors', 'callable-objects'],
  'slug': 'bound-and-unbound-methods',
  'summary': 'instance.method binds self automatically; Class.method is a plain function.',
  'title': 'Bound and Unbound Methods',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Counter:\n'
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
                   'prose': '`instance.method` returns a bound method. The method already '
                            'remembers the instance through `__self__`, so calling it does not '
                            'require passing `self` again.'},
                  {'code': 'unbound_counter = Counter(0)\n'
                           'unbound = Counter.increment\n'
                           'print(type(unbound).__name__)\n'
                           'print(unbound(unbound_counter))\n'
                           'print(unbound(unbound_counter))',
                   'prose': '`Class.method` returns the underlying function — there is no `self` '
                            'attached. Calling it requires passing the instance as the first '
                            'argument explicitly. Using a fresh counter here makes the output '
                            'independent of the previous cell.'},
                  {'code': 'handlers = []\n'
                           'for _ in range(2):\n'
                           '    handlers.append(Counter().increment)\n'
                           '\n'
                           'print(handlers[0]())\n'
                           'print(handlers[0]())\n'
                           'print(handlers[1]())',
                   'prose': 'Bound methods are first-class values. They can be stored in lists, '
                            'passed to other functions, and called later. Each bound method '
                            'carries its own `__self__`, so two methods produced from two '
                            'different instances stay independent.'},
                  {'code': 'descriptor_counter = Counter(0)\n'
                           'func = Counter.__dict__["increment"]\n'
                           'print(type(func).__name__)\n'
                           'rebound = func.__get__(descriptor_counter, Counter)\n'
                           'print(type(rebound).__name__)\n'
                           'print(rebound.__self__ is descriptor_counter)',
                   'prose': 'The binding is the descriptor protocol at work. The function lives on '
                            'the class as a plain function; instance attribute access invokes '
                            '`__get__`, which returns a bound method that knows the instance.'}]},
 {'cells': [{'code': 'class Positive:\n'
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
             'kind': 'cell',
             'line': 22,
             'output': '10\nmust be positive',
             'prose': ['A descriptor object lives on the class.']}],
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
  'doc_path': '/howto/descriptor.html',
  'doc_url': 'https://docs.python.org/3.13/howto/descriptor.html',
  'expected_output': '10\nmust be positive\n',
  'explanation': ['Descriptors customize attribute access through __get__, __set__, or __delete__. '
                  'It exists to make a common boundary explicit instead of leaving the behavior '
                  'implicit in a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['A descriptor object lives on the class.',
            'Attribute access on instances calls descriptor methods.',
            'Properties, methods, and many ORMs build on the descriptor protocol.'],
  'section': 'Data Model',
  'see_also': ['attribute-access', 'properties', 'bound-and-unbound-methods'],
  'slug': 'descriptors',
  'summary': 'Descriptors customize attribute access through __get__, __set__, or __delete__.',
  'title': 'Descriptors',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Positive:\n'
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
                   'prose': 'A descriptor object lives on the class.'}]},
 {'cells': [{'code': 'class Tagged(type):\n'
                     '    def __new__(mcls, name, bases, namespace):\n'
                     '        namespace["tag"] = name.lower()\n'
                     '        return super().__new__(mcls, name, bases, namespace)\n'
                     '\n'
                     'print(Tagged.__name__)',
             'kind': 'cell',
             'line': 22,
             'output': 'Tagged',
             'prose': ['A metaclass customizes class creation. `__new__` receives the class name, '
                       'bases, and namespace before the class object exists.']},
            {'code': 'class Event(metaclass=Tagged):\n'
                     '    pass\n'
                     '\n'
                     'print(Event.tag)\n'
                     'print(type(Event).__name__)',
             'kind': 'cell',
             'line': 39,
             'output': 'event\nTagged',
             'prose': ['The `metaclass=` keyword applies that class-building rule. Here the '
                       'metaclass adds a `tag` attribute to the new class.']}],
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
  'doc_path': '/reference/datamodel.html#metaclasses',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#metaclasses',
  'expected_output': 'event\nTagged\n',
  'explanation': ['A metaclass is the class of a class. Most Python code never needs one, but the '
                  'syntax appears in frameworks that register, validate, or modify classes as they '
                  'are created.',
                  'The `metaclass=` keyword in a class statement chooses the object that builds '
                  'the class. This is advanced machinery; decorators and ordinary functions are '
                  'usually simpler.',
                  'Use metaclasses only when class creation itself is the problem being solved.'],
  'min_python': None,
  'notes': ['Metaclasses customize class creation, not instance behavior directly.',
            'Most code should prefer class decorators, functions, or ordinary inheritance.',
            'You are most likely to meet metaclasses inside frameworks and ORMs.'],
  'section': 'Classes',
  'see_also': ['classes', 'inheritance-and-super', 'special-methods'],
  'slug': 'metaclasses',
  'summary': 'A metaclass customizes how classes themselves are created.',
  'title': 'Metaclasses',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Tagged(type):\n'
                           '    def __new__(mcls, name, bases, namespace):\n'
                           '        namespace["tag"] = name.lower()\n'
                           '        return super().__new__(mcls, name, bases, namespace)\n'
                           '\n'
                           'print(Tagged.__name__)',
                   'prose': 'A metaclass customizes class creation. `__new__` receives the class '
                            'name, bases, and namespace before the class object exists.'},
                  {'code': 'class Event(metaclass=Tagged):\n'
                           '    pass\n'
                           '\n'
                           'print(Event.tag)\n'
                           'print(type(Event).__name__)',
                   'prose': 'The `metaclass=` keyword applies that class-building rule. Here the '
                            'metaclass adds a `tag` attribute to the new class.'}]},
 {'cells': [{'code': 'class Tag:\n'
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
             'kind': 'cell',
             'line': 22,
             'output': '<section>\ncontent\n</section>',
             'prose': ['A class-based context manager implements `__enter__` and `__exit__`. The '
                       'value returned by `__enter__` is bound by `as` when the `with` statement '
                       'uses it.']},
            {'code': 'from contextlib import contextmanager\n'
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
             'kind': 'cell',
             'line': 49,
             'output': '<note>\nbody\n</note>',
             'prose': ['`contextlib.contextmanager` writes the same setup/cleanup shape as a '
                       'generator. Code before `yield` is setup, and code after `yield` is '
                       'cleanup.']},
            {'code': 'try:\n'
                     '    with tag("error"):\n'
                     '        raise ValueError("boom")\n'
                     'except ValueError:\n'
                     '    print("handled")',
             'kind': 'cell',
             'line': 74,
             'output': '<error>\n</error>\nhandled',
             'prose': ['Cleanup still runs when the block raises. Returning `False` from '
                       '`__exit__`, or letting a generator context manager re-raise, allows the '
                       'exception to keep propagating.']}],
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
  'doc_path': '/reference/datamodel.html#context-managers',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#context-managers',
  'expected_output': '<section>\ncontent\n</section>\n<error>\n</error>\nhandled\n',
  'explanation': ['Context managers define setup and cleanup around a block of code. The `with` '
                  'statement guarantees that cleanup runs when the block exits, even when an '
                  'exception is raised.',
                  'The protocol is powered by `__enter__` and `__exit__`. The '
                  '`contextlib.contextmanager` decorator is a concise way to write the same idea '
                  'as a generator when a full class would be noisy.',
                  'Production code often uses `with` for files, locks, transactions, temporary '
                  'state, and resources that need reliable release.'],
  'min_python': None,
  'notes': ['Files, locks, and temporary state commonly use context managers.',
            '`__enter__` and `__exit__` power the protocol.',
            'Use `finally` when cleanup must happen after errors too.',
            'Returning true from `__exit__` suppresses an exception; do that only intentionally.'],
  'section': 'Data Model',
  'see_also': ['exceptions', 'special-methods', 'descriptors'],
  'slug': 'context-managers',
  'summary': 'with ensures setup and cleanup happen together.',
  'title': 'Context Managers',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Tag:\n'
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
                   'prose': 'A class-based context manager implements `__enter__` and `__exit__`. '
                            'The value returned by `__enter__` is bound by `as` when the `with` '
                            'statement uses it.'},
                  {'code': 'from contextlib import contextmanager\n'
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
                   'prose': '`contextlib.contextmanager` writes the same setup/cleanup shape as a '
                            'generator. Code before `yield` is setup, and code after `yield` is '
                            'cleanup.'},
                  {'code': 'try:\n'
                           '    with tag("error"):\n'
                           '        raise ValueError("boom")\n'
                           'except ValueError:\n'
                           '    print("handled")',
                   'prose': 'Cleanup still runs when the block raises. Returning `False` from '
                            '`__exit__`, or letting a generator context manager re-raise, allows '
                            'the exception to keep propagating.'}]},
 {'cells': [{'code': 'profile = {"name": "Ada", "temporary": True}\n'
                     'del profile["temporary"]\n'
                     'print(profile)',
             'kind': 'cell',
             'line': 22,
             'output': "{'name': 'Ada'}",
             'prose': ['Deleting a dictionary key mutates the dictionary. The key is gone; it has '
                       'not been set to `None`.']},
            {'code': 'items = ["a", "b", "c"]\ndel items[1]\nprint(items)',
             'kind': 'cell',
             'line': 36,
             'output': "['a', 'c']",
             'prose': ['Deleting a list item removes that position and shifts later items left.']},
            {'code': 'value = "cached"\ndel value\nprint("value" in locals())',
             'kind': 'cell',
             'line': 50,
             'output': 'False',
             'prose': ['Deleting a name removes the binding from the current namespace. It is '
                       'different from rebinding the name to `None`.']}],
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
  'doc_path': '/reference/simple_stmts.html#the-del-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-del-statement',
  'expected_output': "{'name': 'Ada'}\n['a', 'c']\nFalse\n",
  'explanation': ['`del` removes a binding or an item. It is a statement, not a function, and it '
                  'does not return the removed value.',
                  'Use `del name` when a name should no longer be bound. Use `del mapping[key]` or '
                  '`del sequence[index]` when mutating a container by removing one part.',
                  'This is different from assigning `None`: `None` is still a value, while `del` '
                  'removes the binding or slot.'],
  'min_python': None,
  'notes': ['`del` removes bindings or container entries.',
            'Assign `None` when absence should remain an explicit value.',
            'Use container methods such as `pop()` when you need the removed value back.'],
  'section': 'Data Model',
  'see_also': ['variables', 'dicts', 'mutability'],
  'slug': 'delete-statements',
  'summary': 'del removes bindings, items, and attributes rather than producing a value.',
  'title': 'Delete Statements',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'profile = {"name": "Ada", "temporary": True}\n'
                           'del profile["temporary"]\n'
                           'print(profile)',
                   'prose': 'Deleting a dictionary key mutates the dictionary. The key is gone; it '
                            'has not been set to `None`.'},
                  {'code': 'items = ["a", "b", "c"]\ndel items[1]\nprint(items)',
                   'prose': 'Deleting a list item removes that position and shifts later items '
                            'left.'},
                  {'code': 'value = "cached"\ndel value\nprint("value" in locals())',
                   'prose': 'Deleting a name removes the binding from the current namespace. It is '
                            'different from rebinding the name to `None`.'}]},
 {'cells': [{'code': 'def parse_int(text):\n'
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
             'kind': 'cell',
             'line': 19,
             'output': '42: 42\nchecked 42',
             'prose': ['When no exception is raised, the `else` block runs. Keeping success in '
                       '`else` makes the `try` block contain only the operation that might fail.']},
            {'code': 'text = "python"\n'
                     'try:\n'
                     '    number = parse_int(text)\n'
                     'except ValueError:\n'
                     '    print(f"{text}: invalid")\n'
                     'else:\n'
                     '    print(f"{text}: {number}")\n'
                     'finally:\n'
                     '    print(f"checked {text}")',
             'kind': 'cell',
             'line': 43,
             'output': 'python: invalid\nchecked python',
             'prose': ['When parsing fails, `int()` raises `ValueError`. Catching that specific '
                       'exception makes the expected recovery path explicit.']},
            {'code': 'def safe_parse_broken(text):\n'
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
                     'print(safe_parse_fixed("42"))',
             'kind': 'cell',
             'line': 64,
             'output': '42\n42',
             'prose': ['Bare `except:` and broad `except Exception:` swallow far more than the '
                       'failure you meant to handle, including `KeyboardInterrupt` (bare) and most '
                       'programming bugs (broad). Catch the specific class — `ValueError` here — '
                       'so unexpected failures still surface.']}],
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
          'print(safe_parse_fixed("42"))\n',
  'doc_path': '/tutorial/errors.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html',
  'expected_output': '42: 42\nchecked 42\npython: invalid\nchecked python\n42\n42\n',
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
  'min_python': None,
  'notes': ['Catch the most specific exception you can.',
            '`else` is for success code that should run only if the `try` block did not fail.',
            '`finally` runs whether the operation succeeded or failed.',
            'Avoid bare `except:` and broad `except Exception:` — they hide bugs and absorb '
            'signals like `KeyboardInterrupt`.'],
  'section': 'Errors',
  'see_also': [],
  'slug': 'exceptions',
  'summary': 'Use try, except, else, and finally to separate success, recovery, and cleanup.',
  'title': 'Exceptions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def parse_int(text):\n'
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
                   'prose': 'When no exception is raised, the `else` block runs. Keeping success '
                            'in `else` makes the `try` block contain only the operation that might '
                            'fail.'},
                  {'code': 'text = "python"\n'
                           'try:\n'
                           '    number = parse_int(text)\n'
                           'except ValueError:\n'
                           '    print(f"{text}: invalid")\n'
                           'else:\n'
                           '    print(f"{text}: {number}")\n'
                           'finally:\n'
                           '    print(f"checked {text}")',
                   'prose': 'When parsing fails, `int()` raises `ValueError`. Catching that '
                            'specific exception makes the expected recovery path explicit.'},
                  {'code': 'def safe_parse_broken(text):\n'
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
                           'print(safe_parse_fixed("42"))',
                   'prose': 'Bare `except:` and broad `except Exception:` swallow far more than '
                            'the failure you meant to handle, including `KeyboardInterrupt` (bare) '
                            'and most programming bugs (broad). Catch the specific class — '
                            '`ValueError` here — so unexpected failures still surface.'}]},
 {'cells': [{'code': 'def average(scores):\n'
                     '    assert scores, "scores must not be empty"\n'
                     '    return sum(scores) / len(scores)\n'
                     '\n'
                     'print(average([8, 10]))',
             'kind': 'cell',
             'line': 22,
             'output': '9.0',
             'prose': ['When the assertion is true, execution continues normally. The assertion '
                       "documents the function's internal expectation."]},
            {'code': 'try:\n    average([])\nexcept AssertionError as error:\n    print(error)',
             'kind': 'cell',
             'line': 38,
             'output': 'scores must not be empty',
             'prose': ['When the assertion is false, Python raises `AssertionError`. This signals '
                       'a broken assumption, not a normal recovery path.']}],
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
  'doc_path': '/reference/simple_stmts.html#the-assert-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-assert-statement',
  'expected_output': '9.0\nscores must not be empty\n',
  'explanation': ['`assert` checks an internal assumption. If the condition is false, Python '
                  'raises `AssertionError` with an optional message.',
                  'Use assertions for programmer assumptions, not for validating user input or '
                  'external data. Input validation should raise ordinary exceptions that '
                  'production code expects to handle.',
                  'Assertions make invariants executable while keeping the successful path '
                  'compact.'],
  'min_python': None,
  'notes': ['Use `assert` for internal invariants and debugging assumptions.',
            'Use explicit exceptions for user input, files, network responses, and other expected '
            'failures.',
            'Assertions can be disabled with Python optimization flags, so do not rely on them for '
            'security checks.'],
  'section': 'Errors',
  'see_also': ['exceptions', 'custom-exceptions', 'type-hints'],
  'slug': 'assertions',
  'summary': 'assert documents internal assumptions and fails loudly when they are false.',
  'title': 'Assertions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def average(scores):\n'
                           '    assert scores, "scores must not be empty"\n'
                           '    return sum(scores) / len(scores)\n'
                           '\n'
                           'print(average([8, 10]))',
                   'prose': 'When the assertion is true, execution continues normally. The '
                            "assertion documents the function's internal expectation."},
                  {'code': 'try:\n'
                           '    average([])\n'
                           'except AssertionError as error:\n'
                           '    print(error)',
                   'prose': 'When the assertion is false, Python raises `AssertionError`. This '
                            'signals a broken assumption, not a normal recovery path.'}]},
 {'cells': [{'code': 'class ConfigError(Exception):\n'
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
             'kind': 'cell',
             'line': 22,
             'output': 'ConfigError',
             'prose': ['Catch the low-level exception where it happens, then raise a '
                       'domain-specific exception from it.']},
            {'code': 'try:\n'
                     '    read_port("abc")\n'
                     'except ConfigError as error:\n'
                     '    print(error)\n'
                     '    print(type(error.__cause__).__name__)',
             'kind': 'cell',
             'line': 44,
             'output': 'port must be a number\nValueError',
             'prose': ['The caller handles the domain error. The original `ValueError` remains '
                       'available as `__cause__`.']}],
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
  'doc_path': '/tutorial/errors.html#exception-chaining',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#exception-chaining',
  'expected_output': 'ConfigError\nport must be a number\nValueError\n',
  'explanation': ['Exception chaining connects a higher-level error to the lower-level exception '
                  'that caused it. The syntax is `raise NewError(...) from error`.',
                  'Use chaining when translating implementation details into a domain-specific '
                  'error while preserving the original cause for debugging.',
                  'This is different from hiding the original exception. The caller can catch the '
                  'domain error, and tooling can still inspect `__cause__`.'],
  'min_python': None,
  'notes': ['Use `raise ... from error` when translating exceptions across a boundary.',
            "The new exception's `__cause__` points to the original exception.",
            'Chaining keeps user-facing errors clear without losing debugging context.'],
  'section': 'Errors',
  'see_also': ['exceptions', 'custom-exceptions', 'assertions'],
  'slug': 'exception-chaining',
  'summary': 'raise from preserves the original cause when translating exceptions.',
  'title': 'Exception Chaining',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class ConfigError(Exception):\n'
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
                   'prose': 'Catch the low-level exception where it happens, then raise a '
                            'domain-specific exception from it.'},
                  {'code': 'try:\n'
                           '    read_port("abc")\n'
                           'except ConfigError as error:\n'
                           '    print(error)\n'
                           '    print(type(error.__cause__).__name__)',
                   'prose': 'The caller handles the domain error. The original `ValueError` '
                            'remains available as `__cause__`.'}]},
 {'cells': [{'code': 'errors = ExceptionGroup(\n'
                     '    "batch failed",\n'
                     '    [ValueError("bad port"), TypeError("bad mode")],\n'
                     ')\n'
                     'print(len(errors.exceptions))',
             'kind': 'cell',
             'line': 22,
             'output': '2',
             'prose': ['An exception group bundles several exception objects. This is different '
                       'from an ordinary exception because more than one failure is present.']},
            {'code': 'try:\n'
                     '    raise errors\n'
                     'except* ValueError as group:\n'
                     '    print(type(group).__name__)\n'
                     '    print(group.exceptions[0])\n'
                     'except* TypeError as group:\n'
                     '    print(group.exceptions[0])',
             'kind': 'cell',
             'line': 38,
             'output': 'ExceptionGroup\nbad port\nbad mode',
             'prose': ['`except*` handles matching members of the group. The `ValueError` handler '
                       'sees the value error, and the `TypeError` handler sees the type error.']}],
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
  'doc_path': '/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions',
  'expected_output': '2\nExceptionGroup\nbad port\nbad mode\n',
  'explanation': ['`ExceptionGroup` represents several unrelated exceptions raised together. '
                  '`except*` exists for code that may receive multiple failures at once, '
                  'especially concurrent work.',
                  'Use ordinary `except` for one exception. Use `except*` only when the value '
                  'being handled is an exception group and each matching subgroup needs its own '
                  'handling.',
                  'Each `except*` clause receives a smaller exception group containing the '
                  'matching exceptions.'],
  'min_python': None,
  'notes': ['`except*` is for `ExceptionGroup`, not ordinary single exceptions.',
            'Each `except*` clause handles matching members of the group.',
            'Exception groups often appear around concurrent work.'],
  'section': 'Errors',
  'see_also': ['exceptions', 'exception-chaining', 'async-await'],
  'slug': 'exception-groups',
  'summary': 'except* handles matching exceptions inside an ExceptionGroup.',
  'title': 'Exception Groups',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'errors = ExceptionGroup(\n'
                           '    "batch failed",\n'
                           '    [ValueError("bad port"), TypeError("bad mode")],\n'
                           ')\n'
                           'print(len(errors.exceptions))',
                   'prose': 'An exception group bundles several exception objects. This is '
                            'different from an ordinary exception because more than one failure is '
                            'present.'},
                  {'code': 'try:\n'
                           '    raise errors\n'
                           'except* ValueError as group:\n'
                           '    print(type(group).__name__)\n'
                           '    print(group.exceptions[0])\n'
                           'except* TypeError as group:\n'
                           '    print(group.exceptions[0])',
                   'prose': '`except*` handles matching members of the group. The `ValueError` '
                            'handler sees the value error, and the `TypeError` handler sees the '
                            'type error.'}]},
 {'cells': [{'code': 'import warnings\n'
                     '\n'
                     '\n'
                     'def old_name():\n'
                     '    warnings.warn("old_name is deprecated", DeprecationWarning, '
                     'stacklevel=2)\n'
                     '    return "result"\n'
                     '\n'
                     'warnings.simplefilter("always", DeprecationWarning)\n'
                     'with warnings.catch_warnings(record=True) as caught:\n'
                     '    print(old_name())\n'
                     '    print(caught[0].category.__name__)\n'
                     '    print(str(caught[0].message))',
             'kind': 'cell',
             'line': 17,
             'output': 'result\nDeprecationWarning\nold_name is deprecated',
             'prose': ['Warnings are useful for deprecations and soft failures.']}],
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
  'doc_path': '/library/warnings.html',
  'doc_url': 'https://docs.python.org/3.13/library/warnings.html',
  'expected_output': 'result\nDeprecationWarning\nold_name is deprecated\n',
  'explanation': ['warnings report soft problems without immediately stopping the program. It '
                  'exists to make a common boundary explicit instead of leaving the behavior '
                  'implicit in a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['Warnings are useful for deprecations and soft failures.',
            'Filters decide whether warnings are ignored, shown, or turned into errors.',
            'Tests often capture warnings to assert migration behavior.'],
  'section': 'Errors',
  'see_also': [],
  'slug': 'warnings',
  'summary': 'warnings report soft problems without immediately stopping the program.',
  'title': 'Warnings',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import warnings\n'
                           '\n'
                           '\n'
                           'def old_name():\n'
                           '    warnings.warn("old_name is deprecated", DeprecationWarning, '
                           'stacklevel=2)\n'
                           '    return "result"\n'
                           '\n'
                           'warnings.simplefilter("always", DeprecationWarning)\n'
                           'with warnings.catch_warnings(record=True) as caught:\n'
                           '    print(old_name())\n'
                           '    print(caught[0].category.__name__)\n'
                           '    print(str(caught[0].message))',
                   'prose': 'Warnings are useful for deprecations and soft failures.'}]},
 {'cells': [{'code': 'import math\n'
                     '\n'
                     'radius = 3\n'
                     'area = math.pi * radius ** 2\n'
                     'print(round(area, 2))',
             'kind': 'cell',
             'line': 21,
             'output': '28.27',
             'prose': ['Importing a module gives access to its namespace. The `math.` prefix makes '
                       'it clear where `pi` came from.']},
            {'code': 'from statistics import mean\n\nscores = [8, 10, 9]\nprint(mean(scores))',
             'kind': 'cell',
             'line': 37,
             'output': '9',
             'prose': ['A focused `from ... import ...` brings one definition into the current '
                       'namespace. This keeps a common operation concise without importing every '
                       'name.']},
            {'code': 'print(math.__name__)',
             'kind': 'cell',
             'line': 52,
             'output': 'math',
             'prose': ['Modules are objects too. Their attributes include metadata such as '
                       "`__name__`, which records the module's import name."]},
            {'code': 'import sys\nprint("math" in sys.modules)',
             'kind': 'cell',
             'line': 64,
             'output': 'True',
             'prose': ['Imported modules are cached in `sys.modules`. Later imports reuse the '
                       'module object instead of executing the file again.']}],
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
  'doc_path': '/tutorial/modules.html',
  'doc_url': 'https://docs.python.org/3.13/tutorial/modules.html',
  'expected_output': '28.27\n9\nmath\nTrue\n',
  'explanation': ['Modules organize Python code into files and namespaces. `import` executes a '
                  "module once, stores it in Python's import cache, and gives your program access "
                  'to its definitions.',
                  'This page focuses on import forms and module namespaces. Package layout, '
                  'aliases, and dynamic imports have their own neighboring examples.',
                  'Use module namespaces such as `math.sqrt` when the source of a name should stay '
                  'visible. Use focused imports such as `from statistics import mean` when the '
                  'imported name is clear at the call site.'],
  'min_python': None,
  'notes': ['Prefer plain `import module` when the namespace improves readability.',
            'Use focused imports for a small number of clear names.',
            'Place imports near the top of the file.',
            'Imports execute module top-level code once, then reuse the cached module object.'],
  'section': 'Modules',
  'see_also': ['import-aliases', 'packages'],
  'slug': 'modules',
  'summary': 'Modules organize code into namespaces and expose reusable definitions.',
  'title': 'Modules',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import math\n'
                           '\n'
                           'radius = 3\n'
                           'area = math.pi * radius ** 2\n'
                           'print(round(area, 2))',
                   'prose': 'Importing a module gives access to its namespace. The `math.` prefix '
                            'makes it clear where `pi` came from.'},
                  {'code': 'from statistics import mean\n'
                           '\n'
                           'scores = [8, 10, 9]\n'
                           'print(mean(scores))',
                   'prose': 'A focused `from ... import ...` brings one definition into the '
                            'current namespace. This keeps a common operation concise without '
                            'importing every name.'},
                  {'code': 'print(math.__name__)',
                   'prose': 'Modules are objects too. Their attributes include metadata such as '
                            "`__name__`, which records the module's import name."},
                  {'code': 'import sys\nprint("math" in sys.modules)',
                   'prose': 'Imported modules are cached in `sys.modules`. Later imports reuse the '
                            'module object instead of executing the file again.'}]},
 {'cells': [{'code': 'import statistics as stats\n'
                     '\n'
                     'scores = [8, 10, 9]\n'
                     'print(stats.mean(scores))\n'
                     'print(stats.__name__)',
             'kind': 'cell',
             'line': 21,
             'output': '9\nstatistics',
             'prose': ['A module alias keeps the namespace but changes the local name. Here '
                       '`stats` is shorter, but readers can still see that `mean` belongs to the '
                       'statistics module.']},
            {'code': 'from math import sqrt as square_root\n'
                     '\n'
                     'print(square_root(81))\n'
                     'print(square_root.__name__)',
             'kind': 'cell',
             'line': 38,
             'output': '9.0\nsqrt',
             'prose': ['A name imported with `from` can also be aliased. Use this when the local '
                       'name explains the role better than the original name.']}],
  'code': 'import statistics as stats\n'
          'from math import sqrt as square_root\n'
          '\n'
          'scores = [8, 10, 9]\n'
          'print(stats.mean(scores))\n'
          'print(stats.__name__)\n'
          '\n'
          'print(square_root(81))\n'
          'print(square_root.__name__)\n',
  'doc_path': '/reference/simple_stmts.html#the-import-statement',
  'doc_url': 'https://docs.python.org/3.13/reference/simple_stmts.html#the-import-statement',
  'expected_output': '9\nstatistics\n9.0\nsqrt\n',
  'explanation': ['`as` gives an imported module or imported name a local alias. Use it when a '
                  'conventional short name improves readability or when two imports would '
                  'otherwise collide.',
                  'The alternative is a plain import, which is usually better when the module name '
                  'is already clear. Avoid aliases that make readers guess where a name came from.',
                  'Avoid star imports in examples and production modules because they hide '
                  'dependencies and blur the boundary between modules.'],
  'min_python': None,
  'notes': ['`import module as alias` keeps module-style access under a shorter or clearer name.',
            '`from module import name as alias` imports one name under a local alias.',
            'Prefer plain imports unless an alias improves clarity or follows a strong convention.',
            'Avoid `from module import *` because it makes dependencies harder to see.'],
  'section': 'Modules',
  'see_also': ['modules', 'functions'],
  'slug': 'import-aliases',
  'summary': 'as gives imported modules or names a local alias.',
  'title': 'Import Aliases',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import statistics as stats\n'
                           '\n'
                           'scores = [8, 10, 9]\n'
                           'print(stats.mean(scores))\n'
                           'print(stats.__name__)',
                   'prose': 'A module alias keeps the namespace but changes the local name. Here '
                            '`stats` is shorter, but readers can still see that `mean` belongs to '
                            'the statistics module.'},
                  {'code': 'from math import sqrt as square_root\n'
                           '\n'
                           'print(square_root(81))\n'
                           'print(square_root.__name__)',
                   'prose': 'A name imported with `from` can also be aliased. Use this when the '
                            'local name explains the role better than the original name.'}]},
 {'cells': [{'code': 'import json\n\nprint(json.__name__)',
             'kind': 'cell',
             'line': 22,
             'output': 'json',
             'prose': ['A package is itself a module. The `json` package exposes a namespace that '
                       'can contain submodules.']},
            {'code': 'import json.decoder\n'
                     '\n'
                     'print(json.decoder.__name__)\n'
                     'print(json.decoder.JSONDecoder.__name__)',
             'kind': 'cell',
             'line': 36,
             'output': 'json.decoder\nJSONDecoder',
             'prose': ['Dotted imports name a path through a package. Importing `json.decoder` '
                       'makes that submodule available under the package namespace.']},
            {'code': 'import importlib\n'
                     '\n'
                     'module = importlib.import_module("json.decoder")\n'
                     'print(module is json.decoder)',
             'kind': 'cell',
             'line': 52,
             'output': 'True',
             'prose': ['`importlib.import_module()` imports by string. It is useful for plugin '
                       'systems and dynamic imports, but ordinary `import` is clearer when the '
                       'dependency is known.']},
            {'code': 'import os\n'
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
             'kind': 'cell',
             'line': 67,
             'output': "9\n['area']",
             'prose': ["Inside a package's `__init__.py`, `from .submodule import name` re-exports "
                       "a submodule's name at the package root, and `__all__` lists the names that "
                       '`from package import *` should make visible. This cell builds a temporary '
                       '`shapes` package on disk to make both forms concrete.']}],
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
  'doc_path': '/tutorial/modules.html#packages',
  'doc_url': 'https://docs.python.org/3.13/tutorial/modules.html#packages',
  'expected_output': "json\njson.decoder\nJSONDecoder\nTrue\n9\n['area']\n",
  'explanation': ['Packages are modules that can contain other modules. They let a project group '
                  'related code behind dotted import paths such as `json.decoder` or '
                  '`email.message`.',
                  'At runtime, importing a submodule gives Python a path through that package '
                  'structure. In a project on disk, that structure is usually a directory with '
                  'Python files and often an `__init__.py` file.',
                  'Use packages when one module has grown into a small namespace of related '
                  'modules. Keep module names boring and explicit so readers can tell where '
                  'imported definitions come from.'],
  'min_python': None,
  'notes': ['A package is a module that can contain submodules.',
            'Dotted imports should mirror a meaningful project structure.',
            'Use `from .submodule import name` inside a package to re-export submodule names; set '
            '`__all__` to declare the public surface.',
            'Prefer ordinary imports unless the module name is truly dynamic.'],
  'section': 'Modules',
  'see_also': ['modules', 'import-aliases', 'virtual-environments'],
  'slug': 'packages',
  'summary': 'Packages organize modules into importable directories.',
  'title': 'Packages',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import json\n\nprint(json.__name__)',
                   'prose': 'A package is itself a module. The `json` package exposes a namespace '
                            'that can contain submodules.'},
                  {'code': 'import json.decoder\n'
                           '\n'
                           'print(json.decoder.__name__)\n'
                           'print(json.decoder.JSONDecoder.__name__)',
                   'prose': 'Dotted imports name a path through a package. Importing '
                            '`json.decoder` makes that submodule available under the package '
                            'namespace.'},
                  {'code': 'import importlib\n'
                           '\n'
                           'module = importlib.import_module("json.decoder")\n'
                           'print(module is json.decoder)',
                   'prose': '`importlib.import_module()` imports by string. It is useful for '
                            'plugin systems and dynamic imports, but ordinary `import` is clearer '
                            'when the dependency is known.'},
                  {'code': 'import os\n'
                           'import sys\n'
                           'import tempfile\n'
                           '\n'
                           'with tempfile.TemporaryDirectory() as tmp:\n'
                           '    pkg = os.path.join(tmp, "shapes")\n'
                           '    os.makedirs(pkg)\n'
                           '    with open(os.path.join(pkg, "__init__.py"), "w") as init:\n'
                           '        init.write("from .square import area\\n__all__ = '
                           '[\'area\']\\n")\n'
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
                   'prose': "Inside a package's `__init__.py`, `from .submodule import name` "
                            "re-exports a submodule's name at the package root, and `__all__` "
                            'lists the names that `from package import *` should make visible. '
                            'This cell builds a temporary `shapes` package on disk to make both '
                            'forms concrete.'}]},
 {'cells': [{'code': 'builder = venv.EnvBuilder(with_pip=False)\nbuilder.create(".venv")',
             'kind': 'unsupported',
             'line': 18,
             'output': '',
             'prose': ['`venv.EnvBuilder` configures the description of a new environment, then '
                       '`create(".venv")` materialises it on disk as a directory containing its '
                       'own interpreter and `site-packages`. `with_pip=False` skips bootstrapping '
                       "pip — useful when the venv is for an isolated tool that doesn't need to "
                       'install third-party packages. (This fragment runs in standard Python only '
                       "— Dynamic Workers don't provide the `venv` module or a project environment "
                       'workflow.)']},
            {'code': 'import pathlib\n'
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
             'kind': 'cell',
             'line': 27,
             'output': '.venv\nTrue',
             'prose': ['`venv.EnvBuilder` creates the same kind of isolated environment as `python '
                       '-m venv`. A temporary directory keeps the example from leaving project '
                       'files behind.']}],
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
  'doc_path': '/library/venv.html',
  'doc_url': 'https://docs.python.org/3.13/library/venv.html',
  'expected_output': '.venv\nTrue\n',
  'explanation': ["Virtual environments isolate a project's Python packages. They exist so one "
                  "project can install dependencies without changing another project's "
                  'environment.',
                  'The usual command-line workflow is `python -m venv .venv`, but Python also '
                  'exposes the same feature through the `venv` module. This example creates a '
                  'temporary environment so the example cleans up after itself.',
                  'A virtual environment changes where Python looks for installed packages. It '
                  'does not change the language, and it is separate from package layout, imports, '
                  'and module names.'],
  'min_python': None,
  'notes': ['A virtual environment gives a project its own install location.',
            'Inside a venv, `sys.prefix` usually differs from `sys.base_prefix`.',
            'Use `python -m venv .venv` at the command line for everyday project setup.'],
  'section': 'Modules',
  'see_also': [],
  'slug': 'virtual-environments',
  'summary': "Virtual environments isolate a project's Python packages.",
  'title': 'Virtual Environments',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import pathlib\n'
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
                   'prose': '`venv.EnvBuilder` creates the same kind of isolated environment as '
                            '`python -m venv`. A temporary directory keeps the example from '
                            'leaving project files behind.'}]},
 {'cells': [{'code': 'def total(numbers: list[int]) -> int:\n'
                     '    return sum(numbers)\n'
                     '\n'
                     'print(total([1, 2, 3]))',
             'kind': 'cell',
             'line': 23,
             'output': '6',
             'prose': ['Type hints document expected parameter and return shapes. Python still '
                       'runs the function normally at runtime.']},
            {'code': 'print(total.__annotations__)',
             'kind': 'cell',
             'line': 38,
             'output': "{'numbers': list[int], 'return': <class 'int'>}",
             'prose': ['Python stores annotations on the function object for tools and '
                       'introspection. Type checkers use this information without changing the '
                       'function call syntax.']},
            {'code': 'def label(score: int) -> str:\n'
                     '    return f"score={score}"\n'
                     '\n'
                     'print(label("high"))',
             'kind': 'cell',
             'line': 50,
             'output': 'score=high',
             'prose': ['Most hints are not runtime validation. This call passes a string where the '
                       'hint says `int`; Python still calls the function because the body can '
                       'format any value.']},
            {'code': 'def find(name: str, options: list[str]) -> str | None:\n'
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
             'kind': 'cell',
             'line': 65,
             'output': 'Ada\nNone\n1815\nNone',
             'prose': ['Use `X | Y` (PEP 604) to express "either type". `str | None` says the '
                       'result is a string or absent. `typing.Optional[X]` is the older, '
                       'still-supported spelling for the same idea — `Optional[X]` is equivalent '
                       'to `X | None`.']},
            {'code': 'from typing import TypeAlias\n'
                     '\n'
                     'Score: TypeAlias = int\n'
                     '\n'
                     'def grade(score: Score) -> str:\n'
                     '    return "pass" if score >= 50 else "fail"\n'
                     '\n'
                     'print(grade(72))',
             'kind': 'cell',
             'line': 94,
             'output': 'pass',
             'prose': ['`TypeAlias` names a type so it can be reused with intent. `Score: '
                       'TypeAlias = int` keeps the underlying type at runtime but lets the API '
                       'talk about a domain concept rather than a primitive.']}],
  'code': 'from typing import TypeAlias\n'
          '\n'
          'def total(numbers: list[int]) -> int:\n'
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
          'Score: TypeAlias = int\n'
          '\n'
          'def grade(score: Score) -> str:\n'
          '    return "pass" if score >= 50 else "fail"\n'
          '\n'
          'print(grade(72))\n',
  'doc_path': '/library/typing.html',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html',
  'expected_output': '6\n'
                     "{'numbers': list[int], 'return': <class 'int'>}\n"
                     'score=high\n'
                     'Ada\n'
                     'None\n'
                     '1815\n'
                     'None\n'
                     'pass\n',
  'explanation': ['Type hints are annotations that document expected shapes for values, '
                  'parameters, and return results. They exist so tools and readers can understand '
                  'API boundaries before the program runs.',
                  'Python stores many annotations but does not enforce most of them at runtime. '
                  'Use type hints for communication and static analysis; use validation or '
                  'exceptions when runtime checks are required.',
                  'The alternative to an annotation is prose, tests, or runtime validation. Good '
                  'Python code often uses all three at important boundaries.'],
  'min_python': None,
  'notes': ['Python does not enforce most type hints at runtime.',
            'Tools like type checkers and editors use annotations to catch mistakes earlier.',
            'Use `X | Y` for unions and `Optional[X]` for "X or None"; both spellings mean the '
            'same thing.',
            'Reach for `TypeAlias` when a domain name reads better than a raw primitive type.',
            'Use runtime validation when untrusted input must be rejected while the program runs.'],
  'section': 'Types',
  'see_also': ['union-and-optional-types',
               'type-aliases',
               'generics-and-typevar',
               'runtime-type-checks'],
  'slug': 'type-hints',
  'summary': 'Annotations document expected types and power static analysis.',
  'title': 'Type Hints',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def total(numbers: list[int]) -> int:\n'
                           '    return sum(numbers)\n'
                           '\n'
                           'print(total([1, 2, 3]))',
                   'prose': 'Type hints document expected parameter and return shapes. Python '
                            'still runs the function normally at runtime.'},
                  {'code': 'print(total.__annotations__)',
                   'prose': 'Python stores annotations on the function object for tools and '
                            'introspection. Type checkers use this information without changing '
                            'the function call syntax.'},
                  {'code': 'def label(score: int) -> str:\n'
                           '    return f"score={score}"\n'
                           '\n'
                           'print(label("high"))',
                   'prose': 'Most hints are not runtime validation. This call passes a string '
                            'where the hint says `int`; Python still calls the function because '
                            'the body can format any value.'},
                  {'code': 'def find(name: str, options: list[str]) -> str | None:\n'
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
                   'prose': 'Use `X | Y` (PEP 604) to express "either type". `str | None` says the '
                            'result is a string or absent. `typing.Optional[X]` is the older, '
                            'still-supported spelling for the same idea — `Optional[X]` is '
                            'equivalent to `X | None`.'},
                  {'code': 'from typing import TypeAlias\n'
                           '\n'
                           'Score: TypeAlias = int\n'
                           '\n'
                           'def grade(score: Score) -> str:\n'
                           '    return "pass" if score >= 50 else "fail"\n'
                           '\n'
                           'print(grade(72))',
                   'prose': '`TypeAlias` names a type so it can be reused with intent. `Score: '
                            'TypeAlias = int` keeps the underlying type at runtime but lets the '
                            'API talk about a domain concept rather than a primitive.'}]},
 {'cells': [{'code': 'class Animal:\n'
                     '    pass\n'
                     '\n'
                     'class Dog(Animal):\n'
                     '    pass\n'
                     '\n'
                     'pet = Dog()\n'
                     'print(type(pet).__name__)\n'
                     'print(type(pet) is Animal)',
             'kind': 'cell',
             'line': 23,
             'output': 'Dog\nFalse',
             'prose': ['`type()` reports the exact runtime class. A `Dog` instance is not exactly '
                       'an `Animal` instance.']},
            {'code': 'print(isinstance(pet, Dog))\nprint(isinstance(pet, Animal))',
             'kind': 'cell',
             'line': 44,
             'output': 'True\nTrue',
             'prose': ['`isinstance()` accepts subclasses, which is usually what API boundaries '
                       'want.']},
            {'code': 'print(issubclass(Dog, Animal))',
             'kind': 'cell',
             'line': 58,
             'output': 'True',
             'prose': ['`issubclass()` checks class relationships rather than individual '
                       'objects.']}],
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
  'doc_path': '/library/functions.html#isinstance',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#isinstance',
  'expected_output': 'Dog\nFalse\nTrue\nTrue\n',
  'explanation': ['Runtime type checks inspect real objects while the program is running. They are '
                  'different from type hints, which mostly guide tools before the program runs.',
                  'Use `type()` when the exact class matters, `isinstance()` when subclasses '
                  'should count, and `issubclass()` when checking class relationships. Most APIs '
                  'prefer behavior over type checks, but runtime checks are useful at input '
                  'boundaries.',
                  'Do not turn every function into a wall of `isinstance()` calls. If the code '
                  'only needs an object that can perform an operation, duck typing or a protocol '
                  'may be clearer.'],
  'min_python': None,
  'notes': ['`type()` is exact; `isinstance()` follows inheritance.',
            'Runtime checks inspect objects, not static annotations.',
            'Prefer behavior, protocols, or clear validation over scattered type checks.'],
  'section': 'Types',
  'see_also': ['type-hints', 'protocols', 'casts-and-any', 'abstract-base-classes'],
  'slug': 'runtime-type-checks',
  'summary': 'type, isinstance, and issubclass inspect runtime relationships.',
  'title': 'Runtime Type Checks',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class Animal:\n'
                           '    pass\n'
                           '\n'
                           'class Dog(Animal):\n'
                           '    pass\n'
                           '\n'
                           'pet = Dog()\n'
                           'print(type(pet).__name__)\n'
                           'print(type(pet) is Animal)',
                   'prose': '`type()` reports the exact runtime class. A `Dog` instance is not '
                            'exactly an `Animal` instance.'},
                  {'code': 'print(isinstance(pet, Dog))\nprint(isinstance(pet, Animal))',
                   'prose': '`isinstance()` accepts subclasses, which is usually what API '
                            'boundaries want.'},
                  {'code': 'print(issubclass(Dog, Animal))',
                   'prose': '`issubclass()` checks class relationships rather than individual '
                            'objects.'}]},
 {'cells': [{'code': 'def label(value: int | str) -> str:\n'
                     '    return f"item-{value}"\n'
                     '\n'
                     'print(label(3))\n'
                     'print(label("A"))',
             'kind': 'cell',
             'line': 22,
             'output': 'item-3\nitem-A',
             'prose': ['Use `A | B` when a value may have either type. The function body should '
                       'use operations that make sense for every member of the union.']},
            {'code': 'def greeting(name: str | None) -> str:\n'
                     '    if name is None:\n'
                     '        return "hello guest"\n'
                     '    return f"hello {name.upper()}"\n'
                     '\n'
                     'print(greeting(None))\n'
                     'print(greeting("Ada"))',
             'kind': 'cell',
             'line': 39,
             'output': 'hello guest\nhello ADA',
             'prose': ['`str | None` means the function accepts either a string or explicit '
                       'absence. Check for `None` before calling string methods.']},
            {'code': 'print(greeting.__annotations__)',
             'kind': 'cell',
             'line': 58,
             'output': "{'name': str | None, 'return': <class 'str'>}",
             'prose': ['Union annotations are visible at runtime, but Python does not enforce them '
                       'when the function is called.']}],
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
  'doc_path': '/library/typing.html#typing.Optional',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Optional',
  'expected_output': 'item-3\n'
                     'item-A\n'
                     'hello guest\n'
                     'hello ADA\n'
                     "{'name': str | None, 'return': <class 'str'>}\n",
  'explanation': ['A union type says that a value may have one of several static shapes. `int | '
                  'str` means callers may pass either an integer or a string.',
                  '`T | None` is the modern spelling for an optional value. The annotation '
                  'documents that absence is expected, but the code still needs to handle `None` '
                  'before using the non-optional behavior.',
                  'Unions are useful at boundaries where input is flexible. Inside a function, '
                  'narrow the value with an `is None`, `isinstance()`, or pattern check so the '
                  'rest of the code has one clear shape.'],
  'min_python': None,
  'notes': ['Use `A | B` when a value may have either type.',
            '`T | None` means absence is an expected case, not an error by itself.',
            'Narrow unions before using behavior that belongs to only one member type.'],
  'section': 'Types',
  'see_also': ['none', 'type-hints', 'match-statements'],
  'slug': 'union-and-optional-types',
  'summary': 'The | operator describes values that may have more than one static type.',
  'title': 'Union and Optional Types',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def label(value: int | str) -> str:\n'
                           '    return f"item-{value}"\n'
                           '\n'
                           'print(label(3))\n'
                           'print(label("A"))',
                   'prose': 'Use `A | B` when a value may have either type. The function body '
                            'should use operations that make sense for every member of the union.'},
                  {'code': 'def greeting(name: str | None) -> str:\n'
                           '    if name is None:\n'
                           '        return "hello guest"\n'
                           '    return f"hello {name.upper()}"\n'
                           '\n'
                           'print(greeting(None))\n'
                           'print(greeting("Ada"))',
                   'prose': '`str | None` means the function accepts either a string or explicit '
                            'absence. Check for `None` before calling string methods.'},
                  {'code': 'print(greeting.__annotations__)',
                   'prose': 'Union annotations are visible at runtime, but Python does not enforce '
                            'them when the function is called.'}]},
 {'cells': [{'code': 'type UserId = int\n'
                     'type Scores = dict[UserId, int]\n'
                     '\n'
                     '\n'
                     'def best_user(scores: Scores) -> UserId:\n'
                     '    return max(scores, key=scores.get)\n'
                     '\n'
                     'scores: Scores = {1: 98, 2: 91}\n'
                     'print(best_user(scores))',
             'kind': 'cell',
             'line': 22,
             'output': '1',
             'prose': ['The `type` statement names an annotation shape. Here `Scores` means a '
                       'dictionary from user IDs to integer scores.']},
            {'code': 'print(UserId.__name__)\nprint(Scores.__name__)',
             'kind': 'cell',
             'line': 42,
             'output': 'UserId\nScores',
             'prose': ['Modern aliases are runtime objects that keep their alias name for '
                       'introspection.']},
            {'code': 'LegacyName = str\nprint(LegacyName("Ada"))\nprint(LegacyName is str)',
             'kind': 'cell',
             'line': 56,
             'output': 'Ada\nTrue',
             'prose': ['Assignment-style aliases are still common, but they are just ordinary '
                       'names bound to existing objects.']}],
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
  'doc_path': '/library/typing.html#type-aliases',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#type-aliases',
  'expected_output': '1\nUserId\nAda\n',
  'explanation': ['A type alias gives a name to an annotation shape. It helps readers and type '
                  'checkers understand the role of a value without repeating a long type '
                  'expression everywhere.',
                  'Python 3.13 supports the `type` statement for explicit aliases. Older '
                  'assignment-style aliases still appear in code, but the `type` statement makes '
                  'the intent clear and creates a `TypeAliasType` object at runtime.',
                  'An alias does not create a new runtime type. If you need a static distinction '
                  'between compatible values such as user IDs and order IDs, use `NewType` '
                  'instead.'],
  'min_python': None,
  'notes': ['Use aliases to name repeated or domain-specific annotation shapes.',
            'A type alias does not validate values at runtime.',
            'Use `NewType` when two values share a runtime representation but should not be mixed '
            'statically.'],
  'section': 'Types',
  'see_also': ['type-hints', 'newtype', 'union-and-optional-types'],
  'slug': 'type-aliases',
  'summary': 'Type aliases give a meaningful name to a repeated type shape.',
  'title': 'Type Aliases',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'type UserId = int\n'
                           'type Scores = dict[UserId, int]\n'
                           '\n'
                           '\n'
                           'def best_user(scores: Scores) -> UserId:\n'
                           '    return max(scores, key=scores.get)\n'
                           '\n'
                           'scores: Scores = {1: 98, 2: 91}\n'
                           'print(best_user(scores))',
                   'prose': 'The `type` statement names an annotation shape. Here `Scores` means a '
                            'dictionary from user IDs to integer scores.'},
                  {'code': 'print(UserId.__name__)\nprint(Scores.__name__)',
                   'prose': 'Modern aliases are runtime objects that keep their alias name for '
                            'introspection.'},
                  {'code': 'LegacyName = str\nprint(LegacyName("Ada"))\nprint(LegacyName is str)',
                   'prose': 'Assignment-style aliases are still common, but they are just ordinary '
                            'names bound to existing objects.'}]},
 {'cells': [{'code': 'from typing import TypedDict\n'
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
             'kind': 'cell',
             'line': 23,
             'output': 'Ada: 98',
             'prose': ['Use `TypedDict` for JSON-like records that remain dictionaries.']},
            {'code': 'print(isinstance(record, dict))\nprint(type(record).__name__)',
             'kind': 'cell',
             'line': 46,
             'output': 'True\ndict',
             'prose': ['At runtime, a `TypedDict` value is still a plain dictionary.']},
            {'code': 'from typing import NotRequired\n'
                     '\n'
                     'class UserWithNickname(TypedDict):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '    nickname: NotRequired[str]\n'
                     '\n'
                     'record: UserWithNickname = {"name": "Ada", "score": 98}\n'
                     'print(record.get("nickname", "none"))',
             'kind': 'cell',
             'line': 60,
             'output': 'none',
             'prose': ['`NotRequired` marks a key that type checkers should treat as optional. '
                       'Runtime lookup still uses normal dictionary tools such as `get()`.']}],
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
  'doc_path': '/library/typing.html#typing.TypedDict',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.TypedDict',
  'expected_output': 'Ada: 98\nTrue\nnone\n',
  'explanation': ['`TypedDict` describes dictionary records with known keys. It is useful for '
                  'JSON-like data that should remain a dictionary instead of becoming a class '
                  'instance.',
                  'The important boundary is static versus runtime behavior. Type checkers can '
                  'know that `name` is a string and `score` is an integer, but at runtime the '
                  'value is still an ordinary `dict`.',
                  'Use `TypedDict` for external records and `dataclass` when your own program '
                  'wants attribute access, methods, and construction behavior.'],
  'min_python': None,
  'notes': ['Use `TypedDict` for dictionary records from JSON or APIs.',
            'Type checkers understand required and optional keys.',
            'Runtime behavior is still ordinary dictionary behavior.'],
  'section': 'Types',
  'see_also': ['dicts', 'json', 'dataclasses', 'structured-data-shapes'],
  'slug': 'typed-dicts',
  'summary': 'TypedDict describes dictionaries with known string keys.',
  'title': 'TypedDict',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from typing import TypedDict\n'
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
                   'prose': 'Use `TypedDict` for JSON-like records that remain dictionaries.'},
                  {'code': 'print(isinstance(record, dict))\nprint(type(record).__name__)',
                   'prose': 'At runtime, a `TypedDict` value is still a plain dictionary.'},
                  {'code': 'from typing import NotRequired\n'
                           '\n'
                           'class UserWithNickname(TypedDict):\n'
                           '    name: str\n'
                           '    score: int\n'
                           '    nickname: NotRequired[str]\n'
                           '\n'
                           'record: UserWithNickname = {"name": "Ada", "score": 98}\n'
                           'print(record.get("nickname", "none"))',
                   'prose': '`NotRequired` marks a key that type checkers should treat as '
                            'optional. Runtime lookup still uses normal dictionary tools such as '
                            '`get()`.'}]},
 {'cells': [{'code': 'from dataclasses import dataclass\n'
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
             'kind': 'cell',
             'line': 23,
             'output': "UserClass(name='Ada', score=98)\n100",
             'prose': ['A dataclass is a normal class with `__init__` and `__repr__` generated '
                       'from the annotated fields. Instances are mutable, support attribute '
                       'access, and can carry methods like any other class.']},
            {'code': 'from typing import NamedTuple\n'
                     '\n'
                     'class UserTuple(NamedTuple):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '\n'
                     'b = UserTuple("Ada", 98)\n'
                     'print(b)\n'
                     'print(b.name, b[1])\n'
                     'print(b._replace(score=100))',
             'kind': 'cell',
             'line': 46,
             'output': "UserTuple(name='Ada', score=98)\nAda 98\nUserTuple(name='Ada', score=100)",
             'prose': ['A `NamedTuple` is a tuple subclass with named positions. Instances are '
                       'immutable, support both `obj.field` and `obj[index]`, and the helper '
                       '`_replace` produces a modified copy without mutating the original (since '
                       'assigning to a field would fail).']},
            {'code': 'from typing import TypedDict\n'
                     '\n'
                     'class UserDict(TypedDict):\n'
                     '    name: str\n'
                     '    score: int\n'
                     '\n'
                     'c: UserDict = {"name": "Ada", "score": 98}\n'
                     'print(c)\n'
                     'print(c["name"])\n'
                     'print(type(c).__name__)',
             'kind': 'cell',
             'line': 69,
             'output': "{'name': 'Ada', 'score': 98}\nAda\ndict",
             'prose': ['A `TypedDict` is a plain dictionary at runtime. The annotations exist only '
                       'for the type checker, so the value behaves like any `dict` — useful for '
                       'JSON-shaped data that crosses an API boundary as a mapping.']},
            {'code': 'print(isinstance(a, UserClass))\n'
                     'print(isinstance(b, tuple))\n'
                     'print(isinstance(c, dict))',
             'kind': 'cell',
             'line': 92,
             'output': 'True\nTrue\nTrue',
             'prose': ['Same record, three runtime identities. The dataclass is its own class. The '
                       '`NamedTuple` is literally a tuple. The `TypedDict` is literally a dict. '
                       'That difference drives the choice: pick the form whose runtime behavior '
                       'matches what the rest of the program already expects.']}],
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
  'doc_path': '/library/dataclasses.html',
  'doc_url': 'https://docs.python.org/3.13/library/dataclasses.html',
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
                     'True\n',
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
  'min_python': None,
  'notes': ['`@dataclass` — mutable, attribute access, methods; good default when behavior travels '
            'with data.',
            '`typing.NamedTuple` — immutable, attribute + index access, tuple semantics; good for '
            'small records that flow through unpacking.',
            '`typing.TypedDict` — runtime is `dict`, schema is type-checker-only; good for '
            'JSON-shaped data.',
            '`collections.namedtuple` is the older, untyped form of `NamedTuple`; prefer the '
            '`typing` version in new code.'],
  'section': 'Classes',
  'see_also': ['dataclasses', 'typed-dicts', 'tuples', 'classes'],
  'slug': 'structured-data-shapes',
  'summary': 'dataclass, NamedTuple, and TypedDict each model records with different trade-offs.',
  'title': 'Structured Data Shapes',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from dataclasses import dataclass\n'
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
                   'prose': 'A dataclass is a normal class with `__init__` and `__repr__` '
                            'generated from the annotated fields. Instances are mutable, support '
                            'attribute access, and can carry methods like any other class.'},
                  {'code': 'from typing import NamedTuple\n'
                           '\n'
                           'class UserTuple(NamedTuple):\n'
                           '    name: str\n'
                           '    score: int\n'
                           '\n'
                           'b = UserTuple("Ada", 98)\n'
                           'print(b)\n'
                           'print(b.name, b[1])\n'
                           'print(b._replace(score=100))',
                   'prose': 'A `NamedTuple` is a tuple subclass with named positions. Instances '
                            'are immutable, support both `obj.field` and `obj[index]`, and the '
                            'helper `_replace` produces a modified copy without mutating the '
                            'original (since assigning to a field would fail).'},
                  {'code': 'from typing import TypedDict\n'
                           '\n'
                           'class UserDict(TypedDict):\n'
                           '    name: str\n'
                           '    score: int\n'
                           '\n'
                           'c: UserDict = {"name": "Ada", "score": 98}\n'
                           'print(c)\n'
                           'print(c["name"])\n'
                           'print(type(c).__name__)',
                   'prose': 'A `TypedDict` is a plain dictionary at runtime. The annotations exist '
                            'only for the type checker, so the value behaves like any `dict` — '
                            'useful for JSON-shaped data that crosses an API boundary as a '
                            'mapping.'},
                  {'code': 'print(isinstance(a, UserClass))\n'
                           'print(isinstance(b, tuple))\n'
                           'print(isinstance(c, dict))',
                   'prose': 'Same record, three runtime identities. The dataclass is its own '
                            'class. The `NamedTuple` is literally a tuple. The `TypedDict` is '
                            'literally a dict. That difference drives the choice: pick the form '
                            'whose runtime behavior matches what the rest of the program already '
                            'expects.'}]},
 {'cells': [{'code': 'from typing import Final, Literal\n'
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
             'kind': 'cell',
             'line': 17,
             'output': 'opening for read\nopening for write\nread',
             'prose': ['`Literal` describes a small set of exact allowed values.']}],
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
  'doc_path': '/library/typing.html#typing.Literal',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Literal',
  'expected_output': 'opening for read\nopening for write\nread\n',
  'explanation': ['`Literal` restricts a value to one of a small set of exact options, and `Final` '
                  'tells the type checker that a name should not be rebound. Both are static '
                  "promises that type checkers enforce; Python's runtime assignment rules still "
                  'permit any value through if a program ignores the annotation.',
                  'Use them when an annotation makes a constant or a small option set explicit at '
                  'the API boundary. Prefer simpler neighboring tools when the extra machinery '
                  'would hide the intent.',
                  '`Literal` pairs naturally with type aliases and overloads when a function '
                  'should accept only a known set of strings or numbers. `Final` is most useful '
                  'for module-level constants and class attributes that the rest of the codebase '
                  'should treat as immutable.'],
  'min_python': None,
  'notes': ['`Literal` describes a small set of exact allowed values.',
            '`Final` tells type checkers that a name should not be rebound.',
            'Both are static promises; ordinary runtime assignment rules still apply.'],
  'section': 'Types',
  'see_also': [],
  'slug': 'literal-and-final',
  'summary': 'Literal restricts values, while Final marks names that should not be rebound.',
  'title': 'Literal and Final',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from typing import Final, Literal\n'
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
                   'prose': '`Literal` describes a small set of exact allowed values.'}]},
 {'cells': [{'code': 'from collections.abc import Callable\n'
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
             'kind': 'cell',
             'line': 22,
             'output': '5',
             'prose': ['Use `Callable[[Arg], Return]` for function-shaped values. The callback is '
                       'passed in and called by the receiving function.']},
            {'code': 'class Doubler:\n'
                     '    def __call__(self, number: int) -> int:\n'
                     '        return number * 2\n'
                     '\n'
                     'print(apply_twice(3, Doubler()))',
             'kind': 'cell',
             'line': 44,
             'output': '12',
             'prose': ['Callable annotations are structural: an object with `__call__` can also '
                       'satisfy the shape.']},
            {'code': 'print(callable(add_one), callable(Doubler()))',
             'kind': 'cell',
             'line': 60,
             'output': 'True True',
             'prose': ['Runtime callability is a separate question from static annotation. '
                       '`callable()` checks whether Python can call the object.']}],
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
  'doc_path': '/library/typing.html#annotating-callable-objects',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#annotating-callable-objects',
  'expected_output': '5\n12\nTrue True\n',
  'explanation': ['Callable annotations describe values that can be called like functions. They '
                  'are useful when a function accepts a callback, strategy, predicate, or '
                  'transformation.',
                  '`Callable[[int], int]` says how the callback will be called: one integer '
                  'argument, integer result. The annotation helps tools and readers, while runtime '
                  'still only needs an object that is actually callable.',
                  'Use `Callable` for simple call shapes. Use a protocol when the callback needs '
                  'named attributes, overloaded signatures, or a more descriptive interface.'],
  'min_python': None,
  'notes': ['Use `Callable[[Arg], Return]` for simple function-shaped values.',
            'The annotation documents how the callback will be called.',
            'For complex call signatures, protocols can be clearer.'],
  'section': 'Types',
  'see_also': ['functions', 'callable-objects', 'protocols'],
  'slug': 'callable-types',
  'summary': 'Callable annotations describe functions passed as values.',
  'title': 'Callable Types',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from collections.abc import Callable\n'
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
                   'prose': 'Use `Callable[[Arg], Return]` for function-shaped values. The '
                            'callback is passed in and called by the receiving function.'},
                  {'code': 'class Doubler:\n'
                           '    def __call__(self, number: int) -> int:\n'
                           '        return number * 2\n'
                           '\n'
                           'print(apply_twice(3, Doubler()))',
                   'prose': 'Callable annotations are structural: an object with `__call__` can '
                            'also satisfy the shape.'},
                  {'code': 'print(callable(add_one), callable(Doubler()))',
                   'prose': 'Runtime callability is a separate question from static annotation. '
                            '`callable()` checks whether Python can call the object.'}]},
 {'cells': [{'code': 'from typing import TypeVar\n'
                     '\n'
                     'T = TypeVar("T")\n'
                     '\n'
                     '\n'
                     'def first(items: list[T]) -> T:\n'
                     '    return items[0]\n'
                     '\n'
                     'print(first([1, 2, 3]))\n'
                     'print(first(["Ada", "Grace"]))',
             'kind': 'cell',
             'line': 22,
             'output': '1\nAda',
             'prose': ['A `TypeVar` stands for a type chosen by the caller. The return type '
                       'follows the list element type.']},
            {'code': 'def pair(left: T, right: T) -> tuple[T, T]:\n'
                     '    return (left, right)\n'
                     '\n'
                     'print(pair("x", "y"))',
             'kind': 'cell',
             'line': 44,
             'output': "('x', 'y')",
             'prose': ['Reusing the same `TypeVar` expresses a relationship between parameters and '
                       'results.']},
            {'code': 'print(T.__name__)\nprint(first.__annotations__)',
             'kind': 'cell',
             'line': 59,
             'output': "T\n{'items': list[~T], 'return': ~T}",
             'prose': ['`TypeVar` is visible at runtime, but the relationship is mainly for type '
                       'checkers.']}],
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
  'doc_path': '/library/typing.html#generics',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#generics',
  'expected_output': "1\nAda\n('x', 'y')\nT\n",
  'explanation': ['Generics connect types across an API. A plain function that returns `object` '
                  'loses information; a generic function can say that the returned value has the '
                  'same type as the input element.',
                  'A `TypeVar` stands for a type chosen by the caller. In `list[T] -> T`, the same '
                  '`T` says that a list of strings produces a string and a list of integers '
                  'produces an integer.',
                  'Use generics when a function or class is reusable but still preserves a '
                  'relationship between input and output types.'],
  'min_python': None,
  'notes': ['A `TypeVar` stands for a type chosen by the caller.',
            'Generic functions avoid losing information to `object` or `Any`.',
            'Use generics when input and output types are connected.'],
  'section': 'Types',
  'see_also': ['type-hints', 'collections-module', 'casts-and-any'],
  'slug': 'generics-and-typevar',
  'summary': 'Generics preserve type information across reusable functions and classes.',
  'title': 'Generics and TypeVar',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from typing import TypeVar\n'
                           '\n'
                           'T = TypeVar("T")\n'
                           '\n'
                           '\n'
                           'def first(items: list[T]) -> T:\n'
                           '    return items[0]\n'
                           '\n'
                           'print(first([1, 2, 3]))\n'
                           'print(first(["Ada", "Grace"]))',
                   'prose': 'A `TypeVar` stands for a type chosen by the caller. The return type '
                            'follows the list element type.'},
                  {'code': 'def pair(left: T, right: T) -> tuple[T, T]:\n'
                           '    return (left, right)\n'
                           '\n'
                           'print(pair("x", "y"))',
                   'prose': 'Reusing the same `TypeVar` expresses a relationship between '
                            'parameters and results.'},
                  {'code': 'print(T.__name__)\nprint(first.__annotations__)',
                   'prose': '`TypeVar` is visible at runtime, but the relationship is mainly for '
                            'type checkers.'}]},
 {'cells': [{'code': 'from collections.abc import Callable\n'
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
             'kind': 'cell',
             'line': 17,
             'output': 'calling add\n5',
             'prose': ['`ParamSpec` captures the parameters of a callable.']}],
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
  'doc_path': '/library/typing.html#typing.ParamSpec',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.ParamSpec',
  'expected_output': 'calling add\n5\n',
  'explanation': ['`ParamSpec` lets a wrapper preserve the parameter types of the function it '
                  'wraps. The pressure that justifies it is decorators: a generic decorator that '
                  "returns `Callable[..., R]` erases the wrapped function's argument types, so "
                  'callers lose type-checker help on every call.',
                  'Use `ParamSpec` when a decorator should be transparent to type checkers — the '
                  'wrapped function and the decorated name should accept the same arguments. Reach '
                  'for plain `Callable` when the wrapper deliberately changes the signature.',
                  '`P.args` and `P.kwargs` annotate the `*args` and `**kwargs` of the inner '
                  'wrapper, which is how the parameter spec gets bound. Pair `ParamSpec` with a '
                  '`TypeVar` for the return type when the wrapper should also stay generic over '
                  'what the wrapped function returns.'],
  'min_python': None,
  'notes': ['`ParamSpec` captures the parameters of a callable.',
            'Wrappers can forward `*args` and `**kwargs` without erasing the original signature '
            'for type checkers.',
            'This matters most for decorators.'],
  'section': 'Types',
  'see_also': [],
  'slug': 'paramspec',
  'summary': 'ParamSpec preserves callable parameter types through wrappers.',
  'title': 'ParamSpec',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from collections.abc import Callable\n'
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
                   'prose': '`ParamSpec` captures the parameters of a callable.'}]},
 {'cells': [{'code': 'from typing import overload\n'
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
             'kind': 'cell',
             'line': 17,
             'output': '8\nhaha\ndouble',
             'prose': ['`@overload` signatures are for static type checkers.']}],
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
  'doc_path': '/library/typing.html#typing.overload',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.overload',
  'expected_output': '8\nhaha\ndouble\n',
  'explanation': ['overload describes APIs whose return type depends on argument types. It exists '
                  'to make a common boundary explicit instead of leaving the behavior implicit in '
                  'a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['`@overload` signatures are for static type checkers.',
            'The real implementation comes after the overload declarations.',
            'Use overloads when a single runtime function has multiple precise static shapes.'],
  'section': 'Types',
  'see_also': [],
  'slug': 'overloads',
  'summary': 'overload describes APIs whose return type depends on argument types.',
  'title': 'Overloads',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from typing import overload\n'
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
                   'prose': '`@overload` signatures are for static type checkers.'}]},
 {'cells': [{'code': 'from typing import Any, cast\n'
                     '\n'
                     'raw: Any = {"score": "98"}\n'
                     'score_text = cast(dict[str, str], raw)["score"]\n'
                     'score = int(score_text)\n'
                     'print(score + 2)',
             'kind': 'cell',
             'line': 22,
             'output': '100',
             'prose': ['`Any` disables most static checking for a value. The runtime object is '
                       'still whatever value was actually assigned.']},
            {'code': 'print(cast(list[int], raw) is raw)\nprint(type(raw).__name__)',
             'kind': 'cell',
             'line': 39,
             'output': 'True\ndict',
             'prose': ['`cast()` does not convert or validate the value. It returns the same '
                       'object at runtime.']},
            {'code': 'value: object = {"score": "98"}\n'
                     'if isinstance(value, dict):\n'
                     '    print(value["score"])',
             'kind': 'cell',
             'line': 53,
             'output': '98',
             'prose': ['A real runtime check narrows by inspecting the value. This is safer when '
                       'the input is untrusted.']}],
  'code': 'from typing import Any, cast\n'
          '\n'
          'raw: Any = {"score": "98"}\n'
          'score_text = cast(dict[str, str], raw)["score"]\n'
          'score = int(score_text)\n'
          '\n'
          'print(score + 2)\n'
          'print(cast(list[int], raw) is raw)\n'
          'print(type(raw).__name__)\n',
  'doc_path': '/library/typing.html#typing.cast',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.cast',
  'expected_output': '100\nTrue\ndict\n',
  'explanation': ['`Any` and `cast()` are escape hatches. They are useful at messy boundaries '
                  'where a type checker cannot prove what a value is, but they also remove '
                  'protection when overused.',
                  '`Any` tells static tools to stop checking most operations on a value. `cast(T, '
                  'value)` tells the type checker to treat a value as `T`, but it returns the same '
                  'runtime object unchanged.',
                  'Prefer narrowing with runtime checks when possible. Use `cast()` when another '
                  'invariant already proves the type and the checker cannot see that proof.'],
  'min_python': None,
  'notes': ['`Any` disables most static checking for a value.',
            '`cast()` tells the type checker to trust you without changing the runtime object.',
            'Prefer narrowing with checks when possible.'],
  'section': 'Types',
  'see_also': ['type-hints', 'runtime-type-checks', 'typed-dicts'],
  'slug': 'casts-and-any',
  'summary': 'Any and cast are escape hatches for places static analysis cannot prove.',
  'title': 'Casts and Any',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from typing import Any, cast\n'
                           '\n'
                           'raw: Any = {"score": "98"}\n'
                           'score_text = cast(dict[str, str], raw)["score"]\n'
                           'score = int(score_text)\n'
                           'print(score + 2)',
                   'prose': '`Any` disables most static checking for a value. The runtime object '
                            'is still whatever value was actually assigned.'},
                  {'code': 'print(cast(list[int], raw) is raw)\nprint(type(raw).__name__)',
                   'prose': '`cast()` does not convert or validate the value. It returns the same '
                            'object at runtime.'},
                  {'code': 'value: object = {"score": "98"}\n'
                           'if isinstance(value, dict):\n'
                           '    print(value["score"])',
                   'prose': 'A real runtime check narrows by inspecting the value. This is safer '
                            'when the input is untrusted.'}]},
 {'cells': [{'code': 'from typing import NewType\n'
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
             'kind': 'cell',
             'line': 22,
             'output': 'user 42',
             'prose': ['`NewType` helps type checkers distinguish values that share a runtime '
                       'representation.']},
            {'code': 'oid = OrderId(42)\nprint(uid == oid)\nprint(type(uid).__name__)',
             'kind': 'cell',
             'line': 44,
             'output': 'True\nint',
             'prose': ['At runtime, a `NewType` value is the underlying value. It compares like '
                       'that value and has the same runtime type.']},
            {'code': 'print(UserId.__name__)\nprint(OrderId.__name__)',
             'kind': 'cell',
             'line': 59,
             'output': 'UserId\nOrderId',
             'prose': ['The `NewType` constructor keeps a name for static tools and '
                       'introspection.']}],
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
  'doc_path': '/library/typing.html#typing.NewType',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.NewType',
  'expected_output': 'user 42\nTrue\nint\nUserId\n',
  'explanation': ['`NewType` creates a distinct static identity for a value that is represented by '
                  'an existing runtime type. It is useful for IDs, units, and other values that '
                  'should not be mixed accidentally.',
                  'The key boundary is static versus runtime behavior. A type checker can '
                  'distinguish `UserId` from `OrderId`, but at runtime both values are plain '
                  'integers.',
                  'Use a type alias when you only want a clearer name for a shape. Use `NewType` '
                  'when mixing two compatible shapes should be treated as a mistake by static '
                  'analysis.'],
  'min_python': None,
  'notes': ['`NewType` helps type checkers distinguish values that share a runtime representation.',
            'At runtime, the value is still the underlying type.',
            'Use aliases for readability; use `NewType` for static separation.'],
  'section': 'Types',
  'see_also': ['type-aliases', 'type-hints', 'runtime-type-checks'],
  'slug': 'newtype',
  'summary': 'NewType creates distinct static identities for runtime-compatible values.',
  'title': 'NewType',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from typing import NewType\n'
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
                   'prose': '`NewType` helps type checkers distinguish values that share a runtime '
                            'representation.'},
                  {'code': 'oid = OrderId(42)\nprint(uid == oid)\nprint(type(uid).__name__)',
                   'prose': 'At runtime, a `NewType` value is the underlying value. It compares '
                            'like that value and has the same runtime type.'},
                  {'code': 'print(UserId.__name__)\nprint(OrderId.__name__)',
                   'prose': 'The `NewType` constructor keeps a name for static tools and '
                            'introspection.'}]},
 {'cells': [{'code': 'from typing import Protocol\n'
                     '\n'
                     'class Greeter(Protocol):\n'
                     '    def greet(self) -> str:\n'
                     '        ...\n'
                     '\n'
                     'print(Greeter.__name__)',
             'kind': 'cell',
             'line': 23,
             'output': 'Greeter',
             'prose': ['A protocol names required behavior. The ellipsis marks the method body as '
                       'intentionally unspecified, similar to an interface declaration.']},
            {'code': 'class Person:\n'
                     '    def __init__(self, name):\n'
                     '        self.name = name\n'
                     '\n'
                     '    def greet(self):\n'
                     '        return f"hello {self.name}"\n'
                     '\n'
                     'print(Person("Ada").greet())',
             'kind': 'cell',
             'line': 41,
             'output': 'hello Ada',
             'prose': ['A class can satisfy the protocol without inheriting from it. `Person` has '
                       'a compatible `greet()` method, so it has the right shape for static type '
                       'checkers.']},
            {'code': 'def welcome(greeter: Greeter):\n'
                     '    print(greeter.greet())\n'
                     '\n'
                     'welcome(Person("Ada"))',
             'kind': 'cell',
             'line': 60,
             'output': 'hello Ada',
             'prose': ['Use the protocol as an annotation at the API boundary. The function only '
                       'cares that the object can greet; it does not care about the concrete '
                       'class.']}],
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
  'doc_path': '/library/typing.html#typing.Protocol',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html#typing.Protocol',
  'expected_output': 'hello Ada\nGreeter\n',
  'explanation': ['`Protocol` describes the methods or attributes an object must provide. It '
                  'exists for structural typing: if an object has the right shape, type checkers '
                  'can treat it as compatible.',
                  'This is different from inheritance. Inheritance says a class is explicitly '
                  'derived from a parent; a protocol says callers only need a particular behavior.',
                  'At runtime, ordinary method lookup still applies. Protocols are mainly for '
                  'static analysis, documentation, and API boundaries.'],
  'min_python': None,
  'notes': ['Protocols are for structural typing: compatibility by shape rather than explicit '
            'inheritance.',
            'Type checkers understand protocols; normal runtime method calls still do the work.',
            'Prefer inheritance when shared implementation matters, and protocols when only '
            'required behavior matters.'],
  'section': 'Types',
  'see_also': ['type-hints', 'classes', 'inheritance-and-super', 'abstract-base-classes'],
  'slug': 'protocols',
  'summary': 'Protocol describes required behavior for structural typing.',
  'title': 'Protocols',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from typing import Protocol\n'
                           '\n'
                           'class Greeter(Protocol):\n'
                           '    def greet(self) -> str:\n'
                           '        ...\n'
                           '\n'
                           'print(Greeter.__name__)',
                   'prose': 'A protocol names required behavior. The ellipsis marks the method '
                            'body as intentionally unspecified, similar to an interface '
                            'declaration.'},
                  {'code': 'class Person:\n'
                           '    def __init__(self, name):\n'
                           '        self.name = name\n'
                           '\n'
                           '    def greet(self):\n'
                           '        return f"hello {self.name}"\n'
                           '\n'
                           'print(Person("Ada").greet())',
                   'prose': 'A class can satisfy the protocol without inheriting from it. `Person` '
                            'has a compatible `greet()` method, so it has the right shape for '
                            'static type checkers.'},
                  {'code': 'def welcome(greeter: Greeter):\n'
                           '    print(greeter.greet())\n'
                           '\n'
                           'welcome(Person("Ada"))',
                   'prose': 'Use the protocol as an annotation at the API boundary. The function '
                            'only cares that the object can greet; it does not care about the '
                            'concrete class.'}]},
 {'cells': [{'code': 'from abc import ABC, abstractmethod\n'
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
             'kind': 'cell',
             'line': 22,
             'output': "Can't instantiate abstract class Shape without an implementation for "
                       "abstract method 'area'",
             'prose': ['`ABC` plus `@abstractmethod` declares the contract. Trying to construct '
                       'the base class itself fails because at least one method has no '
                       'implementation. A concrete `describe()` lives alongside the abstract '
                       '`area()` so subclasses inherit shared behavior for free.']},
            {'code': 'class Square(Shape):\n'
                     '    def __init__(self, side):\n'
                     '        self.side = side\n'
                     '\n'
                     '    def area(self):\n'
                     '        return self.side ** 2\n'
                     '\n'
                     'print(Square(3).area())\n'
                     'print(Square(3).describe())',
             'kind': 'cell',
             'line': 47,
             'output': '9\nshape with area 9',
             'prose': ['A subclass that implements every abstract method is concrete and can be '
                       'instantiated. It also inherits the non-abstract methods from the base '
                       'class.']},
            {'code': 'class Incomplete(Shape):\n'
                     '    pass\n'
                     '\n'
                     'try:\n'
                     '    Incomplete()\n'
                     'except TypeError as error:\n'
                     '    print(error)',
             'kind': 'cell',
             'line': 68,
             'output': "Can't instantiate abstract class Incomplete without an implementation for "
                       "abstract method 'area'",
             'prose': ['A subclass that forgets to implement an abstract method also cannot be '
                       'instantiated — that is the value the ABC adds. The error fires at '
                       'construction, not when something later tries to call the missing method.']},
            {'code': 'from typing import Protocol\n'
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
             'kind': 'cell',
             'line': 86,
             'output': '15.0\nFalse\nTrue',
             'prose': ['Contrast with `Protocol`. A `HasArea` protocol accepts any class with an '
                       '`area()` method, no inheritance required. `Triangle` does not inherit from '
                       '`Shape`, so it satisfies the protocol but fails `isinstance(_, Shape)`. '
                       '`Square` satisfies both because it explicitly inherited from the ABC.']}],
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
  'doc_path': '/library/abc.html',
  'doc_url': 'https://docs.python.org/3.13/library/abc.html',
  'expected_output': "Can't instantiate abstract class Shape without an implementation for "
                     "abstract method 'area'\n"
                     '9\n'
                     'shape with area 9\n'
                     "Can't instantiate abstract class Incomplete without an implementation for "
                     "abstract method 'area'\n"
                     '15.0\n'
                     'False\n'
                     'True\n',
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
  'min_python': None,
  'notes': ['`ABC` plus `@abstractmethod` blocks instantiation until every abstract method has an '
            'implementation.',
            'ABCs are nominal — subclasses opt in by inheriting; `isinstance()` reflects that '
            'opt-in.',
            'Protocols are structural — any class with the right shape qualifies, regardless of '
            'inheritance.',
            'Prefer an ABC when shared implementation or explicit opt-in matters; prefer a '
            'Protocol when only behavior at the API boundary matters.'],
  'section': 'Classes',
  'see_also': ['protocols', 'inheritance-and-super', 'classes'],
  'slug': 'abstract-base-classes',
  'summary': 'ABC and abstractmethod enforce that subclasses implement required methods.',
  'title': 'Abstract Base Classes',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from abc import ABC, abstractmethod\n'
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
                   'prose': '`ABC` plus `@abstractmethod` declares the contract. Trying to '
                            'construct the base class itself fails because at least one method has '
                            'no implementation. A concrete `describe()` lives alongside the '
                            'abstract `area()` so subclasses inherit shared behavior for free.'},
                  {'code': 'class Square(Shape):\n'
                           '    def __init__(self, side):\n'
                           '        self.side = side\n'
                           '\n'
                           '    def area(self):\n'
                           '        return self.side ** 2\n'
                           '\n'
                           'print(Square(3).area())\n'
                           'print(Square(3).describe())',
                   'prose': 'A subclass that implements every abstract method is concrete and can '
                            'be instantiated. It also inherits the non-abstract methods from the '
                            'base class.'},
                  {'code': 'class Incomplete(Shape):\n'
                           '    pass\n'
                           '\n'
                           'try:\n'
                           '    Incomplete()\n'
                           'except TypeError as error:\n'
                           '    print(error)',
                   'prose': 'A subclass that forgets to implement an abstract method also cannot '
                            'be instantiated — that is the value the ABC adds. The error fires at '
                            'construction, not when something later tries to call the missing '
                            'method.'},
                  {'code': 'from typing import Protocol\n'
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
                   'prose': 'Contrast with `Protocol`. A `HasArea` protocol accepts any class with '
                            'an `area()` method, no inheritance required. `Triangle` does not '
                            'inherit from `Shape`, so it satisfies the protocol but fails '
                            '`isinstance(_, Shape)`. `Square` satisfies both because it explicitly '
                            'inherited from the ABC.'}]},
 {'cells': [{'code': 'from enum import Enum\n'
                     '\n'
                     'class Status(Enum):\n'
                     '    PENDING = "pending"\n'
                     '    DONE = "done"\n'
                     '\n'
                     'current = Status.PENDING\n'
                     'print(current.name)\n'
                     'print(current.value)',
             'kind': 'cell',
             'line': 17,
             'output': 'PENDING\npending',
             'prose': ['An enum member has a symbolic name and an underlying value. The symbolic '
                       'name is what readers usually care about in code.']},
            {'code': 'print(current is Status.PENDING)\nprint(current == "pending")',
             'kind': 'cell',
             'line': 38,
             'output': 'True\nFalse',
             'prose': ['Compare enum members with enum members, not with raw strings. This keeps '
                       'the set of valid states explicit.']}],
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
  'doc_path': '/library/enum.html',
  'doc_url': 'https://docs.python.org/3.13/library/enum.html',
  'expected_output': 'PENDING\npending\nTrue\nFalse\n',
  'explanation': ['`Enum` defines a fixed set of named values. This makes states and modes easier '
                  'to read than raw strings scattered through a program.',
                  'Each enum member has a name and a value. Comparing enum members is explicit and '
                  'helps avoid typos that plain strings would allow.',
                  'Use enums when a value must be one of a small known set: statuses, modes, '
                  'directions, roles, and similar choices.'],
  'min_python': None,
  'notes': ['Enums make states and choices explicit.',
            'Members have names and values.',
            'Comparing enum members avoids string typo bugs.',
            'Prefer raw strings for open-ended text; prefer enums for a closed set of named '
            'choices.'],
  'section': 'Types',
  'see_also': [],
  'slug': 'enums',
  'summary': 'Enum defines symbolic names for a fixed set of values.',
  'title': 'Enums',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from enum import Enum\n'
                           '\n'
                           'class Status(Enum):\n'
                           '    PENDING = "pending"\n'
                           '    DONE = "done"\n'
                           '\n'
                           'current = Status.PENDING\n'
                           'print(current.name)\n'
                           'print(current.value)',
                   'prose': 'An enum member has a symbolic name and an underlying value. The '
                            'symbolic name is what readers usually care about in code.'},
                  {'code': 'print(current is Status.PENDING)\nprint(current == "pending")',
                   'prose': 'Compare enum members with enum members, not with raw strings. This '
                            'keeps the set of valid states explicit.'}]},
 {'cells': [{'code': 'import re\n'
                     '\n'
                     'text = "Ada: 10, Grace: 9"\n'
                     'pattern = r"([A-Za-z]+): (\\d+)"\n'
                     '\n'
                     'for name, score in re.findall(pattern, text):\n'
                     '    print(name, int(score))',
             'kind': 'cell',
             'line': 21,
             'output': 'Ada 10\nGrace 9',
             'prose': ['Raw strings keep backslashes readable in regex patterns. Capturing groups '
                       'return just the pieces inside parentheses.']},
            {'code': 'match = re.search(r"Grace: (\\d+)", text)\nprint(match.group(1))',
             'kind': 'cell',
             'line': 40,
             'output': '9',
             'prose': ['`re.search()` finds the first match. A match object exposes captured '
                       'groups by position.']},
            {'code': 'print("Grace" in text)',
             'kind': 'cell',
             'line': 53,
             'output': 'True',
             'prose': ['For a simple substring check, ordinary string membership is clearer than '
                       'regex.']},
            {'code': 'start = re.match(r"Ada", text)\n'
                     'print(start is not None)\n'
                     'print(re.match(r"Grace", text))',
             'kind': 'cell',
             'line': 65,
             'output': 'True\nNone',
             'prose': ['`re.match` only matches at the start of the string; `re.search` finds the '
                       'first match anywhere. Picking the right one keeps anchoring intent visible '
                       'without an explicit `^`.']},
            {'code': 'scoreline = re.compile(pattern)\nprint(scoreline.findall(text))',
             'kind': 'cell',
             'line': 80,
             'output': "[('Ada', '10'), ('Grace', '9')]",
             'prose': ['`re.compile` produces a reusable pattern object whose methods skip the '
                       'parser on each call. Reach for it when the same pattern runs in a loop.']},
            {'code': 'casey = "ADA: 11"\n'
                     'print(re.search(r"ada", casey, flags=re.IGNORECASE).group(0))\n'
                     '\n'
                     'print(re.sub(r"\\d+", "?", text))',
             'kind': 'cell',
             'line': 93,
             'output': 'ADA\nAda: ?, Grace: ?',
             'prose': ['Flags such as `re.IGNORECASE` adjust matching without changing the '
                       'pattern. `re.sub` replaces every match with a replacement string and '
                       'returns the rewritten text.']}],
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
  'doc_path': '/library/re.html',
  'doc_url': 'https://docs.python.org/3.13/library/re.html',
  'expected_output': 'Ada 10\n'
                     'Grace 9\n'
                     '9\n'
                     'True\n'
                     'True\n'
                     'None\n'
                     "[('Ada', '10'), ('Grace', '9')]\n"
                     'ADA\n'
                     'Ada: ?, Grace: ?\n',
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
  'min_python': None,
  'notes': ['Use raw strings for regex patterns so backslashes are easier to read.',
            'Use capturing groups when the point is extraction, not just matching.',
            '`re.match` anchors at the start; `re.search` finds the first match anywhere.',
            '`re.compile` saves work when the pattern runs more than once.',
            '`re.sub` rewrites matches; flags like `re.IGNORECASE` change matching behavior '
            'without rewriting the pattern.',
            'Reach for string methods before regex when the pattern is simple.'],
  'section': 'Text',
  'see_also': ['strings', 'string-formatting'],
  'slug': 'regular-expressions',
  'summary': 'The re module searches and extracts text using regular expressions.',
  'title': 'Regular Expressions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import re\n'
                           '\n'
                           'text = "Ada: 10, Grace: 9"\n'
                           'pattern = r"([A-Za-z]+): (\\d+)"\n'
                           '\n'
                           'for name, score in re.findall(pattern, text):\n'
                           '    print(name, int(score))',
                   'prose': 'Raw strings keep backslashes readable in regex patterns. Capturing '
                            'groups return just the pieces inside parentheses.'},
                  {'code': 'match = re.search(r"Grace: (\\d+)", text)\nprint(match.group(1))',
                   'prose': '`re.search()` finds the first match. A match object exposes captured '
                            'groups by position.'},
                  {'code': 'print("Grace" in text)',
                   'prose': 'For a simple substring check, ordinary string membership is clearer '
                            'than regex.'},
                  {'code': 'start = re.match(r"Ada", text)\n'
                           'print(start is not None)\n'
                           'print(re.match(r"Grace", text))',
                   'prose': '`re.match` only matches at the start of the string; `re.search` finds '
                            'the first match anywhere. Picking the right one keeps anchoring '
                            'intent visible without an explicit `^`.'},
                  {'code': 'scoreline = re.compile(pattern)\nprint(scoreline.findall(text))',
                   'prose': '`re.compile` produces a reusable pattern object whose methods skip '
                            'the parser on each call. Reach for it when the same pattern runs in a '
                            'loop.'},
                  {'code': 'casey = "ADA: 11"\n'
                           'print(re.search(r"ada", casey, flags=re.IGNORECASE).group(0))\n'
                           '\n'
                           'print(re.sub(r"\\d+", "?", text))',
                   'prose': 'Flags such as `re.IGNORECASE` adjust matching without changing the '
                            'pattern. `re.sub` replaces every match with a replacement string and '
                            'returns the rewritten text.'}]},
 {'cells': [{'code': 'print(int("42"))\nprint(float("3.5"))',
             'kind': 'cell',
             'line': 17,
             'output': '42\n3.5',
             'prose': ['Use `int()` for whole numbers and `float()` for decimal text. Parsed '
                       'values are real numbers, not strings.']},
            {'code': 'try:\n'
                     '    int("python")\n'
                     'except ValueError as error:\n'
                     '    print(type(error).__name__)',
             'kind': 'cell',
             'line': 31,
             'output': 'ValueError',
             'prose': ['Bad numeric text raises `ValueError`. Catch that specific exception when '
                       'invalid input is part of the normal flow.']}],
  'code': 'print(int("42"))\n'
          'print(float("3.5"))\n'
          '\n'
          'try:\n'
          '    int("python")\n'
          'except ValueError as error:\n'
          '    print(type(error).__name__)\n',
  'doc_path': '/library/functions.html#int',
  'doc_url': 'https://docs.python.org/3.13/library/functions.html#int',
  'expected_output': '42\n3.5\nValueError\n',
  'explanation': ['Parsing turns text into numeric values. `int()` parses whole-number text and '
                  '`float()` parses decimal or scientific-notation text.',
                  'Invalid numeric text raises `ValueError`. Catching that specific exception '
                  'makes it clear that bad input is expected and recoverable.',
                  'After parsing, the result is a number and can participate in arithmetic; before '
                  'parsing, it is just text.'],
  'min_python': None,
  'notes': ['`int()` and `float()` are constructors that also parse strings.',
            'Catch `ValueError` when bad user input is expected and recoverable.'],
  'section': 'Standard Library',
  'see_also': [],
  'slug': 'number-parsing',
  'summary': 'int() and float() parse text into numbers and raise ValueError on bad input.',
  'title': 'Number Parsing',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'print(int("42"))\nprint(float("3.5"))',
                   'prose': 'Use `int()` for whole numbers and `float()` for decimal text. Parsed '
                            'values are real numbers, not strings.'},
                  {'code': 'try:\n'
                           '    int("python")\n'
                           'except ValueError as error:\n'
                           '    print(type(error).__name__)',
                   'prose': 'Bad numeric text raises `ValueError`. Catch that specific exception '
                            'when invalid input is part of the normal flow.'}]},
 {'cells': [{'code': 'class EmptyCartError(Exception):\n    pass\n\nprint(EmptyCartError.__name__)',
             'kind': 'cell',
             'line': 17,
             'output': 'EmptyCartError',
             'prose': ['Create a custom exception when a failure has a name in your problem '
                       'domain. The class can be empty at first.']},
            {'code': 'def checkout(items):\n'
                     '    if not items:\n'
                     '        raise EmptyCartError("cart is empty")\n'
                     '    return "paid"\n'
                     '\n'
                     'print(checkout(["book"]))',
             'kind': 'cell',
             'line': 32,
             'output': 'paid',
             'prose': ['Raise the custom exception where the invalid state is detected. Normal '
                       'inputs still follow the ordinary success path.']},
            {'code': 'try:\n    checkout([])\nexcept EmptyCartError as error:\n    print(error)',
             'kind': 'cell',
             'line': 49,
             'output': 'cart is empty',
             'prose': ['Callers can catch the precise error type without accidentally catching '
                       'unrelated failures.']}],
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
  'doc_path': '/tutorial/errors.html#user-defined-exceptions',
  'doc_url': 'https://docs.python.org/3.13/tutorial/errors.html#user-defined-exceptions',
  'expected_output': 'EmptyCartError\npaid\ncart is empty\n',
  'explanation': ['Custom exceptions give names to failures in your problem domain. A named '
                  'exception is easier to catch and explain than a generic error with only a '
                  'string message.',
                  'Raise the custom exception at the point where the invalid state is discovered. '
                  'Include a message for the specific occurrence.',
                  'Catch custom exceptions at the boundary where recovery makes sense, such as '
                  'returning an error response or asking for corrected input.'],
  'min_python': None,
  'notes': ['Subclass `Exception` for errors callers are expected to catch.',
            'A custom exception name can be clearer than reusing a generic `ValueError` '
            'everywhere.',
            'Catch custom exceptions at a boundary that can recover or report clearly.'],
  'section': 'Errors',
  'see_also': [],
  'slug': 'custom-exceptions',
  'summary': 'Custom exception classes name failures that belong to your domain.',
  'title': 'Custom Exceptions',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'class EmptyCartError(Exception):\n'
                           '    pass\n'
                           '\n'
                           'print(EmptyCartError.__name__)',
                   'prose': 'Create a custom exception when a failure has a name in your problem '
                            'domain. The class can be empty at first.'},
                  {'code': 'def checkout(items):\n'
                           '    if not items:\n'
                           '        raise EmptyCartError("cart is empty")\n'
                           '    return "paid"\n'
                           '\n'
                           'print(checkout(["book"]))',
                   'prose': 'Raise the custom exception where the invalid state is detected. '
                            'Normal inputs still follow the ordinary success path.'},
                  {'code': 'try:\n'
                           '    checkout([])\n'
                           'except EmptyCartError as error:\n'
                           '    print(error)',
                   'prose': 'Callers can catch the precise error type without accidentally '
                            'catching unrelated failures.'}]},
 {'cells': [{'code': 'import json\n'
                     '\n'
                     'payload = {"language": "Python", "versions": [3, 13], "stable": True, '
                     '"missing": None}\n'
                     'text = json.dumps(payload, sort_keys=True)\n'
                     'print(text)',
             'kind': 'cell',
             'line': 22,
             'output': '{"language": "Python", "missing": null, "stable": true, "versions": [3, '
                       '13]}',
             'prose': ['`dumps()` encodes Python data as JSON text. `sort_keys=True` keeps '
                       'dictionary keys in a stable order for reproducible output.']},
            {'code': 'pretty = json.dumps({"language": "Python", "stable": True}, indent=2, '
                     'sort_keys=True)\n'
                     'print(pretty.splitlines()[0])\n'
                     'print(pretty.splitlines()[1])',
             'kind': 'cell',
             'line': 38,
             'output': '{\n  "language": "Python",',
             'prose': ['Formatting options change the JSON text, not the Python value. `indent=2` '
                       'is useful for human-readable output.']},
            {'code': 'decoded = json.loads(text)\n'
                     'print(decoded["language"])\n'
                     'print(decoded["missing"] is None)',
             'kind': 'cell',
             'line': 53,
             'output': 'Python\nTrue',
             'prose': ['`loads()` decodes JSON text back into Python values. JSON `null` becomes '
                       'Python `None`.']},
            {'code': 'try:\n'
                     '    json.loads("{bad json}")\n'
                     'except json.JSONDecodeError as error:\n'
                     '    print(error.__class__.__name__)',
             'kind': 'cell',
             'line': 68,
             'output': 'JSONDecodeError',
             'prose': ['Invalid JSON raises `JSONDecodeError`, so input boundaries should handle '
                       'decode failures explicitly.']}],
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
  'doc_path': '/library/json.html',
  'doc_url': 'https://docs.python.org/3.13/library/json.html',
  'expected_output': '{"language": "Python", "missing": null, "stable": true, "versions": [3, '
                     '13]}\n'
                     '{\n'
                     '  "language": "Python",\n'
                     'Python\n'
                     'True\n'
                     'JSONDecodeError\n',
  'explanation': ['The `json` module converts between Python values and JSON text. Dictionaries, '
                  'lists, strings, numbers, booleans, and `None` map naturally to JSON structures.',
                  'Use `dumps()` when you need a string and `loads()` when you need Python objects '
                  'back. Options such as `sort_keys=True` and `indent=2` control stable, readable '
                  'output.',
                  'JSON is a data format, not a way to preserve arbitrary Python objects. Encode '
                  'simple data structures at service boundaries, and expect decode errors when the '
                  'incoming text is not valid JSON.'],
  'min_python': None,
  'notes': ['`dumps()` returns a string; `loads()` accepts a string.',
            'JSON `true`, `false`, and `null` become Python `True`, `False`, and `None`.',
            'Use `sort_keys=True` when stable text output matters.',
            'JSON only represents data shapes, not arbitrary Python objects or behavior.'],
  'section': 'Standard Library',
  'see_also': ['dicts', 'typed-dicts', 'strings'],
  'slug': 'json',
  'summary': 'json encodes Python values as JSON text and decodes them back.',
  'title': 'JSON',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import json\n'
                           '\n'
                           'payload = {"language": "Python", "versions": [3, 13], "stable": True, '
                           '"missing": None}\n'
                           'text = json.dumps(payload, sort_keys=True)\n'
                           'print(text)',
                   'prose': '`dumps()` encodes Python data as JSON text. `sort_keys=True` keeps '
                            'dictionary keys in a stable order for reproducible output.'},
                  {'code': 'pretty = json.dumps({"language": "Python", "stable": True}, indent=2, '
                           'sort_keys=True)\n'
                           'print(pretty.splitlines()[0])\n'
                           'print(pretty.splitlines()[1])',
                   'prose': 'Formatting options change the JSON text, not the Python value. '
                            '`indent=2` is useful for human-readable output.'},
                  {'code': 'decoded = json.loads(text)\n'
                           'print(decoded["language"])\n'
                           'print(decoded["missing"] is None)',
                   'prose': '`loads()` decodes JSON text back into Python values. JSON `null` '
                            'becomes Python `None`.'},
                  {'code': 'try:\n'
                           '    json.loads("{bad json}")\n'
                           'except json.JSONDecodeError as error:\n'
                           '    print(error.__class__.__name__)',
                   'prose': 'Invalid JSON raises `JSONDecodeError`, so input boundaries should '
                            'handle decode failures explicitly.'}]},
 {'cells': [{'code': 'import logging\n'
                     'import sys\n'
                     '\n'
                     'logger = logging.getLogger("example")\n'
                     'logger.setLevel(logging.INFO)\n'
                     'handler = logging.StreamHandler(sys.stdout)\n'
                     'formatter = logging.Formatter("%(levelname)s:%(message)s")\n'
                     'handler.setFormatter(formatter)\n'
                     'logger.handlers[:] = [handler]\n'
                     '\n'
                     'logger.debug("hidden")\n'
                     'logger.info("service started")\n'
                     'logger.warning("disk almost full")',
             'kind': 'cell',
             'line': 17,
             'output': 'INFO:service started\nWARNING:disk almost full',
             'prose': ['Loggers name where an event came from.']}],
  'code': 'import logging\n'
          'import sys\n'
          '\n'
          'logger = logging.getLogger("example")\n'
          'logger.setLevel(logging.INFO)\n'
          'handler = logging.StreamHandler(sys.stdout)\n'
          'formatter = logging.Formatter("%(levelname)s:%(message)s")\n'
          'handler.setFormatter(formatter)\n'
          'logger.handlers[:] = [handler]\n'
          '\n'
          'logger.debug("hidden")\n'
          'logger.info("service started")\n'
          'logger.warning("disk almost full")\n',
  'doc_path': '/library/logging.html',
  'doc_url': 'https://docs.python.org/3.13/library/logging.html',
  'expected_output': 'INFO:service started\nWARNING:disk almost full\n',
  'explanation': ['`logging` records operational events without using `print` as infrastructure. '
                  'Loggers name where each event came from, handlers route records to outputs, and '
                  'levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`) let operators choose how much '
                  'detail they want to see.',
                  'Use it when a program needs structured records with thresholds — production '
                  'services, command-line tools, scheduled jobs. Prefer plain `print` when a small '
                  'script just needs to show a line of human output.',
                  'The example wires a single stream handler to stdout to keep the output '
                  'deterministic. Real applications usually configure logging once at startup and '
                  'then call `logging.getLogger(__name__)` from each module.'],
  'min_python': None,
  'notes': ['Loggers name where an event came from.',
            'Handlers decide where records go.',
            'Levels let operators choose how much detail to see.'],
  'section': 'Standard Library',
  'see_also': [],
  'slug': 'logging',
  'summary': 'logging records operational events without using print as infrastructure.',
  'title': 'Logging',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import logging\n'
                           'import sys\n'
                           '\n'
                           'logger = logging.getLogger("example")\n'
                           'logger.setLevel(logging.INFO)\n'
                           'handler = logging.StreamHandler(sys.stdout)\n'
                           'formatter = logging.Formatter("%(levelname)s:%(message)s")\n'
                           'handler.setFormatter(formatter)\n'
                           'logger.handlers[:] = [handler]\n'
                           '\n'
                           'logger.debug("hidden")\n'
                           'logger.info("service started")\n'
                           'logger.warning("disk almost full")',
                   'prose': 'Loggers name where an event came from.'}]},
 {'cells': [{'code': 'def add(left, right):\n    return left + right\n\nprint(add(2, 3))',
             'kind': 'cell',
             'line': 22,
             'output': '5',
             'prose': ['A test starts with behavior small enough to name. The function can be '
                       'ordinary code; the test supplies a representative input and expected '
                       'result.']},
            {'code': 'import unittest\n'
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
             'kind': 'cell',
             'line': 37,
             'output': "['test_adds_empty_strings', 'test_adds_numbers', "
                       "'test_divide_by_zero_raises']",
             'prose': ['`unittest.TestCase` groups test methods. `setUp` runs before each test '
                       'method to build per-test fixtures, `assertEqual` checks values, and '
                       '`assertRaises` asserts that a block raises the expected exception type.']},
            {'code': 'import io\n'
                     '\n'
                     'loader = unittest.defaultTestLoader\n'
                     'suite = loader.loadTestsFromTestCase(AddTests)\n'
                     'stream = io.StringIO()\n'
                     'runner = unittest.TextTestRunner(stream=stream, verbosity=0)\n'
                     'result = runner.run(suite)\n'
                     'print(result.testsRun)\n'
                     'print(result.wasSuccessful())',
             'kind': 'cell',
             'line': 72,
             'output': '3\nTrue',
             'prose': ['A runner executes the suite and records whether every assertion passed. '
                       "Capturing the runner stream keeps this page's output deterministic."]}],
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
  'doc_path': '/library/unittest.html',
  'doc_url': 'https://docs.python.org/3.13/library/unittest.html',
  'expected_output': '3\nTrue\n',
  'explanation': ['Tests turn expected behavior into code that can be run again. The useful unit '
                  'is usually a small example of behavior with clear input, action, and assertion.',
                  "Python's `unittest` library provides test cases, assertions, suites, and "
                  'runners. Projects often use `pytest` for ergonomics, but the same idea remains: '
                  'a test names behavior and fails when the behavior changes.',
                  'A broad testing practice also includes fixtures, integration tests, property '
                  'tests, and coverage. This example stays on the smallest standard-library loop: '
                  'define behavior, assert the result, run the suite, inspect success.'],
  'min_python': None,
  'notes': ['Test method names should describe behavior, not implementation details.',
            'A good unit test is deterministic and independent of test order.',
            'Use broader integration tests when the behavior depends on several components working '
            'together.'],
  'section': 'Standard Library',
  'see_also': ['assertions', 'exceptions', 'modules'],
  'slug': 'testing',
  'summary': 'Tests make expected behavior executable and repeatable.',
  'title': 'Testing',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'def add(left, right):\n    return left + right\n\nprint(add(2, 3))',
                   'prose': 'A test starts with behavior small enough to name. The function can be '
                            'ordinary code; the test supplies a representative input and expected '
                            'result.'},
                  {'code': 'import unittest\n'
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
                   'prose': '`unittest.TestCase` groups test methods. `setUp` runs before each '
                            'test method to build per-test fixtures, `assertEqual` checks values, '
                            'and `assertRaises` asserts that a block raises the expected exception '
                            'type.'},
                  {'code': 'import io\n'
                           '\n'
                           'loader = unittest.defaultTestLoader\n'
                           'suite = loader.loadTestsFromTestCase(AddTests)\n'
                           'stream = io.StringIO()\n'
                           'runner = unittest.TextTestRunner(stream=stream, verbosity=0)\n'
                           'result = runner.run(suite)\n'
                           'print(result.testsRun)\n'
                           'print(result.wasSuccessful())',
                   'prose': 'A runner executes the suite and records whether every assertion '
                            "passed. Capturing the runner stream keeps this page's output "
                            'deterministic.'}]},
 {'cells': [{'code': 'result = subprocess.run(\n'
                     '    [sys.executable, "-c", "print(\'child process\')"],\n'
                     '    text=True,\n'
                     '    capture_output=True,\n'
                     '    check=True,\n'
                     ')',
             'kind': 'unsupported',
             'line': 18,
             'output': '',
             'prose': ['`subprocess.run` spawns a child Python interpreter, captures its stdout '
                       'and stderr (`capture_output=True`), decodes them as text (`text=True`), '
                       'and raises `CalledProcessError` if the child exits non-zero '
                       '(`check=True`). The returned `result` holds the captured streams and exit '
                       'code as portable evidence the child ran. (This fragment runs in standard '
                       "Python only — Dynamic Workers don't provide child processes.)"]},
            {'code': 'import subprocess\n'
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
             'kind': 'cell',
             'line': 31,
             'output': 'child process\n0',
             'prose': ['`subprocess.run()` starts a child process and waits for it. '
                       "`capture_output=True` stores the child's standard output and error streams "
                       'on the result object.']}],
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
  'doc_path': '/library/subprocess.html',
  'doc_url': 'https://docs.python.org/3.13/library/subprocess.html',
  'expected_output': 'child process\n0\n',
  'explanation': ['`subprocess` is the standard boundary for running external commands. It starts '
                  'another program, waits for it, and gives you a result object with the exit code '
                  'and captured output.',
                  'Use a list of arguments when possible, capture output when the parent program '
                  'needs to inspect it, and treat a non-zero return code as a failure. The same '
                  'ideas apply whether the child program is Python, Git, a compiler, or another '
                  'command-line tool.',
                  'The important boundary is between Python objects and the operating system '
                  'process table. Python prepares arguments and environment, then the child '
                  'program runs independently and reports back through streams and an exit '
                  'status.'],
  'min_python': None,
  'notes': ['Use a list of arguments instead of shell strings when possible.',
            'Capture output when the parent program needs to inspect it.',
            '`check=True` turns non-zero exits into exceptions.'],
  'section': 'Standard Library',
  'see_also': [],
  'slug': 'subprocesses',
  'summary': 'subprocess runs external commands with explicit arguments and captured outputs.',
  'title': 'Subprocesses',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import subprocess\n'
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
                   'prose': '`subprocess.run()` starts a child process and waits for it. '
                            "`capture_output=True` stores the child's standard output and error "
                            'streams on the result object.'}]},
 {'cells': [{'code': 'with ThreadPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(square, [1, 2, 3])))\n'
                     '\n'
                     'with ProcessPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(pow, [4, 5], [2, 2])))',
             'kind': 'unsupported',
             'line': 18,
             'output': '',
             'prose': ['`ThreadPoolExecutor` runs `square` across two worker threads sharing the '
                       'same interpreter (and the GIL); `ProcessPoolExecutor` runs `pow` across '
                       'two child processes with isolated memory. Each `pool.map` returns an '
                       'iterator over results in input order, and the surrounding `with` block '
                       'joins the workers when the body exits. (This fragment runs in standard '
                       "Python only — Dynamic Workers don't provide native threads or child "
                       'processes.)']},
            {'code': 'from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor\n'
                     '\n'
                     '\n'
                     'def square(number):\n'
                     '    return number * number\n'
                     '\n'
                     'with ThreadPoolExecutor(max_workers=2) as pool:\n'
                     '    print(list(pool.map(square, [1, 2, 3])))',
             'kind': 'cell',
             'line': 30,
             'output': '[1, 4, 9]',
             'prose': ['A thread pool runs ordinary callables while sharing memory with the '
                       'current process. `map()` returns results in input order.']},
            {'code': 'print(ProcessPoolExecutor.__name__)',
             'kind': 'cell',
             'line': 49,
             'output': 'ProcessPoolExecutor',
             'prose': ['A process pool uses separate Python processes. That boundary is heavier, '
                       'but it can run CPU-bound work outside the current interpreter.']}],
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
  'doc_path': '/library/concurrent.futures.html',
  'doc_url': 'https://docs.python.org/3.13/library/concurrent.futures.html',
  'expected_output': '[1, 4, 9]\nProcessPoolExecutor\n',
  'explanation': ['Threads and processes are two ways to run work outside the current control '
                  'path. Threads are useful for overlapping I/O-shaped waits, while processes are '
                  'useful when CPU-bound work needs separate interpreter processes.',
                  'This is different from `asyncio`: threads and processes run callables through '
                  'executors, while `async` code cooperatively awaits coroutines. Choose the '
                  'smallest concurrency model that matches the bottleneck.',
                  'The executor interface lets callers submit ordinary functions without '
                  'committing the rest of the code to one scheduling strategy. That makes it '
                  'easier to compare thread and process boundaries at the call site.'],
  'min_python': None,
  'notes': ['Threads share memory, so mutable shared state needs care.',
            'Processes avoid shared interpreter state but require values to cross a process '
            'boundary.',
            'Prefer `asyncio` for coroutine-based I/O and executors for ordinary blocking '
            'callables.'],
  'section': 'Standard Library',
  'see_also': [],
  'slug': 'threads-and-processes',
  'summary': 'Threads share memory, while processes run in separate interpreters.',
  'title': 'Threads and Processes',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from concurrent.futures import ProcessPoolExecutor, '
                           'ThreadPoolExecutor\n'
                           '\n'
                           '\n'
                           'def square(number):\n'
                           '    return number * number\n'
                           '\n'
                           'with ThreadPoolExecutor(max_workers=2) as pool:\n'
                           '    print(list(pool.map(square, [1, 2, 3])))',
                   'prose': 'A thread pool runs ordinary callables while sharing memory with the '
                            'current process. `map()` returns results in input order.'},
                  {'code': 'print(ProcessPoolExecutor.__name__)',
                   'prose': 'A process pool uses separate Python processes. That boundary is '
                            'heavier, but it can run CPU-bound work outside the current '
                            'interpreter.'}]},
 {'cells': [{'code': 'left, right = socket.socketpair()\n'
                     'left.sendall("ping".encode("utf-8"))\n'
                     'data = right.recv(16)',
             'kind': 'unsupported',
             'line': 18,
             'output': '',
             'prose': ['`socketpair()` returns two connected endpoints. `sendall` writes encoded '
                       'bytes into one end, and `recv` reads up to 16 bytes off the other. The '
                       'byte boundary is the whole point: `"ping".encode("utf-8")` produces '
                       "`b'ping'`, which is what the socket actually moves. (This fragment runs in "
                       "standard Python only — Dynamic Workers don't expose arbitrary sockets and "
                       'this app disables Worker outbound access.)']},
            {'code': 'import socket\n'
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
             'kind': 'cell',
             'line': 28,
             'output': "b'ping'\nping",
             'prose': ['The complete version adds two things: a `try`/`finally` so both endpoints '
                       'close even if `recv` or the surrounding work raises, and a second `print` '
                       'that `decode`s the received bytes back into a Python `str` for display. '
                       "The first `print` shows the raw bytes `b'ping'`; the second shows the "
                       'decoded text `ping`.']}],
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
  'doc_path': '/library/socket.html',
  'doc_url': 'https://docs.python.org/3.13/library/socket.html',
  'expected_output': "b'ping'\nping\n",
  'explanation': ['Networking code sends and receives bytes. Higher-level HTTP clients hide many '
                  'details, but the core boundary is still explicit: text must be encoded before '
                  'sending and decoded after receiving.',
                  'This example uses `socket.socketpair()` so it stays local and deterministic in '
                  'ordinary Python. Real network clients often use `socket.create_connection()` or '
                  'a higher-level HTTP library, but the same byte boundary applies.',
                  'The useful mental model is endpoint plus bytes plus cleanup. A socket connects '
                  'two endpoints, transfers byte strings, and must be closed when the conversation '
                  'is finished.'],
  'min_python': None,
  'notes': ['Network protocols move bytes, not Python `str` objects.',
            'Close real sockets when finished, usually with a context manager or `finally` block.',
            'Use high-level HTTP libraries for application HTTP unless socket-level control is the '
            'lesson.'],
  'section': 'Standard Library',
  'see_also': [],
  'slug': 'networking',
  'summary': 'Networking code exchanges bytes across explicit protocol boundaries.',
  'title': 'Networking',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import socket\n'
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
                   'prose': 'The complete version adds two things: a `try`/`finally` so both '
                            'endpoints close even if `recv` or the surrounding work raises, and a '
                            'second `print` that `decode`s the received bytes back into a Python '
                            "`str` for display. The first `print` shows the raw bytes `b'ping'`; "
                            'the second shows the decoded text `ping`.'}]},
 {'cells': [{'code': 'from datetime import date, datetime, time, timedelta, timezone\n'
                     '\n'
                     'release_day = date(2026, 5, 4)\n'
                     'meeting_time = time(12, 30)\n'
                     'created_at = datetime.combine(release_day, meeting_time, '
                     'tzinfo=timezone.utc)\n'
                     '\n'
                     'print(release_day.isoformat())\n'
                     'print(meeting_time.isoformat())\n'
                     'print(created_at.isoformat())',
             'kind': 'cell',
             'line': 17,
             'output': '2026-05-04\n12:30:00\n2026-05-04T12:30:00+00:00',
             'prose': ['The `datetime` module separates calendar dates, clock times, combined '
                       'datetimes, and durations. Import the types you need explicitly.',
                       'Use `date` for a calendar day and `time` for a time of day. Combine them '
                       'into a timezone-aware `datetime` when you mean an instant.',
                       '`isoformat()` produces stable machine-readable text. It is a good default '
                       'for examples, APIs, and logs.']},
            {'code': 'expires_at = created_at + timedelta(days=7, hours=2)\n'
                     'print(expires_at.isoformat())',
             'kind': 'cell',
             'line': 43,
             'output': '2026-05-11T14:30:00+00:00',
             'prose': ['Use `timedelta` for durations. Adding one to a `datetime` produces another '
                       '`datetime` without manually changing calendar fields.']},
            {'code': 'print(created_at.strftime("%Y-%m-%d %H:%M %Z"))\n'
                     'iso_text = "2026-05-04T12:30:00+00:00"\n'
                     'parsed = datetime.fromisoformat(iso_text)\n'
                     'print(parsed == created_at)',
             'kind': 'cell',
             'line': 56,
             'output': '2026-05-04 12:30 UTC\nTrue',
             'prose': ['Use `strftime()` for human-facing formatting and `fromisoformat()` when '
                       'reading ISO 8601 text back into a `datetime`.']}],
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
  'doc_path': '/library/datetime.html',
  'doc_url': 'https://docs.python.org/3.13/library/datetime.html',
  'expected_output': '2026-05-04\n'
                     '12:30:00\n'
                     '2026-05-04T12:30:00+00:00\n'
                     '2026-05-11T14:30:00+00:00\n'
                     '2026-05-04 12:30 UTC\n'
                     'True\n',
  'explanation': ['The `datetime` module covers several related ideas: `date` for calendar days, '
                  '`time` for clock times, `datetime` for both together, and `timedelta` for '
                  'durations.',
                  'Timezone-aware datetimes avoid ambiguity in real systems. `timezone.utc` is a '
                  'clear default for examples because output stays stable and portable.',
                  'Use ISO formatting for interchange, `strftime()` for display, and parsing '
                  'helpers such as `fromisoformat()` to turn text back into datetime objects.'],
  'min_python': None,
  'notes': ['Use timezone-aware datetimes for instants that cross system or user boundaries.',
            'Use `date` for calendar days, `time` for clock times, `datetime` for both, and '
            '`timedelta` for durations.',
            'Prefer ISO 8601 strings for interchange; use `strftime` for human-facing display.'],
  'section': 'Standard Library',
  'see_also': [],
  'slug': 'datetime',
  'summary': 'datetime represents dates, times, durations, formatting, and parsing.',
  'title': 'Dates and Times',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'from datetime import date, datetime, time, timedelta, timezone\n'
                           '\n'
                           'release_day = date(2026, 5, 4)\n'
                           'meeting_time = time(12, 30)\n'
                           'created_at = datetime.combine(release_day, meeting_time, '
                           'tzinfo=timezone.utc)\n'
                           '\n'
                           'print(release_day.isoformat())\n'
                           'print(meeting_time.isoformat())\n'
                           'print(created_at.isoformat())',
                   'prose': 'The `datetime` module separates calendar dates, clock times, combined '
                            'datetimes, and durations. Import the types you need explicitly.'},
                  {'code': 'from datetime import date, datetime, time, timedelta, timezone\n'
                           '\n'
                           'release_day = date(2026, 5, 4)\n'
                           'meeting_time = time(12, 30)\n'
                           'created_at = datetime.combine(release_day, meeting_time, '
                           'tzinfo=timezone.utc)\n'
                           '\n'
                           'print(release_day.isoformat())\n'
                           'print(meeting_time.isoformat())\n'
                           'print(created_at.isoformat())',
                   'prose': 'Use `date` for a calendar day and `time` for a time of day. Combine '
                            'them into a timezone-aware `datetime` when you mean an instant.'},
                  {'code': 'from datetime import date, datetime, time, timedelta, timezone\n'
                           '\n'
                           'release_day = date(2026, 5, 4)\n'
                           'meeting_time = time(12, 30)\n'
                           'created_at = datetime.combine(release_day, meeting_time, '
                           'tzinfo=timezone.utc)\n'
                           '\n'
                           'print(release_day.isoformat())\n'
                           'print(meeting_time.isoformat())\n'
                           'print(created_at.isoformat())',
                   'prose': '`isoformat()` produces stable machine-readable text. It is a good '
                            'default for examples, APIs, and logs.'},
                  {'code': 'expires_at = created_at + timedelta(days=7, hours=2)\n'
                           'print(expires_at.isoformat())',
                   'prose': 'Use `timedelta` for durations. Adding one to a `datetime` produces '
                            'another `datetime` without manually changing calendar fields.'},
                  {'code': 'print(created_at.strftime("%Y-%m-%d %H:%M %Z"))\n'
                           'iso_text = "2026-05-04T12:30:00+00:00"\n'
                           'parsed = datetime.fromisoformat(iso_text)\n'
                           'print(parsed == created_at)',
                   'prose': 'Use `strftime()` for human-facing formatting and `fromisoformat()` '
                            'when reading ISO 8601 text back into a `datetime`.'}]},
 {'cells': [{'code': 'import csv\n'
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
             'kind': 'cell',
             'line': 17,
             'output': 'Ada\n193\nAda,True',
             'prose': ['Use `DictReader` when column names should become dictionary keys.']}],
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
  'doc_path': '/library/csv.html',
  'doc_url': 'https://docs.python.org/3.13/library/csv.html',
  'expected_output': 'Ada\n193\nAda,True\n',
  'explanation': ['csv reads and writes row-shaped text data. It exists to make a common boundary '
                  'explicit instead of leaving the behavior implicit in a larger program.',
                  'Use it when the problem shape matches the example, and prefer simpler '
                  'neighboring tools when the extra machinery would hide the intent. The notes '
                  'call out the boundary so the feature stays practical rather than decorative.',
                  'The example is small, deterministic, and focused on the semantic point. The '
                  'complete source is editable below, while the walkthrough pairs the source with '
                  'its output.'],
  'min_python': None,
  'notes': ['Use `DictReader` when column names should become dictionary keys.',
            'CSV fields arrive as text, so convert numbers explicitly.',
            '`DictWriter` writes dictionaries back to row-shaped text.'],
  'section': 'Standard Library',
  'see_also': [],
  'slug': 'csv-data',
  'summary': 'csv reads and writes row-shaped text data.',
  'title': 'CSV Data',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import csv\n'
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
                   'prose': 'Use `DictReader` when column names should become dictionary keys.'}]},
 {'cells': [{'code': 'import asyncio\n'
                     '\n'
                     'async def fetch_title(slug):\n'
                     '    await asyncio.sleep(0)\n'
                     '    return slug.replace("-", " ").title()\n'
                     '\n'
                     'coroutine = fetch_title("async-await")\n'
                     'print(coroutine.__class__.__name__)\n'
                     'coroutine.close()',
             'kind': 'cell',
             'line': 24,
             'output': 'coroutine',
             'prose': ['An `async def` function returns a coroutine object when called. The '
                       'function body has not produced its final result yet.']},
            {'code': 'async def main():\n'
                     '    title = await fetch_title("async-await")\n'
                     '    print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'kind': 'cell',
             'line': 44,
             'output': 'Async Await',
             'prose': ['Use `await` inside another coroutine to get the eventual result. '
                       '`asyncio.run()` starts an event loop for the top-level coroutine.']},
            {'code': 'async def main():\n'
                     '    titles = await asyncio.gather(fetch_title("json"), '
                     'fetch_title("datetime"))\n'
                     '    print(titles)\n'
                     '\n'
                     'asyncio.run(main())',
             'kind': 'cell',
             'line': 60,
             'output': "['Json', 'Datetime']",
             'prose': ['`asyncio.gather()` awaits several awaitables and returns their results in '
                       'order. This is the shape used when independent I/O operations can progress '
                       'together.']},
            {'code': 'class Session:\n'
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
             'kind': 'cell',
             'line': 76,
             'output': 'open\njson\ndatetime\nclose',
             'prose': ['`async with` and `async for` are the asynchronous forms of context '
                       'managers and iteration. A class implements `__aenter__`/`__aexit__` to act '
                       'as an async context manager; an `async def` function with `yield` becomes '
                       'an async generator. The dedicated [async iteration and '
                       'context](/iteration/async-iteration-and-context) page explains the '
                       'protocols in depth.']}],
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
  'doc_path': '/library/asyncio-task.html',
  'doc_url': 'https://docs.python.org/3.13/library/asyncio-task.html',
  'expected_output': "Async Await\n['Json', 'Datetime']\nopen\njson\ndatetime\nclose\n",
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
  'min_python': None,
  'notes': ['Calling an async function creates a coroutine object.',
            '`await` yields control until an awaitable completes.',
            'Workers request handlers are async, so this pattern appears around fetches and '
            'bindings.',
            'Prefer ordinary functions when there is no awaitable work to coordinate.'],
  'section': 'Async',
  'see_also': ['async-iteration-and-context', 'functions', 'context-managers'],
  'slug': 'async-await',
  'summary': 'async def creates coroutines, and await pauses until awaitable work completes.',
  'title': 'Async Await',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import asyncio\n'
                           '\n'
                           'async def fetch_title(slug):\n'
                           '    await asyncio.sleep(0)\n'
                           '    return slug.replace("-", " ").title()\n'
                           '\n'
                           'coroutine = fetch_title("async-await")\n'
                           'print(coroutine.__class__.__name__)\n'
                           'coroutine.close()',
                   'prose': 'An `async def` function returns a coroutine object when called. The '
                            'function body has not produced its final result yet.'},
                  {'code': 'async def main():\n'
                           '    title = await fetch_title("async-await")\n'
                           '    print(title)\n'
                           '\n'
                           'asyncio.run(main())',
                   'prose': 'Use `await` inside another coroutine to get the eventual result. '
                            '`asyncio.run()` starts an event loop for the top-level coroutine.'},
                  {'code': 'async def main():\n'
                           '    titles = await asyncio.gather(fetch_title("json"), '
                           'fetch_title("datetime"))\n'
                           '    print(titles)\n'
                           '\n'
                           'asyncio.run(main())',
                   'prose': '`asyncio.gather()` awaits several awaitables and returns their '
                            'results in order. This is the shape used when independent I/O '
                            'operations can progress together.'},
                  {'code': 'class Session:\n'
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
                   'prose': '`async with` and `async for` are the asynchronous forms of context '
                            'managers and iteration. A class implements `__aenter__`/`__aexit__` '
                            'to act as an async context manager; an `async def` function with '
                            '`yield` becomes an async generator. The dedicated [async iteration '
                            'and context](/iteration/async-iteration-and-context) page explains '
                            'the protocols in depth.'}]},
 {'cells': [{'code': 'import asyncio\n'
                     '\n'
                     'async def titles():\n'
                     '    for slug in ["values", "async-await"]:\n'
                     '        await asyncio.sleep(0)\n'
                     '        yield slug.replace("-", " ").title()\n'
                     '\n'
                     'print(titles.__name__)',
             'kind': 'cell',
             'line': 24,
             'output': 'titles',
             'prose': ['An async generator can `await` before yielding each value. `async for` '
                       'consumes those values with the asynchronous iteration protocol.']},
            {'code': 'class Session:\n'
                     '    async def __aenter__(self):\n'
                     '        print("open")\n'
                     '        return self\n'
                     '\n'
                     '    async def __aexit__(self, exc_type, exc, tb):\n'
                     '        print("close")\n'
                     '\n'
                     'print(Session.__name__)',
             'kind': 'cell',
             'line': 43,
             'output': 'Session',
             'prose': ['An async context manager defines `__aenter__` and `__aexit__`. `async '
                       'with` awaits setup and cleanup around the block.']},
            {'code': 'async def main():\n'
                     '    async with Session():\n'
                     '        async for title in titles():\n'
                     '            print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'kind': 'cell',
             'line': 63,
             'output': 'open\nValues\nAsync Await\nclose',
             'prose': ['The top-level coroutine combines both protocols: open the async resource, '
                       'then consume the async stream inside it.']}],
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
  'doc_path': '/reference/compound_stmts.html#async-for',
  'doc_url': 'https://docs.python.org/3.13/reference/compound_stmts.html#async-for',
  'expected_output': 'open\nValues\nAsync Await\nclose\n',
  'explanation': ['`async for` consumes an asynchronous iterator: a stream whose next value may '
                  'require `await`. `async with` surrounds a block with asynchronous setup and '
                  'cleanup.',
                  'These forms appear around network streams, database cursors, locks, and service '
                  'clients where both iteration and cleanup may wait on I/O.',
                  'Use ordinary `for` and `with` when producing the next value or cleaning up does '
                  'not need to await anything.',
                  'The syntax mirrors `for` and `with`, but the protocol methods are '
                  'asynchronous.'],
  'min_python': None,
  'notes': ['`async for` consumes asynchronous iterators.',
            '`async with` awaits asynchronous setup and cleanup.',
            'These forms are common around I/O-shaped resources.'],
  'section': 'Async',
  'see_also': ['async-await', 'iterators', 'context-managers'],
  'slug': 'async-iteration-and-context',
  'summary': 'async for and async with consume asynchronous streams and cleanup protocols.',
  'title': 'Async Iteration and Context',
  'version_notes': None,
  'version_sensitive': False,
  'walkthrough': [{'code': 'import asyncio\n'
                           '\n'
                           'async def titles():\n'
                           '    for slug in ["values", "async-await"]:\n'
                           '        await asyncio.sleep(0)\n'
                           '        yield slug.replace("-", " ").title()\n'
                           '\n'
                           'print(titles.__name__)',
                   'prose': 'An async generator can `await` before yielding each value. `async '
                            'for` consumes those values with the asynchronous iteration protocol.'},
                  {'code': 'class Session:\n'
                           '    async def __aenter__(self):\n'
                           '        print("open")\n'
                           '        return self\n'
                           '\n'
                           '    async def __aexit__(self, exc_type, exc, tb):\n'
                           '        print("close")\n'
                           '\n'
                           'print(Session.__name__)',
                   'prose': 'An async context manager defines `__aenter__` and `__aexit__`. `async '
                            'with` awaits setup and cleanup around the block.'},
                  {'code': 'async def main():\n'
                           '    async with Session():\n'
                           '        async for title in titles():\n'
                           '            print(title)\n'
                           '\n'
                           'asyncio.run(main())',
                   'prose': 'The top-level coroutine combines both protocols: open the async '
                            'resource, then consume the async stream inside it.'}]}]
