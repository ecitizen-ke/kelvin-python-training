# Import flask package and package modules
from flask import Flask, request, jsonify

# Define a class to hold configuration settings


class AppConfig:
    DEBUG = True


# Initialize the Flask application
app = Flask(__name__)

# Load configuration settings from the AppConfig class
app.config.from_object(AppConfig)

# Define a route to handle addition of numbers


@app.route('/add', methods=['GET'])
def add_numbers():
    # Get the values of 'num1' and 'num2' from the request query parameters,
    # or default to 0 if not provided
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))

    # Perform addition
    result = num1 + num2

    # Return the result as JSON
    return jsonify({'result': result})


# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run()
