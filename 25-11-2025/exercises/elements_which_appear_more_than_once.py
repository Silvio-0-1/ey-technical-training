li = [1, 2, 3, 2, 4, 1, 5, 1]
li2 = []
dict = {}

for i in li:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
 
for i, j in dict.items():
    if j > 1:
        li2.append(i)
print(li2)

# or

# for i in set(li):
#     if li.count(i) > 1:
#         li2.append(i)
# print(li2)
