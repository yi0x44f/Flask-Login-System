from flask import Blueprint, jsonify, request
from app.controllers.auth_controller import login_user, register_user, logout_user

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