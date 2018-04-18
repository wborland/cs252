from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, DecimalField, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from wtforms_components import TimeField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    event = StringField('Event Name', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()], format="%m/%d/%Y")
    time = TimeField('Time', validators=[DataRequired()])
    location = StringField('Event Location', validators=[DataRequired()])
    price = DecimalField('Ticket Price (US $)', validators=[DataRequired()], places=2)
    comments = TextAreaField('Comments')
    submit = SubmitField('Post Ticket For Sale')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    venmo = BooleanField('Venmo')
    facebook = BooleanField('Facebook')
    apple = BooleanField('Apple Pay')
    android = BooleanField('Android Pay')
    dollars = BooleanField('Cash')
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPass = PasswordField('Retype Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    
