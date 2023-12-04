from flask import Blueprint, jsonify
from src.controllers.course_controller import count_cursos, count_total_cursos, count_sedes, count_facultades

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