try:
 value = int("50")
except VatueError:
    print("Invalid conversion")
else:
    print("Conversion successful:", value)
