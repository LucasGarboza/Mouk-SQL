import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviarEmail(email_destino, nome):
    #Conexão com SMTP
    server_smtp = "smtp.gmail.com"
    porta = 587
    autor_email = "email de origem"
    autor_senha = "senha"

    #Configurações do Email
    recebedor_email = email_destino
    assunto_email = "Teste Python"
    corpo_email = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Teste</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
            <tr>
                <td align="center">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
                        <tr>
                            <td align="center" style="padding: 40px 0;">
                                <img src="https://cdn.pixabay.com/photo/2017/08/01/13/36/computer-2565478_1280.jpg" alt="Paisagem" width="400" style="display: block; margin: 0 auto;">
                                <p style="margin-top: 20px; text-align: center;">Olá {nome}, seja bem vindo(a)!</p>
                                <p style="text-align: center;">Este é um e-mail de confirmação de cadastro.</p>
                                <p style="text-align: center;">Agradecemos por trabalhar conosco.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Criando o email
    mensagem = MIMEMultipart()
    mensagem["From"] = autor_email
    mensagem["To"] = recebedor_email
    mensagem["Subject"] = assunto_email
    mensagem.attach(MIMEText(corpo_email, "html"))


    #Conectando o servidor smtp
    try:
        conectar = smtplib.SMTP(server_smtp, porta)
        conectar.starttls()

        conectar.login(autor_email, autor_senha)

        conectar.sendmail(autor_email, recebedor_email, mensagem.as_string())
        print("Email enviado com sucesso!")
    except Exception as Erro:
        print(f"Erro com {Erro}")
    finally:
        conectar.quit()
