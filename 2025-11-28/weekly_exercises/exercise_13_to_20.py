# 13. Function that accepts a list of numbers and returns the average
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 14. Function that returns the factorial of a number
def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


# 15. Function that removes all vowels from a string
def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return "".join(x for x in word if x not in vowels)
print(remove_vowels(input("Enter a word: ").lower()))

# 16. Function that finds prime between two numbers
def prime(m, n):
    for i in range(m, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end = " ")

prime(2, 20)

# 17. Write a function that finds the longest word in a given sentence.
def longest_word(sentc):
    return max(sentc.split(" "), key=len)

print(longest_word("this is a sentence"))

# 18. Use lambda to sort a list of dictionaries by the key "age".
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 28}
]

print(sorted(people, key = lambda x:x["age"]))


# 19. Use lambda to compute squares of all elements in a list
y = lambda x:x**2
li = [1, 2, 3, 4, 5]
for i in li:
    print(y(i), end = " ")

# 20. Use lambda with filter to return only even numbers from a list
li = [1, 2, 3, 4, 5, 6]
y = list(filter(lambda x: x%2==0, li))
print(y)