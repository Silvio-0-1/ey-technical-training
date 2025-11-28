w, c, i = "WARNING", "CRITICAL", "INFO"
w_count, c_count, i_count = 0, 0, 0
with open("error.log", "r") as f:
    for line in f:
        if w in line:
            w_count += 1
        elif c in line:
            c_count += 1
        elif i in line:
            i_count += 1

with open("error_summary", "w") as f:
    f.write(f"Number of warnings: {w_count}\n")
    f.write(f"Number of criticals: {c_count}\n")
    f.write(f"Number of errors: {i_count}")