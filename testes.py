import mysql.connector


db = mysql.connector.connect(host='localhost',
                             database='templarios',
                             user='root',
                             password='Janete4353',
                             auth_plugin='mysql_native_password')

cursor = db.cursor()
cursor.execute('''SELECT * FROM membros''')
