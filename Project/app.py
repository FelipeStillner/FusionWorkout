from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request
from forms import loginForm
from User import User
from Client import Client
from Food import Food

app = Flask(__name__)
app.config["SECRET_KEY"] = "dfewfew123213rwdsgert34tgfd1234trgf"

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()
    if form.validate_on_submit():
        validate = User.validate(form.email.data, form.password.data)
        if validate[0]:
            session["user"] = validate[1]
            return redirect(url_for("profile"))
    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = loginForm()
    Client.new("p@p.com", "p", "p", 1, 1, True)
    return render_template("signup.html", form=form)


@app.route("/logout")
def logout():
    if "user" in session:
        del session["user"]
    return redirect(url_for("index"))


@app.route("/profile")
def profile():
    user = User(session["user"])
    if user.kind == "C":
        session["client"] = session["user"]
        return render_template("client.html", name=user.name)
    elif user.kind == "P":
        return render_template("personal.html", name=user.name)
    elif user.kind == "M":
        return render_template("manager.html", name=user.name)
    print("ERROR")
    return redirect(url_for("logout"))


@app.route("/food", methods=["POST"])
def food():
    day = int(request.args.get('day'))
    client = Client(session["client"])
    foods = client.diet.foods[day]
    data = []
    for food in foods:
        data.append((food.name, food.quantity, food.energy))
    return render_template("food.html", data=data, day=days[day], name=client.name)


@app.route("/diet")
def diet():
    client = Client(session["client"])
    return render_template("diet.html", name=client.name)


@app.route("/diet", methods=["POST"])
def diet_post():
    return redirect(url_for("diet"))


@app.route("/changediet")
def changediet():
    return render_template("changediet.html")


@app.route("/workout", methods=["POST"])
def workout():
    c_id = int(request.args.get('id'))
    day = session['day']  # TODO
    client = Client(session["client"])
    circuits = client.exercise_plan.circuits[day]
    data = []
    for c in circuits:
        if c.id == c_id:
            circuit = c
            break
    for workout in circuit.workouts:
        data.append((workout.id, workout.name, workout.repetitions, workout.duration))
    return render_template("workout.html", data=data, day=days[day], name=client.name, circuit= circuit.name)


@app.route("/circuit", methods=["POST"])
def circuit():
    day = int(request.args.get('day'))
    session["day"] = day
    client = Client(session["client"])
    circuits = client.exercise_plan.circuits[day]
    data = []
    for circuit in circuits:
        data.append((circuit.id, circuit.name, circuit.repetitions, 0))
    return render_template("circuit.html", data=data, day=days[day], name=client.name)


@app.route("/exerciseplan")
def exerciseplan():
    client = Client(session["client"])
    return render_template("exerciseplan.html", name=client.name)


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
