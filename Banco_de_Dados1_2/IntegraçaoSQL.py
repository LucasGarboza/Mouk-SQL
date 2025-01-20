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

# Função que tenta criar uma nova tabela com base nos parâmetros passados
def NovaTabela(conexao, tabela):
    try:
        conect = conexao.cursor()
        conect.execute(tabela)
        print("Tabela criada com sucesso!")
    except Error as erro:
        print(erro)

# Função que tenta inserir novos dados com base nos parâmetros passados
def NovosDados(conexao, dados):
    try:
        conect = conexao.cursor()
        conect.execute(dados)
        conexao.commit()
        print("Dados adicionados com sucesso!")
    except Error as erro:
        print(erro)

# Modelo de nova tabela:
# tabela = """CREATE TABLE MOUK_USUARIOS(
#                 ID_USUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
#                 NOME VARCHAR(30),
#                 ANO_NASCIMENTO VARCHAR(10),
#                 EMAIL VARCHAR (30),
#                 CONTATO VARCHAR(15),
#                 CARGO VARCHAR(20),
#                 CPF VARCHAR(15)
#                 );"""

# Modelo de novos dados
# Novos_Dados = ("INSERT INTO MOUK_USUARIOS"
#                "(NOME, ANO_NASCIMENTO, EMAIL, CONTATO, CARGO, CPF)"
#                f"VALUES('{nome}', '{Ano_Nascimento}', '{email}', '{contato}', '{cargo}', '{cpf}')")

# Chama a função de conexão mantendo a integração entre o Python e o SQL
conectar = ConexaoSql()


