# Email Template Generator
# Write a script that reads names from names.txt and generates email templates like:
#
# Dear <name>,
# Your training session starts tomorrow.
# Regards,
# Training Team

email_message = lambda name: f"""Dear {name},
Your training session starts tomorrow.
Regards,
Training Team"""

with open("student_names.txt", "r") as f:
    for i in f:
        record = [x.strip() for x in i.split(",")]
        print(record)
        with open(f"{record[0]}_email.txt", "w") as h:
            h.write(email_message(record[0]))

