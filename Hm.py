from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template("login.html")
database={"Hemanth":'1305',"Sri vastav":1304,"Sathwik":'13499'}
@app.route('/form_login',methods=["POST","GET"])
def login():
    name1=request.form["username"]
    lname=request.form["lastname"]
    pwd=request.form["password"]
    if name1 not in database:
        return render_template("login.html",info="Invalid user")
    else:
        if database[name1]!=pwd:
            return render_template("login.html",info="Invalid Password")
        else:
            return render_template("home.html",name=name1+lname)
if __name__=='__main__':
    app.run(debug=True)