marks = {
    "A": 85,
    "B": 92, 
    "C": 78, 
    "D": 92}

max_value = 0

for i in marks.values():
    if max_value < i:
        max_value = i
        
for i,j in marks.items():
    if j == max_value:
        print(i)
