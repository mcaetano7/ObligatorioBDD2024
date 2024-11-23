import time
from alumnos import select_alumno
from clase import obtener_clases
from conexion import conectarse
from tabulate import tabulate


def alta_alumno_clase(correo):
    while True:
        time.sleep(1)
        cnx, cursor = conectarse('alumno')
        cursor.execute("SELECT ci FROM alumnos WHERE correo = %s", (correo,))
        alumno_ci = cursor.fetchone()[0]
        cursor.execute(
            "SELECT c.id, CONCAT(i.nombre, ' ', i.apellido) AS instructor, a.descripcion, t.hora_inicio, t.hora_fin, a.costo "
            "FROM clase c "
            "JOIN instructores i ON c.ci_instructor = i.ci "
            "JOIN actividades a ON a.id = c.id_actividad "
            "JOIN turnos t ON t.id = c.id_turno "
            "WHERE c.dictada = 0 "
            )
        clases = cursor.fetchall()
        if not clases:
            print("\nNo hay clases disponibles\n")
            return
        else:
            headers = ["ID Clase", "Instructor", "Actividad", "Hora Inicio", "Hora Fin", "Costo"]
            print("\nEstas son las clases disponibles:")
            print(tabulate(clases, headers=headers, tablefmt="fancy_grid"))
            id_clase = input("\nNúmero de clase a la que te deseas inscribir (o presione 0 para volver): ")
            if not validacion_id(correo, id_clase) and id_clase != '0':
                print("\nClase inexistente. ")
                continue
            if id_clase == "0":
                return
            cursor.execute(
                "SELECT COUNT(*) "
                "FROM alumno_clase "
                "WHERE ci_alumno = %s AND id_clase = %s "
                , (alumno_ci, id_clase))
            ya_inscrito = cursor.fetchone()[0]
            if ya_inscrito:
                print("\nYa estás inscripto en esta clase. Elige otra.")
                continue
            cursor.execute(
                "SELECT t.hora_inicio, t.hora_fin "
                "FROM clase c "
                "JOIN turnos t ON t.id = c.id_turno "
                "WHERE c.id = %s"
                , id_clase)
            clase_seleccionada = cursor.fetchone()
            hora_inicio_nueva_clase = clase_seleccionada[0]
            hora_fin_nueva_clase = clase_seleccionada[1]
            cursor.execute(
                "SELECT t.hora_inicio, t.hora_fin "
                "FROM clase c "
                "JOIN alumno_clase ac ON ac.id_clase = c.id "
                "JOIN turnos t ON t.id = c.id_turno "
                "WHERE ac.ci_alumno = %s AND c.dictada = 0"
                , alumno_ci)
            clases_actuales = cursor.fetchall()
            conflicto_horario = False
            for (hora_inicio, hora_fin) in clases_actuales:
                if not (hora_fin_nueva_clase <= hora_inicio or hora_inicio_nueva_clase >= hora_fin):
                    conflicto_horario = True
                    break
            if conflicto_horario:
                print("\nNo puedes inscribirte en esta clase debido a una superposición horaria.")
                continue
            print("\nEquipamientos disponibles para la clase seleccionada:")
            cursor.execute(
                "SELECT e.id, e.descripcion, e.costo "
                "FROM equipamiento e "
                "JOIN actividades a ON e.id_actividad = a.id "
                "WHERE a.id = (SELECT c.id_actividad FROM clase c WHERE c.id = %s)"
                 , id_clase)
            equipamientos = cursor.fetchall()
            headers = ["ID Equipamiento", "Equipamiento", "Costo de alquiler"]
            print(tabulate(equipamientos, headers=headers, tablefmt="fancy_grid"))
            id_equipamiento = input("Elige por su id: ")
            equipamiento_ids = [str(equip[0]) for equip in equipamientos]
            while id_equipamiento not in equipamiento_ids:
                id_equipamiento = input("ID incorrecto, por favor seleccione uno de la lista: ")
            insert_alumno_clase(id_clase, alumno_ci, id_equipamiento)


def insert_alumno_clase(id_clase, ci_alumno, id_equipamiento):
    cnx, cursor = conectarse('alumno')
    cursor.execute("INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES (%s, %s, %s)",
                   (id_clase, ci_alumno, id_equipamiento))
    print(f"\nTe has inscripto al curso {id_clase}")
    cnx.commit()
    cursor.close()
    cnx.close()

def mostrar_alumno_clases(correo):
    while True:
        time.sleep(0.8)
        cnx, cursor = conectarse('alumno')
        cursor.execute("SELECT ac.id_clase, CONCAT(i.nombre, ' ', i.apellido) AS instructor, "
                        "a.descripcion, e.descripcion, t.hora_inicio, t.hora_fin, a.costo + e.costo, c.dictada "
                        "FROM clase c "
                        "JOIN alumno_clase ac on c.id = ac.id_clase "
                        "JOIN instructores i on c.ci_instructor = i.ci "
                        "JOIN actividades a on a.id = c.id_actividad "
                        "JOIN turnos t on t.id = c.id_turno "
                        "JOIN equipamiento e on ac.id_equipamiento = e.id "
                        "JOIN alumnos al on al.ci = ac.ci_alumno "
                        "WHERE al.correo = %s", correo)
        results = cursor.fetchall()
        if not results:
            print("\nNo esás inscripto a ninguna clase.\n")
            break
        else:
            resultados = []
            for fila in results:
                fila = list(fila)
                fila[-1] = 'Sí' if fila[-1] == 1 else 'No'  # Cambiar 1 por 'Sí' y 0 por 'No'
                resultados.append(fila)
            headers = ["ID Clase", "Instructor", "Actividad", "Equipamiento alquilado", "Hora Inicio", "Hora Fin", "Costo total", "Dictada"]
            print("\n                                 TUS CLASES")
            print(tabulate(resultados, headers=headers, tablefmt="fancy_grid"))
            if input("Presione 1 si desea darse de baja de una clase, otra tecla para volver: ") == '1':
                id_clase = input("\nID de la clase a la que desea darse de baja: ")
                ci = select_alumno(correo)[0]
                cursor.execute("SELECT id_clase FROM alumno_clase WHERE ci_alumno = %s", (ci,))
                clases_inscriptas = cursor.fetchall()
                clases_inscriptas_ids = [str(fila[0]) for fila in clases_inscriptas]
                baja_alumno_clase(correo, id_clase)
                if id_clase in clases_inscriptas_ids:
                    baja_alumno_clase(correo, id_clase)
                    print(f"\nEl alumno con correo {correo} ha sido dado de baja de la clase {id_clase}.")
                else:
                    print("\nNo estás inscripto en la clase seleccionada.")
            else:
                break

def baja_alumno_clase(correo, id_clase):
    cnx, cursor = conectarse('alumno')
    alumno_ci = select_alumno(correo)[0]
    cursor.execute("DELETE FROM alumno_clase "
                   "WHERE id_clase = %s AND ci_alumno = %s", (id_clase, alumno_ci))
    cnx.commit()
    cursor.close()
    cnx.close()

def validacion_id(correo, id_clase):
    clases = obtener_clases(correo)
    clases_ids = [str(clase[0]) for clase in clases]
    if id_clase not in clases_ids:
        return False
    return True
