from flask import Flask, request

app = Flask(__name__)

@app.route("/get-item", methods = ["GET"])
def get_item():
	return "GET EXECUTED"

@app.route("/create-item", methods = ["POST"])
def create_item():
	return "POST EXECUTED"

@app.route("/get-item", methods = ["PUT"])
def update_item():
	return "PUT EXECUTED"

@app.route("/get-item", methods = ["DELETE"])
def delete_item():
	return "DELETE EXECUTED"

if __name__ == "__main__":
    app.run(debug = True)

