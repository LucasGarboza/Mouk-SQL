import sqlite3
from sqlite3 import Error
import os

def ConexaoSql():
    local = "C:\\Users\\BLAST INFO E TECH\\Desktop\\Mouk-SQL\\Usuarios Cadastrados.db"
    conexao = None
    try:
        conexao = sqlite3.connect(local)
    except Error as erro:
        print(erro)
    finally:
        return conexao