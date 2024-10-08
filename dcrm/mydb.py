import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'sage',
    password = 'Fafnir89'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE sage")

print("Fatto!")