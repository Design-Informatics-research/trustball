from flask import Flask, redirect, render_template, send_from_directory, request, jsonify, json
import json
import time

app = Flask(__name__)


@app.route('/assets/<path>')
def send_asset(path):
  return send_from_directory('assets', path)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/index_reset")
def index_reset():
  return render_template('reset.html')

@app.route("/terms")
def terms():
  return render_template('terms.html')

@app.route("/p1")
def p1():
  return render_template('p1.html')

@app.route("/p2")
def p2():
  return render_template('p2.html')

@app.route("/p3")
def p3():
  return render_template('p3.html')

@app.route("/btn_index")
def btn_index():
  time.sleep(1)
  return "ok"

@app.route("/btn_Qs")
def btn_Qs():
  time.sleep(1)
  return "ok"

@app.route("/btn_summary")
def btn_summary():
  time.sleep(1)
  return "ok"

@app.route("/motor_begin")
def motor_begin():
  time.sleep(1)
  return "ok"

@app.route("/motors_page1")
def motors_page1():
  time.sleep(1)
  return "ok"

@app.route("/motors_page2")
def motors_page2():
  time.sleep(1)
  return "ok"

@app.route("/motors_page3")
def motors_page3():
  time.sleep(1)
  return "ok"

@app.route("/summary", methods = ['GET','POST'])
def summary():
  if request.method == 'POST':
    d = request.get_json()
    with open('data.json', 'a') as f:
      json.dump(d,f)
      f.write('\n')
    return jsonify({"Message": "Sucess"}),200
  return render_template('summary.html')

@app.route("/cleanballs")
def cleanballs():
  time.sleep(1)
  return "ok"
