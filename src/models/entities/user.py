from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app import db, app
from sqlalchemy.dialects.mysql import TINYINT

from models.dtos.user import UserDTO

class Usuario(db.Model):

    __table_name__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=True)
    aceita_termos: Mapped[TINYINT] = mapped_column(TINYINT, nullable=True)

    @app.route("/", methods=["GET"])
    def user_list():
        with app.app_context():
            users = db.session.query(Usuario).order_by(Usuario.nome)
            print(users)
            return UserDTO(**users.__dict__).model_dump_json()