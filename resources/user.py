from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from db import db
from models.user import UserModel
from models.task import UserTaskModel
from schema import UserSchema,plainUserSchema


blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201,plainUserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data["username"]).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )
        db.session.add(user)
        db.session.commit()

        return user


@blp.route("/getuser")
class GetUser(MethodView):
    @blp.response(200,UserSchema(many=True))
    def get(self):
        return UserModel.query.all()
@blp.route("/getuser/<int:user_id>")
class GetsingleUser(MethodView):
    @blp.response(200,UserSchema())
    def get(self,user_id):
        return UserModel.query.get_or_404(user_id)