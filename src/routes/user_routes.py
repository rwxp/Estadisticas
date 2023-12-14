from flask import Blueprint, jsonify
from src.controllers.user_controller import count_usuarios, count_total_usuarios, count_sedes, count_facultades, count_usuarios_activos
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

@user_blueprint.route('/contar_usuarios_activos', methods=['GET'])
def usuarios_activos():
    total_usuarios_activos = count_usuarios_activos()
    return jsonify({'total_usuarios_activos': total_usuarios_activos})


@user_blueprint.route('/conteo_usuarios_sedes/<int:year>', methods=['GET'])
def generar_grafico_usuarios_sedes(year):
    conteo_sedes = count_sedes(year)
    x_values = []
    y_values = []
    for sede in conteo_sedes:
        x_values.append(sede[0])
        y_values.append(sede[1])
    return jsonify({'x_values': x_values, 'y_values': y_values})

@user_blueprint.route('/conteo_usuarios_facultades/<int:year>', methods=['GET'])
def generar_grafico_usuarios_facultades(year):
    conteo_facultades = count_facultades()
    x_values = []
    y_values = []
    for facultad in conteo_facultades:
        x_values.append(facultad[0])
        y_values.append(facultad[1])
    return jsonify({'x_values': x_values, 'y_values': y_values})