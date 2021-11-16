from conf.PermisosLDAP import datos

def moduloPermisos(cuit):

    try:
        permisos = datos[cuit]
        return permisos

    except Exception:
        return "-1"




