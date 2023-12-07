from flask import render_template
from src.controllers.course_controller import count_cursos, count_total_cursos, count_sedes, count_facultades
import json
import plotly
import plotly_express as px

def mostrar_landing():
    return render_template("landing.html")

def mostrar_cursos():
    cantidad_cursos =  str(count_cursos()) + " cursos creados en el 2023"
    total_cursos =  str(count_total_cursos()) + " cursos en total"
    fig_json = generar_grafico_sedes()
    fig2_json = generar_grafico_facultades()
    return render_template("cursos.html", cantidad_cursos=cantidad_cursos, total_cursos=total_cursos, fig_json=fig_json, fig2_json=fig2_json)

def generar_grafico_sedes( year=2023):
    conteo_sedes = count_sedes()
    x_values = [result[0] for result in conteo_sedes]
    y_values = [result[1] for result in conteo_sedes]
    fig = px.bar(conteo_sedes, x= x_values, y=y_values, title=f"Cursos por sede, Universidad del Valle, año {year}")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def generar_grafico_facultades(year=2023):
    conteo_sedes = count_sedes()
    x_values = [result[0] for result in conteo_sedes]
    y_values = [result[1] for result in conteo_sedes]
    fig = px.bar(conteo_sedes, x= x_values, y=y_values, title=f"Cursos por facultad, Universidad del Valle, año {year}")
    fig2_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig2_json

#Usuarios

def mostrar_usuarios():
    cantidad_cursos =  str(count_cursos()) + " cursos creados en el 2023"
    total_cursos =  str(count_total_cursos()) + " cursos en total"
    fig_json = generar_grafico_sedes()
    fig2_json = generar_grafico_facultades()
    return render_template("user.html", cantidad_cursos=cantidad_cursos, total_cursos=total_cursos, fig_json=fig_json, fig2_json=fig2_json)