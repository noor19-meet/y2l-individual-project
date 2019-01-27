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

@app.route('/' , methods = ['GET','POST'])
def login_page():
	
    if request.method == 'POST':
        user = databases.query_by_name(request.form["name"])
        print(request.form['name'])
        if user is not None:
            if user.password == request.form["password"]:
                session['username'] = user.name
                return redirect(url_for("homepage.html"))

            else:
                error = 'password does not match'
                return render_template('homepage.html', error = error)
        else:

            error = 'username does not exist'
            return render_template('homepage.html', error = error)

    else:

        return render_template('homepage.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True)