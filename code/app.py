# BASE
import json
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_swagger_ui import get_swaggerui_blueprint


#MODULOS1

#from procedimientos.Usuarios import usuarios

#MODULOS2
from web.ConsultaAD import consultaAD
from web.ConsultaPermisosWeb import consultaPermisosWeb
from utils.GenerarToken import generarToken
from ldapsade.ConsultaLDAP import consultaLDAP
from ldapsade.UpdateEmployee import updateEmployee
from web.permisos.ModuloPermisos import moduloPermisos
from web.permisos.ListarPermisos import listarPermisos
from web.permisos.BuscarModifUsuario import buscarModifUsuario
from bbdd.ConsultaDBOld import consultaDB
from web.migraciones.ConsultaReparticiones import consultaReparticiones

app = Flask(__name__)
api = Api(app)


#SWAGGER


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "APES - Catálogo de servicios"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)


#CLASES


# #EU
# class Usuarios(Resource):
#     def get(self):        
#         r = usuarios(datos)
#         return r, 200
#         pass

# class Sectores(Resource):
#     def get(self):
#         pass

# class Reparticiones(Resource):
#     def get(self):
#         pass

# class Migraciones(Resource):
#     def get(self):
#         pass    

# #GEDO

# class Comunicacion_Enviada(Resource):
#     def get(self):
#         pass

# class Comunicacion_Bandeja(Resource):
#     def get(self):
#         pass

# class Gedo_Documento(Resource):
#     def get(self):
#         pass

# class Gedo_Acto_Administrativo(Resource):
#     def get(self):
#         pass    

# class Gedo_Tipo_Documento(Resource):
#     def get(self):
#         pass

# class Gedo_Bandeja(Resource):
#     def get(self):
#         pass

# #EE

# class Expediente(Resource):
#     def get(self):
#         pass

# class Expediente_Documento(Resource):
#     def get(self):
#         pass

# class Expediente_Historial(Resource):
#     def get(self):
#         pass

# class Expediente_Usuario_Asignado(Resource):
#     def get(self):
#         pass

# class Expediente_Buzon_Grupal(Resource):
#     def get(self):
#         pass

# #LOYS

# class Loys_Expediente(Resource):
#     def get(self):
#         pass

# class Loys_Procedimiento(Resource):
#     def get(self):
#         pass

# class Loys_Actividad(Resource):
#     def get(self):
#         pass

# class Loys_Taskinstance(Resource):
#     def get(self):
#         pass

# class Loys_Taskactorpool(Resource):
#     def get(self):
#         pass

# class Loys_Pooledactor(Resource):
#     def get(self):
#         pass

# class Loys_Datos_Postulante(Resource):
#     def get(self):
#         pass


##########################

class ConsultaAD(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        r = consultaAD(json_data)
        return r, 200

class ConsultaPermisosWeb(Resource):
    def get(self,cuit,):
        r = consultaPermisosWeb(cuit)
        return r, 200

class GenerarToken(Resource):
    def get(self):
        r = generarToken()
        return r, 200

# Permisos SADE

class ConsultaLDAP(Resource):
    def get(self, entorno, usuario, atributo):       
        r = consultaLDAP(entorno, usuario, atributo)
        return r, 200

class ModulosPermisos(Resource):
    def get(self, cuit):
        r = moduloPermisos(cuit)
        return r, 200

class BuscarModifUsuario(Resource):
    def get(self, usuario, entorno):
        r = buscarModifUsuario(usuario, entorno)
        return r, 200

class ListarPermisos(Resource):
    def get(self, entorno):       
        r = listarPermisos(entorno)
        return r, 200

class UpdatePermisoLDAP(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        r = updateEmployee(json.dumps(json_data))
        return r, 200

## BBDD

class ConsultaDB(Resource):
    def get(self, entorno, query):
        if id == "0":
            return "No se ingresó una consulta"
        r = consultaDB(entorno, query)
        return r, 200



## MIGRACIONES

##falta en swagger
class ConsultaReparticiones(Resource):
    def get(self, entorno):       
        r = consultaReparticiones(entorno)
        return r, 200

# class InsertLDAP(Resource):
#     def get(self, entorno, usuario):       
#         quote9 = insertLDAP(entorno, usuario)
#         return quote9, 200

# class DeleteLDAP(Resource):
#     def get(self, entorno, usuario):       
#         quote10 = deleteLDAP(entorno, usuario)
#         return quote10, 200

# class UpdateLDAP(Resource):
#     def get(self, entorno, usuario, accion, atributo, valor):       
#         quote11 = updateLDAP(entorno, usuario, accion, atributo, valor)
#         return quote11, 200





        
##########################

api.add_resource(ConsultaAD, "/consultaad", "/consultaad/", "/consultaad/")
api.add_resource(ConsultaPermisosWeb, "/permisosweb", "/permisosweb/", "/permisosweb/<string:cuit>")
api.add_resource(GenerarToken, "/token", "/token/", "/token/")
api.add_resource(ConsultaLDAP, "/consultaldap", "/consultaldap/", "/consultaldap/<string:entorno>, <string:usuario>, <string:atributo>")
# api.add_resource(InsertLDAP, "/insertldap", "/insertldap/", "/insertldap/<string:entorno>, <string:usuario>")
# api.add_resource(DeleteLDAP, "/deleteldap", "/deleteldap/", "/deleteldap/<string:entorno>, <string:usuario>")
# api.add_resource(UpdateLDAP, "/updateldap", "/updateldap/", "/updateldap/<string:entorno>, <string:usuario>, <string:accion>, <string:atributo>, <string:valor>")


api.add_resource(ConsultaDB, "/consultadb", "/consultadb/", "/consultadb/<string:entorno>, <string:query>")
#HERRAMIENTAS
api.add_resource(ModulosPermisos, "/modulopermisos", "/modulopermisos/", "/modulopermisos/<string:cuit>")
api.add_resource(BuscarModifUsuario, "/buscarpermisos", "/buscarpermisos/", "/buscarpermisos/<string:usuario>,<string:entorno>")
api.add_resource(ListarPermisos, "/listarpermisos", "/listarpermisos/", "/listarpermisos/<string:entorno>")
api.add_resource(UpdatePermisoLDAP, "/updatepermiso", "/updatepermiso/", "/updatepermiso/")
api.add_resource(ConsultaReparticiones, "/consultareparticiones", "/consultareparticiones/", "/consultareparticiones/<string:entorno>")



if __name__ == '__main__':
    app.run(debug=True, host = '10.9.10.151', port = 8080)

        
