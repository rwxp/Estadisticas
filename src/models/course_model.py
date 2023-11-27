import psycopg2

def conectar():
    connection = psycopg2.connect(
    host="localhost",
    database="etl_estadisticas",
    user="postgres",
    password="postgres")
    return connection


def traer_cursos(year, sede):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM dim_cursos_activos WHERE year  LIMIT 100" )
    resultados = cursor.fetchall()
    cursor.close()
    return resultadoi
def contar_cursos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM dim_cursos_activos" )
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

