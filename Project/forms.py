from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, DecimalField, IntegerField, BooleanField, DateField, TimeField
from wtforms.validators import Email, InputRequired, EqualTo

class loginForm(FlaskForm):
    email = StringField(validators=[Email(), InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    remember = BooleanField("Remember me", validators=[])
    submit = SubmitField("Login", validators=[])

class signupForm(FlaskForm):
    email = StringField(validators=[Email(), InputRequired()])
    name = StringField(validators=[InputRequired()])
    weight = DecimalField(validators=[InputRequired()])
    height = IntegerField(validators=[InputRequired()])
    sex = RadioField('Sex', choices=[('M','Male'),('F','Female')], validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), EqualTo("confirmPassword")])
    confirmPassword = PasswordField("Confirm Password")
    submit = SubmitField("SignUp", validators=[])

class deleteRegisterForm(FlaskForm):
    id = IntegerField(validators=[InputRequired()])
    submit = SubmitField("DeleteRegister", validators=[])
    
class scheduleForm(FlaskForm):
    id = IntegerField(validators=[InputRequired()])
    submit = SubmitField("Shedule", validators=[])
    
class viewDietForm(FlaskForm):
    idDiet = IntegerField(validators=[InputRequired()])
    submitDiet = SubmitField("viewDiet", validators=[])
    
class viewExerciseForm(FlaskForm):
    idExer = IntegerField(validators=[InputRequired()])
    submitExer = SubmitField("viewExercise", validators=[])

class addFoodForm(FlaskForm):
    clientid = IntegerField(validators=[InputRequired()])
    day = IntegerField(validators=[InputRequired()])
    name = StringField(validators=[InputRequired()])
    quantity = IntegerField(validators=[InputRequired()])
    calories = IntegerField(validators=[InputRequired()])
    submit = SubmitField("addFood", validators=[])
    
class removeFoodForm(FlaskForm):
    id = IntegerField(validators=[InputRequired()])
    submit = SubmitField("removeFood", validators=[])
    
class addCircuitForm(FlaskForm):
    aCclientid = IntegerField(validators=[InputRequired()])
    aCday = IntegerField(validators=[InputRequired()])
    aCname = StringField(validators=[InputRequired()])
    aCrepetitions = IntegerField(validators=[InputRequired()])
    aCsubmit = SubmitField("addCircuit", validators=[])
    
class removeCircuitForm(FlaskForm):
    rCid = IntegerField(validators=[InputRequired()])
    rCsubmit = SubmitField("removeCircuit", validators=[])
    
class addWorkoutForm(FlaskForm):
    aWcircuitid = IntegerField(validators=[InputRequired()])
    aWname = StringField(validators=[InputRequired()])
    aWrepetitions = IntegerField(validators=[InputRequired()])
    aWduration = IntegerField(validators=[InputRequired()])
    aWsubmit = SubmitField("addWorkout", validators=[])
    
class removeWorkoutForm(FlaskForm):
    rWid = IntegerField(validators=[InputRequired()])
    rWsubmit = SubmitField("removeWorkout", validators=[])
    
class manageAppointmentForm(FlaskForm):
    personalid = IntegerField(validators=[InputRequired()])
    time = TimeField(validators=[InputRequired()])
    date = DateField(validators=[InputRequired()])
    submit = SubmitField("manageAppointment", validators=[])