s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6 ,7, 8}

s3 = {i for i in s1 if i not in s2} | {j for j in s2 if j not in s1}

print(s3)
