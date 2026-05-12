+++
slug = "csv-data"
title = "CSV Data"
section = "Standard Library"
summary = "csv reads and writes row-shaped text data."
doc_path = "/library/csv.html"
see_also = [
  "strings",
  "dicts",
  "json",
]
+++

csv reads and writes row-shaped text data. It exists to make a common boundary explicit instead of leaving the behavior implicit in a larger program.

Use it when the problem shape matches the example, and prefer simpler neighboring tools when the extra machinery would hide the intent. The notes call out the boundary so the feature stays practical rather than decorative.

The example is small, deterministic, and focused on the semantic point. The complete source is editable below, while the walkthrough pairs the source with its output.

:::program
```python
import csv
import io

text = "name,score\nAda,98\nGrace,95\n"
reader = csv.DictReader(io.StringIO(text))
rows = list(reader)

print(rows[0]["name"])
print(sum(int(row["score"]) for row in rows))

output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["name", "passed"])
writer.writeheader()
writer.writerow({"name": "Ada", "passed": True})
print(output.getvalue().splitlines()[1])
```
:::

:::cell
Use `DictReader` when column names should become dictionary keys.

```python
import csv
import io

text = "name,score\nAda,98\nGrace,95\n"
reader = csv.DictReader(io.StringIO(text))
rows = list(reader)

print(rows[0]["name"])
print(sum(int(row["score"]) for row in rows))

output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["name", "passed"])
writer.writeheader()
writer.writerow({"name": "Ada", "passed": True})
print(output.getvalue().splitlines()[1])
```

```output
Ada
193
Ada,True
```
:::

:::note
- Use `DictReader` when column names should become dictionary keys.
- CSV fields arrive as text, so convert numbers explicitly.
- `DictWriter` writes dictionaries back to row-shaped text.
:::
