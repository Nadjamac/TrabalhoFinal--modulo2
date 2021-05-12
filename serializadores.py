from flask import Flask, jsonify, request
from main import query, execute, decimal
from modelos import insert_estado, get_estado, insert_usuario, get_usuario, update_usuario, delete_usuario, \
    select_usuarios
from serializadores import estado_from_web, estado_from_db, cidades_from_web, cidades_from_db, usuario_from_web,

usuario_from_db, nome_usuario_from_web,
from validacao import valida_estado, valida_usuario, valida_cidades

app = Flask(__name__)


@app.rota("/ usuarios", métodos=["POST"])
def inserir_usuario("usuario "["id_usuario", "nome_completo", "cpf"], [id_usuario, nome_completo, cpf ]

):
id = id_from_web(**request.json["id"])
nome_completo = nome_completo_from_web(**request.json["nome_completo"])
cpf = cpf_from_web(**request.json["cpf"])

if valida_usuario(**usuario):
    id_usuario = insert_usuario(**usuario)
    usuario_cadastrado = get_usuario(id_usuario)
    return jsonify(usuario_from_db(usuario_cadastrado))
else:
    return jsonify({"erro": "Usuário inválido"})

if valida_id(**id):
    id = insert_id(**id)
    id_cadastrado = get_id(id)
    return jsonify(nome_from_db(id_cadastrado))
else:
    return jsonify({"erro": "id inválido"})

if valida_nome(**nome):
    nome = insert_nome(**nome)
    nome_cadastrado = get_nome(nome)
    return jsonify(nome_from_db(nome_cadastrado))
else:
    return jsonify({"erro": "Nome inválido"})

if valida_cpf(**cpf):
    cpf = insert_cpf(**cpf)
    cpf_cadastrado = get_cpf(cpf)
    return jsonify(cpf_from_db(nome_cadastrado))
else:
    return jsonify({"erro": "cpf inválido"})


@app.rota("/ cidades", métodos=["POST"])
def inserir_cidades("cidade", ["sigla", "nome", ][sigla, nome ]

):
cidades = cidades_from_web(**request.json["cidade"])  # 3 - formata o que vem da internet
sigla = sigla_from_web(**request.json["sigla"])
nome = nome_from_web(**request.json["nome"])

if valida_cidades(**cidades):
    id_cidade = insert_cidade(**cidade)
    cidade_cadastrada = get_cidade(id_cidade)
    return jsonify(usuario_from_db(cidade_cadastrada))
else:
    return jsonify({"erro": "cidade inválida"})

if valida_nome(**nome):
    nome = insert_nome(**nome)
    nome_cadastrado = get_nome(nome)
    return jsonify(nome_from_db)(nome_cadastrado) )
    else:
    return jsonify({"erro": " nome inválido"})

if valida_sigla(**sigla):
    sigla = insert_sigla(**sigla)
    sigla_cadastrada = get_sigla(sigla)
    return jsonify(sigla_from_db)(sigla_cadastrada) )
    else:
    return jsonify({"erro": "sigla inválida"})


@app.rota("/ estado", métodos=["POST"])
def inserir_estado("estados", ["sigla", "nome"], [sigla, nome ]

):
estado = estado_from_web(**request.json["estado"])
sigla = sigla_from_web(**request.json["sigla"])
nome = nome_from_web(**request.json["nome"])

if valida_estado(**estado):
    id_estado = insert_estado(**estado)
    estado_cadastrado = get_estado(id_estado)
    return jsonify(estado_from_db(estado_cadastrado))
else:
    return jsonify({"erro": "estado inválido"})

if valida_sigla(**sigla):
    sigla = insert_sigla(**sigla)
    sigla_cadastrada = get_sigla(sigla)
    return jsonify(sigla_from_db)(sigla_cadastrada) )
    else:
    return jsonify({"erro": "sigla inválida"})

if valida_nome(**nome):
    nome = insert_nome(**nome)
    nome_cadastrado = get_sigla(sigla)
    return jsonify(nome_from_db)(nome_cadastrado) )
    else:
    return jsonify({"erro": " nome inválido"})


@app.rota("/ filmes", métodos=["POST"])
def inserir_filmes("filmes", ["id", "titulo", "ano ", "classificação", "preço", "diretores", "diretores_id",
                   "generos_id"],
                   [id, titulo, ano, classificação, preco, diretores, diretores_id, generos_id ]

):
filmes = filmes_from_web(**request.json["filmes"])
id = id_from_web(**request.json["id"])
titulo = titulo_from_web(**request.json["titulo"])
ano = nome_from_web(**request.json["ano"])
classificacao = classificação_from_web(**request.json["classificação"])
preco = preco_from_web(**request.json["diretores"])
diretores_id = diretores_id(**generos_id)

if valida_id(**filmes):
    filmes = insert_id(**filmes)
    filmes_cadastrado = get_filmes(filmes)
    return jsonify(filmes_from_db(filmes_cadastrado))
else:
    return jsonify({"erro": "filmes inválido"})

if valida_id(**filmes):
    id = insert_id(**filmes)
    id_cadastrado = get_id(id)
    return jsonify(id_from_db(id_cadastrado))
else:
    return jsonify({"erro": "filmes inválido"})

if valida_titulo(**filmes):
    titulo = insert_titulo(**filmes)
    titulo_cadastrada = get_titulo(titulo)
    return jsonify(titulo_from_db)(titulo_cadastrada) )
    else:
    return jsonify({"erro": "titulo inválido"})

if valida_ano(**filmes):
    ano = insert_ano(**filmes)
    ano_cadastrado = get_ano(ano)
    return jsonify(ano_from_db)(ano_cadastrado) )
    else:
    return jsonify({"erro": " ano inválido"})

if valida_classificacao(**filmes):
    classificacao = insert_classificacao(**filmes)
    classificacao_cadastrado = get_classificacao(ano)
    return jsonify(classificacao_from_db)(classificacao_cadastrado) )
    else:
    return jsonify({"erro": " classificacao inválido"})

if valida_preco(**filmes):
    preco = insert_preco(**filmes)
    preco_cadastrado = get_preco(ano)
    return jsonify(preco_from_db)(preco_cadastrado) )
    else:
    return jsonify({"erro": " preco inválido"})

if valida_diretores_id(**filmes):
    diretores_id = insert_diretores_id(**filmes)
    diretores_id_cadastrado = get_diretores_id(diretores_id)
    return jsonify(diretores_id_from_db)(diretores_id_cadastrado) )
    else:
    return jsonify({"erro": " diretores_id inválido"})

if valida_generos_id(**filmes):
    generos_id = insert_generos_id(**filmes)
    generos_id_cadastrado = get_generos_id(generos_id)
    return jsonify(generos_id_from_db)(generos_id_cadastrado) )
    else:
    return jsonify({"erro": "  generos_id inválido"})


@app.rota("/ generos", métodos=["POST"])
def inserir_generos("generos", ["id", "nome"], [id, nome ]

):

if valida_id(**generos):
    id = insert_id(**generos)
    id_cadastrado = get_id(id)
    return jsonify(id_from_db(id_cadastrado))
else:
    return jsonify({"erro": "filmes inválido"})

if valida_nome(**generos):
    nome = insert_nome(**generos)
    nome_cadastrado = get_nome(nome)
    return jsonify(nome_from_db)(nome_cadastrado) )
    else:
    return jsonify({"erro": " nome inválido"})


@app.rota("/ locacoes", métodos=["POST"])
def inserir_locacoes("locacoes", ["id", "data_inicio ", "data_fim", "filmes_id", "usuarios_id"],
                     [id, data_inicio, data_fim, filmes_id, usuarios_id]

):
locacoes = locacoes_from_web(**resquest.json["locacoes"])
id = id_from_web(**request.jon["id"]):
data_inicio = data_inicio_from_web(**request.json["data_inicio"])
data_fim = data_fim_from_web(**request.json["data_fim"])
usuarios_id = usuarios_id_from_web(**request.json["usuarios_id"])

if valida_locacoes(**locacoes):
    locacoes = insert_locacoes(**locacoes)
    locacoes_cadastrado = get_locacoes(locacoes)
    return jsonify(locacoes_from_db(locacoes_cadastrado))
else:
    return jsonify({"erro": "locacoes inválido"})

if valida_id(**locacoes):
    id = insert_id(**locacoes)
    id_cadastrado = get_id(id)
    return jsonify(id_from_db(id_cadastrado))
else:
    return jsonify({"erro": "id inválido"})

if valida_data_inicio(**locacoes):
    data_inicio = insert_data_inicio(**locacoes)
    data_inicio_cadastrado = get_data_inicio(data_inicio)
    return jsonify(data_inicio_from_db(data_inicio))
else:
    return jsonify({"erro": "data_inicio inválido"})

if valida_data_fim(**locacoes):
    data_fim = insert_data_inicio(**locacoes)
    data_fim_cadastrado = get_data_fim(data_fim)
    return jsonify(data_fim_from_db(data_fim))
else:
    return jsonify({"erro": "data_fim inválido"})

if valida_filmes_id(**locacoes):
    filmes_id = insert_filmes_id(**locacoes)
    filmes_id_cadastrado = get_filmes_id(filmes_id)
    return jsonify(filmes_id_from_db(filmes_id))
else:
    return jsonify({"erro": "usuarios_id inválido"})

if valida_usuario_id(**locacoes):
    usuario_id = insert_usuario_id(**locacoes)
    usuario_id_cadastrado = get_usuario_id(usuariO_id)
    return jsonify(usuario_id_from_db(usuario_id))
else:
    return jsonify({"erro": "usuarios_id inválido"})


@app.rota("/ pagamento", métodos=["POST"])
def inserir_pagamento("pagamento", ["id", "status", "cod pagamento", "valor", "data", "locação_id "])
    pagamento_from_web(**request.json
    " pagamento")
    tipo = tipo_from_web(**request.json
    "tipo" )
    status = status_from_web(**request.json
    "status" )
    cod_pagamento = cod_pagamento_from_web(**request.json
    "cod_pagamento" )
    pagamento = pagamento_from_web(**request.json
    "pagamento" )
    valor = valor_from_web(**request.json
    "valor")
    data = data_from_web(**request.json
    "data" )
    locacoes_id = locacoes_id_from_web(**request.json
    "data")


    if valida_pagamento(**pagamentos):
        pagamentos = insert_pagamentos(**pagamentos)
        pagamentos_cadastrado = get_pagamentos(pagamentos)
        return jsonify(pagamentos_from_db(pagamentos_cadastrado))
    else:
        return jsonify({"erro": "pagamentos inválido"})(**pagamentos):

        if valida_id(**id):
            id = insert_id(**id)
            id_cadastrado = get_id(id)
            return jsonify(id_from_db(id_cadastrado))
        else:
            return jsonify({"erro": "id inválido"})(**id):

        if valida_status(**tipo):
            status = insert_status(**status)
            tipo_cadastrado = get_status(status)
            return jsonify(status_from_db(status_cadastrado))
        else:
            return jsonify({"erro": "status inválido"})(**status):

        if valida_cod_pagamento(**cod_pagamento):
             cod_pagamento = insert_cod_pagamento(**cod_pagamento)
             cod_pagamento_cadastrado = get_cod_pagamento(cod_pagamento)
             return jsonify(cod_pagamento_from_db(cod_pagamento_cadastrado))
        else:
             return jsonify({"erro": "tipo inválido"})(**cod_pagamento):

        if valida_data(**cod_data):
             data = insert_data(**cod_data)
             data = get_data(cod_data)
            return jsonify(data_from_db(cod_data))
        else:
            return jsonify({"erro": "data inválido"})(**data):

        if valida_valor(**cod_valor):
           valor_pagamento = insert_valor(**cod_valor)
           valor_cadastrado = get_valor(cod_valor)
            return jsonify(valor_from_db(cod_valor))
        else:
            return jsonify({"erro": "valor inválido"})(**valor):

@app.rota("/ usuarios / <int: id>", métodos=["PUT", "PATCH"])
def alterar_usuario(id):
     usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
      if valida_usuario(**usuario):
         update_usuario(id, **usuario)
         usuario_cadastrado = get_usuario(id)
         return jsonify(usuario_from_db(usuario_cadastrado))
      else:
         return jsonify({"erro": "Usuário inválido"})

                            @app.rota("/ estados / <varchar: sigla,nome>", métodos=["PUT", "PATCH"])
                            def alterar_estado(sigla, nome):
                                estado = estado_from_web(**request.json)  # 3 - formata o que vem da internet
                                if valida_estado(**estado):
                                    update_estado(sigla, nome ** sigla, nome)
                                    estado_cadastrado = get_usuario(sigla, nome)
                                    return jsonify(estado_from_db(estado_cadastrado))
                                else:
                                    return jsonify({"erro": "estado inválido"})


                            @app.rota("/ usuarios / <int: id>", métodos=["DELETE"])
                            def apagar_usuario(id):
                                if:
                                    delete_usuario(id)
                                    return Nenhum
                                else:
                                    return jsonify({"erro": " Usuário possui itens conectados a ele "})

                            @app.rota("/ estado / <varchar: sigla,nome>", métodos=["DELETE"])
                            def apagar_estado(sigla, nome):
                                if:
                                    delete_estado(sigla, nome)
                                    return Nenhum, nenhum
                                else:
                                    return jsonify({"erro": "Usuário possui itens conectados a ele"})

                            @app.rota("/ cidades / <varchar: sigla,nome>", métodos=["DELETE"])
                            def apagar_cidade(sigla, nome):
                                if:
                                    delete_cidade(sigla, nome)
                                    return Nenhum, nenhum
                                else:
                                    return jsonify({"erro": "Usuário possui itens conectados a ele"})

                            @app.rota("/ usuarios", métodos=["GET"])
                            def buscar_usuario():
                                nome_completo = nome_usuario_from_web(**solicitação.args)
                                usuarios = select_usuarios(nome_completo)
                                usuarios_from_db = [usuario_from_db(usuario) para  usuario  em  usuarios]
                                return jsonify(usuarios_from_db)

                            @app.rota("/ estado", métodos=["GET"])
                            def buscar_estado():
                                sigla = sigla_from_web(**solicitação.args)
                                nome = nome_from_web(**solicitação.args)
                                estado = select_estado(sigla, nome)
                                estado_from_db = [estado_from_db(estado) for estado in estados]
                                return jsonify(estado_from_db)



                            __name__ == "__main__":
                            app.executar(host="127.0.0.1", debug=True)

                            @app.route("/usuario/<int:id>", methods=["PUT"])
                            def alterar_usuario(id):
                                pass

                            @app.route("/usuario/<int:id>", methods=["DELETE"])
                            def apagar_usuario(id):
                                pass

                            @app.route("/usuario", methods=["GET"])
                            def listar_usuario():
                                pass

                            if __name__ == "__main__":
                                app.executar(host="127.0.0.1", debug=True)

                            @app.route("/usuario/<int: id >", methods=["PUT"])
                            def alterar_estado(sigla, nome):
                                pass

                            @app.route("/estados/<varchar: sigla, nome >", methods=["DELETE"])
                            def apagar_estado(id):
                                pass

                            @app.route("/estados", methods=["GET"])
                            def listar_estados():
                                pass

                            if __name__ == "__main__":
                                app.executar(host="127.0.0.1", debug=True)


