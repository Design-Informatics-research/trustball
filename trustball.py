from flask import Flask, redirect, render_template, send_from_directory, request, jsonify, json
import servo as servo
import btn as btn
import reset as reset
import json
import time
from thread2 import StopThread, Thread2

app = Flask(__name__)
blink_thread = Thread2(target=btn.blink)
buttonAll_thread = Thread2(target=btn.buttonAll)
buttonTwo_thread = Thread2(target=btn.buttonTwo)

def stop_threads():
    if blink_thread and blink_thread.isAlive():
        blink_thread.stop()
    if buttonAll_thread and buttonAll_thread.isAlive():
        buttonAll_thread.stop()
    if buttonTwo_thread and buttonTwo_thread.isAlive():
        buttonTwo_thread.stop()

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
  stop_threads()
  time.sleep(1)
  blink_thread = Thread2(target=btn.blink)
  blink_thread.start()
  return "ok"

@app.route("/btn_Qs")
def btn_Qs():
  stop_threads()
  buttonAll_thread = Thread2(target=btn.buttonAll)
  buttonAll_thread.start()
  return "ok"

@app.route("/btn_summary")
def btn_summary():
  stop_threads()
  buttonTwo_thread = Thread2(target=btn.buttonTwo)
  buttonTwo_thread.start()
  return "ok"

@app.route("/motor_begin")
def motor_begin():
  servo.open_slower()
  return "ok"

@app.route("/motors_page1")
def motors_page1():
  servo.page1()
  return "ok"

@app.route("/motors_page2")
def motors_page2():
  servo.page2()
  return "ok"

@app.route("/motors_page3")
def motors_page3():
  servo.page3()
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
  reset.open_all()
  reset.close_all()
  return "ok"