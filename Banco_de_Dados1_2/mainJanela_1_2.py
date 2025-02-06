# Importa a biblioteca ctk com todas as funções
from customtkinter import *
# Importa as funções treeview e messagebox do tkinter
from tkinter import ttk, messagebox, PhotoImage, Label
# Importa a função de enviar e-mail do módulo Emails
from Banco_de_Dados.Banco_de_Dados1_2.Emails import enviarEmail
# Importa as funções de inserir novos dados e conexão do módulo de integração Python/SQL
from Banco_de_Dados.Banco_de_Dados1_2.IntegraçaoSQL import NovosDados, ListaDados, DeletaDados
import os

from Banco_de_Dados.Banco_de_Dados1_2.imgs import imgWallpaperOpcaoAtt, imgBotaoDeletar

# Nome da Variável/Janela
janela = CTk()

# Aplicação em classe
class Mouk:
    # Mantém o programa funcionando de forma ordenada
    def __init__(self):
        self.janela = janela
        self.config_tela()
        self.frame_opcoes()
        self.OpcaoCadastrar_Usuarios()
        self.OpcaoAtualizacoes()
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
        self.janela.geometry('1320x660')  # Dimensões x | y

    # Configurações do Frame para as opções laterais a esquerda
    def frame_opcoes(self):
        self.Frame1 = CTkFrame(self.janela,
                               corner_radius=0,
                               fg_color='grey15').place(relx=0, rely=0, relwidth=0.15, relheight=1)

        # Botao 'Cadastrar Usuário'
        BotaoCadastrarUsuario = CTkButton(self.Frame1,
                                   text='USUÁRIOS',
                                   font=("Arial", 11, "bold"),
                                   text_color='white',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   corner_radius=0,
                                   command=self.OpcaoCadastrar_Usuarios).place(relx=0.001, rely=0.062, relwidth=0.15, relheight=0.06)

        # Botão 'Usuários cadastrados'
        BotaoUsuarios = CTkButton(self.Frame1,
                                  text='ATUALIZAÇÕES',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='#228B22',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.OpcaoAtualizacoes).place(relx=0.001, rely=0.0, relwidth=0.15, relheight=0.06)

        # Botão para finalizar a janela
        BotaoEncerrar = CTkButton(self.Frame1,
                                  text='FINALIZAR',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='red',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.encerrar).place(relx=0.001, rely=0.94, relwidth=0.15, relheight=0.06)

    # Configurações do frame com as funcionalidades para as atualizações
    def OpcaoAtualizacoes(self):
        self.OpcaoListar = CTkFrame(self.janela, fg_color='grey18')
        self.OpcaoListar.place(relx=0.152, rely=0, relwidth=0.846, relheight=1)

        imgWallpaperOpcaoAtt(self.OpcaoListar)

    # Configurações do frame com as funcionalidades para cadastrar um usuário
    def OpcaoCadastrar_Usuarios(self):
        self.OpcaoCadastrar = CTkFrame(self.janela, fg_color='grey18')
        self.OpcaoCadastrar.place(relx=0.152, rely=0, relwidth=0.846, relheight=1)

        # Função que lista todos os usuários cadastrados e exibe na relação
        def listar():
            RelacaoUsuarios.delete(*RelacaoUsuarios.get_children())
            comandoSql = "SELECT * FROM MOUK_USUARIOS order by ID_USUARIO"
            relacao = ListaDados(comandoSql)
            for l in relacao:
                RelacaoUsuarios.insert("", "end", values=l)

        # Função que deleta os dados selecionados
        def deletar():
            try:
                DadoSelecionado = RelacaoUsuarios.selection()[0]
                Dados = RelacaoUsuarios.item(DadoSelecionado, "values")
                selecionado = Dados[1]
                comandoSql = f"DELETE FROM MOUK_USUARIOS WHERE NOME LIKE '%{selecionado}%'"
                try:
                    DeletaDados(comandoSql)
                except:
                    messagebox.showinfo(title="Erro", messsage="Erro ao deletar!")
                finally:
                    RelacaoUsuarios.delete(DadoSelecionado)
            except:
                messagebox.showinfo(title="Erro", message="Nenhum item selecionado!")

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
                messagebox.showinfo(title="Informações incompletas", message="Por favor, insira todos os dados para continuar!")

            else:
                try:
                    # Comando que insere novos dados usando as variaveis correspondentes
                    Novos_Dados = ("INSERT INTO MOUK_USUARIOS"
                                   "(NOME, ANO_NASCIMENTO, EMAIL, CONTATO, CARGO, CPF)"
                                   f"VALUES('{nome}', '{AnoNascimento}', '{email}', '{contato}', '{cargo}', '{cpf}')")

                    # Função que tenta inserir novos dados com base nos parâmetros passados
                    NovosDados(Novos_Dados)
                except:
                    # Retorna mensagem de erro caso a inserção de dados não funcione
                    print(f'Erro no cadastro')
                finally:
                    # Exibe texto confirmando o cadastro e envia um e-mail para o usuário confirmando o cadastro
                    enviarEmail(email, nome)
                    messagebox.showinfo(title="Novo Registro", message=f"Usuário(a) {nome} cadastrado(a) com sucesso!")

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
                                     font=("Arial", 12, "bold"),
                                     text_color='white').place(x=27, rely=0.004, relwidth=0.275, relheight=0.06)

        # Caixa de texto para o usuário inserir seu nome
        CxTextoNome = CTkEntry(self.OpcaoCadastrar,
                               placeholder_text='Nome Completo', placeholder_text_color="white")
        CxTextoNome.place(relx=0.1, rely=0.05, relwidth=0.4, relheight=0.06)

        # Caixa de texto para o usuário inserir o ano de nascimento
        CxTexToAnoNascimento = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='Data de Nascimento: DD/MM/AAAA', placeholder_text_color="white")
        CxTexToAnoNascimento.place(relx=0.51, rely=0.05, relwidth=0.3, relheight=0.06)

        # Caixa de texto para o usuário inserir seu e-mail
        CxTexToEmail = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='E-mail', placeholder_text_color="white")
        CxTexToEmail.place(relx=0.1, rely=0.13, relwidth=0.42, relheight=0.06)

        # Caixa de texto para o usuário inserir o contato de telefone
        CxTexToContato = CTkEntry(self.OpcaoCadastrar,
                                  placeholder_text='TEL: (00) 0 0000-0000', placeholder_text_color="white")
        CxTexToContato.place(relx=0.53, rely=0.13, relwidth=0.28, relheight=0.06)

        # Caixa de texto para o usuário inserir seu cpf
        CxTexToCpf = CTkEntry(self.OpcaoCadastrar,
                                placeholder_text='CPF: 000.000.000-00', placeholder_text_color="white")
        CxTexToCpf.place(relx=0.1, rely=0.21, relwidth=0.3, relheight=0.06)

        # Caixa de texto para o usuário inserir seu cargo
        CxTexToCargo = CTkComboBox(self.OpcaoCadastrar,
                                   button_hover_color="#228B22",
                                   dropdown_hover_color="#228B22",
                                   values=["Diretor", "Coordenador", "Lixeiro", "TI"])
        CxTexToCargo.set("Selecione o cargo")
        CxTexToCargo.place(relx=0.41, rely=0.21, relwidth=0.4, relheight=0.06)

        # Botão Cadastrar
        imgAtt = PhotoImage(file="imgs\\add.gif")
        BotaoCadastrar = CTkButton(self.OpcaoCadastrar,
                                   text='CADASTRAR NOVO USUÁRIO',
                                   font=("Arial", 11, "bold"),
                                   text_color='white',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   image=imgAtt,
                                   command=cadastrar).place(relx=0.1, rely=0.29, relwidth=0.71, relheight=0.06)

        # Botão para listar os usuários cadastrados
        imgAtt = PhotoImage(file="imgs\\refresh.gif")
        BotaoListar = CTkButton(self.OpcaoCadastrar,
                                text='LISTAR',
                                font=("Arial", 11, "bold"),
                                text_color='#DCDCDC',
                                hover_color='blue',
                                fg_color='grey25',
                                image=imgAtt,
                                command=listar).place(relx=0.85, rely=0.05, relwidth=0.1, relheight=0.09)

        # Botão para buscar usuários cadastrados
        imgAtt = PhotoImage(file="imgs\\search.gif")
        BotaoBuscar = CTkButton(self.OpcaoCadastrar,
                                text='BUSCAR',
                                font=("Arial", 11, "bold"),
                                text_color='#DCDCDC',
                                hover_color='blue',
                                image=imgAtt,
                                fg_color='grey25').place(relx=0.85, rely=0.155, relwidth=0.1, relheight=0.09)

        # Botão para deletar usuários cadastrados
        imgAtt = PhotoImage(file="imgs\\delete.gif")
        BotaoDeletar = CTkButton(self.OpcaoCadastrar,
                                 text='DELETAR',
                                 font=("Arial", 11, "bold"),
                                 text_color='#DCDCDC',
                                 hover_color='red',
                                 fg_color='grey25',
                                 image=imgAtt,
                                 command=deletar).place(relx=0.85, rely=0.26, relwidth=0.1, relheight=0.09)
        RelacaoUsuarios = ttk.Treeview(self.OpcaoCadastrar, columns=("id", "nome", "data_nascimento", "e-mail",
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
        RelacaoUsuarios.place(relx=0.0001, rely=0.4, relwidth=1, relheight=0.596)

    # Exibe a versão atual do programa (ainda apenas um texto sem atualização automática)
    def versao(self):
        Versao = CTkLabel(self.Frame1,
                          text='V 1.2.8',
                          font=('Arial',10,'bold'),
                          text_color='#228B22',
                          fg_color='grey15').place(relx=0.05, rely=0.9, relwidth=0.05, relheight=0.03)

# Mantém o programa em loop
Mouk()
