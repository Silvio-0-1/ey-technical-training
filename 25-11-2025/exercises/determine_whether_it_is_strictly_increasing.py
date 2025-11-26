numbers = (1, 3, 5, 4, 7, 9)

is_increasing = True

for i in range(0, len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        is_increasing = False
        break

print("Strictly Increasing" if is_increasing else "Not strictly increasing")
