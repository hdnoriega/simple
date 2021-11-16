import ldap

#CONSULTA AL ACTIVE DIRECTORY CON USUARIO Y CONTRASEÑA


def consultaAD(datita):
    conn = ldap.initialize('ldap://ad.buenosaires.gob.ar')
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    try:
        r = conn.simple_bind_s('BUENOSAIRES\\'+datita["cuit"], datita["password"])
    except Exception:
        return "NOK"
        pass

    if str(r) == "(97, [], 1, [])":
        return "OK"
    else:
        return "NOK"


# datos = {"usuario":"20335736479",
#          "pass":"s102Pifa"
# }


#print(consultaAD(datos))
