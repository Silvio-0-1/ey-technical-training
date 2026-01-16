expense_generator = lambda name,  amount: f"{name}: Rs. {amount}"
total = 0
with open("report.txt", "w") as f:
    f.write("Expense Report:\n\n")
    for i in range(0,int(input("Enter total number of items: "))):
        name, amount = input(f"Enter item {i+1} name: "), int(input(f"Enter item {i+1} amount: "))
        f.write(expense_generator(name, amount) + "\n")
        total += amount
    f.write(f"Total Expense: {total}")
print("Report Generated!")
