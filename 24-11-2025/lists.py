# creating and printing a list
x=[10, 20, 30, 40, 50]
print(x)

# list indexing
fruits=["cherry", "apple", "tomato"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# list traversal
l=[]
for i in range(1, 21):
    l.append(i)
print(l)
for i in l:
    if i%2==0:
        print(i, " is even.")
    else:
        print(i, " is odd.")

# list operations
fruits=["cherry", "apple", "tomato"]
print(fruits)

fruits[1]="kiwi"
print(fruits)

fruits.append("mango")
print(fruits)

fruits.insert(1, "banana")
print(fruits)
