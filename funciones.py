from conexion import conectarse



def insert_login(usuario, password):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            cursor.execute("INSERT INTO login (correo, contraseña) VALUES (%s, %s)", (usuario, password))
            print('Consulta ejecutada.')
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
                print('Conexión cerrada')
            else:
                print('No se pudo establecer la conexión.')

#ABM Instructores
def alta_instructor(ci, nombre, apellido):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            cursor.execute("INSERT INTO instructor (ci, nombre, apellido) VALUES (%s, %s, %s)", (ci, nombre, apellido))
            print('Consulta ejecutada.')
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def baja_instructor(ci):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            cursor.execute("DELETE FROM instructor WHERE ci = %s", (ci,))
            print('Consulta ejecutada.')
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def modificacion_instructor(ci, nombre, apellido):  
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            cursor.execute("UPDATE instructor SET nombre = %s, apellido = %s WHERE ci = %s", (nombre, apellido, ci))
            print('Consulta ejecutada.')
            cnx.commit()
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

#ABM Turnos
def insert_turno(id, hora_inicio, hora_fin):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("INSERT INTO turno (id, hora_inicio, hora_fin) VALUES (%s, %s, %s)", (id, hora_inicio, hora_fin))
            cnx.commit()
            print(f"Turno de {hora_inicio} a {hora_fin} creado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close() 
            cnx.close()

def baja_turno(id):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("DELETE FROM turno WHERE id = %s", (id,))
            cnx.commit()
            print(f"Turno {id} eliminado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def modificacion_turno(id, nueva_hora_inicio, nueva_hora_fin):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE turno SET hora_inicio = %s, hora_fin = %s WHERE id = %s", 
                           (nueva_hora_inicio, nueva_hora_fin, id))
            cnx.commit()
            print(f"Turno {id} modificado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

#Modificacion actividades
def modificacion_actividades(id, descripacion, costo):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE actividades SET descripcion = %s, costo = %s WHERE id = %s", 
                           (descripacion, costo, id))
            cnx.commit()
            print(f"Actividad {id} modificada con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

#ABM Alumnos
def insert_alumno(ci, nombre, apellido, fecha_nacimiento):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("INSERT INTO alumno (ci, nombre, apellido, fecha_nacimiento) VALUES (%s, %s, %s, %s)", 
                           (ci, nombre, apellido, fecha_nacimiento)) 
            cnx.commit()
            print(f"Alumno {nombre} {apellido} agregado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def baja_alumno(ci):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("DELETE FROM alumno WHERE ci = %s", (ci,))
            cnx.commit()
            print(f"Alumno {ci} eliminado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()

def modificacion_alumno(ci, nombre, apellido, fecha_nacimiento):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            cursor.execute("UPDATE alumno SET nombre = %s, apellido = %s, fecha_nacimiento = %s WHERE ci = %s", 
                           (nombre, apellido, fecha_nacimiento, ci))
            cnx.commit()
            print(f"Alumno {ci} modificado con éxito.")
        except Exception as e:
            print(f"Error durante la consulta: {e}")
        finally:
            cursor.close()
            cnx.close()