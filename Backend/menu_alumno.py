import time
from Backend.alumno_clase import alta_alumno_clase, mostrar_alumno_clases
from Backend.alumnos import select_alumno, modificar_alumno, baja_alumno
from Backend.login import baja_login

def menu_alumno(correo):
    while True:
        time.sleep(0.8)
        print("\n<< MENÚ ALUMNO >>")
        print("1. Información personal")
        print("2. Inscribirse")
        print('3. Ver mis clases')
        print('4. Desmatricularse')
        print("5. Cerrar sesión")
        opcion = input("\nElige una opción: ")
        if opcion == "1":
            info_alumno(correo)
        elif opcion == "2":
            alta_alumno_clase(correo)
        elif opcion == "3":
            mostrar_alumno_clases(correo)
        elif opcion == "4":
            baja_alumno(correo)
            baja_login(correo)
            break
        elif opcion == "5":
            print("\nSesión cerrada.")
            time.sleep(0.8)
            break

def info_alumno(correo):
    ci, nombre, apellido, fecha_nacimiento, telefono, correo = select_alumno(correo)
    print(f"\n<< TUS DATOS >> \nCédula: {ci}\nNombre: {nombre}\n"
          f"Apellido: {apellido}\nFecha de nacimiento: {fecha_nacimiento}\n"
          f"Telefono: {telefono}\nCorreo: {correo}")
    if input("\nIngrese 1 si desea modificar sus datos, ingrese otro digito si no: ") == '1':
        modificar_alumno(correo)

