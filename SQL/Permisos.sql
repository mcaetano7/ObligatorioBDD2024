USE obligatorio2024;

# creación usuarios
CREATE USER 'administrador'@'%'  IDENTIFIED BY 'adminpass';

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

CREATE VIEW vista_update_instructores AS SELECT nombre, apellido, correo FROM instructores

GRANT UPDATE ON vista_update_instructores TO 'instructor'@'%';

GRANT SELECT, INSERT, DELETE ON instructores TO 'instructor'@'%';

# permisos turnos
GRANT ALL PRIVILEGES ON turnos TO 'administrador'@'%';

GRANT SELECT ON turnos TO 'alumno'@'%';

GRANT SELECT ON turnos TO 'instructor'@'%';

# permisos alumnos
GRANT ALL PRIVILEGES ON alumnos TO 'administrador'@'%';

CREATE VIEW vista_update_alumnos AS SELECT nombre, apellido, fecha_nacimiento, telefono FROM alumnos

GRANT UPDATE ON vista_update_alumnos TO 'alumno'@'%';

GRANT SELECT, INSERT, UPDATE, DELETE ON alumnos TO 'alumno'@'%';

GRANT SELECT ON alumnos TO 'instructor'@'%';

# permisos clase
CREATE VIEW vista_clase_admin AS SELECT ci_instructor, id_actividad, id_turno FROM clase;

GRANT UPDATE ON vista_clase_admin TO 'administrador'@'%';

GRANT INSERT, SELECT, DELETE ON clase TO 'administrador'@'%';

GRANT SELECT ON clase TO 'alumno'@'%';

CREATE VIEW vista_clase_instructor AS SELECT id, dictada FROM clase

GRANT SELECT, UPDATE ON vista_clase_instructor TO 'instructor'@'%';

GRANT SELECT ON clase TO 'instructor'@'%';

# permisos alumno_clase
GRANT ALL PRIVILEGES ON alumno_clase TO 'administrador'@'%';

GRANT SELECT, INSERT, DELETE ON alumno_clase TO 'alumno'@'%';

GRANT SELECT ON alumno_clase TO 'instructor'@'%';

# permisos rol
GRANT ALL PRIVILEGES ON rol TO 'administrador'@'%';


