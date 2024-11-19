from conexion import conectarse
from datetime import datetime, timedelta


def obtener_rol(correo):
    cnx, cursor = conectarse('administrador')
    cursor.execute("SELECT descripcion FROM rol JOIN login ON id_rol = id "
                   "WHERE correo = %s", correo)
    result = cursor.fetchone()[0]
    cursor.close()
    cnx.close()
    return result

def obtener_fecha_nacimiento():
    while True:
        fecha_nac = input("Ingrese su fecha de nacimiento en formato DD/MM/AAAA: ")
        try:
            fecha_valida = datetime.strptime(fecha_nac, "%d/%m/%Y")
            fecha_formateada = fecha_valida.strftime("%Y-%m-%d")
            return fecha_formateada
        except ValueError:
            print("Formato inválido. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")

def mostrar_reportes():
    pass

def validar_hora(hora_str):
    try:
        datetime.strptime(hora_str, '%H:%M')
        return True
    except ValueError:
        return False

def coincidencia_turno(turnos, hora_inicio_dt, hora_fin_dt):
    """Función para verificar si el nuevo turno solapa con algún turno existente"""
    for turno in turnos:
        # Convertir los horarios existentes en datetime.time para compararlos
        if isinstance(turno[1], timedelta):
            hora_inicio_existente = (datetime.min + turno[1]).time()
        else:
            hora_inicio_existente = datetime.strptime(str(turno[1]), '%H:%M:%S').time()

        if isinstance(turno[2], timedelta):
            hora_fin_existente = (datetime.min + turno[2]).time()
        else:
            hora_fin_existente = datetime.strptime(str(turno[2]), '%H:%M:%S').time()

        # Comparar si los horarios de inicio y fin son exactamente iguales
        if hora_inicio_dt.time() == hora_inicio_existente and hora_fin_dt.time() == hora_fin_existente:
            return True
    return False