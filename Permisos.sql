use obligatorio2024;

# creación usuarios
CREATE USER 'administrador'@'localhost'  IDENTIFIED BY 'adminpass';

CREATE USER 'instructor'@'%' IDENTIFIED BY 'instructorpass';

CREATE USER 'alumno'@'%' IDENTIFIED BY 'alumnopass';

# permisos login
GRANT ALL PRIVILEGES ON login TO 'administrador'@'%';

CREATE VIEW vista_correo AS SELECT correo FROM login;

GRANT SELECT ON vista_correo TO 'alumno'@'%';

GRANT SELECT ON vista_correo TO 'instructor'@'%';

# permisos actividades
GRANT ALL PRIVILEGES ON actividades TO 'administrador'@'%';

GRANT SELECT ON actividades TO 'alumno'@'%';

GRANT SELECT ON actividades TO 'instructor'@'%';

# permisos equipamiento
GRANT ALL PRIVILEGES ON equipamiento TO 'administrador'@'%';

GRANT SELECT ON equipamiento TO 'alumno'@'%';

GRANT SELECT ON equipamiento TO 'instructor'@'%';

# permisos instructores
GRANT ALL PRIVILEGES ON instructores TO 'administrador'@'%';

GRANT SELECT ON instructores TO 'alumno'@'%';

GRANT SELECT ON instructores TO 'instructor'@'%';

# permisos turnos
GRANT ALL PRIVILEGES ON turnos TO 'administrador'@'%';

GRANT SELECT ON turnos TO 'alumno'@'%';

GRANT SELECT ON turnos TO 'instructor'@'%';

# permisos alumnos
GRANT ALL PRIVILEGES ON alumnos TO 'administrador'@'%';

GRANT SELECT ON alumnos TO 'alumno'@'%';

GRANT SELECT ON alumnos TO 'instructor'@'%';

# permisos clase
CREATE VIEW vista_clase_admin AS SELECT ci_instructor, id_actividad, id_turno FROM clase;

GRANT UPDATE ON vista_clase_admin TO 'administrador'@'%';

GRANT SELECT, DELETE, INSERT ON clase TO 'administrador'@'%';

GRANT SELECT ON clase TO 'alumno'@'%';

GRANT SELECT ON clase TO 'instructor'@'%';

# permisos alumno_clase
GRANT ALL PRIVILEGES ON alumno_clase TO 'administrador'@'%';

GRANT SELECT ON alumno_clase TO 'alumno'@'%';

GRANT SELECT ON alumno_clase TO 'instructor'@'%';

# permisos rol
GRANT ALL PRIVILEGES ON rol TO 'administrador'@'%';


