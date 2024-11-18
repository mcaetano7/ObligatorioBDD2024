from tabulate import tabulate

from conexion import conectarse

def insert_instructor(ci, nombre, apellido, correo):
    cnx, cursor = conectarse('instructor')
    try:
        cursor.execute("INSERT INTO instructores (ci, nombre, apellido, correo) VALUES (%s, %s, %s, %s)",
                   (ci, nombre, apellido, correo))
        cnx.commit()
        print(f"\nInstructor {nombre} {apellido} registrado con éxito.")
    except Exception as e:
        print(e)
        print("\nYa existe un instructor con esa cédula.")
        cnx.rollback()
        return
    finally:
        cursor.close()
        cnx.close()

def baja_instructor(correo):
    cnx, cursor = conectarse('administrador')
    ci_instructor = obtener_instructor(correo)[0]
    nombre = obtener_instructor(correo)[1]
    cursor.execute(
             "DELETE FROM alumno_clase "
             "WHERE id_clase IN "
             "(SELECT id FROM clase WHERE ci_instructor = %s) "
            , (ci_instructor,))
    cursor.execute(
             "DELETE FROM clase "
             "WHERE ci_instructor = %s"
             , (ci_instructor,))
    cursor.execute(
             "DELETE FROM instructores " 
             "WHERE ci = %s "
             , (ci_instructor,))
    cnx.commit()
    print(f"\nAlumno {nombre} eliminado con éxito.")
    cnx.close()
    cursor.close()

def modificar_instructor(correo):
    print("\nModificación de instructor:")
    nuevo_nombre = input("\nIngrese el nombre del instructor: ")
    nuevo_apellido = input("Ingrese el apellido del instructor: ")
    update_instructor(nuevo_nombre, nuevo_apellido, correo)
    print(f"\nDatos del instructor {nuevo_nombre} modificados correctamente")

def update_instructor(nombre, apellido, correo):
    cnx, cursor = conectarse('instructor')
    cursor.execute("UPDATE vista_update_instructores SET nombre = %s, apellido = %s WHERE correo = %s", (nombre, apellido, correo))
    cnx.commit()
    cursor.close()
    cnx.close()

def obtener_instructor(correo):
    cnx, cursor = conectarse('instructor')
    cursor.execute("SELECT * FROM instructores WHERE correo = %s", correo)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result

def info_instructor(correo):
    ci, nombre, apellido, correo = obtener_instructor(correo)
    datos = [["Cédula", ci],
             ["Nombre", nombre],
             ["Apellido", apellido],
             ["Correo", correo]]
    print("\n        TUS DATOS ")
    print(tabulate(datos, headers=["Campo", "Información"], tablefmt="fancy_grid"))
    if input("\nIngrese 1 si desea modificar sus datos, otra tecla para volver: ") == '1':
        modificar_instructor(correo)