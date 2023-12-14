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
def contar_usuarios(year):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT * FROM dim_users WHERE year=%s'
    year = str(year)
    cursor.execute(consulta, ( year,) )
    resultados = cursor.fetchall()
    cursor.close()
    return len(resultados)

def contar_total_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT DISTINCT COUNT(*) FROM dim_users'
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados[0][0]


def contar_usuarios_sedes(year):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT sede, COUNT(DISTINCT (id)) FROM dim_users WHERE year=%s GROUP BY(sede)'
    year = str(year)
    cursor.execute(consulta, ( year,) )
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def contar_usuarios_facultades(year):
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT sede, COUNT(DISTINCT (id)) FROM dim_users WHERE year=%s GROUP BY(sede)'
    year = str(year)
    cursor.execute(consulta, ( year,) )
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def contar_usuarios_activos():
    conexion = conectar()
    cursor = conexion.cursor()
    consulta = 'SELECT COUNT(*) FROM dim_estudiantes_activos'
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados[0][0]