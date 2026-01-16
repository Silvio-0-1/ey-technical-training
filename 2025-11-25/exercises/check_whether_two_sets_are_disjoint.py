s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 10}

is_disjoint = True

for i in s1:
    if i in s2:
        is_disjoint = False
        break

print("Dis-joint" if is_disjoint else "Joint")
