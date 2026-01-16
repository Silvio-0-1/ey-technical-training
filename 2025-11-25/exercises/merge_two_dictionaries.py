dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
li = []
dict3 = {}

for i, j in dict1.items():
        dict3[i]= j

for i, j in dict2.items():
    if i in dict3:
        if type(dict3[i]) == list:
            dict3[i].append(j)
        else:
            dict3[i]=[dict3[i],j]
    else:
        dict3[i]= j       
        
print(dict3)
