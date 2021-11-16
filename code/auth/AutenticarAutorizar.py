from auth.Autenticar import autenticar
from auth.Autorizar import autorizar
from utils import Log
#from conf.Constantes import auth_fallida

def autenticar_autorizar(**datos):
    if autenticar(datos["token"]):
        pass
    else:
        return False, 403
        #return auth_fallida, 403
    
    q = autorizar(datos["token"], datos["id_servicio"], datos["grupo"])
    #print(q)
    
    if q[0]:
        return q
    else:
        Log.error(q[1])
        return q
