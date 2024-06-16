from flask import Flask
from Users.routes import view_users
from Products.routes import view_products
from index.routes import home_page

app = Flask(__name__)

# Register routes
view_users(app)
view_products(app)
home_page(app)


if __name__ == '__main__':
    app.run(debug=True)
