from tabulate import tabulate
from funciones import obtener_rol
from conexion import conectarse
import time

def modificar_actividades():
    while True:
        time.sleep(0.8)
        print("\n         ACTIVIDADES")
        cnx, cursor = conectarse('administrador')
        cursor.execute("SELECT * FROM actividades")
        actividades = cursor.fetchall()
        print(tabulate(actividades, headers=["ID Actividad", "Descripción", "Costo"], tablefmt="fancy_grid"))
        id_actividad = input("ID de la actividad que deseas modificar (0 para volver): ")
        actividades_ids = [str(actividad[0]) for actividad in actividades]
        while id_actividad not in actividades_ids and id_actividad != "0":
            id_actividad = input("\nID incorrecto, por favor seleccione uno de la lista: ")
        if id_actividad == "0":
            return
        while True:
            nuevo_costo = input("\nIngrese el nuevo costo: ")
            try:
                nuevo_costo = int(nuevo_costo)
                break
            except ValueError:
                print("\nPor favor, ingrese un número válido para el costo.")  # Si hay un error, informa al usuario
        update_actividades(id_actividad, nuevo_costo)
        print(f"\nActividad {id_actividad} modificada correctamente")

def update_actividades(id, costo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("UPDATE actividades SET costo = %s WHERE id = %s",
                   (costo, id))
    cnx.commit()
    cursor.close()
    cnx.close()

def obtener_actividades(correo):
    cnx, cursor = conectarse(obtener_rol(correo))
    cursor.execute("SELECT id, descripcion FROM actividades")
    result = cursor.fetchall()
    return result
