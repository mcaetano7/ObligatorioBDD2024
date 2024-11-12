from conexion import conectarse

def encontrar_rol(correo):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("SELECT descripcion FROM rol JOIN login ON id_rol = id "
                           "WHERE correo = %s", correo)
            return cursor.fetchone()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()
