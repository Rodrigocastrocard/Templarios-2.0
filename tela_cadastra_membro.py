import datetime
import mysql.connector
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pandas as pd

con = mysql.connector.connect(host='localhost',
                             database='templarios',
                             user='root',
                             password='Janete4353',
                             auth_plugin='mysql_native_password')
tela = Tk()
tela.title('Cadastro de Membros')
tela.state("zoomed")

# define columns
columns = ('codigo', 'nome', 'aniversario', 'ativo')

tree = ttk.Treeview(tela, columns=columns, show='headings')

# define campos
tree.heading('codigo', text='Codigo')
tree.heading('nome', text='Nome')
tree.heading('aniversario', text='Aniversário')
tree.heading('ativo', text='Ativo?')

# gera query
membros = []
consulta_sql = """select idmembro, nomemembro, nascimentomembro, ativomembro from membros order by nascimentomembro asc"""
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()


# mostra consulta
for linha in linhas:
    tree.insert('', tk.END, values=linha)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=8, column=20, sticky='nsew')

# add barra de rolagem
scrollbar = ttk.Scrollbar(tela, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=8, column=21, sticky='ns')


def voltar():
    tela.destroy()
    import tela_menu_cadastro


def limpar_campos():
    entry_nomemembro.delete(0, END)
    entry_telformatado.delete(0, END)
    entry_endereco.delete(0, END)
    entry_nascimento.delete(0, END)
    entry_candidatura.delete(0, END)
    entry_telemformatado.delete(0, END)
    entry_sangue.delete(0, END)

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
    cursor.close()
    messagebox.showinfo('ALERTA', \
                        'Registro inserido com sucesso !')
    limpar_campos()



# exportar relatorios
def exportar():
    consulta=('''select * from membros''')
    cursor = con.cursor()
    cursor.execute(consulta)
    result = cursor.fetchall()
    print (result)
    data = {'Codigo': [result,0],
            'Nome': [result,1],
            'telefone': [result,2],
            'Endereço': [result,3],
            'Data de Nascimento': [result,4],
            'Data de Candidatura': [result,5],
            'Telefone de Emergencia': [result,6],
            'Tipo Sanguineo': [result,7],
            'Ativo':[result,8],
            'Data de Cadastro': [result,9],
            }

    df = pd.DataFrame(data)

    df.to_excel(r'C:\Users\Rodrigo Cardoso\Downloads\Cadastro de Membros.xlsx', index=False)
    messagebox.showinfo('ALERTA', \
                        'Registro exportado com sucesso !')


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

campo8 = tk.Label(text="Ativo")
campo8.grid(row=7, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
entry_ativo = tk.Checkbutton()
entry_ativo.grid(row=7,column=2, padx=150, pady=15, sticky='nswe', columnspan = 4)



    #criacao de botões

salvar_botao = Button(tela, bd=0, text='SALVAR', command=salvar)
salvar_botao.place(width=87, height=51, x=50, y=350)

limpar_botao = Button(tela, bd=0, text='LIMPAR', command=limpar_campos)
limpar_botao.place(width=87, height=51, x=150, y=350)

relatorio_botao = Button(tela, bd=0, text='EXPORTAR', command=exportar)
relatorio_botao.place(width=87, height=51, x=250, y=350)

voltar_botao = Button(tela, bd=0, text='VOLTAR', command=voltar)
voltar_botao.place(width=87, height=51, x=1050, y=10)

sair_botao = Button(tela, bd=0, text='SAIR', command=tela.destroy)
sair_botao.place(width=87, height=51, x=1150, y=10)





tela.mainloop()






