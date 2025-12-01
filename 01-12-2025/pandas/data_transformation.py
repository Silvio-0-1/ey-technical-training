import pandas as pd
df = pd.read_csv("students.csv")

# Data Transformations
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print(df)

sorted_df = df.sort_values("Marks", ascending = False)
print("Sorted Data: \n", sorted_df)


df2 = df.copy()
df2.loc[2, "City"] = None # create missing value
print(df2.isnull().sum()) # counts null in each column


df2_filled = df2.fillna("Unknown")
print(df2_filled)