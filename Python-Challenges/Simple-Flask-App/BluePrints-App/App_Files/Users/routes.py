from flask import jsonify, Blueprint

users_bp = Blueprint('users', __name__)


@users_bp.route('/users')
def users():
    credentials = ([
        {'username': 'kelvin', 'password': 'oneup100!'},
        {'username': 'jayden', 'password': 'awesome!!!'}
    ])
    return jsonify(credentials)
