

def valida_diretores(id, nome_completo):
    if len(id) == 0:
        return False

    if len(nome_completo) == 0:
        return False

    diretor = get_diretor(id)
    if len(diretor) > 0:
        return False

    return True