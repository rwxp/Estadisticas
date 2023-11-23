from flask import Blueprint
from src.controllers.usuario_controller import mostrar_userinfo, mostrar_landing, mostrar_masinfo

usuarios_blueprint = Blueprint('usuarios_blueprint', __name__)

# from .usuarios import mostrar_usuarios, crear_usuario

usuarios_blueprint.add_url_rule(
     '/usuarios', 'mostrar_userinfo', mostrar_userinfo)
# usuarios_blueprint.add_url_rule(
#     '/usuarios', 'mostrar_userinfo', mostrar_userinfo)
# usuarios_blueprint.add_url_rule('/info', 'mostrar_masinfo', mostrar_masinfo)
usuarios_blueprint.add_url_rule('/', 'mostrar_landing', mostrar_landing)
# usuarios_blueprint.add_url_rule('/usuarios/crear', 'crear_usuario', crear_usuario, methods=['POST'])
