import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = '',
    password = ''
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE sage")

print("Fatto!")
