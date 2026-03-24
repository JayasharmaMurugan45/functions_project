import mysql.connector
def connection():
    con=mysql.connector.connect(host="mysql.railway.internal",user="root",password="ykyTiAkFsOCYVWLCVFHOzvlezOlOfdml",database="railway",port="3306")
    # print("jay")
    return con
    
connection()
