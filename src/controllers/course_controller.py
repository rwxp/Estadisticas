# Se debe definir las funciones crear usuario y mostrar usuario aca
from src.models.course_model import  contar_cursos 

def count_cursos(year):
    cantidad_cursos = contar_cursos(year)
    return cantidad_cursos

# def cantidad_cursos(year):
#     cantidad = contar_cursos(year)
#     print(f"La cantidad de cursos encontrados es: {cantidad}")