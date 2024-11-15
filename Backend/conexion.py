import pymysql

def conectarse(usuario):
    try:
        if usuario == 'administrador':
            cnx = pymysql.connect(
                user=usuario,
                password='adminpass',
                host='127.0.0.1',
                database='obligatorio2024'
            )
        elif usuario == 'instructor':
            cnx = pymysql.connect(
                user=usuario,
                password='instructorpass',
                host='127.0.0.1',
                database='obligatorio2024'
            )
        elif usuario == 'alumno':
            cnx = pymysql.connect(
                user = usuario,
                password = 'alumnopass',
                host = '127.0.0.1',
                database = 'obligatorio2024'
            )
        cursor = cnx.cursor()
        return cnx, cursor
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None