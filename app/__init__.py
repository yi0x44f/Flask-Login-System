from flask import Flask
from config import Config
from flask_cors import CORS
from app.models.user import db
from flask_jwt_extended import JWTManager
from datetime import timedelta

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)
    db.init_app(app)
    
    jwt.init_app(app)

    with app.app_context():
        db.create_all()
    # Register blueprints here when you create them
    # from app.controllers.test_controller import test_bp
    # app.register_blueprint(test_bp)

    return app
