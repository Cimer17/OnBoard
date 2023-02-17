from flask import Flask, render_template, jsonify
import DB.database

app = Flask(__name__)
db = DB.database.Database()

@app.route("/")
def application():
    return render_template('application.html')

@app.route("/hr")
def hr():
    return render_template('hr.html')

"""@app.route('/checkpeople/<user>', methods=['GET'])
def get_data(user):
    data = db.all_human(user)
    return data
    result = []
    #for row in data:
       # result.append()
    #return jsonify({'name': row[0], 'subdivision': row[1], 'department': row[2]})"""