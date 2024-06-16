from flask import jsonify, Blueprint

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def landing_page():
    return '<h1>This is a Simple Flask App</h1>'
