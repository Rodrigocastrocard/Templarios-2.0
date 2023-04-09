import datetime
import mysql.connector
from datetime import datetime
from tkinter import*
import tkinter as tk
from tkinter import messagebox

con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')

def localizar():
    cursor = con.cursor()
    comando_sql = """select * from membros"""
    cursor.execute(comando_sql)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    tela_localizar = Tk()
    tela_localizar.title('Localizar Membros')
    tela_localizar.state("zoomed")

    campo1 = tk.Label(text="Nome")
    campo1.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)
    entry_nomemembro = tk.Entry()
    entry_nomemembro.grid(row=1, column=2, padx=150, pady=15, sticky='nswe', columnspan=4)



    tela_localizar.mainloop()


localizar()

