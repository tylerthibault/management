from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///management.db'
    app.config['SECRET_KEY'] = 'dev'  # Change this in production
    db.init_app(app)

    with app.app_context():
        # from .models.user import User
        from .models.org import Org
        from .models.user import User
        db.create_all()

        from .controllers.routes import routes
        app.register_blueprint(routes)

        from .controllers.users import users
        app.register_blueprint(users)

        from .controllers.orgs import orgs
        app.register_blueprint(orgs)

    return app

