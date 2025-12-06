# 17. Write a function that returns True if a given year is a leap year.

from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_leap_year(int(input("Enter a year: "))))