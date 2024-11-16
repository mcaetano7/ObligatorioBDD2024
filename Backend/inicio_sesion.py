from login import *
import time
from instructor import alta_instructor, select_instructor
from alumnos import alta_alumno, select_alumno


def inicio_sesion():
    while True:
        time.sleep(0.8)
        print("\n<< BIENVENIDO >>")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("\nElige una opción: ")
        if opcion == '1':
            correo = input("\nCorreo: ")
            contraseña = input("Contraseña: ")
            if validar_credenciales(correo, contraseña):
                print("\nSesión iniciada con exito")
                return correo
            else:
                print("El correo electrónico o la contraseña son incorrectos.")
        elif opcion == '2':
            correo = input("\nCorreo: ")
            if usuario_existente(correo):
                print("Ya existe un usuario con ese correo, pruebe iniciar sesión.")
                correo = None
            if correo is not None:
                contraseña = input("Contraseña: ")
                while len(contraseña) < 4:
                    print("La contraseña debe contener al menos 4 caracteres.")
                    contraseña = input("Contraseña: ")
                confirmpass = input("Vuelva a ingresar la contraseña: ")
                while contraseña != confirmpass:
                    print("Las contraseñas no coinciden")
                    contraseña = input("Contraseña: ")
                    while len(contraseña) < 4:
                        print("La contraseña debe contener al menos 4 caracteres.")
                        contraseña = input("Contraseña: ")
                    confirmpass = input("Vuelva a ingresar la contraseña: ")
                rol = 0
                while rol < 1 or rol > 3:
                    rol = int(input("\n1. Administrador\n2. Instructor\n3. Alumno\nTú que eres: "))
                if rol == 1:
                    print("\nTe enviaremos un mail para corroborar que efectivamente eres un instructor."
                          "\nUna vez valides tu identidad te pediremos tus datos para ingresarte en el sistema.\n")
                    time.sleep(5)
                    insert_login(correo, contraseña, 1)
                    if usuario_existente(correo):
                        print("Te has registrado con exito.")
                        print("Inicie sesión por favor.")
                    else:
                        print("No has sido registrado coreectamente, vuelve a intentarlo.")
                        baja_login(correo)
                elif rol == 2:
                    print("Te enviaremos un mail para corroborar que efectivamente eres un instructor."                          "\nUna vez valides tu identidad te pediremos tus datos para ingresarte en el sistema.")
                    time.sleep(4)
                    insert_login(correo, contraseña, 2)
                    alta_instructor(correo)
                    if select_instructor(correo) is not None:
                        print("Te has registrado con exito.")
                        print("Inicie sesión por favor.")
                    else:
                        print("No has sido registrado coreectamente, vuelve a intentarlo.")
                        baja_login(correo)
                elif rol == 3:
                    insert_login(correo, contraseña, 3)
                    alta_alumno(correo)
                    if select_alumno(correo) is not None:
                        print("Inicie sesión por favor.")
                    else:
                        print("No has sido registrado coreectamente, vuelve a intentarlo.")
                        baja_login(correo)
        elif opcion == '3':
            print("chau.")
            break
        else:
            print("Opción no válida. Por favor, elige de nuevo.")


