from main import insert, select, update, delete, select_bancoDeDados

def insert_diretores( diretores ,  id, nome_completo):
     return insert("diretores",  ["id","nome_completo"])

def update_diretores(diretores ,  id, nome_completo)
    return updade( "diretores", "id" ,id [ "nome_completo"],[nome_completo])

def delete_diretores (id_diretores)]
    delete("diretores","id",id_diretores)

def select_diretores(nome_completo):
    return select_locadora("diretores","nome_completo",nome_completo)

def get_diretores

def insert_filmes( filmes  [titulo, ano , classificaçao , preco  , diretores ]):
    return insert("filmes", ["titulo", "ano","classificacao","preco","diretores"])

def update_filmes ( filmes  [titulo, ano , classificaçao , preco  , diretores)
    return updade("filmes"["titulo", "ano","classificacao","preco","diretores"] titulo, ano , classificaçao , preco  , diretores)

def delete_filmes (id_filme):
    delete ("filmes","id", id_filmes)

def select_filmes( titulo ):
    return select_locadora("filmes",  "titulo",  titulo )

def get_filmes

def insert_generos(generos,id, nome):
    return insert("generos"[ "id", "nome"] )

def update_generos(id, nome):
    update_generos ("generos", "id", id_generos, ["nome"] , [nome] )

def delete_generos(id):
    delete_generos("generos","id", id )

def select_generos(data_inicio,data_fim):
    return select_locadora( "generos " ,"data_inicio","data_fim",data_inicio,data_fim )

def get_generos():


def insert_locacoes (id, data_inicio,data_fim , filmes_id,usuarios_id):
    return insert ("locacoes "[ "id", "data_inicio", "data_fim", "filmes_id", "usuarios_id" ],[id, data_inicio,data_fim , filmes_id,usuarios_id] )

def update_locacoes(id, data_inicio,data_fim , filmes_id,usuarios_id):
    update_locacao("locacoes","id", "data_inicio","data_fim" ,[data_inicio,data_fim ] )

def select_locacoes (id, data_inicio,data_fim ):
    return_select_locacoes("locacoes","id"," data_inicio","data_fim",[ data_inicio,data_fim ])

def delete_locacao(id):
    delete("locacoes","id",id)

def get_locacoes()


def insert_pagamentos (id, status , cod_pagamento, valor, data, locação_id ):
    return insert ("pagamento" ["id","status","cod pagamento", "valor","data","locação_id "])

def update_pagamento(id, status ,locação_id" cod_pagamento, valor, data, locação_id):
    update("pagamento","id","status" ," cod_pagamento", "valor", "data" [id,status , cod_pagamento, valor, data])

def delete_pagamento(id, status ,locação_id" cod_pagamento, valor, data, locação_id):
    update("pagamento",[id," status" ,"locação_id", "cod_pagamento", "valor"," data", "locação_id"],id, status ,locação_id, cod_pagamento, valor, data, locação_id)

def select_pagamento(id,

def insert_usuario(id,nome_completo,cpf)


def update