from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_migrate import Migrate

jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    return app
