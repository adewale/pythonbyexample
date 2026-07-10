+++
slug = "subprocesses"
title = "Subprocesses"
section = "Standard Library"
summary = "subprocess runs external commands with explicit arguments and captured outputs."
doc_path = "/library/subprocess.html"
see_also = [
  "virtual-environments",
  "networking",
  "threads-and-processes",
]
expected_output = "child process\n0\n"
+++

`subprocess` is the standard boundary for running external commands. It starts another program, waits for it, and gives you a result object with the exit code and captured output.

In standard Python this is the right tool for calling Git, compilers, shells, or another Python interpreter. This site's live example runner does not expose an operating-system process table, so the page teaches the proper `subprocess.run()` contract and labels the runner boundary instead of pretending the command can run here.

Use a list of arguments when possible, capture output when the parent program needs to inspect it, and treat a non-zero return code as a failure. The important boundary is between Python objects and the operating system: Python prepares arguments and environment, then the child program reports back through streams and an exit status.

:::program
```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print('child process')"],
    text=True,
    capture_output=True,
    check=True,
)

print(result.stdout.strip())
print(result.returncode)
```
:::

:::cell
`subprocess.run()` spawns a child Python interpreter and waits for it: `capture_output=True` stores the child's stdout and stderr on the result, `text=True` decodes them as strings, and `check=True` raises `CalledProcessError` on a non-zero exit. The result object carries the captured streams and exit code as portable evidence the child ran. The in-browser Run button cannot spawn processes, so pressing Run here fails in the sandbox; the output below was produced by really spawning the child under standard CPython when the example was verified.

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print('child process')"],
    text=True,
    capture_output=True,
    check=True,
)

print(result.stdout.strip())
print(result.returncode)
```

```output
child process
0
```
:::

:::note
- Use a list of arguments instead of shell strings when possible.
- Capture output when the parent program needs to inspect it.
- `check=True` turns non-zero exits into exceptions.
- The verified output came from a real child process under standard CPython at build time; the in-browser sandbox has no process table, so live runs of this page fail there.
:::
