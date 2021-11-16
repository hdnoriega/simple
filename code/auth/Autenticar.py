from conf.Token import listado
from utils import Log

def autenticar(clave):
    for i in listado:
        if i == clave:
            Log.info("Usuario autorizado %s" % clave)
            return True
        else:
            Log.info("Usuario no autorizado %s" % clave)
            return False

