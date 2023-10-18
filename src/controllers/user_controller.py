from models.repository.user import UserRepository
from models.entities.user import UserEntity

from flask_api import status
from flask import request
from app import db


class UserController:

    def find_user():
        try:
            return UserRepository.get_all()
        
        except Exception as erro:
            return f"Erro interno: {erro}", status.HTTP_500_INTERNAL_SERVER_ERROR
        
    def find_user_by_id(id):
        try:
            return UserRepository.get_by_id(id)
        
        except Exception as erro:
            return f"Erro interno: {erro}", status.HTTP_500_INTERNAL_SERVER_ERROR
        
    def save():
        try:
            body = request.get_json()
            user = UserEntity(
                nome = body["nome"],
                idade = body["idade"],
                aceita_termos = 0
            )
            db.session.commit()
            return UserRepository.save(user)
        
        except Exception as erro:
            return f"Erro interno: {erro}", status.HTTP_500_INTERNAL_SERVER_ERROR