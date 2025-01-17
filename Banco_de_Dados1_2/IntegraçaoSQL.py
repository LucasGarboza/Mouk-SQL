import sqlite3
from sqlite3 import Error
import os

# Função que tentar integrar o Python com o SQLite e retorna conexão com o banco de dados
def ConexaoSql():
    local = "C:\\Users\\BLAST INFO E TECH\\Desktop\\Mouk-SQL\\Mouk-SQL\\Banco_de_Dados\\Banco_de_Dados1_2\\Usuarios Cadastrados.db"
    conexao = None
    try:
        conexao = sqlite3.connect(local)
    except Error as erro:
        print(erro)
    finally:
        return conexao

def NovaTabela(conexao, tabela):
    try:
        conect = conexao.cursor()
        conect.execute(tabela)
        print("Tabela criada com sucesso!")
    except Error as erro:
        print(erro)

conectar = ConexaoSql()

tabela = """CREATE TABLE USUARIOS(
            ID_USUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME VARCHAR(30),
            IDADE VARCHAR(3)
            );"""

NovaTabela(conectar, tabela)

conectar.close()

