from conexion import conectarse

def alta_instructor(correo):
    insert_instructor(input("Ingrese su cédula: "),
                      input("Ingrese su nombre: "),
                      input("Ingrese su apellido: "),
                      correo)

def insert_instructor(ci, nombre, apellido, correo):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("INSERT INTO instructores (ci, nombre, apellido, correo) VALUES (%s, %s, %s, %s)", (ci, nombre, apellido, correo))
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def baja_instructor(ci):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("DELETE FROM instructores WHERE ci = %s", ci)
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def modificacion_instructor(ci, nombre, apellido):
    cnx, cursor = conectarse('instructor')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE instructores SET nombre = %s, apellido = %s WHERE ci = %s", (nombre, apellido, ci))
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()