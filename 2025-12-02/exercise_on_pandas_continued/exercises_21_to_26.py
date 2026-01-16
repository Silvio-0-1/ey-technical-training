# 21. Total Sales per Region.
df.groupby("Region")["Sales"].sum()


# 22. Average Profit per Category.
df.groupby("Category")["Profit"].mean()


# 23. Count of orders per Customer.
# 24. Sum of Sales per Segment.
df.groupby("Segment")["Sales"].sum()


# 25. Total Quantity sold per SubCategory.
df.groupby("SubCategory")["Quantity"].sum()


# 26. Mean ShippingDays grouped by Category.
df.groupby("Category")["ShippingDays"].mean()
