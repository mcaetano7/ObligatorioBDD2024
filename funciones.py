from conexion import conectarse

def insert_login(usuario, password):
    cnx, cursor = conectarse()
    if cnx is not None and cursor is not None:
        try:
            print('Ejecutando la consulta...')
            #cursor.execute("INSERT INTO login (correo, contraseña) VALUES (%s, %s)", (usuario, password))
            cursor.execute("SELECT * FROM vista_correo")
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