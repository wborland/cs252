from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, DecimalField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    event = StringField('Event Name', validators=[DataRequired()])
    time = DateTimeField('Date and Time', validators=[DataRequired()])
    location = StringField('Event Location', validators=[DataRequired()])
    price = DecimalField('Ticket Price', validators=[DataRequired()], places=2)
    comments = StringField('Comments')
    submit = SubmitField('Post Ticket For Sale')

