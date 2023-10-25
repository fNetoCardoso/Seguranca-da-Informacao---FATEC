from flask import Blueprint
from controllers.user_controller import UserController


usuario_bp = Blueprint('user_bp', __name__)
usuario_bp.route('/user', methods=["GET"])(UserController.find_user)
usuario_bp.route('/user/find-id/<id>', methods=["GET"])(UserController.find_user_by_id)
usuario_bp.route('/user/save', methods=["POST"])(UserController.save)
usuario_bp.route('/user/update/<id>', methods=["PUT"])(UserController.update)