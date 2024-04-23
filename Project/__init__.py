from flask import Flask
from flask import render_template, redirect, url_for, request
from Project.DBManager import authenticate_user, create_user
from Project.Client import Client
from Project.Application import Application

flask_app = Flask(__name__)

app = Application()


@flask_app.route("/")
def index():
    return render_template("index.html")


@flask_app.route("/login")
def login():
    return render_template("login.html")


@flask_app.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

    if authenticate_user(email, password):
        app.user = Client(email)
        return redirect(url_for("profile"))
    return redirect(url_for("login"))


@flask_app.route("/signup")
def signup():
    return render_template("signup.html")


@flask_app.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")
    if create_user(email, name, password, "C"):
        return redirect(url_for("login"))
    return redirect(url_for("signup"))


@flask_app.route("/logout")
def logout():
    app.user = None
    return redirect(url_for("index"))


@flask_app.route("/profile")
def profile():
    if app.user == None:
        return redirect(url_for("login"))
    return render_template("profile.html", name = app.user.name, email = app.user.email)

@flask_app.route("/weeklyplan")
def weeklyplan():
    if app.user == None:
        return redirect(url_for("login"))
    return render_template("weeklyplan.html", name = app.user.plan.name)

@flask_app.route("/dailyplan")
def dailyplan():
    if app.user == None:
        return redirect(url_for("login"))
    daily = app.user.plan.dailies[0]
    info = list()
    for circuit in daily.circuits:
        info.append(circuit.name)
    return render_template("dailyplan.html", name = app.user.plan.name, day = "0", info = info)


