import time
from alumno_clase import alta_alumno_clase, mostrar_alumno_clases
from alumnos import baja_alumno, info_alumno
from login import baja_login
from tabulate import tabulate
from funciones import mostrar_reportes

def menu_alumno(correo):
    while True:
        time.sleep(0.8)
        menu_opciones = [
            ["1", "Información personal"],
            ["2", "Inscribirse"],
            ["3", "Ver mis clases"],
            ["4", "Ver reportes"],
            ["5", "Eliminar usuario"],
            ["6", "Cerrar sesión"]
        ]
        print("\n      MENÚ ALUMNO ")
        print(tabulate(menu_opciones, headers=["Opción", "Descripción"], tablefmt="fancy_grid"))
        opcion = input("\nElige una opción: ")
        if opcion == "1":
            info_alumno(correo)
        elif opcion == "2":
            alta_alumno_clase(correo)
        elif opcion == "3":
            mostrar_alumno_clases(correo)
        elif opcion == "4":
            mostrar_reportes()
        elif opcion == "5":
            if input("\nPresione 1 para confirmar, otra tecla para volver: ") == '1':
                baja_alumno(correo)
                baja_login(correo)
            break
        elif opcion == '6':
            print("\nSesión cerrada.")
            break
        else:
            print("\nOpción inválida.")




