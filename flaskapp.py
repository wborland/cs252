from flask import Flask, render_template
app = Flask(__name__)

app.config.update(
	TEMPLATES_AUTO_RELOAD = True
)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/gusty/<name>')
def gusty(name):
	return render_template('252.html', user=name)

@app.route('/hey/me')
def he():
        return "Hey"


if __name__ == '__main__':
	app.run()
