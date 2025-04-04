from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
