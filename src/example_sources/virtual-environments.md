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

In standard Python, `python -m venv .venv` is the everyday command. Dynamic Workers do not provide a project-local environment workflow, so this page teaches the proper standard-Python boundary and keeps the runnable evidence limited to what can be observed deterministically.

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
The standard project setup command is `python -m venv .venv`. It creates a directory with its own interpreter entry points and package install location. After activation, `python -m pip install ...` installs into that environment rather than into another project. (This workflow is for standard Python projects — Dynamic Workers are built from declared dependencies instead of an activated shell environment.)

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
- Dynamic Workers use a deployment dependency model, not an activated shell environment.
:::
