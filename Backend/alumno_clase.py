from Backend.alumnos import select_alumno
from Backend.clase import select_clase
from Backend.equipamiento import obtener_equipamientos
from conexion import conectarse
from tabulate import tabulate

def alta_alumno_clase(correo):
    cnx, cursor = conectarse('alumno')
    cursor.execute("SELECT ac.id_clase, CONCAT(i.nombre, ' ', i.apellido) AS instructor, a.descripcion, e.descripcion, t.hora_inicio, t.hora_fin FROM clase c "
                    "JOIN alumno_clase ac on c.id = ac.id_clase "
                    "JOIN instructores i on c.ci_instructor = i.ci "
                    "JOIN actividades a on a.id = c.id_actividad "
                    "JOIN turnos t on t.id = c.id_turno "
                    "JOIN equipamiento e on ac.id_equipamiento = e.id "
                    "JOIN alumnos al on al.ci = ac.ci_alumno "
                    )
    results = cursor.fetchall()
    if not results:
        print("\nNo hay clases disponibles\n")
    else:
        headers = ["ID Clase", "Instructor", "Actividad", "Equipamiento alquilado", "Hora Inicio", "Hora Fin"]
        print("\nEstas son las clases a las que te puedes inscribir:")
        print(tabulate(results, headers=headers, tablefmt="grid"))
        id_clase = input("Número de clase a la que te deseas inscribir: ")
        while select_clase(id_clase, correo) is None:
            id_clase = input("Número de clase incorrecto, ingrese una clase de la lista: ")
        print("\nEquipamientos disponibles para la clase seleccionada:")
        id_actividad = select_clase(id_clase, correo)[2]
        headers = ["ID Equipamiento", "Equipamiento", "Costo de alquiler"]
        print("\nPuedes alquilar uno de estos:")
        print(tabulate(obtener_equipamientos(id_actividad), headers=headers, tablefmt="grid"))
        id_equipamiento = input("Elige por su id: ")
        insert_alumno_clase(id_clase, select_alumno(correo)[0], id_equipamiento)


def insert_alumno_clase(id_clase, ci_alumno, id_equipamiento):
    cnx, cursor = conectarse('alumno')
    cursor.execute("INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES (%s, %s, %s, %s)",
                   (id_clase, ci_alumno, id_equipamiento))
    cnx.commit()
    cursor.close()
    cnx.close()

def mostrar_alumno_clases(correo):
    cnx, cursor = conectarse('alumno')
    cursor.execute("SELECT ac.id_clase, CONCAT(i.nombre, ' ', i.apellido) AS instructor, a.descripcion, e.descripcion, t.hora_inicio, t.hora_fin FROM clase c "
                    "JOIN alumno_clase ac on c.id = ac.id_clase "
                    "JOIN instructores i on c.ci_instructor = i.ci "
                    "JOIN actividades a on a.id = c.id_actividad "
                    "JOIN turnos t on t.id = c.id_turno "
                    "JOIN equipamiento e on ac.id_equipamiento = e.id "
                    "JOIN alumnos al on al.ci = ac.ci_alumno "
                    "WHERE al.correo = %s AND c.dictada = 0", correo)
    results = cursor.fetchall()
    if not results:
        print("\nNo esás inscripto a ninguna clase.\n")
    else:
        headers = ["ID Clase", "Instructor", "Actividad", "Equipamiento alquilado", "Hora Inicio", "Hora Fin"]
        print("\nEstas son tus próximas clases:")
        print(tabulate(results, headers=headers, tablefmt="grid"))
        input("Presione cualquier tecla para volver: ")

def select_alumno_clase(correo):
    pass