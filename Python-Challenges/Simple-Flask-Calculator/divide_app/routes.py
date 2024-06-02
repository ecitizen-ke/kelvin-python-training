# Import the 'divide' function from the 'divide' module in the current package
from .divide import divide
# Import the 'divide_bp' Blueprint from the current package
from . import divide_bp
# Import necessary modules from Flask
from flask import current_app as app, request, jsonify

# Define a route for handling division requests


@divide_bp.route('/divide', methods=['GET'])
def add_route():
    # Get the values of 'num1' and 'num2' from the request parameters, defaulting to 0 if not provided
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    # Calculate the result of dividing 'num1' by 'num2' using the 'divide' function
    result = divide(num1, num2)
    # Return a JSON response containing the division result
    return jsonify({'result': result})
