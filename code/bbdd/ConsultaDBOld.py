import cx_Oracle
import json
import re
from conf.BBDD import datos

def consultaDB(entorno, query, **kwargs):

    try:
        matriz = {}
        matriz[0,0] = 'None'

        con = datos[entorno]
        
        conn = cx_Oracle.connect(con,encoding="UTF-8", nencoding="UTF-8")
        cursor1 = conn.cursor()
        cursor1.callproc("dbms_output.enable")
        resq = cursor1.execute(query)

        salidajson = "{"

        for row, line in enumerate(resq):
            for col, cell in enumerate(line):
                matriz[row,col] = cell
                texto = str(cell)

                for kw in kwargs:
                    try:
                        if kwargs["clean"] == True:
                            texto = re.sub('[^A-Za-z0-9 ñÑ.áÁéÉíÍóÓúÚ]+', '', texto)
                    except Exception:
                        pass

                texto =  texto.replace('"', '\\"').replace("'", "\\'").replace("{", "\\{").replace("}", "\\}").replace("[","\\[").replace("]", "\\]").replace("\n","\\n")
                if col == 0:
                    salidajson = salidajson + "\""+str(row)+"\":{"
                salidajson = salidajson + "\""+str(row)+","+str(col)+"\":\""+texto+"\","
            salidajson = salidajson[:-1]
            salidajson = salidajson +"},"
        salidajson = salidajson[:-1]
        salidajson = salidajson + "}"

        conn.close()


        return json.loads(salidajson)



    except cx_Oracle.Error as e:
        errorObj, = e.args
        print("Error Code:", errorObj.code)
        print("Error Message:", errorObj.message)
        matriz[0,0] = 'Error'
        return str(matriz)


