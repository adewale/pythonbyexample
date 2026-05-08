+++
slug = "subprocesses"
title = "Subprocesses"
section = "Standard Library"
summary = "subprocess runs external commands with explicit arguments and captured outputs."
doc_path = "/library/subprocess.html"
expected_output = "child process\n0\n"
+++

`subprocess` is the standard boundary for running external commands. It starts another program, waits for it, and gives you a result object with the exit code and captured output.

Use a list of arguments when possible, capture output when the parent program needs to inspect it, and treat a non-zero return code as a failure. The same ideas apply whether the child program is Python, Git, a compiler, or another command-line tool.

The important boundary is between Python objects and the operating system process table. Python prepares arguments and environment, then the child program runs independently and reports back through streams and an exit status.

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

:::unsupported
Dynamic Workers do not provide child processes.

```python
result = subprocess.run(
    [sys.executable, "-c", "print('child process')"],
    text=True,
    capture_output=True,
    check=True,
)
```
:::

:::cell
`subprocess.run()` starts a child process and waits for it. `capture_output=True` stores the child's standard output and error streams on the result object.

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
:::
