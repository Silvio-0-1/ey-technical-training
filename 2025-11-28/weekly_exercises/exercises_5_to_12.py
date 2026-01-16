# 5. Remove duplicates from list
li = [1, 3, 1, 5, 1, 4, 5, 3, 6]
cleaned_li=[]
for x in li:
    if x not in cleaned_li:
        cleaned_li.append(x)
print(cleaned_li)

# 6. Rotate to the right by N positions
n = int(input())
l = len(li)
rotated_li = li[l-3:l] + li[0:l-n]
print(rotated_li)

# 7. Return a new list containing only strings > 4 characters
names = ["apple", "river", "stone", "cloud", "dream", "light", "star", "moon", "book", "sky"]
filtered_names = [x for x in names if len(x)>4]
print(filtered_names)

# 8. Convert a list of tuples into a dictionary
li = [("apple", 5), ("river", 3), ("stone", 8), ("cloud", 2)]
d = {}
for i in li:
    d[i[0]] = i[1]
print(d)

# 9. Given a tuple of numbers, find the second-largest number.
t = (1, 6, 4, 2, 9, 3)
print(sorted(list(t))[-2])

# 11. Given a list, print only those elements whose frequency is exactly 2 using sets.
li = [1,2,3,2,3]
y = set()
for i in li:
    if i not in y and li.count(i) == 2:
        y.add(i)
        print(i, end = " ")

# 12. Combine two dictionaries. If a key exists in both, create a list of values.
dict1 = {
    "id": 101,
    "name": "Alice",
    "department": "HR",
    "location": "New York"
}

dict2 = {
    "id": 101,
    "name": "Bob",
    "salary": 75000,
    "location": "Chicago",
    "role": "Manager"
}

dict3 = dict1.copy()

for i, j in dict2.items():
    if i in dict3:
        if type(dict3[i]) == list:
            dict3[i].append(j)
        else:
            dict3[i] = [dict3[i], j]
    else:
        dict3[i] = j
print(dict3)

