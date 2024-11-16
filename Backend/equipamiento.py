from conexion import conectarse

def obtener_equipamientos(id_actividad):
    cnx, cursor = conectarse('alumno')
    cursor.execute("SELECT id, descripcion, costo FROM equipamiento WHERE id_actividad = %s", id_actividad)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result