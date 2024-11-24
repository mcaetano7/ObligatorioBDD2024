USE obligatorio2024;

#reportes ingresos totales
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

#reportes mas alumnos inscriptos
SELECT a.id AS id_actividad, a.descripcion AS actividad, COUNT(DISTINCT ac.ci_alumno) AS total_alumnos
FROM actividades a
JOIN clase c ON a.id = c.id_actividad
JOIN alumno_clase ac ON c.id = ac.id_clase
GROUP BY a.id, a.descripcion
HAVING COUNT(DISTINCT ac.ci_alumno) > 0
ORDER BY total_alumnos DESC
LIMIT 5;

#reportes mas clases elegidas
SELECT t.id AS id_turno, t.hora_inicio, t.hora_fin, COUNT(c.id) AS total_clases
FROM turnos t
LEFT JOIN clase c ON t.id = c.id_turno AND c.dictada = 1
GROUP BY t.id, t.hora_inicio, t.hora_fin
HAVING COUNT(c.id) > 0
ORDER BY total_clases DESC
LIMIT 5;