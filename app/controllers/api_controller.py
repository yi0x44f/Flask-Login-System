from flask import jsonify
from flask_jwt_extended import get_jwt_identity

def get_dashboard_data(request):
    identity = get_jwt_identity()
    return jsonify({
        'message': 'Welcome',
        'user':{
            'name': identity['name'],
            'email': identity['email']
        }
    })

def get_aichat_data(request):
    return jsonify({
        'message': 'AI Chat'
    })