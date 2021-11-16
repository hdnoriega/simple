import pysolr
import json
import ast
from conf.BBDD import SOLR_CORE_GEDO

# pysolr devuelve un diccionario en lugar de un json, intenté pasarlo a json con json.dumps() pero no parece hacer efecto, queda así por el momento
def consultaSolr(core, query):
    salida = ""
    solr = pysolr.Solr(SOLR_CORE_GEDO)
    results = solr.search(query)
    
    for result in results:
        salida = salida + format(result)
    

    #pruebo pasarlo a json
    
    salida2 = ast.literal_eval(salida)
    #salida3 = json.dumps(salida2)

    return salida2

