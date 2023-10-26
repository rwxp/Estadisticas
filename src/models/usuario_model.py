from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    city = db.Column(db.String(200), unique=False, nullable=False)
    def __repr__(self):
        return f'<Usuario {self.username}>'
