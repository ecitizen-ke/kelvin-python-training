# Import flask modules
from flask import Flask, request, jsonify


# Create a Flask application instance
app = Flask(__name__)

# Load settings from settings.py file
app.config.from_pyfile('settings.py')

# Define routes and other application logic


@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 + num2
    return jsonify({'result': result})


# Start the Flask application
if __name__ == "__main__":
    app.run()
