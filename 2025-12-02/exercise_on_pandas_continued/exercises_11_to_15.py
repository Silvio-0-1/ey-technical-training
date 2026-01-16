# 11. Filter all orders from the West region.
west_region = df[df["Region"] == "West"]
west_region


# 12. Filter Technology category with Sales > 400.
filtered_tech = df[(df["Category"] == "Technology") & (df["Sales"] > 400)]
filtered_tech


# 13. Find all products returned by customers.
filtered_products = df[df["Returned"] == "Yes"]
filtered_products


# 14. Show Furniture orders shipped after 2024-01-20.
filtered_furniture = df[(df["Category"] == "Furniture") & (df["ShipDate"] > "2024-01-20")]
filtered_furniture


# 15. Filter orders where Profit < 20.
filtered_profits = df[(df["Profit"] < 20)]
filtered_profits
