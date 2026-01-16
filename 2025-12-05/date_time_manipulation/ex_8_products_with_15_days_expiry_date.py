# 8. Given some expiry dates, find which products expire within the next 15 days.
from datetime import datetime

expiry_date = {
    "Product 1" : "2025-12-08",
    "Product 2" : "2025-12-12",
    "Product 3" : "2025-12-21",
    "Product 4" : "2026-01-15",
    "Product 5" : "2026-06-30"
}
today = datetime.today().date()
for keys, values in expiry_date.items():
    date = datetime.strptime(values, "%Y-%m-%d").date()
    if (date - today).days <= 15:
        print(keys)