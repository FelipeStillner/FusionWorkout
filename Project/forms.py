from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, DecimalField, IntegerField, BooleanField
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


