mixed_tuple = (42, "hello", 3, "world", 100)

str_tuple = tuple(i for i in mixed_tuple if type(i) is str)
num_tuple = tuple(i for i in mixed_tuple if type(i) is int)

print(str_tuple)
print(num_tuple)
