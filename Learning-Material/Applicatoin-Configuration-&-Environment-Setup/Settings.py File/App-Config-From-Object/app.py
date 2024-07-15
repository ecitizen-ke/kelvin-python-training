# Import flask modules
from flask import Flask, request, jsonify

# Import settings object from settings.py
from settings import AppConfig

# Create a Flask application instance
app = Flask(__name__)

# Load settings from AppConfig object
app.config.from_object(AppConfig)

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
