# 1. Given a customer's subscription start date and duration (in days), compute expiry date.
from datetime import date, timedelta

start_date = date(2021, 5, 1)
duration = 90

expiry_date = start_date + timedelta(days = duration)
print("Expiry date: ", expiry_date)
