from funciones import *

correo = None

inicio_sesion()
if(encontrar_rol(correo) == 'alumno'):
    menu_alumno()
#elif(encontrar_rol(correo) == 'instructor'):
    #menu_instructor()
