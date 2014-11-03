from flask import Flask, render_template, session, redirect, request
from pymongo import Connection

app = Flask(__name__)

conn = Connection()
db = conn["logins"]

uname=""

@app.route('/', methods=["GET","POST"])
def home():
        if(uname==""):
                return redirect("/login")
	elif request.method=="GET":
		return render_template("home.html", name=uname)
	else:
		button = request.form["logout"]
		return redirect("/login")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html",error="")
    else:
        uname = request.form["uname"]
        pword = request.form["pword"]
        try:
                print db.logins.find({'uname':uname, 'pword':pword})[0]
                print "vvxbxbgji"
                return redirect("/")
        except:
                return render_template("login.html",error="Either username or password is incorrect")
        #return redirect("/")

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
                                uname=request.form["uname"]
                                pword=request.form["pword"]
				print db.logins.find()
				return redirect("/")
			else:
				return render_template("signup.html", error="Passwords did not match")





if __name__=="__main__":
    app.debug=True
    app.run();
