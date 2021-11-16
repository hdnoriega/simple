from conf.Permisos import permisos
from conf.IdPermisos import id_permisos
from utils import Log

"""
Autorizar

Autorizar recibe tres parámetros, el token, el id del servicio que se intenta consumir y la categoría de dicho servicio

Se valida que el token tenga permiso para utilizar este servicio, que el servicio exista y se devuelve el nombre de la función a utilizar

datos[0] es el token
datos[1] es el id del servicio
datos[2] es el grupo de servicios

"""

def autorizar(*datos):

    if not datos[0] and datos[1] and datos[2]:
        return False, "Uno o varios parámetros son nulos"

    existe_token = False
    existe_grupo = False
    existe_permiso = False
    permiso_habilitado = False
        
    #Verifico que el token esté cargado en el archivo de permisos del usuario
    for i in permisos:
        if datos[0] == i:
            existe_token = True

    if not existe_token:
        return False, "El usuario no tiene dado de alta ningún permiso" 

    #Verifico que el grupo de permisos exista

    for i in id_permisos:
        if datos[2] == i:
            existe_grupo = True
    
    if not existe_grupo:
        return False, "El grupo de permisos no existe"

    #Verifico que el permiso exista en el grupo

    for i in id_permisos[datos[2]]:
        if datos[1] == i:
            existe_permiso = True
    
    if not existe_permiso:
        return False, "El id_permiso no existe"
    
    #Verifico que el token tenga asociado el servicio que se intenta utilizar

    for i in permisos[datos[0]]:
        if datos[1] == i:
            permiso_habilitado = True

    if not permiso_habilitado:
        return False, "El usuario no tiene permiso para utilizar este servicio" 

    #Devuelvo el nombre del servicio a utilizar
    
    if existe_token and permiso_habilitado and existe_permiso:
        Log.info("Autorizado: Token: %s, grupo servicio: %s, código servicio: %s, nombre servicio: %s" % (datos[0], datos[2], datos[1], id_permisos[datos[2]][datos[1]]))
        return True, id_permisos[datos[2]][datos[1]]
