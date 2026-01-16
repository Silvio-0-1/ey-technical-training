# 9. Convert a list of date strings into datetime objects and sort them.
from datetime import datetime
date_strings = [
    "2025-12-06",
    "2025-12-12",
    "2025-12-21",
    "2026-01-15",
    "2026-06-30",
    "2024-02-29"
]

dates = [datetime.strptime(date,"%Y-%m-%d").date() for date in date_strings]
sorted_dates = sorted(dates)
sorted_strings = [d.strftime("%Y-%m-%d") for d in sorted_dates]
print(sorted_strings)
