from flask import Flask, render_template, session, redirect, request
from pymongo import Connection

app = Flask(__name__)

conn = Connection()
db = conn["logins"]

@app.route('/', methods=["GET","POST"])
def home():
	if request.method=="GET":
		try:
			uname = request.form("uname")
		except:
			uname=None
		return render_template("home.html", name=uname)
	else:
		button = request.form["logout"]
		return render_template("login.html",error="")


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
            return render_template("login.html",error="That user does not exist!")
        else:
            return render_template("home.html",name=uname)

@app.route("/signup", methods=["GET","POST"])
def signup():
	if request.method=="GET":
		return render_template("signup.html", error="")
	else:
		d = {'uname':request.form["uname"],
			'pword':request.form["pword"],
             'pwordcheck':request.form["pwordcheck"]}
		uname=request.form["uname"]
		pword=request.form["pword"]
		pwordcheck=request.form["pwordcheck"]
		try:
			test=db.logins.find({'uname':uname})[0]
		except:
			test=None
		if(test != None):
			return render_template("signup.html",error="That username is already being used.")
		else:
			if(pword==pwordcheck):
				db.logins.insert(d)
				print db.logins.find()
				return render_template("home.html",name=uname)
			else:
				return render_template("signup.html", error="Passwords did not match")





if __name__=="__main__":
    app.debug=True
    app.run();
