from Backend.alumnos import alta_alumno
from Backend.login import insert_login, validar_credenciales, usuario_existente
from conexion import conectarse
from instructor import alta_instructor
from getpass4 import getpass
import time


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


def inicio_sesion():
    flag = True
    while flag:
        print("\n--- Menú de Inicio de Sesión ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            correo = input("Correo: ")
            #contraseña = getpass("Contraseña: ")
            contraseña = input("Contraseña: ")
            if validar_credenciales(correo, contraseña):
                print("Sesión iniciada con exito")
                flag = False
            else:
                print("El correo electrónico o la contraseña son incorrectos.")
        elif opcion == '2':
            correo = input("Correo: ")
            if usuario_existente(correo):
                print("Ya existe un usuario con ese correo, pruebe iniciar sesión.")
                correo = None
            if correo is not None:
                contraseña = input("Contraseña: ")
                rol = ""
                while rol != 'alumno' and rol != 'instructor':
                    rol = input("Eres alumno o instructor:")
                if rol == 'alumno':
                    insert_login(correo, contraseña, 3)
                    alta_alumno(correo)
                    print("Te has registrado con exito.")
                elif rol == 'instructor':
                    print("Te enviaremos un mail para corroborar que efectivamente eres un instructor."
                          "\nUna vez valides tu identidad te pediremos tus datos para ingresarte en el sistema.")
                    time.sleep(5)
                    insert_login(correo, contraseña, 2)
                    alta_instructor(correo)
                    print("Te has registrado con exito.")

        elif opcion == '3':
            print("Saliendo del sistema. ¡Hasta luego!")
            #break
        else:
            print("Opción no válida. Por favor, elige de nuevo.")
