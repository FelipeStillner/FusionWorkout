from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, InputRequired

class loginForm(FlaskForm):
    email = StringField(validators=[Email(), InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    remember = BooleanField("Remember me", validators=[])
    submit = SubmitField("Login", validators=[])