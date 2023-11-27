
from flask import Blueprint
from src.controllers.usuario_controller import  mostrar_landing, mostrar_cursos 

app_blueprint = Blueprint('app_blueprint', __name__)

# from .usuarios import mostrar_usuarios, crear_usuario

app_blueprint.add_url_rule(
     '/', 'mostrar_landing', mostrar_landing)