+++
slug = "files-and-pathlib"
title = "Files and pathlib"
section = "Standard Library"
summary = "pathlib names files and directories, and open() reads and writes their text."
doc_path = "/library/pathlib.html"
see_also = [
  "context-managers",
  "exceptions",
  "csv-data",
  "json",
]
+++

A `Path` object names a place in the file system. It does not open anything by itself: it knows how to join names with `/`, take a path apart, and ask the file system questions such as whether the file exists.

Reading and writing are separate steps. `Path.read_text()` and `Path.write_text()` handle a whole small file in one call, while `open()` gives a file object that a `with` block closes for you and that you can loop over line by line.

This page works inside a temporary directory so it leaves nothing behind. Real programs use the same calls on paths they were given, and should always name the text encoding rather than rely on the platform default.

:::program
```python
import shutil
import tempfile
from pathlib import Path

root = Path(tempfile.mkdtemp())
notes = root / "notes.txt"
print(notes.name)
print(notes.suffix)
print(notes.exists())

notes.write_text("first line\nsecond line\n", encoding="utf-8")
print(notes.exists())
text = notes.read_text(encoding="utf-8")
print(text.splitlines())

with open(notes, "a", encoding="utf-8") as handle:
    handle.write("third line\n")

with open(notes, encoding="utf-8") as handle:
    for number, line in enumerate(handle, start=1):
        print(number, line.rstrip())

reports = root / "reports"
reports.mkdir()
(reports / "summary.csv").write_text("total\n3\n", encoding="utf-8")
print(sorted(path.name for path in root.iterdir()))
print([path.relative_to(root).as_posix() for path in root.rglob("*.csv")])
print(reports.is_dir())

missing = root / "missing.txt"
try:
    missing.read_text(encoding="utf-8")
except FileNotFoundError as error:
    print(type(error).__name__)

shutil.rmtree(root)
print(root.exists())
```
:::

:::cell
The `/` operator joins a directory path and a name into a new `Path`. Building a path touches nothing on disk, so `notes` can be taken apart with `.name` and `.suffix` before any file exists.

```python
import shutil
import tempfile
from pathlib import Path

root = Path(tempfile.mkdtemp())
notes = root / "notes.txt"
print(notes.name)
print(notes.suffix)
print(notes.exists())
```

```output
notes.txt
.txt
False
```
:::

:::cell
`write_text()` creates the file, writes the string, and closes it. `read_text()` returns the whole file as one string, which suits small files. Passing `encoding="utf-8"` makes the bytes on disk the same on every machine.

```python
notes.write_text("first line\nsecond line\n", encoding="utf-8")
print(notes.exists())
text = notes.read_text(encoding="utf-8")
print(text.splitlines())
```

```output
True
['first line', 'second line']
```
:::

:::cell
`open()` returns a file object, and the `with` block closes it even if the body raises. Mode `"a"` appends instead of replacing. A file opened for reading is an iterator of lines, each still ending in its newline, so large files can be processed without loading them whole.

```python
with open(notes, "a", encoding="utf-8") as handle:
    handle.write("third line\n")

with open(notes, encoding="utf-8") as handle:
    for number, line in enumerate(handle, start=1):
        print(number, line.rstrip())
```

```output
1 first line
2 second line
3 third line
```
:::

:::cell
Directories are paths too. `mkdir()` creates one, `iterdir()` lists the entries directly inside a directory, and `rglob()` searches every level below it for names matching a pattern. Listing order is up to the file system, so sort when the order matters.

```python
reports = root / "reports"
reports.mkdir()
(reports / "summary.csv").write_text("total\n3\n", encoding="utf-8")
print(sorted(path.name for path in root.iterdir()))
print([path.relative_to(root).as_posix() for path in root.rglob("*.csv")])
print(reports.is_dir())
```

```output
['notes.txt', 'reports']
['reports/summary.csv']
True
```
:::

:::cell
Opening a file that is not there raises `FileNotFoundError`. Catching it is usually better than checking `exists()` first, because the file can appear or vanish between the check and the read. `shutil.rmtree()` removes the temporary directory and everything in it.

```python
missing = root / "missing.txt"
try:
    missing.read_text(encoding="utf-8")
except FileNotFoundError as error:
    print(type(error).__name__)

shutil.rmtree(root)
print(root.exists())
```

```output
FileNotFoundError
False
```
:::

:::note
- A `Path` is a name for a place; building one with `/` does not create or open a file.
- Pass `encoding="utf-8"` to `open()`, `read_text()`, and `write_text()` so text means the same bytes everywhere.
- Use `with open(...)` so the file is closed when the block ends, and loop over the file object to read line by line.
- `iterdir()` lists one directory and `rglob()` searches below it; sort the results when order matters.
- Catch `FileNotFoundError` at the read instead of trusting an earlier `exists()` check.
:::
