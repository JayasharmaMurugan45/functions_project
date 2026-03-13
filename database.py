import mysql.connector
def connection():
    con=mysql.connector.connect(host="ballast.proxy.rlwy.net",user="root",password="fyCCgcmVZMbnkXiXSvRRAWIKwUnbBWZr",database="railway",port="38908")
    # print("jay")
    cur=con.cursor()
    query = "ALTER TABLE registar MODIFY id INT NOT NULL AUTO_INCREMENT PRIMARY KEY"

    cur.execute(query)

    con.commit()
    return con
    
connection()
