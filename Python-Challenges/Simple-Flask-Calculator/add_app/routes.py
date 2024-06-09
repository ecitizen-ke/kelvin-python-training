# Import necessary modules from Flask and the current application context
from flask import current_app as app, request, jsonify

# Import the Blueprint object from the __init__.py file within the same package
from . import add_bp

# Import the add function from the add module
from .add import add

# Define a route within the add_bp Blueprint for handling GET requests to the /add endpoint


@add_bp.route('/add', methods=['GET'])
def add_route():
    # Extract the 'num1' and 'num2' query parameters from the request, defaulting to 0 if not provided
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))

    # Call the add function with the extracted numbers and store the result
    result = add(num1, num2)

    # Return the result as a JSON response
    return jsonify({'result': result})
