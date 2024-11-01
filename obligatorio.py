import pymysql

# Inicializamos las variables fuera de la función
cnx = None
cursor = None


def conectarse():
    global cnx, cursor  # Usamos global para modificar las variables fuera de la función
    try:
        print('Conectando a MySQL...')

        # Establecer conexión
        cnx = pymysql.connect(
            user='root',
            password='rootpassword',
            host='127.0.0.1',
            database='obligatorio2024'
        )

        print('Conexión establecida')

        # Crear un cursor para interactuar con la base de datos
        cursor = cnx.cursor()

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")


# Llamar a la función para conectarse
conectarse()

if cnx is not None and cursor is not None:
    try:
        # Ejecutar una consulta
        print('Ejecutando la consulta...')
        cursor.execute("SELECT * FROM login")
        print('Consulta ejecutada.')

        # Recuperar los resultados
        resultados = cursor.fetchall()

        # Iterar sobre los resultados e imprimirlos
        for el in resultados:
            print(el)

        # Hacer commit si es necesario (solo si has realizado cambios en la BD)
        cnx.commit()

    except Exception as e:
        print(f"Error durante la consulta: {e}")

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        cnx.close()
        print('Conexión cerrada')
else:
    print('No se pudo establecer la conexión.')
