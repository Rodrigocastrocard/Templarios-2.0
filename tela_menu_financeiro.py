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
def fecha_tela():
    janela.destroy()


janela = Tk()
janela.title("MENU FINANCEIRO")
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


botao_receber = Button(janela, text="RECEBIMENTO", command= recebimento)
botao_receber.place(width=130, height=50, x=0, y=0)
botao_pagamento = Button(janela, text="PAGAMENTO", command= pagamento)
botao_pagamento.place(width=130, height=50, x=0, y=50)
botao_altera = Button(janela, text="ALTERACAO", command= altera)
botao_altera.place(width=130, height=50, x=0, y=100)
botao_relatorio = Button(janela, text="RELATORIO", command= relatorio)
botao_relatorio.place(width=130, height=50, x=0, y=150)
botao_voltar = Button(janela, text="VOLTAR", command= menu_principal)
botao_voltar.place(width=130, height=50, x=0, y=200)
botao_sair = Button(janela, text="SAIR", command= fecha_tela)
botao_sair.place(width=130, height=50, x=0, y=250)


#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
