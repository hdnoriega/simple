from auth.Autenticar import autenticar
from procedimientos.Usuarios import usuarios
from procedimientos.Sectores import sectores
from procedimientos.Reparticiones import reparticiones
from procedimientos.Gedo import gedo
import utils.Log
from conf import Consultas
import requests
from web.ConsultaPermisosWeb import consultaPermisosWeb
from ldapsade.ConsultaLDAP import consultaLDAP
from web.permisos.ModuloPermisos import moduloPermisos
from web.migraciones.ConsultaReparticiones import consultaReparticiones

def testAutenticar():
    coso = "12345678"
    print(autenticar(coso))
    #autenticar(coso)



def testUsuarios():
    #Test token no cargado
    #data = {"token":"12345678","id_servicio":22}
    #print(usuarios(**data))
    
    #Test id_servicio no existe
    data = {"token":"12345678","id_servicio":22, "tipo": "156", "anio":"2021"}
    print(gedo(**data))
    

def post(data):
    r = requests.post("http://localhost:8080/consultaad/", json = data)
    print(r.text)

data = {
    "usuario":"20335736479",
    "pass":"s102Pifa"
    }

#post(data)
#testAutenticar()

#testUsuarios()

#testLogging()

#print(consultaLDAP("hml", "HNORIEGA7", "employeeType"))
#print(moduloPermisos("20335736479"))


print(consultaReparticiones("prd"))