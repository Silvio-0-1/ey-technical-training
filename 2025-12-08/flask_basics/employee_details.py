from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [
    {
        "id": 1001,
        "name": "Alice",
        "salary": 50000,
        "department": "HR",
        "designation": "Manager"
    },
    {
        "id": 1002,
        "name": "Bob",
        "salary": 60000,
        "department": "IT",
        "designation": "Software Engineer"
    },
    {
        "id": 1003,
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
        "id" : data.get("id"),
        "name" : data["name"],
        "salary" : data["salary"],
        "department" : data["department"],
        "designation" : data["designation"]
    }
	employees.append(new_employee)
	return "POST EXECUTED"


@app.route("/emp_details/<int:id>", methods = ["PUT"])
def update_item(id):
    data = request.get_json()
    for i in employees:
        if i["id"] == id:
            if data.get("name"):
                i["name"] = data["name"]
            if data.get("salary"):
                i["salary"] = data["salary"]
            if data.get("department"):
                i["department"] = data["department"]
            if data.get("designation"):
                i["designation"] = data["designation"]
    return "PUT EXECUTED"

@app.route("/emp_details/<int:id>", methods = ["DELETE"])
def delete_item(id):
    for i in employees:
        if i["id"] == id:
            employees.remove(i)
    return "DEL EXECUTED"

if __name__ == "__main__":
    app.run(debug = True)