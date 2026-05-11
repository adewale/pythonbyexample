+++
slug = "virtual-environments"
title = "Virtual Environments"
section = "Modules"
summary = "Virtual environments isolate a project's Python packages."
doc_path = "/library/venv.html"
expected_output = ".venv\nTrue\n"
+++

Virtual environments isolate a project's Python packages. They exist so one project can install dependencies without changing another project's environment.

The usual command-line workflow is `python -m venv .venv`, but Python also exposes the same feature through the `venv` module. This example creates a temporary environment so the example cleans up after itself.

A virtual environment changes where Python looks for installed packages. It does not change the language, and it is separate from package layout, imports, and module names.

:::program
```python
import pathlib
import tempfile
import venv

with tempfile.TemporaryDirectory() as directory:
    env_path = pathlib.Path(directory) / ".venv"
    builder = venv.EnvBuilder(with_pip=False)
    builder.create(env_path)

    print(env_path.name)
    print((env_path / "pyvenv.cfg").exists())
```
:::

:::unsupported
`venv.EnvBuilder` configures the description of a new environment, then `create(".venv")` materialises it on disk as a directory containing its own interpreter and `site-packages`. `with_pip=False` skips bootstrapping pip — useful when the venv is for an isolated tool that doesn't need to install third-party packages. (This fragment runs in standard Python only — Dynamic Workers don't provide the `venv` module or a project environment workflow.)

```python
builder = venv.EnvBuilder(with_pip=False)
builder.create(".venv")
```
:::

:::cell
`venv.EnvBuilder` creates the same kind of isolated environment as `python -m venv`. A temporary directory keeps the example from leaving project files behind.

```python
import pathlib
import tempfile
import venv

with tempfile.TemporaryDirectory() as directory:
    env_path = pathlib.Path(directory) / ".venv"
    builder = venv.EnvBuilder(with_pip=False)
    builder.create(env_path)

    print(env_path.name)
    print((env_path / "pyvenv.cfg").exists())
```

```output
.venv
True
```
:::

:::note
- A virtual environment gives a project its own install location.
- Inside a venv, `sys.prefix` usually differs from `sys.base_prefix`.
- Use `python -m venv .venv` at the command line for everyday project setup.
:::
