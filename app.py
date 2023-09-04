from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><h1>Hello, World!<br>i<br>am<br>tired!!!<br><button>moshe</button></h1></p>"

@app.route("/shahar")
def hello_world2():
    return "<p><h1>shahar</h1></p>"

@app.route("/yaakob")
def hello_world3():
    return "<p><h1>yaakob</h1></p>"

@app.route("/ran")
def hello_world4():
    return "<p><h1>ran</h1></p>"

@app.route("/avi")
def hello_world5():
    return "<p><h1>avi</h1></p>"