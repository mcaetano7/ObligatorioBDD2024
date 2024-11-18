from tabulate import tabulate
from conexion import conectarse
from funciones import obtener_fecha_nacimiento

def baja_alumno(correo):
    cnx, cursor = conectarse('alumno')
    nombre = select_alumno(correo)[1]
    alumno_ci = select_alumno(correo)[0]
    cursor.execute("DELETE FROM alumno_clase WHERE ci_alumno = %s", alumno_ci)
    cursor.execute("DELETE FROM alumnos WHERE correo = %s", correo)
    cnx.commit()
    print(f"\nAlumno {nombre} eliminado con éxito.")
    cursor.close()
    cnx.close()

def modificar_alumno(correo):
    print("\nModificación de alumno:")
    nuevo_nombre = input("\nIngrese su nombre: ")
    nuevo_apellido = input("Ingrese su apellido: ")
    fecha = obtener_fecha_nacimiento()
    telefono = input("Ingrese su telefono: ")
    update_alumno(nuevo_nombre, nuevo_apellido, fecha, telefono, correo)
    print(f"\nSus datos fueron modificados correctamente.")

def update_alumno(nombre, apellido, fecha_nacimiento, telefono, correo):
    cnx, cursor = conectarse('alumno')
    cursor.execute("UPDATE alumnos SET nombre = %s, apellido = %s, fecha_nacimiento = %s, telefono = %s WHERE correo = %s",
                   (nombre, apellido, fecha_nacimiento, telefono, correo))
    cnx.commit()
    cursor.close()
    cnx.close()

def select_alumno(correo):
    cnx, cursor = conectarse('alumno')
    cursor.execute("SELECT * FROM alumnos WHERE correo = %s", correo)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result

def info_alumno(correo):
    ci, nombre, apellido, fecha_nacimiento, telefono, correo = select_alumno(correo)
    datos = [["Cédula", ci],
             ["Nombre", nombre],
             ["Apellido", apellido],
             ["Fecha de nacimiento", fecha_nacimiento],
             ["Teléfono", telefono],
             ["Correo", correo]]
    print("\n        TUS DATOS ")
    print(tabulate(datos, headers=["Campo", "Información"], tablefmt="fancy_grid"))
    if input("\nIngrese 1 si desea modificar sus datos, otra tecla para volver: ") == '1':
        modificar_alumno(correo)