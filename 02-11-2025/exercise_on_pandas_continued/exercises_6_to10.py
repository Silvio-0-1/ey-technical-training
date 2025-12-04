# 6. Create a new column ShippingDays = ShipDate - OrderDate.
df["ShippingDays"] = df["ShipDate"] - df["OrderDate"]


# 7. Create ProfitMargin = Profit / Sales.
df["ProfitMargin"] = df["Profit"] / df["Sales"]


# 8. Standardize CustomerName to title case.
df["CustomerName"] = df["CustomerName"].str.title()


# 9. Remove rows where Sales is zero or negative.
df = df[df["Sales"] > 0]


# 10. Convert Discount from decimal to percentage format.
df["Discount"] = df["Discount"].apply(lambda x : str(int(x*100)) + "%")
