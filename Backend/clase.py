import time

from tabulate import tabulate

from Backend.instructor import obtener_instructor, baja_instructor
from actividades import obtener_actividades
from turno import obtener_turnos
from funciones import obtener_rol
from conexion import conectarse

def select_clase(id, correo):
    cnx, cursor = conectarse(obtener_rol(correo))
    cursor.execute("SELECT * FROM clase WHERE id = %s", id)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result

def obtener_clases(correo):
    cnx, cursor = conectarse(obtener_rol(correo))
    cursor.execute("SELECT * FROM clase")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result

def alta_clase(correo):
    while True:
        time.sleep(0.8)
        print("\nElección de clase:")
        actividades = obtener_actividades(correo)
        print(tabulate(actividades, headers=["ID Actividad", "Descripción"], tablefmt="fancy_grid"))
        id_actividad = input("Actividad que deseas enseñar (0 para volver): ")
        actividades_ids = [str(actividad[0]) for actividad in actividades]
        while id_actividad not in actividades_ids and id_actividad != "0":
            id_actividad = input("\nID incorrecto, por favor seleccione uno de la lista: ")
        if id_actividad == "0":
            return
        print("\n")
        turnos = obtener_turnos(correo)
        while True:
            time.sleep(0.8)
            print(tabulate(turnos, headers=["ID Turno", "Hora inicio", "Hora fin"], tablefmt="fancy_grid"))
            id_turno = input("Horario en el que dictaras la clase (0 para volver): ")
            turnos_ids = [str(turno[0]) for turno in turnos]
            while id_turno not in turnos_ids and id_turno != '0':
                id_turno = input("\nID incorrecto, por favor seleccione uno de la lista: ")
            if id_turno == "0":
                break
            cnx, cursor = conectarse(obtener_rol(correo))
            ci_instructor = obtener_instructor(correo)[0]
            cursor.execute("SELECT hora_inicio, hora_fin FROM turnos WHERE id = %s", id_turno)
            turno_seleccionado = cursor.fetchone()
            hora_inicio_seleccionada = turno_seleccionado[0]
            hora_fin_seleccionada = turno_seleccionado[1]
            cursor.execute(
                "SELECT t.hora_inicio, t.hora_fin "
                "FROM clase c "
                "JOIN turnos t ON t.id = c.id_turno "
                "WHERE c.ci_instructor = %s AND c.dictada = 0"
                , ci_instructor)
            clases_actuales = cursor.fetchall()
            conflicto_horario = False
            for (hora_inicio, hora_fin) in clases_actuales:
                if not (hora_fin_seleccionada <= hora_inicio or hora_inicio_seleccionada >= hora_fin):
                    conflicto_horario = True
                    break
            if conflicto_horario:
                print("\nNo puedes inscribirte en esta clase debido a una superposición horaria.\n")
                continue
            cnx.close()
            cursor.close()
            cnx, cursor = conectarse('administrador')
            cursor.execute("INSERT INTO clase(ci_instructor, id_actividad, id_turno) VALUES "
                           "(%s, %s, %s)", (ci_instructor, id_actividad, id_turno))
            cnx.commit()
            cnx.close()
            cursor.close()
            print("\nElección realiada con éxito")
            return

def mostrar_clases_instructor(correo):
    while True:
        time.sleep(0.8)
        cnx, cursor = conectarse('instructor')
        instructor = obtener_instructor(correo)
        ci_instructor = instructor[0]
        cursor.execute("SELECT c.id, a.descripcion, t.hora_inicio, t.hora_fin, c.dictada FROM clase c "
                                           "JOIN actividades a ON a.id = c.id_actividad "
                                           "JOIN turnos t ON t.id = c.id_turno "
                                           "WHERE ci_instructor = %s", ci_instructor)
        clases_instructor = cursor.fetchall()
        if not clases_instructor:
            print("\nNo enseñas en ninguna clase")
            break
        resultados = []
        for fila in clases_instructor:
            fila = list(fila)
            fila[-1] = 'Sí' if fila[-1] == 1 else 'No'
            resultados.append(fila)
        print("\n                            TUS CLASES")
        print(tabulate(resultados, headers=["ID Clase", "Descripción", "Hora inicio", "Hora fin", "Dictada"], tablefmt="fancy_grid"))
        opcion = input("Presione 1 si desea dajar de dar una clase, 2 para marcar una clase como dictada, otra tecla para volver: ")
        if opcion == '1':
            id_clase = input("\nID de la clase que desea dejar: ")
            cursor.execute("SELECT id FROM clase WHERE id = %s AND ci_instructor = %s", (id_clase, ci_instructor))
            clase = cursor.fetchone()
            if clase is None:
                print(f"\nNo eres el instructor de la clase {id_clase} o la clase no existe.")
            else:
                cnx, cursor = conectarse('administrador')
                cursor.execute("DELETE FROM alumno_clase WHERE id_clase = %s", (id_clase,))
                cursor.execute("DELETE FROM clase WHERE id = %s", (id_clase,))
                print(f"\nYa no enseñarás la clase {id_clase}")
                cnx.commit()
                cnx.close()
                cursor.close()
        elif opcion == '2':
            id_clase = input("\nID de la clase que desea marcar como dictada: ")
            cursor.execute("SELECT id, dictada FROM clase WHERE id = %s AND ci_instructor = %s", (id_clase, ci_instructor))
            clase = cursor.fetchone()
            if clase is None:
                print(f"\nNo eres el instructor de la clase {id_clase} o la clase no existe.")
                continue
            if clase[1] == 1:
                print(f"\nLa clase {id_clase} ya está marcada como dictada")
                continue
            cursor.execute("UPDATE vista_clase_instructor SET dictada = 1 WHERE id = %s", (id_clase,))
            print(f"\nLa clase {id_clase} fue marcada como dictada exitosamente.")
            cnx.commit()
        else:
            break

def modificar_clase():
    pass