from models.entities.user import UserEntity
from models.dtos.user import UserDTO
from app import db

class UserRepository:
    
    @staticmethod
    def get_all():
        query = UserEntity.query.all()
        return  [UserDTO(**users.__dict__).dict() for users in query]
    
    @staticmethod
    def get_by_id(id):
        query = UserEntity.query.get(id)
        return UserDTO(**query.__dict__).dict() if query else f"Não foram encontrados dados com este ID: {id}"
    

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.flush()
        db.session.refresh(user)
        return user.id