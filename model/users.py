from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email
        
    def __repr__(self):
        return f'<User {self.name}>'
            
    