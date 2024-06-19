from flask import Flask
from .settings import Config
# Function to create and configure the Flask application


def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # Configure the application with a secret key for CSRF protection
    app.config.from_object(Config)

    # Import and register the routes blueprint
    from app.routes import routes_bp
    app.register_blueprint(routes_bp)

    # Return the configured Flask application instance
    return app
