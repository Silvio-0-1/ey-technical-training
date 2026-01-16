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

# Only employees whose department id exists in department
@app.route("/employee/innerjoin", methods=["GET"])
def get_inner_join():
    sql = """
        SELECT e.name, d.d_name 
        FROM employee_details e 
        INNER JOIN department d 
        ON e.d_id = d.d_id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

# All employees with department names (including those without departments)
@app.route("/employee/leftjoin", methods=["GET"])
def get_left_join():
    sql = """
        SELECT e.name, d.d_name 
        FROM employee_details e 
        LEFT JOIN department d 
        ON e.d_id = d.d_id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

# All departments and the employees under them
@app.route("/employee/rightjoin", methods=["GET"])
def get_right_join():
    sql = """
        SELECT e.name, d.d_name 
        FROM employee_details e 
        RIGHT JOIN department d 
        ON e.d_id = d.d_id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

# All possible employees and departments
@app.route("/employee/fulljoin", methods=["GET"])
def get_full_join():
    sql = """
        SELECT e.name, d.d_name
        FROM employee_details e
        LEFT JOIN department d ON e.d_id = d.d_id
        UNION
        SELECT e.name, d.d_name
        FROM employee_details e
        RIGHT JOIN department d ON e.d_id = d.d_id
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

# All possible cross product of employee and department
@app.route("/employee/crossjoin", methods=["GET"])
def get_cross_join():
    sql = "SELECT e.name, d.d_name FROM employee_details e CROSS JOIN department d"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)

cursor.close()
conn.close()