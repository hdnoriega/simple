import os
import json
from conf.PermisosWeb import datos

#Consulta de permisos habilitados por CUIT

def consultaPermisosWeb(cuit):
    for p in datos:
        try:
            con = p[cuit]
        except Exception:
            con = "NoExiste"
            pass

    return con


