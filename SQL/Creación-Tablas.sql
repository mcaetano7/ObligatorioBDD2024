CREATE SCHEMA obligatorio2024;

USE obligatorio2024;

CREATE TABLE login(
    correo VARCHAR(50) NOT NULL PRIMARY KEY,
    contraseña VARCHAR(100) NOT NULL
);

ALTER TABLE login
    ADD COLUMN id_rol INT;

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
    apellido VARCHAR(20),
    correo VARCHAR(50),
    FOREIGN KEY (correo) REFERENCES login(correo)
);
ALTER TABLE instructores
ADD CONSTRAINT unique_correoI UNIQUE (correo);

CREATE TABLE turnos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    hora_inicio TIME,
    hora_fin TIME
);

CREATE TABLE alumnos(
    ci INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    fecha_nacimiento DATE,
    telefono VARCHAR(20),
    correo VARCHAR(50),
    FOREIGN KEY (correo) REFERENCES login(correo)
);


ALTER TABLE alumnos
ADD CONSTRAINT unique_correo UNIQUE (correo);

CREATE TABLE clase(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ci_instructor INT,
    id_actividad INT,
    id_turno INT,
    dictada BOOLEAN DEFAULT FALSE,
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

CREATE TABLE rol(
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(20) NOT NULL
);

ALTER TABLE login
ADD CONSTRAINT fk_rol FOREIGN KEY (id_rol)
    REFERENCES rol (id);


