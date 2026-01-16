x = [0, 3, 0, 5, 7, 0, 9]

y = [i for i in x if i !=0]
for i in range (0, x.count(0)):
    y.append(0)
  
print(y)

