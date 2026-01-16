# MODULE 4: File Handling (Text, CSV, Exercises)

# 24. Read a text file and count: characters, words, lines.
with open("file.txt", "r") as f:
    content = f.read()
    line_count = len(content.split("\n"))
    word_count = 0
    character_count = 0
    for i in content.split("\n"):
        j = i.split()
        word_count += len(j)
        for k in j:
            character_count += len(k)

print(line_count)
print(word_count)
print(character_count)


# 25. Create a CSV file storing 5 employees and read it back into a dictionary list.

# 26. Write a program that appends log entries to a logfile with timestamps.
import datetime

def write_log(message, filename="logfile.txt"):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

write_log("Application started")
write_log("User logged in")
write_log("Error: Invalid input detected")
write_log("Application closed")

# 27. Build a program that loads a JSON file of products, adds a discount, and writes back.


# 28. Split a text file into two files: first half and second half.
with open("file.txt", "r") as f:
    content = f.read()
    with open("first_half.txt", "w") as g:
        g.write(content[0:len(content)//2])
    with open("second_half.txt", "w") as g:
        g.write(content[len(content)//2:len(content)])


# 29. Convert a CSV file to JSON using Python.