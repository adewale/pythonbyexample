#!/usr/bin/env python3
"""Pin uv.lock's runtime packages to the versions pylock.toml deploys.

Production installs from `pylock.toml`, which pywrangler resolves against
Pyodide wheels. The test suite runs against `uv.lock`. This script moves
every package the two files share to the pylock.toml version so tests
exercise exactly what ships; `tests/test_dependency_locks.py` fails
whenever they drift apart.
"""
from __future__ import annotations

import subprocess
import sys
import tomllib

from _common import ROOT


def main() -> int:
    pylock = tomllib.loads((ROOT / "pylock.toml").read_text())
    pins = [f"{package['name']}=={package['version']}" for package in pylock["packages"]]
    command = ["uv", "lock"]
    for pin in pins:
        command += ["--upgrade-package", pin]
    print("Pinning uv.lock to pylock.toml:", ", ".join(pins))
    return subprocess.run(command, cwd=ROOT, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
