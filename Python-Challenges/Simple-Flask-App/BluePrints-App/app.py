from flask import Flask
from App_Files.Index.routes import index_bp
from App_Files.Products.routes import products_bp
from App_Files.Users.routes import users_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(index_bp)
app.register_blueprint(products_bp)
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run()
