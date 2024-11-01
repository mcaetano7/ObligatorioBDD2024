import pymysql

def conectarse():
    try:
        print('Conectando a MySQL...')
        cnx = pymysql.connect(
            user='root',
            password='rootpassword',
            host='127.0.0.1',
            database='obligatorio2024'
        )
        print('Conexión establecida')
        cursor = cnx.cursor()
        return cnx, cursor
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None