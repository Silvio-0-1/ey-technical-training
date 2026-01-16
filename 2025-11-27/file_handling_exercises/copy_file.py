original_file = "notes.txt"
duplicate_file = "duplicate_notes.txt"

with open(original_file,"r") as f:
    content = f.read()

with open(duplicate_file,"w") as f:
    f.write(content)
