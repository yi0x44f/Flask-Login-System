from flask import jsonify
from werkzeug.security import check_password_hash
from app.models.user import User
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity



def login_user(request):
    data = request.json
    name = data.get('name')
    password = data.get('password')

    if not name or not password:
        return jsonify({'message': 'Name and password are required!'}), 400

    user = User.query.filter_by(name=name).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity={'name': user.name})
        refresh_token = create_refresh_token(identity={'name': user.name})
        return jsonify({
            'message': 'Login success!',
            'user': {
                'name': user.name,
                'email': user.email
            },
            'access_token': access_token,
            'refresh_token': refresh_token
        }), 200
    else:
        return jsonify({'message': 'Login failed! Invalid name or password.'}), 401

def register_user(request):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(name=name).first():
        return jsonify({'message': 'Name already exists!'}), 400
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists!'}), 400



    new_user = User(name=name, email=email, password=password)

    try:
        new_user.save()
        return jsonify({
            'message': 'Registration success!',
            'user': {
                'name': new_user.name,
                'email': new_user.email
            }
        }), 201
    except Exception as e:
        new_user.rollback()
        return jsonify({'message': 'Registration failed!', 'error': str(e)}), 500

def refresh_user(request):
    print("Authorization header:", request.headers.get('Authorization'))

    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)
    return jsonify({
        'message': 'Token refreshed successfully!',
        'access_token': new_access_token
    }), 200

def logout_user():
    return jsonify({'message': 'Logout success!'}), 200