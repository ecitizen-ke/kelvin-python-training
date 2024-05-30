from flask import Flask
from add_app import add_bp, routes
from subtract_app import subtract_bp, routes
from multiply_app import multiply_bp, routes
from divide_app import divide_bp, routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(add_bp)
    app.register_blueprint(subtract_bp)
    app.register_blueprint(multiply_bp)
    app.register_blueprint(divide_bp)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
