# Import the Flask class from he flask module to create the Flask application
from flask import Flask

# Import the Blueprint objects and routes from the respective modules
from add_app import add_bp, routes  # Importing the add blueprint and routes

# Define a function to create the Flask application


def create_app():
    # Create instance of the Flask Class
    app = Flask(__name__)
    app.register_blueprint(add_bp)  # Pmporting the addbluprint and routes

    # Return the configured Flask application instance
    return app


# Create an instance if the flask appliication using the create_app funcion
app = create_app()

# Check if the script is being run directly (as opposed to being imported as a module)
if __name__ == '__main__':
    # Run the Flask application with debugging enabled
    app.run(debug=True)
