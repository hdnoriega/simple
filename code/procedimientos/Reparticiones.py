from auth.AutenticarAutorizar import autenticar_autorizar
from utils import Log, DbAJson
from conf import Constantes, Consultas
from bbdd import ConsultaDB, Parametros

#REPARTICIONES

# La consulta de usuarios admite los siguientes métodos: Consulta por codigo, 
# consulta por id, por repa padre y cantidad por repa padre. 



def reparticiones(**datos):

    datos["grupo"] = "reparticiones"
    q = autenticar_autorizar(**datos)

    if q[0]:
        return eval(q[1]+"(**datos)")
    else:
        return q

def consultaPorCodigo(**datos):

    args = []
    args.append(datos["reparticion"])

    lista_columnas = [Constantes.REPARTICION_ID_REPARTICION, Constantes.REPARTICION_CODIGO_REPARTICION, Constantes.REPARTICION_NOMBRE_REPARTICION, Constantes.REPARTICION_REP_PADRE]
    query = Parametros.agregar(Consultas.REPARTICION, Constantes.REPARTICION_CODIGO_REPARTICION)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaPorRepaPadre(**datos):

    args = []
    args.append(datos["id_repa_padre"])

    lista_columnas = [Constantes.REPARTICION_ID_REPARTICION, Constantes.REPARTICION_CODIGO_REPARTICION, Constantes.REPARTICION_NOMBRE_REPARTICION, Constantes.REPARTICION_REP_PADRE]
    query = Parametros.agregar(Consultas.REPARTICION, Constantes.REPARTICION_REP_PADRE)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaPorRepaPadre_Q(**datos):
    
    args = []
    args.append(datos["id_repa_padre"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.REPARTICION_Q, Constantes.REPARTICION_REP_PADRE)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaPorId(**datos):

    args = []
    args.append(datos["id_reparticion"])

    lista_columnas = [Constantes.REPARTICION_ID_REPARTICION, Constantes.REPARTICION_CODIGO_REPARTICION, Constantes.REPARTICION_NOMBRE_REPARTICION, Constantes.REPARTICION_REP_PADRE]
    query = Parametros.agregar(Consultas.REPARTICION, Constantes.REPARTICION_ID_REPARTICION)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q