# Importa a biblioteca ctk com todas as funções
from customtkinter import *
# Importa a função treeview do tkinter
from tkinter import ttk
# Importa as funções de inserir novos dados e conexão do módulo de integração Python/SQL
from Banco_de_Dados.Banco_de_Dados1_2.IntegraçaoSQL import NovosDados, conectar, ListaDados

# Nome da Variável/Janela
janela = CTk()

# Aplicação em classe
class Mouk:
    # Mantém o programa funcionando de forma ordenada
    def __init__(self):
        self.janela = janela
        self.config_tela()
        self.frame_opcoes()
        self.OpcaoUsuarios_Cadastrados()
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
        self.janela.geometry('1020x660')  # Dimensões x | y

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
                                   command=self.OpcaoCadastrar_Usuarios).place(relx=0.001, rely=0, relwidth=0.25, relheight=0.083)

        # Botão 'Usuários cadastrados'
        BotaoUsuarios = CTkButton(self.Frame1,
                                  text='USUÁRIOS CADASTRADOS',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='#228B22',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.OpcaoUsuarios_Cadastrados).place(x=0.001, rely=0.085, relwidth=0.25, relheight=0.083)

        # Botão para finalizar a janela
        BotaoEncerrar = CTkButton(self.Frame1,
                                  text='FINALIZAR',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='#B22222',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.encerrar).place(x=0.001, rely=0.925, relwidth=0.25, relheight=0.083)

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
                                                 text=f'Usuário {nome} cadastrado com sucesso!',
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
                                     text_color='white').place(relx=0.075, rely=0.02, relwidth=0.275, relheight=0.1)

        # Caixa de texto para o usuário inserir seu nome
        CxTextoNome = CTkEntry(self.OpcaoCadastrar,
                               placeholder_text='Nome Completo')
        CxTextoNome.place(relx=0.15, rely=0.1, relwidth=0.4, relheight=0.1)

        # Caixa de texto para o usuário inserir o ano de nascimento
        CxTexToAnoNascimento = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='Data de Nascimento')
        CxTexToAnoNascimento.place(relx=0.56, rely=0.1, relwidth=0.3, relheight=0.1)

        # Caixa de texto para o usuário inserir seu e-mail
        CxTexToEmail = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='E-mail')
        CxTexToEmail.place(relx=0.15, rely=0.21, relwidth=0.42, relheight=0.1)

        # Caixa de texto para o usuário inserir seu cpf
        CxTexToCpf = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='CPF: 000.000.000-00')
        CxTexToCpf.place(relx=0.15, rely=0.32, relwidth=0.3, relheight=0.1)

        # Caixa de texto para o usuário inserir o contato de telefone
        CxTexToContato = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='TEL: (00) 0 0000-0000')
        CxTexToContato.place(relx=0.58, rely=0.21, relwidth=0.28, relheight=0.1)

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
    def OpcaoUsuarios_Cadastrados(self):
        self.OpcaoListar = CTkFrame(self.janela, fg_color='grey18')
        self.OpcaoListar.place(relx=0.251, rely=0, relwidth=0.75, relheight=1)

        # Função que lista todos os usuários cadastrados e exibe na relação
        def listar():
            RelacaoUsuarios.delete(*RelacaoUsuarios.get_children())
            comandoSql = "SELECT * FROM MOUK_USUARIOS order by ID_USUARIO"
            relacao = ListaDados(conectar, comandoSql)
            for l in relacao:
                RelacaoUsuarios.insert("", "end", values=l)

        # Botão para listar os usuários cadastrados
        BotaoListar = CTkButton(self.OpcaoListar,
                                   text='LISTAR',
                                   font=("Arial", 11, "bold"),
                                   text_color='#DCDCDC',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   command=listar).place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.09)

        # Botão para buscar usuários cadastrados
        BotaoBuscar = CTkButton(self.OpcaoListar,
                                text='BUSCAR',
                                font=("Arial", 11, "bold"),
                                text_color='#DCDCDC',
                                hover_color='#228B22',
                                fg_color='grey25').place(relx=0.45, rely=0.1, relwidth=0.1, relheight=0.09)

        # Botão para deletar usuários cadastrados
        BotaoDeletar = CTkButton(self.OpcaoListar,
                                text='DELETAR',
                                font=("Arial", 11, "bold"),
                                text_color='#DCDCDC',
                                hover_color='#228B22',
                                fg_color='grey25').place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.09)

        RelacaoUsuarios = ttk.Treeview(self.OpcaoListar, columns=("id", "nome", "data_nascimento", "e-mail",
                                                                  "contato", "cargo", "cpf"), show="headings")

        # Configurações das colunas com a  relação dos usuários
        RelacaoUsuarios.column("id", width=30)
        RelacaoUsuarios.heading("id", text="ID")
        RelacaoUsuarios.column("nome", width=300)
        RelacaoUsuarios.heading("nome", text="NOME")
        RelacaoUsuarios.column("data_nascimento", width=130)
        RelacaoUsuarios.heading("data_nascimento", text="DATA NASCIMENTO")
        RelacaoUsuarios.column("e-mail", width=300)
        RelacaoUsuarios.heading("e-mail", text="E-MAIL")
        RelacaoUsuarios.column("contato", width=100)
        RelacaoUsuarios.heading("contato", text="CONTATO")
        RelacaoUsuarios.column("cargo", width=200)
        RelacaoUsuarios.heading("cargo", text="CARGO")
        RelacaoUsuarios.column("cpf", width=100)
        RelacaoUsuarios.heading("cpf", text="CPF")
        RelacaoUsuarios.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.59)

    # Exibe a versão atual do programa (ainda apenas um texto sem atualização automática)
    def versao(self):
        Versao = CTkLabel(self.Frame1,
                          text='V 1.2.4',
                          font=('Arial',10,'bold'),
                          text_color='#228B22',
                          fg_color='grey15').place(relx=0.102, rely=0.89, relwidth=0.05, relheight=0.03)

# Mantém o programa em loop
Mouk()