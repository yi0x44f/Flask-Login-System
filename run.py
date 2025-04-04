from sqlalchemy import text
from flask import jsonify, request, session, Flask
from app.models import User
from app import create_app, db
from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello world.'

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)