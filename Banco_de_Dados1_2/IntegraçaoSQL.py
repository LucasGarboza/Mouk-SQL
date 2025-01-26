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

# Função que desconecta o banco de dados
def Desconectar():
    return conectar.close()

# Função que cria uma nova tabela com base nos parâmetros passados
def NovaTabela(conexao, tabela):
    """
    Comando SQL: "CREATE NEW TABLE NOME_TABELA(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOME VARCHAR(30),
                    EMAIL VARCHAR(30),
                    IDADE VARCHAR(10)
                    );"
    :param conexao:
    :param tabela:
    :return:
    """
    try:
        conect = conexao.cursor()
        conect.execute(tabela)
        print("Tabela criada com sucesso!")

    except Error as erro:
        print(erro)

# Função que cadastra novos dados
def NovosDados(conexao, dados):
    """
    Comando SQL: "INSERT INTO NOME_TABELA
                    (NOME, EMAI, IDADE)
                VALUES ("nome", "email", "idade")"
    :param conexao:
    :param dados:
    :return:
    """
    try:
        conect = conexao.cursor()
        conect.execute(dados)
        conexao.commit()
        print("Novos dados inseridos com sucesso!")
    except Error as erro:
        print(erro)

# Função que deleta dados cadastrados
def DeletaDados(conexao, dados):
    """
    Comando SQL: "DELETE FROM NOME_TABELA WHERE NOME=nome"
    :param conexao:
    :param dados:
    :return:
    """
    try:
        conect = conexao.cursor()
        conect.execute(dados)
        conexao.commit()
        print("Dados deletados com sucesso!")
    except Error as erro:
        print(erro)

# Função que lista todos os cadastros
def ListaDados(conexao, dados):
    conect = conexao.cursor()
    conect.execute(dados)
    lista = conect.fetchall()
    return lista

# Chama a função de conexão
conectar = ConexaoSql()
