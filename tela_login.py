import datetime
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tkinter import*
import tkinter as tk

con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')

def entrar():
    tela.destroy()
    import tela_menu_principal




tela = Tk()
tela.title('Tela de Login')
tela.geometry('400x300')


def validar():
    usuario = entry_nomeusuario.get()
    senha = entry_senha.get()
    senha2 = tuple(senha)

    busca = """select * from usuarios where usuario_senha = (%s)"""
    condicao = (senha2)

    cursor = con.cursor()
    cursor.execute(busca, condicao)
    con.commit()
    linhas = cursor.fetchall()
    print(linhas)
    cursor.close()

    if len(linhas) >= 1:  # Verifica se o retorno contém alguma linha
        tela.destroy()
        import tela_menu_principal

    else:
        print('Usuário ou senha inválido !')

campo1 = tk.Label(text="USUARIO")
campo1.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_nomeusuario = tk.Entry()
entry_nomeusuario.grid(row=1,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

campo2 = tk.Label(text="SENHA")
campo2.grid(row=2, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_senha = tk.Entry()
entry_senha.grid(row=2,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

    #criacao de botões
entrar_botao = Button(tela, bd=0, text='ENTRAR', command=validar)
entrar_botao.place(width=87, height=51, x=100, y=180)

sair_botao = Button(tela, bd=0, text='SAIR', command=tela.destroy)
sair_botao.place(width=87, height=51, x=200, y=180)







tela.mainloop()






