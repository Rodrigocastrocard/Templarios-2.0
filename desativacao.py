from tkinter import*
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import mysql.connector


con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')


def confirmacao_desativa():
    inativar = """update membros set ativomembro = 0 where idmembro = (%s);"""
    sql_data = entry_id_desativa


    cursor = con.cursor()
    cursor.execute(inativar, [sql_data])
    con.commit()
    print(cursor.rowcount, 'Membro desativado com sucesso.')
    cursor.close()

    entry_id_desativa.delete(0, END)



tela_desativa = Tk()
tela_desativa.title('DESATIVAR MEMBRO')
tela_desativa.geometry('400x150')




campo1 = tk.Label(text="Codigo")
campo1.grid(row=3, column=0,padx = 5, pady=10, sticky='nswe', columnspan =4 )
entry_id_desativa = tk.Entry()
entry_id_desativa.grid(row=3,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)


voltar_botao_desativa = Button(tela_desativa, bd=0, text='INATIVAR', command=confirmacao_desativa)
voltar_botao_desativa.place(width=87, height=51, x=50, y=90)

voltar_botao_desativa = Button(tela_desativa, bd=0, text='VOLTAR', command=tela_desativa.destroy)
voltar_botao_desativa.place(width=87, height=51, x=250, y=90)





tela_desativa.mainloop()
