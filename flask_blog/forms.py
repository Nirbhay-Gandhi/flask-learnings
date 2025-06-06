from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class UserRegistrationForm(FlaskForm):
    
    username = StringField('Username',  #label for the field
                           validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    
    password = PasswordField('Password',
                            validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirmpassword',
                            validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')



class UserLoginForm(FlaskForm):
    
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    
    password = PasswordField('Password',
                            validators=[DataRequired()])

    remember = BooleanField('Remember Me')    
    submit = SubmitField('Login')