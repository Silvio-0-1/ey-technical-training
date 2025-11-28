with open("notes.txt", "r") as f:
    for i in f.read().split("\n"):
        if "Python" in i:
            print(i)
