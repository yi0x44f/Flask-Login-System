from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.dashboard_controller import get_dashboard_data

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    return get_dashboard_data(current_user)