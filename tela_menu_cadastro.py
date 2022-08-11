from tkinter import*

def cadastra_membro():
    janela.destroy()
    import cadastra_membro
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


janela = Tk()
janela.title("MENU CADASTRO")
janela.attributes('-fullscreen', True)
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)

botao_cadastra = Button(janela, text="CADASTRAR", command= cadastra_membro)
botao_cadastra.grid(column=0, row=1, padx=10, pady=10)
botao_altera = Button(janela, text="ALTERAR", command= altera_membro)
botao_altera.grid(column=0, row=2, padx=10, pady=10)
botao_inativa = Button(janela, text="INATIVAR", command= desativa_membro)
botao_inativa.grid(column=0, row=3, padx=10, pady=10)
botao_relatorio = Button(janela, text="RELATORIO", command= relmembro)
botao_relatorio.grid(column=0, row=4, padx=10, pady=10)
botao_relatorio = Button(janela, text="VOLTAR", command= menu_principal)
botao_relatorio.grid(column=0, row=5, padx=10, pady=10)

#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
