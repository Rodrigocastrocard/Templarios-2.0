from tkinter import*

def cria_tabelas():
    import cria_tabelas

def teste_conexao():
    import teste_conexao


janela = Tk()
janela.title("MENU CONFIGURACOES")
#texto = Label(janela, text="Clique em cadastrar, para incluir um novo cadastro")
#texto.grid(column=0, row=0, padx=10, pady=10)

botao_tabelas = Button(janela, text="CRIAR TABELAS", command= cria_tabelas)
botao_tabelas.grid(column=0, row=1, padx=10, pady=10)
botao_teste = Button(janela, text="TESTAR CONEXAO", command= teste_conexao)
botao_teste.grid(column=0, row=2, padx=10, pady=10)

#texto_resposta = Label(janela, text="")
#texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
