import mysql.connector
def connection():
    con=mysql.connector.connect(host="shortline.proxy.rlwy.net",user="root",password="ykyTiAkFsOCYVWLCVFHOzvlezOlOfdml",database="railway",port="56916")
    # print("jay")
    return con
    
connection()
