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
    consulta = 'SELECT * FROM dim_cursos_activos WHERE year=%s'
    year = str(year)
    cursor.execute(consulta, ( year,) )
    resultados = cursor.fetchall()
    cursor.close()
    return len(resultados)

def contar_total_cursos():
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT DISTINCT COUNT(*) FROM dim_cursos_activos'
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados[0][0]


def contar_cursos_sedes(year):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT sede, COUNT(DISTINCT (id)) FROM dim_cursos_activos WHERE year=%s GROUP BY(sede)'
    year = str(year)
    cursor.execute(consulta, ( year,) )
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def contar_cursos_facultades(year):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT facultad, COUNT(DISTINCT (id)) FROM dim_cursos_activos WHERE year=%s GROUP BY(facultad)'
    year = str(year)
    cursor.execute(consulta, ( year,) )
    resultados = cursor.fetchall()
    cursor.close()
    return resultados