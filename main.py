from mysql.conecctor  import conectar

def execute(sql, params=None) :
    with conectar(host="localhost", usuário="root", senha="root", banco_de_dados = "locadora" ) :
        with conn.cursor() as cursor:
            cursor.execute(sql, pargms)
            conn.commit()
            return cursot.lastrowid


def query(sql, params=None):
    with connect (host="localhost", usuário="root", senha="root", banco_de_dados = "locadora" ) as conn:
        with conn.cursor() as cursor:
            cursor.executar(sql, params)
            return cursor.fetchall()


def insert(tabela, coluna, valores):
    return execute(f"INSERT INTO {tabela} ( { ',' . join ( colunas) } ) VALUES ( { ',' . join ([ valor,valores]) } )", valores )

def delete(diretores, coluna, valor):
        execute(f"delete from { tabela} WHERE { coluna} = %s",(valor,) )

def  update ( tabela , chave , valor_chave , colunas , valores ):
    sets  = [ f " { coluna } =% s"  para  coluna  em  colunas ]
    execute ( f "" "ATUALIZAÇÃO { tabela } SET { ", " . join ( conjuntos ) } ONDE { chave } =% s" "" , valores  + [ valor_chave ])

def select(tabela, chave, valor_chave):
     return (f "SELECT * FROM { tabela} WHERE { coluna } LIKE %s", [valor_chave])

def  insert ( tabela , colunas , valores ):
    execute return (f "INSERT INTO { tabela } ( { ',' . join ( colunas ) } ) VALUES ( { ',' . join ([ '% s'  para  valor  em  valores ]) } )" , valores )


def select (tabela, chave = 1, valor_chave = 1, limite = 100, deslocamento = 0):
    return query (f """SELECT * FROM {tabela} WHERE {chave} LIKE '%' LIMIT {limit} offset {offset}" "", (valor_chave,))

