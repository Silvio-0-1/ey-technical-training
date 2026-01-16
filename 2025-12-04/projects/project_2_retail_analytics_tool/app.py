# Project 2: Retail Analytics Tool (Python + MySQL + Pandas)
# Create a module that:
# 1. Reads orders from MySQL
# 2. Loads products from CSV
# 3. Merge and generate a revenue dashboard
# 4. Computes top 5 customers
# 5. Saves final report to Excel

import pymysql
import pandas as pd

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='P@ssword',
    database='retail_db'
)
print("Connecting to database...")
if conn:
    print("Connection is successful")

cursor = conn.cursor()

# 1. Read Orders
def read_orders():
    query = """
        SELECT order_id, customer_name, product_id, quantity, price FROM orders
    """
    orders = pd.read_sql(query, conn)
    return orders


# 2. Loads Products from CSV
def load_products():
    products = pd.read_csv("products.csv")
    return products

# 3. Merge and generate a revenue dashboard
def merge_and_generate(orders, products):
    # merge
    merged_df = pd.merge(orders, products, on="product_id", how="left")

    # generate revenue dashboard
    merged_df["revenue"] = merged_df["quantity"] * merged_df["price"]
    revenue_by_category = merged_df.groupby("category")["revenue"].sum()
    print("\nMerged data: \n", merged_df)
    print("\nRevenue by category: \n", revenue_by_category)
    return merged_df

# 4. Computes top 5 customers
def top_customers(merged_df):
    merged_df = merged_df.sort_values("revenue", ascending=False)
    print(merged_df[["customer_name", "revenue"]].head(5))


# 6. Export to CSV
def export_to_csv(merged_df):
    merged_df.to_csv("final_report.csv", index=False)
    print("Employee details exported successfully!")

print("\n\nWelcome to Retail Analytics Tool!")
print("Reading Orders...")
print(orders := read_orders())
print("\nOrders displayed successfully!")

print("Loading Products...")
print(products := load_products())
print("\nProducts loaded successfully!")

print("Merging and generating revenue dashboard...")
merged_df = merge_and_generate(orders, products)

print("Computing top 5 customers...")
top_customers(merged_df)

print("Exporting to CSV")
export_to_csv(merged_df)

cursor.close()
conn.close()
