import mysql.connector
def connection():
    con=mysql.connector.connect(host="ballast.proxy.rlwy.net",user="root",password="fyCCgcmVZMbnkXiXSvRRAWIKwUnbBWZr",database="railway",port="38908")
    # print("jay")
    return con
    
connection()
