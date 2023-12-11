from flask import Blueprint, jsonify
from src.controllers.user_controller import count_usuarios, count_total_usuarios, count_sedes, count_facultades
import json
import plotly
import plotly_express as px

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/contar_usuarios/<int:year>', methods=['GET'])
def usuarios_year(year):
    cantidad_usuarios = count_usuarios(year)
    return jsonify({'cantidad_de_usuarios': cantidad_usuarios})

@user_blueprint.route('/contar_usuarios', methods=['GET'])
def usuarios():
    total_usuarios = count_total_usuarios()
    return jsonify({'total_usuarios': total_usuarios})

@user_blueprint.route('/conteo_usuarios_sedes/<int:year>', methods=['GET'])
def usuarios_sedes(year):
    conteo_sedes = count_sedes(year)
    return jsonify({'usuarios_sedes': conteo_sedes})

@user_blueprint.route('/conteo_usuarios_facultades/<int:year>', methods=['GET'])
def usuarios_facultades(year):
    conteo_facultades = count_facultades(year)
    return jsonify({'conteo_facultades': conteo_facultades})

@user_blueprint.route('/grafico_usuarios_sedes/<int:year>', methods=['GET'])
def generar_grafico_usuarios_sedes(year):
    conteo_sedes = count_sedes(year)
    x_values = [result[0] for result in conteo_sedes]
    y_values = [result[1] for result in conteo_sedes]
    fig = px.bar(conteo_sedes, x= x_values, y=y_values, title=f"Usuarios por sede, Universidad del Valle, año {year}")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

@user_blueprint.route('/grafico_usuarios_facultades/<int:year>', methods=['GET'])
def generar_grafico_usuarios_facultades(year):
    conteo_facultades = count_facultades()
    x_values = [result[0] for result in conteo_facultades]
    y_values = [result[1] for result in conteo_facultades]
    fig = px.bar(conteo_facultades, x= x_values, y=y_values, title=f"Usuarios por facultad, Universidad del Valle, año {year}")
    fig2_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig2_json