from tkinter import PhotoImage, Label

def imgWallpaperOpcaoAtt(janela):
    imgAtt = PhotoImage(file="imgs\\wallpaper.png")
    imgAtualizacao = Label(janela, image=imgAtt)
    imgAtualizacao.photo = imgAtt
    imgAtualizacao.place(relx=0, rely=0, relwidth=1, relheight=1)
