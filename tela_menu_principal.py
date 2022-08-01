from tkinter import*

def cadastro ():
    import tela_menu_cadastro

def financeiro():
    import tela_menu_financeiro

def configuracao():
    import tela_menu_configuracao


janela = Tk()
janela.title("MENU PRINCIPAL")
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)

botao_cadastro = Button(janela, text="MENU CADASTRO", command= cadastro)
botao_cadastro.grid(column=0, row=1, padx=10, pady=10)
botao_financeiro = Button(janela, text="MENU FINANCEIRO", command= financeiro)
botao_financeiro.grid(column=0, row=2, padx=10, pady=10)
botao_configuracao = Button(janela, text="MENU CONFIGURACAO", command= configuracao)
botao_configuracao.grid(column=0, row=3, padx=10, pady=10)

#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
