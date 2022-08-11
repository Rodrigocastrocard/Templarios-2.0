from tkinter import*

def cadastro ():
    janela.destroy()
    import tela_menu_cadastro

def financeiro():
    janela.destroy()
    import tela_menu_financeiro

def configuracao():
    janela.destroy()
    import tela_menu_configuracao


janela = Tk()
janela.title("MENU PRINCIPAL")
janela.attributes('-fullscreen', True)
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)

botao_cadastro = Button(janela, text="CADASTRO", command= cadastro)
botao_cadastro.grid(column=0, row=1, padx=10, pady=10)
botao_financeiro = Button(janela, text="FINANCEIRO", command= financeiro)
botao_financeiro.grid(column=0, row=2, padx=10, pady=10)
botao_configuracao = Button(janela, text="CONFIGURACAO", command= configuracao)
botao_configuracao.grid(column=0, row=3, padx=10, pady=10)
botao_voltar = Button(janela, text="SAIR", command= janela.destroy)
botao_voltar.grid(column=0, row=4, padx=10, pady=10)


#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
