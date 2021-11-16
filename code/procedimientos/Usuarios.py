from auth.AutenticarAutorizar import autenticar_autorizar
from utils import Log, DbAJson
from conf import Constantes, Consultas
from bbdd import ConsultaDB, Parametros

#USUARIOS

# La consulta de usuarios admite los siguientes métodos: Consulta por usuario, 
# consulta por ID_SECTOR_INTERNO. Ambos pueden devolver tanto los datos como 
# la cantidad de registros encontrados (q)


def usuarios(**datos):

    datos["grupo"] = "usuarios"
    q = autenticar_autorizar(**datos)

    if q[0]:
        return eval(q[1]+"(**datos)")
    else:
        return q

def consultaPorUsuario(**datos):

    args = []
    args.append(datos["usuario"])

    lista_columnas = [Constantes.USUARIOS_NOMBRE_USUARIO, Constantes.USUARIOS_SECTOR_INTERNO]
    query = Parametros.agregar(Consultas.USUARIOS, Constantes.USUARIOS_NOMBRE_USUARIO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaPorSector(**datos):
    args = []
    args.append(datos["sector"])

    lista_columnas = [Constantes.USUARIOS_NOMBRE_USUARIO, Constantes.USUARIOS_SECTOR_INTERNO]
    query = Parametros.agregar(Consultas.USUARIOS, Constantes.USUARIOS_SECTOR_INTERNO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaPorSector_Q(**datos):
    args = []
    args.append(datos["sector"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.USUARIOS_Q, Constantes.USUARIOS_SECTOR_INTERNO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q
