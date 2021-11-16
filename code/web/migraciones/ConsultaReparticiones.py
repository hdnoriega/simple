import json
from bbdd.ConsultaDBOld import consultaDB


def consultaReparticiones(entorno):

    try:
        r = consultaDB(entorno, "SELECT CODIGO_REPARTICION, NOMBRE_REPARTICION FROM TRACK_SADE.SADE_REPARTICION") #WHERE CODIGO_REPARTICION LIKE 'DGG%
        
        lista = []

        for i in r:
            v = ""
            for j in r[i]:
                v = v + r[i][j] + "-"
            v = v[:-1]
            lista.append(v)

        return lista    

    except Exception:
        return "error"

