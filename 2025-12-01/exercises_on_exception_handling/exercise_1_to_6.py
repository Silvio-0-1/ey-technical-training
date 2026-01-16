# 1. Zero-division Error
try:
    x, y = int(input()), int(input())
    print(x/y)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. FileNotFoundError and PermissionError
try:
    with open("data.txt", "r") as file:
        value = int(file.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")

# 3. ValueError
try:
 value = int("50")
except ValueError:
    print("Invalid conversion")
else:
    print("Conversion successful:", value)

# 4 IndexError
li = [1,2,3,4,5]
x = int(input("Enter an index number : "))
try:
    print(li[x])
except IndexError:
    print("Index out of range")


# 5. Open a CSV file and handle incorrect file format errors.
class IncorrectFileFormatError(Exception):
    pass

try:
    with open("data.csv") as f:
        reader = f.read()
except FileNotFoundError:
    print("File not found")
except:
    raise IncorrectFileFormatError("Incorrect file format")


# 6. InvalidAgeError if age < 18.
class InvalidAgeError(Exception):
    pass

def calculate_age(age):
    if age < 18:
        raise InvalidAgeError("Age is less than 18")
    return "Eligible"

print(calculate_age(20))
