import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/johansen')
def hello():
    return 'Well! Hello there Mr. Johansen! Nice to see you again!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
