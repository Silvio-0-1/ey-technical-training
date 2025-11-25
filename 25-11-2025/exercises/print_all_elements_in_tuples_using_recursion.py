def print_dict(t):
    for i in t:
        if type(i) != tuple:
            print(i)
        else:
            print_dict(i)

t = (10, (20, 30), (40, (50, 60)))
print_dict(t)
