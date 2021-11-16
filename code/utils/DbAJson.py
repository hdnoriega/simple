import json

"""
Esta función recibe un objeto Cursor devuelto por ConsultaDB y un array con los nombres de columna correspondientes, en orden
"""

def aJson(datos, lista_columnas):
    
    lista = []
    lista_anidada = []
    lista.append(lista_columnas)
    
    for i in datos:
        for j in i:
            lista_anidada.append(j)

        lista.append(lista_anidada)
        lista_anidada = []
    
    lista.pop
    
    return json.dumps(lista, sort_keys=True, default=str) #indent=4
    