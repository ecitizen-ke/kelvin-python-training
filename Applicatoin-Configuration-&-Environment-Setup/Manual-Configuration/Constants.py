# Import necessary modules from the Flask package
from flask import Flask, request, jsonify

# Set debug mode to True
DEBUG = True

# Additional configuration settings
HOST = '0.0.0.0'
PORT = 5000
ENVIRONMENT = 'development'

# Create a Flask application instance
app = Flask(__name__)

# Set debug mode and additional configuration settings using app.config
app.config['DEBUG'] = DEBUG
app.config['HOST'] = HOST
app.config['PORT'] = PORT
app.config['ENV'] = ENVIRONMENT

# Define a route for adding numbers


@app.route('/add', methods=['GET'])
def add_numbers():
    # Extract 'num1' and 'num2' parameters from the query string, defaulting to 0 if not provided
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))

    # Calculate the sum of 'num1' and 'num2'
    result = num1 + num2

    # Return the result as JSON
    return jsonify({'result': result})


# Start the Flask application
if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'],
            debug=app.config['DEBUG'], env=app.config['ENV'])
