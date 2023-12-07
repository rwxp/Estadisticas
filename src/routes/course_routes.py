from flask import Blueprint, jsonify
from src.controllers.course_controller import count_cursos, count_total_cursos, count_sedes, count_facultades
import json 
import plotly
import plotly_express as px 

course_blueprint = Blueprint('course_blueprint', __name__)

@course_blueprint.route('/contar_cursos/<int:year>', methods=['GET'])
def cursos_year(year):
    cantidad_cursos = count_cursos(year)
    return jsonify({'cantidad_de_cursos': cantidad_cursos})

@course_blueprint.route('/contar_cursos', methods=['GET'])
def cursos():
    total_cursos = count_total_cursos()
    return jsonify({'total_cursos': total_cursos})

@course_blueprint.route('/conteo_sedes/<int:year>', methods=['GET'])
def cursos_sedes(year):
    conteo_sedes = count_sedes(year)
    return jsonify({'conteo_sedes': conteo_sedes})

@course_blueprint.route('/conteo_facultades/<int:year>', methods=['GET'])
def cursos_facultades(year):
    conteo_facultades = count_facultades(year)
    return jsonify({'conteo_facultades': conteo_facultades})

@course_blueprint.route('/grafico_sedes/<int:year>', methods=['GET'])
def generar_grafico_sedes(year):
    conteo_sedes = count_sedes(year)
    x_values = [result[0] for result in conteo_sedes]
    y_values = [result[1] for result in conteo_sedes]
    fig = px.bar(conteo_sedes, x= x_values, y=y_values, title=f"Cursos por sede, Universidad del Valle, año {year}")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

@course_blueprint.route('/grafico_facultades/<int:year>', methods=['GET'])
def generar_grafico_facultades(year):
    conteo_facultades = count_facultades()
    x_values = [result[0] for result in conteo_facultades]
    y_values = [result[1] for result in conteo_facultades]
    fig = px.bar(conteo_facultades, x= x_values, y=y_values, title=f"Cursos por facultad, Universidad del Valle, año {year}")
    fig2_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig2_json