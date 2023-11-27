from flask import Blueprint
from src.controllers.usuario_controller import  mostrar_landing, mostrar_cursos 

course_blueprint = Blueprint('course_blueprint', __name__)

# from .usuarios import mostrar_usuarios, crear_usuario

course_blueprint.add_url_rule(
     '/cursos', 'mostrar_cursos', mostrar_cursos)