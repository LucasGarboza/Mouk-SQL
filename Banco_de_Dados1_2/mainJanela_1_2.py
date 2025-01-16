# Importa a biblioteca ctk com todas as funções
from customtkinter import *

# Nome da Variável/Janela
janela = CTk()

# Aplicação em classe
class Mouk:
    def __init__(self):
        # Mantém o programa funcionando de forma ordenada
        self.janela = janela
        self.config_tela()
        self.frame_opçoes()
        self.OpçaoCadastrar_Usuarios()
        self.OpçaoListar_Usuarios()
        self.encerrar()
        self.versao()
        self.janela.mainloop()

    def encerrar(self):
        # Simples função para encerrar o programa
        self.janela.quit()

    def config_tela(self):
        # Configurações da janela
        self.janela.config(background='#363636')  # Cor de fundo
        self.janela.title('Mouk - Banco de Dados')  # Título
        self.janela.geometry('700x500')  # Dimensões x | y

    def frame_opçoes(self):
        # Frame para as opções laterais
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
                                   command=self.OpçaoCadastrar_Usuarios).place(relx=0.001, rely=0, relwidth=0.25, relheight=0.08)

        # Botão 'Usuários cadastrados'
        BotaoUsuarios = CTkButton(self.Frame1,
                                  text='USUÁRIOS CADASTRADOS',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='#228B22',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.OpçaoListar_Usuarios).place(relx=0.001, rely=0.085, relwidth=0.25, relheight=0.08)

        # Botão para finalizar a janela
        BotaoEncerrar = CTkButton(self.Frame1,
                                  text='FINALIZAR',
                                  font=("Arial", 11, "bold"),
                                  text_color='white',
                                  hover_color='#B22222',
                                  fg_color='grey25',
                                  corner_radius=0,
                                  command=self.encerrar).place(relx=0.001, rely=0.925, relwidth=0.25, relheight=0.08)

    def OpçaoCadastrar_Usuarios(self):
        # Configurações do frame com as funcionalidades de cadastrar usuário
        self.OpçaoCadastrar = CTkFrame(janela, fg_color='grey18', corner_radius=0)
        self.OpçaoCadastrar.place(relx=0.251, rely=0, relwidth=0.75, relheight=1)

        def cadastrar():
            # Realiza a coleta e verificação dos dados
            nome = CxTextoNome.get()
            idade = CxTexToIdade.get()
            if nome == '' or idade == '':
                TextoCadastrado = CTkLabel(self.OpçaoCadastrar,
                                           text=f'Por favor insira todos os\n'
                                                f'dados para continuar!',
                                           font=("Arial", 16, "bold"),
                                           text_color='red')
                TextoCadastrado.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.09)
            else:
                try:
                    # Tenta Cadastrar os dados em arquivo de texto
                    with open('cadastros.txt', 'a+', encoding='utf-8') as arquivo:
                        arquivo.writelines(f'{nome};{idade}\n')
                except:
                    print('Erro no cadastro')
                finally:
                    # Exibe texto confirmando o cadastro
                    TextoCadastrado = CTkLabel(self.OpçaoCadastrar,
                                                 text=f'Usuário {nome} cadastrado com sucesso!',
                                                 font=("Arial", 16, "bold"),
                                                 text_color='#228B22')
                    TextoCadastrado.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.09)
                    CxTextoNome.delete(0, END)
                    CxTexToIdade.delete(0, END)

        # Botão Cadastrar
        BotaoCadastrar = CTkButton(self.OpçaoCadastrar,
                                   text='CADASTRAR',
                                   font=("Arial", 11, "bold"),
                                   text_color='#DCDCDC',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   command=cadastrar).place(relx=0.25, rely=0.21, relwidth=0.51, relheight=0.09)

        # Caixa de texto 'Informe os dados'
        TextoInformeDados = CTkLabel(self.OpçaoCadastrar,
                                     text='Informe os dados abaixo:',
                                     font=("Arial", 11, "bold"),
                                     text_color='white').place(relx=0.238, rely=0.02, relwidth=0.3, relheight=0.1)

        # Caixa de texto para o usuário inserir seu nome
        CxTextoNome = CTkEntry(self.OpçaoCadastrar,
                               placeholder_text='Nome Completo')
        CxTextoNome.place(relx=0.25, rely=0.1, relwidth=0.4, relheight=0.1)

        # Caixa de texto para o usuário inserir sua idade
        CxTexToIdade = CTkEntry(self.OpçaoCadastrar,
                                placeholder_text='Idade')
        CxTexToIdade.place(relx=0.66, rely=0.1, relwidth=0.1, relheight=0.1)

    def OpçaoListar_Usuarios(self):
        # # Configurações do frame com as funcionalidades de listar usuários cadastrados
        self.OpçaoCadastrar.place_forget()
        self.OpçaoListar = CTkFrame(janela, fg_color='grey18')
        self.OpçaoListar.place(relx=0.251, rely=0, relwidth=0.75, relheight=1)

        def listar():
            # Tenta procurar por usuários cadastrados
            try:
                with open('cadastros.txt', 'rt') as texto:
                    u = 0.3
                    # Exibe cada usuário cadastrado por linha
                    for linha in texto:
                        dado = linha.split(';')
                        TextoCadastrado = CTkLabel(self.OpçaoListar,
                                               text=f'{dado[0]:<25} {dado[1]:>5}',
                                               font=("Arial", 16, "bold"),
                                               text_color='#228B22')
                        TextoCadastrado.place(relx=0.28, rely=u, relwidth=0.5, relheight=0.1)
                        u += 0.05
                        print(u)
            except:
                # Exibe texto informando não ter localizado nenhum usuário cadastrado
                TextoCadastrado = CTkLabel(self.OpçaoListar,
                                           text='Nenhum usuário cadastrado!',
                                           font=("Arial", 16, "bold"),
                                           text_color='red')
                TextoCadastrado.place(relx=0.26, rely=0.3, relwidth=0.5, relheight=0.1)

        # Botão para listar os usuários cadastrados
        BotaoListar = CTkButton(self.OpçaoListar,
                                   text='Listar',
                                   font=("Arial", 11, "bold"),
                                   text_color='#DCDCDC',
                                   hover_color='#228B22',
                                   fg_color='grey25',
                                   command=listar).place(relx=0.25, rely=0.1, relwidth=0.51, relheight=0.09)

    def versao(self):
        # Exibe a versão atual do programa (ainda apenas um texto sem atualização automatica)
        Versao = CTkLabel(self.Frame1,
                          text='V 1.1',
                          font=('Arial',10,'bold'),
                          text_color='#228B22',
                          fg_color='grey15').place(relx=0.102, rely=0.89, relwidth=0.05, relheight=0.03)

# Mantém o programa em loop
Mouk()