generate_birth_certificate = lambda student, date, time: f"This is to certify that {student} was born on {date} at {time}"

with open("student_names.txt", "w") as f:
    f.write("""
    Shubham, 09 April, 22:30
    Ritaja, 23 August, 21:50
    """)

with open("student_names.txt", "r") as f:
    for i in f:
        record = [x.strip() for x in i.split(",")]
        print(record)
        if len(record) == 3:
            with open(f"{record[0]}.txt","w") as h:
                h.write(generate_birth_certificate(record[0],record[1],record[2]))
