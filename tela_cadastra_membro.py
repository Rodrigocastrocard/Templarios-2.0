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



def salvar():
    nomemembro = entry_nomemembro.get()
    telformatado = entry_telformatado.get()
    enderecomembro = entry_endereco.get()
    data_formatada = entry_nascimento.get()
    data_formatadacand = entry_candidatura.get()
    telemerformatado = entry_telemformatado.get()
    sanguemembro = entry_sangue.get()
    data_cadastro = datetime.today().strftime('%d-%m-%y')


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
    tela.destroy()
    import tela_menu_cadastro


campo1 = tk.Label(text="Nome")
campo1.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_nomemembro = tk.Entry()
entry_nomemembro.grid(row=1,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

campo2 = tk.Label(text="Telefone")
campo2.grid(row=2, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_telformatado = tk.Entry()
entry_telformatado.grid(row=2,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

campo3 = tk.Label(text="Endereco")
campo3.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_endereco = tk.Entry()
entry_endereco.grid(row=3,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

campo4 = tk.Label(text="Nascimento")
campo4.grid(row=4, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_nascimento = tk.Entry()
entry_nascimento.grid(row=4,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

campo5 = tk.Label(text="Candidatura")
campo5.grid(row=5, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_candidatura = tk.Entry()
entry_candidatura.grid(row=5,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

campo6 = tk.Label(text="Tel Emergencia")
campo6.grid(row=6, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_telemformatado = tk.Entry()
entry_telemformatado.grid(row=6,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)

campo7 = tk.Label(text="Sangue")
campo7.grid(row=7, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_sangue = tk.Entry()
entry_sangue.grid(row=7,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)


    #criacao de botões

#Quando clicar em salvar, tem que gravar as informações digitadas nas caixas

sair_botao = Button(tela, bd=0, text='SAIR', command=tela.destroy)
sair_botao.place(width=87, height=51, x=1150, y=600)


salvar_botao = Button(tela, bd=0, text='SALVAR', command=salvar)
salvar_botao.place(width=87, height=51, x=100, y=600)

voltar_botao = Button(tela, bd=0, text='VOLTAR', command=voltar)
voltar_botao.place(width=87, height=51, x=200, y=600)



tela.mainloop()






