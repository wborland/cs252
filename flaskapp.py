from flask import Flask, render_template, send_from_directory, flash, redirect, session
from forms import LoginForm, PostForm, RegisterForm
from flask_login import current_user, login_user
import os

import db
import db.util


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvaz@purdue.edu'

app.config.update(
	TEMPLATES_AUTO_RELOAD = True
)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/dark')
def index():
	return render_template('index-dark.html')

@app.route('/')
def light():
	return render_template('index-light.html')

@app.route('/logout')
def logout():
        session.pop('username', None)
        return redirect('/')

@app.route('/login')
def login():
        form = LoginForm()
        return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def login2():
        form = LoginForm()
        if form.validate_on_submit(): #and user exists in db
            flash('Logged in as {} with password {}'.format(
                form.email.data, form.password.data))
            session['username'] = form.email.data
            return redirect('/')
        else :
            flash('You must fill out both fields')
            return render_template('login.html', form=form)

@app.route('/register')
def register():
        form = RegisterForm()
        return render_template('register.html', form=form)

@app.route('/register', methods=['POST'])
def register2():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirmPass.data:
            flash('Passwords must match')
            return render_template('register.html', form=form)

        if form.venmo.data == False and form.facebook.data == False and form.apple.data == False and form.android.data == False and form.dollars.data == False:
            flash('You must select at least one form of payment')
            return render_template('register.html', form=form)

        methods = ''
        for field in form:
            if field.type == "BooleanField" and field.data == True:
                methods += field.label.text
                methods += ','
        flash('selected methods: ' + methods)
        session['username'] = form.email.data
        flash('logged in as: ' + form.email.data)
        return redirect('/')
    else:
        flash('Please fill out every field')
        return render_template('register.html', form=form)

@app.route('/postTix')
def postTix():
        form = PostForm()
        return render_template('postTicket.html', form=form)

@app.route('/postTix', methods=['POST'])
def postTix2():
        form = PostForm()
        if form.validate_on_submit(): 
            flash('Post for event {} on date {} at {} for price {}'.format(
                form.event.data, form.time.data, form.location.data, form.price.data))
            return redirect('/')
        else :
            flash('That was not valid')
            return render_template('postTicket.html', form=form)


@app.route('/hey/me')
def he():
        return "Hey"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
        app.secret_key = 'dvaz'
        app.run()

