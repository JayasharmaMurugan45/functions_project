from flask import Flask,render_template,request
from database import connection
app=Flask(__name__)
@app.route('/home')
def reg():
    return render_template("home_page.html")
@app.route("/search")
def jay():
    return render_template('search.html')
@app.route('/shows',methods=['GET','post'])
def search_records():
    names=request.form.get('name')
    fathernames=request.form.get('fathername')
    villages=request.form.get('village')
    
    if not names or not fathernames or not villages:
        return render_template('error.html')
    
    con = None
    cur = None
    try:
        con=connection()
        cur=con.cursor()
        query = "SELECT * FROM register WHERE name=%s AND fathername=%s AND village=%s"
        print(f"Executing query with: name={names}, fathername={fathernames}, village={villages}")
        cur.execute(query, (names, fathernames, villages))
        valus=cur.fetchone()
        print(f"Query result: {valus}")
        if valus:
            return render_template('datashowing.html',name=valus[1],fathername=valus[2],village=valus[3],amount=valus[4])
        else:
            return render_template('error3.html')
    except Exception as e:
        print(f"ERROR in /shows: {e}")
        return render_template('error.html')
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
@app.route('/register',methods=['GET','post'])
def register_page():
    if request.method == 'GET':
        return render_template('register.html')
    
    n=request.form.get("newname")
    f=request.form.get("newfathername")
    v=request.form.get("newvillage")
    a=request.form.get("amount")
    
    if not n or not f or not v or not a:
        return render_template('error1.html')
    
    con = None
    cur = None
    try:
        con=connection()
        cur=con.cursor()    
        query="select name,fathername from register where name=%s and fathername=%s"
        print(f"Checking if exists: name={n}, fathername={f}")
        cur.execute(query,(n,f,))
        value=cur.fetchall()
        print(f"Existing records: {value}")
       
        if value :
            return render_template('error2.html')
        else:
            insert_query="insert into register (name,fathername,village,amount) values (%s,%s,%s,%s)"
            print(f"Inserting: name={n}, fathername={f}, village={v}, amount={a}")
            cur.execute(insert_query,(n,f,v,a))
            con.commit()
            print("Insert successful")
            return render_template("success.html",na=n,fa=f,va=v,am=a)
    except Exception as e:
        print(f"ERROR in /register: {e}")
        return render_template('error1.html')
    finally:
        if cur:
            cur.close()
        if con:
            con.close()
if __name__=='__main__':
    app.run(debug=True)