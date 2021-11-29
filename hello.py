from flask import Flask, jsonify, request
from models.task import Task

app = Flask(__name__)

tasks = [
    Task("Thrash day","On Wednesdays take the trhash out",False),
    Task("Chorus","Take sofia to chorus",True),
]


@app.route("/api/v1/task")
def getTasks():
    return jsonify(tasks)
