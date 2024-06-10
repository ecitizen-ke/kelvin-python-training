from flask import jsonify


def view_products(myApp):
    @myApp.route('/products')
    def products():
        product = ({
            'fruits': ['mangoes', 'grapes', 'watermellon', 'apples', 'berries'],
            'beverages': ['soda', 'water', 'lemonade', 'fruit juice', 'soda water']
        })
        return jsonify(product)
