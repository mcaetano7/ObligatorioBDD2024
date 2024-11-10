from conexion import conectarse


#Modificacion actividades
def modificacion_actividades(id, descripacion, costo):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE actividades SET descripcion = %s, costo = %s WHERE id = %s",
                           (descripacion, costo, id))
            cnx.commit()
            print(f"Actividad {id} modificada con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()
