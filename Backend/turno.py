from funciones import obtener_rol
from conexion import conectarse

def agregar_turno():
    print("Ingreso de nuevo turno")
    hora_inicio = input("Ingrese el horario de inicio en formato HH:MM: ")
    hora_fin = input("Ingrese el horario de fin en formato HH:MM: ")

    insert_turno(hora_inicio, hora_fin)
    print(f"Turno de {hora_inicio} a {hora_fin} agregado correctamente")

def eliminar_turno():
    print("Eliminación de turno")
    id_turno = input("Ingrese el id del turno a eliminar: ")

    delete_turno(id_turno)
    print(f"Turno {id_turno} eliminado correctamente")

def modificar_turno():
    print("Modificación de turno")
    id_turno = input("Ingrese el id del turno a modificar: ")
    hora_inicio = input("Ingrese el horario de inicio en formato HH:MM: ")
    hora_fin = input("Ingrese el horario de fin en formato HH:MM: ")
    update_turno(id_turno, hora_inicio, hora_fin)
    print(f"Turno {id_turno} modificado correctamente")

def insert_turno(hora_inicio, hora_fin):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("INSERT INTO turno (hora_inicio, hora_fin) "
                           "VALUES (%s, %s)", (hora_inicio, hora_fin))
            cnx.commit()
            print(f"Turno de {hora_inicio} a {hora_fin} creado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()


def delete_turno(id):
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


def update_turno(id, nueva_hora_inicio, nueva_hora_fin):
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

def obtener_turnos(correo):
    cnx, cursor = conectarse(obtener_rol(correo))
    cursor.execute("SELECT * FROM turnos")
    result = cursor.fetchall()
    return result
