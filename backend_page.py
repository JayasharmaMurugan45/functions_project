from flask import Flask,render_template,request
from database import connection
app=Flask(__name__)
@app.route('/')
def reg():
    return render_template("home_page.html")
@app.route("/search")
def jay():
    return render_template('search.html')
@app.route("/register")
def jaya():
    return render_template('register.html')
@app.route('/shows',methods=['GET','post'])
def jayas():
    names=request.form.get('name')
    fathernames=request.form.get('fathername')
    villages=request.form.get('village')
    con=connection()
    cur=con.cursor()
    if names and fathernames and villages:
        query="select * from register where name=%s and fathername=%s and village=%s"
        cur.execute(query,(names,fathernames,villages,))
        valus=cur.fetchone()
        if valus:
            return render_template('datashowing.html',name=valus[1],fathername=valus[2],village=valus[3],amount=valus[4])
        else:
            return render_template('error3.html')
    else:
        return render_template('error.html')
@app.route('/register',methods=['GET','post'])
def jaa():
    n=request.form.get("newname")
    f=request.form.get("newfathername")
    v=request.form.get("newvillage")
    a=request.form.get("amount")
    con=connection()
    cur=con.cursor()    
    if n and f and v and a:
        query="select name,fathername from register where name=%s and fathername=%s"
        cur.execute(query,(n,f,))
        value=cur.fetchall()
       
        if value :
            return render_template('error2.html')
        else:
            cur.execute("insert into register (name,fathername,village,amount) values (%s,%s,%s,%s)",(n,f,v,a))
            con.commit()
            cur.close()
            con.close()
            return render_template("success.html",na=n,fa=f,va=v,am=a)
    else:
        return render_template('error1.html')
if __name__=='__main__':
    app.run(debug=True)