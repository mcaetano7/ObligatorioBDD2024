from conexion import conectarse
from funciones import obtener_fecha_nacimiento

def alta_alumno(correo):
    cedula = input("\nIngrese su cédula: ")
    while len(cedula) != 8:
        print("La cédula debe tener 8 números.")
        cedula = input("Ingrese su cédula: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_nacimiento = obtener_fecha_nacimiento()
    telefono = input("Ingrese su telefono: ")
    insert_alumno(cedula, nombre, apellido, fecha_nacimiento, telefono, correo)

def insert_alumno(ci, nombre, apellido, fecha_nacimiento, telefono, correo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("INSERT INTO alumnos (ci, nombre, apellido,"
                   " fecha_nacimiento, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s)",
                   (ci, nombre, apellido, fecha_nacimiento, telefono, correo))
    cnx.commit()
    print(f"\nAlumno {nombre} {apellido} registrado con éxito.")
    cursor.close()
    cnx.close()


def baja_alumno(correo):
    cnx, cursor = conectarse('administrador')
    nombre = select_alumno(correo)[1]
    cursor.execute("DELETE FROM alumnos WHERE correo = %s", correo)
    cnx.commit()
    print(f"\nAlumno {nombre} eliminado con éxito.")
    cursor.close()
    cnx.close()

def modificar_alumno(correo):
    print("\nModificación de alumno")
    nuevo_nombre = input("Ingrese su nombre: ")
    nuevo_apellido = input("Ingrese su apellido: ")
    fecha = obtener_fecha_nacimiento()
    telefono = input("Ingrese su telefono: ")
    update_alumno(nuevo_nombre, nuevo_apellido, fecha, telefono, correo)
    print(f"Sus datos fueron modificados correctamente.")

def update_alumno(nombre, apellido, fecha_nacimiento, telefono, correo):
    cnx, cursor = conectarse('alumno')
    cursor.execute("UPDATE alumnos SET nombre = %s, apellido = %s, fecha_nacimiento = %s, telefono = %s WHERE correo = %s",
                   (nombre, apellido, fecha_nacimiento, telefono, correo))
    cnx.commit()
    print(f"Alumno {nombre} modificado con éxito.")
    cursor.close()
    cnx.close()

def select_alumno(correo):
    cnx, cursor = conectarse('alumno')
    cursor.execute("SELECT * FROM alumnos WHERE correo = %s", correo)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result


