import psycopg2
from flask import render_template

def conectar():
    connection = psycopg2.connect(
    host="localhost",
    database="etl_estadisticas",
    user="postgres",
    password="postgres")
    return connection

# Se encarga de contar tods los cursos activos de un anhio particular.
def contar_cursos(year):
    conexion = conectar()
    cursor = conexion.cursor()
    # consulta = "SELECT DISTINCT COUNT(*) FROM dim_cursos_activos WHERE Year = %s"
    consulta = "SELECT * FROM dim_cursos_activos"
    cursor.execute(consulta, ( str(year), )) 
    resultados = cursor.fetchall()
    cursor.close()
    return len(resultados)

# Se encarga de traer todos los cursos activos teniendo en cuenta el year y una sede.
# def traer_cursos(year, sede):
#     conexion = conectar()
#     cursor = conexion.cursor()
#     consulta = "SELECT * FROM dim_cursos_activos WHERE year=%s AND sede=%s"
#     cursor.execute(consulta, ( year, sede))
#     resultados = cursor.fetchall()
#     cursor.close()
#     return resultado