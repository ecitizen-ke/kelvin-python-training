# Import necessary modules from Flask
from flask import Flask, jsonify, request, render_template

# Initialize a Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def index():
    # Return a simple string as a response
    return "Hello World!!"

# Define a route for the "/about" URL
@app.route('/about')
def aboutUs():
    # Return a simple string as a response for the About Us page
    return "This is an About Us Page"

# Define a dynamic route that takes a username as a parameter
@app.route('/user/<username>')
def userProfile(username):
    # Render an HTML template called 'userprofile.html' and pass the username variable to it
    return render_template('userprofile.html', username=username)

# Run the application
if __name__ == '__main__':
    # Start the Flask development server in debug mode
    app.run(debug=True)
