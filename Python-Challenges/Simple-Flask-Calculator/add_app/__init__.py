# Import the Blueprint class from Flask
from flask import Blueprint

# Create a Blueprint named 'add_bp' for organizing routes related to addition
add_bp = Blueprint('add', __name__)
