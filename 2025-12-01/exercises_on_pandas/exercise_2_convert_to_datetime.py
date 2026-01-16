# 2. Convert the Date column to datetime and extract Year, Month, Day and add them as new columns.

import pandas as pd
df = pd.read_csv("customer.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day


print(df)
df.to_csv("customer_datetime.csv", index=False)
