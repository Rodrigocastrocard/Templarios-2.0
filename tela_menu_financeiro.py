from tkinter import*

def recebimento ():
    import recebimento

def pagamento():
    import pagamentos

def altera():
    import altera_fin

def relatorio():
    import relatorio_fin


janela = Tk()
janela.title("MENU FINANCEIRO")
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

#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
