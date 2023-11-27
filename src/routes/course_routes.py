from flask import Blueprint
from src.controllers.course_controller import count_cursos 

course_blueprint = Blueprint('course_blueprint', __name__)

course_blueprint.add_url_rule(
     '/contar_cursos', 'cursos_init', print(count_cursos(2016)))