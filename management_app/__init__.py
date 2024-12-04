from flask import Flask
from management_app.config.db import init_db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super duper secret key'

    init_db(app)

    from management_app.controllers.user import user_bp
    app.register_blueprint(user_bp)

    from management_app.controllers.routes import bp
    app.register_blueprint(bp)

    return app