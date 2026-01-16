# 7. Find how many orders were paid using Cash, Credit Card and UPI

import pandas as pd
df = pd.read_csv("customer.csv")

print("\nTotal number of orders with Cash:")
print(df.groupby("PaymentMethod")["OrderID"].count()["Cash"])

print("\nTotal number of orders with Credit Card:")
print(df.groupby("PaymentMethod")["OrderID"].count()["Credit Card"])

print("\nTotal number of orders with UPI:")
print(df.groupby("PaymentMethod")["OrderID"].count()["UPI"])