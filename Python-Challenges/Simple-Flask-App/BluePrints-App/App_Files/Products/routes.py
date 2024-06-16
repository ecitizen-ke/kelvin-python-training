from flask import jsonify, Blueprint

products_bp = Blueprint('products', __name__)


@products_bp.route('/products')
def products():
    product = ({
        'fruits': ['mangoes', 'grapes', 'watermelon', 'apples', 'berries'],
        'beverages': ['soda', 'water', 'lemonade', 'fruit juice', 'soda water']
    })
    return jsonify(product)
