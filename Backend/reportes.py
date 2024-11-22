from tabulate import tabulate
from conexion import conectarse
from funciones import obtener_rol
import time

def mostrar_reportes(correo):
    cnx, cursor = conectarse(obtener_rol(correo))
    query1 = """
        SELECT a.id AS id_actividad,
a.descripcion AS actividad,
SUM(CASE
WHEN ac.id_clase IS NOT NULL THEN a.costo
ELSE 0
END) + IFNULL(SUM(e.costo), 0) AS ingresos_totales
FROM actividades a
LEFT JOIN clase c ON a.id = c.id_actividad
LEFT JOIN alumno_clase ac ON c.id = ac.id_clase
LEFT JOIN equipamiento e ON ac.id_equipamiento = e.id
GROUP BY a.id, a.descripcion
HAVING ingresos_totales > 0
ORDER BY ingresos_totales DESC
LIMIT 5;
    """
    cursor.execute(query1)
    ingresos = cursor.fetchall()

    query2 = """
    SELECT a.id AS id_actividad, a.descripcion AS actividad, COUNT(DISTINCT ac.ci_alumno) AS total_alumnos
    FROM actividades a
    JOIN clase c ON a.id = c.id_actividad
    JOIN alumno_clase ac ON c.id = ac.id_clase
    GROUP BY a.id, a.descripcion
    HAVING COUNT(DISTINCT ac.ci_alumno) > 0
    ORDER BY total_alumnos DESC
    LIMIT 5;
    """
    cursor.execute(query2)
    alumnos = cursor.fetchall()

    query3 = """
    SELECT t.id AS id_turno, t.hora_inicio, t.hora_fin, COUNT(c.id) AS total_clases
    FROM turnos t
    LEFT JOIN clase c ON t.id = c.id_turno AND c.dictada = 1
    GROUP BY t.id, t.hora_inicio, t.hora_fin
    HAVING COUNT(c.id) > 0
    ORDER BY total_clases DESC
    LIMIT 5;
    """

    cursor.execute(query3)
    turnos = cursor.fetchall()

    if obtener_rol(correo) == 'administrador':
        time.sleep(0.8)
        print("\nActividades con más ingresos:")
        if not ingresos:
            print("\nNo ha habido ingresos")
        else:
            print(tabulate(ingresos, headers=["ID actividad", "Descripción", "Ingresos totales"], tablefmt="fancy_grid"))

    time.sleep(0.8)
    print("\nActividades con mas alumnos:")
    if not alumnos:
        print("\nNo hay alumnos en ninguna clase")
    else:
        print(tabulate(alumnos, headers=["ID actividad", "Descripcion", "Total alumnos"], tablefmt="fancy_grid"))

    time.sleep(0.8)
    print("\nTurnos con mas clases dictadas:")
    if not turnos:
        print("\nNo se ha dictado ninguna clase")
    else:
        print(tabulate(turnos, headers=["ID Turno", "Hora de inicio",
                                    "Hora de finalizacion", "Total de clases"], tablefmt="fancy_grid"))

    input("\nPresione cualquier tecla para volver: ")

    cursor.close()
    cnx.close()
