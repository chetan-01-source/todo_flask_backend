from db import db
class UserTaskModel(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(80), nullable=False)
    task = db.Column(db.String(800),nullable=False)
    user_id = db.Column(
        db.Integer,db.ForeignKey("user.id"), unique=False,nullable=False)
    user=db.relationship("UserModel",back_populates="tasks")