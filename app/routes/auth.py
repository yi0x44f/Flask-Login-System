from flask import Blueprint, request
from app.controllers.auth_controller import login_user, register_user, logout_user, refresh_user
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_user(request)

@auth_bp.route('/register', methods=['POST'])
def register():
    return register_user(request)

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return logout_user()

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    return refresh_user(request)