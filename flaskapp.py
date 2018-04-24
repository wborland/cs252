from flask import Flask, render_template, send_from_directory, flash, redirect, session, jsonify, request, url_for
from forms import LoginForm, PostForm, RegisterForm, SearchForm, ResultForm
from datetime import date
import os

import db
import user.db
import datetime

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

@app.route('/')
def light():
    if "username" in session:
        return redirect('/dashboard')
    else:
        return render_template("index-light.html")


@app.route('/dashboard')
def dashbaord():
    ticket = user.db.get_user_tickets(user.db.get_user_id(session["username"]))


    return render_template("dashboard.html", tickets = ticket)

@app.route('/db')
def db():
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
        if form.validate_on_submit() and user.db.check_login(form.email.data, form.password.data) == 1: #and user exists in db
            email = form.email.data
            password = form.password.data
            print("Hello", user.db.check_login(email, password))

            session['username'] = form.email.data
            session['id'] = user.db.get_user_id(form.email.data)
            return redirect('/')
        else :
            return render_template('login.html', form=form, error="Incorrect Credentials")

@app.route('/register')
def register():
        form = RegisterForm()
        return render_template('register.html', form=form)

@app.route('/register', methods=['POST'])
def register2():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirmPass.data:
            return render_template('register.html', form=form, error="Password do not match.")

        if form.venmo.data == False and form.facebook.data == False and form.apple.data == False and form.android.data == False and form.dollars.data == False:
            return render_template('register.html', form=form, error="You must select at least one form of payment.")

        methods = ''
        for field in form:
            if field.type == "BooleanField" and field.data == True:
                methods += field.label.text
                methods += ','

        session['username'] = form.email.data
        user.db.add_user(form.firstName.data, form.lastName.data, form.email.data, form.password.data, methods)
        session['id'] = user.db.get_user_id(form.email.data)

        return redirect('/')
    else:
        return render_template('register.html', form=form, error="Please fill out all fields.")

@app.route('/postTix')
def postTix():
    if "username" in session:
        form = PostForm()
        return render_template('postTicket.html', form=form)
    else:
        return redirect(url_for("light"))

@app.route('/postTix', methods=['POST'])
def postTix2():
        form = PostForm()
        if form.validate_on_submit():
            print(user.db.add_ticket(user.db.get_user_id(session["username"]), user.db.get_user_name(user.db.get_user_id(session["username"])), form.event.data, datetime.datetime.combine(form.date.data, form.time.data), form.price.data, form.comments.data, form.location.data))
            return redirect('/')
        else :
            return render_template('postTicket.html', form=form)

@app.route('/searchTix')
def searchTix():
        form = SearchForm()
        return render_template('searchTicket.html', form=form)

@app.route('/searchTix', methods=['POST'])
def searchTix2():
    form = SearchForm()
    and_flag = 0
    sql_cmd = "SELECT user_id, name, event, date_time, price, description, location, payment FROM `studentTix`.`tickets` RIGHT JOIN studentTix.user ON user.id = tickets.user_id WHERE user.id = tickets.user_id " 
    out = ""

    if len(form.event.data) > 0:
        and_flag = 1
        sql_cmd += "AND event LIKE " + "'%" + form.event.data + "%'"

    if len(form.location.data) > 0:
            sql_cmd += " AND location LIKE " + "'%" + form.location.data + "%'"

    if form.date.data is not None:
            sql_cmd += " AND date_time LIKE " + "'%" + str(form.date.data) + "%'"

    if form.time.data is not None:
            sql_cmd += " AND date_time LIKE " + "'%" + str(form.time.data) + "%'"

    if form.price1.data == True:
            sql_cmd += " AND price BETWEEN 0 AND 19.99"

    if form.price2.data == True:
            sql_cmd += " OR price BETWEEN 20 AND 39.99"

    if form.price3.data == True:
            sql_cmd += " OR price BETWEEN 40 AND 59.99"

    if form.price4.data == True:
            sql_cmd += " OR price BETWEEN 60 AND 79.99"

    if form.price5.data == True:
            sql_cmd += " OR price BETWEEN 80 AND 99.99"

    if form.price6.data == True:
            sql_cmd += " OR price >= 100.00"

    sql_cmd += " AND NOT user_id = " + user.db.get_user_id(session["username"]) 

    return_me = user.db.run_command(sql_cmd)
    session['results'] = return_me
    return redirect('/results')


@app.route('/basicsearch', methods=['GET', 'POST'])
def basic_search():
    if request.method == 'GET':
        out = user.db.basic_search()
        #return jsonify(search=out)
        return render_template('ticketResults.html', results=out)
    else:
        return request.form.get('message')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return render_template('ticketResults.html', results=session['results'])
    else:
        return request.form.get('message')


@app.route('/usermessage/<to_id>/<message>')
def messageseller(to_id,message):
    if "username" in session:
        user.db.add_message(to_id, user.db.get_user_id(session['username']), message)
        return redirect(url_for("messages"))
    else:
        print("message")
        return redirect(url_for("light"))


@app.route('/messages')
def messages():
    if "username" in session:
        id = user.db.get_user_id(session["username"])
        out = user.db.get_all_user_messages(id)
        return render_template('messages.html', users=user.db.get_all_user_messages(id))
    else:
        print("method")
        return redirect(url_for("light"))

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    to_id = request.form['to_id']
    email = session['username']
    from_id = user.db.get_user_id(email)

    user.db.add_message(to_id, from_id, message)

    return redirect(url_for("messages"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
        app.secret_key = 'dvaz'
        app.run()

