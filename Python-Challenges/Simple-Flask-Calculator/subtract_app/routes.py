from . subtract import subtract
from . import subtract_bp
from flask import current_app as app, request, jsonify


@subtract_bp.route('/subtract', methods=['GET'])
def add_route():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = subtract(num1, num2)
    return jsonify({'result': result})
