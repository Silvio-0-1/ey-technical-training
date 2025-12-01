#   Create a bank withdrawal function that raises LowBalanceError when balance is insufficient.
#   Write a safe calculator function that handles invalid operators and incorrect inputs.
#   Write a program using try–except–else–finally to read user input and write it into a file safely.

# 7. Convert items of a list to integers, handling conversion errors
li = ["1", "2", "3", "X", "4", "5"]
li2 = []
for i in li:
    try:
        li2.append(int(i))

    except ValueError:
        print("Could not convert to an integer.")
print(li2)


# 10. Using try–except–else–finally to read user input and write it into a file safely.
def write_to_file():
    try:
        with open("file.txt", "w") as f:
            f.write(input())
    except FileNotFoundError:
        print("File not found.")
    else:
        print(f"Successfully written to file.")
    finally:
        f.close()
        print("Operation completed.")

write_to_file()