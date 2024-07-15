# Applying specific config settings from the settings.py file onto the app.py file

from flask import Flask, request, jsonify
from settings import DATABASE_URI, DEBUG, SECRET_KEY

app = Flask(__name__)
app.config['DATABASE_URI'] = DATABASE_URI
app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 + num2
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])


# Using the app.config.from_object('settings') format to load the settings.py configurations onto the app.py on launch

'''
from flask import Flask, request, jsonify
from settings import *

app = Flask(__name__)
app.config.from_object('settings')

@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 + num2
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])

# Using the app.config.from_('settings') format to load the settings.py configurations onto the app.py on launch
 

'''
# Using the app.config.from_pyfile('settings') format to load the settings.py configurations onto the app.py on launch


'''
# Import necessary modules
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

'''

# Using the app.config.from_mapping() format to load the .env configurations onto the app.py on launch directly without a need for a settings.py file

'''
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load settings from environment variables
app.config.from_mapping(
    DEBUG=os.getenv('DEBUG') == 'True',
    DATABASE_URI=os.getenv('DATABASE_URI'),
    # Add other settings as needed
)

@app.route('/add', methods=['GET'])
def add_numbers():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = num1 + num2
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run()

'''
