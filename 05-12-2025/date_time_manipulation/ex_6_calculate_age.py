# 1\6. Calculate a user's precise age (years, months, days) based on DOB.

from datetime import datetime, timedelta, date

def calculate_age(dob, today = date.today()):
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        days +=30

    if months < 0:
        years -= 1
        months +=12

    return f"{years} years, {months} months, {days} days"

dob = datetime.strptime(input("Enter date of birth: "), "%Y-%m-%d").date()
print("Precise age: ", calculate_age(dob))