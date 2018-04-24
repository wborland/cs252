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
    dollars = BooleanField('Cash (In Person)')
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPass = PasswordField('Retype Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    
class SearchForm(FlaskForm):
    submit = SubmitField('Search')
    event = StringField('Event Name')
    date = DateField('Date', format="%m/%d/%Y")
    time = TimeField('Time')
    location = StringField('Event Location')
    #price = NumberRangeField('Price Range')
    price1 = BooleanField('$0 - $19.99')
    price2 = BooleanField('$20 - $39.99')
    price3 = BooleanField('$40 - $59.99')
    price4 = BooleanField('$60 - $79.99')
    price5 = BooleanField('$80 - $99.99')
    price6 = BooleanField('$100+')

class ResultForm(FlaskForm):
    seller = str('')
    submit = SubmitField('Message seller about this ticket')
