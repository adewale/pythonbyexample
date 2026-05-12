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

CSV is row-shaped text: each line is a record, and each comma-separated field arrives as a string. The `csv` module understands quoting, delimiters, and newlines, so it is safer than splitting lines by comma yourself.

Use `DictReader` when a header row names the columns. Convert fields explicitly after reading, and use `DictWriter` when the program needs to produce the same row shape again.

CSV is a good fit for flat tabular data. Use JSON or another structured format when values are nested or when types need to survive the text boundary.

:::program
```python
import csv
import io

text = "name,score\nAda,98\nGrace,95\n"
rows = list(csv.DictReader(io.StringIO(text)))
print(rows[0])
print(sum(int(row["score"]) for row in rows))

output = io.StringIO(newline="")
writer = csv.DictWriter(output, fieldnames=["name", "passed"])
writer.writeheader()
writer.writerow({"name": "Ada", "passed": True})
print(output.getvalue().splitlines()[1])
```
:::

:::cell
`DictReader` uses the header row as dictionary keys. The values are still strings because CSV is text.

```python
import csv
import io

text = "name,score\nAda,98\nGrace,95\n"
rows = list(csv.DictReader(io.StringIO(text)))

print(rows[0])
print(type(rows[0]["score"]).__name__)
```

```output
{'name': 'Ada', 'score': '98'}
str
```
:::

:::cell
Convert numeric fields at the boundary where the program leaves CSV text and starts doing arithmetic.

```python
print(sum(int(row["score"]) for row in rows))
```

```output
193
```
:::

:::cell
`DictWriter` turns dictionaries back into row-shaped text with the same column order.

```python
output = io.StringIO(newline="")
writer = csv.DictWriter(output, fieldnames=["name", "passed"])
writer.writeheader()
writer.writerow({"name": "Ada", "passed": True})

print(output.getvalue().splitlines()[1])
```

```output
Ada,True
```
:::

:::note
- Let `csv` handle quoting and delimiters instead of calling `split(",")`.
- CSV fields are text until your code converts them.
- Reach for JSON when records need nested lists, dictionaries, booleans, or numbers that preserve their type.
:::
