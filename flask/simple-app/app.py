#!flask/bin/python
from flask import Flask, request, request_started
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')
