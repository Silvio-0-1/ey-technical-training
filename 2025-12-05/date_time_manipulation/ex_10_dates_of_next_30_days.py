# 10. Generate a list of dates for the next 30 days starting from today.
from datetime import datetime, timedelta

today = datetime.today().date()
dates = []

for i in range(30):
    dates.append((today + timedelta(days=i)).strftime("%Y-%m-%d"))

print(dates)