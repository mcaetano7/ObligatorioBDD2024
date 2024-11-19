import time
from datetime import datetime, timedelta
from funciones import obtener_rol, validar_hora, coincidencia_turno
from conexion import conectarse
from tabulate import tabulate

def agregar_turno():
    while True:
        time.sleep(0.8)
        cnx, cursor = conectarse('administrador')
        cursor.execute("SELECT * FROM turnos")
        turnos = cursor.fetchall()
        print("\n              TURNOS")
        print(tabulate(turnos, headers=["ID Turno", "Hora inicio", "Hora fin"], tablefmt="fancy_grid"))
        while True:
            hora_inicio = input("\nIngrese el horario de inicio en formato HH:MM (0 para volver): ")
            if hora_inicio == "0":
                return
            if validar_hora(hora_inicio):
                break
            else:
                print("\nFormato incorrecto. Por favor, ingrese un horario válido (HH:MM).")
        while True:
            hora_fin = input("\nIngrese el horario de fin en formato HH:MM (0 para volver): ")
            if hora_fin == "0":
                return
            if validar_hora(hora_fin):
                break
            else:
                print("\nFormato incorrecto. Por favor, ingrese un horario válido (HH:MM).")
        hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M')
        hora_fin_dt = datetime.strptime(hora_fin, '%H:%M')
        if hora_fin_dt - hora_inicio_dt != timedelta(hours=2):
            print("\nLa diferencia entre la hora de inicio y fin debe ser de 2 horas.\n")
            continue
        if coincidencia_turno(turnos, hora_inicio_dt, hora_fin_dt):
            print("\nEl turno ingresado coincide con un turno existente.")
            continue
        insert_turno(hora_inicio, hora_fin)
        print(f"\nTurno de {hora_inicio} a {hora_fin} agregado correctamente")

def insert_turno(hora_inicio, hora_fin):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("INSERT INTO turnos (hora_inicio, hora_fin) "
                           "VALUES (%s, %s)", (hora_inicio, hora_fin))
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def eliminar_turno():
    while True:
        time.sleep(0.8)
        cnx, cursor = conectarse('administrador')
        cursor.execute("SELECT * FROM turnos")
        turnos = cursor.fetchall()
        print("\n              TURNOS")
        print(tabulate(turnos, headers=["ID Turno", "Hora inicio", "Hora fin"], tablefmt="fancy_grid"))
        id_turno = input("ID del turno que deseas eliminar (0 para volver): ")
        turnos_ids = [str(turno[0]) for turno in turnos]
        while id_turno not in turnos_ids and id_turno != '0':
            id_turno = input("\nID incorrecto, por favor seleccione uno de la lista: ")
        if id_turno == "0":
            break
        clases_asociadas = clases_por_turno(id_turno)
        if clases_asociadas:
            print(f"\nSe dictan clases en el turno que desea eliminar.")
            confirmacion = input("\nPresiona 1 para eliminar todas las clases que se dicten en el turno seleccionado, o cualquier otra tecla para cancelar: ")
            if confirmacion == "1":
                cnx, cursor = conectarse('administrador')
                if cnx is not None and cursor is not None:
                    try:
                        cursor.execute(
                            "DELETE FROM alumno_clase WHERE id_clase IN (SELECT id FROM clase WHERE id_turno = %s)",
                            (id_turno,))
                        cursor.execute("DELETE FROM clase WHERE id_turno = %s", (id_turno,))
                        cnx.commit()
                    except Exception as e:
                        print(f"Error durante la consulta: {e}")
                    finally:
                        cursor.close()
                        cnx.close()
                    delete_turno(id_turno)
                    print(f"\nTurno {id_turno} y todas sus referencias eliminadas correctamente.")
            else:
                print("\nOperación cancelada.")
        else:
            delete_turno(id_turno)
            print(f"\nTurno {id_turno} eliminado correctamente.")

def delete_turno(id):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("DELETE FROM turnos WHERE id = %s", (id,))
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def modificar_turno():
    while True:
        time.sleep(0.8)
        cnx, cursor = conectarse('administrador')
        cursor.execute("SELECT * FROM turnos")
        turnos = cursor.fetchall()
        print("\n              TURNOS")
        print(tabulate(turnos, headers=["ID Turno", "Hora inicio", "Hora fin"], tablefmt="fancy_grid"))
        while True:
            id_turno = input("ID del turno que deseas modificar (0 para volver): ")
            turnos_ids = [str(turno[0]) for turno in turnos]
            while id_turno not in turnos_ids and id_turno != '0':
                id_turno = input("\nID incorrecto, por favor seleccione uno de la lista: ")
            if id_turno == "0":
                return
            clases_asociadas = clases_por_turno(id_turno)
            if clases_asociadas:
                print(f"\nExisten clases que se dictan en el turno que desea modificar.")
                confirmacion = input("\nPresiona 1 para modificar el turno de todas formas, o cualquier otra tecla para cancelar: ")
                if confirmacion != "1":
                    print("\nOperación cancelada")
                    break
            while True:
                hora_inicio = input("\nIngrese el horario de inicio en formato HH:MM (0 para volver): ")
                if hora_inicio == "0":
                    return
                if validar_hora(hora_inicio):
                    break
                else:
                    print("\nFormato incorrecto. Por favor, ingrese un horario válido (HH:MM).")
            while True:
                hora_fin = input("\nIngrese el horario de fin en formato HH:MM (0 para volver): ")
                if hora_fin == "0":
                    return
                if validar_hora(hora_fin):
                    break
                else:
                    print("\nFormato incorrecto. Por favor, ingrese un horario válido (HH:MM).")
            hora_inicio_dt = datetime.strptime(hora_inicio, '%H:%M')
            hora_fin_dt = datetime.strptime(hora_fin, '%H:%M')
            if hora_fin_dt - hora_inicio_dt != timedelta(hours=2):
                print("\nLa diferencia entre la hora de inicio y fin debe ser de 2 horas.\n")
                continue
            if coincidencia_turno(turnos, hora_inicio_dt, hora_fin_dt):
                print("\nEl turno ingresado coincide con un turno existente.")
                continue
            update_turno(id_turno, hora_inicio, hora_fin)
            print(f"\nAhora el turno {id_turno} es de {hora_inicio} a {hora_fin}")
            break

def update_turno(id, nueva_hora_inicio, nueva_hora_fin):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE turnos SET hora_inicio = %s, hora_fin = %s WHERE id = %s",
                           (nueva_hora_inicio, nueva_hora_fin, id))
            cnx.commit()
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

def clases_por_turno(id_turno):
    cnx, cursor = conectarse('administrador')
    clases = []
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("SELECT * FROM clase WHERE id_turno = %s", (id_turno,))
            clases = cursor.fetchall()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()
    return clases