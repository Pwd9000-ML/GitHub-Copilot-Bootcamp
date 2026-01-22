from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret')
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    from app.routes.users import users_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    
    # Health check
    @app.route('/health')
    def health():
        return {'status': 'ok', 'service': 'bootcamp-backend-py'}, 200
    
    # Error handlers
    # TODO: Add comprehensive error handlers
    # - 400 Bad Request
    # - 401 Unauthorized
    # - 403 Forbidden
    # - 404 Not Found
    # - 500 Internal Server Error
    
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404
    
    return app
