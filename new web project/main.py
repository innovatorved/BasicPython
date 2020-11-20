
from flask import Flask , request
from flask import render_template ,redirect ,url_for
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

i=0

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/movie')
def mov():
    return render_template("movie.html")

@app.route('/tech')
def techie():
    return render_template("tech.html")

@app.route('/tv')
def television():
    return render_template("tv.html")

@app.route('/Me' , methods = ['GET','POST'])
def contact():
    if i == 0:
         #print("True")
        if request.method == 'POST':
            #print("done")
            if 'name' in request.form and 'email'in request.form:
                name = request.form['name']
                email = request.form['email']
                msg = request.form['message']
                print(name)
                print(email)
                print(msg)
    return render_template("form.html")

####################3
'''
import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
'''
#######################
if __name__ == '__main__':
    app.run()
