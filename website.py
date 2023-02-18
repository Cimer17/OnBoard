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
    return f'Доступ выдан {chat_id}!'



@app.route('/submit', methods=['POST'])
def submit_handler():
    choice = requests.form['choice']
    if choice == 'page1':
        return redirect('/page1')

@app.route('/page1')
def page1():
    return """
    <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <div class="box1">
            <p>Раздел обработки меня</p>
        </div>

    </head>
    </html>
  """

if __name__ == '__main__':
    target=app.run()