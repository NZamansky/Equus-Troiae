from flask import Flask, render_template, session, redirect, request
from pymongo import Connection

app = Flask(__name__)

conn = Connection()
db = conn["logins"]

@app.route('/', methods=["GET","POST"])
def home():
    uname = request.form("uname")
    return render_template("home.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html",error="")
    else:
        # post
        button = request.form["b"]
        uname = request.form["uname"]
        pword = request.form["pword"]
        if(db.logins.find({'uname':uname}) != None):
            return render_template("login.html",error="Already a user with that name")
        else:
            return render_template("home.html",name=uname)

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        d = {'uname':request.form["uname"],
             'pword':request.form["pword"]}
        db.logins.insert(d)
        print db.logins.find()
        return render_template("home.html",name=uname)









if __name__=="__main__":
    app.debug=True
    app.run();
