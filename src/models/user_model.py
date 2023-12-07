import psycopg2

def conectar():
    connection = psycopg2.connect(
    host="localhost",
    database="etl_estadisticas",
    user="postgres",
    password="postgres")
    return connection


def traer_usuarios(year, sede):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM dim_user WHERE year  LIMIT 100" )
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def contar_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM dim_estudiantes_activos" )
    resultados = cursor.fetchall()
    cursor.close()
    return resultados