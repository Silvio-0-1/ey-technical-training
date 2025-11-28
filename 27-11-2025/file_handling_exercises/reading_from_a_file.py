file_name = "notes.txt"

with open(file_name, "r") as file:
        for line in file:
            print(line.strip())  # strip() removes extra newline characters

