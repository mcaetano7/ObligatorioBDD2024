USE obligatorio2024;

INSERT INTO turnos(hora_inicio, hora_fin) VALUES
('9:00', '11:00'),
('12:00', '14:00'),
('16:00', '18:00');

INSERT INTO actividades(descripcion, costo) VALUES
('Snowboard', 2500),
('Ski', 2900),
('Moto de Nieve', 4500);

INSERT INTO equipamiento(id_actividad, descripcion, costo) VALUES
(1, 'Antiparras', 500),
(2, 'Antiparras', 500),
(3, 'Antiparras', 500),
(1, 'Casco', 650),
(2, 'Casco', 650),
(3, 'Casco', 650),
(1, 'Tabla de snowboard', 800),
(2, 'Esquíes', 750),
(1, 'Botas de nieve', 300),
(2, 'Botas de nieve', 300),
(3, 'Botas de nieve', 300);

INSERT INTO rol(descripcion) VALUES
('administrador'),
('instructor'),
('alumno');

INSERT INTO login(correo, contraseña, id_rol) VALUES
('juanperezcerro@gmail.com', '1234', 1);

