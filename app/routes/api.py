from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.api_controller import get_dashboard_data
from app.controllers.api_controller import get_aichat_data

api_bp = Blueprint('api', __name__)

@api_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    return get_dashboard_data(request)


@api_bp.route('/aichat')
def aichat(request):
    return get_aichat_data(request)