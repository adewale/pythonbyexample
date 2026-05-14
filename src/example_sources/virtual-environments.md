+++
slug = "virtual-environments"
title = "Virtual Environments"
section = "Modules"
summary = "Virtual environments isolate a project's Python packages."
doc_path = "/library/venv.html"
see_also = [
  "packages",
  "modules",
  "import-aliases",
]
expected_output = ".venv\nTrue\n"
+++

Virtual environments isolate a project's installed packages from the global Python installation and from other projects. The usual workflow is a command-line one: create `.venv`, activate it, then install project dependencies there.

In standard Python, `python -m venv .venv` is the everyday command. This site's live example runner is built from declared dependencies rather than an activated shell environment, so the runnable part keeps to deterministic evidence while the page still teaches the standard-Python workflow.

A virtual environment changes installation and import paths. It does not change the Python language, package layout rules, or module names.

:::program
```python
import pathlib
import tempfile
import venv

with tempfile.TemporaryDirectory() as directory:
    env_path = pathlib.Path(directory) / ".venv"
    builder = venv.EnvBuilder(with_pip=False)
    builder.create(env_path)

    config = (env_path / "pyvenv.cfg").read_text()
    print(env_path.name)
    print("home" in config)
```
:::

:::unsupported
The standard project setup command is `python -m venv .venv`. It creates a directory with its own interpreter entry points and package install location. After activation, `python -m pip install ...` installs into that environment rather than into another project. (This workflow is for standard Python projects. The Python By Example runner is deployed from declared dependencies instead of an activated shell environment.)

```python
import subprocess
import sys

subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
subprocess.run([".venv/bin/python", "-m", "pip", "install", "requests"], check=True)
```
:::

:::cell
`venv.EnvBuilder` exposes the same environment-creation mechanism as `python -m venv`. A temporary directory keeps the example from leaving project files behind.

```python
import pathlib
import tempfile
import venv

with tempfile.TemporaryDirectory() as directory:
    env_path = pathlib.Path(directory) / ".venv"
    builder = venv.EnvBuilder(with_pip=False)
    builder.create(env_path)

    config = (env_path / "pyvenv.cfg").read_text()
    print(env_path.name)
    print("home" in config)
```

```output
.venv
True
```
:::

:::note
- Use `python -m venv .venv` for everyday standard-Python project setup.
- A venv isolates installed packages; it does not change how imports are written.
- This site's runner uses a deployment dependency model, not an activated shell environment.
- That runner constraint is separate from the standard Python `venv` workflow you would use in local projects.
:::
