from ldap3 import Server, Connection, ALL, ObjectDef, AttrDef, Reader, Writer, Entry, Attribute, OperationalAttribute
import json
from conf.LDAP import datos

def consultaLDAP(entorno, usuario, atributo):

    try:

        con = datos[entorno]
        usr = datos[entorno+"usr"]
        pw =  datos[entorno+"pw"]

        server = Server(con, get_info=ALL)
        conn = Connection(server, usr, pw, auto_bind=True)
        conn.search("cn="+usuario+",ou=sade,dc=gob,dc=ar", "(objectclass=person)", attributes=atributo)

        a = conn.entries[0]

        res = a.entry_to_json()

        return json.loads(str(res))

    except Exception:
        return "error"

    
