li = [1, -4, 0, -8, 5, -10, -9, 2]

for i in li:
    if i >= 0:
        li.remove(i)
        li.append(i)
        
print(li)
  
