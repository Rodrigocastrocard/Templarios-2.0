from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import  canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import  pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import  SimpleDocTemplate,Image
import  webbrowser
import datetime
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tkinter import*
import tkinter as tk
from tkinter import messagebox


root = Tk()


class Funcoes():

    def limpar_campos(self):
        self.entry_nomemembro.delete(0, END)
        self.entry_telformatado.delete(0, END)
        self.entry_endereco.delete(0, END)
        self.entry_nascimento.delete(0, END)
        self.entry_candidatura.delete(0, END)
        self.entry_telemformatado.delete(0, END)
        self.entry_sangue.delete(0, END)
    def db_conect(self):
        self.conexao = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')
        self.cursor = self.conexao.cursor()
        print("conectando ao banco de dados");
    def db_desconect(self):
        self.conexao.close();print("Desconectando ao banco de dados");

    def capturar_campos(self):
        self.nomemembro = self.entry_nomemembro.get()
        self.telmembro = self.entry_telmembro.get()
        self.enderecomembro = self.entry_enderecomembro.get()
        self.nascimentomembro = self.entry_nascimemtomembro.get()
    def add_cliente(self):
        #obter dados dos campos
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""INSERT INTO membros (nomemembro,telmembro,enderecomembro) 
        VALUES(?,?,?)""",(self.nomemembro,self.telmembro,self.enderecomembro))
        self.conexao.commit()
        self.db_desconect()
        self.select_lista()
        self.limpar_campos()
    def select_lista(self):
        self.lista_grid.delete(*self.lista_grid.get_children())
        self.db_conect()
        lista = self.cursor.execute("""SELECT idmembro , nomemembro,telmembro,nascimentomembro
         FROM clientes ORDER BY nome ASC;""")
        for l in lista:
            self.lista_grid.insert("",END,values=l)
        self.db_desconect()
    def OnDubleClick(self,event):
        self.limpar_campos()
        self.lista_grid.selection()

        for x in self.lista_grid.selection():
            col1,col2,col3,col4 = self.lista_grid.item(x,'values')
            self.entry_nomemembro.insert(END, col1)
            self.entry_telmembro.insert(END, col2)
            self.entry_telmembro.insert(END, col3)
            self.entry_nascimentomembro.insert(END, col4)
    def deleta_cliente(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""DELETE FROM membros WHERE idmembro = ?""",(self.codigomembro))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.select_lista()

    def alterar_cliente(self):
        self.capturar_campos()
        self.db_conect()
        self.cursor.execute("""UPDATE membros SET nomemembro = ?, telmembro = ?, nascimentomembro = ? 
        WHERE idmembro = ?;
        """,(self.nomemembro,self.telmembro,self.nascimentomembro,self.codigomembro))
        self.conexao.commit()
        self.db_desconect()
        self.limpar_campos()
        self.select_lista()

    def Buscar_Cliente(self):
        self.db_conect()
        self.lista_grid.delete(*self.lista_grid.get_children())

        self.entry_nomemembro.insert(END,'%')
        nome = '%'+self.entry_nomemembro.get()
        self.cursor.execute("""SELECT * FROM membros WHERE nomemembro LIKE '%s' COLLATE NOCASE ORDER BY Nome ASC"""%nome)
        Resultado_busca = self.cursor.fetchall()

        for cliente in Resultado_busca:
            self.lista_grid.insert("",END,values=cliente)
        self.db_desconect()

        self.limpar_campos()
        self.db_desconect()



class Aplication(Funcoes):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.grid_cliente()
        self.widgets_frame1()
        self.Menus()
        self.criar_tabela()
        self.select_lista()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#6a50c9')
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=850, height=700)
        self.root.minsize(width=400, height=300)

    def frames_tela(self):
        self.frame1 = Frame(self.root, bd=4, bg="#fff",
                            highlightbackground="#b471f8", highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame2 = Frame(self.root, bd=4, bg="#fff",
                            highlightbackground="#b471f8", highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        # botão limpar
        self.bt_limpar = Button(self.frame1, text="Limpar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'), command=self.limpar_campos)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Buscar
        self.bt_buscar = Button(self.frame1, text="Buscar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.Buscar_Cliente)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        # botão Novo
        self.bt_novo = Button(self.frame1, text="Novo",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Altera
        self.bt_alterar = Button(self.frame1, text="Alterar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão Apagar
        self.bt_apagar = Button(self.frame1, text="Apagar",
                                bg="#583bbf", fg="white", font=('verdana', 8, 'bold'),command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # label e entry - codigo -----------------------------
        self.lb_codigo = Label(self.frame1, text="Codigo",
                               bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.entry_codigo = Entry(self.frame1, text="Codigo",
                                  bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_codigo.place(relx=0.05, rely=0.15, relwidth=0.08)

        # label e entry - nome ----------------------------------
        self.lb_nome = Label(self.frame1, text="Nome",
                             bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.entry_nome = Entry(self.frame1,
                                bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_nome.place(relx=0.05, rely=0.45, relwidth=0.7)

        # label e entry - Telfone--------------------------
        self.lb_telfone = Label(self.frame1, text="Telfone",
                                bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_telfone.place(relx=0.05, rely=0.6)

        self.entry_telfone = Entry(self.frame1,
                                   bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_telfone.place(relx=0.05, rely=0.7, relwidth=0.4)

        # label e entry - Cidade -----------------------
        self.lb_cidade = Label(self.frame1, text="Cidade",
                               bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.entry_cidade = Entry(self.frame1,
                                  bg="white", fg="#583bbf", font=('verdana', 10, 'bold'))
        self.entry_cidade.place(relx=0.5, rely=0.7, relwidth=0.5)

    def grid_cliente(self):
        self.lista_grid = ttk.Treeview(self.frame2, height=3,
                                       column=('col1', 'col2', 'col3', 'col4'))
        self.lista_grid.heading("#0", text='')
        self.lista_grid.heading("#1", text='CODIGO')
        self.lista_grid.heading("#2", text='NOME')
        self.lista_grid.heading("#3", text='TELEFONE')
        self.lista_grid.heading("#4", text='CIDADE')

        self.lista_grid.column("#0", width=1)
        self.lista_grid.column("#1", width=25)
        self.lista_grid.column("#2", width=200)
        self.lista_grid.column("#3", width=125)
        self.lista_grid.column("#4", width=125)
        self.lista_grid.place(relx=0.005, rely=0.1, relwidth=0.95, relheight=0.86)

        self.scrol_lista = Scrollbar(self.frame2, orient='vertical')
        self.lista_grid.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.88)
        self.lista_grid.bind("<Double-1>",self.OnDubleClick)

    def Menus(self):
        Menubar = Menu(self.root)
        self.root.config(menu=Menubar)
        filemenu = Menu(Menubar)
        filemenu2 = Menu(Menubar)

        def Quit(): self.root.destroy()

        Menubar.add_cascade(label="opções",menu=filemenu)
        Menubar.add_cascade(label="Funções", menu=filemenu2)

        filemenu.add_command(label="Sair",command=Quit)
        filemenu2.add_command(label="Limpar campos", command=self.limpar_campos)
        filemenu2.add_command(label="Gerar Relatório", command=self.Gerar_Ficha)


Aplication()