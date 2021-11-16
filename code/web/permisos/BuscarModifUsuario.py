import json
from web.permisos.ListarPermisos import listarPermisos
from ldapsade.ConsultaLDAP import consultaLDAP

#RECIBE USUARIO Y ENTORNO Y DEVUELVE EL LISTADO DE PERMISOS EXISTENTES EN EL USUARIO

def buscarModifUsuario(usuario, entorno):

    try:

        permisos = listarPermisos(entorno)

        arrayPermisos = "["
        for i in permisos:
            arrayPermisos = arrayPermisos + "{\"seleccionado\":false, \"nombre\": \""+ permisos[i][i+",1"] +"\", \"modulo\":\""+permisos[i][i+",4"]+"\", \"descripcion\":\""+permisos[i][i+",2"]+"\",\"id\":\""+permisos[i][i+",0"]+"\"},"
        
        arrayPermisos = arrayPermisos[:-1]
        arrayPermisos = arrayPermisos+"]"
        arraypermisos2 = json.loads(arrayPermisos)

        permisosUsuario = consultaLDAP(entorno, usuario, "employeeType")

        c = 0
        
        for i in permisosUsuario["attributes"]["employeeType"]:
            c = 0
            for j in arraypermisos2:
                if (j["nombre"] == i):
                    arraypermisos2[c]["seleccionado"] = True
                c = c + 1

        return arraypermisos2

    except Exception:
        return "error"






