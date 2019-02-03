#!/usr/bin/python3.6
from flask import Flask
from flask import render_template
from flask import request
import forms

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    ticketform = forms.TicketForm()
    comment = "macro test"
    return render_template('index.html', comment = comment, form = ticketform)

@app.route('/tickets')
def generic():
    return render_template('ticket.html')


@app.route('/params')
def parameters():
    param = request.args.get('param1', 'parametro')
    return 'hello params is {}'.format(param)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
