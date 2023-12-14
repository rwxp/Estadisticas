# Se debe definir las funciones crear usuario y mostrar usuario aca
from src.models.user_model import  contar_usuarios ,contar_total_usuarios, contar_usuarios_sedes, contar_usuarios_activos

def count_usuarios(year = 2023):
    cantidad_usuarios = contar_usuarios(year)
    return cantidad_usuarios

def count_total_usuarios():
    total_usuarios = contar_total_usuarios()
    return total_usuarios

def count_sedes(year = 2023):
    usuarios_sedes = contar_usuarios_sedes(year)
    return usuarios_sedes

def count_facultades(year = 2023):
    usuarios_facultades = contar_usuarios_sedes(year)
    return usuarios_facultades

def count_usuarios_activos():
    usuarios_activos = contar_usuarios_activos()
    return usuarios_activos