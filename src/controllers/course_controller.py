# Se debe definir las funciones crear usuario y mostrar usuario aca
from src.models.course_model import  contar_cursos ,contar_total_cursos, contar_cursos_sedes, contar_cursos_facultades

def count_cursos(year = 2023):
    cantidad_cursos = contar_cursos(year)
    return cantidad_cursos

def count_total_cursos():
    total_cursos = contar_total_cursos()
    return total_cursos

def count_sedes(year = 2023):
    cursos_sedes = contar_cursos_sedes(year)
    return cursos_sedes

def count_facultades(year = 2023):
    cursos_facultades = contar_cursos_facultades(year)
    return cursos_facultades