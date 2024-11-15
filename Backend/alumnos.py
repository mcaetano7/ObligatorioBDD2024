from conexion import conectarse
from datetime import datetime

def alta_alumno(correo):
    cedula = input("Ingrese su cédula: ")
    while len(cedula) != 8:
        print("La cédula debe tener 8 números.")
        cedula = input("Ingrese su cédula: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_nac = input("Ingrese su fecha de nacimiento en formato YYYY-MM-DD: ")
    if not datetime.strptime(fecha_nac, "%Y-%m-%d"):
        print("La fecha que ingresaste no está en el formato correcto.")
        fecha_nac = input("Ingrese su fecha de nacimiento en formato YYYY-MM-DD: ")
    telefono = input("Ingrese su telefono: ")
    insert_alumno(cedula, nombre, apellido, fecha_nac, telefono, correo)

def insert_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            fecha_obj = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
            cursor.execute("INSERT INTO alumnos (ci, nombre, apellido,"
                           " fecha_nacimiento, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s)",
                           (ci, nombre, apellido, fecha_obj, telefono, correo))
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
