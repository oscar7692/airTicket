#!/bin/python3
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    param = request.args.get('param1', 'parametro')
    return 'hello params is {}'.format(param)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
