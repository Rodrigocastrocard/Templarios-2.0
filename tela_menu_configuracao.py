from tkinter import*

def cria_tabelas():
    janela.destroy()
    import cria_tabelas

def teste_conexao():
    janela.destroy()
    import teste_conexao

def menu_principal():
    janela.destroy()
    import tela_menu_principal
def fecha_tela():
    janela.destroy()


janela = Tk()
janela.title("MENU CONFIGURACOES")
janela.state("zoomed")
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)



#importar imagem
img_tela = PhotoImage(file="images\\telatemp.png")

#criando labels
lab_fundo=Label(janela, image=img_tela)
lab_fundo.pack()

botao_tabelas = Button(janela, text="CRIAR TABELAS", command= cria_tabelas)
botao_tabelas.place(width=130, height=50, x=0, y=0)
botao_teste = Button(janela, text="TESTAR CONEXAO", command= teste_conexao)
botao_teste.place(width=130, height=50, x=0, y=50)
botao_voltar = Button(janela, text="VOLTAR", command= menu_principal)
botao_voltar.place(width=130, height=50, x=0, y=100)
botao_sair = Button(janela, text="SAIR", command= fecha_tela)
botao_sair.place(width=130, height=50, x=0, y=150)



#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
