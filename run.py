from app import create_app
from app.routes.auth import auth_bp
from app.routes.api import api_bp

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello world.'

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)