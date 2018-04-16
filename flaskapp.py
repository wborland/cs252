from flask import Flask, render_template, send_from_directory
import os

import db
import db.util
import user.db


app = Flask(__name__)

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
	return user.db.create_user()

	
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
	app.run()
