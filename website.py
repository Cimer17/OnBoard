from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def application():
    return render_template('application.html')

@app.route("/hr")
def hr():
    return render_template('hr.html')