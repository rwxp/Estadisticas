from flask import Blueprint
from src.controllers.usuario_controller import cantidad_usuarios, mostrar_layout

usuarios_blueprint = Blueprint('usuarios_blueprint', __name__)

# from .usuarios import mostrar_usuarios, crear_usuario



usuarios_blueprint.add_url_rule('/usuarios', 'cantidad_usuarios', cantidad_usuarios)
usuarios_blueprint.add_url_rule('/', 'mostrar_layout', mostrar_layout)
# usuarios_blueprint.add_url_rule('/usuarios/crear', 'crear_usuario', crear_usuario, methods=['POST'])
