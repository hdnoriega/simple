from auth.AutenticarAutorizar import autenticar_autorizar
from utils import Log, DbAJson
from conf import Constantes, Consultas
from bbdd import ConsultaDB, Parametros

#USUARIOS

# La consulta de usuarios admite los siguientes métodos: Consulta por usuario, 
# consulta por ID_SECTOR_INTERNO. Ambos pueden devolver tanto los datos como 
# la cantidad de registros encontrados (q)


def sectores(**datos):

    datos["grupo"] = "sectores"
    q = autenticar_autorizar(**datos)

    if q[0]:
        return eval(q[1]+"(**datos)")
    else:
        return q

def consultaPorReparticion(**datos):

    args = []
    args.append(datos["reparticion"])

    lista_columnas = [Constantes.SECTOR_ID_SECTOR_INTERNO, Constantes.SECTOR_CODIGO_REPARTICION, Constantes.SECTOR_CODIGO_SECTOR_INTERNO, Constantes.SECTOR_NOMBRE_SECTOR_INTERNO]
    query = Parametros.agregar(Consultas.SECTOR_INTERNO, Constantes.SECTOR_CODIGO_REPARTICION)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaPorIdSector(**datos):

    args = []
    args.append(datos["id_sector"])

    lista_columnas = [Constantes.SECTOR_ID_SECTOR_INTERNO, Constantes.SECTOR_CODIGO_REPARTICION, Constantes.SECTOR_CODIGO_SECTOR_INTERNO, Constantes.SECTOR_NOMBRE_SECTOR_INTERNO]
    query = Parametros.agregar(Consultas.SECTOR_INTERNO, Constantes.SECTOR_ID_SECTOR_INTERNO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaPorReparticion_Q(**datos):
    
    args = []
    args.append(datos["reparticion"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.SECTOR_INTERNO_Q, Constantes.SECTOR_CODIGO_REPARTICION)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q
