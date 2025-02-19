# Importa a biblioteca do Sqlite3 (SQL)
from sqlite3 import Error,connect

# Função que integra o Python com o SQLite e retorna conexão com o banco de dados
def ConexaoSql():
    local = "C:\\Users\\BLAST INFO E TECH\\Desktop\\Mouk-SQL\\Mouk-SQL\\Banco_de_Dados\\Banco_de_Dados1_2\\Usuarios Cadastrados.db"
    conexao = None
    try:
        conexao = connect(local)
    except Error as erro:
        print(erro)
    finally:
        return conexao

# Função que cria uma nova tabela com base nos parâmetros passados
def NovaTabela():
    comandoSql = """CREATE TABLE MOUK_USUARIOS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOME VARCHAR(30),
                        EMAIL VARCHAR(30),
                        DATA_NASCIMENTO VARCHAR(10),
                        SENHA VARCHAR(20),
                        CARGO VARCHAR(20),
                        CONTATO VARCHAR(20),
                        CPF VARCHAR(20)
                    );"""
    try:
        conectar = ConexaoSql()
        conect = conectar.cursor()
        conect.execute(comandoSql)
        print("Tabela criada com sucesso!")
        conectar.close()
    except Error as erro:
        print(erro)

# Função que cadastra novos dados
def NovosDados(dados):
    """
    Comando SQL: "INSERT INTO NOME_TABELA
                    (NOME, EMAIl, IDADE)
                VALUES ("nome", "email", "idade")"
    """
    try:
        conectar = ConexaoSql()
        conect = conectar.cursor()
        conect.execute(dados)
        conectar.commit()
        conectar.close()
        print("Novos dados inseridos com sucesso!")
    except Error as erro:
        print(erro)

# Função que deleta dados cadastrados
def DeletaDados(dados):
    """
    Comando SQL: "DELETE FROM NOME_TABELA WHERE NOME=nome"
    """
    try:
        conectar = ConexaoSql()
        conect = conectar.cursor()
        conect.execute(dados)
        conectar.commit()
        conectar.close()
        print("Dados deletados com sucesso!")
    except Error as erro:
        print(erro)

# Função que lista todos os cadastros
def ListaDados(dados):
    conectar = ConexaoSql()
    conect = conectar.cursor()
    conect.execute(dados)
    lista = conect.fetchall()
    conectar.close()
    return lista

# Função que busca apenas os dados solicitados nos cadastros
def BuscaDados():
    pass

# Função que altera apenas os dados solicitados nos cadastros
def AlteraDados():
    pass
