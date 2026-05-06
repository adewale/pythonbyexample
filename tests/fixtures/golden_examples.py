"""Versioned example catalog for Python By Example.

To update for a new Python release, change PYTHON_VERSION and add/edit examples here.
Examples are intentionally self-contained so each can run inside a Dynamic Python Worker.
"""

import contextlib
import io

PYTHON_VERSION = "3.13"
REFERENCE_URL = f"https://docs.python.org/{PYTHON_VERSION}/"

EXAMPLES = [
    {
        "slug": "hello-world",
        "title": "Hello World",
        "section": "Basics",
        "summary": "The first Python program prints a line of text.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/introduction.html",
        "code": "print(\"hello world\")\n",
        "notes": [
            "`print()` writes text followed by a newline.",
            "Strings can be delimited with single or double quotes.",
        ],
    },
    {
        "slug": "values",
        "title": "Values",
        "section": "Basics",
        "summary": "Python has strings, integers, floats, booleans, and None.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/stdtypes.html",
        "code": "print(\"python\" + \" by example\")\nprint(1 + 2)\nprint(7 / 2)\nprint(True and False)\nprint(None)\n",
        "notes": [
            "Operators usually return new values; they do not mutate their operands.",
            "True, False, and None are capitalized singleton constants.",
        ],
    },

    {
        "slug": "numbers",
        "title": "Numbers",
        "section": "Basics",
        "summary": "Python numbers include integers and floating-point values.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/stdtypes.html#numeric-types-int-float-complex",
        "code": "count = 10\nratio = 0.25\n\nprint(count + 5)\nprint(count / 4)\nprint(count // 4)\nprint(count % 4)\nprint(2 ** 5)\nprint(round(3.14159, 2))\n",
        "notes": ["Python's `int` has arbitrary precision; it grows as large as memory allows.", "Python's `float` is the usual double-precision floating-point type; core Python does not expose separate `float32` and `float64` syntax.", "Use `/` for true division and `//` for floor division."],
        "walkthrough": [
            {"prose": "Python has `int` for whole numbers and `float` for floating-point numbers. You usually write them directly as literals.", "code": "count = 10\nratio = 0.25"},
            {"prose": "Arithmetic operators return new numeric values. True division with `/` returns a `float`, even when both inputs are integers.", "code": "print(count + 5)\nprint(count / 4)"},
            {"prose": "Floor division and modulo are useful when you need quotient and remainder behavior. Powers use `**`, not `^`.", "code": "print(count // 4)\nprint(count % 4)\nprint(2 ** 5)"},
            {"prose": "Floating-point values are approximate, so examples often round display output when the lesson is about presentation rather than precision.", "code": "print(round(3.14159, 2))"},
        ],
    },
    {
        "slug": "booleans",
        "title": "Booleans",
        "section": "Basics",
        "summary": "Booleans represent truth values and combine with logical operators.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/stdtypes.html#boolean-type-bool",
        "code": "logged_in = True\nhas_permission = False\n\nprint(logged_in and has_permission)\nprint(logged_in or has_permission)\nprint(not has_permission)\n\nname = \"Ada\"\nprint(name == \"Ada\" and len(name) > 0)\n",
        "notes": ["Boolean constants are `True` and `False`, with capital letters.", "`and` and `or` short-circuit: Python does not evaluate the right side if the left side already determines the result."],
        "walkthrough": [
            {"prose": "Use booleans for facts that are either true or false. Python spells the constants `True` and `False`.", "code": "logged_in = True\nhas_permission = False"},
            {"prose": "Use `and`, `or`, and `not` to combine truth values. These operators read like English and short-circuit when possible.", "code": "print(logged_in and has_permission)\nprint(logged_in or has_permission)\nprint(not has_permission)"},
            {"prose": "Comparisons produce booleans too, so they compose naturally with logical operators in conditions and validation checks.", "code": "name = \"Ada\"\nprint(name == \"Ada\" and len(name) > 0)"},
        ],
    },
    {
        "slug": "none",
        "title": "None",
        "section": "Basics",
        "summary": "None represents the absence of a value.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/constants.html#None",
        "code": "result = None\nprint(result is None)\n\ndef find_score(name):\n    if name == \"Ada\":\n        return 10\n    return None\n\nscore = find_score(\"Grace\")\nif score is None:\n    print(\"missing score\")\n",
        "notes": ["Use `is None` rather than `== None`; `None` is a singleton identity value.", "A function that reaches the end without `return` also returns `None`."],
        "walkthrough": [
            {"prose": "`None` is Python's value for “nothing here.” It is commonly used as a sentinel when a real result is unavailable.", "code": "result = None\nprint(result is None)"},
            {"prose": "Functions often return `None` when lookup or parsing fails without raising an exception.", "code": "def find_score(name):\n    if name == \"Ada\":\n        return 10\n    return None"},
            {"prose": "Check for `None` with `is None`. That tests identity with the singleton object instead of asking for value equality.", "code": "score = find_score(\"Grace\")\nif score is None:\n    print(\"missing score\")"},
        ],
    },
    {
        "slug": "constants",
        "title": "Constants",
        "section": "Basics",
        "summary": "Python uses naming conventions for values that should not change.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/classes.html#python-scopes-and-namespaces",
        "code": "MAX_RETRIES = 3\nAPI_VERSION = \"2026-05\"\n\nfor attempt in range(1, MAX_RETRIES + 1):\n    print(f\"attempt {attempt} of {MAX_RETRIES}\")\n\nprint(API_VERSION)\n",
        "notes": ["Python has no `const` keyword for ordinary names.", "All-caps names such as `MAX_RETRIES` communicate that a value is intended to stay fixed."],
        "walkthrough": [
            {"prose": "Python does not have a `const` declaration like Go or Rust. Instead, modules use all-caps names for values callers should treat as fixed.", "code": "MAX_RETRIES = 3\nAPI_VERSION = \"2026-05\""},
            {"prose": "The interpreter will still let you rebind the name, but the convention is strong enough that readers understand the design intent.", "code": "for attempt in range(1, MAX_RETRIES + 1):\n    print(f\"attempt {attempt} of {MAX_RETRIES}\")"},
            {"prose": "Constants are useful for configuration values that should be named once and reused instead of repeated as magic literals.", "code": "print(API_VERSION)"},
        ],
    },
    {
        "slug": "variables",
        "title": "Variables",
        "section": "Basics",
        "summary": "Names are bound to values with assignment.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/reference/simple_stmts.html#assignment-statements",
        "code": "message = \"hi\"\ncount = 3\ncount += 1\n\nprint(message)\nprint(count)\n",
        "notes": [
            "Python variables are names bound to objects, not boxes with fixed types.",
            "Augmented assignment like += rebinding is common for counters.",
        ],
    },
    {
        "slug": "for-loops",
        "title": "For Loops",
        "section": "Control Flow",
        "summary": "for iterates over any iterable object.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#for-statements",
        "code": "for name in [\"Ada\", \"Grace\", \"Guido\"]:\n    print(name)\n\nfor number in range(3):\n    print(number)\n",
        "notes": [
            "Blocks are defined by indentation.",
            "range(3) yields 0, 1, and 2.",
        ],
    },
    {
        "slug": "functions",
        "title": "Functions",
        "section": "Functions",
        "summary": "Use def to package reusable behavior.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#defining-functions",
        "code": "def greet(name, excited=False):\n    ending = \"!\" if excited else \".\"\n    return f\"Hello, {name}{ending}\"\n\nprint(greet(\"Python\"))\nprint(greet(\"Workers\", excited=True))\n",
        "notes": [
            "Functions return None unless they execute a return statement.",
            "Keyword arguments make call sites easier to read.",
        ],
    },
    {
        "slug": "lists",
        "title": "Lists",
        "section": "Collections",
        "summary": "Lists are ordered, mutable collections.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/datastructures.html#more-on-lists",
        "code": "numbers = [3, 1, 4]\nnumbers.append(1)\nprint(numbers)\nprint(sorted(numbers))\nprint(numbers[0])\nprint(numbers[-1])\n",
        "notes": [
            "append() mutates the list in place.",
            "Negative indexes count from the end.",
        ],
    },
    {
        "slug": "dicts",
        "title": "Dictionaries",
        "section": "Collections",
        "summary": "Dictionaries map keys to values.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/datastructures.html#dictionaries",
        "code": "person = {\"name\": \"Ada\", \"language\": \"Python\"}\nperson[\"year\"] = 1843\n\nfor key, value in person.items():\n    print(key, value)\n",
        "notes": [
            "dict preserves insertion order in modern Python.",
            "items() yields key/value pairs.",
        ],
    },
    {
        "slug": "classes",
        "title": "Classes",
        "section": "Classes",
        "summary": "Classes bundle data and behavior.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/classes.html",
        "code": "class Counter:\n    def __init__(self):\n        self.value = 0\n\n    def increment(self):\n        self.value += 1\n        return self.value\n\ncounter = Counter()\nprint(counter.increment())\nprint(counter.increment())\n",
        "notes": ["self is the instance being operated on.", "__init__ initializes new objects."],
    },
    {
        "slug": "exceptions",
        "title": "Exceptions",
        "section": "Errors",
        "summary": "Use try and except to handle exceptional cases.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/errors.html",
        "code": "def parse_int(text):\n    try:\n        return int(text)\n    except ValueError:\n        return None\n\nprint(parse_int(\"42\"))\nprint(parse_int(\"python\"))\n",
        "notes": ["Catch the most specific exception you can.", "Unhandled exceptions stop the current flow."],
    },
    {
        "slug": "modules",
        "title": "Modules",
        "section": "Modules",
        "summary": "Modules let you organize code and use the standard library.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/modules.html",
        "code": "import math\nfrom statistics import mean\n\nprint(math.sqrt(81))\nprint(mean([2, 4, 6]))\n",
        "notes": ["The standard library is Python's batteries-included toolbox.", "Imports are usually placed at the top of a file."],
    },
    {
        "slug": "strings",
        "title": "Strings",
        "section": "Text",
        "summary": "Strings are immutable Unicode text sequences.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/stdtypes.html#text-sequence-type-str",
        "code": "name = \"Python\"\nprint(name.lower())\nprint(f\"Hello, {name}!\")\nprint(\",\".join([\"a\", \"b\", \"c\"]))\n",
        "notes": ["f-strings interpolate expressions into text.", "String methods return new strings."],
    },

    {
        "slug": "string-formatting",
        "title": "String Formatting",
        "section": "Text",
        "summary": "f-strings format values directly inside string literals.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/inputoutput.html#formatted-string-literals",
        "code": "name = \"Ada\"\nscore = 9.5\n\nprint(f\"{name} scored {score}\")\nprint(f\"{name:>8} | {score:05.1f}\")\nprint(f\"{score = }\")\n",
        "notes": ["Use `f\"...\"` strings for most new formatting code.", "Format specifications after `:` control alignment, width, padding, and precision."],
        "walkthrough": [
            {"prose": "An f-string evaluates expressions inside braces and inserts their string form into the surrounding text.", "code": "name = \"Ada\"\nscore = 9.5\n\nprint(f\"{name} scored {score}\")"},
            {"prose": "Format specifications after `:` control presentation. Here the name is right-aligned and the score is padded with one decimal place.", "code": "print(f\"{name:>8} | {score:05.1f}\")"},
            {"prose": "The debug form `name =` is handy while learning or logging because it prints both the expression and the value.", "code": "print(f\"{score = }\")"},
        ],
    },
    {
        "slug": "comprehensions",
        "title": "Comprehensions",
        "section": "Collections",
        "summary": "Comprehensions build collections from iterables concisely.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/datastructures.html#list-comprehensions",
        "code": "squares = [n * n for n in range(6)]\neven_squares = {n: n * n for n in range(6) if n % 2 == 0}\nprint(squares)\nprint(even_squares)\n",
        "notes": ["Comprehensions combine mapping and filtering.", "Keep complex comprehensions readable."],
    },
    {
        "slug": "conditionals",
        "title": "Conditionals",
        "section": "Control Flow",
        "summary": "if, elif, and else choose which block runs.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#if-statements",
        "code": "temperature = 72\n\nif temperature < 60:\n    print(\"cold\")\nelif temperature < 80:\n    print(\"comfortable\")\nelse:\n    print(\"hot\")\n\nitems = [\"coat\", \"hat\"]\nif items:\n    print(f\"packing {len(items)} items\")\n\nstatus = \"ok\" if temperature < 90 else \"danger\"\nprint(status)\n",
        "notes": ["Python has no mandatory parentheses around conditions; the colon and indentation define the block.", "Comparison operators such as `<` and `==` can be chained, as in `0 < value < 10`.", "Keep branch bodies short; move larger work into functions so the decision remains easy to scan."],
        "walkthrough": [
            {
                "prose": "Start with the value that the branches will test. A conditional is only useful when the branch condition is visible and meaningful.",
                "code": "temperature = 72",
            },
            {
                "prose": "Use `if`, `elif`, and `else` for one ordered choice. Python tests the branches from top to bottom and runs only the first matching block.",
                "code": "if temperature < 60:\n    print(\"cold\")\nelif temperature < 80:\n    print(\"comfortable\")\nelse:\n    print(\"hot\")",
            },
            {
                "prose": "Truthiness is part of conditional flow. Empty collections are false, so `if items:` reads as “if there is anything to work with.”",
                "code": "items = [\"coat\", \"hat\"]\nif items:\n    print(f\"packing {len(items)} items\")",
            },
            {
                "prose": "Use the ternary expression when you are choosing a value. If either side needs multiple statements, use a normal `if` block instead.",
                "code": "status = \"ok\" if temperature < 90 else \"danger\"\nprint(status)",
            },
        ],
    },
    {
        "slug": "while-loops",
        "title": "While Loops",
        "section": "Control Flow",
        "summary": "while repeats as long as a condition is true.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/reference/compound_stmts.html#while",
        "code": "count = 3\nwhile count > 0:\n    print(count)\n    count -= 1\nprint(\"go\")\n",
        "notes": ["Update loop state so the condition eventually becomes false.", "break and continue also work in while loops."],
    },
    {
        "slug": "match-statements",
        "title": "Match Statements",
        "section": "Control Flow",
        "summary": "match selects cases using structural pattern matching.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#match-statements",
        "code": "command = (\"move\", 3, 4)\n\nmatch command:\n    case (\"move\", x, y):\n        print(f\"move to {x},{y}\")\n    case (\"quit\",):\n        print(\"quit\")\n    case _:\n        print(\"unknown\")\n",
        "notes": ["Patterns can destructure sequences and objects.", "case _ is the catch-all pattern."],
    },
    {
        "slug": "tuples",
        "title": "Tuples",
        "section": "Collections",
        "summary": "Tuples are ordered, immutable collections often used for records.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/datastructures.html#tuples-and-sequences",
        "code": "point = (3, 4)\nx, y = point\nprint(point)\nprint(x + y)\n",
        "notes": ["Tuple unpacking binds multiple names at once.", "A tuple's length and item identities cannot be changed in place."],
    },
    {
        "slug": "sets",
        "title": "Sets",
        "section": "Collections",
        "summary": "Sets store unique values and support set algebra.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/datastructures.html#sets",
        "code": "languages = {\"python\", \"go\", \"python\"}\ncompiled = {\"go\", \"rust\"}\nprint(sorted(languages))\nprint(sorted(languages | compiled))\nprint(\"python\" in languages)\n",
        "notes": ["Duplicates collapse to one set member.", "Use |, &, and - for union, intersection, and difference."],
    },
    {
        "slug": "slices",
        "title": "Slices",
        "section": "Collections",
        "summary": "Slices select ranges from sequences.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/introduction.html#lists",
        "code": "letters = [\"a\", \"b\", \"c\", \"d\", \"e\"]\nprint(letters[1:4])\nprint(letters[:2])\nprint(letters[::2])\n",
        "notes": ["The stop index is excluded.", "Omitted bounds default to the beginning or end."],
    },
    {
        "slug": "keyword-only-arguments",
        "title": "Keyword-only Arguments",
        "section": "Functions",
        "summary": "Use * to require selected arguments to be named.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#special-parameters",
        "code": "def connect(host, *, timeout=5, secure=True):\n    print(host, timeout, secure)\n\nconnect(\"example.com\", timeout=10)\n",
        "notes": ["Keyword-only arguments make call sites explicit.", "They are useful for options and flags."],
    },

    {
        "slug": "multiple-return-values",
        "title": "Multiple Return Values",
        "section": "Functions",
        "summary": "Python returns multiple values by returning a tuple and unpacking it.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/datastructures.html#tuples-and-sequences",
        "code": "def divide_with_remainder(total, size):\n    quotient = total // size\n    remainder = total % size\n    return quotient, remainder\n\nboxes, leftover = divide_with_remainder(17, 5)\nprint(boxes)\nprint(leftover)\n",
        "notes": ["A comma creates a tuple; `return a, b` returns one tuple containing two values.", "Unpacking at the call site gives each returned position a meaningful name."],
        "walkthrough": [
            {"prose": "Python functions can appear to return multiple values. The mechanism is simple: `return quotient, remainder` returns a tuple.", "code": "def divide_with_remainder(total, size):\n    quotient = total // size\n    remainder = total % size\n    return quotient, remainder"},
            {"prose": "Callers usually unpack the tuple immediately. The names at the call site document what each position means.", "code": "boxes, leftover = divide_with_remainder(17, 5)\nprint(boxes)\nprint(leftover)"},
        ],
    },
    {
        "slug": "closures",
        "title": "Closures",
        "section": "Functions",
        "summary": "Inner functions can remember values from an enclosing scope.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/reference/executionmodel.html#binding-of-names",
        "code": "def make_multiplier(factor):\n    def multiply(value):\n        return value * factor\n    return multiply\n\ndouble = make_multiplier(2)\ntriple = make_multiplier(3)\n\nprint(double(5))\nprint(triple(5))\n",
        "notes": ["A closure keeps access to names from the scope where the inner function was created.", "Closures are useful for callbacks, small factories, and decorators."],
        "walkthrough": [
            {"prose": "Define a function inside another function when the inner behavior needs to remember some setup value.", "code": "def make_multiplier(factor):\n    def multiply(value):\n        return value * factor\n    return multiply"},
            {"prose": "Each call creates a new closure. `double` remembers `factor == 2`, while `triple` remembers `factor == 3`.", "code": "double = make_multiplier(2)\ntriple = make_multiplier(3)"},
            {"prose": "Calling the returned function later still has access to the captured value.", "code": "print(double(5))\nprint(triple(5))"},
        ],
    },
    {
        "slug": "recursion",
        "title": "Recursion",
        "section": "Functions",
        "summary": "Recursive functions solve a problem by calling themselves with a smaller input.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#defining-functions",
        "code": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))\n",
        "notes": ["Every recursive function needs a base case that stops the calls.", "Python limits recursion depth, so loops are often better for very deep repetition."],
        "walkthrough": [
            {"prose": "A recursive function must handle the smallest case directly. Here `0!` is the base case.", "code": "def factorial(n):\n    if n == 0:\n        return 1"},
            {"prose": "The recursive case calls the same function with a smaller input, moving toward the base case.", "code": "    return n * factorial(n - 1)"},
            {"prose": "The result is built as the calls return. Recursion is elegant for tree-shaped problems, but loops are often simpler for plain counting.", "code": "print(factorial(5))"},
        ],
    },
    {
        "slug": "lambdas",
        "title": "Lambdas",
        "section": "Functions",
        "summary": "lambda creates small anonymous functions.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#lambda-expressions",
        "code": "pairs = [(\"b\", 2), (\"a\", 3), (\"c\", 1)]\nby_number = sorted(pairs, key=lambda item: item[1])\nprint(by_number)\n",
        "notes": ["Lambdas are expressions, not statements.", "They are often passed as key functions."],
    },
    {
        "slug": "generators",
        "title": "Generators",
        "section": "Iteration",
        "summary": "yield produces a lazy sequence of values.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/classes.html#generators",
        "code": "def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor value in countdown(3):\n    print(value)\n",
        "notes": ["Generator functions return iterators.", "Values are produced on demand."],
    },
    {
        "slug": "decorators",
        "title": "Decorators",
        "section": "Functions",
        "summary": "Decorators wrap or register functions using @ syntax.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/glossary.html#term-decorator",
        "code": "def loud(func):\n    def wrapper(name):\n        return func(name).upper()\n    return wrapper\n\n@loud\ndef greet(name):\n    return f\"hello {name}\"\n\nprint(greet(\"python\"))\n",
        "notes": ["@decorator is shorthand for rebinding a function.", "Frameworks often use decorators to register handlers."],
    },
    {
        "slug": "context-managers",
        "title": "Context Managers",
        "section": "Data Model",
        "summary": "with ensures setup and cleanup happen together.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/reference/datamodel.html#context-managers",
        "code": "from contextlib import contextmanager\n\n@contextmanager\ndef tag(name):\n    print(f\"<{name}>\")\n    yield\n    print(f\"</{name}>\")\n\nwith tag(\"section\"):\n    print(\"content\")\n",
        "notes": ["Files, locks, and temporary state commonly use context managers.", "__enter__ and __exit__ power the protocol."],
    },
    {
        "slug": "dataclasses",
        "title": "Dataclasses",
        "section": "Classes",
        "summary": "dataclass generates common class methods for data containers.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/dataclasses.html",
        "code": "from dataclasses import dataclass\n\n@dataclass\nclass User:\n    name: str\n    active: bool = True\n\nuser = User(\"Ada\")\nprint(user)\nprint(user.active)\n",
        "notes": ["Type annotations define dataclass fields.", "Defaults can be supplied like normal class attributes."],
    },
    {
        "slug": "type-hints",
        "title": "Type Hints",
        "section": "Types",
        "summary": "Annotations document expected types and power static analysis.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/typing.html",
        "code": "def total(numbers: list[int]) -> int:\n    return sum(numbers)\n\nprint(total([1, 2, 3]))\nprint(total.__annotations__)\n",
        "notes": ["Python does not enforce most type hints at runtime.", "Tools like type checkers and editors use annotations."],
    },
    {
        "slug": "enums",
        "title": "Enums",
        "section": "Types",
        "summary": "Enum defines symbolic names for a fixed set of values.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/enum.html",
        "code": "from enum import Enum\n\nclass Status(Enum):\n    PENDING = \"pending\"\n    DONE = \"done\"\n\nprint(Status.PENDING.name)\nprint(Status.DONE.value)\n",
        "notes": ["Enums make states and choices explicit.", "Members have names and values."],
    },

    {
        "slug": "number-parsing",
        "title": "Number Parsing",
        "section": "Standard Library",
        "summary": "int() and float() parse text into numbers and raise ValueError on bad input.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/functions.html#int",
        "code": "print(int(\"42\"))\nprint(float(\"3.5\"))\n\ntry:\n    int(\"python\")\nexcept ValueError as error:\n    print(type(error).__name__)\n",
        "notes": ["`int()` and `float()` are constructors that also parse strings.", "Catch `ValueError` when bad user input is expected and recoverable."],
        "walkthrough": [
            {"prose": "Use `int()` for whole numbers and `float()` for decimal text. Parsed values are real numbers, not strings.", "code": "print(int(\"42\"))\nprint(float(\"3.5\"))"},
            {"prose": "Bad numeric text raises `ValueError`. Catch that specific exception when invalid input is part of the normal flow.", "code": "try:\n    int(\"python\")\nexcept ValueError as error:\n    print(type(error).__name__)"},
        ],
    },
    {
        "slug": "custom-exceptions",
        "title": "Custom Exceptions",
        "section": "Errors",
        "summary": "Custom exception classes name failures that belong to your domain.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/errors.html#user-defined-exceptions",
        "code": "class EmptyCartError(Exception):\n    pass\n\ndef checkout(items):\n    if not items:\n        raise EmptyCartError(\"cart is empty\")\n    return \"paid\"\n\ntry:\n    checkout([])\nexcept EmptyCartError as error:\n    print(error)\n",
        "notes": ["Subclass `Exception` for errors callers are expected to catch.", "A custom exception name can be clearer than reusing a generic `ValueError` everywhere."],
        "walkthrough": [
            {"prose": "Create a custom exception when a failure has a name in your problem domain. The class can be empty at first.", "code": "class EmptyCartError(Exception):\n    pass"},
            {"prose": "Raise the custom exception where the invalid state is detected. The message explains this particular occurrence.", "code": "def checkout(items):\n    if not items:\n        raise EmptyCartError(\"cart is empty\")\n    return \"paid\""},
            {"prose": "Callers can catch the precise error type without accidentally catching unrelated failures.", "code": "try:\n    checkout([])\nexcept EmptyCartError as error:\n    print(error)"},
        ],
    },
    {
        "slug": "json",
        "title": "JSON",
        "section": "Standard Library",
        "summary": "json encodes and decodes JSON data.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/json.html",
        "code": "import json\n\ndata = {\"language\": \"Python\", \"versions\": [3, 13]}\ntext = json.dumps(data, sort_keys=True)\nprint(text)\nprint(json.loads(text)[\"language\"])\n",
        "notes": ["JSON maps naturally to dicts, lists, strings, numbers, booleans, and None.", "Use sort_keys for deterministic output."],
    },
    {
        "slug": "datetime",
        "title": "Dates and Times",
        "section": "Standard Library",
        "summary": "datetime represents dates, times, durations, formatting, and parsing.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/datetime.html",
        "code": "from datetime import date, datetime, time, timedelta, timezone\n\nrelease_day = date(2026, 5, 4)\nmeeting_time = time(12, 30)\ncreated_at = datetime.combine(release_day, meeting_time, tzinfo=timezone.utc)\n\nprint(release_day.isoformat())\nprint(meeting_time.isoformat())\nprint(created_at.isoformat())\n\nexpires_at = created_at + timedelta(days=7, hours=2)\nprint(expires_at.isoformat())\n\nprint(created_at.strftime(\"%Y-%m-%d %H:%M %Z\"))\nparsed = datetime.fromisoformat(\"2026-05-04T12:30:00+00:00\")\nprint(parsed == created_at)\n",
        "notes": ["Use timezone-aware datetimes for instants that cross system or user boundaries.", "Use `date` for calendar days, `time` for clock times, `datetime` for both, and `timedelta` for durations.", "Prefer ISO 8601 strings for interchange; use `strftime` for human-facing display."],
        "walkthrough": [
            {"prose": "The `datetime` module separates calendar dates, clock times, combined datetimes, and durations. Import the types you need explicitly.", "code": "from datetime import date, datetime, time, timedelta, timezone"},
            {"prose": "Use `date` for a calendar day and `time` for a time of day. Combine them into a timezone-aware `datetime` when you mean an instant.", "code": "release_day = date(2026, 5, 4)\nmeeting_time = time(12, 30)\ncreated_at = datetime.combine(release_day, meeting_time, tzinfo=timezone.utc)"},
            {"prose": "`isoformat()` produces stable machine-readable text. It is a good default for examples, APIs, and logs.", "code": "print(release_day.isoformat())\nprint(meeting_time.isoformat())\nprint(created_at.isoformat())"},
            {"prose": "Use `timedelta` for durations. Adding one to a `datetime` produces another `datetime` without manually changing calendar fields.", "code": "expires_at = created_at + timedelta(days=7, hours=2)\nprint(expires_at.isoformat())"},
            {"prose": "Use `strftime()` for human-facing formatting and `fromisoformat()` when reading ISO 8601 text back into a `datetime`.", "code": "print(created_at.strftime(\"%Y-%m-%d %H:%M %Z\"))\nparsed = datetime.fromisoformat(\"2026-05-04T12:30:00+00:00\")\nprint(parsed == created_at)"},
        ],
    },
    {
        "slug": "sorting",
        "title": "Sorting",
        "section": "Collections",
        "summary": "sorted returns a new ordered list from any iterable.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/howto/sorting.html",
        "code": "users = [{\"name\": \"Ada\", \"score\": 10}, {\"name\": \"Guido\", \"score\": 8}]\nranked = sorted(users, key=lambda user: user[\"score\"], reverse=True)\nprint(ranked[0][\"name\"])\n",
        "notes": ["key functions compute values to sort by.", "list.sort() sorts a list in place."],
    },
    {
        "slug": "itertools",
        "title": "Itertools",
        "section": "Iteration",
        "summary": "itertools provides efficient iterator building blocks.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/itertools.html",
        "code": "import itertools\n\nprint(list(itertools.islice(itertools.count(10), 3)))\nprint(list(itertools.chain([1, 2], [3])))\n",
        "notes": ["Iterator pipelines avoid building intermediate lists.", "Use islice to take a finite piece from an infinite iterator."],
    },
    {
        "slug": "iterating-over-iterables",
        "title": "Iterating over Iterables",
        "section": "Iteration",
        "summary": "for loops work with any iterable, not just numeric ranges.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#for-statements",
        "code": "names = [\"Ada\", \"Grace\", \"Guido\"]\n\n# Iterate over values directly.\nfor name in names:\n    print(name)\n\n# enumerate adds a counter without manual indexing.\nfor index, name in enumerate(names):\n    print(index, name)\n\nscores = {\"Ada\": 10, \"Grace\": 9}\n\n# items yields key/value pairs from a dictionary.\nfor name, score in scores.items():\n    print(name, score)\n",
        "notes": ["Python's for statement consumes iterables through the iterator protocol.", "Prefer enumerate() over range(len(...)) when you need an index."],
        "walkthrough": [
            {
                "prose": "Start with an ordinary list. A list is iterable, so a for loop can ask it for one value at a time.",
                "code": 'names = ["Ada", "Grace", "Guido"]',
            },
            {
                "prose": "When you only need the values, iterate over the collection directly. There is no index variable because the loop body does not need one.",
                "code": '# Iterate over values directly.\nfor name in names:\n    print(name)',
            },
            {
                "prose": "When you need both a position and a value, use enumerate(). It keeps the counter tied to iteration without manual indexing.",
                "code": '# enumerate adds a counter without manual indexing.\nfor index, name in enumerate(names):\n    print(index, name)',
            },
            {
                "prose": "Dictionaries are iterable too, but dict.items() is the clearest way to say that the loop needs keys and values together.",
                "code": 'scores = {"Ada": 10, "Grace": 9}\n\n# items yields key/value pairs from a dictionary.\nfor name, score in scores.items():\n    print(name, score)',
            },
        ],
    },

    {
        "slug": 'truthiness',
        "title": 'Truthiness',
        "section": 'Basics',
        "summary": 'Python conditions use truthiness, not only explicit booleans.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/stdtypes.html#truth-value-testing",
        "code": 'items = []\nname = "Ada"\n\nif not items:\n    print("no items")\n\nif name:\n    print("has a name")\n\nprint(bool(0))\nprint(bool(42))\n',
        "notes": ['Empty containers and zero-like numbers are false in conditions.', 'Use explicit comparisons when they communicate intent better than truthiness.'],
    },
    {
        "slug": 'equality-and-identity',
        "title": 'Equality and Identity',
        "section": 'Data Model',
        "summary": '== compares values, while is compares object identity.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/reference/expressions.html#is-not",
        "code": 'left = [1, 2, 3]\nright = [1, 2, 3]\nsame = left\n\nprint(left == right)\nprint(left is right)\nprint(left is same)\nprint(None is None)\n',
        "notes": ['Use == for ordinary value comparisons.', 'Use is primarily for singletons such as None, True, and False.'],
    },
    {
        "slug": 'mutability',
        "title": 'Mutability',
        "section": 'Data Model',
        "summary": 'Some objects can change in place, and names can share one object.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/reference/datamodel.html#objects-values-and-types",
        "code": 'first = ["python"]\nsecond = first\nsecond.append("workers")\n\nprint(first)\nprint(second)\n\ntext = "python"\ntext.upper()\nprint(text)\n',
        "notes": ['Lists and dictionaries are mutable; strings and tuples are immutable.', 'Aliasing is useful, but copy mutable containers when independent changes are needed.'],
    },
    {
        "slug": 'unpacking',
        "title": 'Unpacking',
        "section": 'Collections',
        "summary": 'Unpacking binds names from sequences and mappings concisely.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/datastructures.html#tuples-and-sequences",
        "code": 'point = (3, 4)\nx, y = point\nprint(x, y)\n\nfirst, *middle, last = [1, 2, 3, 4]\nprint(first, middle, last)\n\ndef describe(name, language):\n    print(name, language)\n\ndata = {"name": "Ada", "language": "Python"}\ndescribe(**data)\n',
        "notes": ['Starred unpacking collects the remaining values into a list.', 'Dictionary unpacking with ** is common when calling functions with structured data.'],
    },
    {
        "slug": 'args-and-kwargs',
        "title": 'Args and Kwargs',
        "section": 'Functions',
        "summary": '*args collects extra positional arguments and **kwargs collects named ones.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/tutorial/controlflow.html#arbitrary-argument-lists",
        "code": 'def report(title, *items, **metadata):\n    print(title)\n    print(items)\n    print(metadata)\n\nreport("scores", 10, 9, owner="Ada", public=True)\n',
        "notes": ['Use these tools when a function naturally accepts a flexible shape.', 'Prefer explicit parameters when the accepted arguments are known and fixed.'],
    },
    {
        "slug": 'properties',
        "title": 'Properties',
        "section": 'Classes',
        "summary": '@property exposes computed or validated attributes with normal attribute syntax.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/functions.html#property",
        "code": 'class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n\n    @property\n    def area(self):\n        return self.width * self.height\n\nbox = Rectangle(3, 4)\nprint(box.area)\n',
        "notes": ['Properties let APIs start simple and grow validation or computation later.', 'Callers access a property like an attribute, not like a method.'],
    },
    {
        "slug": 'special-methods',
        "title": 'Special Methods',
        "section": 'Data Model',
        "summary": 'Special methods connect your objects to Python syntax and built-ins.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/reference/datamodel.html#special-method-names",
        "code": 'class Bag:\n    def __init__(self, items):\n        self.items = list(items)\n\n    def __len__(self):\n        return len(self.items)\n\n    def __iter__(self):\n        return iter(self.items)\n\n    def __repr__(self):\n        return f"Bag({self.items!r})"\n\nbag = Bag(["a", "b"])\nprint(len(bag))\nprint(list(bag))\nprint(bag)\n',
        "notes": ["Dunder methods are looked up by Python's data model protocols.", 'Implement the smallest protocol that makes your object feel native.'],
    },
    {
        "slug": 'regular-expressions',
        "title": 'Regular Expressions',
        "section": 'Text',
        "summary": 'The re module searches and extracts text using regular expressions.',
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/re.html",
        "code": 'import re\n\ntext = "Ada: 10, Grace: 9"\npattern = r"([A-Za-z]+): (\\d+)"\n\nfor name, score in re.findall(pattern, text):\n    print(name, int(score))\n\nprint(bool(re.search(r"Grace", text)))\n',
        "notes": ['Use raw strings for regex patterns so backslashes are easier to read.', 'For simple substring checks, ordinary string methods are often clearer than regex.'],
    },
    {
        "slug": "async-await",
        "title": "Async Await",
        "section": "Async",
        "summary": "async def defines coroutines that can be awaited.",
        "doc_url": f"https://docs.python.org/{PYTHON_VERSION}/library/asyncio-task.html",
        "code": "import asyncio\n\nasync def answer():\n    await asyncio.sleep(0)\n    return 42\n\nprint(asyncio.run(answer()))\n",
        "notes": ["await yields control until an awaitable completes.", "Cloudflare Workers handlers are async functions."],
    },
]


EXPLANATIONS = {
    "hello-world": ["Every Python program starts by executing statements from top to bottom. Calling `print()` is the smallest useful program because it shows how Python evaluates an expression and sends text to standard output.", "Strings are ordinary values, so the message passed to `print()` can be changed, stored in a variable, or produced by a function. This example keeps the first program intentionally small."],
    "values": ["Python has a compact set of built-in value types that cover most day-to-day programs: text, numbers, booleans, and None. Operators combine these values and return new values.", "Division with / always produces a float, while boolean operators such as and and or work with truth values. None represents the absence of a value and is commonly used as a default or sentinel."],

    "numbers": ["Python's numeric model starts with `int` and `float`. Integers are arbitrary precision, while floats are the ordinary double-precision floating-point values used for approximate decimal work.", "The division operators are intentionally distinct: `/` means true division and produces a float, while `//` means floor division. `%` gives the remainder and `**` computes powers.", "Use rounding for display, not as a substitute for understanding floating-point approximation. Financial code usually needs `decimal.Decimal`, which is a later standard-library topic."],
    "booleans": ["Booleans are the values `True` and `False`. They are produced by comparisons and combined with `and`, `or`, and `not`.", "Python's logical operators short-circuit. That means the right side is evaluated only when needed, which keeps guard checks efficient and safe.", "Booleans are also connected to truthiness: many objects can be tested in conditions even when they are not literally `True` or `False`."],
    "none": ["`None` represents the absence of a value. It is the usual sentinel when a function has no result to return but the absence itself is meaningful.", "Because `None` is a singleton, idiomatic Python checks it with `is None` or `is not None`. This avoids confusing identity with value equality.", "A function that reaches the end without a `return` statement returns `None`, so explicit `None` results should be documented by names and control flow."],
    "constants": ["Python has no `const` keyword for ordinary variables. Instead, modules use all-caps names to mark values that should be treated as constants by convention.", "The interpreter will not stop rebinding, but the convention is important API communication. Readers understand that `MAX_RETRIES` is configuration, not loop state.", "Named constants remove magic values from code and give repeated literals one place to change."],
    "string-formatting": ["Formatted string literals, or f-strings, are the everyday way to combine text with Python expressions. They keep the expression close to the words it explains.", "Format specifications after `:` control presentation details such as width, alignment, padding, and precision. This is useful for reports and aligned terminal output.", "The debug form with `=` is convenient while learning because it prints both the expression and its value without writing the name twice."],
    "multiple-return-values": ["Python multiple return values are tuple return values with friendly syntax. `return a, b` creates one tuple containing two positions.", "Most callers unpack that tuple immediately. Good target names make the meaning of each returned position explicit.", "Use this for small, fixed groups of results. For larger records, a dataclass or named tuple usually communicates better."],
    "closures": ["A closure is a function that remembers names from the scope where it was created. This lets you configure behavior once and call it later.", "Each call to the outer function creates a separate remembered environment. That is why `double` and `triple` can share the same code but keep different factors.", "Closures are a foundation for decorators, callbacks, and small function factories."],
    "recursion": ["A recursive function calls itself to solve a smaller version of the same problem. The base case is the input that can be answered directly.", "The recursive case must move toward the base case. Without that progress, recursion becomes an infinite chain of calls until Python raises a recursion-depth error.", "Python supports recursion, but it does not optimize tail calls. Prefer loops for very deep or simple repetition."],
    "number-parsing": ["Parsing turns text into numeric values. `int()` parses whole-number text and `float()` parses decimal or scientific-notation text.", "Invalid numeric text raises `ValueError`. Catching that specific exception makes it clear that bad input is expected and recoverable.", "After parsing, the result is a number and can participate in arithmetic; before parsing, it is just text."],
    "custom-exceptions": ["Custom exceptions give names to failures in your problem domain. A named exception is easier to catch and explain than a generic error with only a string message.", "Raise the custom exception at the point where the invalid state is discovered. Include a message for the specific occurrence.", "Catch custom exceptions at the boundary where recovery makes sense, such as returning an error response or asking for corrected input."],
    "variables": ["Python variables are names bound to objects. Assignment creates or rebinds a name; it does not require a declaration and it does not permanently attach a type to the name.", "Augmented assignment such as += is the idiomatic way to update counters and accumulators. It reads the current binding, computes a new value or mutates in place when appropriate, and stores the result."],
    "strings": ["Python strings are immutable Unicode text sequences. Methods such as lower() and join() return new strings rather than changing the original value.", "Formatted string literals, usually called f-strings, are the common way to build readable messages from values. They evaluate expressions inside braces and convert the result to text."],
    "conditionals": ["`if`, `elif`, and `else` let a program choose one path based on a condition. Python uses indentation to show which statements belong to each branch.", "Conditions use Python truthiness: booleans work directly, and many objects such as empty lists or empty strings are considered false. Order branches from most specific to most general.", "Use `elif` to keep one decision flat instead of nested. Use Python's ternary expression only when you are choosing between two values."],
    "for-loops": ["Python for loops iterate over values from an iterable. This is different from languages where for primarily means incrementing a numeric counter.", "range() is itself an iterable that produces numbers lazily. Use it when you need a sequence of integers, but prefer direct iteration when you already have a collection."],
    "iterating-over-iterables": ["The for statement works with any iterable object: lists, strings, dictionaries, generators, files, and many standard-library helpers. This makes iteration a central Python protocol rather than a special case for arrays.", "Use enumerate() when you need positions and values together, and dict.items() when you need keys and values. These helpers express intent better than manual indexing."],
    "while-loops": ["A while loop repeats while its condition remains true. It is useful when the number of iterations is not known ahead of time, such as reading until a sentinel appears.", "The loop body should normally move the program closer to stopping. Updating state inside the loop keeps the condition meaningful and avoids accidental infinite loops."],
    "match-statements": ["match provides structural pattern matching: it compares a subject against patterns and can bind names from the matched structure. It is more expressive than a long chain of equality checks.", "Patterns are tried from top to bottom. The underscore pattern is a conventional catch-all and should usually appear last so more specific cases get a chance to match."],
    "lists": ["Lists are Python's general-purpose mutable sequence type. They preserve order, support indexing, and can grow or shrink as your program runs.", "Methods such as append() change the list in place, while functions such as sorted() return a new list. Knowing which operations mutate helps avoid surprising shared-state bugs."],
    "tuples": ["Tuples are ordered immutable sequences. They are often used when a small group of values belongs together, such as coordinates or multiple return values.", "Unpacking binds names from a tuple or other sequence in one statement. It makes code clearer when the positions have obvious meanings."],
    "dicts": ["Dictionaries map keys to values and are the standard representation for lookup tables, JSON-like records, and many configuration shapes. Modern Python preserves insertion order.", "Iterating with items() yields key/value pairs directly. This is clearer and more efficient than looping over keys and performing a second lookup for each value."],
    "sets": ["Sets store unique hashable values. They are ideal for membership tests, de-duplication, and comparing groups of items.", "Set operators mirror mathematical notation: union, intersection, and difference express common collection operations without manual loops."],
    "slices": ["Slicing extracts a range from a sequence using start, stop, and optional step. The stop index is excluded, which keeps adjacent ranges easy to compose.", "Omitted bounds default to the beginning or end of the sequence. A step can skip items or reverse a sequence when it is negative."],
    "comprehensions": ["Comprehensions build lists, dictionaries, and sets from iterables in a compact form. They combine mapping and optional filtering in one expression.", "Use comprehensions for straightforward transformations. If the expression becomes hard to read, an explicit loop is often the better teaching and maintenance choice."],
    "sorting": ["sorted() accepts any iterable and returns a new list in sorted order. The original collection is left untouched, which makes it safe to use in expressions.", "The key function tells Python what value to compare for each item. This is the idiomatic way to sort dictionaries, objects, and tuples by a specific field."],
    "functions": ["Functions package behavior behind a name. def creates a function object that can accept arguments, compute values, and return a result.", "Default and keyword arguments make call sites readable. A function that reaches the end without return produces None, which is itself a normal Python value."],
    "keyword-only-arguments": ["A bare * in a function signature marks the following parameters as keyword-only. Callers must name those arguments explicitly.", "This is useful for options such as timeouts, flags, and modes where positional calls would be ambiguous or easy to misread."],
    "lambdas": ["lambda creates a small anonymous function expression. It is most useful when a function is needed briefly, such as a sort key or callback.", "Because lambdas are limited to one expression, they should stay simple. Use def when the behavior needs a name, statements, or explanation."],
    "generators": ["A generator function uses yield to produce values lazily. Calling the function returns an iterator; the body runs only as values are requested.", "Generators are useful for pipelines, large inputs, and infinite sequences because they avoid building an entire collection in memory."],
    "itertools": ["The itertools module contains iterator building blocks for combining, slicing, grouping, and repeating streams of values. These tools pair naturally with for loops and generators.", "Many itertools functions are lazy, including count() and chain(). Use helpers such as islice() to take a finite window from an infinite iterator."],
    "decorators": ["A decorator is a callable that receives a function and returns a replacement. The @ syntax applies that transformation at function definition time.", "Decorators are common in frameworks because they can register handlers or add behavior while keeping the decorated function focused on the core action."],
    "classes": ["Classes define new types that combine data and behavior. Methods are functions stored on the class and receive the instance as their first argument, conventionally named self.", "__init__ initializes each new instance. Instance attributes such as self.value belong to the object, so different Counter instances can hold different state."],
    "dataclasses": ["dataclass is a standard-library decorator for classes that mainly store data. It generates methods such as __init__ and __repr__ from type-annotated fields.", "Dataclasses reduce boilerplate while keeping classes explicit. They are a good fit for simple records, configuration objects, and values passed between layers."],
    "context-managers": ["Context managers define setup and cleanup around a block of code. The with statement guarantees that cleanup runs when the block exits, even when an exception is raised.", "The contextlib.contextmanager decorator is a concise way to write context managers as generators. Production code often uses with for files, locks, transactions, and temporary state."],
    "exceptions": ["Exceptions represent errors or unusual conditions that interrupt normal control flow. try and except let you recover at the point where recovery makes sense.", "Catch specific exceptions whenever possible. A broad catch can hide programming mistakes, while a targeted ValueError handler documents exactly what failure is expected."],
    "modules": ["Modules organize Python code into files and namespaces. import executes a module once and then gives your program access to its definitions.", "The standard library is large and intentionally useful. Importing focused tools such as math.sqrt or statistics.mean keeps examples small while relying on well-tested implementations."],
    "type-hints": ["Type hints are annotations that document expected shapes for values, parameters, and return results. Python stores many annotations but does not enforce most of them at runtime.", "Editors, linters, and type checkers use annotations to catch mistakes earlier. They are especially valuable at API boundaries and in larger codebases."],
    "enums": ["Enum defines a fixed set of named values. This makes states and modes easier to read than raw strings scattered through a program.", "Each enum member has a name and a value. Comparing enum members is explicit and helps avoid typos that plain strings would allow."],

    "truthiness": ["Truthiness is one of Python's most important conveniences: conditions can test objects directly instead of requiring explicit boolean comparisons everywhere.", "Empty containers, numeric zero, None, and False are false; most other values are true. This makes common checks such as if items: concise and idiomatic.", "Use truthiness when it reads naturally, but choose explicit comparisons when the distinction matters, such as checking whether a value is exactly None."],
    "equality-and-identity": ["Python separates equality from identity. Equality asks whether two objects should be considered the same value, while identity asks whether two names point to the same object.", "This distinction matters for mutable containers because two equal lists can still be independent objects. Mutating one should not imply mutating the other unless they share identity.", "The is operator is best reserved for identity checks against singletons such as None. For ordinary values, == is the comparison readers expect."],
    "mutability": ["Objects in Python can be mutable or immutable. Mutable objects such as lists can change in place, while immutable objects such as strings produce new values instead.", "Names can share one mutable object, so a change through one name is visible through another. This is powerful, but it is also the source of many beginner surprises.", "Understanding mutability explains why copying containers, avoiding mutable defaults, and returning new values are recurring Python design choices."],
    "unpacking": ["Unpacking binds multiple names from one iterable or mapping. It makes the structure of data visible at the point where values are introduced.", "Starred unpacking handles variable-length sequences by collecting the middle or remaining values. This keeps common head-tail patterns readable.", "Dictionary unpacking with ** connects structured data to function calls. It is widely used in configuration, adapters, and code that bridges APIs."],
    "args-and-kwargs": ["*args and **kwargs let a function accept flexible positional and keyword arguments. They are the function-call counterpart to unpacking.", "These parameters are useful for wrappers, decorators, logging helpers, and APIs that forward arguments to another function.", "They should not replace clear signatures. If a function has a stable interface, explicit parameters document expectations better than a bag of arguments."],
    "properties": ["Properties let a class expose computed data through attribute access. Callers write obj.area, while the class still runs code to produce the value.", "This keeps public APIs pleasant without giving up the ability to validate, derive, or later change how a value is stored.", "Use properties for cheap, attribute-like operations. Expensive work or actions with side effects should usually remain explicit methods."],
    "special-methods": ["Special methods, often called dunder methods, connect user-defined classes to Python syntax and built-ins such as len(), iter(), and repr().", "Implementing these methods lets your objects participate in Python protocols rather than forcing callers to learn custom method names for common operations.", "Good special methods make objects feel boring in the best way: they work with the language features Python programmers already know."],
    "regular-expressions": ["Regular expressions are a compact language for searching and extracting text patterns. Python's re module provides the standard interface.", "Regex is powerful for structured text with repeated patterns, such as names followed by numbers. Capturing groups return just the pieces you care about.", "They are not always the right tool. Prefer ordinary string methods when the pattern is simple, because simpler code is easier to maintain."],
    "json": ["The json module converts between Python values and JSON text. Dictionaries, lists, strings, numbers, booleans, and None map naturally to JSON structures.", "Use dumps() when you need a string and loads() when you need Python objects back. Deterministic options such as sort_keys make output stable for examples and tests."],
    "datetime": ["The `datetime` module covers several related ideas: `date` for calendar days, `time` for clock times, `datetime` for both together, and `timedelta` for durations.", "Timezone-aware datetimes avoid ambiguity in real systems. `timezone.utc` is a clear default for examples because output stays stable and portable.", "Use ISO formatting for interchange, `strftime()` for display, and parsing helpers such as `fromisoformat()` to turn text back into datetime objects."],
    "async-await": ["async def creates a coroutine function, and await pauses that coroutine until another awaitable completes. This lets one worker handle other tasks while waiting for I/O.", "Cloudflare Workers handlers are asynchronous, so understanding await is practical for fetch calls, bindings, and service interactions even when a small example only sleeps briefly."],
}

def _code_chunks(code):
    return [chunk for chunk in code.strip().split("\n\n") if chunk.strip()]


for example in EXAMPLES:
    explanation = list(EXPLANATIONS[example["slug"]])
    if len(explanation) < 3:
        explanation.append(" ".join(example.get("notes", [])))
    chunks = _code_chunks(example["code"])
    if "walkthrough" not in example:
        example["walkthrough"] = [
            {
                "prose": explanation[min(index, len(explanation) - 1)],
                "code": chunk,
            }
            for index, chunk in enumerate(chunks)
        ]
    example["explanation"] = explanation

SLUG_ORDER = [
    "hello-world",
    "values",
    "numbers",
    "booleans",
    "none",
    "variables",
    "constants",
    "truthiness",
    "equality-and-identity",
    "mutability",
    "strings",
    "string-formatting",
    "conditionals",
    "for-loops",
    "iterating-over-iterables",
    "match-statements",
    "while-loops",
    "lists",
    "tuples",
    "unpacking",
    "dicts",
    "sets",
    "slices",
    "comprehensions",
    "sorting",
    "functions",
    "keyword-only-arguments",
    "args-and-kwargs",
    "multiple-return-values",
    "closures",
    "recursion",
    "lambdas",
    "generators",
    "itertools",
    "decorators",
    "classes",
    "dataclasses",
    "properties",
    "special-methods",
    "context-managers",
    "exceptions",
    "modules",
    "type-hints",
    "enums",
    "regular-expressions",
    "number-parsing",
    "custom-exceptions",
    "json",
    "datetime",
    "async-await",
]

def _expected_output(code):
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        exec(code, {"__name__": "__main__"})
    return stdout.getvalue()



_EXAMPLE_IMPROVEMENTS = {
    "values": {
        "code": "text = \"python\"\ncount = 3\nratio = 2.5\nready = True\nmissing = None\n\nprint(text.upper())\nprint(count + 4)\nprint(ratio * 2)\nprint(ready and count > 0)\nprint(missing is None)\n",
        "notes": ["Values are objects; names point to them and operations usually create new values.", "Use `is None` for the absence marker, not `== None`.", "A small value tour should make later pages feel familiar, not replace the dedicated pages for numbers, strings, and booleans."],
        "explanation": ["A Python program works by evaluating expressions into values. The most common first values are text, integers, floats, booleans, and `None`.", "Operators and method calls produce more values. `text.upper()` returns a new string, arithmetic returns numbers, and comparisons or logical operators return booleans.", "`None` is a real singleton value used to mean “no value here.” Checking it with `is None` introduces identity before the later equality and mutability examples."],
        "walkthrough": [
            {"prose": "Start with several built-in values. Python does not require declarations before binding these names.", "code": "text = \"python\"\ncount = 3\nratio = 2.5\nready = True\nmissing = None"},
            {"prose": "Methods and operators evaluate to new values. The original `text`, `count`, and `ratio` bindings remain ordinary objects you can reuse.", "code": "print(text.upper())\nprint(count + 4)\nprint(ratio * 2)"},
            {"prose": "Boolean expressions combine facts, and `None` is checked by identity because it is a singleton absence marker.", "code": "print(ready and count > 0)\nprint(missing is None)"},
        ],
    },
    "strings": {
        "code": "language = \"Python\"\nmessage = \"  Python by Example  \"\n\nprint(language[0])\nprint(language.lower())\nprint(message.strip())\nprint(f\"Hello, {language}!\")\nprint(\", \".join([\"lists\", \"dicts\", \"sets\"]))\n",
        "notes": ["Strings are sequences of Unicode characters, so indexing and many sequence operations work.", "String methods return new strings because strings are immutable.", "Use `join()` when building text from many pieces; it makes the separator explicit."],
        "explanation": ["Python strings are immutable Unicode text sequences. That means they behave like sequences for reading, but operations such as `lower()` and `strip()` create new strings instead of changing the original.", "Common string work is transformation and composition: normalize case, remove surrounding whitespace, interpolate values, and join pieces with a separator.", "Because strings are immutable, you can pass them around safely without worrying that another function will alter the object in place."],
        "walkthrough": [
            {"prose": "Strings store Unicode text and can be indexed like other sequences.", "code": "language = \"Python\"\nmessage = \"  Python by Example  \"\n\nprint(language[0])"},
            {"prose": "Methods such as `lower()` and `strip()` return transformed strings. They do not mutate the original value.", "code": "print(language.lower())\nprint(message.strip())"},
            {"prose": "Use f-strings for readable interpolation and `join()` when a separator belongs between several pieces.", "code": "print(f\"Hello, {language}!\")\nprint(\", \".join([\"lists\", \"dicts\", \"sets\"]))"},
        ],
    },
    "match-statements": {
        "code": "command = {\"action\": \"move\", \"x\": 3, \"y\": 4}\n\nmatch command:\n    case {\"action\": \"move\", \"x\": x, \"y\": y}:\n        print(f\"move to {x},{y}\")\n    case {\"action\": \"quit\"}:\n        print(\"quit\")\n    case {\"action\": action}:\n        print(f\"unknown action: {action}\")\n    case _:\n        print(\"invalid command\")\n",
        "notes": ["`match` compares structure, not just equality.", "Patterns can bind names such as `x` and `y` while matching.", "Put the catch-all `_` case last, because cases are tried from top to bottom."],
        "explanation": ["Structural pattern matching lets a program choose a branch based on the shape of data. It is especially useful when commands, messages, or parsed data have a few known forms.", "A `case` pattern can both check constants and bind names. The move case checks the action and extracts `x` and `y` in one readable step.", "Order matters because Python tries cases from top to bottom. Specific shapes should appear before broad fallback cases such as `_`."],
        "walkthrough": [
            {"prose": "Use `match` when the shape of a value is the decision. This command is a dictionary with an action and coordinates.", "code": "command = {\"action\": \"move\", \"x\": 3, \"y\": 4}"},
            {"prose": "A mapping pattern can check required keys and bind values from them. Here `x` and `y` become ordinary local names in the block.", "code": "match command:\n    case {\"action\": \"move\", \"x\": x, \"y\": y}:\n        print(f\"move to {x},{y}\")"},
            {"prose": "Other cases describe other valid shapes. A broader action case can report an unknown command while still extracting the action name.", "code": "    case {\"action\": \"quit\"}:\n        print(\"quit\")\n    case {\"action\": action}:\n        print(f\"unknown action: {action}\")"},
            {"prose": "The `_` pattern is the catch-all. Keep it last so specific patterns have a chance to match first.", "code": "    case _:\n        print(\"invalid command\")"},
        ],
    },
    "dicts": {
        "code": "profile = {\"name\": \"Ada\", \"language\": \"Python\"}\nprofile[\"year\"] = 1843\n\nprint(profile[\"name\"])\nprint(profile.get(\"timezone\", \"UTC\"))\n\nfor key, value in profile.items():\n    print(f\"{key}: {value}\")\n",
        "notes": ["Dictionaries preserve insertion order in modern Python.", "Use `get()` when a missing key has a reasonable default.", "Use direct indexing when a missing key should be treated as an error."],
        "explanation": ["Dictionaries are Python's built-in mapping type. They connect keys to values and are the natural shape for records, lookup tables, and JSON-like data.", "Direct indexing communicates that a key must exist. `get()` communicates that absence is expected and supplies a default value.", "Iterating with `items()` gives each key and value together, which is clearer than looping over keys and indexing again."],
        "walkthrough": [
            {"prose": "Create a dictionary with literal key/value pairs, then add another key by assignment.", "code": "profile = {\"name\": \"Ada\", \"language\": \"Python\"}\nprofile[\"year\"] = 1843"},
            {"prose": "Use `[]` for required keys and `get()` when a missing key can use a default.", "code": "print(profile[\"name\"])\nprint(profile.get(\"timezone\", \"UTC\"))"},
            {"prose": "Use `items()` when the loop needs both the key and the value.", "code": "for key, value in profile.items():\n    print(f\"{key}: {value}\")"},
        ],
    },
    "while-loops": {
        "code": "remaining = 3\n\nwhile remaining > 0:\n    print(f\"launch in {remaining}\")\n    remaining -= 1\n\nprint(\"liftoff\")\n",
        "notes": ["Use `while` when the stopping condition matters more than a fixed iterable.", "Update loop state inside the body so the condition can become false.", "Prefer `for` when you already have a collection or range to consume."],
        "explanation": ["A `while` loop repeats as long as its condition remains true. It is useful when you are waiting for state to change rather than consuming an existing iterable.", "The loop body must make progress toward the stopping condition. Here decrementing `remaining` prevents an infinite loop.", "Many Python loops should be `for` loops, but `while` is the right tool for countdowns, sentinels, polling, and other condition-driven repetition."],
        "walkthrough": [
            {"prose": "Start with the state that controls the loop. The condition will be checked before every iteration.", "code": "remaining = 3"},
            {"prose": "The body runs while the condition is true. Updating `remaining` moves the program toward stopping.", "code": "while remaining > 0:\n    print(f\"launch in {remaining}\")\n    remaining -= 1"},
            {"prose": "Execution continues after the loop once the condition becomes false.", "code": "print(\"liftoff\")"},
        ],
    },
    "lists": {
        "code": "numbers = [3, 1, 4]\nnumbers.append(1)\n\nprint(numbers)\nprint(numbers[0])\nprint(numbers[-1])\nprint(sorted(numbers))\nprint(numbers)\n",
        "notes": ["Lists are mutable sequences: methods such as `append()` change the list in place.", "Negative indexes count from the end.", "`sorted()` returns a new list; `list.sort()` sorts the existing list in place."],
        "explanation": ["Lists are Python's general-purpose mutable sequence type. Use them when order matters and the collection may grow, shrink, or be rearranged.", "Indexing reads individual positions. `0` is the first item, and negative indexes count backward from the end.", "Mutation and copying matter: `append()` changes the list, while `sorted()` returns a new ordered list and leaves the original alone."],
        "walkthrough": [
            {"prose": "Create a list with square brackets. Because lists are mutable, `append()` changes this same list object.", "code": "numbers = [3, 1, 4]\nnumbers.append(1)\n\nprint(numbers)"},
            {"prose": "Use indexes to read positions. Negative indexes are convenient for reading from the end.", "code": "print(numbers[0])\nprint(numbers[-1])"},
            {"prose": "Use `sorted()` when you want an ordered copy and still need the original order afterward.", "code": "print(sorted(numbers))\nprint(numbers)"},
        ],
    },
    "tuples": {
        "code": "point = (3, 4)\nred = (255, 0, 0)\n\nx, y = point\nprint(x + y)\nprint(red)\nprint(point == (3, 4))\n",
        "notes": ["Tuples are immutable sequences with fixed length.", "Use tuples for small records where position has meaning.", "Unpacking gives names to tuple positions at the point of use."],
        "explanation": ["Tuples are ordered immutable sequences. They are useful for small fixed records such as coordinates, colors, or multiple return values.", "Unpacking turns positional data into named local variables. That makes tuple use readable when each position has a clear meaning.", "Because tuples are immutable, their length and item references cannot be changed in place after creation."],
        "walkthrough": [
            {"prose": "Use tuples for fixed-size groups where the positions are part of the meaning.", "code": "point = (3, 4)\nred = (255, 0, 0)"},
            {"prose": "Unpacking gives useful names to tuple positions instead of leaving readers to remember indexes.", "code": "x, y = point\nprint(x + y)"},
            {"prose": "Tuples compare by value and keep their fixed structure.", "code": "print(red)\nprint(point == (3, 4))"},
        ],
    },
    "sets": {
        "code": "languages = {\"python\", \"go\", \"python\"}\ncompiled = {\"go\", \"rust\"}\n\nprint(sorted(languages))\nprint(\"python\" in languages)\nprint(sorted(languages | compiled))\nprint(sorted(languages & compiled))\nprint(sorted(languages - compiled))\n",
        "notes": ["Sets remove duplicates and support fast membership tests.", "Set algebra operators make union, intersection, and difference explicit.", "Sets are unordered, so sort them when examples need deterministic display."],
        "explanation": ["Sets store unique hashable values. Use them when membership and de-duplication matter more than order.", "The `in` operator is the everyday membership test. Set algebra then expresses how groups relate to each other.", "Because sets are unordered, examples often wrap output in `sorted()` so the display is deterministic."],
        "walkthrough": [
            {"prose": "Creating a set automatically removes duplicates. The repeated `python` value appears only once.", "code": "languages = {\"python\", \"go\", \"python\"}\ncompiled = {\"go\", \"rust\"}\n\nprint(sorted(languages))"},
            {"prose": "Membership checks are the most common set operation.", "code": "print(\"python\" in languages)"},
            {"prose": "Union, intersection, and difference describe relationships between groups without manual loops.", "code": "print(sorted(languages | compiled))\nprint(sorted(languages & compiled))\nprint(sorted(languages - compiled))"},
        ],
    },
    "slices": {
        "code": "letters = [\"a\", \"b\", \"c\", \"d\", \"e\"]\n\nprint(letters[1:4])\nprint(letters[:2])\nprint(letters[2:])\nprint(letters[::2])\nprint(letters[::-1])\n",
        "notes": ["Slice stop indexes are excluded, so adjacent ranges compose cleanly.", "Omitted bounds mean the beginning or end of the sequence.", "A negative step walks backward through the sequence."],
        "explanation": ["Slicing reads a range from a sequence with `start:stop:step`. It is one of Python's most compact tools for working with ordered data.", "The stop index is excluded. This convention makes lengths and adjacent slices easier to reason about.", "Omitted bounds default to the beginning or end, and the optional step can skip items or reverse a sequence."],
        "walkthrough": [
            {"prose": "Start with an ordered sequence. Slices return selected ranges without changing the original list.", "code": "letters = [\"a\", \"b\", \"c\", \"d\", \"e\"]"},
            {"prose": "The stop index is excluded. Omitting a bound means “from the beginning” or “through the end.”", "code": "print(letters[1:4])\nprint(letters[:2])\nprint(letters[2:])"},
            {"prose": "The step controls how the slice moves. A step of `2` skips, and `-1` walks backward.", "code": "print(letters[::2])\nprint(letters[::-1])"},
        ],
    },
    "classes": {
        "code": "class Counter:\n    def __init__(self, start=0):\n        self.value = start\n\n    def increment(self, amount=1):\n        self.value += amount\n        return self.value\n\nfirst = Counter()\nsecond = Counter(10)\n\nprint(first.increment())\nprint(second.increment(5))\n",
        "notes": ["`self` is the instance the method is operating on.", "`__init__` initializes each new object.", "Instance attributes belong to one object, not to the class as a whole."],
        "explanation": ["Classes define new object types by bundling data with behavior. They are useful when several values and operations belong together.", "`__init__` initializes each instance, and methods receive the instance as `self`. Assigning `self.value` stores state on that particular object.", "Separate instances keep separate state. Mutating one `Counter` does not change another because each object has its own attributes."],
        "walkthrough": [
            {"prose": "Define a class when data and behavior should travel together. The initializer gives each object its starting state.", "code": "class Counter:\n    def __init__(self, start=0):\n        self.value = start"},
            {"prose": "Methods are functions attached to the class. `self` is the particular object receiving the method call.", "code": "    def increment(self, amount=1):\n        self.value += amount\n        return self.value"},
            {"prose": "Each instance has independent state, so these two counters can advance differently.", "code": "first = Counter()\nsecond = Counter(10)\n\nprint(first.increment())\nprint(second.increment(5))"},
        ],
    },
}

_EXECUTABLE_CELL_IMPROVEMENTS = {
    "match-statements": {
        "walkthrough": [
            {
                "prose": "Use `match` when the shape of a value is the decision. This command is a dictionary with an action and coordinates; the first case checks that shape and binds `x` and `y`.",
                "code": "command = {\"action\": \"move\", \"x\": 3, \"y\": 4}\n\nmatch command:\n    case {\"action\": \"move\", \"x\": x, \"y\": y}:\n        print(f\"move to {x},{y}\")",
            },
            {
                "prose": "Other cases describe other valid shapes. This complete fragment changes the command so the `quit` case is the first matching pattern.",
                "code": "command = {\"action\": \"quit\"}\n\nmatch command:\n    case {\"action\": \"move\", \"x\": x, \"y\": y}:\n        print(f\"move to {x},{y}\")\n    case {\"action\": \"quit\"}:\n        print(\"quit\")",
            },
            {
                "prose": "Broader patterns and the `_` catch-all belong after specific cases. This fragment extracts an unknown action before the final fallback would run.",
                "code": "command = {\"action\": \"jump\"}\n\nmatch command:\n    case {\"action\": \"move\", \"x\": x, \"y\": y}:\n        print(f\"move to {x},{y}\")\n    case {\"action\": \"quit\"}:\n        print(\"quit\")\n    case {\"action\": action}:\n        print(f\"unknown action: {action}\")\n    case _:\n        print(\"invalid command\")",
            },
        ],
    },
    "recursion": {
        "walkthrough": [
            {
                "prose": "A recursive function must handle the smallest case directly. Here `0!` is the base case, so the function can answer without another call.",
                "code": "def factorial(n):\n    if n == 0:\n        return 1\n\nprint(factorial(0))",
            },
            {
                "prose": "The recursive case calls the same function with a smaller input, moving toward the base case. The result is built as the calls return.",
                "code": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))",
            },
        ],
    },
    "classes": {
        "walkthrough": [
            {
                "prose": "Define a class when data and behavior should travel together. The initializer gives each object its starting state.",
                "code": "class Counter:\n    def __init__(self, start=0):\n        self.value = start\n\nfirst = Counter()\nsecond = Counter(10)\nprint(first.value)\nprint(second.value)",
            },
            {
                "prose": "Methods are functions attached to the class. `self` is the particular object receiving the method call, so separate instances keep separate state.",
                "code": "class Counter:\n    def __init__(self, start=0):\n        self.value = start\n\n    def increment(self, amount=1):\n        self.value += amount\n        return self.value\n\nfirst = Counter()\nsecond = Counter(10)\nprint(first.increment())\nprint(second.increment(5))",
            },
        ],
    },
    "properties": {
        "walkthrough": [
            {
                "prose": "A class can store ordinary attributes during initialization. Callers read those attributes directly when they are plain data.",
                "code": "class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n\nbox = Rectangle(3, 4)\nprint(box.width)\nprint(box.height)",
            },
            {
                "prose": "A property exposes computed data through attribute access. Callers write `box.area`, while the class still runs code to derive the value.",
                "code": "class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n\n    @property\n    def area(self):\n        return self.width * self.height\n\nbox = Rectangle(3, 4)\nprint(box.area)",
            },
        ],
    },
    "special-methods": {
        "walkthrough": [
            {
                "prose": "Start with a normal class that stores its data. Special methods build on ordinary instance state.",
                "code": "class Bag:\n    def __init__(self, items):\n        self.items = list(items)\n\nbag = Bag([\"a\", \"b\"])\nprint(bag.items)",
            },
            {
                "prose": "Implement `__len__` to let `len()` ask the object for its size using Python's standard protocol.",
                "code": "class Bag:\n    def __init__(self, items):\n        self.items = list(items)\n\n    def __len__(self):\n        return len(self.items)\n\nbag = Bag([\"a\", \"b\"])\nprint(len(bag))",
            },
            {
                "prose": "Implement `__iter__` to make the object iterable. Then tools such as `list()` can consume it without a custom method name.",
                "code": "class Bag:\n    def __init__(self, items):\n        self.items = list(items)\n\n    def __len__(self):\n        return len(self.items)\n\n    def __iter__(self):\n        return iter(self.items)\n\nbag = Bag([\"a\", \"b\"])\nprint(list(bag))",
            },
            {
                "prose": "Implement `__repr__` to give the object a useful developer-facing representation when it is printed or inspected.",
                "code": "class Bag:\n    def __init__(self, items):\n        self.items = list(items)\n\n    def __len__(self):\n        return len(self.items)\n\n    def __iter__(self):\n        return iter(self.items)\n\n    def __repr__(self):\n        return f\"Bag({self.items!r})\"\n\nbag = Bag([\"a\", \"b\"])\nprint(bag)",
            },
        ],
    },
    "type-hints": {
        "walkthrough": [
            {
                "prose": "Type hints document expected parameter and return shapes. Python still runs the function normally at runtime.",
                "code": "def total(numbers: list[int]) -> int:\n    return sum(numbers)\n\nprint(total([1, 2, 3]))",
            },
            {
                "prose": "Python stores annotations on the function object for tools and introspection, but it does not enforce most hints by itself.",
                "code": "def total(numbers: list[int]) -> int:\n    return sum(numbers)\n\nprint(total.__annotations__)",
            },
        ],
    },
}
for slug, improvement in _EXECUTABLE_CELL_IMPROVEMENTS.items():
    _EXAMPLE_IMPROVEMENTS.setdefault(slug, {}).update(improvement)

for example in EXAMPLES:
    if example["slug"] in _EXAMPLE_IMPROVEMENTS:
        example.update(_EXAMPLE_IMPROVEMENTS[example["slug"]])

_EXAMPLE_ORDER = {slug: index for index, slug in enumerate(SLUG_ORDER)}
EXAMPLES = sorted(EXAMPLES, key=lambda example: _EXAMPLE_ORDER.get(example["slug"], 999))
for example in EXAMPLES:
    example.setdefault("expected_output", _expected_output(example["code"]))
EXAMPLES_BY_SLUG = {example["slug"]: example for example in EXAMPLES}
