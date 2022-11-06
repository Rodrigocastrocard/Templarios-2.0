import datetime
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tkinter import*
import tkinter as tk

con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')

def voltar():
    tela.destroy()
    import tela_menu_cadastro



tela = Tk()
tela.title('Cadastro de Entidade')
tela.state("zoomed")


imagem = PhotoImage(file="images\\cadent.png")

lab_imagem=Label(tela, image=imagem)
lab_imagem.pack()


def salvar():
    nomemembro = entry_nomemembro.get()
    telformatado = entry_telformatado.get()
    enderecomembro = entry_endereco.get()
    data_formatada = entry_nascimento.get()
    data_formatadacand = entry_candidatura.get()
    telemerformatado = entry_telformatado.get()
    sanguemembro = entry_sangue.get()
    data_cadastro = datetime.today()


    inserir = """INSERT INTO membros
       							( nomemembro, telmembro, enderecomembro, nascimentomembro, candidaturamembro, emergenciamembro, sanguemembro, data_cadastro)
       							values (%s, %s, %s, %s, %s, %s, %s,%s);
       							"""

    sql_data = (
        nomemembro, telformatado, enderecomembro, data_formatada, data_formatadacand, telemerformatado, sanguemembro,
        data_cadastro)

    cursor = con.cursor()
    cursor.execute(inserir, sql_data)
    con.commit()
    print(cursor.rowcount, 'Registro inserido com sucesso.\n')
    cursor.close()



entry_nomemembro = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER)  #gravar informação na variavel para salvar
entry_nomemembro.place(width=500, height=30, x=400, y=50)

entry_telformatado = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER)  #gravar informação na variavel para salvar
entry_telformatado.place(width=200, height=30, x=400, y=120)

entry_endereco = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
entry_endereco.place(width=600, height=30, x=400, y=190)

entry_nascimento = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
entry_nascimento.place(width=150, height=30, x=400, y=260)

entry_candidatura = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
entry_candidatura.place(width=150, height=30, x=400, y=330)

entry_emergencia = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
entry_emergencia.place(width=200, height=30, x=400, y=390)

entry_sangue = Entry(tela, bd=2, font=("Calibri",15),justify=CENTER) #gravar informação na variavel para salvar
entry_sangue.place(width=50, height=30, x=400, y=460)


    #criacao de botões

#Quando clicar em salvar, tem que gravar as informações digitadas nas caixas

sair_botao = Button(tela, bd=0, text='SAIR', command=tela.destroy)
sair_botao.place(width=87, height=51, x=1150, y=600)


salvar_botao = Button(tela, bd=0, text='SALVAR', command=salvar)
salvar_botao.place(width=87, height=51, x=100, y=600)

voltar_botao = Button(tela, bd=0, text='VOLTAR', command=voltar)
voltar_botao.place(width=87, height=51, x=200, y=600)



tela.mainloop()






