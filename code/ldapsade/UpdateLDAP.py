from ldap3 import Server, Connection, ALL, ObjectDef, AttrDef, Reader, Writer, Entry, Attribute, OperationalAttribute
import json
from conf.LDAP import datos

def updateLDAP(entorno, usuario, accion, atributo, valor):

    try:
        con = datos[entorno]
        usr = datos[entorno+"usr"]
        pw =  datos[entorno+"pw"]

        server = Server(con, get_info=ALL)
        conn = Connection(server, usr, pw, auto_bind=True)

        conn.bind()
        conn.modify('cn='+usuario+',ou=sade,dc=gob,dc=ar',{atributo:[(accion, [valor])]})

        res = conn.result
        conn.unbind()

        return res
        
        #accion puede ser MODIFY_ADD, MODIFY_DELETE o MODIFY_REPLACE

    except Exception:
        return "error"