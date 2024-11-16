from funciones import obtener_rol
from conexion import conectarse

def select_clase(id, correo):
    if obtener_rol(correo) == 'alumno':
        cnx, cursor = conectarse('alumno')
    elif obtener_rol(correo) == 'instructor':
        cnx, cursor = conectarse('instructor')
    cursor.execute("SELECT * FROM clase WHERE id = %s", id)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result
