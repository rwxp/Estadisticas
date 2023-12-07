from flask import render_template
from src.controllers.course_controller import count_cursos, count_total_cursos, count_sedes, count_facultades
from src.routes.course_routes import generar_grafico_sedes, generar_grafico_facultades

def mostrar_landing():
    return render_template("landing.html")

def mostrar_cursos():
    cantidad_cursos =  str(count_cursos()) + " cursos creados en el 2023"
    total_cursos =  str(count_total_cursos()) + " cursos en total"
    fig_json = generar_grafico_sedes(2023)
    fig2_json = generar_grafico_facultades(2023)
    return render_template("cursos.html", cantidad_cursos=cantidad_cursos, total_cursos=total_cursos, fig_json=fig_json, fig2_json=fig2_json)
