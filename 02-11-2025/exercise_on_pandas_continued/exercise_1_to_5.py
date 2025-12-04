import pandas as pd

# 1. Load the CSV and display first 10 rows.
df = pd.read_csv("superstore_dataset.csv")
print("Top 10 rows:\n")
df.head(10)


# 2. Show total number of rows and columns.
print("No. of rows: ", df.shape[0], "\nNo. of columns: ",df.shape[1])


# 3. Find data types of each column.
df.dtypes


# 4. Identify columns containing missing values.
df.isna().sum()
# or
# df.isnull().sum()


# 5. Convert OrderDate and ShipDate to datetime.
df["OrderDate"]=pd.to_datetime(df["OrderDate"], format = "%d-%m-%Y")
df["ShipDate"]=pd.to_datetime(df["ShipDate"], format = "%d-%m-%Y")
