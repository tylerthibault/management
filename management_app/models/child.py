from management_app.config.db import db

class Child(db.Model):
    __tablename__ = 'children'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    pin = db.Column(db.String(10))
    
    # Foreign Keys
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, data:dict):
        self.username = data['username']
        self.pin = data['pin']
        self.users_id = data['users_id']

    @classmethod
    def create(cls, data:dict):
        child = cls({
            'username': data['username'],
            'pin': data['pin'],
            'users_id': data['users_id']
        })
        db.session.add(child)
        db.session.commit()
        return child