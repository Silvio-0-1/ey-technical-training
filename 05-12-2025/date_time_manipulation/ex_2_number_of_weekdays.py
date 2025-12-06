# 2. Given two dates (start_date, end_date), write a function that returns the number of weekdays.
from datetime import date, timedelta

def count_weekdays(start_date, end_date):
    counter = 0
    while start_date <= end_date:
        if start_date.weekday() < 5:
            counter += 1
        start_date += timedelta(days=1)

    return counter

print(count_weekdays(date.today(), date.today() + timedelta(days=30)))



