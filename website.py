from flask import Flask, redirect, render_template, jsonify, request
import DB.database
import requests


app = Flask(__name__)
db = DB.database.Database()

@app.route("/")
def application():
    return render_template('application.html')

@app.route("/application")
def hr():
    return render_template('application.html')

@app.route('/access')
def access():
    return render_template('access.html')

# API
@app.route('/grant-access', methods=['POST'])
def grant_access():
    chat_id = request.form['chat_id']
    name = request.form['name']
    subdivision = request.form['subdivision']
    JOBTITLE = request.form['JOBTITLE']
    department = request.form['department']
    # Здесь можно выполнить логику выдачи доступа к боту для указанного чата
    db = DB.database.People()
    db.create(chat_id, name, subdivision, JOBTITLE, department)
    db.close()
    return render_template('accessright.html')

<<<<<<< HEAD
@app.route('/difi')
def difi():
    return render_template("experiment.html")
# @app.route('/submit_handler', methods=['POST'])
# def submit_handler():
#     choice = request.form['choice']
#     if choice == 'page1':
#         return render_template('experiment.html')
=======

@app.route('/submit', methods=['POST'])
def submit_handler():
    choice = requests.form['choice']
    if choice == 'page1':
        return redirect('/page1')
>>>>>>> d69551365bd7edc8dd483fba97b460e6c7c2957f


if __name__ == '__main__':
    app.run()