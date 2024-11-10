from conexion import conectarse


#ABM Instructores
def alta_instructor(ci, nombre, apellido):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            cursor.execute("INSERT INTO instructor (ci, nombre, apellido) VALUES (%s, %s, %s)", (ci, nombre, apellido))
            print('Consulta ejecutada.')
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def baja_instructor(ci):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            cursor.execute("DELETE FROM instructor WHERE ci = %s", (ci,))
            print('Consulta ejecutada.')
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def modificacion_instructor(ci, nombre, apellido):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            cursor.execute("UPDATE instructor SET nombre = %s, apellido = %s WHERE ci = %s", (nombre, apellido, ci))
            print('Consulta ejecutada.')
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()