+++
slug = "datetime"
title = "Dates and Times"
section = "Standard Library"
summary = "datetime represents dates, times, durations, formatting, and parsing."
doc_path = "/library/datetime.html"
+++

The `datetime` module covers several related ideas: `date` for calendar days, `time` for clock times, `datetime` for both together, and `timedelta` for durations.

Timezone-aware datetimes avoid ambiguity in real systems. `timezone.utc` is a clear default for examples because output stays stable and portable.

Use ISO formatting for interchange, `strftime()` for display, and parsing helpers such as `fromisoformat()` to turn text back into datetime objects.

:::program
```python
from datetime import date, datetime, time, timedelta, timezone

release_day = date(2026, 5, 4)
meeting_time = time(12, 30)
created_at = datetime.combine(release_day, meeting_time, tzinfo=timezone.utc)

print(release_day.isoformat())
print(meeting_time.isoformat())
print(created_at.isoformat())

expires_at = created_at + timedelta(days=7, hours=2)
print(expires_at.isoformat())

print(created_at.strftime("%Y-%m-%d %H:%M %Z"))
iso_text = "2026-05-04T12:30:00+00:00"
parsed = datetime.fromisoformat(iso_text)
print(parsed == created_at)
```
:::

:::cell
The `datetime` module separates calendar dates, clock times, combined datetimes, and durations. Import the types you need explicitly.

Use `date` for a calendar day and `time` for a time of day. Combine them into a timezone-aware `datetime` when you mean an instant.

`isoformat()` produces stable machine-readable text. It is a good default for examples, APIs, and logs.

```python
from datetime import date, datetime, time, timedelta, timezone

release_day = date(2026, 5, 4)
meeting_time = time(12, 30)
created_at = datetime.combine(release_day, meeting_time, tzinfo=timezone.utc)

print(release_day.isoformat())
print(meeting_time.isoformat())
print(created_at.isoformat())
```

```output
2026-05-04
12:30:00
2026-05-04T12:30:00+00:00
```
:::

:::cell
Use `timedelta` for durations. Adding one to a `datetime` produces another `datetime` without manually changing calendar fields.

```python
expires_at = created_at + timedelta(days=7, hours=2)
print(expires_at.isoformat())
```

```output
2026-05-11T14:30:00+00:00
```
:::

:::cell
Use `strftime()` for human-facing formatting and `fromisoformat()` when reading ISO 8601 text back into a `datetime`.

```python
print(created_at.strftime("%Y-%m-%d %H:%M %Z"))
iso_text = "2026-05-04T12:30:00+00:00"
parsed = datetime.fromisoformat(iso_text)
print(parsed == created_at)
```

```output
2026-05-04 12:30 UTC
True
```
:::

:::note
- Use timezone-aware datetimes for instants that cross system or user boundaries.
- Use `date` for calendar days, `time` for clock times, `datetime` for both, and `timedelta` for durations.
- Prefer ISO 8601 strings for interchange; use `strftime` for human-facing display.
:::
