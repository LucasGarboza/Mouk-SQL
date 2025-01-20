# Importa a biblioteca ctk com todas as funções
from customtkinter import *
# Importa as funções de inserir novos dados e conexão do módulo de integração Python/SQL
from Banco_de_Dados.Banco_de_Dados1_2.IntegraçaoSQL import NovosDados, conectar

# Nome da Variável/Janela
janela = CTk()

# Aplicação em classe
class Mouk:
    # Mantém o programa funcionando de forma ordenada
    def __init__(self):
        self.janela = janela
        self.config_tela()
        self.frame_opcoes()
        self.OpcaoListar_Usuarios()
        self.OpcaoCadastrar_Usuarios()
        self.encerrar()
        self.versao()
        self.janela.mainloop()

    # Simples função para encerrar o programa
    def encerrar(self):
        self.janela.quit()

    # Configurações da janela com o customtkinter
    def config_tela(self):
        self.janela.config(background='#363636')  # Cor de fundo
        self.janela.title('Mouk - Banco de Dados')  # Título
        self.janela.geometry('700x500')  # Dimensões x | y

    # Configurações do Frame para as opções laterais a esquerda
    def frame_opcoes(self):
        self.Frame1 = CTkFrame(self.janela,
                               corner_radius=0,
                               fg_color='grey15').place(relx=0, rely=0, relwidth=0.25, relheight=1)

        # Botao 'Cadastrar Usuário'
        BotaoCadastrarUsuario = CTkButton(self.Frame1,
                                   text='CADASTRAR USUÁRIO',
                                   font=("Arial", 11, "bold"),
                                   text_color='white',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   corner_radius=0,
                                   command=self.OpcaoCadastrar_Usuarios).place(relx=0.001, rely=0, relwidth=0.25, relheight=0.08)

        # Botão 'Usuários cadastrados'
        BotaoUsuarios = CTkButton(self.Frame1,
                                  text='USUÁRIOS CADASTRADOS',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='#228B22',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.OpcaoListar_Usuarios).place(relx=0.001, rely=0.085, relwidth=0.25, relheight=0.08)

        # Botão para finalizar a janela
        BotaoEncerrar = CTkButton(self.Frame1,
                                  text='FINALIZAR',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='#B22222',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.encerrar).place(relx=0.001, rely=0.925, relwidth=0.25, relheight=0.08)

    # Configurações do frame com as funcionalidades para cadastrar um usuário
    def OpcaoCadastrar_Usuarios(self):
        self.OpcaoCadastrar = CTkFrame(janela, fg_color='grey18', corner_radius=0)
        self.OpcaoCadastrar.place(relx=0.251, rely=0, relwidth=0.75, relheight=1)

        # Realiza a coleta e verificação e validação dos dados e os cadastra no banco de dados
        def cadastrar():
            # nome = CxTextoNome.get()
            AnoNascimento = CxTexToAnoNascimento.get()
            cpf = CxTexToCpf.get()
            email = CxTexToEmail.get()
            cargo = CxTexToCargo.get()
            contato = CxTexToContato.get()
            nome = CxTextoNome.get()

            # Verifica se algum campo está vazio e retorna uma mensagem de erro
            if nome == '' or AnoNascimento == '' or cpf == '' or email == '' or cargo == '' or contato == '':
                TextoCadastrado = CTkLabel(self.OpcaoCadastrar,
                                           text=f'Por favor insira todos os\n'
                                                f'dados para continuar!',
                                           font=("Arial", 16, "bold"),
                                           text_color='red').place(relx=0.1, rely=0.53, relwidth=0.8, relheight=0.09)
            else:
                try:
                    # # Tenta Cadastrar os dados em arquivo de texto (Versão antiga usando bloco de texto)
                    # with open('cadastros.txt', 'a+', encoding='utf-8') as arquivo:
                    #     arquivo.writelines(f'{nome};{AnoNascimento}\n')

                    # Comando que insere novos dados usando as variaveis correspondentes
                    Novos_Dados = ("INSERT INTO MOUK_USUARIOS"
                                   "(NOME, ANO_NASCIMENTO, EMAIL, CONTATO, CARGO, CPF)"
                                   f"VALUES('{nome}', '{AnoNascimento}', '{email}', '{contato}', '{cargo}', '{cpf}')")

                    # Função que tenta inserir novos dados com base nos parâmetros passados
                    NovosDados(conectar, Novos_Dados)
                except:
                    # Retorna mensagem de erro caso a inserção de dados não funcione
                    print(f'Erro no cadastro')
                finally:
                    # Exibe texto confirmando o cadastro
                    TextoCadastrado = CTkLabel(self.OpcaoCadastrar,
                                                 text=f'Usuário {nome[1]} cadastrado com sucesso!',
                                                 font=("Arial", 16, "bold"),
                                                 text_color='#228B22')
                    TextoCadastrado.place(relx=0.1, rely=0.53, relwidth=0.8, relheight=0.09)
                    # Deleta todos os dados adicionados na janela para um novo cadastro
                    CxTextoNome.delete(0, END)
                    CxTexToAnoNascimento.delete(0, END)
                    CxTexToCargo.delete(0, END)
                    CxTexToContato.delete(0, END)
                    CxTexToCpf.delete(0, END)
                    CxTexToEmail.delete(0, END)

        # Caixa de texto 'Informe os dados'
        TextoInformeDados = CTkLabel(self.OpcaoCadastrar,
                                     text='Informe os dados abaixo:',
                                     font=("Arial", 11, "bold"),
                                     text_color='white').place(relx=0.15, rely=0.02, relwidth=0.275, relheight=0.1)

        # Caixa de texto para o usuário inserir seu nome
        CxTextoNome = CTkEntry(self.OpcaoCadastrar,
                               placeholder_text='Nome Completo')
        CxTextoNome.place(relx=0.15, rely=0.1, relwidth=0.4, relheight=0.1)

        # Caixa de texto para o usuário inserir o ano de nascimento
        CxTexToAnoNascimento = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='Ano de Nascimento')
        CxTexToAnoNascimento.place(relx=0.56, rely=0.1, relwidth=0.3, relheight=0.1)

        # Caixa de texto para o usuário inserir seu e-mail
        CxTexToEmail = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='E-mail')
        CxTexToEmail.place(relx=0.15, rely=0.21, relwidth=0.45, relheight=0.1)

        # Caixa de texto para o usuário inserir seu cpf
        CxTexToCpf = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='CPF: 000.000.000-00')
        CxTexToCpf.place(relx=0.15, rely=0.32, relwidth=0.3, relheight=0.1)

        # Caixa de texto para o usuário inserir o contato de telefone
        CxTexToContato = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='(00) 0 0000-0000')
        CxTexToContato.place(relx=0.61, rely=0.21, relwidth=0.25, relheight=0.1)

        # Caixa de texto para o usuário inserir seu cargo
        CxTexToCargo = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='Cargo')
        CxTexToCargo.place(relx=0.46, rely=0.32, relwidth=0.4, relheight=0.1)

        # Botão Cadastrar
        BotaoCadastrar = CTkButton(self.OpcaoCadastrar,
                                   text='CADASTRAR',
                                   font=("Arial", 11, "bold"),
                                   text_color='#DCDCDC',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   command=cadastrar).place(relx=0.15, rely=0.43, relwidth=0.71, relheight=0.09)

    # Configurações do frame com as funcionalidades para listar usuários cadastrados
    def OpcaoListar_Usuarios(self):
        self.OpcaoListar = CTkFrame(self.janela, fg_color='grey18')
        self.OpcaoListar.place(relx=0.251, rely=0, relwidth=0.75, relheight=1)

        def listar():
            # Tenta procurar por usuários cadastrados
            try:
                with open('cadastros.txt', 'rt') as texto:
                    u = 0.3
                    # Exibe cada usuário cadastrado por linha
                    for linha in texto:
                        dado = linha.split(';')
                        TextoCadastrado = CTkLabel(self.OpcaoListar,
                                               text=f'{dado[0]:<25} {dado[1]:>5}',
                                               font=("Arial", 16, "bold"),
                                               text_color='#228B22')
                        TextoCadastrado.place(relx=0.28, rely=u, relwidth=0.5, relheight=0.1)
                        u += 0.05
            except:
                # Exibe texto informando não ter localizado nenhum usuário cadastrado
                TextoCadastrado = CTkLabel(self.OpcaoListar,
                                           text='Nenhum usuário cadastrado!',
                                           font=("Arial", 16, "bold"),
                                           text_color='red')
                TextoCadastrado.place(relx=0.26, rely=0.3, relwidth=0.5, relheight=0.1)

        # Botão para listar os usuários cadastrados
        BotaoListar = CTkButton(self.OpcaoListar,
                                   text='Listar',
                                   font=("Arial", 11, "bold"),
                                   text_color='#DCDCDC',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   command=listar).place(relx=0.25, rely=0.1, relwidth=0.51, relheight=0.09)

    # Exibe a versão atual do programa (ainda apenas um texto sem atualização automatica)
    def versao(self):
        Versao = CTkLabel(self.Frame1,
                          text='V 1.1',
                          font=('Arial',10,'bold'),
                          text_color='#228B22',
                          fg_color='grey15').place(relx=0.102, rely=0.89, relwidth=0.05, relheight=0.03)

# Mantém o programa em loop
Mouk()