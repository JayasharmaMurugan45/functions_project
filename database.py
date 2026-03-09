import mysql.connector
def connection():
    con=mysql.connector.connect(host="localhost",user="root",password="jay@123",database="registration")
    # print("jay")
    return con
    
connection()