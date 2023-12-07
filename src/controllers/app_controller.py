from src.models.app_model import mostrar_landing, mostrar_cursos, mostrar_usuarios
from flask import render_template


def render_landing():
    return mostrar_landing()

def render_cursos():
    return mostrar_cursos()

def render_usuarios():
    return mostrar_usuarios()