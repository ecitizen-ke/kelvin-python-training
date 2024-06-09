# Import the 'multiply' function from the 'multiply' module within the current package
from .multiplication import multiply
# Import the 'multiply_bp' Blueprint from the current package
from . import multiply_bp
# Import necessary modules from Flask
from flask import current_app as app, request, jsonify

# Define a route for multiplying two numbers


@multiply_bp.route('/multiply', methods=['GET'])
def multiply_route():
    # Retrieve 'num1' and 'num2' from the query parameters of the request URL, defaulting to 0 if not provided
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    # Calculate the result by calling the 'multiply' function with 'num1' and 'num2' as arguments
    result = multiply(num1, num2)
    # Return a JSON response containing the result of the multiplication
    return jsonify({'result': result})
