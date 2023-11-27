# Se debe definir las funciones crear usuario y mostrar usuario aca
from src.models.course_model import traer_cursos
from flask import render_template

def mostrar_cursos():
    cursos = traer_cursos()
    return render_template("cursos.html")