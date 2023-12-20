from flask import Flask, jsonify
from flask_smorest import Api
from db import db
from resources.user import blp as UserBlueprint
from resources.task import blp as TaskBlueprint
def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///todo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(TaskBlueprint)
    # JWT configuration ends

    with app.app_context():
        import models  # noqa: F401

        db.create_all()

    return app
