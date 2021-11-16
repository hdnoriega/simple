import logging
from conf.Constantes import log_file
from datetime import datetime

"""
Utilidad para registrar logs en un archivo de texto.

Para utilizar, importar el módulo y llamar a cada una de las funciones de acuerdo al tipo de log
"""

def error(datos):
    logging.basicConfig(filename=log_file, level=logging.ERROR)
    logging.error(str(datetime.now()) + " " + datos)

def info(datos):
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logging.info(str(datetime.now()) + " " + datos)

def debug(datos):
    logging.basicConfig(filename=log_file, level=logging.DEBUG)
    logging.debug(datos)
