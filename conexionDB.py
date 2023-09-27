import mysql.connector

def conexionBD():
    mydb= mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        db='senasoft'
        )
    if mydb:
        print("Conexión exitosa")
    else:
        print("Error de conexión")
    return mydb