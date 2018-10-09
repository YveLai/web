from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
  return 'Hello Napier'

@app.route("/no")
def lonely():
   return 'no lover'
