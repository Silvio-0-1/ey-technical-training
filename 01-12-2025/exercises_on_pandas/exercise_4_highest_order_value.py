# 4. Find the top 5 highest-value orders by TotalPrice.

import pandas as pd

df = pd.read_csv("customer.csv")

sorted_df = df.sort_values("TotalPrice", ascending = False)
print("Sorted Data: \n", sorted_df.head(5))