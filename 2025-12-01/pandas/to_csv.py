import pandas as pd

data = {
"Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
"Marks": [85, 92, 78, 65, 55],
"City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
"Age": [22, 25, 23, 21, 24]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index = False)
print("CSV file created.")


