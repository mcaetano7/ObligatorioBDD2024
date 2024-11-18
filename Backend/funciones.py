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
        fecha_nac = input("Ingrese su fecha de nacimiento en formato DD/MM/AAAA: ")
        try:
            fecha_valida = datetime.strptime(fecha_nac, "%d/%m/%Y")
            fecha_formateada = fecha_valida.strftime("%Y-%m-%d")
            return fecha_formateada
        except ValueError:
            print("Formato inválido. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")

def mostrar_reportes():
    pass
