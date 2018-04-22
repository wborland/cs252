from flask import Flask, render_template, send_from_directory, flash, redirect, session, jsonify, request
from forms import LoginForm, PostForm, RegisterForm, SearchForm, ResultForm
from datetime import date
import os

import db
import user.db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvaz@purdue.edu'

app.config.update(
	TEMPLATES_AUTO_RELOAD = True
)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/grr')
def grr():
        return '<html>\nA Systems <em><b>God</b></em>\n</html>'

@app.route('/dark')
def index():
	return render_template('index-dark.html')

@app.route('/')
def light():
        return redirect('/searchTix')
	#return render_template('index-light.html')

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
        form = LoginForm()

        return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def login2():
        form = LoginForm()
        if form.validate_on_submit(): #and user exists in db
            flash('Logged in as {} with password {}'.format(
                form.email.data, form.password.data))

            email = form.email.data
            password = form.password.data
            print("Hello", user.db.check_login(email, password))


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

        user.db.add_user(form.firstName.data, form.lastName.data, form.email.data, form.password.data, methods)

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
            if form.price.data < 0:
                flash('Price must be a positive number')
                return render_template('postTicket.html', form=form)
            flash('Post for event {} on date {} at time {} location {} for price {} with comments \'{}\''.format(
                form.event.data, form.date.data.strftime('%x'), form.time.data, form.location.data, form.price.data, form.comments.data))

            print(user.db.add_ticket(3, session["username"], form.event.data, form.date.data, form.price.data, form.comments.data, form.location.data))

            return redirect('/')
        else :
            flash('That was not valid')
            return render_template('postTicket.html', form=form)

@app.route('/searchTix')
def searchTix():
        form = SearchForm()
        return render_template('searchTicket.html', form=form)

@app.route('/searchTix', methods=['POST'])
def searchTix2():
    form = SearchForm()
    and_flag = 0
    sql_cmd = "SELECT user_id, name, event, date_time, price, description, location FROM `studentTix`.`tickets` WHERE " 
    out = ""

    if len(form.event.data) > 0:
        and_flag = 1
        sql_cmd += "event LIKE " + "'%" + form.event.data + "%'"

    if len(form.location.data) > 0:
        if and_flag == 1:
            sql_cmd += " AND location LIKE " + "'%" + form.location.data + "%'"
        else:
            and_flag = 1
            sql_cmd += "location LIKE " + "'%" + form.location.data + "%'"

    if form.date.data is not None:
        if and_flag == 1:
            sql_cmd += " AND date_time LIKE " + "'%" + str(form.date.data) + "%'"
        else:
            and_flag = 1
            sql_cmd += " date_time LIKE " + "'%" + str(form.date.data) + "%'"

    if form.time.data is not None:
        if and_flag == 1:
            sql_cmd += " AND date_time LIKE " + "'%" + str(form.time.data) + "%'"
        else:
            and_flag = 1
            sql_cmd += " date_time LIKE " + "'%" + str(form.time.data) + "%'"


    if form.price1.data == True:
        if and_flag == 1:
            sql_cmd += " AND price BETWEEN 0 AND 19.99"
        else:
            and_flag = 1
            sql_cmd += " price BETWEEN 0 AND 19.99"

    if form.price2.data == True:
        if and_flag == 1:
            sql_cmd += " OR price BETWEEN 20 AND 39.99"
        else:
            and_flag = 1
            sql_cmd += " price BETWEEN 20 AND 39.99"


    if form.price3.data == True:
        if and_flag == 1:
            sql_cmd += " OR price BETWEEN 40 AND 59.99"
        else:
            and_flag = 1
            sql_cmd += " price BETWEEN 40 AND 59.99"


    if form.price4.data == True:
        if and_flag == 1:
            sql_cmd += " OR price BETWEEN 60 AND 79.99"
        else:
            and_flag = 1
            sql_cmd += " price BETWEEN 60 AND 79.99"



    if form.price5.data == True:
        if and_flag == 1:
            sql_cmd += " OR price BETWEEN 80 AND 99.99"
        else:
            and_flag = 1
            sql_cmd += " price BETWEEN 80 AND 99.99"



    if form.price6.data == True:
        if and_flag == 1:
            sql_cmd += " OR price >= 100.00"
        else:
            and_flag = 1
            sql_cmd += " price >= 100.00"


    if and_flag == 0:
        sql_cmd = sql_cmd[:-7]

    return_me = user.db.run_command(sql_cmd)
    return str(return_me)


@app.route('/basicsearch', methods=['GET', 'POST'])
def basic_search():
    out = user.db.basic_search()
    if request.method == 'GET':
        #return jsonify(search=out)
        return render_template('ticketResults.html', results=out)
    else:
        for result in out:
            if result[1] in request.form:
                return result[1]
        else:
            return 'Something\'s wrong'


@app.route('/hey/me')
def he():
        return "Hey"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
        app.secret_key = 'dvaz'
        app.run()

