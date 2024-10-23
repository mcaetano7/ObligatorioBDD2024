CREATE DATABASE `obligatoriobdd2024` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;

USE obligatoriobdd2024;

CREATE TABLE login(
    correo VARCHAR(50) NOT NULL PRIMARY KEY,
    contraseña VARCHAR(20) NOT NULL
);

CREATE TABLE actividades(
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100),
    costo INT
);

CREATE TABLE equipamiento(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_actividad INT,
    descripcion VARCHAR(100),
    costo INT,
    FOREIGN KEY (id_actividad) REFERENCES actividades(id)
);

CREATE TABLE instructores(
    ci INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR(20)
);

CREATE TABLE turnos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    hora_inicio TIME,
    hora_fin TIME
);

CREATE TABLE alumnos(
    ci INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    fecha_nacimiento DATE
);

CREATE TABLE clase(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ci_instructor INT,
    id_actividad INT,
    id_turno INT,
    dictada TINYINT(1) DEFAULT 0,
    FOREIGN KEY (ci_instructor) REFERENCES instructores(ci),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id),
    FOREIGN KEY (id_turno) REFERENCES turnos(id)
);

CREATE TABLE alumno_clase(
    id_clase INT,
    ci_alumno INT,
    id_equipamiento INT,
    PRIMARY KEY (id_clase, ci_alumno),
    FOREIGN KEY (id_clase) REFERENCES clase(id),
    FOREIGN KEY (ci_alumno) REFERENCES alumnos(ci),
    FOREIGN KEY (id_equipamiento) REFERENCES equipamiento(id)
);