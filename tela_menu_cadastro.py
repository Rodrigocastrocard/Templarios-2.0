from tkinter import*

def cadastra_membro():
    janela.destroy()
    import tela_cadastra_membro

def altera_membro():
    janela.destroy()
    import altera_membro
def desativa_membro():
    janela.destroy()
    import desativa_membro
def relmembro():
    janela.destroy()
    import relmembro
def menu_principal():
    janela.destroy()
    import tela_menu_principal
def fecha_tela():
    janela.destroy()


janela = Tk()
janela.title("MENU CADASTRO")
janela.state("zoomed")
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)


'''
#importar imagem
img_tela = PhotoImage(file="images\\telatemp.png")

#criando labels
lab_fundo=Label(janela, image=img_tela)
lab_fundo.pack()
'''

botao_cadastra = Button(janela, text="CADASTRAR", command= cadastra_membro)
botao_cadastra.place(width=130, height=50, x=0, y=0)
botao_altera = Button(janela, text="ALTERAR", command= altera_membro)
botao_altera.place(width=130, height=50, x=0, y=50)
botao_inativa = Button(janela, text="INATIVAR", command= desativa_membro)
botao_inativa.place(width=130, height=50, x=0, y=100)
botao_relatorio = Button(janela, text="RELATORIO", command= relmembro)
botao_relatorio.place(width=130, height=50, x=0, y=150)
botao_voltar = Button(janela, text="VOLTAR", command= menu_principal)
botao_voltar.place(width=130, height=50, x=0, y=200)
botao_sair = Button(janela, text="SAIR", command= fecha_tela)
botao_sair.place(width=130, height=50, x=0, y=250)

#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
