# 4. Write a function that checks if a given date is in the future, past, or today.
from datetime import date, timedelta

dates = [date.today() - timedelta(days=10),
         date.today() + timedelta(days=15),
         date.today()
]

for i in dates:
    if i > date.today():
        print(f"{i} is in future")
    elif i < date.today():
        print(f"{i} is in past")
    else:
        print(f"{i} is today")