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
            'the result.'],
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
 {'slug': 'none',
  'title': 'None',
  'section': 'Basics',
  'summary': 'None represents the absence of a value.',
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
          'if score is None:\n'
          '    print("missing score")\n',
  'expected_output': 'True\nmissing score\n',
  'notes': ['Use `is None` rather than `== None`; `None` is a singleton identity value.',
            'A function that reaches the end without `return` also returns `None`.'],
  'cells': [{'prose': ["`None` is Python's value for “nothing here.” It is commonly used as a sentinel when a real "
                       'result is unavailable.'],
             'code': 'result = None\nprint(result is None)',
             'output': 'True',
             'line': 17},
            {'prose': ['Functions often return `None` when lookup or parsing fails without raising an exception.',
                       'Check for `None` with `is None`. That tests identity with the singleton object instead of '
                       'asking for value equality.'],
             'code': 'def find_score(name):\n'
                     '    if name == "Ada":\n'
                     '        return 10\n'
                     '    return None\n'
                     '\n'
                     'score = find_score("Grace")\n'
                     'if score is None:\n'
                     '    print("missing score")',
             'output': 'missing score',
             'line': 30}]},
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
             'line': 17},
            {'prose': ['Assignment can rebind the same name to a different value. The name is not permanently attached '
                       'to the first object.'],
             'code': 'message = "hello"\nprint(message)',
             'output': 'hello',
             'line': 30},
            {'prose': ['Augmented assignment reads the current binding, computes an updated value, and stores the '
                       'result back under the same name.'],
             'code': 'count = 3\ncount += 1\nprint(count)',
             'output': '4',
             'line': 43}]},
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
  'summary': 'Some objects can change in place, and names can share one object.',
  'doc_url': 'https://docs.python.org/3.13/reference/datamodel.html#objects-values-and-types',
  'code': 'first = ["python"]\n'
          'second = first\n'
          'second.append("workers")\n'
          '\n'
          'print(first)\n'
          'print(second)\n'
          '\n'
          'text = "python"\n'
          'text.upper()\n'
          'print(text)\n',
  'expected_output': "['python', 'workers']\n['python', 'workers']\npython\n",
  'notes': ['Lists and dictionaries are mutable; strings and tuples are immutable.',
            'Aliasing is useful, but copy mutable containers when independent changes are needed.'],
  'cells': [{'prose': ['Objects in Python can be mutable or immutable. Mutable objects such as lists can change in '
                       'place, while immutable objects such as strings produce new values instead.',
                       'Names can share one mutable object, so a change through one name is visible through another. '
                       'This is powerful, but it is also the source of many beginner surprises.'],
             'code': 'first = ["python"]\nsecond = first\nsecond.append("workers")\n\nprint(first)\nprint(second)',
             'output': "['python', 'workers']\n['python', 'workers']",
             'line': 17},
            {'prose': ['Understanding mutability explains why copying containers, avoiding mutable defaults, and '
                       'returning new values are recurring Python design choices.'],
             'code': 'text = "python"\ntext.upper()\nprint(text)',
             'output': 'python',
             'line': 37}]},
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
            'Dictionary unpacking with ** is common when calling functions with structured data.'],
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
  'summary': 'Sets store unique values and support set algebra.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/datastructures.html#sets',
  'code': 'languages = {"python", "go", "python"}\n'
          'compiled = {"go", "rust"}\n'
          '\n'
          'print(sorted(languages))\n'
          'print("python" in languages)\n'
          'print(sorted(languages | compiled))\n'
          'print(sorted(languages & compiled))\n'
          'print(sorted(languages - compiled))\n',
  'expected_output': "['go', 'python']\nTrue\n['go', 'python', 'rust']\n['go']\n['python']\n",
  'notes': ['Sets remove duplicates and support fast membership tests.',
            'Set algebra operators make union, intersection, and difference explicit.',
            'Sets are unordered, so sort them when examples need deterministic display.'],
  'cells': [{'prose': ['Creating a set automatically removes duplicates. The repeated `python` value appears only '
                       'once.'],
             'code': 'languages = {"python", "go", "python"}\ncompiled = {"go", "rust"}\n\nprint(sorted(languages))',
             'output': "['go', 'python']",
             'line': 17},
            {'prose': ['Membership checks are the most common set operation.'],
             'code': 'print("python" in languages)',
             'output': 'True',
             'line': 32},
            {'prose': ['Union, intersection, and difference describe relationships between groups without manual '
                       'loops.'],
             'code': 'print(sorted(languages | compiled))\n'
                     'print(sorted(languages & compiled))\n'
                     'print(sorted(languages - compiled))',
             'output': "['go', 'python', 'rust']\n['go']\n['python']",
             'line': 44}]},
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
 {'slug': 'recursion',
  'title': 'Recursion',
  'section': 'Functions',
  'summary': 'Recursive functions solve a problem by calling themselves with a smaller input.',
  'doc_url': 'https://docs.python.org/3.13/tutorial/controlflow.html#defining-functions',
  'code': 'def factorial(n):\n'
          '    if n == 0:\n'
          '        return 1\n'
          '    return n * factorial(n - 1)\n'
          '\n'
          'print(factorial(5))\n',
  'expected_output': '120\n',
  'notes': ['Every recursive function needs a base case that stops the calls.',
            'Python limits recursion depth, so loops are often better for very deep repetition.'],
  'cells': [{'prose': ['A recursive function must handle the smallest case directly. Here `0!` is the base case, so '
                       'the function can answer without another call.'],
             'code': 'def factorial(n):\n    if n == 0:\n        return 1\n\nprint(factorial(0))',
             'output': '1',
             'line': 17},
            {'prose': ['The recursive case calls the same function with a smaller input, moving toward the base case. '
                       'The result is built as the calls return.'],
             'code': 'def factorial(n):\n'
                     '    if n == 0:\n'
                     '        return 1\n'
                     '    return n * factorial(n - 1)\n'
                     '\n'
                     'print(factorial(5))',
             'output': '120',
             'line': 33}]},
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
            'A generator is consumed as you iterate over it.'],
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
  'summary': 'Classes bundle data and behavior.',
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
          'print(first.increment())\n'
          'print(second.increment(5))\n',
  'expected_output': '1\n15\n',
  'notes': ['`self` is the instance the method is operating on.',
            '`__init__` initializes each new object.',
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
             'line': 17},
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
             'line': 41}]},
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
 {'slug': 'type-hints',
  'title': 'Type Hints',
  'section': 'Types',
  'summary': 'Annotations document expected types and power static analysis.',
  'doc_url': 'https://docs.python.org/3.13/library/typing.html',
  'code': 'def total(numbers: list[int]) -> int:\n'
          '    return sum(numbers)\n'
          '\n'
          'print(total([1, 2, 3]))\n'
          'print(total.__annotations__)\n',
  'expected_output': "6\n{'numbers': list[int], 'return': <class 'int'>}\n",
  'notes': ['Python does not enforce most type hints at runtime.',
            'Tools like type checkers and editors use annotations.'],
  'cells': [{'prose': ['Type hints document expected parameter and return shapes. Python still runs the function '
                       'normally at runtime.'],
             'code': 'def total(numbers: list[int]) -> int:\n    return sum(numbers)\n\nprint(total([1, 2, 3]))',
             'output': '6',
             'line': 17},
            {'prose': ['Python stores annotations on the function object for tools and introspection, but it does not '
                       'enforce most hints by itself.'],
             'code': 'def total(numbers: list[int]) -> int:\n    return sum(numbers)\n\nprint(total.__annotations__)',
             'output': "{'numbers': list[int], 'return': <class 'int'>}",
             'line': 32}]},
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
            'Comparing enum members avoids string typo bugs.'],
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
            'Workers request handlers are async, so this pattern appears around fetches and bindings.'],
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
             'line': 17},
            {'prose': ['Use `await` inside another coroutine to get the eventual result. `asyncio.run()` starts an '
                       'event loop for the top-level coroutine.'],
             'code': 'async def main():\n'
                     '    title = await fetch_title("async-await")\n'
                     '    print(title)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': 'Async Await',
             'line': 37},
            {'prose': ['`asyncio.gather()` awaits several awaitables and returns their results in order. This is the '
                       'shape used when independent I/O operations can progress together.'],
             'code': 'async def main():\n'
                     '    titles = await asyncio.gather(fetch_title("json"), fetch_title("datetime"))\n'
                     '    print(titles)\n'
                     '\n'
                     'asyncio.run(main())',
             'output': "['Json', 'Datetime']",
             'line': 53}]}]
