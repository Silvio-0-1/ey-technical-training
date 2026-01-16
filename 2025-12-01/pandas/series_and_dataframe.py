import pandas as pd

#Series
s = pd.Series([10, 20, 30, 40])
print(s)

# Dataframe
data = {
"Name": ["Aisha", "Rahul", "John"],
"Marks": [85, 92, 78]
}

df = pd.DataFrame(data)
print(df)