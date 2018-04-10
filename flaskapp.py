from flask import Flask, render_template
app = Flask(__name__)

app.config.update(
	TEMPLATES_AUTO_RELOAD = True
)

@app.route('/dark')
def index():
	return render_template('index-dark.html')

@app.route('/')
def light():
	return render_template('index-light.html')

@app.route('/hey/me')
def he():
        return "Hey"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
	app.run()
