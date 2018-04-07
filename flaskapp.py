from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return "This is the index page"

@app.route('/gusty/<name>')
def gusty(name):
	return render_template('252.html', user=name);



if __name__ == '__main__':
	app.run(debug==True)
