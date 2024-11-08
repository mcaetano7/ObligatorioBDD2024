import pymysql

def conectarse(user):
    try:
        print('Conectando a MySQL...')
        if user == 'administrador':
            cnx = pymysql.connect(
                user=user,
                password='adminpass',
                host='127.0.0.1',
                database='obligatorio2024'
            )
        elif user == 'instructor':
            cnx = pymysql.connect(
                user=user,
                password='instructorpass',
                host='127.0.0.1',
                database='obligatorio2024'
            )
        elif user == 'alumno':
            cnx = pymysql.connect(
                user=user,
                password='alumnopass',
                host='127.0.0.1',
                database='obligatorio2024'
            )
        print('Conexión establecida')
        cursor = cnx.cursor()
        return cnx, cursor
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None, None