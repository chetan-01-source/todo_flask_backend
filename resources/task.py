from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.user import UserModel
from models.task import UserTaskModel
from schema import plainUserTaskSchema,UserTaskSchema,UserSchema,UpdateUserTaskSchema

blp = Blueprint("Tasks", "tasks", description="Operations on tasks")

@blp.route("/task")
class Task(MethodView):
    @blp.arguments(UserTaskSchema)
    @blp.response(201,UserTaskSchema)
    def post(self,task_data):
        task=UserTaskModel(**task_data) 

        try:
            db.session.add(task)
            db.session.commit()
            return task
        except SQLAlchemyError as e:
            print(e)
            abort(404,message="error occured while inserting a task")
    
    @blp.response(200,UserTaskSchema(many=True))
    def get(self):
        return UserTaskModel.query.all()
    
@blp.route("/task/<int:user_id>")
class singleTask(MethodView):
    @blp.response(200,UserSchema)
    def get(self,user_id):
        user=UserModel.query.get_or_404(user_id)
        return user
    
@blp.route("/delete/<int:task_id>")
class deleteTask(MethodView):
    def delete(self,task_id):
        task=UserTaskModel.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return {"status":200,"message":"item has been deleted"}
    
@blp.route("/update/<int:task_id>")
class UpdateTask(MethodView):
    @blp.arguments(UpdateUserTaskSchema)
    @blp.response(201,UserTaskSchema)
    def put(self,task_data,task_id):
         Task= UserTaskModel.query.get_or_404(task_id)
         if Task:
             Task.taskname=task_data["taskname"]
             Task.task=task_data["task"]
             db.session.commit()
             return Task
         else:
             task=UserTaskModel(id=task_id,**task_data)
             db.session.add(task)
             db.session.commit()
             return task