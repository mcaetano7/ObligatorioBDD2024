from conexion import conectarse

#ABM Turnos


def insert_turno(id, hora_inicio, hora_fin):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("INSERT INTO turno (id, hora_inicio, hora_fin) "
                           "VALUES (%s, %s, %s)", (id, hora_inicio, hora_fin))
            cnx.commit()
            print(f"Turno de {hora_inicio} a {hora_fin} creado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()


def baja_turno(id):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("DELETE FROM turno WHERE id = %s", (id,))
            cnx.commit()
            print(f"Turno {id} eliminado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()


def modificacion_turno(id, nueva_hora_inicio, nueva_hora_fin):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE turno SET hora_inicio = %s, hora_fin = %s WHERE id = %s",
                           (nueva_hora_inicio, nueva_hora_fin, id))
            cnx.commit()
            print(f"Turno {id} modificado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()
