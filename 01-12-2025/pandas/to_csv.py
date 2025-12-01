import pandas as pd

data = {
"Name": ["Aisha", "Rahul", "John"],
"Marks": [85, 92, 78],
"City": ["Mumbai", "Delhi", "Chennai"]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index = False)
print("CSV file created.")