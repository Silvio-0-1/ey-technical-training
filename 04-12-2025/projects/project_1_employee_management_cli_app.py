# Project 1: Employee Management CLI App
# Connect Python MySQL and build features:
# 1. Add employee
# 2. View all
# 3. Update salary
# 4. Delete employee
# 5. Search by name
# 6. Export to CSV

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='P@ssword',
    database='emp'
)
if conn:
    print("Connection is successful")

cursor = conn.cursor()

# 1. Add employee
def add_employee():
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    dept = input("Enter employee department: ")

    query = """
        INSERT INTO employee_details (emp_id, emp_name, salary, dept_name)
        VALUES (%s, %s, %s, %s)    
    """
    try:
        cursor.execute(query, (emp_id, name, salary, dept))
        conn.commit()
        print("Employee added successfully!")
    except:
        print("Employee ID already exists!")

# 2. View all
def view_employees():
    query = """
        SELECT * FROM employee_details
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("Employees displayed successfully!")

# 3. Update salary
def update_salary():
    emp_id = int(input("Enter employee ID to update: "))
    new_salary = int(input("Enter new salary: "))
    query = """
        UPDATE employee_details
        SET salary = %s
        WHERE emp_id = %s
    """
    cursor.execute(query, (new_salary, emp_id))
    conn.commit()
    print("Salary updated successfully!")

# 4. Delete employee
def delete_employee():
    try:
        emp_id = int(input("Enter employee ID to be deleted: "))
        query = """
            DELETE FROM employee_details
            WHERE emp_id = %s
        """
        cursor.execute(query, (emp_id))
        conn.commit()
        print("Employee deleted successfully!")
    except:
        print("Employee ID does not exist!")


# 5. Search by name
def search_by_name():
    name = input("Enter employee name: ")
    query = """
        SELECT * FROM employee_details
        WHERE emp_name = %s
    """
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute(query, (name))
    print("Employee details displayed successfully!")

# 6. Export to CSV
import pandas as pd
def export_to_csv():
    query = """
            SELECT * FROM employee_details
        """
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    df.to_csv("employee_details.csv", index=False)
    print("Employee details exported successfully!")


while 1:
    print("\n\nWelcome to the employee management app!")
    print("1. Add employee")
    print("2. View employees")
    print("3. Update employee salary")
    print("4. Delete an employee")
    print("5. Search employee by name")
    print("6. Export employees to csv file")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    elif choice == 3:
        update_salary()
    elif choice == 4:
        delete_employee()
    elif choice == 5:
        search_by_name()
    elif choice == 6:
        export_to_csv()
    elif choice == 7:
        break
    else:
        print("Invalid choice!")

cursor.close()
conn.close()
