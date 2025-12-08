from flask import Flask, request, jsonify

app = Flask(__name__)

employee = [
    ("name", "Shubham"),
    ("id", 64),
    ("company", "EY"),
    ("salary", 35)
]

@app.route("/emp_details", methods = ["GET"])
def get_item():
	return jsonify(employee)

@app.route("/emp_details", methods = ["POST"])
def add_item():
	data = request.get_json()
	item = data.get("nickname")
	employee.append(("nickname", item))
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