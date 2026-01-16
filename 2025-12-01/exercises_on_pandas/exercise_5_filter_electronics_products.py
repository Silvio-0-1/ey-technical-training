# 5. Filter the dataset to show only Electronics products with Quantity > 1.
import pandas as pd
df = pd.read_csv("customer.csv")

filtered = df[(df["Category"] == "Electronics") & (df["Quantity"] > 1)]
print("Electronics products with Quantity > 1: \n", filtered)