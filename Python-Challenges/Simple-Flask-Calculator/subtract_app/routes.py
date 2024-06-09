# Import the subtract function from the subtract module within the current package
from .subtract import subtract
# Import the subtract_bp Blueprint from the current package
from . import subtract_bp
# Import objects from Flask needed for the route handler
from flask import current_app as app, request, jsonify

# Define a route for handling GET requests to '/subtract'


@subtract_bp.route('/subtract', methods=['GET'])
def add_route():
    # Get the values of 'num1' and 'num2' query parameters from the request URL, defaulting to 0 if not provided
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    # Call the subtract function with the provided numbers
    result = subtract(num1, num2)
    # Return a JSON response with the result of the subtraction operation
    return jsonify({'result': result})
