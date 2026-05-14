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

:::unsupported
`subprocess.run` spawns a child Python interpreter, captures its stdout and stderr (`capture_output=True`), decodes them as text (`text=True`), and raises `CalledProcessError` if the child exits non-zero (`check=True`). The returned `result` holds the captured streams and exit code as portable evidence the child ran. (This fragment runs in standard Python only — the Python By Example runner does not provide child processes.)

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
- If you run this in local/server Python, the child process is real; on this site, the runnable evidence preserves the API shape without spawning a process.
:::
