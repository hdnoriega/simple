from uuid import uuid4
import json

def generarToken():
    token = uuid4()
    return str(token)
