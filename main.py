from flask import Flask
from flask import render_template
import applications
from flask import request
from flask import url_for
import json
from setting import  FIRST_ROW, SECOND_ROW, THIRD_ROW, FOURTH_ROW, LAST_ROW

app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/password_generator')
def generator():
  return render_template("passwordgenerator.html")

@app.route('/generator_form', methods = ["POST","GET"])
def generate():
   if request.method == 'POST' and (request.form['password_length'] != ' ' and request.form['banned_symbols'] != ' '):
    return json.dumps({'passw': applications.generate(int(request.form['password_length']), request.form['banned_symbols'])})

@app.route('/calculator')
def calculator():
      return render_template("calculator.html",  first_row=FIRST_ROW,
                           second_row=SECOND_ROW, third_row=THIRD_ROW, fourth_row=FOURTH_ROW, last_row = LAST_ROW)

app.run(host='0.0.0.0', port=8080, debug=True)