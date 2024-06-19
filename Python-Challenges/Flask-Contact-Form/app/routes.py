from flask import Blueprint, render_template, current_app
from app.objects import LoginForm

# Create a Blueprint named 'routes_bp' for routes
routes_bp = Blueprint('routes', __name__)

# Define a route for '/'


@routes_bp.route('/', methods=['GET', 'POST'])
def index():
    # Create an instance of LoginForm
    form = LoginForm()

    # Check if the form is submitted and valid
    if form.validate_on_submit():
        return 'Form Successfully Submitted'  # Return a success message

    # Render the 'index.html' template with the form
    return render_template('index.html', form=form)
