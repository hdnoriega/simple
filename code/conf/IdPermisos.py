"""

En este archivo se detalla el listado de permisos con su respectivo ID.

"""
id_permisos = {
    "usuarios":{
        1:"consultaPorUsuario",
        2:"consultaPorSector",
        3:"consultaPorSector_Q",
    },
    "sectores":{
        4:"consultaPorReparticion",
        5:"consultaPorReparticion_Q",
        6:"consultaPorIdSector",
    },
    "reparticiones":{
        7:"consultaPorCodigo",
        8:"consultaPorRepaPadre",
        9:"consultaPorRepaPadre_Q",
        10:"consultaPorId",
    },
    "gedo":{
        11:"consultaCcooEnviada",
        12:"consultaCcooEnviada_Q",
        13:"consultaCcooPorIdDocumento",
        14:"consultaCcooBandeja",
        15:"consultaCcooBandeja_Q",
        16:"consultaDocumentoUsuario",
        17:"consultaDocumentoUsuario_Q",
        18:"consultaDocumentoPorId",
        19:"consultaDocumentoPorReparticion",
        20:"consultaDocumentoReparticion_Q",
        21:"consultaDocumentoPorNumero",
        22:"consultaDocumentoTipo_Q",
    },
    }