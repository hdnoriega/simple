from ldap3 import Server, Connection, ALL, ObjectDef, AttrDef, Reader, Writer, Entry, Attribute, OperationalAttribute
import json
from conf.LDAP import datos

def insertLDAP(entorno, usuario):

    try:
        con = datos[entorno]
        usr = datos[entorno+"usr"]
        pw =  datos[entorno+"pw"]

        server = Server(con, get_info=ALL)
        conn = Connection(server, usr, pw, auto_bind=True)
        conn.add('cn='+usuario+',ou=sade,dc=gob,dc=ar', ['inetOrgPerson','organizationalPerson', 'person'], {'sn': usuario})
        res = conn.result
        conn.unbind()

        return res

    except Exception:
        return "error"