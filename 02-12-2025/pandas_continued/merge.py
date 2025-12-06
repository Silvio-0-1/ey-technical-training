import pandas as pd

# Step 1: Load CSV files
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

# Step 2: Merge on customer_id
combined = pd.merge(orders, customers, on="customer_id", how="inner")

# Step 3: Generate combined report
print("Combined Report:")
print(combined)

# Step 4: Optionally save to a new CSV
combined.to_csv("combined_report.csv", index=False)
