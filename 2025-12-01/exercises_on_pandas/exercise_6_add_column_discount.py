# 6. Add a new column Discount:
# 10 percent discount for Returning customers
# 5 percent discount for New customers
# Compute final price after discount.

import pandas as pd
df = pd.read_csv("customer.csv")

df["Discount"] = df["CustomerType"].apply(lambda x: 10 if x == "Returning" else 5)
df["FinalPrice"] = df["TotalPrice"] * df["Discount"]/100

print(df)