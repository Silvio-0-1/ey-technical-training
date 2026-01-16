numbers = (33, 20, 30, 60, 50)
max = numbers[0]
min = numbers[0]

for num in numbers[1:]:
    max_val = num if num > max_val else max_val
    min_val = num if num < min_val else min_val

print("Maximum: ", max)
print("Minimum: ", min)
