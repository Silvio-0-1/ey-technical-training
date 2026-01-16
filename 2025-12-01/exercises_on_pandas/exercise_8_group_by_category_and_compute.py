# 8. Group by Category and compute: Total quantity sold, Total revenue

import pandas as pd
df = pd.read_csv("customer.csv")

print("\nTotal quantity category wise: \n")
print(df.groupby("Category")["Quantity"].sum())

print("\nTotal revenue category wise: \n")
print(df.groupby("Category")["TotalPrice"].sum())