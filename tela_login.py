from tkinter import *
import mysql.connector
con = mysql.connector.connect(host='localhost', database='templarios', user='root', password='Janete4353')


master = Tk()
master.title('Login')
master.geometry("500x560+450+100")



#abrir nova janela



# variaveis Globais
esconda_senha = StringVar()




#importar imagens
img_fundo = PhotoImage(file="images\\usuario.png")
img_botao = PhotoImage(file="images\\entrar.png")

#criacao de labels

lab_fundo=Label(master, image=img_fundo)
lab_fundo.pack()

#criacao de caixas de entrada
en_usuario = Entry(master, bd=2, font=("Calibri",15),justify=CENTER)
en_usuario.place(width=410, height=45, x=45, y=170)

en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri",15),justify=CENTER)
en_senha.place(width=410, height=45, x=45, y=255)


def valida_credencial():
    consulta_sql = "select * from usuarios "
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    if len(linhas) == 1:  # Verifica se o retorno contém alguma linha
        master.destroy()
        import tela_menu_principal

    else:
        print('Usuário ou senha inválido !')


    #criacao de botões
en_botao = Button(master, bd=0, image=img_botao, command=valida_credencial)
en_botao.place(width=87, height=51, x=206, y=450)






master.mainloop()
