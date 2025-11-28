file_name = "notes.txt"

word_count = 0
for i in open(file_name,"r"):
    for j in i.split():
        word_count += 1

print(word_count)