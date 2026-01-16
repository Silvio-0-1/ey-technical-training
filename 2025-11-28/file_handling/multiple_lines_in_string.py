def write_employee_record(emp_id, name, salary):
    record = f"""
    Employee Record:
    id: {emp_id}
    name: {name}
    salary: {salary}
    """

    with open("employee.txt", "w") as f:
        f.write(record)

write_employee_record(964, "Shubham", 35000)
