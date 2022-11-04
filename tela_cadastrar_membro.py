import datetime
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tkinter import*

con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')

def cadastros():
    tela.destroy()
    import tela_menu_cadastro



tela = Tk()
tela.title('Cadastro de Entidade')
tela.state("zoomed")


imagem = PhotoImage(file="images\\cadent.png")

lab_imagem=Label(tela, image=imagem)
lab_imagem.pack()


nomemembro = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER)  #gravar informação na variavel para salvar
nomemembro.place(width=500, height=30, x=400, y=50)

telformatado = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER)  #gravar informação na variavel para salvar
telformatado.place(width=200, height=30, x=400, y=120)

endereco = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
endereco.place(width=600, height=30, x=400, y=190)

nascimento = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
nascimento.place(width=150, height=30, x=400, y=260)

candidatura = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
candidatura.place(width=150, height=30, x=400, y=330)

emergencia = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
emergencia.place(width=200, height=30, x=400, y=390)

sangue = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
sangue.place(width=50, height=30, x=400, y=460)


    #criacao de botões

#Quando clicar em salvar, tem que gravar as informações digitadas nas caixas

sair_botao = Button(tela, bd=0, text='SAIR', command=tela.destroy)
sair_botao.place(width=87, height=51, x=1150, y=600)


salvar_botao = Button(tela, bd=0, text='SALVAR', command=tela.destroy)
salvar_botao.place(width=87, height=51, x=100, y=600)

voltar_botao = Button(tela, bd=0, text='VOLTAR', command=cadastros)
voltar_botao.place(width=87, height=51, x=200, y=600)



tela.mainloop()






