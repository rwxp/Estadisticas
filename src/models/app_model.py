from flask import render_template
from src.controllers.course_controller import count_cursos, count_total_cursos, count_sedes, count_facultades

def mostrar_landing():
    return render_template("landing.html")

def mostrar_cursos():
    cantidad_cursos =  str(count_cursos()) + " cursos creados en el 2023"
    total_cursos =  str(count_total_cursos()) + " cursos en total"
    return render_template("cursos.html", cantidad_cursos=cantidad_cursos, total_cursos=total_cursos)
