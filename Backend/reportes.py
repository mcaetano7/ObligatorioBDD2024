from tabulate import tabulate
from conexion import conectarse


def mostrar_reportes():
    cnx, cursor = conectarse('reportes')
    query1 = """
    SELECT a.id AS id_actividad, a.descripcion AS actividad, SUM(a.costo + IFNULL(e.costo, 0)) AS ingresos_totales
    FROM actividades a
    LEFT JOIN equipamiento e ON a.id = e.id_actividad
    LEFT JOIN clase c ON a.id = e.id_actividad
    GROUP BY a.id, a.descripcion
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
    ORDER BY total_alumnos DESC
    LIMIT 5;
    """
    cursor.execute(query2)
    alumnos = cursor.fetchall()

    query3 = """
    SELECT t.id AS id_turno, t.hora_inicio, t.hora_fin, COUNT(c.id) AS total_clases
    FROM turnos t
    LEFT JOIN clase c ON t.id = c.id_turno
    GROUP BY t.id, t.hora_inicio, t.hora_fin
    ORDER BY total_clases DESC
    LIMIT 5;
    """

    cursor.execute(query3)
    turnos = cursor.fetchall()

    print("\nActividades con más ingresos:")
    print(tabulate(ingresos, headers=["ID actividad", "Descripción", "Ingresos totales"], tablefmt="fancy_grid"))

    print("\nActividades con mas alumnos:")
    print(tabulate(alumnos, headers=["ID actividad", "Descripcion", "Total alumnos"], tablefmt="fancy_grid"))

    print("\nTurnos con mas clases dictadas:")
    print(tabulate(turnos, headers=["ID Turno", "Hora de inicio",
                                    "Hora de finalizacion", "Total de clases"], tablefmt="fancy_grid"))

    cursor.close()
    cnx.close()
