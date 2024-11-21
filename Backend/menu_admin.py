import time
from tabulate import tabulate
from funciones import mostrar_reportes
from turno import agregar_turno, eliminar_turno, modificar_turno
from actividades import modificar_actividades
from clase import modificar_clase


def menu_admin():
    while True:
        time.sleep(0.8)
        menu_opciones = [
            ["1", "ABM Turnos"],
            ["2", "Modificar actividades"],
            ["3", "Modificar clases"],
            ["4", "Ver reportes"],
            ["5", "Cerrar Sesión"]
        ]
        print("\n      MENÚ DE ADMINISTRADOR")
        print(tabulate(menu_opciones, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
        opcion = input("\nIngrese una opción: ")
        if opcion == "1":
            menu_admin_turnos()
        elif opcion == "2":
            modificar_actividades()
        elif opcion == "3":
            modificar_clase()
        elif opcion == "4":
            mostrar_reportes()
        elif opcion == "5":
            print("\nCerrando sesión")
            break
        else:
            print("\nOpción incorrecta")


def menu_admin_turnos():
    while True:
        time.sleep(0.8)
        opciones = [
            ["1", "Agregar un turno"],
            ["2", "Eliminar un turno"],
            ["3", "Modificar un turno"],
            ["4", "Volver al menu principal"]
        ]
        print("\n           ABM TURNOS")
        print(tabulate(opciones, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
        opcion = input("Elige una opción: ")
        if opcion == '1':
            agregar_turno()
        elif opcion == '2':
            eliminar_turno()
        elif opcion == '3':
            modificar_turno()
        elif opcion == '4':
            print("\nVolviendo al menu de administrador")
            break
        else:
            print("\nOpción no válida")