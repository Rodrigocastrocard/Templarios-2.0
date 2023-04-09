import datetime
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tkinter import*
import tkinter as tk
from tkinter import messagebox

con = mysql.connector.connect(host='localhost',
                             database='templarios',
                             user='root',
                             password='Janete4353',
                             auth_plugin='mysql_native_password')






def alterar_cliente(self):
    self.capturar_campos()
    self.db_conect()
    self.cursor.execute("""UPDATE clientes SET nome = ?, telefone = ?, cidade = ? 
    WHERE id = ?;
    """, (self.nome, self.telefone, self.cidade, self.codigo))
    self.conexao.commit()
    self.db_desconect()
    self.limpar_campos()
    self.select_lista()