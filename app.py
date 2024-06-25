from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def star_data():
    return jsonify({
        "data": data,
        "message": "Success"
    })

@app.route("/star")
def star():
    name = request.args.get()
    star_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data": star_data, 
        "message": "Success"
    })

app.run()