import json
from bbdd.ConsultaDBOld import consultaDB


def listarPermisos(entorno):

    try:
        r = consultaDB(entorno, "SELECT * FROM EU_SADE.ADMINSADE_PERMISOS ORDER BY ID ASC")
        return r    

    except Exception:
        return "error"