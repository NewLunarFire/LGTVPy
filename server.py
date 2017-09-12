from lg import LGTV
from flask import Flask
app = Flask(__name__)

lg = LGTV(port='COM3')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/power", methods=['GET'])
def getPower():
    if lg.powermode().value == 0:
        return "Powered off"
    elif lg.powermode().value == 1:
        return "Powered on"
    else:
        return "Unknown"

@app.route("/on")
def powerOn():
    lg.poweron()
    return "Done"

@app.route("/off")
def powerOff():
    lg.poweroff()
    return "Done"