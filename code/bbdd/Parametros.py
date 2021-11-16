def agregar(query, valor):
    if query.find("WHERE") != -1:
        query = query + " AND " + valor + " = :valor1"
    else:
        query = query + " WHERE " + valor + " = :valor1"
    return query
            
    