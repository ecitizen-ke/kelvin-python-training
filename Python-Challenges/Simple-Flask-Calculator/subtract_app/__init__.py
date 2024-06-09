# Import the Blueprint class from Flask
from flask import Blueprint
# Create a Blueprint named 'subtract_bp' with the current package as its module name
subtract_bp = Blueprint('subtract_bp', __name__)
