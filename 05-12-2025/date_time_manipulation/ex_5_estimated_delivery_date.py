# 15. Given a order_date and delivery_timeline, calculate estimated_delivery_date.

from datetime import datetime, timedelta

order_date = datetime.strptime("2025-12-06", "%Y-%m-%d").date() # extracts only date
delivery_timeline = 7

delivery_date = order_date + timedelta(days=delivery_timeline)
print(delivery_date)
