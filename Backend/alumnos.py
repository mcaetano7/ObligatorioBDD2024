from conexion import conectarse

def alta_alumno(correo):
    insert_alumno(input("Ingrese su cédula: "),
                  input("Ingrese su nombre: "),
                  input("Ingrese su apellido: "),
                  input("Ingrese su fecha de nacimiento: "),
                  input("Ingrese su telefono: "),
                  correo)

def insert_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("INSERT INTO alumno (ci, nombre, apellido, fecha_nacimiento, telefono, correo) VALUES (%s, %s, %s, %s, %s, %S)",
                           (ci, nombre, apellido, fecha_nacimiento, telefono, correo))
            cnx.commit()
            print(f"Alumno {nombre} {apellido} agregado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()


def baja_alumno(ci):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("DELETE FROM alumno WHERE ci = %s", (ci,))
            cnx.commit()
            print(f"Alumno {ci} eliminado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()


def modificacion_alumno(ci, nombre, apellido, fecha_nacimiento):
    cnx, cursor = conectarse('alumno')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE alumno SET nombre = %s, apellido = %s, fecha_nacimiento = %s WHERE ci = %s",
                           (nombre, apellido, fecha_nacimiento, ci))
            cnx.commit()
            print(f"Alumno {ci} modificado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()
