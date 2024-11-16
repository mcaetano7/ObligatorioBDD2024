from conexion import conectarse
from hash import *


def insert_login(correo, contraseña, id_rol):
    cnx, cursor = conectarse('administrador')
    hashed_password = hash_password(contraseña)
    cursor.execute("INSERT INTO login (correo, contraseña, id_rol) VALUES (%s, %s, %s)",
                    (correo, hashed_password, id_rol))
    cnx.commit()
    cursor.close()
    cnx.close()


def baja_login(correo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("DELETE FROM login WHERE correo = %s", correo)
    cnx.commit()
    cursor.close()
    cnx.close()


def validar_credenciales(correo, contraseña) -> bool:
    cnx, cursor = conectarse('administrador')
    cursor.execute("SELECT contraseña FROM login WHERE correo = %s", correo)
    result = cursor.fetchone()
    if result is None:
        return False
    hashed_password = result[0].encode('utf-8')
    cursor.close()
    cnx.close()
    if check_password(contraseña, hashed_password):
        return True
    else:
        return False

def usuario_existente(correo) -> bool:
    cnx, cursor = conectarse('administrador')
    cursor.execute("SELECT correo FROM login WHERE correo = %s", (correo,))
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    if result is not None:
        return True
    return False


