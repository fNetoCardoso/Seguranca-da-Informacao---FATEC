from models.entities.user import UserEntity
from models.dtos.user import UserDTO
from app import app

class UserRepository:
    
    @app.route("/", methods=["GET"])
    def get_all():
        query = UserEntity.query.all()
        return  [UserDTO(**users.__dict__).dict() for users in query]