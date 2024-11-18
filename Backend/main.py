from Backend.equipamiento import obtener_equipamientos
from inicio_sesion import *
from menu_admin import menu_admin
from menu_alumno import menu_alumno
from menu_instructor import menu_instructor
from funciones import obtener_rol

while True:
    correo = inicio_sesion()
    if correo is None:
        break
    else:
        if obtener_rol(correo) == 'administrador':
            menu_admin()
        elif obtener_rol(correo) == 'instructor':
            menu_instructor(correo)
        elif obtener_rol(correo) == 'alumno':
            menu_alumno(correo)

