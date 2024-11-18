from turno import *
from instructor import *
from actividades import modificar_actividades


def menu_admin():
    while True:
        print("\nMenu de administrador: ")
        print("1. ABM instructores")
        print("2. ABM turnos")
        print("3. Modificacion de actividades")
        print("4. Cerrar sesión")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            menu_admin_instructores()
        elif opcion == "2":
            menu_admin_turnos()
        elif opcion == "3":
            modificar_actividades()
        elif opcion == "4":
            print("\nSaliendo del menu de administrador")
            break
        else:
            print("Opcion incorrecta")


def menu_admin_turnos():
    while True:
        print("Estas son tus opciones: \n")
        print("1. Agregar un turno")
        print("2. Eliminar un turno")
        print("3. Modificar un turno")
        print("4. Volver al menu principal")
        opcion = input("Elige una opción:")
        if opcion == '1':
            agregar_turno()
        elif opcion == '2':
            eliminar_turno()
        elif opcion == '3':
            modificar_turno()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")

def agregar_turno():
    print("\nIngreso de nuevo turno")
    hora_inicio = input("Ingrese el horario de inicio en formato HH:MM: ")
    hora_fin = input("Ingrese el horario de fin en formato HH:MM: ")

    insert_turno(hora_inicio, hora_fin)
    print(f"Turno de {hora_inicio} a {hora_fin} agregado correctamente")


def eliminar_turno():
    print("\nEliminación de turno")
    id_turno = input("Ingrese el id del turno a eliminar: ")

    eliminar_turno(id_turno)
    print(f"Turno {id_turno} eliminado correctamente")


def modificar_turno():
    print("\nModificación de turno")
    id_turno = input("Ingrese el id del turno a modificar: ")
    hora_inicio = input("Ingrese el horario de inicio en formato HH:MM: ")
    hora_fin = input("Ingrese el horario de fin en formato HH:MM: ")

    modificar_turno(id_turno, hora_inicio, hora_fin)
    print(f"Turno {id_turno} modificado correctamente")


def menu_admin_instructores():
    while True:
        print("\nEstas son tus opciones: ")
        print("1. Agregar un instructor")
        print("2. Eliminar un instructor")
        print("3. Modificar un instructor")
        print("4. Volver al menu principal")
        opcion = input("Elige una opción:")

        if opcion == '1':
            agregar_instructor()
        elif opcion == '2':
            eliminar_instructor()
        elif opcion == '3':
            modificacion_instructor()
        elif opcion == '4':
            break
        else:
            print("Opción no válida")





def eliminar_instructor():
    print("\nEliminación de instructor")
    ci_instructor = input("Ingrese la cédula del instructor: ")

    baja_instructor(ci_instructor)
    print(f"Instructor con cédula {ci_instructor} eliminado correctamente")


def modificar_instructor():
    print("Modificación de instructor")
    ci_instructor = input("Ingrese la cedula del instructor: ")
    nuevo_nombre = input("Ingrese el nombre del instructor: ")
    nuevo_apellido = input("Ingrese el apellido del instructor: ")
    nueva_fecha_nacimiento = input("Ingrese la fecha de nacimiento del instructor en formato YYYY-MM-DD: ")

    modificar_instructor(ci_instructor, nuevo_nombre, nuevo_apellido, nueva_fecha_nacimiento)
    print(f"Datos del instructor con cédula {ci_instructor} modificados correctamente")



