# 9. Identify the store with the highest total sales.
import pandas as pd
df = pd.read_csv("customer.csv")

store_sales = df.groupby("Store")["TotalPrice"].sum()

highest_store = store_sales.idxmax()
highest_sales = store_sales.max()

print("Store-wise total sales:\n", store_sales)
print("\nStore with the highest total sales:", highest_store)
print("Total Sales:", highest_sales)

# 10. Filter rows where Product name contains the letter “a” or “A”.
filtered = df[df["Product"].str.contains("a",case=False)]
print(filtered)


# 11. Sort the dataset by Date and then by TotalPrice.
sorted_df = df.sort_values(by=["Date", "TotalPrice"], ascending=[True, True])
print("Sorted Data: \n", sorted_df)


# 12. Find the average revenue per order for each CustomerType.
average_revenue = df.groupby("CustomerType")["TotalPrice"].mean()
print(average_revenue)