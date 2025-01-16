# Imports de libs necessárias
from time import sleep
from Banco_de_Dados.Banco_de_Dados1_0 import cadastros1_0
from Banco_de_Dados.Banco_de_Dados1_0.cadastros1_0 import cabeçalho
from Banco_de_Dados import layout
from Banco_de_Dados.cores import vermelho, negrito

# Programa principal
fim = False
while not fim:
    layout.layout()
    resposta = input(f'{negrito}Sua resposta: ')
    cabeçalho('Processando...')
    sleep(1)
    if resposta == '1':
        cadastros1_0.listar()
    elif resposta == '2':
        cadastros1_0.cadastrar()
    elif resposta == '3':
        cabeçalho(f'Saindo...', vermelho)
        fim = True
