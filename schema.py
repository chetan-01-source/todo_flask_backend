from marshmallow import fields,Schema

class plainUserTaskSchema(Schema):
    id = fields.Int(dump_only=True)
    taskname = fields.Str(required=True)
    task = fields.Str(required=True)

class plainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)

class UpdateUserTaskSchema(Schema):
    
    taskname=fields.Str(required=True)
    task=fields.Str(required=True)

class UserTaskSchema(plainUserTaskSchema):
    user_id=fields.Int(required=True,load_only=True)
    user=fields.Nested(plainUserSchema(),dump_only=True)
class UserSchema(plainUserSchema):
    tasks=fields.List(fields.Nested(plainUserTaskSchema()), dump_only=True)