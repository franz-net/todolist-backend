from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"title": "Thrash day", "description": "On Wednesdays take the trhash out", "complete": False},
    {"title": "Chorus", "description": "Take sofia to chorus", "complete": True},
]


@app.route("/api/v1/task")
def getTasks():
    return jsonify(tasks)
