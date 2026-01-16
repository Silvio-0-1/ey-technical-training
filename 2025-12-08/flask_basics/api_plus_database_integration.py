from flask import Flask, request, jsonify
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='P@ssword',
    database='employee'
)

cursor = conn.cursor()

app = Flask(__name__)

@app.route("/employee", methods=["GET"])
def get_employee():
    sql = "SELECT * FROM employee_details"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)


@app.route("/employee", methods=["POST"])
def add_item():
    data = request.get_json()
    id = data.get("id")
    name = data.get("name")
    salary = data.get("salary")

    if not id or not name or not salary:
        return jsonify({"error": "id, name, and salary are required"}), 400

    sql = "INSERT INTO employee_details (id, name, salary) VALUES (%s, %s, %s)"
    cursor.execute(sql, (id, name, salary))
    conn.commit()
    return "Employee added successfully"


@app.route("/employee/<int:id>", methods=["DELETE"])
def delete_by_index(id):
    try:
        sql = "DELETE FROM employee_details WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()
        return "Employee deleted successfully"
    except:
        return jsonify({"error": "Invalid index"}), 400


@app.route("/employee/<int:id>", methods=["PUT"])
def put_item(id):
    try:
        data = request.get_json()
        name = data.get("name")
        salary = data.get("salary")

        if not name or not salary:
            return jsonify({"error": "name, and salary are required"}), 400

        sql = "UPDATE employee_details SET name=%s, salary=%s WHERE id=%s"
        cursor.execute(sql, (name, salary, id))

        conn.commit()

        return "Employee updated successfully"
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def page_not_found(e):
    return "Route doesn't exist", 404


if __name__ == "__main__":
    app.run(debug=True)

cursor.close()
conn.close()