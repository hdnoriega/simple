from auth.AutenticarAutorizar import autenticar_autorizar
from utils import Log, DbAJson
from conf import Constantes, Consultas
from bbdd import ConsultaDB, Parametros

#USUARIOS

# La consulta de usuarios admite los siguientes métodos: Consulta por usuario, 
# consulta por ID_SECTOR_INTERNO. Ambos pueden devolver tanto los datos como 
# la cantidad de registros encontrados (q)


def gedo(**datos):

    datos["grupo"] = "gedo"
    q = autenticar_autorizar(**datos)
    #print(q)

    if q[0]:
        return eval(q[1]+"(**datos)")
    else:
        return q

def consultaCcooEnviada(**datos):

    args = []
    args.append(datos["usuario"])

    lista_columnas = [Constantes.GEDO_CCOO_ENVIADA_FECHA, Constantes.GEDO_CCOO_ENVIADA_USUARIO, Constantes.GEDO_CCOO_ENVIADA_ID_DOCUMENTO]
    query = Parametros.agregar(Consultas.COMUNICACION_ENVIADA, Constantes.GEDO_CCOO_ENVIADA_USUARIO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaCcooEnviada_Q(**datos):
    args = []
    args.append(datos["usuario"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.COMUNICACION_ENVIADA_Q, Constantes.GEDO_CCOO_ENVIADA_USUARIO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaCcooPorIdDocumento(**datos):

    args = []
    args.append(datos["id_documento"])

    lista_columnas = [Constantes.GEDO_CCOO_ENVIADA_FECHA, Constantes.GEDO_CCOO_ENVIADA_USUARIO, Constantes.GEDO_CCOO_ENVIADA_ID_DOCUMENTO]
    query = Parametros.agregar(Consultas.COMUNICACION_ENVIADA, Constantes.GEDO_CCOO_ENVIADA_ID_DOCUMENTO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaCcooBandeja(**datos):

    args = []
    args.append(datos["usuario"])

    lista_columnas = [Constantes.GEDO_CCOO_BANDEJA_USUARIO, Constantes.GEDO_CCOO_BANDEJA_LEIDO, Constantes.GEDO_CCOO_BANDEJA_ID_COMUNICACION]
    query = Parametros.agregar(Consultas.COMUNICACION_BANDEJA, Constantes.GEDO_CCOO_BANDEJA_USUARIO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaCcooBandeja_Q(**datos):
    args = []
    args.append(datos["usuario"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.COMUNICACION_BANDEJA, Constantes.GEDO_CCOO_BANDEJA_USUARIO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaDocumentoUsuario(**datos):

    args = []
    args.append(datos["usuario"])

    lista_columnas = [Constantes.GEDO_DOCUMENTO_ID, Constantes.GEDO_DOCUMENTO_NUMERO, Constantes.GEDO_DOCUMENTO_ANIO, Constantes.GEDO_DOCUMENTO_REPARTICION, Constantes.GEDO_DOCUMENTO_MOTIVO, Constantes.GEDO_DOCUMENTO_USUARIO, Constantes.GEDO_DOCUMENTO_FECHA_CREACION, Constantes.GEDO_DOCUMENTO_TIPO, Constantes.GEDO_DOCUMENTO_SISTEMA, Constantes.GEDO_DOCUMENTO_RESERVA]
    query = Parametros.agregar(Consultas.DOCUMENTO, Constantes.GEDO_DOCUMENTO_USUARIO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaDocumentoUsuario_Q(**datos):
    args = []
    args.append(datos["usuario"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.DOCUMENTO_Q, Constantes.GEDO_DOCUMENTO_USUARIO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaDocumentoPorId(**datos):

    args = []
    args.append(datos["id_documento"])

    lista_columnas = [Constantes.GEDO_DOCUMENTO_ID, Constantes.GEDO_DOCUMENTO_NUMERO, Constantes.GEDO_DOCUMENTO_ANIO, Constantes.GEDO_DOCUMENTO_REPARTICION, Constantes.GEDO_DOCUMENTO_MOTIVO, Constantes.GEDO_DOCUMENTO_USUARIO, Constantes.GEDO_DOCUMENTO_FECHA_CREACION, Constantes.GEDO_DOCUMENTO_TIPO, Constantes.GEDO_DOCUMENTO_SISTEMA, Constantes.GEDO_DOCUMENTO_RESERVA]
    query = Parametros.agregar(Consultas.DOCUMENTO, Constantes.GEDO_DOCUMENTO_ID)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

### OJO ###
def consultaDocumentoPorReparticion(**datos):

    args = []
    args.append(datos["reparticion"])

    lista_columnas = [Constantes.GEDO_DOCUMENTO_ID, Constantes.GEDO_DOCUMENTO_NUMERO, Constantes.GEDO_DOCUMENTO_ANIO, Constantes.GEDO_DOCUMENTO_REPARTICION, Constantes.GEDO_DOCUMENTO_MOTIVO, Constantes.GEDO_DOCUMENTO_USUARIO, Constantes.GEDO_DOCUMENTO_FECHA_CREACION, Constantes.GEDO_DOCUMENTO_TIPO, Constantes.GEDO_DOCUMENTO_SISTEMA, Constantes.GEDO_DOCUMENTO_RESERVA]
    query = Parametros.agregar(Consultas.DOCUMENTO, Constantes.GEDO_DOCUMENTO_REPARTICION)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

### FIN OJO O_O ###

def consultaDocumentoReparticion_Q(**datos):
    args = []
    args.append(datos["reparticion"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.DOCUMENTO_Q, Constantes.GEDO_DOCUMENTO_REPARTICION)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

    
def consultaDocumentoPorNumero(**datos):

    args = []
    args.append(datos["numero"])

    lista_columnas = [Constantes.GEDO_DOCUMENTO_ID, Constantes.GEDO_DOCUMENTO_NUMERO, Constantes.GEDO_DOCUMENTO_ANIO, Constantes.GEDO_DOCUMENTO_REPARTICION, Constantes.GEDO_DOCUMENTO_MOTIVO, Constantes.GEDO_DOCUMENTO_USUARIO, Constantes.GEDO_DOCUMENTO_FECHA_CREACION, Constantes.GEDO_DOCUMENTO_TIPO, Constantes.GEDO_DOCUMENTO_SISTEMA, Constantes.GEDO_DOCUMENTO_RESERVA]
    query = Parametros.agregar(Consultas.DOCUMENTO, Constantes.GEDO_DOCUMENTO_NUMERO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q

def consultaDocumentoTipo_Q(**datos):
    args = []
    args.append(datos["tipo"])

    lista_columnas = ["Q"]
    query = Parametros.agregar(Consultas.DOCUMENTO_Q, Constantes.GEDO_DOCUMENTO_TIPO)
    q = DbAJson.aJson(ConsultaDB.consultaDB(query, args), lista_columnas)
    return q