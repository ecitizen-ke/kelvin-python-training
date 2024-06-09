# Importing Blueprint from Flask
from flask import Blueprint

# Creating a Blueprint object named 'divide_bp'
# The first argument is the name of the blueprint, and the second argument is __name__,
# which is a special Python variable that holds the name of the current Python module.
divide_bp = Blueprint('divide_bp', __name__)
