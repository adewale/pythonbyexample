# Similar example-driven language learning sites

Compared on: tightness of examples, prose/code proximity, runnable feedback, official-doc alignment, and breadth.

| Site | URL | Relative strengths | Relative weaknesses vs Python By Example / Go By Example |
|---|---|---|---|
| Go By Example | https://gobyexample.com/ | Best-in-class pacing; prose sits beside the exact code it explains; deterministic output; broad language tour. | Go-specific; source is static rather than editable in-place. |
| Rust By Example | https://doc.rust-lang.org/rust-by-example/ | Authoritative for Rust; strong progression; many examples are runnable in the Rust Playground. | More chapter/tutorial-like than Go By Example; pages can be longer and denser. |
| Kotlin Tour / former Kotlin By Example route | https://kotlinlang.org/docs/kotlin-tour-welcome.html | Official, modern, clear language tour with runnable playground affordances in Kotlin ecosystem. | Less minimal than Go By Example; topic pages are broader and less consistently example-card shaped. |
| Nim By Example | https://nim-by-example.github.io/ | Close in spirit to Go By Example; concise pages and broad language feature coverage. | Visual/editorial polish is simpler; less official than language docs. |
| Ruby by Example | https://ruby-by-example.netlify.app/ | Directly matches the X By Example pattern; compact table of Ruby topics including hello world, types, variables, control flow, blocks, arrays, hashes, files, modules, and OOP. | Less polished and less authoritative than Go By Example; appears community-hosted; explanations are thinner and it lacks our official-doc/runtime integration. |
| Learn X By Example: Ruby | https://learnxbyexample.com/ruby/ | Larger multi-language X By Example catalog with a Ruby section; useful for topic inspiration and cross-language consistency. | More generated/aggregated in feel; weaker identity and editorial craft than Go By Example. |
| Zig by Example | https://zig-by-example.com/ | Focused example catalog for Zig with practical snippets. | Availability/hosting may be inconsistent; less canonical than official docs; smaller ecosystem signal. |
| Elixir School | https://elixirschool.com/en/ | Excellent community-maintained curriculum; strong conceptual explanations across language and ecosystem. | Lesson/course format rather than tiny one-concept examples; not as terse as Go By Example. |
| Crystal language tutorials | https://crystal-lang.org/reference/latest/tutorials/basics/ | Official, clean basics tour for a Python/Ruby-like compiled language. | More documentation narrative than X By Example; fewer isolated runnable snippets. |
| C# Tour | https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/tutorials/ | Official, polished, often interactive via Microsoft Learn tooling. | Platform-heavy; not as compact or linear as Go By Example. |
| TypeScript Handbook intro | https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html | Official, precise, good for type-system concepts. | Handbook style; examples teach TS differences more than a complete language-by-example progression. |
| Dart language tour | https://dart.dev/language | Official and comprehensive; modern docs with many focused examples. | Reference/tutorial hybrid; longer pages, less immediate output orientation. |
| Scala By Example | https://www.scala-lang.org/docu/files/ScalaByExample.pdf | Historically important example-driven Scala text. | PDF/book format; not interactive; older and less web-native. |
| Learn X in Y Minutes | https://learnxinyminutes.com/ | Huge multi-language coverage; extremely compact code-first introductions. | Too compressed for most beginners; prose/code proximity is good, but depth, official links, and runnable output are limited. |
| AMP documentation examples / former AMP By Example | https://amp.dev/documentation/examples/ | Excellent example catalog for a web platform: searchable examples, live previews, source-oriented learning, and strong connection to official documentation. It shows how example pages can double as practical reference material. | Platform/component examples rather than a programming-language tour; pages are more product-doc/task oriented and less literate than Go By Example. |

Python-specific comparison sites remain relevant:

| Site | URL | Relative strengths | Relative weaknesses |
|---|---|---|---|
| Python official tutorial | https://docs.python.org/3/tutorial/ | Authoritative, precise, maintained with the language. | Longer narrative; not a quick standalone example catalog; no built-in playground. |
| Python Standard Library docs | https://docs.python.org/3/library/ | Complete authority for modules and edge cases. | Reference-first rather than lesson-first. |
| Real Python | https://realpython.com/ | Deep explanations, practical context, strong editorial quality. | Long-form articles; not a concise example catalog. |
| Programiz Python examples | https://www.programiz.com/python-programming/examples | Beginner-friendly tasks; many small examples. | Problem/algorithm focused more than language-abstraction focused. |
| W3Schools Python examples | https://www.w3schools.com/python/python_examples.asp | Very approachable; many interactive snippets. | Less authoritative and less cohesive than Go By Example. |
| PyMOTW-3 | https://pymotw.com/3/ | Strong standard-library coverage with focused module examples. | Module-reference focus; less suited as a beginner language progression. |

Positioning for this project: keep Go By Example's compact language tour, borrow Rust/Kotlin's expectation that examples can run, preserve Python-doc authority, and avoid course-like sprawl.
