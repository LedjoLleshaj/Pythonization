# Dates and Time - Study Notes

Python provides the `datetime` module to work with date and time objects.

## Core Objects
- **`date(year, month, day)`**: Represents a calendar date.
- **`time(hour, minute, second)`**: Represents a time of day.
- **`datetime(year, month, day, hour, ...)`**: Represents both date and time.
- **`timedelta`**: Represents a duration (the difference between two dates or times).

```python
from datetime import date, time, datetime, timedelta

# Current date/time
now = datetime.now()
today = date.today()

# Math with dates
tomorrow = today + timedelta(days=1)
```

## Formatting with `strftime`
The `strftime` (string format time) method converts a datetime object into a readable string.

Common Format Codes:
- `%Y`: 4-digit year (e.g., 2024)
- `%y`: 2-digit year (e.g., 24)
- `%m`: Month as a number (01-12)
- `%B`: Month name (e.g., January)
- `%d`: Day of the month (01-31)
- `%A`: Day of the week (e.g., Monday)
- `%H`: Hour (00-23)
- `%M`: Minute (00-59)
- `%S`: Second (00-59)

```python
now.strftime("%Y/%m/%d %H:%M:%S") # "2024/08/29 14:30:05"
```

## Key Properties
- `today.year`, `today.month`, `today.day`
- `now.hour`, `now.minute`, `now.second`
- `timedelta.days`, `timedelta.total_seconds()`
