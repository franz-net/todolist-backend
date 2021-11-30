from marshmallow import Schema, fields


class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return "<Task(name={self.title!r}>".format(self=self)


class TaskSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    status = fields.Str()
