nums = [23, 89, 12, 78, 55, 42]

max = second_max = -1
for i in nums:
    if max < i:
        max = i

for i in nums:
    if second_max < i and i is not max:
        second_max = i
print(second_max)
