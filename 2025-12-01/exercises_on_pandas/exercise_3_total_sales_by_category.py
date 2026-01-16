# 3. Calculate total sales for Store, City, Category.

import pandas as pd
df = pd.read_csv("customer.csv")

print("\nTotal sales for Stores: \n")
print(df.groupby("Store")["TotalPrice"].sum())

print("\nTotal sales for City: \n")
print(df.groupby("City")["TotalPrice"].sum())

print("\nTotal sales for Category: \n")
print(df.groupby("Category")["TotalPrice"].sum())


