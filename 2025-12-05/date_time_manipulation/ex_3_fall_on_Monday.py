# 3. You are given a list of attendance timestamps. Count how many fall on a Monday.

from datetime import datetime

attendance = [
    "2025-12-01 09:00:40",  # Monday
    "2025-12-02 09:01:45",  # Tuesday
    "2025-12-08 09:05:30",  # Monday
    "2025-12-06 09:10:00",  # Saturday
]

monday_count = 0
for i in attendance:
    dt = datetime.strptime(i, "%Y-%m-%d %H:%M:%S") # parsing
    if dt.weekday() == 0:
        monday_count += 1

print(monday_count)