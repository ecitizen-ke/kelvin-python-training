# Import necessary modules from the Flask package
from flask import Flask, request, jsonify
import os

# Set the 'FLASK_DEBUG' environment variable to '1' (True)
os.environ['FLASK_DEBUG'] = '1'
# Set additional configuration settings using environment variables
os.environ['DATABASE_URL'] = 'mysql://user:password@localhost/db_name'
os.environ['SECRET_KEY'] = 'your_secret_key'
os.environ['LOG_LEVEL'] = 'DEBUG'

# Create a Flask application instance
app = Flask(__name__)

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


# Start the Flask application with debug mode based on the 'FLASK_DEBUG' environment variable
if __name__ == "__main__":
    app.run(debug=bool(os.environ.get('FLASK_DEBUG', False)))
