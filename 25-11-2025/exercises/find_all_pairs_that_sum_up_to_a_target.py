s = {2, 4, 6, 8, 10}

pairs = {(i,j) for i in s for j in s if i+j == 12 and i <= j}

print(pairs)
