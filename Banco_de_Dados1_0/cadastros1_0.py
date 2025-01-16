from time import sleep
from Banco_de_Dados.cores import verde, negrito, limpa, amarelo, vermelho


def cabeçalho(txt, cor=verde, temp=0.1):
    print(f'{negrito}-' * 32)
    print(f'{cor}{txt:^32}{limpa}')
    print(f'{negrito}-' * 32)
    sleep(temp)


def cadastrar():
    cabeçalho('NOVO CADASTRO')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    cabeçalho('Processando...', temp=0.5)
    if usuarioExiste('cadastros.txt', f'{nome};{idade}'):
        cabeçalho('Usuário já existe!', vermelho)
        sleep(1)
        cabeçalho('Retornando ao menu principal...', temp=1)
    else:
        cabeçalho('Processando...', temp=0.5)
        with open('cadastros.txt', 'a+', encoding='utf-8') as arquivo:
            arquivo.writelines(f'{nome};{idade}\n')
        sleep(0.5)
        cabeçalho('Cadastrado com sucesso!')
        sleep(1)


def listar():
    arquivoExiste('cadastros.txt')
    cabeçalho('LISTA DE CADASTROS')
    print(f'NOME'.ljust(26), f'IDADE'.rjust(5))
    with open('cadastros.txt', 'rt') as texto:
        for linha in texto:
            dado = linha.split(';')
            print(f'{dado[0]:<30}{dado[1]:>2}', end='')
    sleep(3)
    cabeçalho('Retornando ao menu principal...')


def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        arquivo = open(arq, 'w+')
        arquivo.close()
        print(f"{amarelo}Arquivo '{arq}' está vazio, criado com sucesso!{limpa}")


def alterarArquivo(arquivo):
    with open(arquivo, 'rt') as arquivo:
        for linha in arquivo:
            print(linha, end='')
        arquivo.close()


def usuarioExiste(arquivo, usuarioe):
    with open(arquivo, 'rt') as texto:
        for linha in texto:
            dados = linha.split(';')
            users = usuarioe.split(';')
            if dados [0] == users[0] and int(dados[1]) == int(users[1]):
                return True
            else:
                return False