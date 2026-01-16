# 14. Write the filtered Electronics-only dataset into a new CSV file.
import pandas as pd
df = pd.read_csv("customer.csv")

filtered = df[(df["Category"] == "Electronics")]
print("Electronics-only dataset: \n", filtered)