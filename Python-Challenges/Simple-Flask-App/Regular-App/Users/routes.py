from flask import jsonify


def view_users(myapp):
    @myapp.route('/users')
    def users():
        credentials = ([
            {'username': 'kelvin', 'password': 'oneup100!'},
            {'username': 'jayden', 'password': 'awesome!!!'}
        ])
        return jsonify(credentials)
