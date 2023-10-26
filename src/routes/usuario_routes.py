from flask import Blueprint
from src.controllers.usuario_controller import mostrar_userinfo, mostrar_layout, mostrar_masinfo

usuarios_blueprint = Blueprint('usuarios_blueprint', __name__)

# from .usuarios import mostrar_usuarios, crear_usuario

usuarios_blueprint.add_url_rule(
    '/usuarios', 'mostrar_user-info', mostrar_userinfo)
usuarios_blueprint.add_url_rule('/info', 'mostrar_masinfo', mostrar_masinfo)
usuarios_blueprint.add_url_rule('/', 'mostrar_layout', mostrar_layout)
# usuarios_blueprint.add_url_rule('/usuarios/crear', 'crear_usuario', crear_usuario, methods=['POST'])
