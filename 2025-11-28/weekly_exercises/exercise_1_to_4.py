# 1. Print the largest
print(max(int(input("Enter num 1: ")), int(input("Enter num 2: ")), int(input("Enter num 3: "))))

# 2. Palindrome
word = input("Enter word: ")
print("Palindrome" if word == word[::-1] else "Not Palindrome")

# 3. Count Characters
from collections import Counter
print(Counter(input("Enter word: ")))

# 4. Remove special characters
word = input("Enter word: ")
print("".join(ch for ch in word if ch.isalnum()))