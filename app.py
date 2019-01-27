from flask import Flask, render_template 	 	
app = Flask(__name__)

import databases


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/cars')
def cars():
	return render_template ("cars.html")

@app.route('/fps')
def fps():
	return render_template ("fps.html")

@app.route('/mmorpg')
def mmorpg():
	return render_template ("mmorpg.html")

@app.route('/moba')
def moba():
	return render_template ("moba.html")

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)