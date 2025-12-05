# MODULE 2: Data Structures (Lists, Tuples, Sets, Dicts) (10 Exercises)

# 6. Given a list of product prices, remove duplicates while maintaining order.
li = [10, 34, 89, 34, 45, 10, 89]
unique = []
for i in li:
    if i not in unique:
        unique.append(i)
print(unique)


# 7. Merge two lists into a dictionary of {key: value} where list1 is keys and list2 is values.
keys = [1, 2, 3, 4, 5]
values = ["a", "b", "c", "d", "e"]
di = {}
for i in range(0, len(keys)):
    di[keys[i]] = values[i]
print(di)


# 8. Given a dictionary of student marks, return the top 3 students.
di = {
    "student1" : 98,
    "student2" : 95,
    "student3" : 91,
    "student4" : 94,
    "student5" : 94
}
sorted_by_values = dict(sorted(di.items(), key=lambda item: item[1], reverse=True))
count = 0
for i, j in sorted_by_values.items():
    print(i, j)
    count += 1
    if count == 3:
        break


# 9. Flatten a nested list like [[1,2],[3,4,5],6,[7, 8]] into a single list.
def flatten_list(li):
    for i in li:
        if type(i) == list:
            flatten_list(i)
        else:
            print(i, end= " ")

flatten_list([[1,2],[3,4,5],6,[7, 8]])


# 10. Find common elements between three sets.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6, 7}
C = {7, 8, 3, 4, 1, 5}

print((A & B) & C)


# 11. Convert a list of tuples to a dictionary.
li = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e")]
di = {}
for i in li:
    di[i[0]] = i[1]
print(di)


# 12. Given a tuple of names, return one tuple with unique names.
tup = ("Alice", "Bob", "Charlie", "Diana", "Ethan", "Charlie", "Alice", "Diana")
print(tuple(set(tup)))

# 13. Build a program to reverse every alternate element in a list.
li = ["Aurora", "Banana", "Cobalt", "Delta", "Echo", "Falcon", "Galaxy", "Horizon"]
for i in range(0, len(li), 2):
    li[i] = li[i][::-1]
print(li)

# 14. From a dictionary of employees, filter only employees with salary above 60000.
di = {
    "Alice": 60500,
    "Bob": 59800,
    "Charlie": 61200,
    "Diana": 59000,
    "Ethan": 60000
}
di2 = di.copy()
for keys, values in di.items():
    if values < 60000:
        del di2[keys]
print(di2)


# 15. Given two dictionaries, combine them but sum values for same keys.
dict1 = {"Alice": 60000, "Bob": 58000, "Charlie": 62000}
dict2 = {"Bob": 2000, "Diana": 59000, "Charlie": 3000}

dict3 = dict1.copy()

for i, j in dict2.items():
    if i in dict3.keys():
        dict3[i] += dict2[i]
    else:
        dict3[i] = dict2[i]

print(dict3)