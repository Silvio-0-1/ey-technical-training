# 1. Display first 5 rows, last 5 rows, column names, shape

import pandas as pd

df = pd.read_csv("customer.csv")

print("\nFirst 5 rows: \n", df.head(5))
print("\nLast 5 rows: \n", df.tail(5))
print("\nShape: ", df.shape)
print("\nColumns: \n", df.columns)
print("\nDescribe: \n", df.describe())