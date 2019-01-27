#!/bin/python3
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tickets')
def generic():
    return render_template('generic.html')


@app.route('/params')
def parameters():
    param = request.args.get('param1', 'parametro')
    return 'hello params is {}'.format(param)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
