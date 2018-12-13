from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "Whatever"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/This/is/the/route')
def new():
    return "You found the route!"

@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    name = request.form['name']
    email = request.form['email']

    if not name:
        flash("Name is required.")
    if not email:
        flash("Email is required.")

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        session['name'] = name
        session['email'] = email
        return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/id/<num>')
def id(num):
    session['id'] = num
    return redirect('/success')

@app.route('/clear')
def clear():
    session.clear() # clears all keys in session
    return redirect('/')

app.run(debug=True, port=5432)
