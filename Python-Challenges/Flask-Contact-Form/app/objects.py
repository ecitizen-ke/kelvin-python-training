from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

# Define a FlaskForm subclass named LoginForm


class LoginForm(FlaskForm):
    # Define a StringField for 'username' with InputRequired validator
    username = StringField('Username', validators=[InputRequired()])

    # Define a PasswordField for 'password' with InputRequired validator
    password = PasswordField('Password', validators=[InputRequired()])
