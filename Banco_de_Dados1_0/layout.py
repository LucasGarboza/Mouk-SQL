from Banco_de_Dados.cores import verde, limpa, azul


def layout():
    print(f'-' * 32)
    print(f'MENU PRINCIPAL'.center(32))
    print(f'-' * 32)
    print(f'{verde}1{limpa} - {azul}Ver pessoas cadastradas{limpa}')
    print(f'{verde}2{limpa} - {azul}Cadastrar nova pessoa{limpa}')
    print(f'{verde}3{limpa} - {azul}Sair do sistema{limpa}')
    print(f'-' * 32)
    return layout