from flask import Flask
from flask import render_template, redirect, url_for
from flask import session

from forms import loginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

#Substituir pelo bd
users = [{'id':1,'name':'Cladomiro', 'email': 'admin@admin.com', 'password': 'admin'},
         {'id':2,'name':'Robervaldo', 'email': 'ademiro@gmail.com', 'password': 'admin'}] 


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()
    if(form.validate_on_submit()):
        for user in users:
            if(user['email']==form.email.data and user['password']==form.password.data):
                session['user']=user['id']
                return redirect(url_for("profile"))
    
        
    return render_template("login.html", form=form)


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    return redirect(url_for("signup"))


@app.route("/logout")
def logout():
    if "user" in session:
        del session['user']
    return redirect(url_for("index"))


@app.route("/profile")
def profile():
    return render_template("client.html")


@app.route("/client")
def client():
    return render_template("client.html")


@app.route("/personal")
def personal():
    return render_template("personal.html")


@app.route("/manager")
def manager():
    return render_template("manager.html")


@app.route("/food")
def food():
    return render_template("food.html")


@app.route("/diet")
def diet():
    return render_template("diet.html")


@app.route("/diet", methods=["POST"])
def diet_post():
    return redirect(url_for("diet"))


@app.route("/changediet")
def changediet():
    return render_template("changediet.html")


@app.route("/workout")
def workout():
    return render_template("workout.html")


@app.route("/circuit")
def circuit():
    return render_template("circuit.html")


@app.route("/exerciseplan")
def exerciseplan():
    return render_template("exerciseplan.html")


@app.route("/exerciseplan", methods=["POST"])
def exerciseplan_post():
    return redirect(url_for("exerciseplan"))


@app.route("/changeexerciseplan")
def changeexerciseplan():
    return render_template("changeexerciseplan.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/manageappointment")
def manageappointment():
    return render_template("manageappointment.html")


@app.route("/times")
def times():
    return render_template("times.html")


@app.route("/deleteregister")
def deleteregister():
    return render_template("deleteregister.html")


@app.route("/deleteregister", methods=["POST"])
def deleteregister_post():
    return redirect(url_for("deleteregister"))
