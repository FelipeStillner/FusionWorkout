from flask import Flask
from flask import render_template, redirect, url_for
from flask import session, request
from forms import *
from User import User
from Client import Client
from Appointment import Appointment
from Food import Food
from Circuit import Circuit
from Workout import Workout

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
    form = signupForm()
    if form.validate_on_submit():
        if User.notRegistered(form.email.data):
            print("teste")
            Client.new(
                form.email.data,
                form.name.data,
                form.password.data,
                form.weight.data,
                form.height.data,
                form.sex.data,
            )
            return redirect(url_for("login"))
    return render_template("signup.html", form=form)


@app.route("/logout")
def logout():
    if "user" in session:
        del session["user"]
    return redirect(url_for("index"))


@app.route("/profile", methods=["POST", "GET"])
def profile():
    user = User(session["user"])
    if user.kind == "C":
        session["client"] = session["user"]
        return render_template("client.html", name=user.name)
    elif user.kind == "P":
        exerForm = viewExerciseForm()
        if exerForm.validate_on_submit():
            session["client"] = exerForm.idExer.data
            client = Client(session["client"])
            return render_template("exerciseplan.html", name=client.name)
        dietForm = viewDietForm()
        if dietForm.validate_on_submit():
            session["client"] = dietForm.idDiet.data
            client = Client(session["client"])
            return render_template("diet.html", name=client.name)
        return render_template(
            "personal.html", name=user.name, exerForm=exerForm, dietForm=dietForm
        )
    elif user.kind == "M":
        exerForm = viewExerciseForm()
        if exerForm.validate_on_submit():
            session["client"] = exerForm.idExer.data
            client = Client(session["client"])
            return render_template("exerciseplan.html", name=client.name)
        dietForm = viewDietForm()
        if dietForm.validate_on_submit():
            session["client"] = dietForm.idDiet.data
            client = Client(session["client"])
            return render_template("diet.html", name=client.name)
        return render_template(
            "manager.html", name=user.name, exerForm=exerForm, dietForm=dietForm
        )
    print("ERROR")
    return redirect(url_for("logout"))


@app.route("/food", methods=["POST"])
def food():
    day = int(request.args.get("day"))
    client = Client(session["client"])
    foods = client.diet.foods[day]
    data = []
    for food in foods:
        data.append((food.id, food.name, food.quantity, food.energy))
    return render_template("food.html", data=data, day=days[day], name=client.name)


@app.route("/diet")
def diet():
    client = Client(session["client"])
    return render_template("diet.html", name=client.name)


@app.route("/changediet", methods=["POST", "GET"])
def changediet():
    addForm = addFoodForm()
    if addForm.validate_on_submit():
        Food.add(
            addForm.clientid.data,
            addForm.day.data,
            addForm.name.data,
            addForm.quantity.data,
            addForm.calories.data,
        )
        return redirect(url_for("profile"))
    removeForm = removeFoodForm()
    if removeForm.validate_on_submit():
        Food.remove(removeForm.id.data)
        return redirect(url_for("profile"))
    return render_template(
        "changediet.html", addFoodForm=addForm, removeFoodForm=removeForm
    )


@app.route("/workout", methods=["POST"])
def workout():
    c_id = int(request.args.get("id"))
    day = session["day"]
    client = Client(session["client"])
    circuits = client.exercise_plan.circuits[day]
    data = []
    for c in circuits:
        if c.id == c_id:
            circuit = c
            break
    for workout in circuit.workouts:
        data.append((workout.id, workout.name, workout.repetitions, workout.duration))
    return render_template(
        "workout.html", data=data, day=days[day], name=client.name, circuit=circuit.name
    )


@app.route("/circuit", methods=["POST"])
def circuit():
    day = int(request.args.get("day"))
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


@app.route("/changeexerciseplan", methods=["POST", "GET"])
def changeexerciseplan():
    addCForm = addCircuitForm()
    if addCForm.validate_on_submit():
        Circuit.add(
            addCForm.aCclientid.data,
            addCForm.aCday.data,
            addCForm.aCname.data,
            addCForm.aCrepetitions.data,
        )
        return redirect(url_for("profile"))
    removeCForm = removeCircuitForm()
    if removeCForm.validate_on_submit():
        Circuit.remove(removeCForm.rCid.data)
        return redirect(url_for("profile"))
    addWForm = addWorkoutForm()
    if addWForm.validate_on_submit():

        Workout.add(
            addWForm.aWcircuitid.data,
            addWForm.aWname.data,
            addWForm.aWrepetitions.data,
            "0:00:" + str(addWForm.aWduration.data),
        )
        return redirect(url_for("profile"))
    removeWForm = removeWorkoutForm()
    if removeWForm.validate_on_submit():
        Workout.remove(removeWForm.rWid.data)
        return redirect(url_for("profile"))
    return render_template(
        "changeexerciseplan.html",
        addCForm=addCForm,
        removeCForm=removeCForm,
        addWForm=addWForm,
        removeWForm=removeWForm,
    )


@app.route("/schedule", methods=["POST", "GET"])
def schedule():
    form = scheduleForm()
    if form.validate_on_submit():
        client = Client(session["client"])
        client.set_appointment(form.id.data)
        return redirect(url_for("profile"))
    return render_template("schedule.html", form=form)


@app.route("/manageappointment", methods=["POST", "GET"])
def manageappointment():
    form = manageAppointmentForm()
    if form.validate_on_submit():
        Appointment.add(form.date.data, form.personalid.data, form.time.data)  # TODO: FORM
    return render_template("manageappointment.html", form = form)


@app.route("/times")
def times():
    user = User(session["user"])
    if user.kind == "C":
        data = []
        schedules = Appointment.from_client(int(session["client"]))
        for s in schedules:
            data.append((s.id, s.clientid, s.personalid, s.date, s.time))
        return render_template("times.html", name=user.name, data=data)
    elif user.kind == "P":
        data = []
        schedules = Appointment.from_personal(int(session["user"]))
        for s in schedules:
            data.append((s.id, s.clientid, s.personalid, s.date, s.time))
        return render_template("times.html", name=user.name, data=data)
    elif user.kind == "M":
        data = []
        schedules = Appointment.all()
        for s in schedules:
            data.append((s.id, s.clientid, s.personalid, s.date, s.time))
        return render_template("times.html", name=user.name, data=data)
    return render_template("times.html")


@app.route("/deleteregister", methods=["POST", "GET"])
def deleteregister():
    form = deleteRegisterForm()
    if form.validate_on_submit():
        Client.delete(form.id.data)
        return redirect(url_for("profile"))
    return render_template("deleteregister.html", form=form)
