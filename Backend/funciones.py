from conexion import conectarse
from datetime import datetime

def obtener_rol(correo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("SELECT descripcion FROM rol JOIN login ON id_rol = id "
                   "WHERE correo = %s", correo)
    result = cursor.fetchone()[0]
    cursor.close()
    cnx.close()
    return result

def obtener_fecha_nacimiento():
    while True:
        fecha_nac = input("Ingrese su fecha de nacimiento en formato YYYY-MM-DD: ")
        try:
            fecha_valida = datetime.strptime(fecha_nac, "%Y-%m-%d")
            return fecha_valida
        except ValueError:
            print("Formato inválido. Por favor, ingrese la fecha en el formato YYYY-MM-DD.")