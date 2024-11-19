import time
from tabulate import tabulate
from clase import alta_clase, mostrar_clases_instructor
from login import baja_login
from instructor import baja_instructor, info_instructor


def menu_instructor(correo):
    while True:
        time.sleep(0.8)
        menu_opciones = [
            ["1", "Información personal"],
            ["2", "Eleccíón de clase"],
            ["3", "Ver mis clases"],
            ["4", "Ver reportes"],
            ["5", "Eliminar usuario"],
            ["6", "Cerrar sesión"]
        ]
        print("\n       MENÚ INSTRUCTOR ")
        print(tabulate(menu_opciones, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
        opcion = input("\nIngrese una opción: ")
        if opcion == "1":
            info_instructor(correo)
        elif opcion == "2":
            alta_clase(correo)
        elif opcion == "3":
            mostrar_clases_instructor(correo)
        elif opcion == "4":
            pass
        elif opcion == "5":
            if input("\nPresione 1 para confirmar, otra tecla para volver: ") == '1':
                baja_instructor(correo)
                baja_login(correo)
            break
        elif opcion == "6":
            print("\nSesión cerrada.")
            break
        else:
            print("\nOpción inválida.")


