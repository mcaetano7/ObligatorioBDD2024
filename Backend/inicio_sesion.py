from tabulate import tabulate
from login import *
import time
from instructor import obtener_instructor
from alumnos import select_alumno


def inicio_sesion():
    while True:
        time.sleep(0.8)
        menu_opciones = [
            ["1", "Iniciar sesión"],
            ["2", "Registrarse"],
            ["3", "Salir"]
        ]
        print("\n       BIENVENIDO ")
        print(tabulate(menu_opciones, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
        opcion = input("\nIngrese una opción: ")
        if opcion == '1':
            correo = input("\nCorreo: ")
            contraseña = input("Contraseña: ")
            if validar_credenciales(correo, contraseña):
                print("\nSesión iniciada con éxito")
                return correo
            else:
                print("El correo electrónico o la contraseña son incorrectos.")
        elif opcion == '2':
            correo = input("\nCorreo (0 para cancelar): ")
            if correo == '0':
                print("\n Cancelando operación.")
                continue
            if usuario_existente(correo):
                print("Ya existe un usuario con ese correo, pruebe iniciar sesión.")
                correo = None
            if correo is not None:
                contraseña = input("Contraseña (0 para cancelar): ")
                if contraseña == '0':
                    print("\nCancelando operación.")
                    continue
                while len(contraseña) < 4:
                    print("\nLa contraseña debe contener al menos 4 caracteres.")
                    contraseña = input("Contraseña: ")
                confirmpass = input("Vuelva a ingresar la contraseña (0 para cancelar): ")
                if confirmpass == '0':
                    print("\nCancelando operación.")
                    continue
                while contraseña != confirmpass:
                    print("Las contraseñas no coinciden")
                    contraseña = input("Contraseña: ")
                    while len(contraseña) < 4:
                        print("La contraseña debe contener al menos 4 caracteres.")
                        contraseña = input("Contraseña: ")
                    confirmpass = input("Vuelva a ingresar la contraseña: ")
                rol = 0
                while rol < 1 or rol > 3:
                    roles = [[1, 'Administrador'], [2, 'Instructor'], [3, 'Alumno']]
                    print("\n")
                    print(tabulate(roles, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
                    rol = int(input("Tú que eres: "))
                if rol == 1:
                    print("\nTe enviaremos un mail para corroborar que efectivamente eres un administrador.\n")
                    time.sleep(5)
                    insert_login(correo, contraseña, 1)
                    if usuario_existente(correo):
                        print("\nTe has registrado con exito.\n")
                        print("\nInicie sesión por favor.")
                    else:
                        print("\nNo has sido registrado coreectamente, vuelve a intentarlo.")
                        baja_login(correo)
                elif rol == 2:
                    print("\nTe enviaremos un mail para corroborar que efectivamente eres un instructor.\n"
                          "Una vez valides tu identidad te pediremos tus datos para ingresarte en el sistema.\n")
                    time.sleep(4)
                    alta_usuario(correo, contraseña, 2)
                    if obtener_instructor(correo) is not None:
                        print("\nTe has registrado con exito.\n")
                        print("\nInicie sesión por favor.")
                    else:
                        print("\nNo has sido registrado correctamente, vuelve a intentarlo.")
                        baja_login(correo)
                elif rol == 3:
                    alta_usuario(correo, contraseña, 3)
                    if select_alumno(correo) is not None:
                        print("\nInicie sesión por favor.")
                    else:
                        print("\nNo has sido registrado coreectamente, vuelve a intentarlo.")
                        baja_login(correo)
        elif opcion == '3':
            print("\nchau.")
            return None
        else:
            print("\nOpción inválida. Por favor, elige de nuevo.")