# Importa a biblioteca do Sqlite3 (SQL)
import sqlite3
from webbrowser import Error


# Função que integra o Python com o SQLite e retorna conexão com o banco de dados
def ConexaoSql():
    local = "C:\\Users\\BLAST INFO E TECH\\Desktop\\Mouk-SQL\\Mouk-SQL\\Banco_de_Dados\\Banco_de_Dados1_2\\Usuarios Cadastrados.db"
    conexao = None
    try:
        conexao = sqlite3.connect(local)
    except sqlite3.Error as erro:
        print(erro)
    finally:
        return conexao

# Função que cria uma nova tabela com base nos parâmetros passados
def NovaTabela(conexao, tabela):
    try:
        conect = conexao.cursor()
        conect.execute(tabela)
        print("Tabela criada com sucesso!")
    except sqlite3.Error as erro:
        print(erro)

# Função que insere novos dados com base nos parâmetros passados
def NovosDados(conexao, dados):
    try:
        conect = conexao.cursor()
        conect.execute(dados)
        conexao.commit()
        print("Novos dados inseridos com sucesso!")
    except sqlite3.Error as erro:
        print(erro)

# Função que deleta dados com base nos parâmetros passados
def DeletaDados(conexao, dados):
    try:
        conect = conexao.cursor()
        conect.execute(dados)
        conexao.commit()
        print("Dados deletados com sucesso!")
    except Error as erro:
        print(erro)

# Chama a função de conexão
conectar = ConexaoSql()
