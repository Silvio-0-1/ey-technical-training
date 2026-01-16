# MODULE 5: Pandas (CSV, JSON, Missing Data, Grouping, Merging) (10 Exercises)

import pandas as pd

# 30. Load retail dataset and find: total orders, total revenue, and top 5 products.
df = pd.read_csv("retail_dataset.csv")
total_orders = df["OrderID"].count()
total_revenue = df["TotalPrice"].sum()

print("Total Order: ", total_orders)
print("Total Revenue: ", total_revenue)
print("Top 5 products: ", df.head(5))


# 31. Identify missing values and fill numeric columns with median, categorical with mode.
print(df.isnull().sum())

for col in df.select_dtypes(include=["number"]).columns:
    median_value = df[col].median()
    df[col].fillna(median_value, inplace=True)

for col in df.select_dtypes(include=["object"]).columns:
    mode_value = df[col].mode()[0]  # mode() returns a Series
    df[col].fillna(mode_value, inplace=True)

print("\nCleaned DataFrame:")
print(df)

# 32. Group by product category and calculate: total sales, count of orders, average price.
print(df.groupby("Category")["TotalPrice"].sum())
print(df.groupby("Category")["OrderID"].count())
print(df.groupby("Category")["UnitPrice"].mean())


# 33. Create a new column "DiscountedPrice" = price minus 10 percent.
df["DiscountedPrice"] = df["TotalPrice"] * 0.99
print(df)


# 34. Merge a customers.csv and orders.csv on customer-id and generate a combined report.

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

combined = pd.merge(orders, customers, on="customer_id", how="inner")

print("Combined Report:")
print(combined)

combined.to_csv("combined_report.csv", index=False)

# 35. Load a JSON file containing customers and normalize nested fields.

# 36. Filter transactions for customers who spent more than 5000 total.
filtered_transactions = df[df["DiscountedPrice"] > 50000]
print(filtered_transactions)


# 37. Generate pivot table: category vs month showing total sales.


# 38. Remove outliers using IOR and list the cleaned dataset.


# 39. Combine multiple CSVs into one final DataFrame and remove duplicates.