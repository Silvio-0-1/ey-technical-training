import pandas as pd
df = pd.read_csv("students.csv")

print(df)

print("Head: \n", df.head(2))
print("Tail: \n", df.tail(2))

print("Shape: ", df.shape)
print("Columns: \n", df.columns)
print("Describe: \n", df.describe())

print(df["Name"])
print(df[["Name", "Marks"]])

# Filters
high_scores = df[df["Marks"] > 70]
print("Marks more than 70: \n", high_scores)

filtered = df[(df["Marks"] > 70) & (df["Age"] > 22)]
print("Marks > 70 and Age > 22: \n", filtered)

