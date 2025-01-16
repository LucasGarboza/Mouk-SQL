from customtkinter import *


def fechar():
    """
    Finaliza a janela atual
    :return: QUIT
    """
    janela.quit()

# Configurações da janela
janela = CTk() #Nome da variável
set_appearance_mode('dark') #Aparência
janela.title('Banco de Dados') #Título
janela.geometry('450x300') #Dimensões x | y

# Texto 'Novo Usuário'
TextoCadastrar = CTkLabel(janela,
                          text='NOVO USUÁRIO',
                          font=('Arial', 18, 'bold'),
                          text_color='#32CD32').place(relx=0.25, rely=0.001, relwidth=0.5, relheight=0.15)

# Caixa de texto para o 'nome'
CxTextoNome = CTkEntry(janela,
                       placeholder_text='Nome Completo').place(relx=0.25, rely=0.15, relwidth=0.4, relheight=0.15)

#Caixa de texto para 'idade'
CxTexToIdade = CTkEntry(janela,
                        placeholder_text='Idade').place(relx=0.65, rely=0.15, relwidth=0.1, relheight=0.15)

# Botão para listar usuários já cadastrados
BotaoCadastrar = CTkButton(janela,
                        text='CADASTRAR',
                        font=("Arial", 14, "bold"),
                        text_color='#DCDCDC',
                        text_color_disabled='black',
                        hover_color='#228B22',
                        fg_color='#696969').place(relx=0.25, rely=0.31, relwidth=0.5, relheight=0.10)

# Mensagem de texto 'ou' servindo de divisão de funções na tela
TextoOu = CTkLabel(janela,
                   text='OU',
                   text_color='#00CED1',
                   font=('Arial',14,'bold')).place(relx=0.45, rely=0.46, relwidth=0.1, relheight=0.05)

# Texto 'Usuários cadastrados'
TextoUsuarios = CTkLabel(janela,
                          text='USUÁRIOS CADASTRADOS',
                          font=('Arial', 18, 'bold'),
                          text_color='#32CD32').place(relx=0.1, rely=0.51, relwidth=0.8, relheight=0.15)

# Botão para listar os usuários já cadastrados
BotaoListar = CTkButton(janela,
                        text='LISTAR',
                        font=("Arial", 14, "bold"),
                        text_color='#DCDCDC',
                        text_color_disabled='black',
                        hover_color='#1E90FF',
                        fg_color='#696969').place(relx=0.25, rely=0.63, relwidth=0.5, relheight=0.10)

# Botão para finalizar a janela
BotaoEncerrar = CTkButton(janela,
                          text='FINALIZAR',
                          command=fechar,
                          font=("Arial", 14, "bold"),
                          text_color='#DCDCDC',
                          hover_color='#B22222',
                          fg_color='#696969').place(relx=0.38, rely=0.9, relwidth=0.25, relheight=0.10)

janela.mainloop()