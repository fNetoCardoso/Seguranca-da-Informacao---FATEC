from app import db

class UserEntity(db.Model):

    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    idade = db.Column(db.Integer, nullable=True)
    aceita_termos = db.Column(db.Boolean, nullable=True)

    