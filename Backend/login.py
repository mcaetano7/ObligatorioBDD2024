from funciones import obtener_fecha_nacimiento
from conexion import conectarse
from hash import *


def insert_login(correo, contraseña, id_rol):
    cnx, cursor = conectarse('administrador')
    hashed_password = hash_password(contraseña)
    cursor.execute("INSERT INTO login (correo, contraseña, id_rol) VALUES (%s, %s, %s)",
                    (correo, hashed_password, id_rol))
    cnx.close()
    cursor.close()

def alta_usuario(correo, contraseña,id_rol):
    cnx, cursor = conectarse('administrador')
    cnx.begin()
    hashed_password = hash_password(contraseña)
    cursor.execute("INSERT INTO login (correo, contraseña, id_rol) VALUES (%s, %s, %s)",
                   (correo, hashed_password, id_rol))
    if id_rol == 3:
        cedula = input("\nIngrese su cédula: ")
        while len(cedula) != 8:
            print("La cédula debe tener 8 números.")
            cedula = int(input("Ingrese su cédula: "))
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        fecha_nacimiento = obtener_fecha_nacimiento()
        telefono = input("Ingrese su telefono: ")
        try:
            cursor.execute("INSERT INTO alumnos (ci, nombre, apellido,"
                           " fecha_nacimiento, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s)",
                           (cedula, nombre, apellido, fecha_nacimiento, telefono, correo))
            cnx.commit()
            print(f"\nAlumno {nombre} {apellido} registrado con éxito.")
        except:
            print("\nYa existe un alumno con esa cédula.")
            cnx.rollback()
            return
        finally:
            cursor.close()
            cnx.close()
    else:
        ci = input("\nIngrese su cédula: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        try:
            cursor.execute("INSERT INTO instructores (ci, nombre, apellido, correo) VALUES (%s, %s, %s, %s)",
                           (ci, nombre, apellido, correo))
            cnx.commit()
            print(f"\nInstructor {nombre} {apellido} registrado con éxito.")
        except:
            print("\nYa existe un instructor con esa cédula.")
            cnx.rollback()
            return
        finally:
            cursor.close()
            cnx.close()

def baja_login(correo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("DELETE FROM login WHERE correo = %s", correo)
    cnx.commit()
    cursor.close()
    cnx.close()


def validar_credenciales(correo, contraseña) -> bool:
    cnx, cursor = conectarse('administrador')
    cursor.execute("SELECT contraseña FROM login WHERE correo = %s", correo)
    result = cursor.fetchone()
    if result is None:
        return False
    hashed_password = result[0].encode('utf-8')
    cursor.close()
    cnx.close()
    if check_password(contraseña, hashed_password):
        return True
    else:
        return False

def usuario_existente(correo) -> bool:
    cnx, cursor = conectarse('administrador')
    cursor.execute("SELECT correo FROM login WHERE correo = %s", (correo,))
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    if result is not None:
        return True
    return False


