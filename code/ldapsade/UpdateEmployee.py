from ldap3 import Server, Connection, ALL, ObjectDef, AttrDef, Reader, Writer, Entry, Attribute, OperationalAttribute, set_config_parameter
import json
from conf.LDAP import datos
from web.permisos.ListarPermisos import listarPermisos

set_config_parameter('DEFAULT_CLIENT_ENCODING', 'utf-8')

def updateEmployee(valor):

    try:
        valor = json.loads(valor)
        atributo = "employeeType"
        accion = "MODIFY_REPLACE"

        con = datos[valor["entorno"]]
        usr = datos[valor["entorno"]+"usr"]
        pw =  datos[valor["entorno"]+"pw"]

        listapermisos = listarPermisos(valor["entorno"])

        listajson = json.loads(listapermisos.text)
        modificar = []
        for i in listajson:
            for j in valor["permisos"]:
                if listajson[i][i+",0"] == j:
                    modificar.append(listajson[i][i+",1"])

        server = Server(con, get_info=ALL)
        conn = Connection(server, usr, pw, auto_bind=True)

        conn.bind()

        conn.modify('cn='+valor["usuario"]+',ou=sade,dc=gob,dc=ar',{atributo:[(accion, modificar)]})
        res = conn.result

        conn.unbind()

        return res
    
    except Exception:
        return "error"
    #accion puede ser MODIFY_ADD, MODIFY_DELETE o MODIFY_REPLACE

#data = {"usuario":"EVERIS", "entorno":"prd", "permisos":["cosito1", "cosito2","cosito3"]}
#updateEmployeeType(data)
