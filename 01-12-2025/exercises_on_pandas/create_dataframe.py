data = [
    {"OrderID": 1001, "Date": "2024-01-05", "Store": "Store A", "City": "Mumbai", "Product": "Laptop", "Category": "Electronics", "Quantity": 1, "UnitPrice": 55000, "TotalPrice": 55000, "PaymentMethod": "Credit Card", "CustomerType": "New"},
    {"OrderID": 1002, "Date": "2024-01-05", "Store": "Store B", "City": "Delhi", "Product": "Shampoo", "Category": "Personal Care", "Quantity": 3, "UnitPrice": 120, "TotalPrice": 360, "PaymentMethod": "Cash", "CustomerType": "Returning"},
    {"OrderID": 1003, "Date": "2024-01-06", "Store": "Store C", "City": "Bangalore", "Product": "Jeans", "Category": "Apparel", "Quantity": 2, "UnitPrice": 1500, "TotalPrice": 3000, "PaymentMethod": "Credit Card", "CustomerType": "New"},
    {"OrderID": 1004, "Date": "2024-01-06", "Store": "Store A", "City": "Mumbai", "Product": "Smartphone", "Category": "Electronics", "Quantity": 1, "UnitPrice": 25000, "TotalPrice": 25000, "PaymentMethod": "UPI", "CustomerType": "Returning"},
    {"OrderID": 1005, "Date": "2024-01-07", "Store": "Store B", "City": "Delhi", "Product": "Bread", "Category": "Grocery", "Quantity": 5, "UnitPrice": 40, "TotalPrice": 200, "PaymentMethod": "Cash", "CustomerType": "New"},
    {"OrderID": 1006, "Date": "2024-01-07", "Store": "Store C", "City": "Bangalore", "Product": "T-Shirt", "Category": "Apparel", "Quantity": 4, "UnitPrice": 800, "TotalPrice": 3200, "PaymentMethod": "Credit Card", "CustomerType": "Returning"},
    {"OrderID": 1007, "Date": "2024-01-08", "Store": "Store A", "City": "Mumbai", "Product": "Milk", "Category": "Grocery", "Quantity": 10, "UnitPrice": 50, "TotalPrice": 500, "PaymentMethod": "UPI", "CustomerType": "New"},
    {"OrderID": 1008, "Date": "2024-01-08", "Store": "Store B", "City": "Delhi", "Product": "Perfume", "Category": "Personal Care", "Quantity": 1, "UnitPrice": 2500, "TotalPrice": 2500, "PaymentMethod": "Credit Card", "CustomerType": "Returning"},
    {"OrderID": 1009, "Date": "2024-01-09", "Store": "Store C", "City": "Bangalore", "Product": "Headphones", "Category": "Electronics", "Quantity": 2, "UnitPrice": 1500, "TotalPrice": 3000, "PaymentMethod": "Cash", "CustomerType": "New"},
    {"OrderID": 1010, "Date": "2024-01-09", "Store": "Store A", "City": "Mumbai", "Product": "Rice", "Category": "Grocery", "Quantity": 3, "UnitPrice": 90, "TotalPrice": 270, "PaymentMethod": "Credit Card", "CustomerType": "Returning"},
    {"OrderID": 1011, "Date": "2024-01-10", "Store": "Store B", "City": "Delhi", "Product": "Shoes", "Category": "Apparel", "Quantity": 1, "UnitPrice": 3000, "TotalPrice": 3000, "PaymentMethod": "UPI", "CustomerType": "New"},
    {"OrderID": 1012, "Date": "2024-01-10", "Store": "Store C", "City": "Bangalore", "Product": "Milk", "Category": "Grocery", "Quantity": 12, "UnitPrice": 48, "TotalPrice": 576, "PaymentMethod": "Cash", "CustomerType": "Returning"},
    {"OrderID": 1013, "Date": "2024-01-11", "Store": "Store A", "City": "Mumbai", "Product": "Charger", "Category": "Electronics", "Quantity": 2, "UnitPrice": 600, "TotalPrice": 1200, "PaymentMethod": "Credit Card", "CustomerType": "New"},
    {"OrderID": 1014, "Date": "2024-01-11", "Store": "Store B", "City": "Delhi", "Product": "Notebook", "Category": "Stationery", "Quantity": 10, "UnitPrice": 35, "TotalPrice": 350, "PaymentMethod": "Cash", "CustomerType": "Returning"},
    {"OrderID": 1015, "Date": "2024-01-12", "Store": "Store C", "City": "Bangalore", "Product": "Smartwatch", "Category": "Electronics", "Quantity": 1, "UnitPrice": 8000, "TotalPrice": 8000, "PaymentMethod": "UPI", "CustomerType": "New"},
    {"OrderID": 1016, "Date": "2024-01-12", "Store": "Store A", "City": "Mumbai", "Product": "Biscuits", "Category": "Grocery", "Quantity": 6, "UnitPrice": 25, "TotalPrice": 150, "PaymentMethod": "Credit Card", "CustomerType": "Returning"},
    {"OrderID": 1017, "Date": "2024-01-12", "Store": "Store B", "City": "Delhi", "Product": "Jacket", "Category": "Apparel", "Quantity": 1, "UnitPrice": 4500, "TotalPrice": 4500, "PaymentMethod": "UPI", "CustomerType": "New"},
    {"OrderID": 1018, "Date": "2024-01-13", "Store": "Store C", "City": "Bangalore", "Product": "Soap", "Category": "Personal Care", "Quantity": 4, "UnitPrice": 45, "TotalPrice": 180, "PaymentMethod": "Cash", "CustomerType": "Returning"},
    {"OrderID": 1019, "Date": "2024-01-13", "Store": "Store A", "City": "Mumbai", "Product": "Keyboard", "Category": "Electronics", "Quantity": 1, "UnitPrice": 1200, "TotalPrice": 1200, "PaymentMethod": "UPI", "CustomerType": "New"},
    {"OrderID": 1020, "Date": "2024-01-13", "Store": "Store B", "City": "Delhi", "Product": "Shirt", "Category": "Apparel", "Quantity": 2, "UnitPrice": 1100, "TotalPrice": 2200, "PaymentMethod": "Credit Card", "CustomerType": "Returning"}
]

import pandas as pd
df = pd.DataFrame(data)

df.to_csv("customer.csv", index = False)
print("CSV file created.")





# print("Head: \n", df.head(2))
# print("Tail: \n", df.tail(2))
#
# print("Shape: ", df.shape)
# print("Columns: \n", df.columns)
# print("Describe: \n", df.describe())
#
# print(df["Name"])
# print(df[["Name", "Marks"]])
#
# # Filters
# high_scores = df[df["Marks"] > 70]
# print("Marks more than 70: \n", high_scores)
#
# filtered = df[(df["Marks"] > 70) & (df["Age"] > 22)]
# print("Marks > 70 and Age > 22: \n", filtered)