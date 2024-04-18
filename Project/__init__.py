from flask import Flask
from flask import render_template, redirect, url_for, request
from Project.DBManager import authenticate_user, create_user
from Project.User import User

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    u = User("client@gmail.com")
    print(u.dbg())
    return render_template("profile.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

    if (authenticate_user(email, password)):
        return redirect(url_for("logout"))
    return redirect(url_for("login"))


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    if create_user(email, name, password, "C"):
        return redirect(url_for("login"))
    return redirect(url_for("signup"))


@app.route("/logout")
def logout():
    return "Logout"
