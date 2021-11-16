from conf.BBDD import prd
import cx_Oracle


# Por el momento sólo se programó para que pueda recibir un parámetro adicional de búsqueda, búsquedas más refinadas escapan al propósito original de esta herramienta

def consultaDB(query, *args):
    conn = cx_Oracle.connect(prd, encoding="UTF-8", nencoding="UTF-8")
    cursor = conn.cursor()
    return cursor.execute(query, valor1 = "".join(args[0]))
