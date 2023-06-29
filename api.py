from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

#path parameter/ query paramter
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "John Doe",
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200
#we jsonify the dictionary for the user, allows flask to parse value and return as json data

@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

@app.route("/api")
def api():
    response = requests.get("https://randomfox.ca/floof")
    json = response.json()
    image = json["image"]

    return image

    #you can get data in raw format , string, html

if __name__ == "__main__":
    app.run(debug=True)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello/{name}")
async def hello(name):
    return f"hello {name}"