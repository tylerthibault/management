from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///management.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        from management_app.models.user import User
        from management_app.models.family import Family
        from management_app.models.parent import Parent
        from management_app.models.child import Child
        from management_app.models.login_record import LoginRecord
        
        db.create_all()
