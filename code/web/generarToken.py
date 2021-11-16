from uuid import uuid4

def generarToken():
    token = uuid4()
    return str(token)
