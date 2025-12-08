from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [
    {
        "name": "Alice",
        "salary": 50000,
        "department": "HR",
        "designation": "Manager"
    },
    {
        "name": "Bob",
        "salary": 60000,
        "department": "IT",
        "designation": "Software Engineer"
    },
    {
        "name": "Charlie",
        "salary": 55000,
        "department": "Finance",
        "designation": "Analyst"
    }
]

@app.route("/emp_details", methods = ["GET"])
def get_item():
	return jsonify(employees)

@app.route("/emp_details", methods = ["POST"])
def add_item():
	data = request.get_json()
	new_employee = {
        "name" : data["name"],
        "salary" : data["salary"],
        "department" : data["department"],
        "designation" : data["designation"]
    }
	employees.append(new_employee)
	return "POST EXECUTED"


@app.route("/emp_details/<int:index>", methods = ["PUT"])
def update_item(index):
    data = request.get_json()
    new_value = data.get("salary")
    employee[index] = ("salary", new_value)
    return "PUT EXECUTED"

@app.route("/emp_details/<int:index>", methods = ["DELETE"])
def delete_item(index):
    employee.pop(index)
    return "PUT EXECUTED"

if __name__ == "__main__":
    app.run(debug = True)