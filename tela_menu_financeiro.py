from tkinter import*

def recebimento ():
    janela.destroy()
    import recebimento

def pagamento():
    janela.destroy()
    import pagamentos

def altera():
    janela.destroy()
    import altera_fin

def relatorio():
    janela.destroy()
    import relatorio_fin

def menu_principal():
    janela.destroy()
    import tela_menu_principal


janela = Tk()
janela.title("MENU FINANCEIRO")
janela.attributes('-fullscreen', True)
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)

botao_receber = Button(janela, text="RECEBIMENTO", command= recebimento)
botao_receber.grid(column=0, row=1, padx=10, pady=10)
botao_pagamento = Button(janela, text="PAGAMENTO", command= pagamento)
botao_pagamento.grid(column=0, row=2, padx=10, pady=10)
botao_altera = Button(janela, text="ALTERACAO", command= altera)
botao_altera.grid(column=0, row=3, padx=10, pady=10)
botao_relatorio = Button(janela, text="RELATORIO", command= relatorio)
botao_relatorio.grid(column=0, row=4, padx=10, pady=10)
botao_relatorio = Button(janela, text="VOLTAR", command= menu_principal)
botao_relatorio.grid(column=0, row=5, padx=10, pady=10)


#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
