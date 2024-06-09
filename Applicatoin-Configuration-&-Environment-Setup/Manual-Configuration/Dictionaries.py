# Import necessary modules from the Flask package
from flask import Flask, request, jsonify

# Define configuration settings for the Flask application
app_config = {
    'DEBUG': True  # Enable debug mode for the Flask application
}

# Create a Flask application instance
app = Flask(__name__)

# Update the application configuration settings with the specified configuration dictionary
app.config.update(app_config)

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


# Start the Flask application if the script is executed directly
if __name__ == "__main__":
    app.run()
