from tkinter import PhotoImage, Label

def imgWallpaperOpcaoAtt(janela):
    imgAtt = PhotoImage(file="imgs\\wallpaper tela de atualizações.gif")
    imgAtualizaçao = Label(janela, image=imgAtt)
    imgAtualizaçao.photo = imgAtt
    imgAtualizaçao.place(relx=0, rely=0, relwidth=1, relheight=1)
