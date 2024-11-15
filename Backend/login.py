from conexion import conectarse
from hash import *

def insert_login(correo, contraseña, id_rol):
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            hashed_password = hash_password(contraseña)
            cursor.execute("INSERT INTO login (correo, contraseña, id_rol) VALUES (%s, %s, %s)", (correo, hashed_password, id_rol))
            resultados = cursor.fetchall()
            for el in resultados:
                print(el)
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if cnx is not None:
                cnx.close()
            else:
                print('No se pudo establecer la conexión.')

def baja_login(correo):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("DELETE FROM login WHERE correo = %s", correo)
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def validar_credenciales(correo, contraseña) -> bool:
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("SELECT contraseña FROM login WHERE correo = %s", correo)
            result = cursor.fetchone()
            if result is None:
                return False
            hashed_password = result[0].encode('utf-8')
            if check_password(contraseña, hashed_password):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al validar credenciales: {e}")
            return False
        finally:
            cursor.close()
            cnx.close()
    else:
        print("No se pudo conectar a la base de datos.")
        return False

def usuario_existente(correo) -> bool:
    cnx, cursor = conectarse('administrador')
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("SELECT correo FROM login WHERE correo = %s", (correo,))
            result = cursor.fetchone()
            if result is not None:
                return True
            return False
        except Exception as e:
            print(f"Error al validar credenciales: {e}")
            return False
        finally:
            cursor.close()
            cnx.close()
    else:
        print("No se pudo conectar a la base de datos.")
        return False