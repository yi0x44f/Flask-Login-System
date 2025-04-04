from flask import jsonify

def get_dashboard_data(current_user):
    return jsonify({
        'message': f'Welcome to the dashboard, {current_user["name"]}!',
        'user': current_user
    }), 200