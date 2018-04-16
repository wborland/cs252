from flask import Flask, render_template, send_from_directory, flash, redirect, session
from forms import LoginForm, PostForm
from flask_login import current_user, login_user
import os

import db
import db.util
import user.db


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

@app.route('/db')
def db():
	out = user.db.add_user("Will", "BORLAND", "Testing", "password")
	print(out)
	return str(out)
	
@app.route('/logout')
def logout():
        session.pop('username', None)
        return redirect('/')

@app.route('/login')
def login():
        #if current_user.is_authrnticated:
            #flash('You are already logged in')
            #return redirect('/')

        form = LoginForm()
        return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def login2():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Logged in as {} with password {}'.format(
                form.email.data, form.password.data))
            session['username'] = form.email.data
            return redirect('/')
        else :
            flash('You must fill out both fields')
            return render_template('login.html', form=form)

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

