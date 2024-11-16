from conexion import conectarse

def modificar_actividades():
    print("\nmostrar actividades:")
    id_actividad = input("Ingrese el id de la actividad a modificar: ")
    nuevo_costo = input("Ingrese el nuevo costo: ")

    update_actividades(id_actividad, nuevo_costo)
    print(f"\nActividad {id_actividad} modificada correctamente")

def update_actividades(id, costo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("UPDATE actividades SET costo = %s WHERE id = %s",
                   (costo, id))
    cnx.commit()
    print(f"Actividad {id} modificada con éxito.")
    cursor.close()
    cnx.close()
