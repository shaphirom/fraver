from utils.db import db
from datetime import datetime

class Notas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    body = db.Column(db.Text, nullable = False)
    pub_date = db.Column(db.DateTime, nullable = False, default = datetime.now)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    category = db.relationship('Category', backref = db.backref('notas'), lazy=True)

    def __repr__(self):
        return f'<Notas {self.title}>'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable = False)

    def __repr__(self):
        return f'<Category {self.name}>'

# >>> py = Category(name='Python')
# >>> Notas(title='Hello Python!', body='Python is pretty cool', category=py)
# >>> p = Post(title='Snakes', body='Ssssssss')
# >>> py.posts.append(p)
# >>> db.session.add(py)
    