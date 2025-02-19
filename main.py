# Importa a biblioteca ctk com todas as funções
from customtkinter import *
# Importa as bibliotecas necessárias do tkinter
from tkinter import ttk, messagebox, PhotoImage, LabelFrame
# Importa a função de enviar e-mail do módulo Emails
from Banco_de_Dados.Emails import enviarEmail
# Importa as funções necessárias do módulo de integração Python/SQL
from Banco_de_Dados.IntegraçaoSQL import NovosDados, ListaDados, DeletaDados
# Importa a função necessária do módulo de imagens
from Banco_de_Dados.imgs import imgWallpaperOpcaoAtt

# Janelas presentes no programa
janela_main = CTk()
janela_login = CTkToplevel()

# Janela de Login
class MoukLogin:
    # Mantém o programa funcionando de forma ordenada
    def __init__(self):
        self.janela_login = janela_login
        self.config_tela()
        self.OpcaoLogin()
        self.janela_login.mainloop()

    # Configurações da janela de login
    def config_tela(self):
        self.janela_login.config(background="white")  # Cor de fundo
        self.janela_login.title("Mouk - Login")  # Título
        self.janela_login.geometry("700x400")  # Dimensões x | y
        self.janela_login.maxsize(width=700, height=400)
        self.janela_login.minsize(width=700, height=400)

    # Funcão que valida os dados de login e retorna o programa principal
    def OpcaoLogin(self):
        def logar():
            login = CxTextoLogin.get()
            senha = CxTextoSenha.get()
            if not login == "" and not senha == "":
                janela_login.destroy()
                # Mantém o programa em loop
                Mouk()
            else:
                messagebox.showinfo(title="Informações incompletas", message="Preencha todos os dados para continuar")

        def MostrarSenha():
            if CxTextoSenha.cget("show") == "*":
                CxTextoSenha.configure(show="")
            else:
                CxTextoSenha.configure(show="*")

        def sair():
            janela_login.quit()

        imgAtt = PhotoImage(file="imgs\\tela login.png")
        imgWallpaperTelaLogin = CTkButton(self.janela_login,
                                          image=imgAtt,
                                          hover=False,
                                          fg_color="black",
                                          corner_radius=0)
        imgWallpaperTelaLogin.place(relx=0, rely=0, relwidth=1, relheight=1)

        CxTextoInfoLogin = CTkLabel(self.janela_login,
                                    text="Entre para continuar",
                                    text_color="#32CD32",
                                    font=("Arial", 18, "bold"))
        CxTextoInfoLogin.place(relx=0.45, rely=0.15, relwidth=0.45, relheight=0.1)

        CxTextoLogin = CTkEntry(self.janela_login,
                                text_color="grey30",
                                placeholder_text="Usuário",
                                placeholder_text_color="#A9A9A9",
                                fg_color="white",
                                font=("Arial", 16, "bold"))
        CxTextoLogin.place(relx=0.45, rely=0.25, relwidth=0.45, relheight=0.15)

        CxTextoSenha = CTkEntry(self.janela_login,
                                text_color="grey30",
                                placeholder_text="Senha",
                                placeholder_text_color="#A9A9A9",
                                fg_color="white",
                                font=("Arial", 16, "bold"),
                                show="*")
        CxTextoSenha.place(relx=0.45, rely=0.42, relwidth=0.45, relheight=0.15)

        imgAtt = PhotoImage(file="imgs\\show.gif")
        BotaoMostrarSenha = CTkButton(self.janela_login,
                                      bg_color="white",
                                      fg_color="white",
                                      hover_color="white",
                                      text="",
                                      image=imgAtt,
                                      command=MostrarSenha)
        BotaoMostrarSenha.place(relx=0.84, rely=0.445, relwidth=0.05, relheight=0.1)

        BotaoLogin = CTkButton(self.janela_login,
                               text="Entrar",
                               text_color="white",
                               font=("Arial", 16, "bold"),
                               hover_color="#228B22",
                               fg_color="#696969",
                               command=logar)
        BotaoLogin.place(relx=0.45, rely=0.59, relwidth=0.45, relheight=0.1)

        BotaoSair = CTkButton(self.janela_login,
                              text="Sair",
                              text_color="white",
                              font=("Arial", 16, "bold"),
                              hover_color="red",
                              fg_color="#696969",
                              command=sair)
        BotaoSair.place(relx=0.45, rely=0.72, relwidth=0.45, relheight=0.1)

# Programa principal
class Mouk:
    # Mantém o programa funcionando de forma ordenada
    def __init__(self):
        self.janela_main = janela_main
        self.config_tela()
        self.frame_opcoes()
        self.OpcaoCadastrar_Usuarios()
        self.OpcaoAtualizacoes()
        self.encerrar()
        self.versao()
        self.janela_main.mainloop()

    # Simples função para encerrar o programa
    def encerrar(self):
        self.janela_main.quit()

    # Configurações da janela_main com o customtkinter
    def config_tela(self):
        self.janela_main.config(background='black')  # Cor de fundo
        self.janela_main.title('Mouk - Banco de Dados')  # Título
        self.janela_main.geometry('1320x660')  # Dimensões x | y

    # Configurações do Frame para as opções laterais a esquerda
    def frame_opcoes(self):
        self.Frame1 = CTkFrame(self.janela_main,
                               corner_radius=0,
                               fg_color='grey15').place(relx=0, rely=0, relwidth=0.15, relheight=1)

        # Botao 'Cadastrar Usuário'
        CTkButton(self.Frame1,
                   text='USUÁRIOS',
                   font=("Arial", 11, "bold"),
                   text_color='white',
                   hover_color='#228B22',
                   fg_color='grey25',
                   corner_radius=0,
                   command=self.OpcaoCadastrar_Usuarios).place(relx=0.001, rely=0.062, relwidth=0.15, relheight=0.06)

        # Botão 'Usuários cadastrados'
        CTkButton(self.Frame1,
                  text='ATUALIZAÇÕES',
                  font=("Arial", 11, "bold"),
                  text_color='white',
                  hover_color='#228B22',
                  fg_color='grey25',
                  corner_radius=0,
                  command=self.OpcaoAtualizacoes).place(relx=0.001, rely=0.0, relwidth=0.15, relheight=0.06)

        # Botão para finalizar a janela_main
        CTkButton(self.Frame1,
                  text='FINALIZAR',
                  font=("Arial", 11, "bold"),
                  text_color='white',
                  hover_color='red',
                  fg_color='grey25',
                  corner_radius=0,
                  command=self.encerrar).place(relx=0.001, rely=0.94, relwidth=0.15, relheight=0.06)

    # Configurações do frame com as funcionalidades para as atualizações
    def OpcaoAtualizacoes(self):
        self.OpcaoListar = CTkFrame(self.janela_main, fg_color='black', bg_color="black", border_color="black")
        self.OpcaoListar.place(relx=0.152, rely=0, relwidth=0.846, relheight=1)

        imgWallpaperOpcaoAtt(self.OpcaoListar)

    # Configurações do frame com as funcionalidades para cadastrar um usuário
    def OpcaoCadastrar_Usuarios(self):
        self.OpcaoCadastrar = CTkFrame(self.janela_main, fg_color="white", corner_radius=0)
        self.OpcaoCadastrar.place(relx=0.152, rely=0, relwidth=0.846, relheight=1)

        # Função que lista todos os usuários cadastrados e exibe na relação
        def listar():
            RelacaoUsuarios.delete(*RelacaoUsuarios.get_children())
            comandoSql = "SELECT * FROM MOUK_USUARIOS order by ID"
            relacao = ListaDados(comandoSql)
            for l in relacao:
                RelacaoUsuarios.insert("", "end", values=l, tags="Mouk")

        def buscar():
            pass

        # Função que deleta os dados selecionados
        def deletar():
            try:
                DadoSelecionado = RelacaoUsuarios.selection()[0]
                Dados = RelacaoUsuarios.item(DadoSelecionado, "values")
                selecionado = Dados[1]
                comandoSql = f"DELETE FROM MOUK_USUARIOS WHERE NOME LIKE '%{selecionado}%'"
                try:
                    DeletaDados(comandoSql)
                except Exception as erro:
                    print(erro)
                    messagebox.showinfo(title="Erro", messsage=f"Erro ao deletar!")
                finally:
                    RelacaoUsuarios.delete(DadoSelecionado)
            except Exception as erro:
                print(erro)
                messagebox.showinfo(title="Erro", message=f"Nenhum item selecionado!")

        # Realiza a coleta e verificação e validação dos dados e os cadastra no banco de dados
        def cadastrar():
            # nome = CxTextoNome.get()
            AnoNascimento = CxTexToAnoNascimento.get()
            cpf = CxTexToCpf.get()
            email = CxTexToEmail.get()
            cargo = CxTexToCargo.get()
            contato = CxTexToContato.get()
            nome = CxTextoNome.get()
            senha = CxTextoSenha.get()

            # Verifica se algum campo está vazio e retorna uma mensagem de erro
            if nome == "" or AnoNascimento == "" or cpf == "" or email == "" or cargo == "" or contato == "" or senha == "":
                messagebox.showinfo(title="Informações incompletas", message="Por favor, insira todos os dados para continuar!")

            else:
                try:
                    # Comando que insere novos dados usando as variaveis correspondentes
                    Novos_Dados = ("INSERT INTO MOUK_USUARIOS"
                                   "(NOME, EMAIL, DATA_NASCIMENTO, SENHA, CARGO, CONTATO, CPF)"
                                   f"VALUES('{nome}', '{email}', '{AnoNascimento}', '{senha}', '{cargo}', '{contato}', '{cpf}')")

                    # Função que tenta inserir novos dados com base nos parâmetros passados
                    NovosDados(Novos_Dados)
                except Exception as erro:
                    # Retorna mensagem de erro caso a inserção de dados não funcione
                    print(f'Erro no cadastro {erro}')
                finally:
                    # Exibe texto confirmando o cadastro e envia um e-mail para o usuário confirmando o cadastro
                    enviarEmail(email, nome)
                    messagebox.showinfo(title="Novo Registro", message=f"Usuário(a) {nome} cadastrado(a) com sucesso!")

                    # Deleta todos os dados adicionados na janela_main para um novo cadastro
                    CxTextoNome.delete(0, END)
                    CxTexToAnoNascimento.delete(0, END)
                    CxTexToContato.delete(0, END)
                    CxTexToCpf.delete(0, END)
                    CxTexToEmail.delete(0, END)
                    CxTextoSenha.delete(0, END)

        # Caixa de texto 'Informe os dados abaixo'
        CxTextoInfo = LabelFrame(self.OpcaoCadastrar,
                                 text="Informe os dados abaixo:",
                                 font=("Arial", 12, "bold"))
        CxTextoInfo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.37)

        # Caixa de texto para o usuário inserir seu nome
        CxTextoNome = CTkEntry(self.OpcaoCadastrar,
                               text_color="black",
                               placeholder_text="Nome Completo",
                               placeholder_text_color="black",
                               fg_color="#F5F5F5")
        CxTextoNome.place(relx=0.1, rely=0.05, relwidth=0.4, relheight=0.06)

        # Caixa de texto para o usuário inserir o ano de nascimento
        CxTexToAnoNascimento = CTkEntry(self.OpcaoCadastrar,
                                        text_color="black",
                                        placeholder_text="Data de Nascimento",
                                        placeholder_text_color="black",
                                        fg_color="#F5F5F5")
        CxTexToAnoNascimento.place(relx=0.51, rely=0.05, relwidth=0.16, relheight=0.06)

        # Caixa de texto para o usuário inserir a senha
        CxTextoSenha = CTkEntry(self.OpcaoCadastrar,
                                text_color="black",
                                placeholder_text="Senha",
                                placeholder_text_color="black",
                                fg_color="#F5F5F5")
        CxTextoSenha.place(relx=0.68, rely=0.05, relwidth=0.13, relheight=0.06)

        # Caixa de texto para o usuário inserir seu e-mail
        CxTexToEmail = CTkEntry(self.OpcaoCadastrar,
                               text_color="black",
                                placeholder_text="E-mail",
                                placeholder_text_color="black",
                                fg_color="#F5F5F5")
        CxTexToEmail.place(relx=0.1, rely=0.13, relwidth=0.42, relheight=0.06)

        # Caixa de texto para o usuário inserir o contato de telefone
        CxTexToContato = CTkEntry(self.OpcaoCadastrar,
                               text_color="black",
                                  placeholder_text="TEL: (00) 0 0000-0000",
                                  placeholder_text_color="black",
                                  fg_color="#F5F5F5")
        CxTexToContato.place(relx=0.53, rely=0.13, relwidth=0.28, relheight=0.06)

        # Caixa de texto para o usuário inserir seu cpf
        CxTexToCpf = CTkEntry(self.OpcaoCadastrar,
                              text_color="black",
                              placeholder_text="CPF: 000.000.000-00",
                              placeholder_text_color="black",
                              fg_color="#F5F5F5")
        CxTexToCpf.place(relx=0.1, rely=0.21, relwidth=0.3, relheight=0.06)

        # Caixa de texto para o usuário inserir seu cargo
        CxTexToCargo = CTkComboBox(self.OpcaoCadastrar,
                                   text_color="black",
                                   button_hover_color="#228B22",
                                   dropdown_hover_color="#228B22",
                                   values=["Diretor", "Coordenador", "Lixeiro", "TI"],
                                   fg_color="#F5F5F5")
        CxTexToCargo.configure(text_color="black")
        CxTexToCargo.set("Selecione o cargo")
        CxTexToCargo.place(relx=0.41, rely=0.21, relwidth=0.4, relheight=0.06)

        # Botão Cadastrar
        imgAtt = PhotoImage(file="imgs\\add.gif")
        BotaoCadastrar = CTkButton(self.OpcaoCadastrar,
                                   text="CADASTRAR NOVO USUÁRIO",
                                   font=("Arial", 11, "bold"),
                                   text_color="white",
                                   hover_color="#228B22",
                                   fg_color="#696969",
                                   image=imgAtt,
                                   command=cadastrar).place(relx=0.1, rely=0.29, relwidth=0.71, relheight=0.06)

        # Botão para listar os usuários cadastrados
        imgAtt = PhotoImage(file="imgs\\refresh.gif")
        BotaoListar = CTkButton(self.OpcaoCadastrar,
                                text="LISTAR",
                                font=("Arial", 11, "bold"),
                                text_color="#DCDCDC",
                                hover_color="blue",
                                fg_color="#696969",
                                image=imgAtt,
                                command=listar).place(relx=0.85, rely=0.05, relwidth=0.1, relheight=0.09)

        # Botão para buscar usuários cadastrados
        imgAtt = PhotoImage(file="imgs\\search.gif")
        BotaoBuscar = CTkButton(self.OpcaoCadastrar,
                                text="BUSCAR",
                                font=("Arial", 11, "bold"),
                                text_color="#DCDCDC",
                                hover_color="blue",
                                fg_color="#696969",
                                image=imgAtt,
                                command=buscar).place(relx=0.85, rely=0.155, relwidth=0.1, relheight=0.09)

        # Botão para deletar usuários cadastrados
        imgAtt = PhotoImage(file="imgs\\delete.gif")
        BotaoDeletar = CTkButton(self.OpcaoCadastrar,
                                 text="DELETAR",
                                 font=("Arial", 11, "bold"),
                                 text_color="#DCDCDC",
                                 hover_color="red",
                                 fg_color="#696969",
                                 image=imgAtt,
                                 command=deletar).place(relx=0.85, rely=0.26, relwidth=0.1, relheight=0.09)

        # Treeview com a relação dos usuários
        RelacaoUsuarios = ttk.Treeview(self.OpcaoCadastrar,
                                       columns=("id", "nome", "e-mail", "data_nascimento", "senha", "cargo", "contato", "cpf"),
                                       show="headings")

        RelacaoUsuarios.tag_configure("Mouk", font=("Arial", 12), background="white")

        # Configurações das colunas com a  relação dos usuários
        RelacaoUsuarios.column("id", width=30)
        RelacaoUsuarios.heading("id", text="ID")
        RelacaoUsuarios.column("nome", width=200)
        RelacaoUsuarios.heading("nome", text="NOME")
        RelacaoUsuarios.column("e-mail", width=150)
        RelacaoUsuarios.heading("e-mail", text="E-MAIL")
        RelacaoUsuarios.column("data_nascimento", width=80)
        RelacaoUsuarios.heading("data_nascimento", text="DATA NASCIMENTO")
        RelacaoUsuarios.column("senha", width=100)
        RelacaoUsuarios.heading("senha", text="SENHA")
        RelacaoUsuarios.column("contato", width=100)
        RelacaoUsuarios.column("cargo", width=200)
        RelacaoUsuarios.heading("cargo", text="CARGO")
        RelacaoUsuarios.heading("contato", text="CONTATO")
        RelacaoUsuarios.column("cpf", width=100)
        RelacaoUsuarios.heading("cpf", text="CPF")
        RelacaoUsuarios.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.58)

    # Exibe a versão atual do programa (ainda apenas um texto sem atualização automática)
    def versao(self):
        CTkLabel(self.Frame1,
                  text="V 1.2.10",
                  font=("Arial",10,"bold"),
                  text_color="#228B22",
                  fg_color="grey15").place(relx=0.05, rely=0.9, relwidth=0.05, relheight=0.03)

# Mantém a janela de login aberta em loop
MoukLogin()
