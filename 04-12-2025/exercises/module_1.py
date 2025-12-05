# MODULE 1: Python Basics (5 Exercises)

# 1. Write a program that reads a string and prints the number of vowels, consonants, and digits.
word = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
vowel_counter = consonant_counter = digit_counter = 0
for letter in word:
    if letter in vowels:
        vowel_counter += 1
    elif letter.isdigit():
        digit_counter += 1
    elif letter != " ":
        consonant_counter += 1
print("No. of vowels: ", vowel_counter)
print("No. of consonants: ", consonant_counter)
print("No. of digits: ", digit_counter)


# 2. Create a function that takes a sentence and returns a dictionary of word frequencies.
def word_counter(word):
    di = {}
    for i in word.split():
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    return di

print(word_counter(input("Enter a word: ").lower()))

# 3. Implement a mini calculator with add, subtract, multiply, and divide using functions.
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

num1, num2 = int(input("Enter a number: ")), int(input("Enter another number: "))
x = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
print(addition(num1, num2) if x ==1 else subtraction(num1, num2) if x ==2 else multiplication(num1, num2) if x == 3 else division(num1, num2))

# 4. Write a program that reads N numbers and returns the second highest value without sorting.
li = []
max = second_max = 0
for i in range(5):
    li.append(int(input()))

for i in li:
    if i > max:
        second_max = max
        max = i
    elif i < max and i > second_max:
        second_max = i

print(second_max)

# 5. Read 10 values and store them into a list without using loops (use list comprehension).
li = [int(input()) for x in range(10)]
print(li)
