from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(200), unique=True, nullable=False)
    def __repr__(self):
        return f'<Usuario {self.nombre_usuario}>'
