from flask import Flask, render_template, session, redirect, request
from pymongo import Connection

app = Flask(__name__)

conn = Connection()
logins = conn["logins"]

@app.route('/', methods=["GET","POST"])
def home():
    uname = request.form("uname")
    return render_template("home.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        # post
        button = request.form["b"]
        uname = request.form["uname"]
        pword = request.form["pword"]
        valid_user = utils.authenticate(uname,pword)
        if button=="cancel" or not(valid_user):
            return render_template("login.html")
        else:
            return render_template("home.html",name=uname)

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        d = {'uname':request.form["uname"],
             'pword':request.form["pword"]}
        return render_template("home.html",name=uname)









if __name__=="__main__":
    app.debug=True
    app.run();
