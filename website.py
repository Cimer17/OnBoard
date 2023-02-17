from flask import Flask, redirect, render_template, jsonify
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

"""@app.route('/checkpeople/<user>', methods=['GET'])
def get_data(user):
    data = db.all_human(user)
    return data
    result = []
    #for row in data:
       # result.append()
    #return jsonify({'name': row[0], 'subdivision': row[1], 'department': row[2]})"""

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