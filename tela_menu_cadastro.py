from tkinter import*

def cadastra_membro():
    import cadastra_membro
def altera_membro():
    import altera_membro
def desativa_membro():
    import desativa_membro
def relmembro():
    import relmembro


janela = Tk()
janela.title("MENU CADASTRO")
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

#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
