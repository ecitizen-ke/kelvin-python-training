# Import flask modules
from flask import Flask, request, jsonify

# Import settings from settings.py
from settings import DEBUG, HOST, PORT, ENVIRONMENT

# Create a Flask application instance
app = Flask(__name__)

# Set debug mode and additional configuration settings using app.config
app.config['DEBUG'] = DEBUG
app.config['HOST'] = HOST
app.config['PORT'] = PORT
app.config['ENV'] = ENVIRONMENT

# Define routes and other application logic


@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 + num2
    return jsonify({'result': result})


# Start the Flask application
if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'],
            debug=app.config['DEBUG'], env=app.config['ENV'])
