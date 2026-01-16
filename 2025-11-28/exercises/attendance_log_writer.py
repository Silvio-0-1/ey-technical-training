attendance_log = lambda name, timestamp, status: f"Name: {name}, Status: Present, Reporting Time: {timestamp}" if status else f"{name}, Status: Absent"

with open("attendance_log.txt", "w") as f:
    for i in range(0, int(input("Enter number of students: "))):
        name = input(f"Enter student{i+1} name: ")
        status = int(input(f"Enter 1 for Present or 0 for Absent:"))
        if status:
            timestamp = input(f"Enter student{i+1} timestamp: ")
        f.write(attendance_log(name, timestamp, status) + "\n")
print("Report generated!")