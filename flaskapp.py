from flask import Flask, render_template, send_from_directory, flash, redirect
from forms import LoginForm
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

@app.route('/login', methods=['GET', 'POST'])
def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Logged in as {} with password {}'.format(
                form.email.data, form.password.data))
            return redirect('/')
        return render_template('login.html', form=form)

@app.route('/hey/me')
def he():
        return "Hey"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
	app.run()
