from conexion import conectarse


def alta_instructor(correo):
    insert_instructor(input("Ingrese su cédula: "),
                      input("Ingrese su nombre: "),
                      input("Ingrese su apellido: "),
                      correo)


def insert_instructor(ci, nombre, apellido, correo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("INSERT INTO instructores (ci, nombre, apellido, correo) VALUES (%s, %s, %s, %s)",
                   (ci, nombre, apellido, correo))
    cnx.commit()
    cursor.close()
    cnx.close()


def delete_instructor(ci):
    cnx, cursor = conectarse('administrador')
    cursor.execute("DELETE FROM instructores WHERE ci = %s", ci)
    cnx.commit()
    cursor.close()
    cnx.close()

def modificar_instructor(correo):
    print("Modificación de instructor")
    nuevo_nombre = input("Ingrese el nombre del instructor: ")
    nuevo_apellido = input("Ingrese el apellido del instructor: ")
    update_instructor(nuevo_nombre, nuevo_apellido, correo)
    print(f"Datos del instructor {nuevo_nombre} modificados correctamente")

def update_instructor(nombre, apellido, correo):
    cnx, cursor = conectarse('instructor')
    cursor.execute("UPDATE instructores SET nombre = %s, apellido = %s WHERE correo = %s", (nombre, apellido, correo))
    cnx.commit()
    cursor.close()
    cnx.close()

def select_instructor(correo):
    cnx, cursor = conectarse('instructor')
    cursor.execute("SELECT * FROM instructores WHERE correo = %s", correo)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result