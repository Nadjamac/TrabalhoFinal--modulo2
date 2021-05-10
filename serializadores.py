def diretores_from_web(**kwargs):
    return {
        "id": kwargs["id"] if kwargs["id"] else "",
        "nome completo": kwargs["nome completo"] if kwargs["nome completo"] else "",
    }

def diretores_from_db(*args):
    return {
        "id": args[0],
        "nome completo": args[1],
    }