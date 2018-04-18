from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, DecimalField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    event = StringField('Event Name', validators=[DataRequired()])
    time = DateTimeField('Date and Time', validators=[DataRequired()])
    location = StringField('Event Location', validators=[DataRequired()])
    price = DecimalField('Ticket Price (US $)', validators=[DataRequired()], places=2)
    comments = StringField('Comments')
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
    
