
from flask import Blueprint
from src.controllers.app_controller import render_landing, render_cursos

app_blueprint = Blueprint('app_blueprint', __name__)

# from .usuarios import mostrar_usuarios, crear_usuario

app_blueprint.add_url_rule(
     '/', 'render_landing', render_landing)

app_blueprint.add_url_rule(
     '/cursos', 'render_cursos', render_cursos)