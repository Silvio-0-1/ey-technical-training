# 13. Create a pivot table:
# Rows: Category
# Columns: PaymentMethod
# Values: TotalPrice (sum)
import pandas as pd
df = pd.read_csv("customer.csv")

pivot = pd.pivot_table(
    df,
    values="TotalPrice",       # Values to aggregate
    index="Category",          # Rows
    columns="PaymentMethod",   # Columns
    aggfunc="sum",             # Aggregation function
    fill_value=0               # Replace NaN with 0
)

print(pivot)
