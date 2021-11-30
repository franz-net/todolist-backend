from flask import Flask, jsonify, request
from flask.scaffold import _matching_loader_thinks_module_is_package
from models.task import Task, TaskSchema

app = Flask(__name__)

tasks = [
    Task("Thrash day", "On Wednesdays take the trhash out", "Completed"),
    Task("Chorus", "Take sofia to chorus", "In Progress"),
]


@app.route("/api/v1/task")
def getTasks():
    schema = TaskSchema(many=True)
    return jsonify(schema.dump(tasks))


@app.route("/api/v1/task", methods=["POST"])
def addTask():
    task = TaskSchema().load(request.get_json())
    tasks.append(task)
    return "", 204
